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
class AppAccessRiskVerdict(typing_extensions.TypedDict, total=False):
    otherApps: typing_extensions.Literal[
        "UNKNOWN",
        "UNEVALUATED",
        "NOT_INSTALLED",
        "INSTALLED",
        "CAPTURING",
        "CONTROLLING",
    ]
    playOrSystemApps: typing_extensions.Literal[
        "UNKNOWN",
        "UNEVALUATED",
        "NOT_INSTALLED",
        "INSTALLED",
        "CAPTURING",
        "CONTROLLING",
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
    deviceRecognitionVerdict: _list[
        typing_extensions.Literal[
            "UNKNOWN",
            "MEETS_BASIC_INTEGRITY",
            "MEETS_DEVICE_INTEGRITY",
            "MEETS_STRONG_INTEGRITY",
            "MEETS_VIRTUAL_INTEGRITY",
        ]
    ]
    recentDeviceActivity: RecentDeviceActivity

@typing.type_check_only
class EnvironmentDetails(typing_extensions.TypedDict, total=False):
    appAccessRiskVerdict: AppAccessRiskVerdict
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
class RecentDeviceActivity(typing_extensions.TypedDict, total=False):
    deviceActivityLevel: typing_extensions.Literal[
        "DEVICE_ACTIVITY_LEVEL_UNSPECIFIED",
        "UNEVALUATED",
        "LEVEL_1",
        "LEVEL_2",
        "LEVEL_3",
        "LEVEL_4",
    ]

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
    requestDetails: RequestDetails
    testingDetails: TestingDetails
