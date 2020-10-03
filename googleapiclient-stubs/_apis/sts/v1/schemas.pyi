import typing

import typing_extensions

class GoogleIdentityStsV1ExchangeTokenRequest(typing_extensions.TypedDict, total=False):
    options: str
    subjectToken: str
    grantType: str
    subjectTokenType: str
    requestedTokenType: str

class GoogleIdentityStsV1ExchangeTokenResponse(
    typing_extensions.TypedDict, total=False
):
    token_type: str
    access_token: str
    issued_token_type: str
    expires_in: int
