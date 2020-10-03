import typing

import typing_extensions

class Alert(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    isDismissible: bool
    message: str
    severity: str
    type: str

class AdClients(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    items: typing.List[AdClient]
    etag: str

class AdUnit(typing_extensions.TypedDict, total=False):
    customStyle: AdStyle
    feedAdsSettings: typing.Dict[str, typing.Any]
    contentAdsSettings: typing.Dict[str, typing.Any]
    name: str
    status: str
    mobileContentAdsSettings: typing.Dict[str, typing.Any]
    id: str
    kind: str
    savedStyleId: str
    code: str

class UrlChannels(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    items: typing.List[UrlChannel]
    nextPageToken: str

class SavedReports(typing_extensions.TypedDict, total=False):
    items: typing.List[SavedReport]
    kind: str
    nextPageToken: str
    etag: str

class Alerts(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[Alert]

class CustomChannels(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    nextPageToken: str
    items: typing.List[CustomChannel]

class SavedAdStyles(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    items: typing.List[SavedAdStyle]
    nextPageToken: str

class AdCode(typing_extensions.TypedDict, total=False):
    ampBody: str
    adCode: str
    kind: str
    ampHead: str

class CustomChannel(typing_extensions.TypedDict, total=False):
    targetingInfo: typing.Dict[str, typing.Any]
    name: str
    code: str
    kind: str
    id: str

class SavedReport(typing_extensions.TypedDict, total=False):
    name: str
    kind: str
    id: str

class Payment(typing_extensions.TypedDict, total=False):
    paymentDate: str
    id: str
    kind: str
    paymentAmount: str
    paymentAmountCurrencyCode: str

class UrlChannel(typing_extensions.TypedDict, total=False):
    kind: str
    urlPattern: str
    id: str

class Metadata(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[ReportingMetadataEntry]

class SavedAdStyle(typing_extensions.TypedDict, total=False):
    name: str
    adStyle: AdStyle
    kind: str
    id: str

class Payments(typing_extensions.TypedDict, total=False):
    items: typing.List[Payment]
    kind: str

class Accounts(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    items: typing.List[Account]
    nextPageToken: str

class ReportingMetadataEntry(typing_extensions.TypedDict, total=False):
    requiredMetrics: typing.List[str]
    supportedProducts: typing.List[str]
    compatibleDimensions: typing.List[str]
    compatibleMetrics: typing.List[str]
    id: str
    kind: str
    requiredDimensions: typing.List[str]

class AdsenseReportsGenerateResponse(typing_extensions.TypedDict, total=False):
    warnings: typing.List[str]
    averages: typing.List[str]
    kind: str
    endDate: str
    totalMatchedRows: str
    rows: typing.List[list]
    totals: typing.List[str]
    headers: typing.List[typing.Dict[str, typing.Any]]
    startDate: str

class Account(typing.Dict[str, typing.Any]): ...

class AdUnits(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[AdUnit]
    etag: str
    kind: str

class AdStyle(typing_extensions.TypedDict, total=False):
    kind: str
    corners: str
    font: typing.Dict[str, typing.Any]
    colors: typing.Dict[str, typing.Any]

class AdClient(typing_extensions.TypedDict, total=False):
    id: str
    supportsReporting: bool
    arcOptIn: bool
    productCode: str
    kind: str
