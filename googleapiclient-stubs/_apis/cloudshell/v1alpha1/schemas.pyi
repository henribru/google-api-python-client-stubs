import typing

_list = list

@typing.type_check_only
class AuthorizeEnvironmentRequest(typing.TypedDict, total=False):
    accessToken: str
    expireTime: str
    idToken: str

@typing.type_check_only
class CreatePublicKeyRequest(typing.TypedDict, total=False):
    key: PublicKey

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    dockerImage: str
    id: str
    name: str
    publicKeys: _list[PublicKey]
    size: typing.Literal["VM_SIZE_UNSPECIFIED", "DEFAULT", "BOOSTED"]
    sshHost: str
    sshPort: int
    sshUsername: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DISABLED", "STARTING", "RUNNING", "DELETING"
    ]
    vmSizeExpireTime: str
    webHost: str
    webPorts: _list[int]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PublicKey(typing.TypedDict, total=False):
    format: typing.Literal[
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
class StartEnvironmentMetadata(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "UNARCHIVING_DISK",
        "AWAITING_VM",
        "AWAITING_COMPUTE_RESOURCES",
        "FINISHED",
    ]

@typing.type_check_only
class StartEnvironmentRequest(typing.TypedDict, total=False):
    accessToken: str
    publicKeys: _list[PublicKey]

@typing.type_check_only
class StartEnvironmentResponse(typing.TypedDict, total=False):
    environment: Environment

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
