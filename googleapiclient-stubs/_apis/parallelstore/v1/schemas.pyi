import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DestinationGcsBucket(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class DestinationParallelstore(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class ExportDataRequest(typing_extensions.TypedDict, total=False):
    destinationGcsBucket: DestinationGcsBucket
    metadataOptions: TransferMetadataOptions
    requestId: str
    serviceAccount: str
    sourceParallelstore: SourceParallelstore

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportDataRequest(typing_extensions.TypedDict, total=False):
    destinationParallelstore: DestinationParallelstore
    metadataOptions: TransferMetadataOptions
    requestId: str
    serviceAccount: str
    sourceGcsBucket: SourceGcsBucket

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    accessPoints: _list[str]
    capacityGib: str
    createTime: str
    daosVersion: str
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
    unreachable: _list[str]

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
class ReconciliationOperationMetadata(typing_extensions.TypedDict, total=False):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

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

@typing.type_check_only
class TransferMetadataOptions(typing_extensions.TypedDict, total=False):
    gid: typing_extensions.Literal["GID_UNSPECIFIED", "GID_SKIP", "GID_NUMBER_PRESERVE"]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "MODE_SKIP", "MODE_PRESERVE"]
    uid: typing_extensions.Literal["UID_UNSPECIFIED", "UID_SKIP", "UID_NUMBER_PRESERVE"]
