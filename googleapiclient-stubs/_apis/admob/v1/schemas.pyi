import typing

import typing_extensions

class LocalizationSettings(typing_extensions.TypedDict, total=False):
    languageCode: str
    currencyCode: str

class NetworkReportSpecSortCondition(typing_extensions.TypedDict, total=False):
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
    ]

class ListPublisherAccountsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    account: typing.List[PublisherAccount]

class Date(typing_extensions.TypedDict, total=False):
    month: int
    year: int
    day: int

class GenerateNetworkReportRequest(typing_extensions.TypedDict, total=False):
    reportSpec: NetworkReportSpec

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
    ]
    order: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
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

class MediationReportSpec(typing_extensions.TypedDict, total=False):
    timeZone: str
    maxReportRows: int
    metrics: typing.List[str]
    dimensionFilters: typing.List[MediationReportSpecDimensionFilter]
    localizationSettings: LocalizationSettings
    dimensions: typing.List[str]
    dateRange: DateRange
    sortConditions: typing.List[MediationReportSpecSortCondition]

class GenerateMediationReportResponse(typing_extensions.TypedDict, total=False):
    row: ReportRow
    footer: ReportFooter
    header: ReportHeader

class GenerateNetworkReportResponse(typing_extensions.TypedDict, total=False):
    header: ReportHeader
    footer: ReportFooter
    row: ReportRow

class GenerateMediationReportRequest(typing_extensions.TypedDict, total=False):
    reportSpec: MediationReportSpec

class DateRange(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date

class MediationReportSpecDimensionFilter(typing_extensions.TypedDict, total=False):
    matchesAny: StringList
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
    ]

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
    ]
    matchesAny: StringList

class ReportRowDimensionValue(typing_extensions.TypedDict, total=False):
    displayLabel: str
    value: str

class NetworkReportSpec(typing_extensions.TypedDict, total=False):
    timeZone: str
    dimensionFilters: typing.List[NetworkReportSpecDimensionFilter]
    dateRange: DateRange
    maxReportRows: int
    localizationSettings: LocalizationSettings
    sortConditions: typing.List[NetworkReportSpecSortCondition]
    metrics: typing.List[str]
    dimensions: typing.List[str]

class ReportHeader(typing_extensions.TypedDict, total=False):
    localizationSettings: LocalizationSettings
    dateRange: DateRange
    reportingTimeZone: str

class ReportRowMetricValue(typing_extensions.TypedDict, total=False):
    doubleValue: float
    microsValue: str
    integerValue: str

class PublisherAccount(typing_extensions.TypedDict, total=False):
    name: str
    publisherId: str
    currencyCode: str
    reportingTimeZone: str

class ReportRow(typing_extensions.TypedDict, total=False):
    dimensionValues: typing.Dict[str, typing.Any]
    metricValues: typing.Dict[str, typing.Any]

class StringList(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class ReportWarning(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE",
        "DATA_DELAYED",
        "OTHER",
        "REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY",
    ]
    description: str

class ReportFooter(typing_extensions.TypedDict, total=False):
    matchingRowCount: str
    warnings: typing.List[ReportWarning]
