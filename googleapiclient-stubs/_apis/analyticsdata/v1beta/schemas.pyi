import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActiveMetricRestriction(typing_extensions.TypedDict, total=False):
    metricName: str
    restrictedMetricTypes: _list[str]

@typing.type_check_only
class BatchRunPivotReportsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[RunPivotReportRequest]

@typing.type_check_only
class BatchRunPivotReportsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    pivotReports: _list[RunPivotReportResponse]

@typing.type_check_only
class BatchRunReportsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[RunReportRequest]

@typing.type_check_only
class BatchRunReportsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    reports: _list[RunReportResponse]

@typing.type_check_only
class BetweenFilter(typing_extensions.TypedDict, total=False):
    fromValue: NumericValue
    toValue: NumericValue

@typing.type_check_only
class CaseExpression(typing_extensions.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class CheckCompatibilityRequest(typing_extensions.TypedDict, total=False):
    compatibilityFilter: typing_extensions.Literal[
        "COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    dimensionFilter: FilterExpression
    dimensions: _list[Dimension]
    metricFilter: FilterExpression
    metrics: _list[Metric]

@typing.type_check_only
class CheckCompatibilityResponse(typing_extensions.TypedDict, total=False):
    dimensionCompatibilities: _list[DimensionCompatibility]
    metricCompatibilities: _list[MetricCompatibility]

@typing.type_check_only
class Cohort(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    dimension: str
    name: str

@typing.type_check_only
class CohortReportSettings(typing_extensions.TypedDict, total=False):
    accumulate: bool

@typing.type_check_only
class CohortSpec(typing_extensions.TypedDict, total=False):
    cohortReportSettings: CohortReportSettings
    cohorts: _list[Cohort]
    cohortsRange: CohortsRange

@typing.type_check_only
class CohortsRange(typing_extensions.TypedDict, total=False):
    endOffset: int
    granularity: typing_extensions.Literal[
        "GRANULARITY_UNSPECIFIED", "DAILY", "WEEKLY", "MONTHLY"
    ]
    startOffset: int

@typing.type_check_only
class ConcatenateExpression(typing_extensions.TypedDict, total=False):
    delimiter: str
    dimensionNames: _list[str]

@typing.type_check_only
class DateRange(typing_extensions.TypedDict, total=False):
    endDate: str
    name: str
    startDate: str

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    dimensionExpression: DimensionExpression
    name: str

@typing.type_check_only
class DimensionCompatibility(typing_extensions.TypedDict, total=False):
    compatibility: typing_extensions.Literal[
        "COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    dimensionMetadata: DimensionMetadata

@typing.type_check_only
class DimensionExpression(typing_extensions.TypedDict, total=False):
    concatenate: ConcatenateExpression
    lowerCase: CaseExpression
    upperCase: CaseExpression

@typing.type_check_only
class DimensionHeader(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class DimensionMetadata(typing_extensions.TypedDict, total=False):
    apiName: str
    category: str
    customDefinition: bool
    deprecatedApiNames: _list[str]
    description: str
    uiName: str

@typing.type_check_only
class DimensionOrderBy(typing_extensions.TypedDict, total=False):
    dimensionName: str
    orderType: typing_extensions.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "ALPHANUMERIC",
        "CASE_INSENSITIVE_ALPHANUMERIC",
        "NUMERIC",
    ]

@typing.type_check_only
class DimensionValue(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    betweenFilter: BetweenFilter
    fieldName: str
    inListFilter: InListFilter
    numericFilter: NumericFilter
    stringFilter: StringFilter

@typing.type_check_only
class FilterExpression(dict[str, typing.Any]): ...

@typing.type_check_only
class FilterExpressionList(dict[str, typing.Any]): ...

@typing.type_check_only
class InListFilter(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    dimensions: _list[DimensionMetadata]
    metrics: _list[MetricMetadata]
    name: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    expression: str
    invisible: bool
    name: str

@typing.type_check_only
class MetricCompatibility(typing_extensions.TypedDict, total=False):
    compatibility: typing_extensions.Literal[
        "COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    metricMetadata: MetricMetadata

@typing.type_check_only
class MetricHeader(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
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
class MetricMetadata(typing_extensions.TypedDict, total=False):
    apiName: str
    blockedReasons: _list[str]
    category: str
    customDefinition: bool
    deprecatedApiNames: _list[str]
    description: str
    expression: str
    type: typing_extensions.Literal[
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
class MetricOrderBy(typing_extensions.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class MetricValue(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class MinuteRange(typing_extensions.TypedDict, total=False):
    endMinutesAgo: int
    name: str
    startMinutesAgo: int

@typing.type_check_only
class NumericFilter(typing_extensions.TypedDict, total=False):
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED",
        "EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
    ]
    value: NumericValue

@typing.type_check_only
class NumericValue(typing_extensions.TypedDict, total=False):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class OrderBy(typing_extensions.TypedDict, total=False):
    desc: bool
    dimension: DimensionOrderBy
    metric: MetricOrderBy
    pivot: PivotOrderBy

@typing.type_check_only
class Pivot(typing_extensions.TypedDict, total=False):
    fieldNames: _list[str]
    limit: str
    metricAggregations: _list[str]
    offset: str
    orderBys: _list[OrderBy]

@typing.type_check_only
class PivotDimensionHeader(typing_extensions.TypedDict, total=False):
    dimensionValues: _list[DimensionValue]

@typing.type_check_only
class PivotHeader(typing_extensions.TypedDict, total=False):
    pivotDimensionHeaders: _list[PivotDimensionHeader]
    rowCount: int

@typing.type_check_only
class PivotOrderBy(typing_extensions.TypedDict, total=False):
    metricName: str
    pivotSelections: _list[PivotSelection]

@typing.type_check_only
class PivotSelection(typing_extensions.TypedDict, total=False):
    dimensionName: str
    dimensionValue: str

@typing.type_check_only
class PropertyQuota(typing_extensions.TypedDict, total=False):
    concurrentRequests: QuotaStatus
    potentiallyThresholdedRequestsPerHour: QuotaStatus
    serverErrorsPerProjectPerHour: QuotaStatus
    tokensPerDay: QuotaStatus
    tokensPerHour: QuotaStatus
    tokensPerProjectPerHour: QuotaStatus

@typing.type_check_only
class QuotaStatus(typing_extensions.TypedDict, total=False):
    consumed: int
    remaining: int

@typing.type_check_only
class ResponseMetaData(typing_extensions.TypedDict, total=False):
    currencyCode: str
    dataLossFromOtherRow: bool
    emptyReason: str
    schemaRestrictionResponse: SchemaRestrictionResponse
    subjectToThresholding: bool
    timeZone: str

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    dimensionValues: _list[DimensionValue]
    metricValues: _list[MetricValue]

@typing.type_check_only
class RunPivotReportRequest(dict[str, typing.Any]): ...

@typing.type_check_only
class RunPivotReportResponse(typing_extensions.TypedDict, total=False):
    aggregates: _list[Row]
    dimensionHeaders: _list[DimensionHeader]
    kind: str
    metadata: ResponseMetaData
    metricHeaders: _list[MetricHeader]
    pivotHeaders: _list[PivotHeader]
    propertyQuota: PropertyQuota
    rows: _list[Row]

@typing.type_check_only
class RunRealtimeReportRequest(typing_extensions.TypedDict, total=False):
    dimensionFilter: FilterExpression
    dimensions: _list[Dimension]
    limit: str
    metricAggregations: _list[str]
    metricFilter: FilterExpression
    metrics: _list[Metric]
    minuteRanges: _list[MinuteRange]
    orderBys: _list[OrderBy]
    returnPropertyQuota: bool

@typing.type_check_only
class RunRealtimeReportResponse(typing_extensions.TypedDict, total=False):
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
class RunReportRequest(dict[str, typing.Any]): ...

@typing.type_check_only
class RunReportResponse(typing_extensions.TypedDict, total=False):
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
class SchemaRestrictionResponse(typing_extensions.TypedDict, total=False):
    activeMetricRestrictions: _list[ActiveMetricRestriction]

@typing.type_check_only
class StringFilter(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    matchType: typing_extensions.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
        "PARTIAL_REGEXP",
    ]
    value: str
