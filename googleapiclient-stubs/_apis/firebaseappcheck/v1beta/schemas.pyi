import typing

_list = list

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAppAttestConfig(typing.TypedDict, total=False):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAppCheckToken(typing.TypedDict, total=False):
    attestationToken: str
    token: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAttestationTokenResponse(
    typing.TypedDict, total=False
):
    attestationToken: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetAppAttestConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaAppAttestConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaDeviceCheckConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetPlayIntegrityConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaPlayIntegrityConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaRecaptchaConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaEnterpriseConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaV3ConfigsResponse(
    typing.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaRecaptchaV3Config]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateResourcePoliciesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleFirebaseAppcheckV1betaUpdateResourcePolicyRequest]
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateResourcePoliciesResponse(
    typing.TypedDict, total=False
):
    resourcePolicies: _list[GoogleFirebaseAppcheckV1betaResourcePolicy]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleFirebaseAppcheckV1betaUpdateServiceRequest]
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponse(
    typing.TypedDict, total=False
):
    services: _list[GoogleFirebaseAppcheckV1betaService]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDebugToken(typing.TypedDict, total=False):
    displayName: str
    etag: str
    name: str
    token: str
    updateTime: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDeviceCheckConfig(typing.TypedDict, total=False):
    keyId: str
    name: str
    privateKey: str
    privateKeySet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeAppAttestAssertionRequest(
    typing.TypedDict, total=False
):
    artifact: str
    assertion: str
    challenge: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationRequest(
    typing.TypedDict, total=False
):
    attestationStatement: str
    challenge: str
    keyId: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationResponse(
    typing.TypedDict, total=False
):
    appCheckToken: GoogleFirebaseAppcheckV1betaAppCheckToken
    artifact: str
    attestationToken: GoogleFirebaseAppcheckV1betaAttestationTokenResponse

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeCustomTokenRequest(
    typing.TypedDict, total=False
):
    customToken: str
    jti: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeDebugTokenRequest(
    typing.TypedDict, total=False
):
    debugToken: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeDeviceCheckTokenRequest(
    typing.TypedDict, total=False
):
    deviceToken: str
    limitedUse: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangePlayIntegrityTokenRequest(
    typing.TypedDict, total=False
):
    limitedUse: bool
    playIntegrityToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeRecaptchaEnterpriseTokenRequest(
    typing.TypedDict, total=False
):
    limitedUse: bool
    recaptchaEnterpriseToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeRecaptchaTokenRequest(
    typing.TypedDict, total=False
):
    recaptchaToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeRecaptchaV3TokenRequest(
    typing.TypedDict, total=False
):
    limitedUse: bool
    recaptchaV3Token: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeResponse(
    typing.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeResponse(
    typing.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListDebugTokensResponse(
    typing.TypedDict, total=False
):
    debugTokens: _list[GoogleFirebaseAppcheckV1betaDebugToken]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListResourcePoliciesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    resourcePolicies: _list[GoogleFirebaseAppcheckV1betaResourcePolicy]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[GoogleFirebaseAppcheckV1betaService]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPlayIntegrityConfig(typing.TypedDict, total=False):
    accountDetails: GoogleFirebaseAppcheckV1betaPlayIntegrityConfigAccountDetails
    appIntegrity: GoogleFirebaseAppcheckV1betaPlayIntegrityConfigAppIntegrity
    deviceIntegrity: GoogleFirebaseAppcheckV1betaPlayIntegrityConfigDeviceIntegrity
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPlayIntegrityConfigAccountDetails(
    typing.TypedDict, total=False
):
    requireLicensed: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPlayIntegrityConfigAppIntegrity(
    typing.TypedDict, total=False
):
    allowUnrecognizedVersion: bool

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPlayIntegrityConfigDeviceIntegrity(
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
class GoogleFirebaseAppcheckV1betaPublicJwk(typing.TypedDict, total=False):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPublicJwkSet(typing.TypedDict, total=False):
    keys: _list[GoogleFirebaseAppcheckV1betaPublicJwk]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaConfig(typing.TypedDict, total=False):
    minValidScore: float
    name: str
    siteSecret: str
    siteSecretSet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfig(
    typing.TypedDict, total=False
):
    name: str
    riskAnalysis: GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfigRiskAnalysis
    siteKey: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfigRiskAnalysis(
    typing.TypedDict, total=False
):
    minValidScore: float

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaV3Config(typing.TypedDict, total=False):
    minValidScore: float
    name: str
    siteSecret: str
    siteSecretSet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaResourcePolicy(typing.TypedDict, total=False):
    enforcementMode: typing.Literal["OFF", "UNENFORCED", "ENFORCED"]
    etag: str
    name: str
    targetResource: str
    updateTime: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaService(typing.TypedDict, total=False):
    enforcementMode: typing.Literal["OFF", "UNENFORCED", "ENFORCED"]
    etag: str
    name: str
    replayProtection: typing.Literal["OFF", "UNENFORCED", "ENFORCED"]
    updateTime: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaUpdateResourcePolicyRequest(
    typing.TypedDict, total=False
):
    resourcePolicy: GoogleFirebaseAppcheckV1betaResourcePolicy
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaUpdateServiceRequest(typing.TypedDict, total=False):
    service: GoogleFirebaseAppcheckV1betaService
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaVerifyAppCheckTokenRequest(
    typing.TypedDict, total=False
):
    appCheckToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaVerifyAppCheckTokenResponse(
    typing.TypedDict, total=False
):
    alreadyConsumed: bool

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...
