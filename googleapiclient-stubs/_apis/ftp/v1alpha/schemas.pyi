import typing

import typing_extensions

_list = list

@typing.type_check_only
class AllowedConsumer(typing_extensions.TypedDict, total=False):
    connectionLimit: str
    project: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeniedConsumer(typing_extensions.TypedDict, total=False):
    project: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExternalServerConfig(typing_extensions.TypedDict, total=False):
    allowedCidrBlocks: _list[str]
    ipAddress: str

@typing.type_check_only
class InternalServerConfig(typing_extensions.TypedDict, total=False):
    consumerAcceptList: _list[AllowedConsumer]
    consumerRejectList: _list[DeniedConsumer]
    pscEndpoints: _list[PscEndpoint]
    serviceAttachment: str

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
class ListServersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    servers: _list[Server]
    unreachable: _list[str]

@typing.type_check_only
class ListUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    users: _list[User]

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
class PscEndpoint(typing_extensions.TypedDict, total=False):
    endpoint: str
    network: str
    status: str

@typing.type_check_only
class Server(typing_extensions.TypedDict, total=False):
    accessType: typing_extensions.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "EXTERNAL", "INTERNAL"
    ]
    createTime: str
    displayName: str
    externalConfig: ExternalServerConfig
    googleManagedServerCredential: ServerCredential
    internalConfig: InternalServerConfig
    labels: dict[str, typing.Any]
    name: str
    serviceAgent: str
    state: typing_extensions.Literal[
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
class ServerCredential(typing_extensions.TypedDict, total=False):
    asymmetricAlgorithm: str
    fingerprint: str

@typing.type_check_only
class StartServerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopServerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StorageDirectoryMapping(typing_extensions.TypedDict, total=False):
    bucket: str
    bucketPrefix: str
    directory: str
    permission: typing_extensions.Literal[
        "PERMISSION_UNSPECIFIED", "READ_ONLY", "READ_WRITE"
    ]

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    createTime: str
    customerServiceAccount: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "ERROR", "UPDATING", "DELETING"
    ]
    storageDirectoryMappings: _list[StorageDirectoryMapping]
    updateTime: str
    userCredentials: _list[UserCredential]
    username: str

@typing.type_check_only
class UserCredential(typing_extensions.TypedDict, total=False):
    credentialName: str
    credentialType: typing_extensions.Literal["TYPE_UNSPECIFIED", "PUBLIC_KEY"]
    sshPublicKeyBody: str
