import typing

import typing_extensions
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
    customDimension: typing.List[CustomDimension]
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
    cohorts: typing.List[Cohort]
    lifetimeValue: bool

@typing.type_check_only
class ColumnHeader(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[str]
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
    pivotValueRegions: typing.List[PivotValueRegion]
    values: typing.List[str]

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    histogramBuckets: typing.List[str]
    name: str

AlternativeDimensionFilter = typing_extensions.TypedDict(
    "AlternativeDimensionFilter",
    {
        "caseSensitive": bool,
        "dimensionName": str,
        "expressions": typing.List[str],
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
    filters: typing.List[DimensionFilter]
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
    products: typing.List[ProductData]
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
    reportRequests: typing.List[ReportRequest]
    useResourceQuotas: bool

@typing.type_check_only
class GetReportsResponse(typing_extensions.TypedDict, total=False):
    queryCost: int
    reports: typing.List[Report]
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
    goals: typing.List[GoalData]

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
    filters: typing.List[MetricFilter]
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "OR", "AND"]

@typing.type_check_only
class MetricHeader(typing_extensions.TypedDict, total=False):
    metricHeaderEntries: typing.List[MetricHeaderEntry]
    pivotHeaders: typing.List[PivotHeader]

@typing.type_check_only
class MetricHeaderEntry(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "CURRENCY", "PERCENT", "TIME"
    ]

@typing.type_check_only
class OrFiltersForSegment(typing_extensions.TypedDict, total=False):
    segmentFilterClauses: typing.List[SegmentFilterClause]

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
    dimensionFilterClauses: typing.List[DimensionFilterClause]
    dimensions: typing.List[Dimension]
    maxGroupCount: int
    metrics: typing.List[Metric]
    startGroup: int

@typing.type_check_only
class PivotHeader(typing_extensions.TypedDict, total=False):
    pivotHeaderEntries: typing.List[PivotHeaderEntry]
    totalPivotGroupsCount: int

@typing.type_check_only
class PivotHeaderEntry(typing_extensions.TypedDict, total=False):
    dimensionNames: typing.List[str]
    dimensionValues: typing.List[str]
    metric: MetricHeaderEntry

@typing.type_check_only
class PivotValueRegion(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

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
    isDataGolden: bool
    maximums: typing.List[DateRangeValues]
    minimums: typing.List[DateRangeValues]
    rowCount: int
    rows: typing.List[ReportRow]
    samplesReadCounts: typing.List[str]
    samplingSpaceSizes: typing.List[str]
    totals: typing.List[DateRangeValues]

@typing.type_check_only
class ReportRequest(typing_extensions.TypedDict, total=False):
    cohortGroup: CohortGroup
    dateRanges: typing.List[DateRange]
    dimensionFilterClauses: typing.List[DimensionFilterClause]
    dimensions: typing.List[Dimension]
    filtersExpression: str
    hideTotals: bool
    hideValueRanges: bool
    includeEmptyRows: bool
    metricFilterClauses: typing.List[MetricFilterClause]
    metrics: typing.List[Metric]
    orderBys: typing.List[OrderBy]
    pageSize: int
    pageToken: str
    pivots: typing.List[Pivot]
    samplingLevel: typing_extensions.Literal[
        "SAMPLING_UNSPECIFIED", "DEFAULT", "SMALL", "LARGE"
    ]
    segments: typing.List[Segment]
    viewId: str

@typing.type_check_only
class ReportRow(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[str]
    metrics: typing.List[DateRangeValues]

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
    activityTypes: typing.List[str]
    dateRange: DateRange
    pageSize: int
    pageToken: str
    user: User
    viewId: str

@typing.type_check_only
class SearchUserActivityResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sampleRate: float
    sessions: typing.List[UserActivitySession]
    totalRows: int

@typing.type_check_only
class Segment(typing_extensions.TypedDict, total=False):
    dynamicSegment: DynamicSegment
    segmentId: str

@typing.type_check_only
class SegmentDefinition(typing_extensions.TypedDict, total=False):
    segmentFilters: typing.List[SegmentFilter]

@typing.type_check_only
class SegmentDimensionFilter(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    dimensionName: str
    expressions: typing.List[str]
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
    orFiltersForSegment: typing.List[OrFiltersForSegment]

@typing.type_check_only
class SequenceSegment(typing_extensions.TypedDict, total=False):
    firstStepShouldMatchFirstHit: bool
    segmentSequenceSteps: typing.List[SegmentSequenceStep]

@typing.type_check_only
class SimpleSegment(typing_extensions.TypedDict, total=False):
    orFiltersForSegment: typing.List[OrFiltersForSegment]

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
    activities: typing.List[Activity]
    dataSource: str
    deviceCategory: str
    platform: str
    sessionDate: str
    sessionId: str
