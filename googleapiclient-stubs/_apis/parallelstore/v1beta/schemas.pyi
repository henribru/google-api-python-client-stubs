import typing

import typing_extensions

_list = list

@typing.type_check_only
class DestinationGcsBucket(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class DestinationParallelstore(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class ExportDataRequest(typing_extensions.TypedDict, total=False):
    destinationGcsBucket: DestinationGcsBucket
    requestId: str
    serviceAccount: str
    sourceParallelstore: SourceParallelstore

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportDataRequest(typing_extensions.TypedDict, total=False):
    destinationParallelstore: DestinationParallelstore
    requestId: str
    serviceAccount: str
    sourceGcsBucket: SourceGcsBucket

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    accessPoints: _list[str]
    capacityGib: str
    createTime: str
    deploymentType: typing_extensions.Literal[
        "DEPLOYMENT_TYPE_UNSPECIFIED", "SCRATCH", "PERSISTENT"
    ]
    description: str
    directoryStripeLevel: typing_extensions.Literal[
        "DIRECTORY_STRIPE_LEVEL_UNSPECIFIED",
        "DIRECTORY_STRIPE_LEVEL_MIN",
        "DIRECTORY_STRIPE_LEVEL_BALANCED",
        "DIRECTORY_STRIPE_LEVEL_MAX",
    ]
    effectiveReservedIpRange: str
    fileStripeLevel: typing_extensions.Literal[
        "FILE_STRIPE_LEVEL_UNSPECIFIED",
        "FILE_STRIPE_LEVEL_MIN",
        "FILE_STRIPE_LEVEL_BALANCED",
        "FILE_STRIPE_LEVEL_MAX",
    ]
    labels: dict[str, typing.Any]
    name: str
    network: str
    reservedIpRange: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
        "UPGRADING",
        "REPAIRING",
    ]
    updateTime: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
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
class SourceGcsBucket(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class SourceParallelstore(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
