import typing

import typing_extensions

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class FailoverInstanceRequest(typing_extensions.TypedDict, total=False):
    dataProtectionMode: typing_extensions.Literal[
        "DATA_PROTECTION_MODE_UNSPECIFIED", "LIMITED_DATA_LOSS", "FORCE_DATA_LOSS"
    ]

class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudCommonOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    statusDetail: str
    endTime: str
    target: str
    createTime: str
    verb: str
    cancelRequested: bool

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class ExportInstanceRequest(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

class ImportInstanceRequest(typing_extensions.TypedDict, total=False):
    inputConfig: InputConfig

class InstanceAuthString(typing_extensions.TypedDict, total=False):
    authString: str

class GoogleCloudRedisV1beta1ZoneMetadata(typing_extensions.TypedDict, total=False): ...
class Empty(typing_extensions.TypedDict, total=False): ...

class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    metadata: typing.Dict[str, typing.Any]
    locationId: str
    name: str
    labels: typing.Dict[str, typing.Any]

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    error: Status
    done: bool
    response: typing.Dict[str, typing.Any]

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    unreachable: typing.List[str]
    nextPageToken: str

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

class Instance(typing_extensions.TypedDict, total=False):
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
    name: str
    port: int
    authorizedNetwork: str
    locationId: str
    displayName: str
    connectMode: typing_extensions.Literal[
        "CONNECT_MODE_UNSPECIFIED", "DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"
    ]
    statusMessage: str
    memorySizeGb: int
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "BASIC", "STANDARD_HA"]
    alternativeLocationId: str
    redisConfigs: typing.Dict[str, typing.Any]
    redisVersion: str
    host: str
    labels: typing.Dict[str, typing.Any]
    createTime: str
    authEnabled: bool
    persistenceIamIdentity: str
    currentLocationId: str
    reservedIpRange: str

class GoogleCloudRedisV1beta1LocationMetadata(typing_extensions.TypedDict, total=False):
    availableZones: typing.Dict[str, typing.Any]

class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False):
    redisVersion: str

class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
