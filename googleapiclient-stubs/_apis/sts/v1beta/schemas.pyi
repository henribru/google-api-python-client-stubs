import typing

import typing_extensions

class GoogleIdentityStsV1betaExchangeTokenRequest(
    typing_extensions.TypedDict, total=False
):
    requestedTokenType: str
    subjectTokenType: str
    scope: str
    options: str
    grantType: str
    audience: str
    subjectToken: str

class GoogleIdentityStsV1betaExchangeTokenResponse(
    typing_extensions.TypedDict, total=False
):
    issued_token_type: str
    token_type: str
    expires_in: int
    access_token: str
