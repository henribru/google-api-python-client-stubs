import typing

import typing_extensions

class PosixAccount(typing_extensions.TypedDict, total=False):
    username: str
    gecos: str
    shell: str
    primary: bool
    systemId: str
    name: str
    operatingSystemType: typing_extensions.Literal[
        "OPERATING_SYSTEM_TYPE_UNSPECIFIED", "LINUX", "WINDOWS"
    ]
    uid: str
    homeDirectory: str
    accountId: str
    gid: str

class LoginProfile(typing_extensions.TypedDict, total=False):
    name: str
    sshPublicKeys: typing.Dict[str, typing.Any]
    posixAccounts: typing.List[PosixAccount]

class ImportSshPublicKeyResponse(typing_extensions.TypedDict, total=False):
    details: str
    loginProfile: LoginProfile

class SshPublicKey(typing_extensions.TypedDict, total=False):
    expirationTimeUsec: str
    fingerprint: str
    key: str
    name: str

class Empty(typing_extensions.TypedDict, total=False): ...
