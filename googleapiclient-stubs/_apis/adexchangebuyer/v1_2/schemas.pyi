import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    bidderLocation: _list[dict[str, typing.Any]]
    cookieMatchingNid: str
    cookieMatchingUrl: str
    id: int
    kind: str
    maximumActiveCreatives: int
    maximumTotalQps: int
    numberActiveCreatives: int

@typing.type_check_only
class AccountsList(typing_extensions.TypedDict, total=False):
    items: _list[Account]
    kind: str

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    HTMLSnippet: str
    accountId: int
    advertiserId: _list[str]
    advertiserName: str
    agencyId: str
    apiUploadTimestamp: str
    attribute: _list[int]
    buyerCreativeId: str
    clickThroughUrl: _list[str]
    corrections: _list[dict[str, typing.Any]]
    disapprovalReasons: _list[dict[str, typing.Any]]
    filteringReasons: dict[str, typing.Any]
    height: int
    impressionTrackingUrl: _list[str]
    kind: str
    productCategories: _list[int]
    restrictedCategories: _list[int]
    sensitiveCategories: _list[int]
    status: str
    vendorType: _list[int]
    version: int
    videoURL: str
    width: int

@typing.type_check_only
class CreativesList(typing_extensions.TypedDict, total=False):
    items: _list[Creative]
    kind: str
    nextPageToken: str
