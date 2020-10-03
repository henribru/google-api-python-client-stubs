import typing

import typing_extensions

class SshPublicKey(typing_extensions.TypedDict, total=False):
    fingerprint: str
    expirationTimeUsec: str
    name: str
    key: str

class ImportSshPublicKeyResponse(typing_extensions.TypedDict, total=False):
    details: str
    loginProfile: LoginProfile

class LoginProfile(typing_extensions.TypedDict, total=False):
    posixAccounts: typing.List[PosixAccount]
    sshPublicKeys: typing.Dict[str, typing.Any]
    name: str

class Empty(typing_extensions.TypedDict, total=False): ...

class PosixAccount(typing_extensions.TypedDict, total=False):
    gecos: str
    operatingSystemType: typing_extensions.Literal[
        "OPERATING_SYSTEM_TYPE_UNSPECIFIED", "LINUX", "WINDOWS"
    ]
    uid: str
    shell: str
    accountId: str
    username: str
    gid: str
    systemId: str
    primary: bool
    homeDirectory: str
    name: str
