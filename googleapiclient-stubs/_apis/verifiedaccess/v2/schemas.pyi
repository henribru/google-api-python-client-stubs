import typing

import typing_extensions

_list = list

@typing.type_check_only
class Challenge(typing_extensions.TypedDict, total=False):
    alternativeChallenge: str
    challenge: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VerifyChallengeResponseRequest(typing_extensions.TypedDict, total=False):
    challengeResponse: str
    expectedIdentity: str

@typing.type_check_only
class VerifyChallengeResponseResult(typing_extensions.TypedDict, total=False):
    devicePermanentId: str
    deviceSignal: str
    keyTrustLevel: typing_extensions.Literal[
        "KEY_TRUST_LEVEL_UNSPECIFIED",
        "CHROME_OS_VERIFIED_MODE",
        "CHROME_OS_DEVELOPER_MODE",
        "CHROME_BROWSER_TPM_KEY",
        "CHROME_BROWSER_OS_KEY",
    ]
    signedPublicKeyAndChallenge: str
