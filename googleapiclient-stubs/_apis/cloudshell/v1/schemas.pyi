import typing

_list = list

@typing.type_check_only
class AddPublicKeyMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class AddPublicKeyRequest(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class AddPublicKeyResponse(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class AuthorizeEnvironmentMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class AuthorizeEnvironmentRequest(typing.TypedDict, total=False):
    accessToken: str
    expireTime: str
    idToken: str

@typing.type_check_only
class AuthorizeEnvironmentResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateEnvironmentMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteEnvironmentMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    dockerImage: str
    id: str
    name: str
    publicKeys: _list[str]
    sshHost: str
    sshPort: int
    sshUsername: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SUSPENDED", "PENDING", "RUNNING", "DELETING"
    ]
    webHost: str

@typing.type_check_only
class GenerateAccessTokenResponse(typing.TypedDict, total=False):
    accessToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class RemovePublicKeyMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemovePublicKeyRequest(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class RemovePublicKeyResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class StartEnvironmentMetadata(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "UNARCHIVING_DISK",
        "AWAITING_COMPUTE_RESOURCES",
        "FINISHED",
    ]

@typing.type_check_only
class StartEnvironmentRequest(typing.TypedDict, total=False):
    accessToken: str
    publicKeys: _list[str]

@typing.type_check_only
class StartEnvironmentResponse(typing.TypedDict, total=False):
    environment: Environment

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
