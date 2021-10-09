import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdUnit(typing_extensions.TypedDict, total=False):
    adFormat: str
    adTypes: _list[str]
    adUnitId: str
    appId: str
    displayName: str
    name: str

@typing.type_check_only
class App(typing_extensions.TypedDict, total=False):
    appId: str
    linkedAppInfo: AppLinkedAppInfo
    manualAppInfo: AppManualAppInfo
    name: str
    platform: str

@typing.type_check_only
class AppLinkedAppInfo(typing_extensions.TypedDict, total=False):
    appStoreId: str
    displayName: str

@typing.type_check_only
class AppManualAppInfo(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateRange(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class GenerateMediationReportRequest(typing_extensions.TypedDict, total=False):
    reportSpec: MediationReportSpec

@typing.type_check_only
class GenerateMediationReportResponse(typing_extensions.TypedDict, total=False):
    footer: ReportFooter
    header: ReportHeader
    row: ReportRow

@typing.type_check_only
class GenerateNetworkReportRequest(typing_extensions.TypedDict, total=False):
    reportSpec: NetworkReportSpec

@typing.type_check_only
class GenerateNetworkReportResponse(typing_extensions.TypedDict, total=False):
    footer: ReportFooter
    header: ReportHeader
    row: ReportRow

@typing.type_check_only
class ListAdUnitsResponse(typing_extensions.TypedDict, total=False):
    adUnits: _list[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListAppsResponse(typing_extensions.TypedDict, total=False):
    apps: _list[App]
    nextPageToken: str

@typing.type_check_only
class ListPublisherAccountsResponse(typing_extensions.TypedDict, total=False):
    account: _list[PublisherAccount]
    nextPageToken: str

@typing.type_check_only
class LocalizationSettings(typing_extensions.TypedDict, total=False):
    currencyCode: str
    languageCode: str

@typing.type_check_only
class MediationReportSpec(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    dimensionFilters: _list[MediationReportSpecDimensionFilter]
    dimensions: _list[str]
    localizationSettings: LocalizationSettings
    maxReportRows: int
    metrics: _list[str]
    sortConditions: _list[MediationReportSpecSortCondition]
    timeZone: str

@typing.type_check_only
class MediationReportSpecDimensionFilter(typing_extensions.TypedDict, total=False):
    dimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_SOURCE",
        "AD_SOURCE_INSTANCE",
        "AD_UNIT",
        "APP",
        "MEDIATION_GROUP",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    matchesAny: StringList

@typing.type_check_only
class MediationReportSpecSortCondition(typing_extensions.TypedDict, total=False):
    dimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_SOURCE",
        "AD_SOURCE_INSTANCE",
        "AD_UNIT",
        "APP",
        "MEDIATION_GROUP",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    metric: typing_extensions.Literal[
        "METRIC_UNSPECIFIED",
        "AD_REQUESTS",
        "CLICKS",
        "ESTIMATED_EARNINGS",
        "IMPRESSIONS",
        "IMPRESSION_CTR",
        "MATCHED_REQUESTS",
        "MATCH_RATE",
        "OBSERVED_ECPM",
    ]
    order: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]

@typing.type_check_only
class NetworkReportSpec(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    dimensionFilters: _list[NetworkReportSpecDimensionFilter]
    dimensions: _list[str]
    localizationSettings: LocalizationSettings
    maxReportRows: int
    metrics: _list[str]
    sortConditions: _list[NetworkReportSpecSortCondition]
    timeZone: str

@typing.type_check_only
class NetworkReportSpecDimensionFilter(typing_extensions.TypedDict, total=False):
    dimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_UNIT",
        "APP",
        "AD_TYPE",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    matchesAny: StringList

@typing.type_check_only
class NetworkReportSpecSortCondition(typing_extensions.TypedDict, total=False):
    dimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_UNIT",
        "APP",
        "AD_TYPE",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    metric: typing_extensions.Literal[
        "METRIC_UNSPECIFIED",
        "AD_REQUESTS",
        "CLICKS",
        "ESTIMATED_EARNINGS",
        "IMPRESSIONS",
        "IMPRESSION_CTR",
        "IMPRESSION_RPM",
        "MATCHED_REQUESTS",
        "MATCH_RATE",
        "SHOW_RATE",
    ]
    order: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]

@typing.type_check_only
class PublisherAccount(typing_extensions.TypedDict, total=False):
    currencyCode: str
    name: str
    publisherId: str
    reportingTimeZone: str

@typing.type_check_only
class ReportFooter(typing_extensions.TypedDict, total=False):
    matchingRowCount: str
    warnings: _list[ReportWarning]

@typing.type_check_only
class ReportHeader(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    localizationSettings: LocalizationSettings
    reportingTimeZone: str

@typing.type_check_only
class ReportRow(typing_extensions.TypedDict, total=False):
    dimensionValues: dict[str, typing.Any]
    metricValues: dict[str, typing.Any]

@typing.type_check_only
class ReportRowDimensionValue(typing_extensions.TypedDict, total=False):
    displayLabel: str
    value: str

@typing.type_check_only
class ReportRowMetricValue(typing_extensions.TypedDict, total=False):
    doubleValue: float
    integerValue: str
    microsValue: str

@typing.type_check_only
class ReportWarning(typing_extensions.TypedDict, total=False):
    description: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE",
        "DATA_DELAYED",
        "OTHER",
        "REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY",
    ]

@typing.type_check_only
class StringList(typing_extensions.TypedDict, total=False):
    values: _list[str]
