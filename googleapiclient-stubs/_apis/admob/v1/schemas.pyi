import typing

_list = list

@typing.type_check_only
class AdUnit(typing.TypedDict, total=False):
    adFormat: str
    adTypes: _list[str]
    adUnitId: str
    appId: str
    displayName: str
    name: str

@typing.type_check_only
class App(typing.TypedDict, total=False):
    appApprovalState: typing.Literal[
        "APP_APPROVAL_STATE_UNSPECIFIED", "ACTION_REQUIRED", "IN_REVIEW", "APPROVED"
    ]
    appId: str
    linkedAppInfo: AppLinkedAppInfo
    manualAppInfo: AppManualAppInfo
    name: str
    platform: str

@typing.type_check_only
class AppLinkedAppInfo(typing.TypedDict, total=False):
    appStoreId: str
    displayName: str

@typing.type_check_only
class AppManualAppInfo(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class GenerateMediationReportRequest(typing.TypedDict, total=False):
    reportSpec: MediationReportSpec

@typing.type_check_only
class GenerateMediationReportResponse(typing.TypedDict, total=False):
    footer: ReportFooter
    header: ReportHeader
    row: ReportRow

@typing.type_check_only
class GenerateNetworkReportRequest(typing.TypedDict, total=False):
    reportSpec: NetworkReportSpec

@typing.type_check_only
class GenerateNetworkReportResponse(typing.TypedDict, total=False):
    footer: ReportFooter
    header: ReportHeader
    row: ReportRow

@typing.type_check_only
class ListAdUnitsResponse(typing.TypedDict, total=False):
    adUnits: _list[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListAppsResponse(typing.TypedDict, total=False):
    apps: _list[App]
    nextPageToken: str

@typing.type_check_only
class ListPublisherAccountsResponse(typing.TypedDict, total=False):
    account: _list[PublisherAccount]
    nextPageToken: str

@typing.type_check_only
class LocalizationSettings(typing.TypedDict, total=False):
    currencyCode: str
    languageCode: str

@typing.type_check_only
class MediationReportSpec(typing.TypedDict, total=False):
    dateRange: DateRange
    dimensionFilters: _list[MediationReportSpecDimensionFilter]
    dimensions: _list[
        typing.Literal[
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
    ]
    localizationSettings: LocalizationSettings
    maxReportRows: int
    metrics: _list[
        typing.Literal[
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
    ]
    sortConditions: _list[MediationReportSpecSortCondition]
    timeZone: str

@typing.type_check_only
class MediationReportSpecDimensionFilter(typing.TypedDict, total=False):
    dimension: typing.Literal[
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
class MediationReportSpecSortCondition(typing.TypedDict, total=False):
    dimension: typing.Literal[
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
    metric: typing.Literal[
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
    order: typing.Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class NetworkReportSpec(typing.TypedDict, total=False):
    dateRange: DateRange
    dimensionFilters: _list[NetworkReportSpecDimensionFilter]
    dimensions: _list[
        typing.Literal[
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
    ]
    localizationSettings: LocalizationSettings
    maxReportRows: int
    metrics: _list[
        typing.Literal[
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
    ]
    sortConditions: _list[NetworkReportSpecSortCondition]
    timeZone: str

@typing.type_check_only
class NetworkReportSpecDimensionFilter(typing.TypedDict, total=False):
    dimension: typing.Literal[
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
class NetworkReportSpecSortCondition(typing.TypedDict, total=False):
    dimension: typing.Literal[
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
    metric: typing.Literal[
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
    order: typing.Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class PublisherAccount(typing.TypedDict, total=False):
    currencyCode: str
    name: str
    publisherId: str
    reportingTimeZone: str

@typing.type_check_only
class ReportFooter(typing.TypedDict, total=False):
    matchingRowCount: str
    warnings: _list[ReportWarning]

@typing.type_check_only
class ReportHeader(typing.TypedDict, total=False):
    dateRange: DateRange
    localizationSettings: LocalizationSettings
    reportingTimeZone: str

@typing.type_check_only
class ReportRow(typing.TypedDict, total=False):
    dimensionValues: dict[str, typing.Any]
    metricValues: dict[str, typing.Any]

@typing.type_check_only
class ReportRowDimensionValue(typing.TypedDict, total=False):
    displayLabel: str
    value: str

@typing.type_check_only
class ReportRowMetricValue(typing.TypedDict, total=False):
    doubleValue: float
    integerValue: str
    microsValue: str

@typing.type_check_only
class ReportWarning(typing.TypedDict, total=False):
    description: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE",
        "DATA_DELAYED",
        "OTHER",
        "REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY",
    ]

@typing.type_check_only
class StringList(typing.TypedDict, total=False):
    values: _list[str]
