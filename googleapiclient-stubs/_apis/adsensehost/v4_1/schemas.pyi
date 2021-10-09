import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str
    status: str

@typing.type_check_only
class Accounts(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Account]
    kind: str

@typing.type_check_only
class AdClient(typing_extensions.TypedDict, total=False):
    arcOptIn: bool
    id: str
    kind: str
    productCode: str
    supportsReporting: bool

@typing.type_check_only
class AdClients(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[AdClient]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AdCode(typing_extensions.TypedDict, total=False):
    adCode: str
    kind: str

@typing.type_check_only
class AdStyle(typing_extensions.TypedDict, total=False):
    colors: dict[str, typing.Any]
    corners: str
    font: dict[str, typing.Any]
    kind: str

@typing.type_check_only
class AdUnit(typing_extensions.TypedDict, total=False):
    code: str
    contentAdsSettings: dict[str, typing.Any]
    customStyle: AdStyle
    id: str
    kind: str
    mobileContentAdsSettings: dict[str, typing.Any]
    name: str
    status: str

@typing.type_check_only
class AdUnits(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[AdUnit]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AssociationSession(typing_extensions.TypedDict, total=False):
    accountId: str
    id: str
    kind: str
    productCodes: _list[str]
    redirectUrl: str
    status: str
    userLocale: str
    websiteLocale: str
    websiteUrl: str

@typing.type_check_only
class CustomChannel(typing_extensions.TypedDict, total=False):
    code: str
    id: str
    kind: str
    name: str

@typing.type_check_only
class CustomChannels(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[CustomChannel]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    averages: _list[str]
    headers: _list[dict[str, typing.Any]]
    kind: str
    rows: _list[list]
    totalMatchedRows: str
    totals: _list[str]
    warnings: _list[str]

@typing.type_check_only
class UrlChannel(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    urlPattern: str

@typing.type_check_only
class UrlChannels(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[UrlChannel]
    kind: str
    nextPageToken: str
