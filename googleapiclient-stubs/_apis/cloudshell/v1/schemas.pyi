import typing

import typing_extensions
@typing.type_check_only
class AddPublicKeyMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddPublicKeyRequest(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class AddPublicKeyResponse(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class AuthorizeEnvironmentMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AuthorizeEnvironmentRequest(typing_extensions.TypedDict, total=False):
    accessToken: str
    expireTime: str
    idToken: str

@typing.type_check_only
class AuthorizeEnvironmentResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateEnvironmentMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteEnvironmentMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    dockerImage: str
    id: str
    name: str
    publicKeys: typing.List[str]
    sshHost: str
    sshPort: int
    sshUsername: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "SUSPENDED", "PENDING", "RUNNING", "DELETING"
    ]
    webHost: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class RemovePublicKeyMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemovePublicKeyRequest(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class RemovePublicKeyResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StartEnvironmentMetadata(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "UNARCHIVING_DISK",
        "AWAITING_COMPUTE_RESOURCES",
        "FINISHED",
    ]

@typing.type_check_only
class StartEnvironmentRequest(typing_extensions.TypedDict, total=False):
    accessToken: str
    publicKeys: typing.List[str]

@typing.type_check_only
class StartEnvironmentResponse(typing_extensions.TypedDict, total=False):
    environment: Environment

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
