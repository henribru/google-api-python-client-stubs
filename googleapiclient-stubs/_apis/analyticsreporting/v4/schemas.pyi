import typing

import typing_extensions

_list = list

@typing.type_check_only
class Activity(typing_extensions.TypedDict, total=False):
    activityTime: str
    activityType: typing_extensions.Literal[
        "ACTIVITY_TYPE_UNSPECIFIED",
        "PAGEVIEW",
        "SCREENVIEW",
        "GOAL",
        "ECOMMERCE",
        "EVENT",
    ]
    appview: ScreenviewData
    campaign: str
    channelGrouping: str
    customDimension: _list[CustomDimension]
    ecommerce: EcommerceData
    event: EventData
    goals: GoalSetData
    hostname: str
    keyword: str
    landingPagePath: str
    medium: str
    pageview: PageviewData
    source: str

@typing.type_check_only
class Cohort(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    name: str
    type: typing_extensions.Literal["UNSPECIFIED_COHORT_TYPE", "FIRST_VISIT_DATE"]

@typing.type_check_only
class CohortGroup(typing_extensions.TypedDict, total=False):
    cohorts: _list[Cohort]
    lifetimeValue: bool

@typing.type_check_only
class ColumnHeader(typing_extensions.TypedDict, total=False):
    dimensions: _list[str]
    metricHeader: MetricHeader

@typing.type_check_only
class CustomDimension(typing_extensions.TypedDict, total=False):
    index: int
    value: str

@typing.type_check_only
class DateRange(typing_extensions.TypedDict, total=False):
    endDate: str
    startDate: str

@typing.type_check_only
class DateRangeValues(typing_extensions.TypedDict, total=False):
    pivotValueRegions: _list[PivotValueRegion]
    values: _list[str]

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    histogramBuckets: _list[str]
    name: str

AlternativeDimensionFilter = typing_extensions.TypedDict(
    "AlternativeDimensionFilter",
    {
        "caseSensitive": bool,
        "dimensionName": str,
        "expressions": _list[str],
        "not": bool,
        "operator": typing_extensions.Literal[
            "OPERATOR_UNSPECIFIED",
            "REGEXP",
            "BEGINS_WITH",
            "ENDS_WITH",
            "PARTIAL",
            "EXACT",
            "NUMERIC_EQUAL",
            "NUMERIC_GREATER_THAN",
            "NUMERIC_LESS_THAN",
            "IN_LIST",
        ],
    },
    total=False,
)

@typing.type_check_only
class DimensionFilter(AlternativeDimensionFilter): ...

@typing.type_check_only
class DimensionFilterClause(typing_extensions.TypedDict, total=False):
    filters: _list[DimensionFilter]
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "OR", "AND"]

@typing.type_check_only
class DynamicSegment(typing_extensions.TypedDict, total=False):
    name: str
    sessionSegment: SegmentDefinition
    userSegment: SegmentDefinition

@typing.type_check_only
class EcommerceData(typing_extensions.TypedDict, total=False):
    actionType: typing_extensions.Literal[
        "UNKNOWN",
        "CLICK",
        "DETAILS_VIEW",
        "ADD_TO_CART",
        "REMOVE_FROM_CART",
        "CHECKOUT",
        "PAYMENT",
        "REFUND",
        "CHECKOUT_OPTION",
    ]
    ecommerceType: typing_extensions.Literal[
        "ECOMMERCE_TYPE_UNSPECIFIED", "CLASSIC", "ENHANCED"
    ]
    products: _list[ProductData]
    transaction: TransactionData

@typing.type_check_only
class EventData(typing_extensions.TypedDict, total=False):
    eventAction: str
    eventCategory: str
    eventCount: str
    eventLabel: str
    eventValue: str

@typing.type_check_only
class GetReportsRequest(typing_extensions.TypedDict, total=False):
    reportRequests: _list[ReportRequest]
    useResourceQuotas: bool

@typing.type_check_only
class GetReportsResponse(typing_extensions.TypedDict, total=False):
    queryCost: int
    reports: _list[Report]
    resourceQuotasRemaining: ResourceQuotasRemaining

@typing.type_check_only
class GoalData(typing_extensions.TypedDict, total=False):
    goalCompletionLocation: str
    goalCompletions: str
    goalIndex: int
    goalName: str
    goalPreviousStep1: str
    goalPreviousStep2: str
    goalPreviousStep3: str
    goalValue: float

@typing.type_check_only
class GoalSetData(typing_extensions.TypedDict, total=False):
    goals: _list[GoalData]

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    alias: str
    expression: str
    formattingType: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "CURRENCY", "PERCENT", "TIME"
    ]

AlternativeMetricFilter = typing_extensions.TypedDict(
    "AlternativeMetricFilter",
    {
        "comparisonValue": str,
        "metricName": str,
        "not": bool,
        "operator": typing_extensions.Literal[
            "OPERATOR_UNSPECIFIED", "EQUAL", "LESS_THAN", "GREATER_THAN", "IS_MISSING"
        ],
    },
    total=False,
)

@typing.type_check_only
class MetricFilter(AlternativeMetricFilter): ...

@typing.type_check_only
class MetricFilterClause(typing_extensions.TypedDict, total=False):
    filters: _list[MetricFilter]
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "OR", "AND"]

@typing.type_check_only
class MetricHeader(typing_extensions.TypedDict, total=False):
    metricHeaderEntries: _list[MetricHeaderEntry]
    pivotHeaders: _list[PivotHeader]

@typing.type_check_only
class MetricHeaderEntry(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "CURRENCY", "PERCENT", "TIME"
    ]

@typing.type_check_only
class OrFiltersForSegment(typing_extensions.TypedDict, total=False):
    segmentFilterClauses: _list[SegmentFilterClause]

@typing.type_check_only
class OrderBy(typing_extensions.TypedDict, total=False):
    fieldName: str
    orderType: typing_extensions.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "VALUE",
        "DELTA",
        "SMART",
        "HISTOGRAM_BUCKET",
        "DIMENSION_AS_INTEGER",
    ]
    sortOrder: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]

@typing.type_check_only
class PageviewData(typing_extensions.TypedDict, total=False):
    pagePath: str
    pageTitle: str

@typing.type_check_only
class Pivot(typing_extensions.TypedDict, total=False):
    dimensionFilterClauses: _list[DimensionFilterClause]
    dimensions: _list[Dimension]
    maxGroupCount: int
    metrics: _list[Metric]
    startGroup: int

@typing.type_check_only
class PivotHeader(typing_extensions.TypedDict, total=False):
    pivotHeaderEntries: _list[PivotHeaderEntry]
    totalPivotGroupsCount: int

@typing.type_check_only
class PivotHeaderEntry(typing_extensions.TypedDict, total=False):
    dimensionNames: _list[str]
    dimensionValues: _list[str]
    metric: MetricHeaderEntry

@typing.type_check_only
class PivotValueRegion(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ProductData(typing_extensions.TypedDict, total=False):
    itemRevenue: float
    productName: str
    productQuantity: str
    productSku: str

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    columnHeader: ColumnHeader
    data: ReportData
    nextPageToken: str

@typing.type_check_only
class ReportData(typing_extensions.TypedDict, total=False):
    dataLastRefreshed: str
    emptyReason: str
    isDataGolden: bool
    maximums: _list[DateRangeValues]
    minimums: _list[DateRangeValues]
    rowCount: int
    rows: _list[ReportRow]
    samplesReadCounts: _list[str]
    samplingSpaceSizes: _list[str]
    totals: _list[DateRangeValues]

@typing.type_check_only
class ReportRequest(typing_extensions.TypedDict, total=False):
    cohortGroup: CohortGroup
    dateRanges: _list[DateRange]
    dimensionFilterClauses: _list[DimensionFilterClause]
    dimensions: _list[Dimension]
    filtersExpression: str
    hideTotals: bool
    hideValueRanges: bool
    includeEmptyRows: bool
    metricFilterClauses: _list[MetricFilterClause]
    metrics: _list[Metric]
    orderBys: _list[OrderBy]
    pageSize: int
    pageToken: str
    pivots: _list[Pivot]
    samplingLevel: typing_extensions.Literal[
        "SAMPLING_UNSPECIFIED", "DEFAULT", "SMALL", "LARGE"
    ]
    segments: _list[Segment]
    viewId: str

@typing.type_check_only
class ReportRow(typing_extensions.TypedDict, total=False):
    dimensions: _list[str]
    metrics: _list[DateRangeValues]

@typing.type_check_only
class ResourceQuotasRemaining(typing_extensions.TypedDict, total=False):
    dailyQuotaTokensRemaining: int
    hourlyQuotaTokensRemaining: int

@typing.type_check_only
class ScreenviewData(typing_extensions.TypedDict, total=False):
    appName: str
    mobileDeviceBranding: str
    mobileDeviceModel: str
    screenName: str

@typing.type_check_only
class SearchUserActivityRequest(typing_extensions.TypedDict, total=False):
    activityTypes: _list[str]
    dateRange: DateRange
    pageSize: int
    pageToken: str
    user: User
    viewId: str

@typing.type_check_only
class SearchUserActivityResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sampleRate: float
    sessions: _list[UserActivitySession]
    totalRows: int

@typing.type_check_only
class Segment(typing_extensions.TypedDict, total=False):
    dynamicSegment: DynamicSegment
    segmentId: str

@typing.type_check_only
class SegmentDefinition(typing_extensions.TypedDict, total=False):
    segmentFilters: _list[SegmentFilter]

@typing.type_check_only
class SegmentDimensionFilter(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    dimensionName: str
    expressions: _list[str]
    maxComparisonValue: str
    minComparisonValue: str
    operator: typing_extensions.Literal[
        "OPERATOR_UNSPECIFIED",
        "REGEXP",
        "BEGINS_WITH",
        "ENDS_WITH",
        "PARTIAL",
        "EXACT",
        "IN_LIST",
        "NUMERIC_LESS_THAN",
        "NUMERIC_GREATER_THAN",
        "NUMERIC_BETWEEN",
    ]

AlternativeSegmentFilter = typing_extensions.TypedDict(
    "AlternativeSegmentFilter",
    {
        "not": bool,
        "sequenceSegment": SequenceSegment,
        "simpleSegment": SimpleSegment,
    },
    total=False,
)

@typing.type_check_only
class SegmentFilter(AlternativeSegmentFilter): ...

AlternativeSegmentFilterClause = typing_extensions.TypedDict(
    "AlternativeSegmentFilterClause",
    {
        "dimensionFilter": SegmentDimensionFilter,
        "metricFilter": SegmentMetricFilter,
        "not": bool,
    },
    total=False,
)

@typing.type_check_only
class SegmentFilterClause(AlternativeSegmentFilterClause): ...

@typing.type_check_only
class SegmentMetricFilter(typing_extensions.TypedDict, total=False):
    comparisonValue: str
    maxComparisonValue: str
    metricName: str
    operator: typing_extensions.Literal[
        "UNSPECIFIED_OPERATOR", "LESS_THAN", "GREATER_THAN", "EQUAL", "BETWEEN"
    ]
    scope: typing_extensions.Literal[
        "UNSPECIFIED_SCOPE", "PRODUCT", "HIT", "SESSION", "USER"
    ]

@typing.type_check_only
class SegmentSequenceStep(typing_extensions.TypedDict, total=False):
    matchType: typing_extensions.Literal[
        "UNSPECIFIED_MATCH_TYPE", "PRECEDES", "IMMEDIATELY_PRECEDES"
    ]
    orFiltersForSegment: _list[OrFiltersForSegment]

@typing.type_check_only
class SequenceSegment(typing_extensions.TypedDict, total=False):
    firstStepShouldMatchFirstHit: bool
    segmentSequenceSteps: _list[SegmentSequenceStep]

@typing.type_check_only
class SimpleSegment(typing_extensions.TypedDict, total=False):
    orFiltersForSegment: _list[OrFiltersForSegment]

@typing.type_check_only
class TransactionData(typing_extensions.TypedDict, total=False):
    transactionId: str
    transactionRevenue: float
    transactionShipping: float
    transactionTax: float

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["USER_ID_TYPE_UNSPECIFIED", "USER_ID", "CLIENT_ID"]
    userId: str

@typing.type_check_only
class UserActivitySession(typing_extensions.TypedDict, total=False):
    activities: _list[Activity]
    dataSource: str
    deviceCategory: str
    platform: str
    sessionDate: str
    sessionId: str
