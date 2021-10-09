import typing

import typing_extensions

_list = list

@typing.type_check_only
class Challenge(typing_extensions.TypedDict, total=False):
    alternativeChallenge: SignedData
    challenge: SignedData

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SignedData(typing_extensions.TypedDict, total=False):
    data: str
    signature: str

@typing.type_check_only
class VerifyChallengeResponseRequest(typing_extensions.TypedDict, total=False):
    challengeResponse: SignedData
    expectedIdentity: str

@typing.type_check_only
class VerifyChallengeResponseResult(typing_extensions.TypedDict, total=False):
    deviceEnrollmentId: str
    devicePermanentId: str
    signedPublicKeyAndChallenge: str
    verificationOutput: str
