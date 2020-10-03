import typing

import typing_extensions

class FailoverInstanceRequest(typing_extensions.TypedDict, total=False):
    dataProtectionMode: typing_extensions.Literal[
        "DATA_PROTECTION_MODE_UNSPECIFIED", "LIMITED_DATA_LOSS", "FORCE_DATA_LOSS"
    ]

class GoogleCloudRedisV1OperationMetadata(typing_extensions.TypedDict, total=False):
    cancelRequested: bool
    endTime: str
    createTime: str
    target: str
    verb: str
    apiVersion: str
    statusDetail: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class GoogleCloudRedisV1LocationMetadata(typing_extensions.TypedDict, total=False):
    availableZones: typing.Dict[str, typing.Any]

class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

class Empty(typing_extensions.TypedDict, total=False): ...

class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False):
    redisVersion: str

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    instances: typing.List[Instance]
    unreachable: typing.List[str]

class Location(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    displayName: str
    locationId: str
    name: str
    labels: typing.Dict[str, typing.Any]

class Instance(typing_extensions.TypedDict, total=False):
    persistenceIamIdentity: str
    locationId: str
    memorySizeGb: int
    alternativeLocationId: str
    statusMessage: str
    host: str
    createTime: str
    authorizedNetwork: str
    connectMode: typing_extensions.Literal[
        "CONNECT_MODE_UNSPECIFIED", "DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"
    ]
    displayName: str
    redisVersion: str
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "BASIC", "STANDARD_HA"]
    redisConfigs: typing.Dict[str, typing.Any]
    currentLocationId: str
    port: int
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "REPAIRING",
        "MAINTENANCE",
        "IMPORTING",
        "FAILING_OVER",
    ]
    reservedIpRange: str
    labels: typing.Dict[str, typing.Any]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class GoogleCloudRedisV1ZoneMetadata(typing_extensions.TypedDict, total=False): ...

class ImportInstanceRequest(typing_extensions.TypedDict, total=False):
    inputConfig: InputConfig

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class ExportInstanceRequest(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status
