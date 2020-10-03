import typing

import typing_extensions

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class StartEnvironmentRequest(typing_extensions.TypedDict, total=False):
    accessToken: str
    publicKeys: typing.List[PublicKey]

class Environment(typing_extensions.TypedDict, total=False):
    webPorts: typing.List[int]
    dockerImage: str
    sshPort: int
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "DISABLED", "STARTING", "RUNNING", "DELETING"
    ]
    webHost: str
    sshHost: str
    publicKeys: typing.List[PublicKey]
    id: str
    vmSizeExpireTime: str
    sshUsername: str
    size: typing_extensions.Literal["VM_SIZE_UNSPECIFIED", "DEFAULT", "BOOSTED"]

class StartEnvironmentResponse(typing_extensions.TypedDict, total=False):
    environment: Environment

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    done: bool
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str

class Empty(typing_extensions.TypedDict, total=False): ...

class AuthorizeEnvironmentRequest(typing_extensions.TypedDict, total=False):
    expireTime: str
    accessToken: str
    idToken: str

class StartEnvironmentMetadata(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "UNARCHIVING_DISK",
        "AWAITING_VM",
        "AWAITING_COMPUTE_RESOURCES",
        "FINISHED",
    ]

class PublicKey(typing_extensions.TypedDict, total=False):
    name: str
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED",
        "SSH_DSS",
        "SSH_RSA",
        "ECDSA_SHA2_NISTP256",
        "ECDSA_SHA2_NISTP384",
        "ECDSA_SHA2_NISTP521",
    ]
    key: str

class CreatePublicKeyRequest(typing_extensions.TypedDict, total=False):
    key: PublicKey
