import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...

class Challenge(typing_extensions.TypedDict, total=False):
    challenge: SignedData
    alternativeChallenge: SignedData

class VerifyChallengeResponseRequest(typing_extensions.TypedDict, total=False):
    expectedIdentity: str
    challengeResponse: SignedData

class SignedData(typing_extensions.TypedDict, total=False):
    data: str
    signature: str

class VerifyChallengeResponseResult(typing_extensions.TypedDict, total=False):
    verificationOutput: str
    deviceEnrollmentId: str
    devicePermanentId: str
    signedPublicKeyAndChallenge: str
