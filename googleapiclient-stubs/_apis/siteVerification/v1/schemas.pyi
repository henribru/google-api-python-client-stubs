import typing

import typing_extensions
@typing.type_check_only
class SiteVerificationWebResourceGettokenRequest(
    typing_extensions.TypedDict, total=False
):
    site: typing.Dict[str, typing.Any]
    verificationMethod: str

@typing.type_check_only
class SiteVerificationWebResourceGettokenResponse(
    typing_extensions.TypedDict, total=False
):
    method: str
    token: str

@typing.type_check_only
class SiteVerificationWebResourceListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[SiteVerificationWebResourceResource]

@typing.type_check_only
class SiteVerificationWebResourceResource(typing_extensions.TypedDict, total=False):
    id: str
    owners: typing.List[str]
    site: typing.Dict[str, typing.Any]
