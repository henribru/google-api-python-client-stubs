import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAppAttestConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAppCheckToken(
    typing_extensions.TypedDict, total=False
):
    attestationToken: str
    token: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAttestationTokenResponse(
    typing_extensions.TypedDict, total=False
):
    attestationToken: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetAppAttestConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaAppAttestConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaDeviceCheckConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetPlayIntegrityConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaPlayIntegrityConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaRecaptchaConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaEnterpriseConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaV3ConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaRecaptchaV3Config]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetSafetyNetConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1betaSafetyNetConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleFirebaseAppcheckV1betaUpdateServiceRequest]
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponse(
    typing_extensions.TypedDict, total=False
):
    services: _list[GoogleFirebaseAppcheckV1betaService]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDebugToken(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    token: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDeviceCheckConfig(
    typing_extensions.TypedDict, total=False
):
    keyId: str
    name: str
    privateKey: str
    privateKeySet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeAppAttestAssertionRequest(
    typing_extensions.TypedDict, total=False
):
    artifact: str
    assertion: str
    challenge: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationRequest(
    typing_extensions.TypedDict, total=False
):
    attestationStatement: str
    challenge: str
    keyId: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationResponse(
    typing_extensions.TypedDict, total=False
):
    appCheckToken: GoogleFirebaseAppcheckV1betaAppCheckToken
    artifact: str
    attestationToken: GoogleFirebaseAppcheckV1betaAttestationTokenResponse

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeCustomTokenRequest(
    typing_extensions.TypedDict, total=False
):
    customToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeDebugTokenRequest(
    typing_extensions.TypedDict, total=False
):
    debugToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeDeviceCheckTokenRequest(
    typing_extensions.TypedDict, total=False
):
    deviceToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangePlayIntegrityTokenRequest(
    typing_extensions.TypedDict, total=False
):
    playIntegrityToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeRecaptchaEnterpriseTokenRequest(
    typing_extensions.TypedDict, total=False
):
    recaptchaEnterpriseToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeRecaptchaTokenRequest(
    typing_extensions.TypedDict, total=False
):
    recaptchaToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeRecaptchaV3TokenRequest(
    typing_extensions.TypedDict, total=False
):
    recaptchaV3Token: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeSafetyNetTokenRequest(
    typing_extensions.TypedDict, total=False
):
    safetyNetToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeResponse(
    typing_extensions.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeResponse(
    typing_extensions.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListDebugTokensResponse(
    typing_extensions.TypedDict, total=False
):
    debugTokens: _list[GoogleFirebaseAppcheckV1betaDebugToken]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListServicesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    services: _list[GoogleFirebaseAppcheckV1betaService]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPlayIntegrityConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPublicJwk(typing_extensions.TypedDict, total=False):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPublicJwkSet(
    typing_extensions.TypedDict, total=False
):
    keys: _list[GoogleFirebaseAppcheckV1betaPublicJwk]

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    siteSecret: str
    siteSecretSet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    siteKey: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaV3Config(
    typing_extensions.TypedDict, total=False
):
    name: str
    siteSecret: str
    siteSecretSet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaSafetyNetConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaService(typing_extensions.TypedDict, total=False):
    enforcementMode: typing_extensions.Literal["OFF", "UNENFORCED", "ENFORCED"]
    name: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaUpdateServiceRequest(
    typing_extensions.TypedDict, total=False
):
    service: GoogleFirebaseAppcheckV1betaService
    updateMask: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
