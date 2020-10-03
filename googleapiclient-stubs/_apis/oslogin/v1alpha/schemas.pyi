import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...

class ImportSshPublicKeyResponse(typing_extensions.TypedDict, total=False):
    loginProfile: LoginProfile
    details: str

class SshPublicKey(typing_extensions.TypedDict, total=False):
    name: str
    key: str
    fingerprint: str
    expirationTimeUsec: str

class PosixAccount(typing_extensions.TypedDict, total=False):
    shell: str
    accountId: str
    name: str
    gid: str
    uid: str
    systemId: str
    primary: bool
    operatingSystemType: typing_extensions.Literal[
        "OPERATING_SYSTEM_TYPE_UNSPECIFIED", "LINUX", "WINDOWS"
    ]
    username: str
    homeDirectory: str
    gecos: str

class LoginProfile(typing_extensions.TypedDict, total=False):
    name: str
    posixAccounts: typing.List[PosixAccount]
    sshPublicKeys: typing.Dict[str, typing.Any]
