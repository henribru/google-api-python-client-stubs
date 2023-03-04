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
    requestDetails: RequestDetails
    testingDetails: TestingDetails
