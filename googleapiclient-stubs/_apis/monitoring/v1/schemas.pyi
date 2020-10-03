import typing

import typing_extensions

class Dashboard(typing_extensions.TypedDict, total=False):
    name: str
    gridLayout: GridLayout
    etag: str
    mosaicLayout: MosaicLayout
    displayName: str
    rowLayout: RowLayout
    columnLayout: ColumnLayout

class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

class Aggregation(typing_extensions.TypedDict, total=False):
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
    groupByFields: typing.List[str]
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

class Field(typing_extensions.TypedDict, total=False):
    number: int
    typeUrl: str
    jsonName: str
    name: str
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    defaultValue: str
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
    packed: bool
    options: typing.List[Option]
    oneofIndex: int

class DataSet(typing_extensions.TypedDict, total=False):
    plotType: typing_extensions.Literal[
        "PLOT_TYPE_UNSPECIFIED", "LINE", "STACKED_AREA", "STACKED_BAR", "HEATMAP"
    ]
    minAlignmentPeriod: str
    legendTemplate: str
    timeSeriesQuery: TimeSeriesQuery

class GaugeView(typing_extensions.TypedDict, total=False):
    lowerBound: float
    upperBound: float

class StatisticalTimeSeriesFilter(typing_extensions.TypedDict, total=False):
    numTimeSeries: int
    rankingMethod: typing_extensions.Literal[
        "METHOD_UNSPECIFIED", "METHOD_CLUSTER_OUTLIER"
    ]

class SparkChartView(typing_extensions.TypedDict, total=False):
    minAlignmentPeriod: str
    sparkChartType: typing_extensions.Literal[
        "SPARK_CHART_TYPE_UNSPECIFIED", "SPARK_LINE", "SPARK_BAR"
    ]

class ColumnLayout(typing_extensions.TypedDict, total=False):
    columns: typing.List[Column]

class ListDashboardsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    dashboards: typing.List[Dashboard]

class Text(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "MARKDOWN", "RAW"]
    content: str

class Option(typing_extensions.TypedDict, total=False):
    value: typing.Dict[str, typing.Any]
    name: str

class Widget(typing_extensions.TypedDict, total=False):
    xyChart: XyChart
    title: str
    blank: Empty
    text: Text
    scorecard: Scorecard

class RowLayout(typing_extensions.TypedDict, total=False):
    rows: typing.List[Row]

class TimeSeriesFilterRatio(typing_extensions.TypedDict, total=False):
    denominator: RatioPart
    numerator: RatioPart
    secondaryAggregation: Aggregation
    pickTimeSeriesFilter: PickTimeSeriesFilter
    statisticalTimeSeriesFilter: StatisticalTimeSeriesFilter

class Empty(typing_extensions.TypedDict, total=False): ...

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class ChartOptions(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "COLOR", "X_RAY", "STATS"]

class Column(typing_extensions.TypedDict, total=False):
    widgets: typing.List[Widget]
    weight: str

class Tile(typing_extensions.TypedDict, total=False):
    height: int
    yPos: int
    widget: Widget
    width: int
    xPos: int

class TimeSeriesQuery(typing_extensions.TypedDict, total=False):
    timeSeriesQueryLanguage: str
    timeSeriesFilterRatio: TimeSeriesFilterRatio
    timeSeriesFilter: TimeSeriesFilter
    unitOverride: str

class GridLayout(typing_extensions.TypedDict, total=False):
    columns: str
    widgets: typing.List[Widget]

class DroppedLabels(typing_extensions.TypedDict, total=False):
    label: typing.Dict[str, typing.Any]

class RatioPart(typing_extensions.TypedDict, total=False):
    aggregation: Aggregation
    filter: str

class MosaicLayout(typing_extensions.TypedDict, total=False):
    columns: int
    tiles: typing.List[Tile]

class PickTimeSeriesFilter(typing_extensions.TypedDict, total=False):
    rankingMethod: typing_extensions.Literal[
        "METHOD_UNSPECIFIED",
        "METHOD_MEAN",
        "METHOD_MAX",
        "METHOD_MIN",
        "METHOD_SUM",
        "METHOD_LATEST",
    ]
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "TOP", "BOTTOM"]
    numTimeSeries: int

class Threshold(typing_extensions.TypedDict, total=False):
    color: typing_extensions.Literal["COLOR_UNSPECIFIED", "YELLOW", "RED"]
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "ABOVE", "BELOW"]
    label: str
    value: float

class Row(typing_extensions.TypedDict, total=False):
    widgets: typing.List[Widget]
    weight: str

class TimeSeriesFilter(typing_extensions.TypedDict, total=False):
    filter: str
    secondaryAggregation: Aggregation
    pickTimeSeriesFilter: PickTimeSeriesFilter
    aggregation: Aggregation
    statisticalTimeSeriesFilter: StatisticalTimeSeriesFilter

class Scorecard(typing_extensions.TypedDict, total=False):
    sparkChartView: SparkChartView
    thresholds: typing.List[Threshold]
    timeSeriesQuery: TimeSeriesQuery
    gaugeView: GaugeView

class XyChart(typing_extensions.TypedDict, total=False):
    dataSets: typing.List[DataSet]
    yAxis: Axis
    xAxis: Axis
    chartOptions: ChartOptions
    thresholds: typing.List[Threshold]
    timeshiftDuration: str

class Type(typing_extensions.TypedDict, total=False):
    name: str
    oneofs: typing.List[str]
    fields: typing.List[Field]
    sourceContext: SourceContext
    options: typing.List[Option]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

class Axis(typing_extensions.TypedDict, total=False):
    scale: typing_extensions.Literal["SCALE_UNSPECIFIED", "LINEAR", "LOG10"]
    label: str
