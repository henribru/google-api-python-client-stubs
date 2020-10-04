import typing

import typing_extensions
@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str
    status: str

@typing.type_check_only
class Accounts(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Account]
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
    items: typing.List[AdClient]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AdCode(typing_extensions.TypedDict, total=False):
    adCode: str
    kind: str

@typing.type_check_only
class AdStyle(typing_extensions.TypedDict, total=False):
    colors: typing.Dict[str, typing.Any]
    corners: str
    font: typing.Dict[str, typing.Any]
    kind: str

@typing.type_check_only
class AdUnit(typing_extensions.TypedDict, total=False):
    code: str
    contentAdsSettings: typing.Dict[str, typing.Any]
    customStyle: AdStyle
    id: str
    kind: str
    mobileContentAdsSettings: typing.Dict[str, typing.Any]
    name: str
    status: str

@typing.type_check_only
class AdUnits(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[AdUnit]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AssociationSession(typing_extensions.TypedDict, total=False):
    accountId: str
    id: str
    kind: str
    productCodes: typing.List[str]
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
    items: typing.List[CustomChannel]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    averages: typing.List[str]
    headers: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    rows: typing.List[list]
    totalMatchedRows: str
    totals: typing.List[str]
    warnings: typing.List[str]

@typing.type_check_only
class UrlChannel(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    urlPattern: str

@typing.type_check_only
class UrlChannels(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[UrlChannel]
    kind: str
    nextPageToken: str
