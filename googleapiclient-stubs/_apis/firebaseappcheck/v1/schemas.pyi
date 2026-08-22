import typing

_list = list

@typing.type_check_only
class GoogleFirebaseAppcheckV1AppAttestConfig(typing.TypedDict, total=False):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1AppCheckToken(typing.TypedDict, total=False):
    token: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1AppAttestConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1DeviceCheckConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1PlayIntegrityConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1RecaptchaV3Config]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchUpdateResourcePoliciesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleFirebaseAppcheckV1UpdateResourcePolicyRequest]
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchUpdateResourcePoliciesResponse(
    typing.TypedDict, total=False
):
    resourcePolicies: _list[GoogleFirebaseAppcheckV1ResourcePolicy]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchUpdateServicesRequest(typing.TypedDict, total=False):
    requests: _list[GoogleFirebaseAppcheckV1UpdateServiceRequest]
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchUpdateServicesResponse(
    typing.TypedDict, total=False
):
    services: _list[GoogleFirebaseAppcheckV1Service]

@typing.type_check_only
class GoogleFirebaseAppcheckV1DebugToken(typing.TypedDict, total=False):
    displayName: str
    etag: str
    name: str
    token: str
    updateTime: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1DeviceCheckConfig(typing.TypedDict, total=False):
    keyId: str
    name: str
    privateKey: str
    privateKeySet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequest(
    typing.TypedDict, total=False
):
    artifact: str
    assertion: str
    challenge: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequest(
    typing.TypedDict, total=False
):
    attestationStatement: str
    challenge: str
    keyId: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponse(
    typing.TypedDict, total=False
):
    appCheckToken: GoogleFirebaseAppcheckV1AppCheckToken
    artifact: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeCustomTokenRequest(typing.TypedDict, total=False):
    customToken: str
    jti: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeDebugTokenRequest(typing.TypedDict, total=False):
    debugToken: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequest(
    typing.TypedDict, total=False
):
    deviceToken: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequest(
    typing.TypedDict, total=False
):
    limitedUse: bool
    playIntegrityToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequest(
    typing.TypedDict, total=False
):
    limitedUse: bool
    recaptchaEnterpriseToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequest(
    typing.TypedDict, total=False
):
    limitedUse: bool
    recaptchaV3Token: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponse(
    typing.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponse(
    typing.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ListDebugTokensResponse(typing.TypedDict, total=False):
    debugTokens: _list[GoogleFirebaseAppcheckV1DebugToken]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ListResourcePoliciesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    resourcePolicies: _list[GoogleFirebaseAppcheckV1ResourcePolicy]

@typing.type_check_only
class GoogleFirebaseAppcheckV1ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[GoogleFirebaseAppcheckV1Service]

@typing.type_check_only
class GoogleFirebaseAppcheckV1PlayIntegrityConfig(typing.TypedDict, total=False):
    accountDetails: GoogleFirebaseAppcheckV1PlayIntegrityConfigAccountDetails
    appIntegrity: GoogleFirebaseAppcheckV1PlayIntegrityConfigAppIntegrity
    deviceIntegrity: GoogleFirebaseAppcheckV1PlayIntegrityConfigDeviceIntegrity
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1PlayIntegrityConfigAccountDetails(
    typing.TypedDict, total=False
):
    requireLicensed: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1PlayIntegrityConfigAppIntegrity(
    typing.TypedDict, total=False
):
    allowUnrecognizedVersion: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1PlayIntegrityConfigDeviceIntegrity(
    typing.TypedDict, total=False
):
    minDeviceRecognitionLevel: typing.Literal[
        "DEVICE_RECOGNITION_LEVEL_UNSPECIFIED",
        "NO_INTEGRITY",
        "MEETS_BASIC_INTEGRITY",
        "MEETS_DEVICE_INTEGRITY",
        "MEETS_STRONG_INTEGRITY",
    ]

@typing.type_check_only
class GoogleFirebaseAppcheckV1PublicJwk(typing.TypedDict, total=False):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1PublicJwkSet(typing.TypedDict, total=False):
    keys: _list[GoogleFirebaseAppcheckV1PublicJwk]

@typing.type_check_only
class GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig(typing.TypedDict, total=False):
    name: str
    riskAnalysis: GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigRiskAnalysis
    siteKey: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigRiskAnalysis(
    typing.TypedDict, total=False
):
    minValidScore: float

@typing.type_check_only
class GoogleFirebaseAppcheckV1RecaptchaV3Config(typing.TypedDict, total=False):
    minValidScore: float
    name: str
    siteSecret: str
    siteSecretSet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ResourcePolicy(typing.TypedDict, total=False):
    enforcementMode: typing.Literal["OFF", "UNENFORCED", "ENFORCED"]
    etag: str
    name: str
    targetResource: str
    updateTime: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1Service(typing.TypedDict, total=False):
    enforcementMode: typing.Literal["OFF", "UNENFORCED", "ENFORCED"]
    etag: str
    name: str
    replayProtection: typing.Literal["OFF", "UNENFORCED", "ENFORCED"]
    updateTime: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1UpdateResourcePolicyRequest(
    typing.TypedDict, total=False
):
    resourcePolicy: GoogleFirebaseAppcheckV1ResourcePolicy
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1UpdateServiceRequest(typing.TypedDict, total=False):
    service: GoogleFirebaseAppcheckV1Service
    updateMask: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...
