import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIdentityStsV1AccessBoundary(typing_extensions.TypedDict, total=False):
    accessBoundaryRules: _list[GoogleIdentityStsV1AccessBoundaryRule]

@typing.type_check_only
class GoogleIdentityStsV1AccessBoundaryRule(typing_extensions.TypedDict, total=False):
    availabilityCondition: GoogleTypeExpr
    availablePermissions: _list[str]
    availableResource: str

@typing.type_check_only
class GoogleIdentityStsV1Options(typing_extensions.TypedDict, total=False):
    accessBoundary: GoogleIdentityStsV1AccessBoundary
    audiences: _list[str]
    userProject: str

@typing.type_check_only
class GoogleIdentityStsV1betaAccessBoundary(typing_extensions.TypedDict, total=False):
    accessBoundaryRules: _list[GoogleIdentityStsV1betaAccessBoundaryRule]

@typing.type_check_only
class GoogleIdentityStsV1betaAccessBoundaryRule(
    typing_extensions.TypedDict, total=False
):
    availabilityCondition: GoogleTypeExpr
    availablePermissions: _list[str]
    availableResource: str

@typing.type_check_only
class GoogleIdentityStsV1betaExchangeTokenRequest(
    typing_extensions.TypedDict, total=False
):
    audience: str
    grantType: str
    options: str
    requestedTokenType: str
    scope: str
    subjectToken: str
    subjectTokenType: str

@typing.type_check_only
class GoogleIdentityStsV1betaExchangeTokenResponse(
    typing_extensions.TypedDict, total=False
):
    access_token: str
    expires_in: int
    issued_token_type: str
    token_type: str

@typing.type_check_only
class GoogleIdentityStsV1betaOptions(typing_extensions.TypedDict, total=False):
    accessBoundary: GoogleIdentityStsV1betaAccessBoundary
    audiences: _list[str]
    userProject: str

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
