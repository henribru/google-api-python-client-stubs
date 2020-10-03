import typing

import typing_extensions

class SiteVerificationWebResourceGettokenResponse(
    typing_extensions.TypedDict, total=False
):
    method: str
    token: str

class SiteVerificationWebResourceResource(typing_extensions.TypedDict, total=False):
    owners: typing.List[str]
    site: typing.Dict[str, typing.Any]
    id: str

class SiteVerificationWebResourceListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[SiteVerificationWebResourceResource]

class SiteVerificationWebResourceGettokenRequest(
    typing_extensions.TypedDict, total=False
):
    verificationMethod: str
    site: typing.Dict[str, typing.Any]
