import typing

import typing_extensions

_list = list

@typing.type_check_only
class GenerateAccessTokenRequest(typing_extensions.TypedDict, total=False):
    delegates: _list[str]
    lifetime: str
    scope: _list[str]

@typing.type_check_only
class GenerateAccessTokenResponse(typing_extensions.TypedDict, total=False):
    accessToken: str
    expireTime: str

@typing.type_check_only
class GenerateIdTokenRequest(typing_extensions.TypedDict, total=False):
    audience: str
    delegates: _list[str]
    includeEmail: bool

@typing.type_check_only
class GenerateIdTokenResponse(typing_extensions.TypedDict, total=False):
    token: str

@typing.type_check_only
class SignBlobRequest(typing_extensions.TypedDict, total=False):
    delegates: _list[str]
    payload: str

@typing.type_check_only
class SignBlobResponse(typing_extensions.TypedDict, total=False):
    keyId: str
    signedBlob: str

@typing.type_check_only
class SignJwtRequest(typing_extensions.TypedDict, total=False):
    delegates: _list[str]
    payload: str

@typing.type_check_only
class SignJwtResponse(typing_extensions.TypedDict, total=False):
    keyId: str
    signedJwt: str
