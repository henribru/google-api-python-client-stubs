import typing

import typing_extensions
@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportInstanceRequest(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

@typing.type_check_only
class FailoverInstanceRequest(typing_extensions.TypedDict, total=False):
    dataProtectionMode: typing_extensions.Literal[
        "DATA_PROTECTION_MODE_UNSPECIFIED", "LIMITED_DATA_LOSS", "FORCE_DATA_LOSS"
    ]

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudRedisV1beta1LocationMetadata(typing_extensions.TypedDict, total=False):
    availableZones: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRedisV1beta1ZoneMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportInstanceRequest(typing_extensions.TypedDict, total=False):
    inputConfig: InputConfig

@typing.type_check_only
class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    alternativeLocationId: str
    authEnabled: bool
    authorizedNetwork: str
    connectMode: typing_extensions.Literal[
        "CONNECT_MODE_UNSPECIFIED", "DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"
    ]
    createTime: str
    currentLocationId: str
    displayName: str
    host: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    memorySizeGb: int
    name: str
    persistenceIamIdentity: str
    port: int
    redisConfigs: typing.Dict[str, typing.Any]
    redisVersion: str
    reservedIpRange: str
    serverCaCerts: typing.List[TlsCertificate]
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
    statusMessage: str
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "BASIC", "STANDARD_HA"]
    transitEncryptionMode: typing_extensions.Literal[
        "TRANSIT_ENCRYPTION_MODE_UNSPECIFIED", "SERVER_AUTHENTICATION", "DISABLED"
    ]

@typing.type_check_only
class InstanceAuthString(typing_extensions.TypedDict, total=False):
    authString: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TlsCertificate(typing_extensions.TypedDict, total=False):
    cert: str
    createTime: str
    expireTime: str
    serialNumber: str
    sha1Fingerprint: str

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False):
    redisVersion: str
