import typing

_list = list

@typing.type_check_only
class SiteVerificationWebResourceGettokenRequest(typing.TypedDict, total=False):
    site: dict[str, typing.Any]
    verificationMethod: str

@typing.type_check_only
class SiteVerificationWebResourceGettokenResponse(typing.TypedDict, total=False):
    method: str
    token: str

@typing.type_check_only
class SiteVerificationWebResourceListResponse(typing.TypedDict, total=False):
    items: _list[SiteVerificationWebResourceResource]

@typing.type_check_only
class SiteVerificationWebResourceResource(typing.TypedDict, total=False):
    id: str
    owners: _list[str]
    site: dict[str, typing.Any]
