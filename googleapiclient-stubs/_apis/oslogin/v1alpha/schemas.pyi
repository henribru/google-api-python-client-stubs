import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyRequest(
    typing.TypedDict, total=False
):
    appEngineInstance: str
    cloudRunResource: str
    computeInstance: str
    serviceAccount: str
    sshPublicKey: str

@typing.type_check_only
class GoogleCloudOsloginControlplaneRegionalV1alphaSignSshPublicKeyResponse(
    typing.TypedDict, total=False
):
    signedSshPublicKey: str

@typing.type_check_only
class ImportSshPublicKeyResponse(typing.TypedDict, total=False):
    details: str
    loginProfile: LoginProfile

@typing.type_check_only
class LoginProfile(typing.TypedDict, total=False):
    name: str
    posixAccounts: _list[PosixAccount]
    securityKeys: _list[SecurityKey]
    sshPublicKeys: dict[str, typing.Any]

@typing.type_check_only
class PosixAccount(typing.TypedDict, total=False):
    accountId: str
    gecos: str
    gid: str
    homeDirectory: str
    name: str
    operatingSystemType: typing.Literal[
        "OPERATING_SYSTEM_TYPE_UNSPECIFIED", "LINUX", "WINDOWS"
    ]
    primary: bool
    shell: str
    systemId: str
    uid: str
    username: str

@typing.type_check_only
class ProvisionPosixAccountRequest(typing.TypedDict, total=False):
    regions: _list[str]

@typing.type_check_only
class SecurityKey(typing.TypedDict, total=False):
    deviceNickname: str
    privateKey: str
    publicKey: str
    universalTwoFactor: UniversalTwoFactor
    webAuthn: WebAuthn

@typing.type_check_only
class SignSshPublicKeyRequest(typing.TypedDict, total=False):
    sshPublicKey: str

@typing.type_check_only
class SignSshPublicKeyResponse(typing.TypedDict, total=False):
    signedSshPublicKey: str

@typing.type_check_only
class SshPublicKey(typing.TypedDict, total=False):
    expirationTimeUsec: str
    fingerprint: str
    key: str
    name: str

@typing.type_check_only
class UniversalTwoFactor(typing.TypedDict, total=False):
    appId: str

@typing.type_check_only
class WebAuthn(typing.TypedDict, total=False):
    rpId: str
