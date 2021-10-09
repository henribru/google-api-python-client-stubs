import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportSshPublicKeyResponse(typing_extensions.TypedDict, total=False):
    details: str
    loginProfile: LoginProfile

@typing.type_check_only
class LoginProfile(typing_extensions.TypedDict, total=False):
    name: str
    posixAccounts: _list[PosixAccount]
    securityKeys: _list[SecurityKey]
    sshPublicKeys: dict[str, typing.Any]

@typing.type_check_only
class PosixAccount(typing_extensions.TypedDict, total=False):
    accountId: str
    gecos: str
    gid: str
    homeDirectory: str
    name: str
    operatingSystemType: typing_extensions.Literal[
        "OPERATING_SYSTEM_TYPE_UNSPECIFIED", "LINUX", "WINDOWS"
    ]
    primary: bool
    shell: str
    systemId: str
    uid: str
    username: str

@typing.type_check_only
class SecurityKey(typing_extensions.TypedDict, total=False):
    privateKey: str
    publicKey: str
    universalTwoFactor: UniversalTwoFactor
    webAuthn: WebAuthn

@typing.type_check_only
class SshPublicKey(typing_extensions.TypedDict, total=False):
    expirationTimeUsec: str
    fingerprint: str
    key: str
    name: str

@typing.type_check_only
class UniversalTwoFactor(typing_extensions.TypedDict, total=False):
    appId: str

@typing.type_check_only
class WebAuthn(typing_extensions.TypedDict, total=False):
    rpId: str
