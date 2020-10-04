import typing

import typing_extensions
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
    groupByFields: typing.List[str]
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
class Axis(typing_extensions.TypedDict, total=False):
    label: str
    scale: typing_extensions.Literal["SCALE_UNSPECIFIED", "LINEAR", "LOG10"]

@typing.type_check_only
class ChartOptions(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "COLOR", "X_RAY", "STATS"]

@typing.type_check_only
class Column(typing_extensions.TypedDict, total=False):
    weight: str
    widgets: typing.List[Widget]

@typing.type_check_only
class ColumnLayout(typing_extensions.TypedDict, total=False):
    columns: typing.List[Column]

@typing.type_check_only
class Dashboard(typing_extensions.TypedDict, total=False):
    columnLayout: ColumnLayout
    displayName: str
    etag: str
    gridLayout: GridLayout
    mosaicLayout: MosaicLayout
    name: str
    rowLayout: RowLayout

@typing.type_check_only
class DataSet(typing_extensions.TypedDict, total=False):
    legendTemplate: str
    minAlignmentPeriod: str
    plotType: typing_extensions.Literal[
        "PLOT_TYPE_UNSPECIFIED", "LINE", "STACKED_AREA", "STACKED_BAR", "HEATMAP"
    ]
    timeSeriesQuery: TimeSeriesQuery

@typing.type_check_only
class DroppedLabels(typing_extensions.TypedDict, total=False):
    label: typing.Dict[str, typing.Any]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

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
    options: typing.List[Option]
    packed: bool
    typeUrl: str

@typing.type_check_only
class GaugeView(typing_extensions.TypedDict, total=False):
    lowerBound: float
    upperBound: float

@typing.type_check_only
class GridLayout(typing_extensions.TypedDict, total=False):
    columns: str
    widgets: typing.List[Widget]

@typing.type_check_only
class ListDashboardsResponse(typing_extensions.TypedDict, total=False):
    dashboards: typing.List[Dashboard]
    nextPageToken: str

@typing.type_check_only
class MosaicLayout(typing_extensions.TypedDict, total=False):
    columns: int
    tiles: typing.List[Tile]

@typing.type_check_only
class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

@typing.type_check_only
class PickTimeSeriesFilter(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "TOP", "BOTTOM"]
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
class RatioPart(typing_extensions.TypedDict, total=False):
    aggregation: Aggregation
    filter: str

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    weight: str
    widgets: typing.List[Widget]

@typing.type_check_only
class RowLayout(typing_extensions.TypedDict, total=False):
    rows: typing.List[Row]

@typing.type_check_only
class Scorecard(typing_extensions.TypedDict, total=False):
    gaugeView: GaugeView
    sparkChartView: SparkChartView
    thresholds: typing.List[Threshold]
    timeSeriesQuery: TimeSeriesQuery

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
class Text(typing_extensions.TypedDict, total=False):
    content: str
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "MARKDOWN", "RAW"]

@typing.type_check_only
class Threshold(typing_extensions.TypedDict, total=False):
    color: typing_extensions.Literal["COLOR_UNSPECIFIED", "YELLOW", "RED"]
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "ABOVE", "BELOW"]
    label: str
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
    timeSeriesFilter: TimeSeriesFilter
    timeSeriesFilterRatio: TimeSeriesFilterRatio
    timeSeriesQueryLanguage: str
    unitOverride: str

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    fields: typing.List[Field]
    name: str
    oneofs: typing.List[str]
    options: typing.List[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class Widget(typing_extensions.TypedDict, total=False):
    blank: Empty
    scorecard: Scorecard
    text: Text
    title: str
    xyChart: XyChart

@typing.type_check_only
class XyChart(typing_extensions.TypedDict, total=False):
    chartOptions: ChartOptions
    dataSets: typing.List[DataSet]
    thresholds: typing.List[Threshold]
    timeshiftDuration: str
    xAxis: Axis
    yAxis: Axis
