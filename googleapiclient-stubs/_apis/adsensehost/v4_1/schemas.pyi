import typing

import typing_extensions

class UrlChannels(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    items: typing.List[UrlChannel]
    etag: str

class CustomChannel(typing_extensions.TypedDict, total=False):
    code: str
    name: str
    id: str
    kind: str

class Accounts(typing_extensions.TypedDict, total=False):
    items: typing.List[Account]
    kind: str
    etag: str

class AdCode(typing_extensions.TypedDict, total=False):
    adCode: str
    kind: str

class AdClients(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[AdClient]
    etag: str
    nextPageToken: str

class CustomChannels(typing_extensions.TypedDict, total=False):
    etag: str
    nextPageToken: str
    items: typing.List[CustomChannel]
    kind: str

class Report(typing_extensions.TypedDict, total=False):
    kind: str
    warnings: typing.List[str]
    rows: typing.List[list]
    headers: typing.List[typing.Dict[str, typing.Any]]
    totals: typing.List[str]
    totalMatchedRows: str
    averages: typing.List[str]

class AdClient(typing_extensions.TypedDict, total=False):
    supportsReporting: bool
    id: str
    kind: str
    productCode: str
    arcOptIn: bool

class Account(typing_extensions.TypedDict, total=False):
    kind: str
    id: str
    status: str
    name: str

class AdUnit(typing_extensions.TypedDict, total=False):
    code: str
    customStyle: AdStyle
    contentAdsSettings: typing.Dict[str, typing.Any]
    mobileContentAdsSettings: typing.Dict[str, typing.Any]
    name: str
    id: str
    status: str
    kind: str

class AssociationSession(typing_extensions.TypedDict, total=False):
    kind: str
    status: str
    redirectUrl: str
    websiteLocale: str
    userLocale: str
    accountId: str
    websiteUrl: str
    productCodes: typing.List[str]
    id: str

class AdStyle(typing_extensions.TypedDict, total=False):
    colors: typing.Dict[str, typing.Any]
    corners: str
    kind: str
    font: typing.Dict[str, typing.Any]

class AdUnits(typing_extensions.TypedDict, total=False):
    items: typing.List[AdUnit]
    kind: str
    etag: str
    nextPageToken: str

class UrlChannel(typing_extensions.TypedDict, total=False):
    urlPattern: str
    kind: str
    id: str
