import typing

_list = list

@typing.type_check_only
class Challenge(typing.TypedDict, total=False):
    alternativeChallenge: SignedData
    challenge: SignedData

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class SignedData(typing.TypedDict, total=False):
    data: str
    signature: str

@typing.type_check_only
class VerifyChallengeResponseRequest(typing.TypedDict, total=False):
    challengeResponse: SignedData
    expectedIdentity: str

@typing.type_check_only
class VerifyChallengeResponseResult(typing.TypedDict, total=False):
    attestedDeviceId: str
    deviceEnrollmentId: str
    devicePermanentId: str
    signedPublicKeyAndChallenge: str
    verificationOutput: str
