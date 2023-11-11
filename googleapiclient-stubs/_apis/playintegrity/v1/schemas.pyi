import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccountActivity(typing_extensions.TypedDict, total=False):
    activityLevel: typing_extensions.Literal[
        "ACTIVITY_LEVEL_UNSPECIFIED",
        "UNEVALUATED",
        "UNUSUAL",
        "UNKNOWN",
        "TYPICAL_BASIC",
        "TYPICAL_STRONG",
    ]

@typing.type_check_only
class AccountDetails(typing_extensions.TypedDict, total=False):
    accountActivity: AccountActivity
    appLicensingVerdict: typing_extensions.Literal[
        "UNKNOWN", "LICENSED", "UNLICENSED", "UNEVALUATED"
    ]

@typing.type_check_only
class AppIntegrity(typing_extensions.TypedDict, total=False):
    appRecognitionVerdict: typing_extensions.Literal[
        "UNKNOWN", "PLAY_RECOGNIZED", "UNRECOGNIZED_VERSION", "UNEVALUATED"
    ]
    certificateSha256Digest: _list[str]
    packageName: str
    versionCode: str

@typing.type_check_only
class DecodeIntegrityTokenRequest(typing_extensions.TypedDict, total=False):
    integrityToken: str

@typing.type_check_only
class DecodeIntegrityTokenResponse(typing_extensions.TypedDict, total=False):
    tokenPayloadExternal: TokenPayloadExternal

@typing.type_check_only
class DeviceIntegrity(typing_extensions.TypedDict, total=False):
    deviceRecognitionVerdict: _list[str]

@typing.type_check_only
class EnvironmentDetails(typing_extensions.TypedDict, total=False):
    playProtectVerdict: typing_extensions.Literal[
        "PLAY_PROTECT_VERDICT_UNSPECIFIED",
        "UNEVALUATED",
        "NO_ISSUES",
        "NO_DATA",
        "MEDIUM_RISK",
        "HIGH_RISK",
        "POSSIBLE_RISK",
    ]

@typing.type_check_only
class GuidanceDetails(typing_extensions.TypedDict, total=False):
    userRemediationDetails: _list[UserRemediationDetails]

@typing.type_check_only
class RequestDetails(typing_extensions.TypedDict, total=False):
    nonce: str
    requestHash: str
    requestPackageName: str
    timestampMillis: str

@typing.type_check_only
class TestingDetails(typing_extensions.TypedDict, total=False):
    isTestingResponse: bool

@typing.type_check_only
class TokenPayloadExternal(typing_extensions.TypedDict, total=False):
    accountDetails: AccountDetails
    appIntegrity: AppIntegrity
    deviceIntegrity: DeviceIntegrity
    environmentDetails: EnvironmentDetails
    guidanceDetails: GuidanceDetails
    requestDetails: RequestDetails
    testingDetails: TestingDetails

@typing.type_check_only
class UserRemediationDetails(typing_extensions.TypedDict, total=False):
    remediation: typing_extensions.Literal[
        "UNKNOWN_USER_REMEDIATION",
        "RESTORE_FACTORY_ROM",
        "LOCK_BOOTLOADER",
        "GET_UNMODIFIED_APP",
        "SIGN_INTO_GOOGLE_ACCOUNT",
        "INSTALL_APP_FROM_PLAY",
    ]
