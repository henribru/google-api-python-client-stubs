import typing

_list = list

@typing.type_check_only
class AllowedConsumer(typing.TypedDict, total=False):
    connectionLimit: str
    project: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeniedConsumer(typing.TypedDict, total=False):
    project: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExternalServerConfig(typing.TypedDict, total=False):
    allowedCidrBlocks: _list[str]
    ipAddress: str

@typing.type_check_only
class InternalServerConfig(typing.TypedDict, total=False):
    consumerAcceptList: _list[AllowedConsumer]
    consumerRejectList: _list[DeniedConsumer]
    pscEndpoints: _list[PscEndpoint]
    serviceAttachment: str

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
class ListServersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    servers: _list[Server]
    unreachable: _list[str]

@typing.type_check_only
class ListUsersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    users: _list[User]

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
class PscEndpoint(typing.TypedDict, total=False):
    endpoint: str
    network: str
    status: str

@typing.type_check_only
class Server(typing.TypedDict, total=False):
    accessType: typing.Literal["ACCESS_TYPE_UNSPECIFIED", "EXTERNAL", "INTERNAL"]
    createTime: str
    displayName: str
    externalConfig: ExternalServerConfig
    googleManagedServerCredential: ServerCredential
    internalConfig: InternalServerConfig
    labels: dict[str, typing.Any]
    name: str
    serviceAgent: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "STARTING",
        "ACTIVE",
        "STOPPING",
        "STOPPED",
        "DELETING",
        "ERROR",
        "UPDATING",
    ]
    updateTime: str

@typing.type_check_only
class ServerCredential(typing.TypedDict, total=False):
    asymmetricAlgorithm: str
    fingerprint: str

@typing.type_check_only
class StartServerRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopServerRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StorageDirectoryMapping(typing.TypedDict, total=False):
    bucket: str
    bucketPrefix: str
    directory: str
    permission: typing.Literal["PERMISSION_UNSPECIFIED", "READ_ONLY", "READ_WRITE"]

@typing.type_check_only
class User(typing.TypedDict, total=False):
    createTime: str
    customerServiceAccount: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "ERROR", "UPDATING", "DELETING"
    ]
    storageDirectoryMappings: _list[StorageDirectoryMapping]
    updateTime: str
    userCredentials: _list[UserCredential]
    username: str

@typing.type_check_only
class UserCredential(typing.TypedDict, total=False):
    credentialName: str
    credentialType: typing.Literal["TYPE_UNSPECIFIED", "PUBLIC_KEY"]
    sshPublicKeyBody: str
