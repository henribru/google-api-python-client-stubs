import typing

_list = list

@typing.type_check_only
class Activity(typing.TypedDict, total=False):
    activityTime: str
    activityType: typing.Literal[
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
class Cohort(typing.TypedDict, total=False):
    dateRange: DateRange
    name: str
    type: typing.Literal["UNSPECIFIED_COHORT_TYPE", "FIRST_VISIT_DATE"]

@typing.type_check_only
class CohortGroup(typing.TypedDict, total=False):
    cohorts: _list[Cohort]
    lifetimeValue: bool

@typing.type_check_only
class ColumnHeader(typing.TypedDict, total=False):
    dimensions: _list[str]
    metricHeader: MetricHeader

@typing.type_check_only
class CustomDimension(typing.TypedDict, total=False):
    index: int
    value: str

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    endDate: str
    startDate: str

@typing.type_check_only
class DateRangeValues(typing.TypedDict, total=False):
    pivotValueRegions: _list[PivotValueRegion]
    values: _list[str]

@typing.type_check_only
class Dimension(typing.TypedDict, total=False):
    histogramBuckets: _list[str]
    name: str

AlternativeDimensionFilter = typing.TypedDict(
    "AlternativeDimensionFilter",
    {
        "caseSensitive": bool,
        "dimensionName": str,
        "expressions": _list[str],
        "not": bool,
        "operator": typing.Literal[
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
class DimensionFilterClause(typing.TypedDict, total=False):
    filters: _list[DimensionFilter]
    operator: typing.Literal["OPERATOR_UNSPECIFIED", "OR", "AND"]

@typing.type_check_only
class DynamicSegment(typing.TypedDict, total=False):
    name: str
    sessionSegment: SegmentDefinition
    userSegment: SegmentDefinition

@typing.type_check_only
class EcommerceData(typing.TypedDict, total=False):
    actionType: typing.Literal[
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
    ecommerceType: typing.Literal["ECOMMERCE_TYPE_UNSPECIFIED", "CLASSIC", "ENHANCED"]
    products: _list[ProductData]
    transaction: TransactionData

@typing.type_check_only
class EventData(typing.TypedDict, total=False):
    eventAction: str
    eventCategory: str
    eventCount: str
    eventLabel: str
    eventValue: str

@typing.type_check_only
class GetReportsRequest(typing.TypedDict, total=False):
    reportRequests: _list[ReportRequest]
    useResourceQuotas: bool

@typing.type_check_only
class GetReportsResponse(typing.TypedDict, total=False):
    queryCost: int
    reports: _list[Report]
    resourceQuotasRemaining: ResourceQuotasRemaining

@typing.type_check_only
class GoalData(typing.TypedDict, total=False):
    goalCompletionLocation: str
    goalCompletions: str
    goalIndex: int
    goalName: str
    goalPreviousStep1: str
    goalPreviousStep2: str
    goalPreviousStep3: str
    goalValue: float

@typing.type_check_only
class GoalSetData(typing.TypedDict, total=False):
    goals: _list[GoalData]

@typing.type_check_only
class Metric(typing.TypedDict, total=False):
    alias: str
    expression: str
    formattingType: typing.Literal[
        "METRIC_TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "CURRENCY", "PERCENT", "TIME"
    ]

AlternativeMetricFilter = typing.TypedDict(
    "AlternativeMetricFilter",
    {
        "comparisonValue": str,
        "metricName": str,
        "not": bool,
        "operator": typing.Literal[
            "OPERATOR_UNSPECIFIED", "EQUAL", "LESS_THAN", "GREATER_THAN", "IS_MISSING"
        ],
    },
    total=False,
)

@typing.type_check_only
class MetricFilter(AlternativeMetricFilter): ...

@typing.type_check_only
class MetricFilterClause(typing.TypedDict, total=False):
    filters: _list[MetricFilter]
    operator: typing.Literal["OPERATOR_UNSPECIFIED", "OR", "AND"]

@typing.type_check_only
class MetricHeader(typing.TypedDict, total=False):
    metricHeaderEntries: _list[MetricHeaderEntry]
    pivotHeaders: _list[PivotHeader]

@typing.type_check_only
class MetricHeaderEntry(typing.TypedDict, total=False):
    name: str
    type: typing.Literal[
        "METRIC_TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "CURRENCY", "PERCENT", "TIME"
    ]

@typing.type_check_only
class OrFiltersForSegment(typing.TypedDict, total=False):
    segmentFilterClauses: _list[SegmentFilterClause]

@typing.type_check_only
class OrderBy(typing.TypedDict, total=False):
    fieldName: str
    orderType: typing.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "VALUE",
        "DELTA",
        "SMART",
        "HISTOGRAM_BUCKET",
        "DIMENSION_AS_INTEGER",
    ]
    sortOrder: typing.Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class PageviewData(typing.TypedDict, total=False):
    pagePath: str
    pageTitle: str

@typing.type_check_only
class Pivot(typing.TypedDict, total=False):
    dimensionFilterClauses: _list[DimensionFilterClause]
    dimensions: _list[Dimension]
    maxGroupCount: int
    metrics: _list[Metric]
    startGroup: int

@typing.type_check_only
class PivotHeader(typing.TypedDict, total=False):
    pivotHeaderEntries: _list[PivotHeaderEntry]
    totalPivotGroupsCount: int

@typing.type_check_only
class PivotHeaderEntry(typing.TypedDict, total=False):
    dimensionNames: _list[str]
    dimensionValues: _list[str]
    metric: MetricHeaderEntry

@typing.type_check_only
class PivotValueRegion(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ProductData(typing.TypedDict, total=False):
    itemRevenue: float
    productName: str
    productQuantity: str
    productSku: str

@typing.type_check_only
class Report(typing.TypedDict, total=False):
    columnHeader: ColumnHeader
    data: ReportData
    nextPageToken: str

@typing.type_check_only
class ReportData(typing.TypedDict, total=False):
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
class ReportRequest(typing.TypedDict, total=False):
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
    samplingLevel: typing.Literal["SAMPLING_UNSPECIFIED", "DEFAULT", "SMALL", "LARGE"]
    segments: _list[Segment]
    viewId: str

@typing.type_check_only
class ReportRow(typing.TypedDict, total=False):
    dimensions: _list[str]
    metrics: _list[DateRangeValues]

@typing.type_check_only
class ResourceQuotasRemaining(typing.TypedDict, total=False):
    dailyQuotaTokensRemaining: int
    hourlyQuotaTokensRemaining: int

@typing.type_check_only
class ScreenviewData(typing.TypedDict, total=False):
    appName: str
    mobileDeviceBranding: str
    mobileDeviceModel: str
    screenName: str

@typing.type_check_only
class SearchUserActivityRequest(typing.TypedDict, total=False):
    activityTypes: _list[
        typing.Literal[
            "ACTIVITY_TYPE_UNSPECIFIED",
            "PAGEVIEW",
            "SCREENVIEW",
            "GOAL",
            "ECOMMERCE",
            "EVENT",
        ]
    ]
    dateRange: DateRange
    pageSize: int
    pageToken: str
    user: User
    viewId: str

@typing.type_check_only
class SearchUserActivityResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sampleRate: float
    sessions: _list[UserActivitySession]
    totalRows: int

@typing.type_check_only
class Segment(typing.TypedDict, total=False):
    dynamicSegment: DynamicSegment
    segmentId: str

@typing.type_check_only
class SegmentDefinition(typing.TypedDict, total=False):
    segmentFilters: _list[SegmentFilter]

@typing.type_check_only
class SegmentDimensionFilter(typing.TypedDict, total=False):
    caseSensitive: bool
    dimensionName: str
    expressions: _list[str]
    maxComparisonValue: str
    minComparisonValue: str
    operator: typing.Literal[
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

AlternativeSegmentFilter = typing.TypedDict(
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

AlternativeSegmentFilterClause = typing.TypedDict(
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
class SegmentMetricFilter(typing.TypedDict, total=False):
    comparisonValue: str
    maxComparisonValue: str
    metricName: str
    operator: typing.Literal[
        "UNSPECIFIED_OPERATOR", "LESS_THAN", "GREATER_THAN", "EQUAL", "BETWEEN"
    ]
    scope: typing.Literal["UNSPECIFIED_SCOPE", "PRODUCT", "HIT", "SESSION", "USER"]

@typing.type_check_only
class SegmentSequenceStep(typing.TypedDict, total=False):
    matchType: typing.Literal[
        "UNSPECIFIED_MATCH_TYPE", "PRECEDES", "IMMEDIATELY_PRECEDES"
    ]
    orFiltersForSegment: _list[OrFiltersForSegment]

@typing.type_check_only
class SequenceSegment(typing.TypedDict, total=False):
    firstStepShouldMatchFirstHit: bool
    segmentSequenceSteps: _list[SegmentSequenceStep]

@typing.type_check_only
class SimpleSegment(typing.TypedDict, total=False):
    orFiltersForSegment: _list[OrFiltersForSegment]

@typing.type_check_only
class TransactionData(typing.TypedDict, total=False):
    transactionId: str
    transactionRevenue: float
    transactionShipping: float
    transactionTax: float

@typing.type_check_only
class User(typing.TypedDict, total=False):
    type: typing.Literal["USER_ID_TYPE_UNSPECIFIED", "USER_ID", "CLIENT_ID"]
    userId: str

@typing.type_check_only
class UserActivitySession(typing.TypedDict, total=False):
    activities: _list[Activity]
    dataSource: str
    deviceCategory: str
    platform: str
    sessionDate: str
    sessionId: str
