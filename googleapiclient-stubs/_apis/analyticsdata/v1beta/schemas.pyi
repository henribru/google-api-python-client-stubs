import typing

_list = list

@typing.type_check_only
class ActiveMetricRestriction(typing.TypedDict, total=False):
    metricName: str
    restrictedMetricTypes: _list[
        typing.Literal[
            "RESTRICTED_METRIC_TYPE_UNSPECIFIED", "COST_DATA", "REVENUE_DATA"
        ]
    ]

@typing.type_check_only
class AudienceExport(typing.TypedDict, total=False):
    audience: str
    audienceDisplayName: str
    beginCreatingTime: str
    creationQuotaTokensCharged: int
    dimensions: _list[V1betaAudienceDimension]
    errorMessage: str
    name: str
    percentageCompleted: float
    rowCount: int
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED"]

@typing.type_check_only
class AudienceListMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class BatchRunPivotReportsRequest(typing.TypedDict, total=False):
    requests: _list[RunPivotReportRequest]

@typing.type_check_only
class BatchRunPivotReportsResponse(typing.TypedDict, total=False):
    kind: str
    pivotReports: _list[RunPivotReportResponse]

@typing.type_check_only
class BatchRunReportsRequest(typing.TypedDict, total=False):
    requests: _list[RunReportRequest]

@typing.type_check_only
class BatchRunReportsResponse(typing.TypedDict, total=False):
    kind: str
    reports: _list[RunReportResponse]

@typing.type_check_only
class BetweenFilter(typing.TypedDict, total=False):
    fromValue: NumericValue
    toValue: NumericValue

@typing.type_check_only
class CaseExpression(typing.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class CheckCompatibilityRequest(typing.TypedDict, total=False):
    compatibilityFilter: typing.Literal[
        "COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    dimensionFilter: FilterExpression
    dimensions: _list[Dimension]
    metricFilter: FilterExpression
    metrics: _list[Metric]

@typing.type_check_only
class CheckCompatibilityResponse(typing.TypedDict, total=False):
    dimensionCompatibilities: _list[DimensionCompatibility]
    metricCompatibilities: _list[MetricCompatibility]

@typing.type_check_only
class Cohort(typing.TypedDict, total=False):
    dateRange: DateRange
    dimension: str
    name: str

@typing.type_check_only
class CohortReportSettings(typing.TypedDict, total=False):
    accumulate: bool

@typing.type_check_only
class CohortSpec(typing.TypedDict, total=False):
    cohortReportSettings: CohortReportSettings
    cohorts: _list[Cohort]
    cohortsRange: CohortsRange

@typing.type_check_only
class CohortsRange(typing.TypedDict, total=False):
    endOffset: int
    granularity: typing.Literal["GRANULARITY_UNSPECIFIED", "DAILY", "WEEKLY", "MONTHLY"]
    startOffset: int

@typing.type_check_only
class Comparison(typing.TypedDict, total=False):
    comparison: str
    dimensionFilter: FilterExpression
    name: str

@typing.type_check_only
class ComparisonMetadata(typing.TypedDict, total=False):
    apiName: str
    description: str
    uiName: str

@typing.type_check_only
class ConcatenateExpression(typing.TypedDict, total=False):
    delimiter: str
    dimensionNames: _list[str]

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    endDate: str
    name: str
    startDate: str

@typing.type_check_only
class Dimension(typing.TypedDict, total=False):
    dimensionExpression: DimensionExpression
    name: str

@typing.type_check_only
class DimensionCompatibility(typing.TypedDict, total=False):
    compatibility: typing.Literal[
        "COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    dimensionMetadata: DimensionMetadata

@typing.type_check_only
class DimensionExpression(typing.TypedDict, total=False):
    concatenate: ConcatenateExpression
    lowerCase: CaseExpression
    upperCase: CaseExpression

@typing.type_check_only
class DimensionHeader(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class DimensionMetadata(typing.TypedDict, total=False):
    apiName: str
    category: str
    customDefinition: bool
    deprecatedApiNames: _list[str]
    description: str
    uiName: str

@typing.type_check_only
class DimensionOrderBy(typing.TypedDict, total=False):
    dimensionName: str
    orderType: typing.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "ALPHANUMERIC",
        "CASE_INSENSITIVE_ALPHANUMERIC",
        "NUMERIC",
    ]

@typing.type_check_only
class DimensionValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class EmptyFilter(typing.TypedDict, total=False): ...

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    betweenFilter: BetweenFilter
    emptyFilter: EmptyFilter
    fieldName: str
    inListFilter: InListFilter
    numericFilter: NumericFilter
    stringFilter: StringFilter

@typing.type_check_only
class FilterExpression(typing.TypedDict, total=False):
    andGroup: FilterExpressionList
    filter: Filter
    notExpression: FilterExpression
    orGroup: FilterExpressionList

@typing.type_check_only
class FilterExpressionList(typing.TypedDict, total=False):
    expressions: _list[FilterExpression]

@typing.type_check_only
class InListFilter(typing.TypedDict, total=False):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class ListAudienceExportsResponse(typing.TypedDict, total=False):
    audienceExports: _list[AudienceExport]
    nextPageToken: str

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    comparisons: _list[ComparisonMetadata]
    dimensions: _list[DimensionMetadata]
    metrics: _list[MetricMetadata]
    name: str

@typing.type_check_only
class Metric(typing.TypedDict, total=False):
    expression: str
    invisible: bool
    name: str

@typing.type_check_only
class MetricCompatibility(typing.TypedDict, total=False):
    compatibility: typing.Literal[
        "COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    metricMetadata: MetricMetadata

@typing.type_check_only
class MetricHeader(typing.TypedDict, total=False):
    name: str
    type: typing.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "TYPE_INTEGER",
        "TYPE_FLOAT",
        "TYPE_SECONDS",
        "TYPE_MILLISECONDS",
        "TYPE_MINUTES",
        "TYPE_HOURS",
        "TYPE_STANDARD",
        "TYPE_CURRENCY",
        "TYPE_FEET",
        "TYPE_MILES",
        "TYPE_METERS",
        "TYPE_KILOMETERS",
    ]

@typing.type_check_only
class MetricMetadata(typing.TypedDict, total=False):
    apiName: str
    blockedReasons: _list[
        typing.Literal[
            "BLOCKED_REASON_UNSPECIFIED", "NO_REVENUE_METRICS", "NO_COST_METRICS"
        ]
    ]
    category: str
    customDefinition: bool
    deprecatedApiNames: _list[str]
    description: str
    expression: str
    type: typing.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "TYPE_INTEGER",
        "TYPE_FLOAT",
        "TYPE_SECONDS",
        "TYPE_MILLISECONDS",
        "TYPE_MINUTES",
        "TYPE_HOURS",
        "TYPE_STANDARD",
        "TYPE_CURRENCY",
        "TYPE_FEET",
        "TYPE_MILES",
        "TYPE_METERS",
        "TYPE_KILOMETERS",
    ]
    uiName: str

@typing.type_check_only
class MetricOrderBy(typing.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class MetricValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class MinuteRange(typing.TypedDict, total=False):
    endMinutesAgo: int
    name: str
    startMinutesAgo: int

@typing.type_check_only
class NumericFilter(typing.TypedDict, total=False):
    operation: typing.Literal[
        "OPERATION_UNSPECIFIED",
        "EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
    ]
    value: NumericValue

@typing.type_check_only
class NumericValue(typing.TypedDict, total=False):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrderBy(typing.TypedDict, total=False):
    desc: bool
    dimension: DimensionOrderBy
    metric: MetricOrderBy
    pivot: PivotOrderBy

@typing.type_check_only
class Pivot(typing.TypedDict, total=False):
    fieldNames: _list[str]
    limit: str
    metricAggregations: _list[
        typing.Literal[
            "METRIC_AGGREGATION_UNSPECIFIED", "TOTAL", "MINIMUM", "MAXIMUM", "COUNT"
        ]
    ]
    offset: str
    orderBys: _list[OrderBy]

@typing.type_check_only
class PivotDimensionHeader(typing.TypedDict, total=False):
    dimensionValues: _list[DimensionValue]

@typing.type_check_only
class PivotHeader(typing.TypedDict, total=False):
    pivotDimensionHeaders: _list[PivotDimensionHeader]
    rowCount: int

@typing.type_check_only
class PivotOrderBy(typing.TypedDict, total=False):
    metricName: str
    pivotSelections: _list[PivotSelection]

@typing.type_check_only
class PivotSelection(typing.TypedDict, total=False):
    dimensionName: str
    dimensionValue: str

@typing.type_check_only
class PropertyQuota(typing.TypedDict, total=False):
    concurrentRequests: QuotaStatus
    potentiallyThresholdedRequestsPerHour: QuotaStatus
    serverErrorsPerProjectPerHour: QuotaStatus
    tokensPerDay: QuotaStatus
    tokensPerHour: QuotaStatus
    tokensPerProjectPerHour: QuotaStatus

@typing.type_check_only
class QueryAudienceExportRequest(typing.TypedDict, total=False):
    limit: str
    offset: str

@typing.type_check_only
class QueryAudienceExportResponse(typing.TypedDict, total=False):
    audienceExport: AudienceExport
    audienceRows: _list[V1betaAudienceRow]
    rowCount: int

@typing.type_check_only
class QuotaStatus(typing.TypedDict, total=False):
    consumed: int
    remaining: int

@typing.type_check_only
class ResponseMetaData(typing.TypedDict, total=False):
    currencyCode: str
    dataLossFromOtherRow: bool
    emptyReason: str
    samplingMetadatas: _list[SamplingMetadata]
    schemaRestrictionResponse: SchemaRestrictionResponse
    subjectToThresholding: bool
    timeZone: str

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    dimensionValues: _list[DimensionValue]
    metricValues: _list[MetricValue]

@typing.type_check_only
class RunPivotReportRequest(typing.TypedDict, total=False):
    cohortSpec: CohortSpec
    comparisons: _list[Comparison]
    currencyCode: str
    dateRanges: _list[DateRange]
    dimensionFilter: FilterExpression
    dimensions: _list[Dimension]
    keepEmptyRows: bool
    metricFilter: FilterExpression
    metrics: _list[Metric]
    pivots: _list[Pivot]
    property: str
    returnPropertyQuota: bool

@typing.type_check_only
class RunPivotReportResponse(typing.TypedDict, total=False):
    aggregates: _list[Row]
    dimensionHeaders: _list[DimensionHeader]
    kind: str
    metadata: ResponseMetaData
    metricHeaders: _list[MetricHeader]
    pivotHeaders: _list[PivotHeader]
    propertyQuota: PropertyQuota
    rows: _list[Row]

@typing.type_check_only
class RunRealtimeReportRequest(typing.TypedDict, total=False):
    dimensionFilter: FilterExpression
    dimensions: _list[Dimension]
    limit: str
    metricAggregations: _list[
        typing.Literal[
            "METRIC_AGGREGATION_UNSPECIFIED", "TOTAL", "MINIMUM", "MAXIMUM", "COUNT"
        ]
    ]
    metricFilter: FilterExpression
    metrics: _list[Metric]
    minuteRanges: _list[MinuteRange]
    orderBys: _list[OrderBy]
    returnPropertyQuota: bool

@typing.type_check_only
class RunRealtimeReportResponse(typing.TypedDict, total=False):
    dimensionHeaders: _list[DimensionHeader]
    kind: str
    maximums: _list[Row]
    metricHeaders: _list[MetricHeader]
    minimums: _list[Row]
    propertyQuota: PropertyQuota
    rowCount: int
    rows: _list[Row]
    totals: _list[Row]

@typing.type_check_only
class RunReportRequest(typing.TypedDict, total=False):
    cohortSpec: CohortSpec
    comparisons: _list[Comparison]
    currencyCode: str
    dateRanges: _list[DateRange]
    dimensionFilter: FilterExpression
    dimensions: _list[Dimension]
    keepEmptyRows: bool
    limit: str
    metricAggregations: _list[
        typing.Literal[
            "METRIC_AGGREGATION_UNSPECIFIED", "TOTAL", "MINIMUM", "MAXIMUM", "COUNT"
        ]
    ]
    metricFilter: FilterExpression
    metrics: _list[Metric]
    offset: str
    orderBys: _list[OrderBy]
    property: str
    returnPropertyQuota: bool

@typing.type_check_only
class RunReportResponse(typing.TypedDict, total=False):
    dimensionHeaders: _list[DimensionHeader]
    kind: str
    maximums: _list[Row]
    metadata: ResponseMetaData
    metricHeaders: _list[MetricHeader]
    minimums: _list[Row]
    propertyQuota: PropertyQuota
    rowCount: int
    rows: _list[Row]
    totals: _list[Row]

@typing.type_check_only
class SamplingMetadata(typing.TypedDict, total=False):
    samplesReadCount: str
    samplingSpaceSize: str

@typing.type_check_only
class SchemaRestrictionResponse(typing.TypedDict, total=False):
    activeMetricRestrictions: _list[ActiveMetricRestriction]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringFilter(typing.TypedDict, total=False):
    caseSensitive: bool
    matchType: typing.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
        "PARTIAL_REGEXP",
    ]
    value: str

@typing.type_check_only
class V1betaAudienceDimension(typing.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class V1betaAudienceDimensionValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class V1betaAudienceRow(typing.TypedDict, total=False):
    dimensionValues: _list[V1betaAudienceDimensionValue]
