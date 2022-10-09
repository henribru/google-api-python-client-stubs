import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleFirebaseAppcheckV1AppAttestConfig(typing_extensions.TypedDict, total=False):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1AppCheckToken(typing_extensions.TypedDict, total=False):
    token: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1AppAttestConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1DeviceCheckConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1PlayIntegrityConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1RecaptchaV3Config]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    configs: _list[GoogleFirebaseAppcheckV1SafetyNetConfig]

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchUpdateServicesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleFirebaseAppcheckV1UpdateServiceRequest]
    updateMask: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchUpdateServicesResponse(
    typing_extensions.TypedDict, total=False
):
    services: _list[GoogleFirebaseAppcheckV1Service]

@typing.type_check_only
class GoogleFirebaseAppcheckV1DebugToken(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    token: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1DeviceCheckConfig(
    typing_extensions.TypedDict, total=False
):
    keyId: str
    name: str
    privateKey: str
    privateKeySet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequest(
    typing_extensions.TypedDict, total=False
):
    artifact: str
    assertion: str
    challenge: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequest(
    typing_extensions.TypedDict, total=False
):
    attestationStatement: str
    challenge: str
    keyId: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponse(
    typing_extensions.TypedDict, total=False
):
    appCheckToken: GoogleFirebaseAppcheckV1AppCheckToken
    artifact: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeCustomTokenRequest(
    typing_extensions.TypedDict, total=False
):
    customToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeDebugTokenRequest(
    typing_extensions.TypedDict, total=False
):
    debugToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequest(
    typing_extensions.TypedDict, total=False
):
    deviceToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequest(
    typing_extensions.TypedDict, total=False
):
    playIntegrityToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequest(
    typing_extensions.TypedDict, total=False
):
    recaptchaEnterpriseToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequest(
    typing_extensions.TypedDict, total=False
):
    recaptchaV3Token: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequest(
    typing_extensions.TypedDict, total=False
):
    safetyNetToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponse(
    typing_extensions.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponse(
    typing_extensions.TypedDict, total=False
):
    challenge: str
    ttl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ListDebugTokensResponse(
    typing_extensions.TypedDict, total=False
):
    debugTokens: _list[GoogleFirebaseAppcheckV1DebugToken]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1ListServicesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    services: _list[GoogleFirebaseAppcheckV1Service]

@typing.type_check_only
class GoogleFirebaseAppcheckV1PlayIntegrityConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1PublicJwk(typing_extensions.TypedDict, total=False):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1PublicJwkSet(typing_extensions.TypedDict, total=False):
    keys: _list[GoogleFirebaseAppcheckV1PublicJwk]

@typing.type_check_only
class GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    siteKey: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1RecaptchaV3Config(
    typing_extensions.TypedDict, total=False
):
    name: str
    siteSecret: str
    siteSecretSet: bool
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1SafetyNetConfig(typing_extensions.TypedDict, total=False):
    name: str
    tokenTtl: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1Service(typing_extensions.TypedDict, total=False):
    enforcementMode: typing_extensions.Literal["OFF", "UNENFORCED", "ENFORCED"]
    name: str

@typing.type_check_only
class GoogleFirebaseAppcheckV1UpdateServiceRequest(
    typing_extensions.TypedDict, total=False
):
    service: GoogleFirebaseAppcheckV1Service
    updateMask: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
