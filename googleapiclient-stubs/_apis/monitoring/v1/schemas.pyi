import typing

import typing_extensions

_list = list

@typing.type_check_only
class Aggregation(typing_extensions.TypedDict, total=False):
    alignmentPeriod: str
    crossSeriesReducer: typing_extensions.Literal[
        "REDUCE_NONE",
        "REDUCE_MEAN",
        "REDUCE_MIN",
        "REDUCE_MAX",
        "REDUCE_SUM",
        "REDUCE_STDDEV",
        "REDUCE_COUNT",
        "REDUCE_COUNT_TRUE",
        "REDUCE_COUNT_FALSE",
        "REDUCE_FRACTION_TRUE",
        "REDUCE_PERCENTILE_99",
        "REDUCE_PERCENTILE_95",
        "REDUCE_PERCENTILE_50",
        "REDUCE_PERCENTILE_05",
    ]
    groupByFields: _list[str]
    perSeriesAligner: typing_extensions.Literal[
        "ALIGN_NONE",
        "ALIGN_DELTA",
        "ALIGN_RATE",
        "ALIGN_INTERPOLATE",
        "ALIGN_NEXT_OLDER",
        "ALIGN_MIN",
        "ALIGN_MAX",
        "ALIGN_MEAN",
        "ALIGN_COUNT",
        "ALIGN_SUM",
        "ALIGN_STDDEV",
        "ALIGN_COUNT_TRUE",
        "ALIGN_COUNT_FALSE",
        "ALIGN_FRACTION_TRUE",
        "ALIGN_PERCENTILE_99",
        "ALIGN_PERCENTILE_95",
        "ALIGN_PERCENTILE_50",
        "ALIGN_PERCENTILE_05",
        "ALIGN_PERCENT_CHANGE",
    ]

@typing.type_check_only
class AggregationFunction(typing_extensions.TypedDict, total=False):
    parameters: _list[Parameter]
    type: str

@typing.type_check_only
class AlertChart(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Axis(typing_extensions.TypedDict, total=False):
    label: str
    scale: typing_extensions.Literal["SCALE_UNSPECIFIED", "LINEAR", "LOG10"]

@typing.type_check_only
class Breakdown(typing_extensions.TypedDict, total=False):
    aggregationFunction: AggregationFunction
    column: str
    limit: int
    sortOrder: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED",
        "SORT_ORDER_NONE",
        "SORT_ORDER_ASCENDING",
        "SORT_ORDER_DESCENDING",
    ]

@typing.type_check_only
class ChartOptions(typing_extensions.TypedDict, total=False):
    displayHorizontal: bool
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "COLOR", "X_RAY", "STATS"]

@typing.type_check_only
class CollapsibleGroup(typing_extensions.TypedDict, total=False):
    collapsed: bool

@typing.type_check_only
class Column(typing_extensions.TypedDict, total=False):
    weight: str
    widgets: _list[Widget]

@typing.type_check_only
class ColumnLayout(typing_extensions.TypedDict, total=False):
    columns: _list[Column]

@typing.type_check_only
class ColumnSettings(typing_extensions.TypedDict, total=False):
    alignment: typing_extensions.Literal[
        "CELL_ALIGNMENT_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"
    ]
    column: str
    displayName: str
    thresholds: _list[Threshold]
    visible: bool

@typing.type_check_only
class ColumnSortingOptions(typing_extensions.TypedDict, total=False):
    column: str
    direction: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED",
        "SORT_ORDER_NONE",
        "SORT_ORDER_ASCENDING",
        "SORT_ORDER_DESCENDING",
    ]

@typing.type_check_only
class Dashboard(typing_extensions.TypedDict, total=False):
    annotations: DashboardAnnotations
    columnLayout: ColumnLayout
    dashboardFilters: _list[DashboardFilter]
    displayName: str
    etag: str
    gridLayout: GridLayout
    labels: dict[str, typing.Any]
    mosaicLayout: MosaicLayout
    name: str
    rowLayout: RowLayout

@typing.type_check_only
class DashboardAnnotations(typing_extensions.TypedDict, total=False):
    defaultResourceNames: _list[str]
    eventAnnotations: _list[EventAnnotation]

@typing.type_check_only
class DashboardFilter(typing_extensions.TypedDict, total=False):
    filterType: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "RESOURCE_LABEL",
        "METRIC_LABEL",
        "USER_METADATA_LABEL",
        "SYSTEM_METADATA_LABEL",
        "GROUP",
        "VALUE_ONLY",
    ]
    labelKey: str
    stringArray: StringArray
    stringArrayValue: StringArray
    stringValue: str
    templateVariable: str
    timeSeriesQuery: TimeSeriesQuery
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "STRING", "STRING_ARRAY"
    ]

@typing.type_check_only
class DataSet(typing_extensions.TypedDict, total=False):
    breakdowns: _list[Breakdown]
    dimensions: _list[Dimension]
    legendTemplate: str
    measures: _list[Measure]
    minAlignmentPeriod: str
    plotType: typing_extensions.Literal[
        "PLOT_TYPE_UNSPECIFIED", "LINE", "STACKED_AREA", "STACKED_BAR", "HEATMAP"
    ]
    sort: _list[ColumnSortingOptions]
    targetAxis: typing_extensions.Literal["TARGET_AXIS_UNSPECIFIED", "Y1", "Y2"]
    timeSeriesQuery: TimeSeriesQuery

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    column: str
    columnType: str
    floatBinSize: float
    maxBinCount: int
    numericBinSize: int
    sortColumn: str
    sortOrder: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED",
        "SORT_ORDER_NONE",
        "SORT_ORDER_ASCENDING",
        "SORT_ORDER_DESCENDING",
    ]
    timeBinSize: str

@typing.type_check_only
class DroppedLabels(typing_extensions.TypedDict, total=False):
    label: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ErrorReportingPanel(typing_extensions.TypedDict, total=False):
    projectNames: _list[str]
    services: _list[str]
    versions: _list[str]

@typing.type_check_only
class EventAnnotation(typing_extensions.TypedDict, total=False):
    displayName: str
    enabled: bool
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "GKE_WORKLOAD_DEPLOYMENT",
        "GKE_POD_CRASH",
        "GKE_POD_UNSCHEDULABLE",
        "GKE_CONTAINER_CREATION_FAILED",
        "GKE_CLUSTER_CREATE_DELETE",
        "GKE_CLUSTER_UPDATE",
        "GKE_NODE_POOL_UPDATE",
        "GKE_CLUSTER_AUTOSCALER",
        "GKE_POD_AUTOSCALER",
        "VM_TERMINATION",
        "VM_GUEST_OS_ERROR",
        "VM_START_FAILED",
        "MIG_UPDATE",
        "MIG_AUTOSCALER",
        "CLOUD_RUN_DEPLOYMENT",
        "CLOUD_SQL_FAILOVER",
        "CLOUD_SQL_START_STOP",
        "CLOUD_SQL_STORAGE",
        "UPTIME_CHECK_FAILURE",
        "CLOUD_ALERTING_ALERT",
        "SERVICE_HEALTH_INCIDENT",
        "SAP_BACKINT",
    ]
    filter: str
    resourceNames: _list[str]

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    defaultValue: str
    jsonName: str
    kind: typing_extensions.Literal[
        "TYPE_UNKNOWN",
        "TYPE_DOUBLE",
        "TYPE_FLOAT",
        "TYPE_INT64",
        "TYPE_UINT64",
        "TYPE_INT32",
        "TYPE_FIXED64",
        "TYPE_FIXED32",
        "TYPE_BOOL",
        "TYPE_STRING",
        "TYPE_GROUP",
        "TYPE_MESSAGE",
        "TYPE_BYTES",
        "TYPE_UINT32",
        "TYPE_ENUM",
        "TYPE_SFIXED32",
        "TYPE_SFIXED64",
        "TYPE_SINT32",
        "TYPE_SINT64",
    ]
    name: str
    number: int
    oneofIndex: int
    options: _list[Option]
    packed: bool
    typeUrl: str

@typing.type_check_only
class GaugeView(typing_extensions.TypedDict, total=False):
    lowerBound: float
    upperBound: float

@typing.type_check_only
class GridLayout(typing_extensions.TypedDict, total=False):
    columns: str
    widgets: _list[Widget]

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class IncidentList(typing_extensions.TypedDict, total=False):
    monitoredResources: _list[MonitoredResource]
    policyNames: _list[str]

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ListDashboardsResponse(typing_extensions.TypedDict, total=False):
    dashboards: _list[Dashboard]
    nextPageToken: str

@typing.type_check_only
class ListMetricsScopesByMonitoredProjectResponse(
    typing_extensions.TypedDict, total=False
):
    metricsScopes: _list[MetricsScope]

@typing.type_check_only
class LogsPanel(typing_extensions.TypedDict, total=False):
    filter: str
    resourceNames: _list[str]

@typing.type_check_only
class Measure(typing_extensions.TypedDict, total=False):
    aggregationFunction: AggregationFunction
    column: str

@typing.type_check_only
class MetricsScope(typing_extensions.TypedDict, total=False):
    createTime: str
    monitoredProjects: _list[MonitoredProject]
    name: str
    updateTime: str

@typing.type_check_only
class MonitoredProject(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str

@typing.type_check_only
class MonitoredResource(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class MosaicLayout(typing_extensions.TypedDict, total=False):
    columns: int
    tiles: _list[Tile]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class OpsAnalyticsQuery(typing_extensions.TypedDict, total=False):
    sql: str

@typing.type_check_only
class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: dict[str, typing.Any]

@typing.type_check_only
class Parameter(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str

@typing.type_check_only
class PickTimeSeriesFilter(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "TOP", "BOTTOM"]
    interval: Interval
    numTimeSeries: int
    rankingMethod: typing_extensions.Literal[
        "METHOD_UNSPECIFIED",
        "METHOD_MEAN",
        "METHOD_MAX",
        "METHOD_MIN",
        "METHOD_SUM",
        "METHOD_LATEST",
    ]

@typing.type_check_only
class PieChart(typing_extensions.TypedDict, total=False):
    chartType: typing_extensions.Literal["PIE_CHART_TYPE_UNSPECIFIED", "PIE", "DONUT"]
    dataSets: _list[PieChartDataSet]
    showLabels: bool

@typing.type_check_only
class PieChartDataSet(typing_extensions.TypedDict, total=False):
    dimensions: _list[Dimension]
    measures: _list[Measure]
    minAlignmentPeriod: str
    sliceNameTemplate: str
    timeSeriesQuery: TimeSeriesQuery

@typing.type_check_only
class QueryExemplarsRequest(typing_extensions.TypedDict, total=False):
    end: str
    query: str
    start: str

@typing.type_check_only
class QueryInstantRequest(typing_extensions.TypedDict, total=False):
    query: str
    time: str
    timeout: str

@typing.type_check_only
class QueryLabelsRequest(typing_extensions.TypedDict, total=False):
    end: str
    match: str
    start: str

@typing.type_check_only
class QueryRangeRequest(typing_extensions.TypedDict, total=False):
    end: str
    query: str
    start: str
    step: str
    timeout: str

@typing.type_check_only
class QuerySeriesRequest(typing_extensions.TypedDict, total=False):
    end: str
    start: str

@typing.type_check_only
class RatioPart(typing_extensions.TypedDict, total=False):
    aggregation: Aggregation
    filter: str

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    weight: str
    widgets: _list[Widget]

@typing.type_check_only
class RowLayout(typing_extensions.TypedDict, total=False):
    rows: _list[Row]

@typing.type_check_only
class Scorecard(typing_extensions.TypedDict, total=False):
    blankView: Empty
    dimensions: _list[Dimension]
    gaugeView: GaugeView
    measures: _list[Measure]
    sparkChartView: SparkChartView
    thresholds: _list[Threshold]
    timeSeriesQuery: TimeSeriesQuery

@typing.type_check_only
class SectionHeader(typing_extensions.TypedDict, total=False):
    dividerBelow: bool
    subtitle: str

@typing.type_check_only
class SingleViewGroup(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

@typing.type_check_only
class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

@typing.type_check_only
class SparkChartView(typing_extensions.TypedDict, total=False):
    minAlignmentPeriod: str
    sparkChartType: typing_extensions.Literal[
        "SPARK_CHART_TYPE_UNSPECIFIED", "SPARK_LINE", "SPARK_BAR"
    ]

@typing.type_check_only
class StatisticalTimeSeriesFilter(typing_extensions.TypedDict, total=False):
    numTimeSeries: int
    rankingMethod: typing_extensions.Literal[
        "METHOD_UNSPECIFIED", "METHOD_CLUSTER_OUTLIER"
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringArray(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class TableDataSet(typing_extensions.TypedDict, total=False):
    minAlignmentPeriod: str
    tableDisplayOptions: TableDisplayOptions
    tableTemplate: str
    timeSeriesQuery: TimeSeriesQuery

@typing.type_check_only
class TableDisplayOptions(typing_extensions.TypedDict, total=False):
    shownColumns: _list[str]

@typing.type_check_only
class Text(typing_extensions.TypedDict, total=False):
    content: str
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "MARKDOWN", "RAW"]
    style: TextStyle

@typing.type_check_only
class TextStyle(typing_extensions.TypedDict, total=False):
    backgroundColor: str
    fontSize: typing_extensions.Literal[
        "FONT_SIZE_UNSPECIFIED",
        "FS_EXTRA_SMALL",
        "FS_SMALL",
        "FS_MEDIUM",
        "FS_LARGE",
        "FS_EXTRA_LARGE",
    ]
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "H_LEFT", "H_CENTER", "H_RIGHT"
    ]
    padding: typing_extensions.Literal[
        "PADDING_SIZE_UNSPECIFIED",
        "P_EXTRA_SMALL",
        "P_SMALL",
        "P_MEDIUM",
        "P_LARGE",
        "P_EXTRA_LARGE",
    ]
    pointerLocation: typing_extensions.Literal[
        "POINTER_LOCATION_UNSPECIFIED",
        "PL_TOP",
        "PL_RIGHT",
        "PL_BOTTOM",
        "PL_LEFT",
        "PL_TOP_LEFT",
        "PL_TOP_RIGHT",
        "PL_RIGHT_TOP",
        "PL_RIGHT_BOTTOM",
        "PL_BOTTOM_RIGHT",
        "PL_BOTTOM_LEFT",
        "PL_LEFT_BOTTOM",
        "PL_LEFT_TOP",
    ]
    textColor: str
    verticalAlignment: typing_extensions.Literal[
        "VERTICAL_ALIGNMENT_UNSPECIFIED", "V_TOP", "V_CENTER", "V_BOTTOM"
    ]

@typing.type_check_only
class Threshold(typing_extensions.TypedDict, total=False):
    color: typing_extensions.Literal["COLOR_UNSPECIFIED", "YELLOW", "RED"]
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "ABOVE", "BELOW"]
    label: str
    targetAxis: typing_extensions.Literal["TARGET_AXIS_UNSPECIFIED", "Y1", "Y2"]
    value: float

@typing.type_check_only
class Tile(typing_extensions.TypedDict, total=False):
    height: int
    widget: Widget
    width: int
    xPos: int
    yPos: int

@typing.type_check_only
class TimeSeriesFilter(typing_extensions.TypedDict, total=False):
    aggregation: Aggregation
    filter: str
    pickTimeSeriesFilter: PickTimeSeriesFilter
    secondaryAggregation: Aggregation
    statisticalTimeSeriesFilter: StatisticalTimeSeriesFilter

@typing.type_check_only
class TimeSeriesFilterRatio(typing_extensions.TypedDict, total=False):
    denominator: RatioPart
    numerator: RatioPart
    pickTimeSeriesFilter: PickTimeSeriesFilter
    secondaryAggregation: Aggregation
    statisticalTimeSeriesFilter: StatisticalTimeSeriesFilter

@typing.type_check_only
class TimeSeriesQuery(typing_extensions.TypedDict, total=False):
    opsAnalyticsQuery: OpsAnalyticsQuery
    outputFullDuration: bool
    prometheusQuery: str
    timeSeriesFilter: TimeSeriesFilter
    timeSeriesFilterRatio: TimeSeriesFilterRatio
    timeSeriesQueryLanguage: str
    unitOverride: str

@typing.type_check_only
class TimeSeriesTable(typing_extensions.TypedDict, total=False):
    columnSettings: _list[ColumnSettings]
    dataSets: _list[TableDataSet]
    metricVisualization: typing_extensions.Literal[
        "METRIC_VISUALIZATION_UNSPECIFIED", "NUMBER", "BAR"
    ]

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    edition: str
    fields: _list[Field]
    name: str
    oneofs: _list[str]
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal[
        "SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"
    ]

@typing.type_check_only
class Widget(typing_extensions.TypedDict, total=False):
    alertChart: AlertChart
    blank: Empty
    collapsibleGroup: CollapsibleGroup
    errorReportingPanel: ErrorReportingPanel
    id: str
    incidentList: IncidentList
    logsPanel: LogsPanel
    pieChart: PieChart
    scorecard: Scorecard
    sectionHeader: SectionHeader
    singleViewGroup: SingleViewGroup
    text: Text
    timeSeriesTable: TimeSeriesTable
    title: str
    xyChart: XyChart

@typing.type_check_only
class XyChart(typing_extensions.TypedDict, total=False):
    chartOptions: ChartOptions
    dataSets: _list[DataSet]
    thresholds: _list[Threshold]
    timeshiftDuration: str
    xAxis: Axis
    y2Axis: Axis
    yAxis: Axis
