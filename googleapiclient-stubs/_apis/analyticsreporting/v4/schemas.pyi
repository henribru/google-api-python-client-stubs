import typing

import typing_extensions

class GetReportsResponse(typing_extensions.TypedDict, total=False):
    reports: typing.List[Report]
    resourceQuotasRemaining: ResourceQuotasRemaining
    queryCost: int

class SegmentSequenceStep(typing_extensions.TypedDict, total=False):
    orFiltersForSegment: typing.List[OrFiltersForSegment]
    matchType: typing_extensions.Literal[
        "UNSPECIFIED_MATCH_TYPE", "PRECEDES", "IMMEDIATELY_PRECEDES"
    ]

class SimpleSegment(typing_extensions.TypedDict, total=False):
    orFiltersForSegment: typing.List[OrFiltersForSegment]

class Segment(typing_extensions.TypedDict, total=False):
    dynamicSegment: DynamicSegment
    segmentId: str

class SearchUserActivityRequest(typing_extensions.TypedDict, total=False):
    viewId: str
    pageSize: int
    activityTypes: typing.List[str]
    pageToken: str
    user: User
    dateRange: DateRange

class PivotValueRegion(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class MetricHeaderEntry(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "CURRENCY", "PERCENT", "TIME"
    ]
    name: str

class DynamicSegment(typing_extensions.TypedDict, total=False):
    userSegment: SegmentDefinition
    name: str
    sessionSegment: SegmentDefinition

class ColumnHeader(typing_extensions.TypedDict, total=False):
    metricHeader: MetricHeader
    dimensions: typing.List[str]

class Pivot(typing_extensions.TypedDict, total=False):
    dimensionFilterClauses: typing.List[DimensionFilterClause]
    dimensions: typing.List[Dimension]
    maxGroupCount: int
    metrics: typing.List[Metric]
    startGroup: int

class Metric(typing_extensions.TypedDict, total=False):
    alias: str
    formattingType: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "CURRENCY", "PERCENT", "TIME"
    ]
    expression: str

class GoalData(typing_extensions.TypedDict, total=False):
    goalPreviousStep1: str
    goalName: str
    goalCompletionLocation: str
    goalPreviousStep2: str
    goalValue: float
    goalCompletions: str
    goalIndex: int
    goalPreviousStep3: str

class DimensionFilterClause(typing_extensions.TypedDict, total=False):
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "OR", "AND"]
    filters: typing.List[DimensionFilter]

class ResourceQuotasRemaining(typing_extensions.TypedDict, total=False):
    dailyQuotaTokensRemaining: int
    hourlyQuotaTokensRemaining: int

class CohortGroup(typing_extensions.TypedDict, total=False):
    lifetimeValue: bool
    cohorts: typing.List[Cohort]

class PageviewData(typing_extensions.TypedDict, total=False):
    pageTitle: str
    pagePath: str

class ReportRow(typing_extensions.TypedDict, total=False):
    metrics: typing.List[DateRangeValues]
    dimensions: typing.List[str]

class SequenceSegment(typing_extensions.TypedDict, total=False):
    segmentSequenceSteps: typing.List[SegmentSequenceStep]
    firstStepShouldMatchFirstHit: bool

class SegmentDefinition(typing_extensions.TypedDict, total=False):
    segmentFilters: typing.List[SegmentFilter]

class ReportRequest(typing_extensions.TypedDict, total=False):
    viewId: str
    filtersExpression: str
    metrics: typing.List[Metric]
    segments: typing.List[Segment]
    pivots: typing.List[Pivot]
    dateRanges: typing.List[DateRange]
    pageSize: int
    pageToken: str
    hideValueRanges: bool
    dimensions: typing.List[Dimension]
    dimensionFilterClauses: typing.List[DimensionFilterClause]
    cohortGroup: CohortGroup
    hideTotals: bool
    metricFilterClauses: typing.List[MetricFilterClause]
    includeEmptyRows: bool
    samplingLevel: typing_extensions.Literal[
        "SAMPLING_UNSPECIFIED", "DEFAULT", "SMALL", "LARGE"
    ]
    orderBys: typing.List[OrderBy]

MetricFilter = typing_extensions.TypedDict(
    "MetricFilter",
    {
        "comparisonValue": str,
        "not": bool,
        "metricName": str,
        "operator": typing_extensions.Literal[
            "OPERATOR_UNSPECIFIED", "EQUAL", "LESS_THAN", "GREATER_THAN", "IS_MISSING"
        ],
    },
    total=False,
)

class SegmentMetricFilter(typing_extensions.TypedDict, total=False):
    operator: typing_extensions.Literal[
        "UNSPECIFIED_OPERATOR", "LESS_THAN", "GREATER_THAN", "EQUAL", "BETWEEN"
    ]
    maxComparisonValue: str
    scope: typing_extensions.Literal[
        "UNSPECIFIED_SCOPE", "PRODUCT", "HIT", "SESSION", "USER"
    ]
    comparisonValue: str
    metricName: str

SegmentFilter = typing_extensions.TypedDict(
    "SegmentFilter",
    {
        "sequenceSegment": SequenceSegment,
        "simpleSegment": SimpleSegment,
        "not": bool,
    },
    total=False,
)

class ScreenviewData(typing_extensions.TypedDict, total=False):
    mobileDeviceModel: str
    mobileDeviceBranding: str
    appName: str
    screenName: str

class SearchUserActivityResponse(typing_extensions.TypedDict, total=False):
    totalRows: int
    sessions: typing.List[UserActivitySession]
    nextPageToken: str
    sampleRate: float

class DateRangeValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]
    pivotValueRegions: typing.List[PivotValueRegion]

class Cohort(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    name: str
    type: typing_extensions.Literal["UNSPECIFIED_COHORT_TYPE", "FIRST_VISIT_DATE"]

class PivotHeaderEntry(typing_extensions.TypedDict, total=False):
    dimensionNames: typing.List[str]
    dimensionValues: typing.List[str]
    metric: MetricHeaderEntry

class SegmentDimensionFilter(typing_extensions.TypedDict, total=False):
    maxComparisonValue: str
    minComparisonValue: str
    caseSensitive: bool
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
    dimensionName: str
    expressions: typing.List[str]

class ProductData(typing_extensions.TypedDict, total=False):
    productName: str
    productQuantity: str
    itemRevenue: float
    productSku: str

class GoalSetData(typing_extensions.TypedDict, total=False):
    goals: typing.List[GoalData]

class UserActivitySession(typing_extensions.TypedDict, total=False):
    sessionDate: str
    activities: typing.List[Activity]
    deviceCategory: str
    platform: str
    sessionId: str
    dataSource: str

class CustomDimension(typing_extensions.TypedDict, total=False):
    index: int
    value: str

class TransactionData(typing_extensions.TypedDict, total=False):
    transactionShipping: float
    transactionId: str
    transactionTax: float
    transactionRevenue: float

DimensionFilter = typing_extensions.TypedDict(
    "DimensionFilter",
    {
        "dimensionName": str,
        "expressions": typing.List[str],
        "not": bool,
        "caseSensitive": bool,
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

class User(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["USER_ID_TYPE_UNSPECIFIED", "USER_ID", "CLIENT_ID"]
    userId: str

class MetricHeader(typing_extensions.TypedDict, total=False):
    pivotHeaders: typing.List[PivotHeader]
    metricHeaderEntries: typing.List[MetricHeaderEntry]

class OrFiltersForSegment(typing_extensions.TypedDict, total=False):
    segmentFilterClauses: typing.List[SegmentFilterClause]

class Dimension(typing_extensions.TypedDict, total=False):
    name: str
    histogramBuckets: typing.List[str]

class PivotHeader(typing_extensions.TypedDict, total=False):
    totalPivotGroupsCount: int
    pivotHeaderEntries: typing.List[PivotHeaderEntry]

class EcommerceData(typing_extensions.TypedDict, total=False):
    transaction: TransactionData
    products: typing.List[ProductData]
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

class MetricFilterClause(typing_extensions.TypedDict, total=False):
    filters: typing.List[MetricFilter]
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "OR", "AND"]

SegmentFilterClause = typing_extensions.TypedDict(
    "SegmentFilterClause",
    {
        "metricFilter": SegmentMetricFilter,
        "not": bool,
        "dimensionFilter": SegmentDimensionFilter,
    },
    total=False,
)

class EventData(typing_extensions.TypedDict, total=False):
    eventValue: str
    eventLabel: str
    eventCount: str
    eventAction: str
    eventCategory: str

class GetReportsRequest(typing_extensions.TypedDict, total=False):
    reportRequests: typing.List[ReportRequest]
    useResourceQuotas: bool

class DateRange(typing_extensions.TypedDict, total=False):
    startDate: str
    endDate: str

class ReportData(typing_extensions.TypedDict, total=False):
    isDataGolden: bool
    samplingSpaceSizes: typing.List[str]
    dataLastRefreshed: str
    totals: typing.List[DateRangeValues]
    rowCount: int
    maximums: typing.List[DateRangeValues]
    samplesReadCounts: typing.List[str]
    minimums: typing.List[DateRangeValues]
    rows: typing.List[ReportRow]

class Activity(typing_extensions.TypedDict, total=False):
    activityType: typing_extensions.Literal[
        "ACTIVITY_TYPE_UNSPECIFIED",
        "PAGEVIEW",
        "SCREENVIEW",
        "GOAL",
        "ECOMMERCE",
        "EVENT",
    ]
    source: str
    campaign: str
    appview: ScreenviewData
    goals: GoalSetData
    event: EventData
    activityTime: str
    pageview: PageviewData
    customDimension: typing.List[CustomDimension]
    channelGrouping: str
    ecommerce: EcommerceData
    keyword: str
    medium: str
    hostname: str
    landingPagePath: str

class OrderBy(typing_extensions.TypedDict, total=False):
    sortOrder: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    fieldName: str
    orderType: typing_extensions.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "VALUE",
        "DELTA",
        "SMART",
        "HISTOGRAM_BUCKET",
        "DIMENSION_AS_INTEGER",
    ]

class Report(typing_extensions.TypedDict, total=False):
    columnHeader: ColumnHeader
    nextPageToken: str
    data: ReportData
