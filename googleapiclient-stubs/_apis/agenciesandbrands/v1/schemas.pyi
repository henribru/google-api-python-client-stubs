import typing

_list = list

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    fixed: FixedDateRange
    relative: typing.Literal[
        "RELATIVE_DATE_RANGE_UNSPECIFIED",
        "TODAY",
        "YESTERDAY",
        "THIS_WEEK_TO_DATE",
        "THIS_WEEK_TO_YESTERDAY",
        "THIS_MONTH_TO_DATE",
        "THIS_MONTH_TO_YESTERDAY",
        "THIS_QUARTER_TO_DATE",
        "THIS_QUARTER_TO_YESTERDAY",
        "THIS_YEAR_TO_DATE",
        "THIS_YEAR_TO_YESTERDAY",
        "LAST_WEEK",
        "LAST_WEEK_STARTING_SUNDAY",
        "LAST_MONTH",
        "LAST_QUARTER",
        "LAST_YEAR",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_60_DAYS",
        "LAST_90_DAYS",
        "LAST_93_DAYS",
        "LAST_180_DAYS",
        "LAST_360_DAYS",
        "LAST_365_DAYS",
        "LAST_3_MONTHS",
        "LAST_6_MONTHS",
        "LAST_12_MONTHS",
        "ALL_AVAILABLE",
    ]

@typing.type_check_only
class DoubleList(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchReportResultRowsResponse(typing.TypedDict, total=False):
    dateRanges: _list[FixedDateRange]
    nextPageToken: str
    rows: _list[Row]
    runTime: str
    totalRowCount: int

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    dimension: typing.Literal[
        "DIMENSION_UNSPECIFIED",
        "ADVERTISER_DOMAIN",
        "AGENCY_ACCOUNT_ID",
        "AGENCY_ACCOUNT_NAME",
        "BID_FILTERING_REASON",
        "BID_FILTERING_REASON_NAME",
        "BUYER_SDK",
        "CAMPAIGN_ID",
        "CAMPAIGN_NAME",
        "COUNTRY",
        "CREATIVE_FORMAT",
        "CREATIVE_ID",
        "CREATIVE_POLICIES",
        "CREATIVE_POLICIES_NAME",
        "CREATIVE_SIZE",
        "CURATION_DATA_SEGMENT_ID",
        "CURATION_PARTNER_NAME",
        "CURATOR_FEE_TYPE",
        "DATE",
        "DEAL_ID",
        "DEAL_NAME",
        "DETECTED_ADVERTISER_NAME",
        "DSP_NAME",
        "DSP_SEAT_ID",
        "ENVIRONMENT",
        "ENVIRONMENT_NAME",
        "GMA_SDK",
        "HOUR",
        "MOBILE_APP_ID",
        "MOBILE_APP_NAME",
        "MOBILE_OS",
        "MONTH",
        "PACKAGE_FEE_VISIBILITY",
        "PLACEMENT_ID",
        "PLATFORM",
        "PUBLISHER_DOMAIN",
        "PUBLISHER_ID",
        "PUBLISHER_NAME",
        "PUBLISHER_PROTECTIONS",
        "PUBLISHER_PROTECTIONS_NAME",
        "SELLER_AUTHORIZATION",
        "SELLER_AUTHORIZATION_NAME",
        "SUPPLY_PATH_TYPE",
        "SUPPLY_PATH_TYPE_NAME",
        "TRANSACTION_TYPE",
        "VAST_ERROR_CODE",
        "WEEK",
    ]
    metric: typing.Literal[
        "METRIC_UNSPECIFIED",
        "ACTIVE_VIEW_MEASURABILITY_RATE",
        "ACTIVE_VIEW_MEASURABLE",
        "ACTIVE_VIEW_VIEWABILITY_RATE",
        "ACTIVE_VIEW_VIEWABLE",
        "AUCTIONS_WON",
        "BIDS",
        "BIDS_IN_AUCTION",
        "CLICKS",
        "CPC",
        "CPM",
        "CURATION_PARTNER_FEE",
        "DISCOUNT_AMOUNT",
        "EFFECTIVE_DISCOUNT_RATE",
        "ENGAGED_VIEWS",
        "IMPRESSIONS",
        "PRE_DISCOUNT_SPEND",
        "PRE_DISCOUNT_SPEND_WITHOUT_CURATION_PARTNER_FEE",
        "REACHED_QUERIES",
        "SPEND",
        "SPEND_WITHOUT_CURATION_PARTNER_FEE",
        "VAST_ERROR_COUNT",
        "VIDEO_COMPLETE",
        "VIDEO_FIRST_QUARTILE",
        "VIDEO_MIDPOINT",
        "VIDEO_START",
        "VIDEO_THIRD_QUARTILE",
        "VIDEO_VTR",
    ]

@typing.type_check_only
class FieldFilter(typing.TypedDict, total=False):
    field: Field
    operation: typing.Literal[
        "IN",
        "NOT_IN",
        "CONTAINS",
        "NOT_CONTAINS",
        "LESS_THAN",
        "LESS_THAN_EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_EQUALS",
        "BETWEEN",
        "MATCHES",
        "NOT_MATCHES",
    ]
    values: _list[ReportValue]

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    andFilter: FilterList
    fieldFilter: FieldFilter
    notFilter: Filter
    orFilter: FilterList

@typing.type_check_only
class FilterList(typing.TypedDict, total=False):
    filters: _list[Filter]

@typing.type_check_only
class FixedDateRange(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class IntList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ListReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]
    totalSize: int

@typing.type_check_only
class MetricValueGroup(typing.TypedDict, total=False):
    primaryValues: _list[ReportValue]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Report(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    locale: str
    name: str
    reportDefinition: ReportDefinition
    reportId: str
    updateTime: str

@typing.type_check_only
class ReportDefinition(typing.TypedDict, total=False):
    currencyCode: str
    dateRange: DateRange
    dimensions: _list[
        typing.Literal[
            "DIMENSION_UNSPECIFIED",
            "ADVERTISER_DOMAIN",
            "AGENCY_ACCOUNT_ID",
            "AGENCY_ACCOUNT_NAME",
            "BID_FILTERING_REASON",
            "BID_FILTERING_REASON_NAME",
            "BUYER_SDK",
            "CAMPAIGN_ID",
            "CAMPAIGN_NAME",
            "COUNTRY",
            "CREATIVE_FORMAT",
            "CREATIVE_ID",
            "CREATIVE_POLICIES",
            "CREATIVE_POLICIES_NAME",
            "CREATIVE_SIZE",
            "CURATION_DATA_SEGMENT_ID",
            "CURATION_PARTNER_NAME",
            "CURATOR_FEE_TYPE",
            "DATE",
            "DEAL_ID",
            "DEAL_NAME",
            "DETECTED_ADVERTISER_NAME",
            "DSP_NAME",
            "DSP_SEAT_ID",
            "ENVIRONMENT",
            "ENVIRONMENT_NAME",
            "GMA_SDK",
            "HOUR",
            "MOBILE_APP_ID",
            "MOBILE_APP_NAME",
            "MOBILE_OS",
            "MONTH",
            "PACKAGE_FEE_VISIBILITY",
            "PLACEMENT_ID",
            "PLATFORM",
            "PUBLISHER_DOMAIN",
            "PUBLISHER_ID",
            "PUBLISHER_NAME",
            "PUBLISHER_PROTECTIONS",
            "PUBLISHER_PROTECTIONS_NAME",
            "SELLER_AUTHORIZATION",
            "SELLER_AUTHORIZATION_NAME",
            "SUPPLY_PATH_TYPE",
            "SUPPLY_PATH_TYPE_NAME",
            "TRANSACTION_TYPE",
            "VAST_ERROR_CODE",
            "WEEK",
        ]
    ]
    filters: _list[Filter]
    metrics: _list[
        typing.Literal[
            "METRIC_UNSPECIFIED",
            "ACTIVE_VIEW_MEASURABILITY_RATE",
            "ACTIVE_VIEW_MEASURABLE",
            "ACTIVE_VIEW_VIEWABILITY_RATE",
            "ACTIVE_VIEW_VIEWABLE",
            "AUCTIONS_WON",
            "BIDS",
            "BIDS_IN_AUCTION",
            "CLICKS",
            "CPC",
            "CPM",
            "CURATION_PARTNER_FEE",
            "DISCOUNT_AMOUNT",
            "EFFECTIVE_DISCOUNT_RATE",
            "ENGAGED_VIEWS",
            "IMPRESSIONS",
            "PRE_DISCOUNT_SPEND",
            "PRE_DISCOUNT_SPEND_WITHOUT_CURATION_PARTNER_FEE",
            "REACHED_QUERIES",
            "SPEND",
            "SPEND_WITHOUT_CURATION_PARTNER_FEE",
            "VAST_ERROR_COUNT",
            "VIDEO_COMPLETE",
            "VIDEO_FIRST_QUARTILE",
            "VIDEO_MIDPOINT",
            "VIDEO_START",
            "VIDEO_THIRD_QUARTILE",
            "VIDEO_VTR",
        ]
    ]
    sorts: _list[Sort]
    timeZone: str
    timeZoneSource: typing.Literal[
        "TIME_ZONE_SOURCE_UNSPECIFIED", "AD_EXCHANGE", "UTC", "PROVIDED", "AGENCY"
    ]

@typing.type_check_only
class ReportValue(typing.TypedDict, total=False):
    boolValue: bool
    bytesValue: str
    doubleListValue: DoubleList
    doubleValue: float
    intListValue: IntList
    intValue: str
    stringListValue: StringList
    stringValue: str

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    dimensionValues: _list[ReportValue]
    metricValueGroups: _list[MetricValueGroup]

@typing.type_check_only
class RunReportMetadata(typing.TypedDict, total=False):
    percentComplete: int
    report: str

@typing.type_check_only
class RunReportRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RunReportResponse(typing.TypedDict, total=False):
    reportResult: str

@typing.type_check_only
class Sort(typing.TypedDict, total=False):
    descending: bool
    field: Field

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringList(typing.TypedDict, total=False):
    values: _list[str]
