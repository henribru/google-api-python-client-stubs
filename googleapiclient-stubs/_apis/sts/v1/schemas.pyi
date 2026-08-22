import typing

_list = list

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIdentityStsV1AccessBoundary(typing.TypedDict, total=False):
    accessBoundaryRules: _list[GoogleIdentityStsV1AccessBoundaryRule]

@typing.type_check_only
class GoogleIdentityStsV1AccessBoundaryRule(typing.TypedDict, total=False):
    availabilityCondition: GoogleTypeExpr
    availablePermissions: _list[str]
    availableResource: str

@typing.type_check_only
class GoogleIdentityStsV1ExchangeTokenRequest(typing.TypedDict, total=False):
    audience: str
    grantType: str
    options: str
    requestedTokenType: str
    scope: str
    subjectToken: str
    subjectTokenType: str

@typing.type_check_only
class GoogleIdentityStsV1ExchangeTokenResponse(typing.TypedDict, total=False):
    access_boundary_session_key: str
    access_token: str
    expires_in: int
    issued_token_type: str
    token_type: str

@typing.type_check_only
class GoogleIdentityStsV1Jwk(typing.TypedDict, total=False):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

@typing.type_check_only
class GoogleIdentityStsV1Jwks(typing.TypedDict, total=False):
    keys: _list[GoogleIdentityStsV1Jwk]

@typing.type_check_only
class GoogleIdentityStsV1OpenIdProviderConfig(typing.TypedDict, total=False):
    authorization_endpoint: str
    id_token_signing_alg_values_supported: _list[str]
    issuer: str
    jwks_uri: str
    response_types_supported: _list[str]
    subject_types_supported: _list[str]
    token_endpoint: str

@typing.type_check_only
class GoogleIdentityStsV1Options(typing.TypedDict, total=False):
    accessBoundary: GoogleIdentityStsV1AccessBoundary
    bindCertFingerprint: str
    userProject: str

@typing.type_check_only
class GoogleIdentityStsV1betaAccessBoundary(typing.TypedDict, total=False):
    accessBoundaryRules: _list[GoogleIdentityStsV1betaAccessBoundaryRule]

@typing.type_check_only
class GoogleIdentityStsV1betaAccessBoundaryRule(typing.TypedDict, total=False):
    availabilityCondition: GoogleTypeExpr
    availablePermissions: _list[str]
    availableResource: str

@typing.type_check_only
class GoogleIdentityStsV1betaOptions(typing.TypedDict, total=False):
    accessBoundary: GoogleIdentityStsV1betaAccessBoundary
    userProject: str

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
