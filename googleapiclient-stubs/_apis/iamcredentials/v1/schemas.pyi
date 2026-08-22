import typing

_list = list

@typing.type_check_only
class GenerateAccessTokenRequest(typing.TypedDict, total=False):
    delegates: _list[str]
    lifetime: str
    scope: _list[str]

@typing.type_check_only
class GenerateAccessTokenResponse(typing.TypedDict, total=False):
    accessToken: str
    expireTime: str

@typing.type_check_only
class GenerateIdTokenRequest(typing.TypedDict, total=False):
    audience: str
    delegates: _list[str]
    includeEmail: bool
    organizationNumberIncluded: bool

@typing.type_check_only
class GenerateIdTokenResponse(typing.TypedDict, total=False):
    token: str

@typing.type_check_only
class ServiceAccountAllowedLocations(typing.TypedDict, total=False):
    encodedLocations: str
    locations: _list[str]

@typing.type_check_only
class SignBlobRequest(typing.TypedDict, total=False):
    delegates: _list[str]
    payload: str

@typing.type_check_only
class SignBlobResponse(typing.TypedDict, total=False):
    keyId: str
    signedBlob: str

@typing.type_check_only
class SignJwtRequest(typing.TypedDict, total=False):
    delegates: _list[str]
    payload: str

@typing.type_check_only
class SignJwtResponse(typing.TypedDict, total=False):
    keyId: str
    signedJwt: str

@typing.type_check_only
class WorkforcePoolAllowedLocations(typing.TypedDict, total=False):
    encodedLocations: str
    locations: _list[str]

@typing.type_check_only
class WorkloadIdentityPoolAllowedLocations(typing.TypedDict, total=False):
    encodedLocations: str
    locations: _list[str]
