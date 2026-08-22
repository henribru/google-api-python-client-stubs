import typing

_list = list

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DestinationGcsBucket(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class DestinationParallelstore(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class ExportDataRequest(typing.TypedDict, total=False):
    destinationGcsBucket: DestinationGcsBucket
    metadataOptions: TransferMetadataOptions
    requestId: str
    serviceAccount: str
    sourceParallelstore: SourceParallelstore

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ImportDataRequest(typing.TypedDict, total=False):
    destinationParallelstore: DestinationParallelstore
    metadataOptions: TransferMetadataOptions
    requestId: str
    serviceAccount: str
    sourceGcsBucket: SourceGcsBucket

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    accessPoints: _list[str]
    capacityGib: str
    createTime: str
    daosVersion: str
    deploymentType: typing.Literal[
        "DEPLOYMENT_TYPE_UNSPECIFIED", "SCRATCH", "PERSISTENT"
    ]
    description: str
    directoryStripeLevel: typing.Literal[
        "DIRECTORY_STRIPE_LEVEL_UNSPECIFIED",
        "DIRECTORY_STRIPE_LEVEL_MIN",
        "DIRECTORY_STRIPE_LEVEL_BALANCED",
        "DIRECTORY_STRIPE_LEVEL_MAX",
    ]
    effectiveReservedIpRange: str
    fileStripeLevel: typing.Literal[
        "FILE_STRIPE_LEVEL_UNSPECIFIED",
        "FILE_STRIPE_LEVEL_MIN",
        "FILE_STRIPE_LEVEL_BALANCED",
        "FILE_STRIPE_LEVEL_MAX",
    ]
    labels: dict[str, typing.Any]
    name: str
    network: str
    reservedIpRange: str
    state: typing.Literal[
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
class ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[Instance]
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
class ReconciliationOperationMetadata(typing.TypedDict, total=False):
    deleteResource: bool
    exclusiveAction: typing.Literal["UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"]

@typing.type_check_only
class SourceGcsBucket(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class SourceParallelstore(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TransferMetadataOptions(typing.TypedDict, total=False):
    gid: typing.Literal["GID_UNSPECIFIED", "GID_SKIP", "GID_NUMBER_PRESERVE"]
    mode: typing.Literal["MODE_UNSPECIFIED", "MODE_SKIP", "MODE_PRESERVE"]
    uid: typing.Literal["UID_UNSPECIFIED", "UID_SKIP", "UID_NUMBER_PRESERVE"]
