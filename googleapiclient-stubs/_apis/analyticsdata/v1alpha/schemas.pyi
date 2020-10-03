import typing

import typing_extensions

class RunPivotReportResponse(typing_extensions.TypedDict, total=False):
    rows: typing.List[Row]
    metadata: ResponseMetaData
    pivotHeaders: typing.List[PivotHeader]
    dimensionHeaders: typing.List[DimensionHeader]
    propertyQuota: PropertyQuota
    metricHeaders: typing.List[MetricHeader]
    aggregates: typing.List[Row]

class DateRange(typing_extensions.TypedDict, total=False):
    endDate: str
    name: str
    startDate: str

class DimensionMetadata(typing_extensions.TypedDict, total=False):
    apiName: str
    uiName: str
    description: str
    deprecatedApiNames: typing.List[str]

class PivotSelection(typing_extensions.TypedDict, total=False):
    dimensionValue: str
    dimensionName: str

class NumericValue(typing_extensions.TypedDict, total=False):
    int64Value: str
    doubleValue: float

class BatchRunReportsRequest(typing_extensions.TypedDict, total=False):
    entity: Entity
    requests: typing.List[RunReportRequest]

class MetricHeader(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "TYPE_INTEGER",
        "TYPE_FLOAT",
        "TYPE_SECONDS",
        "TYPE_CURRENCY",
    ]

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

class RunReportRequest(typing.Dict[str, typing.Any]): ...

class PivotOrderBy(typing_extensions.TypedDict, total=False):
    metricName: str
    pivotSelections: typing.List[PivotSelection]

class RunPivotReportRequest(typing_extensions.TypedDict, total=False):
    metricFilter: FilterExpression
    metrics: typing.List[Metric]
    dimensions: typing.List[Dimension]
    entity: Entity
    cohortSpec: CohortSpec
    pivots: typing.List[Pivot]
    keepEmptyRows: bool
    currencyCode: str
    dateRanges: typing.List[DateRange]
    returnPropertyQuota: bool
    dimensionFilter: FilterExpression

class MetricMetadata(typing_extensions.TypedDict, total=False):
    uiName: str
    expression: str
    apiName: str
    description: str
    type: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "TYPE_INTEGER",
        "TYPE_FLOAT",
        "TYPE_SECONDS",
        "TYPE_CURRENCY",
    ]
    deprecatedApiNames: typing.List[str]

class Filter(typing_extensions.TypedDict, total=False):
    nullFilter: bool
    fieldName: str
    stringFilter: StringFilter
    inListFilter: InListFilter
    betweenFilter: BetweenFilter
    numericFilter: NumericFilter

class Pivot(typing_extensions.TypedDict, total=False):
    offset: str
    limit: str
    orderBys: typing.List[OrderBy]
    metricAggregations: typing.List[str]
    fieldNames: typing.List[str]

class DimensionHeader(typing_extensions.TypedDict, total=False):
    name: str

class CaseExpression(typing_extensions.TypedDict, total=False):
    dimensionName: str

class FilterExpressionList(typing_extensions.TypedDict, total=False):
    expressions: typing.List[FilterExpression]

class CohortReportSettings(typing_extensions.TypedDict, total=False):
    accumulate: bool

class StringFilter(typing_extensions.TypedDict, total=False):
    matchType: typing_extensions.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
        "PARTIAL_REGEXP",
    ]
    caseSensitive: bool
    value: str

class DimensionExpression(typing_extensions.TypedDict, total=False):
    upperCase: CaseExpression
    concatenate: ConcatenateExpression
    lowerCase: CaseExpression

class FilterExpression(typing.Dict[str, typing.Any]): ...

class PivotHeader(typing_extensions.TypedDict, total=False):
    rowCount: int
    pivotDimensionHeaders: typing.List[PivotDimensionHeader]

class BatchRunReportsResponse(typing_extensions.TypedDict, total=False):
    reports: typing.List[RunReportResponse]

class PropertyQuota(typing_extensions.TypedDict, total=False):
    serverErrorsPerProjectPerHour: QuotaStatus
    tokensPerDay: QuotaStatus
    tokensPerHour: QuotaStatus
    concurrentRequests: QuotaStatus

class DimensionOrderBy(typing_extensions.TypedDict, total=False):
    orderType: typing_extensions.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "ALPHANUMERIC",
        "CASE_INSENSITIVE_ALPHANUMERIC",
        "NUMERIC",
    ]
    dimensionName: str

class Entity(typing_extensions.TypedDict, total=False):
    propertyId: str

class QuotaStatus(typing_extensions.TypedDict, total=False):
    consumed: int
    remaining: int

class ResponseMetaData(typing_extensions.TypedDict, total=False):
    dataLossFromOtherRow: bool

class DimensionValue(typing_extensions.TypedDict, total=False):
    value: str

class InListFilter(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    values: typing.List[str]

class MetricOrderBy(typing_extensions.TypedDict, total=False):
    metricName: str

class OrderBy(typing_extensions.TypedDict, total=False):
    dimension: DimensionOrderBy
    metric: MetricOrderBy
    pivot: PivotOrderBy
    desc: bool

class RunReportResponse(typing_extensions.TypedDict, total=False):
    propertyQuota: PropertyQuota
    maximums: typing.List[Row]
    totals: typing.List[Row]
    metadata: ResponseMetaData
    rows: typing.List[Row]
    minimums: typing.List[Row]
    dimensionHeaders: typing.List[DimensionHeader]
    rowCount: int
    metricHeaders: typing.List[MetricHeader]

class MetricValue(typing_extensions.TypedDict, total=False):
    value: str

class UniversalMetadata(typing_extensions.TypedDict, total=False):
    metrics: typing.List[MetricMetadata]
    dimensions: typing.List[DimensionMetadata]

class CohortSpec(typing_extensions.TypedDict, total=False):
    cohortReportSettings: CohortReportSettings
    cohortsRange: CohortsRange
    cohorts: typing.List[Cohort]

class Cohort(typing_extensions.TypedDict, total=False):
    name: str
    dateRange: DateRange
    dimension: str

class Metric(typing_extensions.TypedDict, total=False):
    name: str
    invisible: bool
    expression: str

class Dimension(typing_extensions.TypedDict, total=False):
    dimensionExpression: DimensionExpression
    name: str

class PivotDimensionHeader(typing_extensions.TypedDict, total=False):
    dimensionValues: typing.List[DimensionValue]

class CohortsRange(typing_extensions.TypedDict, total=False):
    startOffset: int
    endOffset: int
    granularity: typing_extensions.Literal[
        "GRANULARITY_UNSPECIFIED", "DAILY", "WEEKLY", "MONTHLY"
    ]

class BatchRunPivotReportsRequest(typing_extensions.TypedDict, total=False):
    entity: Entity
    requests: typing.List[RunPivotReportRequest]

class ConcatenateExpression(typing_extensions.TypedDict, total=False):
    dimensionNames: typing.List[str]
    delimiter: str

class BetweenFilter(typing_extensions.TypedDict, total=False):
    fromValue: NumericValue
    toValue: NumericValue

class BatchRunPivotReportsResponse(typing_extensions.TypedDict, total=False):
    pivotReports: typing.List[RunPivotReportResponse]

class Row(typing_extensions.TypedDict, total=False):
    metricValues: typing.List[MetricValue]
    dimensionValues: typing.List[DimensionValue]
