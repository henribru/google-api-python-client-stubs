import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuthorizeEnvironmentRequest(typing_extensions.TypedDict, total=False):
    accessToken: str
    expireTime: str
    idToken: str

@typing.type_check_only
class CreatePublicKeyRequest(typing_extensions.TypedDict, total=False):
    key: PublicKey

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    dockerImage: str
    id: str
    name: str
    publicKeys: _list[PublicKey]
    size: typing_extensions.Literal["VM_SIZE_UNSPECIFIED", "DEFAULT", "BOOSTED"]
    sshHost: str
    sshPort: int
    sshUsername: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "DISABLED", "STARTING", "RUNNING", "DELETING"
    ]
    vmSizeExpireTime: str
    webHost: str
    webPorts: _list[int]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PublicKey(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED",
        "SSH_DSS",
        "SSH_RSA",
        "ECDSA_SHA2_NISTP256",
        "ECDSA_SHA2_NISTP384",
        "ECDSA_SHA2_NISTP521",
    ]
    key: str
    name: str

@typing.type_check_only
class StartEnvironmentMetadata(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "UNARCHIVING_DISK",
        "AWAITING_VM",
        "AWAITING_COMPUTE_RESOURCES",
        "FINISHED",
    ]

@typing.type_check_only
class StartEnvironmentRequest(typing_extensions.TypedDict, total=False):
    accessToken: str
    publicKeys: _list[PublicKey]

@typing.type_check_only
class StartEnvironmentResponse(typing_extensions.TypedDict, total=False):
    environment: Environment

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
