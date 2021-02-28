import typing

import typing_extensions
@typing.type_check_only
class GoogleIdentityStsV1ExchangeTokenRequest(typing_extensions.TypedDict, total=False):
    audience: str
    grantType: str
    options: str
    requestedTokenType: str
    scope: str
    subjectToken: str
    subjectTokenType: str

@typing.type_check_only
class GoogleIdentityStsV1ExchangeTokenResponse(
    typing_extensions.TypedDict, total=False
):
    access_token: str
    expires_in: int
    issued_token_type: str
    token_type: str
