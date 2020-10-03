import typing

import typing_extensions

class GenerateAccessTokenRequest(typing_extensions.TypedDict, total=False):
    lifetime: str
    scope: typing.List[str]
    delegates: typing.List[str]

class SignJwtResponse(typing_extensions.TypedDict, total=False):
    signedJwt: str
    keyId: str

class GenerateIdTokenRequest(typing_extensions.TypedDict, total=False):
    audience: str
    includeEmail: bool
    delegates: typing.List[str]

class SignJwtRequest(typing_extensions.TypedDict, total=False):
    payload: str
    delegates: typing.List[str]

class GenerateIdTokenResponse(typing_extensions.TypedDict, total=False):
    token: str

class SignBlobRequest(typing_extensions.TypedDict, total=False):
    delegates: typing.List[str]
    payload: str

class GenerateAccessTokenResponse(typing_extensions.TypedDict, total=False):
    accessToken: str
    expireTime: str

class SignBlobResponse(typing_extensions.TypedDict, total=False):
    signedBlob: str
    keyId: str
