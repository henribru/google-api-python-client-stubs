import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(dict[str, typing.Any]): ...

@typing.type_check_only
class Accounts(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Account]
    kind: str
    nextPageToken: str

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
    ampBody: str
    ampHead: str
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
    feedAdsSettings: dict[str, typing.Any]
    id: str
    kind: str
    mobileContentAdsSettings: dict[str, typing.Any]
    name: str
    savedStyleId: str
    status: str

@typing.type_check_only
class AdUnits(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[AdUnit]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AdsenseReportsGenerateResponse(typing_extensions.TypedDict, total=False):
    averages: _list[str]
    endDate: str
    headers: _list[dict[str, typing.Any]]
    kind: str
    rows: _list[list]
    startDate: str
    totalMatchedRows: str
    totals: _list[str]
    warnings: _list[str]

@typing.type_check_only
class Alert(typing_extensions.TypedDict, total=False):
    id: str
    isDismissible: bool
    kind: str
    message: str
    severity: str
    type: str

@typing.type_check_only
class Alerts(typing_extensions.TypedDict, total=False):
    items: _list[Alert]
    kind: str

@typing.type_check_only
class CustomChannel(typing_extensions.TypedDict, total=False):
    code: str
    id: str
    kind: str
    name: str
    targetingInfo: dict[str, typing.Any]

@typing.type_check_only
class CustomChannels(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[CustomChannel]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    items: _list[ReportingMetadataEntry]
    kind: str

@typing.type_check_only
class Payment(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    paymentAmount: str
    paymentAmountCurrencyCode: str
    paymentDate: str

@typing.type_check_only
class Payments(typing_extensions.TypedDict, total=False):
    items: _list[Payment]
    kind: str

@typing.type_check_only
class ReportingMetadataEntry(typing_extensions.TypedDict, total=False):
    compatibleDimensions: _list[str]
    compatibleMetrics: _list[str]
    id: str
    kind: str
    requiredDimensions: _list[str]
    requiredMetrics: _list[str]
    supportedProducts: _list[str]

@typing.type_check_only
class SavedAdStyle(typing_extensions.TypedDict, total=False):
    adStyle: AdStyle
    id: str
    kind: str
    name: str

@typing.type_check_only
class SavedAdStyles(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[SavedAdStyle]
    kind: str
    nextPageToken: str

@typing.type_check_only
class SavedReport(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class SavedReports(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[SavedReport]
    kind: str
    nextPageToken: str

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
