import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AndroidKeySettings(
    typing_extensions.TypedDict, total=False
):
    allowAllPackageNames: bool
    allowedPackageNames: _list[str]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest(
    typing_extensions.TypedDict, total=False
):
    annotation: typing_extensions.Literal[
        "ANNOTATION_UNSPECIFIED",
        "LEGITIMATE",
        "FRAUDULENT",
        "PASSWORD_CORRECT",
        "PASSWORD_INCORRECT",
    ]
    reasons: _list[str]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Assessment(
    typing_extensions.TypedDict, total=False
):
    event: GoogleCloudRecaptchaenterpriseV1Event
    name: str
    riskAnalysis: GoogleCloudRecaptchaenterpriseV1RiskAnalysis
    tokenProperties: GoogleCloudRecaptchaenterpriseV1TokenProperties

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeMetrics(
    typing_extensions.TypedDict, total=False
):
    failedCount: str
    nocaptchaCount: str
    pageloadCount: str
    passedCount: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Event(typing_extensions.TypedDict, total=False):
    expectedAction: str
    siteKey: str
    token: str
    userAgent: str
    userIpAddress: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1IOSKeySettings(
    typing_extensions.TypedDict, total=False
):
    allowAllBundleIds: bool
    allowedBundleIds: _list[str]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Key(typing_extensions.TypedDict, total=False):
    androidSettings: GoogleCloudRecaptchaenterpriseV1AndroidKeySettings
    createTime: str
    displayName: str
    iosSettings: GoogleCloudRecaptchaenterpriseV1IOSKeySettings
    labels: dict[str, typing.Any]
    name: str
    testingOptions: GoogleCloudRecaptchaenterpriseV1TestingOptions
    webSettings: GoogleCloudRecaptchaenterpriseV1WebKeySettings

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListKeysResponse(
    typing_extensions.TypedDict, total=False
):
    keys: _list[GoogleCloudRecaptchaenterpriseV1Key]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Metrics(typing_extensions.TypedDict, total=False):
    challengeMetrics: _list[GoogleCloudRecaptchaenterpriseV1ChallengeMetrics]
    name: str
    scoreMetrics: _list[GoogleCloudRecaptchaenterpriseV1ScoreMetrics]
    startTime: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1MigrateKeyRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RiskAnalysis(
    typing_extensions.TypedDict, total=False
):
    reasons: _list[str]
    score: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ScoreDistribution(
    typing_extensions.TypedDict, total=False
):
    scoreBuckets: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ScoreMetrics(
    typing_extensions.TypedDict, total=False
):
    actionMetrics: dict[str, typing.Any]
    overallMetrics: GoogleCloudRecaptchaenterpriseV1ScoreDistribution

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TestingOptions(
    typing_extensions.TypedDict, total=False
):
    testingChallenge: typing_extensions.Literal[
        "TESTING_CHALLENGE_UNSPECIFIED", "NOCAPTCHA", "UNSOLVABLE_CHALLENGE"
    ]
    testingScore: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TokenProperties(
    typing_extensions.TypedDict, total=False
):
    action: str
    createTime: str
    hostname: str
    invalidReason: typing_extensions.Literal[
        "INVALID_REASON_UNSPECIFIED",
        "UNKNOWN_INVALID_REASON",
        "MALFORMED",
        "EXPIRED",
        "DUPE",
        "MISSING",
        "BROWSER_ERROR",
    ]
    valid: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1WebKeySettings(
    typing_extensions.TypedDict, total=False
):
    allowAllDomains: bool
    allowAmpTraffic: bool
    allowedDomains: _list[str]
    challengeSecurityPreference: typing_extensions.Literal[
        "CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED", "USABILITY", "BALANCE", "SECURITY"
    ]
    integrationType: typing_extensions.Literal[
        "INTEGRATION_TYPE_UNSPECIFIED", "SCORE", "CHECKBOX", "INVISIBLE"
    ]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
