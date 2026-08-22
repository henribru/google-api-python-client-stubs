import typing

_list = list

@typing.type_check_only
class AccountActivity(typing.TypedDict, total=False):
    activityLevel: typing.Literal[
        "ACTIVITY_LEVEL_UNSPECIFIED",
        "UNEVALUATED",
        "UNUSUAL",
        "UNKNOWN",
        "TYPICAL_BASIC",
        "TYPICAL_STRONG",
    ]

@typing.type_check_only
class AccountDetails(typing.TypedDict, total=False):
    accountActivity: AccountActivity
    appLicensingVerdict: typing.Literal[
        "UNKNOWN", "LICENSED", "UNLICENSED", "UNEVALUATED"
    ]

@typing.type_check_only
class AppAccessRiskVerdict(typing.TypedDict, total=False):
    appsDetected: _list[
        typing.Literal[
            "APPS_DETECTED_UNSPECIFIED",
            "KNOWN_INSTALLED",
            "KNOWN_CAPTURING",
            "KNOWN_OVERLAYS",
            "KNOWN_CONTROLLING",
            "UNKNOWN_INSTALLED",
            "UNKNOWN_CAPTURING",
            "UNKNOWN_OVERLAYS",
            "UNKNOWN_CONTROLLING",
        ]
    ]

@typing.type_check_only
class AppIntegrity(typing.TypedDict, total=False):
    appRecognitionVerdict: typing.Literal[
        "UNKNOWN", "PLAY_RECOGNIZED", "UNRECOGNIZED_VERSION", "UNEVALUATED"
    ]
    certificateSha256Digest: _list[str]
    packageName: str
    versionCode: str

@typing.type_check_only
class DecodeIntegrityTokenRequest(typing.TypedDict, total=False):
    integrityToken: str

@typing.type_check_only
class DecodeIntegrityTokenResponse(typing.TypedDict, total=False):
    tokenPayloadExternal: TokenPayloadExternal

@typing.type_check_only
class DecodePcIntegrityTokenRequest(typing.TypedDict, total=False):
    integrityToken: str

@typing.type_check_only
class DecodePcIntegrityTokenResponse(typing.TypedDict, total=False):
    tokenPayloadExternal: PcTokenPayloadExternal

@typing.type_check_only
class DeviceAttributes(typing.TypedDict, total=False):
    sdkVersion: int

@typing.type_check_only
class DeviceIntegrity(typing.TypedDict, total=False):
    deviceAttributes: DeviceAttributes
    deviceRecall: DeviceRecall
    deviceRecognitionVerdict: _list[
        typing.Literal[
            "UNKNOWN",
            "MEETS_BASIC_INTEGRITY",
            "MEETS_DEVICE_INTEGRITY",
            "MEETS_STRONG_INTEGRITY",
            "MEETS_VIRTUAL_INTEGRITY",
        ]
    ]
    legacyDeviceRecognitionVerdict: _list[
        typing.Literal[
            "UNKNOWN",
            "MEETS_BASIC_INTEGRITY",
            "MEETS_DEVICE_INTEGRITY",
            "MEETS_STRONG_INTEGRITY",
            "MEETS_VIRTUAL_INTEGRITY",
        ]
    ]
    recentDeviceActivity: RecentDeviceActivity

@typing.type_check_only
class DeviceRecall(typing.TypedDict, total=False):
    values: Values
    writeDates: WriteDates

@typing.type_check_only
class EnvironmentDetails(typing.TypedDict, total=False):
    appAccessRiskVerdict: AppAccessRiskVerdict
    playProtectVerdict: typing.Literal[
        "PLAY_PROTECT_VERDICT_UNSPECIFIED",
        "UNEVALUATED",
        "NO_ISSUES",
        "NO_DATA",
        "MEDIUM_RISK",
        "HIGH_RISK",
        "POSSIBLE_RISK",
    ]

@typing.type_check_only
class PcAccountDetails(typing.TypedDict, total=False):
    appLicensingVerdict: typing.Literal[
        "UNKNOWN", "LICENSED", "UNLICENSED", "UNEVALUATED"
    ]

@typing.type_check_only
class PcDeviceIntegrity(typing.TypedDict, total=False):
    deviceRecognitionVerdict: _list[
        typing.Literal["DEVICE_RECOGNITION_VERDICT_UNSPECIFIED", "MEETS_PC_INTEGRITY"]
    ]

@typing.type_check_only
class PcRequestDetails(typing.TypedDict, total=False):
    requestHash: str
    requestPackageName: str
    requestTime: str

@typing.type_check_only
class PcTestingDetails(typing.TypedDict, total=False):
    isTestingResponse: bool

@typing.type_check_only
class PcTokenPayloadExternal(typing.TypedDict, total=False):
    accountDetails: PcAccountDetails
    deviceIntegrity: PcDeviceIntegrity
    requestDetails: PcRequestDetails
    testingDetails: PcTestingDetails

@typing.type_check_only
class RecentDeviceActivity(typing.TypedDict, total=False):
    deviceActivityLevel: typing.Literal[
        "DEVICE_ACTIVITY_LEVEL_UNSPECIFIED",
        "UNEVALUATED",
        "LEVEL_1",
        "LEVEL_2",
        "LEVEL_3",
        "LEVEL_4",
    ]

@typing.type_check_only
class RequestDetails(typing.TypedDict, total=False):
    nonce: str
    requestHash: str
    requestPackageName: str
    timestampMillis: str

@typing.type_check_only
class TestingDetails(typing.TypedDict, total=False):
    isTestingResponse: bool

@typing.type_check_only
class TokenPayloadExternal(typing.TypedDict, total=False):
    accountDetails: AccountDetails
    appIntegrity: AppIntegrity
    deviceIntegrity: DeviceIntegrity
    environmentDetails: EnvironmentDetails
    requestDetails: RequestDetails
    testingDetails: TestingDetails

@typing.type_check_only
class Values(typing.TypedDict, total=False):
    bitFirst: bool
    bitSecond: bool
    bitThird: bool

@typing.type_check_only
class WriteDates(typing.TypedDict, total=False):
    yyyymmFirst: int
    yyyymmSecond: int
    yyyymmThird: int

@typing.type_check_only
class WriteDeviceRecallRequest(typing.TypedDict, total=False):
    integrityToken: str
    newValues: Values

@typing.type_check_only
class WriteDeviceRecallResponse(typing.TypedDict, total=False): ...
