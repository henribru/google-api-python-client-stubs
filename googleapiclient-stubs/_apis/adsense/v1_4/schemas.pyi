import typing

import typing_extensions
@typing.type_check_only
class Account(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Accounts(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Account]
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
    items: typing.List[AdClient]
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
    colors: typing.Dict[str, typing.Any]
    corners: str
    font: typing.Dict[str, typing.Any]
    kind: str

@typing.type_check_only
class AdUnit(typing_extensions.TypedDict, total=False):
    code: str
    contentAdsSettings: typing.Dict[str, typing.Any]
    customStyle: AdStyle
    feedAdsSettings: typing.Dict[str, typing.Any]
    id: str
    kind: str
    mobileContentAdsSettings: typing.Dict[str, typing.Any]
    name: str
    savedStyleId: str
    status: str

@typing.type_check_only
class AdUnits(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[AdUnit]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AdsenseReportsGenerateResponse(typing_extensions.TypedDict, total=False):
    averages: typing.List[str]
    endDate: str
    headers: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    rows: typing.List[list]
    startDate: str
    totalMatchedRows: str
    totals: typing.List[str]
    warnings: typing.List[str]

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
    items: typing.List[Alert]
    kind: str

@typing.type_check_only
class CustomChannel(typing_extensions.TypedDict, total=False):
    code: str
    id: str
    kind: str
    name: str
    targetingInfo: typing.Dict[str, typing.Any]

@typing.type_check_only
class CustomChannels(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[CustomChannel]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    items: typing.List[ReportingMetadataEntry]
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
    items: typing.List[Payment]
    kind: str

@typing.type_check_only
class ReportingMetadataEntry(typing_extensions.TypedDict, total=False):
    compatibleDimensions: typing.List[str]
    compatibleMetrics: typing.List[str]
    id: str
    kind: str
    requiredDimensions: typing.List[str]
    requiredMetrics: typing.List[str]
    supportedProducts: typing.List[str]

@typing.type_check_only
class SavedAdStyle(typing_extensions.TypedDict, total=False):
    adStyle: AdStyle
    id: str
    kind: str
    name: str

@typing.type_check_only
class SavedAdStyles(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[SavedAdStyle]
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
    items: typing.List[SavedReport]
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
    items: typing.List[UrlChannel]
    kind: str
    nextPageToken: str
