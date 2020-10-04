import typing

import typing_extensions
@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    bidderLocation: typing.List[typing.Dict[str, typing.Any]]
    cookieMatchingNid: str
    cookieMatchingUrl: str
    id: int
    kind: str
    maximumActiveCreatives: int
    maximumTotalQps: int
    numberActiveCreatives: int

@typing.type_check_only
class AccountsList(typing_extensions.TypedDict, total=False):
    items: typing.List[Account]
    kind: str

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    HTMLSnippet: str
    accountId: int
    advertiserId: typing.List[str]
    advertiserName: str
    agencyId: str
    apiUploadTimestamp: str
    attribute: typing.List[int]
    buyerCreativeId: str
    clickThroughUrl: typing.List[str]
    corrections: typing.List[typing.Dict[str, typing.Any]]
    disapprovalReasons: typing.List[typing.Dict[str, typing.Any]]
    filteringReasons: typing.Dict[str, typing.Any]
    height: int
    impressionTrackingUrl: typing.List[str]
    kind: str
    productCategories: typing.List[int]
    restrictedCategories: typing.List[int]
    sensitiveCategories: typing.List[int]
    status: str
    vendorType: typing.List[int]
    version: int
    videoURL: str
    width: int

@typing.type_check_only
class CreativesList(typing_extensions.TypedDict, total=False):
    items: typing.List[Creative]
    kind: str
    nextPageToken: str
