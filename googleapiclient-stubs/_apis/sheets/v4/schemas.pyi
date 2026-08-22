import typing

_list = list

@typing.type_check_only
class AddBandingRequest(typing.TypedDict, total=False):
    bandedRange: BandedRange

@typing.type_check_only
class AddBandingResponse(typing.TypedDict, total=False):
    bandedRange: BandedRange

@typing.type_check_only
class AddChartRequest(typing.TypedDict, total=False):
    chart: EmbeddedChart

@typing.type_check_only
class AddChartResponse(typing.TypedDict, total=False):
    chart: EmbeddedChart

@typing.type_check_only
class AddConditionalFormatRuleRequest(typing.TypedDict, total=False):
    index: int
    rule: ConditionalFormatRule

@typing.type_check_only
class AddDataSourceRequest(typing.TypedDict, total=False):
    dataSource: DataSource

@typing.type_check_only
class AddDataSourceResponse(typing.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    dataSource: DataSource

@typing.type_check_only
class AddDimensionGroupRequest(typing.TypedDict, total=False):
    range: DimensionRange

@typing.type_check_only
class AddDimensionGroupResponse(typing.TypedDict, total=False):
    dimensionGroups: _list[DimensionGroup]

@typing.type_check_only
class AddFilterViewRequest(typing.TypedDict, total=False):
    filter: FilterView

@typing.type_check_only
class AddFilterViewResponse(typing.TypedDict, total=False):
    filter: FilterView

@typing.type_check_only
class AddNamedRangeRequest(typing.TypedDict, total=False):
    namedRange: NamedRange

@typing.type_check_only
class AddNamedRangeResponse(typing.TypedDict, total=False):
    namedRange: NamedRange

@typing.type_check_only
class AddProtectedRangeRequest(typing.TypedDict, total=False):
    protectedRange: ProtectedRange

@typing.type_check_only
class AddProtectedRangeResponse(typing.TypedDict, total=False):
    protectedRange: ProtectedRange

@typing.type_check_only
class AddSheetRequest(typing.TypedDict, total=False):
    properties: SheetProperties

@typing.type_check_only
class AddSheetResponse(typing.TypedDict, total=False):
    properties: SheetProperties

@typing.type_check_only
class AddSlicerRequest(typing.TypedDict, total=False):
    slicer: Slicer

@typing.type_check_only
class AddSlicerResponse(typing.TypedDict, total=False):
    slicer: Slicer

@typing.type_check_only
class AddTableRequest(typing.TypedDict, total=False):
    table: Table

@typing.type_check_only
class AddTableResponse(typing.TypedDict, total=False):
    table: Table

@typing.type_check_only
class AppendCellsRequest(typing.TypedDict, total=False):
    fields: str
    rows: _list[RowData]
    sheetId: int
    tableId: str

@typing.type_check_only
class AppendDimensionRequest(typing.TypedDict, total=False):
    dimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
    length: int
    sheetId: int

@typing.type_check_only
class AppendValuesResponse(typing.TypedDict, total=False):
    spreadsheetId: str
    tableRange: str
    updates: UpdateValuesResponse

@typing.type_check_only
class AutoFillRequest(typing.TypedDict, total=False):
    range: GridRange
    sourceAndDestination: SourceAndDestination
    useAlternateSeries: bool

@typing.type_check_only
class AutoResizeDimensionsRequest(typing.TypedDict, total=False):
    dataSourceSheetDimensions: DataSourceSheetDimensionRange
    dimensions: DimensionRange

@typing.type_check_only
class BandedRange(typing.TypedDict, total=False):
    bandedRangeId: int
    bandedRangeReference: str
    columnProperties: BandingProperties
    range: GridRange
    rowProperties: BandingProperties

@typing.type_check_only
class BandingProperties(typing.TypedDict, total=False):
    firstBandColor: Color
    firstBandColorStyle: ColorStyle
    footerColor: Color
    footerColorStyle: ColorStyle
    headerColor: Color
    headerColorStyle: ColorStyle
    secondBandColor: Color
    secondBandColorStyle: ColorStyle

@typing.type_check_only
class BaselineValueFormat(typing.TypedDict, total=False):
    comparisonType: typing.Literal[
        "COMPARISON_TYPE_UNDEFINED", "ABSOLUTE_DIFFERENCE", "PERCENTAGE_DIFFERENCE"
    ]
    description: str
    negativeColor: Color
    negativeColorStyle: ColorStyle
    position: TextPosition
    positiveColor: Color
    positiveColorStyle: ColorStyle
    textFormat: TextFormat

@typing.type_check_only
class BasicChartAxis(typing.TypedDict, total=False):
    format: TextFormat
    position: typing.Literal[
        "BASIC_CHART_AXIS_POSITION_UNSPECIFIED",
        "BOTTOM_AXIS",
        "LEFT_AXIS",
        "RIGHT_AXIS",
    ]
    title: str
    titleTextPosition: TextPosition
    viewWindowOptions: ChartAxisViewWindowOptions

@typing.type_check_only
class BasicChartDomain(typing.TypedDict, total=False):
    domain: ChartData
    reversed: bool

@typing.type_check_only
class BasicChartSeries(typing.TypedDict, total=False):
    color: Color
    colorStyle: ColorStyle
    dataLabel: DataLabel
    lineStyle: LineStyle
    pointStyle: PointStyle
    series: ChartData
    styleOverrides: _list[BasicSeriesDataPointStyleOverride]
    targetAxis: typing.Literal[
        "BASIC_CHART_AXIS_POSITION_UNSPECIFIED",
        "BOTTOM_AXIS",
        "LEFT_AXIS",
        "RIGHT_AXIS",
    ]
    type: typing.Literal[
        "BASIC_CHART_TYPE_UNSPECIFIED",
        "BAR",
        "LINE",
        "AREA",
        "COLUMN",
        "SCATTER",
        "COMBO",
        "STEPPED_AREA",
    ]

@typing.type_check_only
class BasicChartSpec(typing.TypedDict, total=False):
    axis: _list[BasicChartAxis]
    chartType: typing.Literal[
        "BASIC_CHART_TYPE_UNSPECIFIED",
        "BAR",
        "LINE",
        "AREA",
        "COLUMN",
        "SCATTER",
        "COMBO",
        "STEPPED_AREA",
    ]
    compareMode: typing.Literal[
        "BASIC_CHART_COMPARE_MODE_UNSPECIFIED", "DATUM", "CATEGORY"
    ]
    domains: _list[BasicChartDomain]
    headerCount: int
    interpolateNulls: bool
    legendPosition: typing.Literal[
        "BASIC_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
    ]
    lineSmoothing: bool
    series: _list[BasicChartSeries]
    stackedType: typing.Literal[
        "BASIC_CHART_STACKED_TYPE_UNSPECIFIED",
        "NOT_STACKED",
        "STACKED",
        "PERCENT_STACKED",
    ]
    threeDimensional: bool
    totalDataLabel: DataLabel

@typing.type_check_only
class BasicFilter(typing.TypedDict, total=False):
    criteria: dict[str, typing.Any]
    filterSpecs: _list[FilterSpec]
    range: GridRange
    sortSpecs: _list[SortSpec]
    tableId: str

@typing.type_check_only
class BasicSeriesDataPointStyleOverride(typing.TypedDict, total=False):
    color: Color
    colorStyle: ColorStyle
    index: int
    pointStyle: PointStyle

@typing.type_check_only
class BatchClearValuesByDataFilterRequest(typing.TypedDict, total=False):
    dataFilters: _list[DataFilter]

@typing.type_check_only
class BatchClearValuesByDataFilterResponse(typing.TypedDict, total=False):
    clearedRanges: _list[str]
    spreadsheetId: str

@typing.type_check_only
class BatchClearValuesRequest(typing.TypedDict, total=False):
    ranges: _list[str]

@typing.type_check_only
class BatchClearValuesResponse(typing.TypedDict, total=False):
    clearedRanges: _list[str]
    spreadsheetId: str

@typing.type_check_only
class BatchGetValuesByDataFilterRequest(typing.TypedDict, total=False):
    dataFilters: _list[DataFilter]
    dateTimeRenderOption: typing.Literal["SERIAL_NUMBER", "FORMATTED_STRING"]
    majorDimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
    valueRenderOption: typing.Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]

@typing.type_check_only
class BatchGetValuesByDataFilterResponse(typing.TypedDict, total=False):
    spreadsheetId: str
    valueRanges: _list[MatchedValueRange]

@typing.type_check_only
class BatchGetValuesResponse(typing.TypedDict, total=False):
    spreadsheetId: str
    valueRanges: _list[ValueRange]

@typing.type_check_only
class BatchUpdateSpreadsheetRequest(typing.TypedDict, total=False):
    includeSpreadsheetInResponse: bool
    requests: _list[Request]
    responseIncludeGridData: bool
    responseRanges: _list[str]

@typing.type_check_only
class BatchUpdateSpreadsheetResponse(typing.TypedDict, total=False):
    replies: _list[Response]
    spreadsheetId: str
    updatedSpreadsheet: Spreadsheet

@typing.type_check_only
class BatchUpdateValuesByDataFilterRequest(typing.TypedDict, total=False):
    data: _list[DataFilterValueRange]
    includeValuesInResponse: bool
    responseDateTimeRenderOption: typing.Literal["SERIAL_NUMBER", "FORMATTED_STRING"]
    responseValueRenderOption: typing.Literal[
        "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
    ]
    valueInputOption: typing.Literal[
        "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
    ]

@typing.type_check_only
class BatchUpdateValuesByDataFilterResponse(typing.TypedDict, total=False):
    responses: _list[UpdateValuesByDataFilterResponse]
    spreadsheetId: str
    totalUpdatedCells: int
    totalUpdatedColumns: int
    totalUpdatedRows: int
    totalUpdatedSheets: int

@typing.type_check_only
class BatchUpdateValuesRequest(typing.TypedDict, total=False):
    data: _list[ValueRange]
    includeValuesInResponse: bool
    responseDateTimeRenderOption: typing.Literal["SERIAL_NUMBER", "FORMATTED_STRING"]
    responseValueRenderOption: typing.Literal[
        "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
    ]
    valueInputOption: typing.Literal[
        "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
    ]

@typing.type_check_only
class BatchUpdateValuesResponse(typing.TypedDict, total=False):
    responses: _list[UpdateValuesResponse]
    spreadsheetId: str
    totalUpdatedCells: int
    totalUpdatedColumns: int
    totalUpdatedRows: int
    totalUpdatedSheets: int

@typing.type_check_only
class BigQueryDataSourceSpec(typing.TypedDict, total=False):
    projectId: str
    querySpec: BigQueryQuerySpec
    tableSpec: BigQueryTableSpec

@typing.type_check_only
class BigQueryQuerySpec(typing.TypedDict, total=False):
    rawQuery: str

@typing.type_check_only
class BigQueryTableSpec(typing.TypedDict, total=False):
    datasetId: str
    tableId: str
    tableProjectId: str

@typing.type_check_only
class BooleanCondition(typing.TypedDict, total=False):
    type: typing.Literal[
        "CONDITION_TYPE_UNSPECIFIED",
        "NUMBER_GREATER",
        "NUMBER_GREATER_THAN_EQ",
        "NUMBER_LESS",
        "NUMBER_LESS_THAN_EQ",
        "NUMBER_EQ",
        "NUMBER_NOT_EQ",
        "NUMBER_BETWEEN",
        "NUMBER_NOT_BETWEEN",
        "TEXT_CONTAINS",
        "TEXT_NOT_CONTAINS",
        "TEXT_STARTS_WITH",
        "TEXT_ENDS_WITH",
        "TEXT_EQ",
        "TEXT_IS_EMAIL",
        "TEXT_IS_URL",
        "DATE_EQ",
        "DATE_BEFORE",
        "DATE_AFTER",
        "DATE_ON_OR_BEFORE",
        "DATE_ON_OR_AFTER",
        "DATE_BETWEEN",
        "DATE_NOT_BETWEEN",
        "DATE_IS_VALID",
        "ONE_OF_RANGE",
        "ONE_OF_LIST",
        "BLANK",
        "NOT_BLANK",
        "CUSTOM_FORMULA",
        "BOOLEAN",
        "TEXT_NOT_EQ",
        "DATE_NOT_EQ",
        "FILTER_EXPRESSION",
    ]
    values: _list[ConditionValue]

@typing.type_check_only
class BooleanRule(typing.TypedDict, total=False):
    condition: BooleanCondition
    format: CellFormat

@typing.type_check_only
class Border(typing.TypedDict, total=False):
    color: Color
    colorStyle: ColorStyle
    style: typing.Literal[
        "STYLE_UNSPECIFIED",
        "DOTTED",
        "DASHED",
        "SOLID",
        "SOLID_MEDIUM",
        "SOLID_THICK",
        "NONE",
        "DOUBLE",
    ]
    width: int

@typing.type_check_only
class Borders(typing.TypedDict, total=False):
    bottom: Border
    left: Border
    right: Border
    top: Border

@typing.type_check_only
class BubbleChartSpec(typing.TypedDict, total=False):
    bubbleBorderColor: Color
    bubbleBorderColorStyle: ColorStyle
    bubbleLabels: ChartData
    bubbleMaxRadiusSize: int
    bubbleMinRadiusSize: int
    bubbleOpacity: float
    bubbleSizes: ChartData
    bubbleTextStyle: TextFormat
    domain: ChartData
    groupIds: ChartData
    legendPosition: typing.Literal[
        "BUBBLE_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
        "INSIDE_LEGEND",
    ]
    series: ChartData

@typing.type_check_only
class CancelDataSourceRefreshRequest(typing.TypedDict, total=False):
    dataSourceId: str
    isAll: bool
    references: DataSourceObjectReferences

@typing.type_check_only
class CancelDataSourceRefreshResponse(typing.TypedDict, total=False):
    statuses: _list[CancelDataSourceRefreshStatus]

@typing.type_check_only
class CancelDataSourceRefreshStatus(typing.TypedDict, total=False):
    reference: DataSourceObjectReference
    refreshCancellationStatus: RefreshCancellationStatus

@typing.type_check_only
class CandlestickChartSpec(typing.TypedDict, total=False):
    data: _list[CandlestickData]
    domain: CandlestickDomain

@typing.type_check_only
class CandlestickData(typing.TypedDict, total=False):
    closeSeries: CandlestickSeries
    highSeries: CandlestickSeries
    lowSeries: CandlestickSeries
    openSeries: CandlestickSeries

@typing.type_check_only
class CandlestickDomain(typing.TypedDict, total=False):
    data: ChartData
    reversed: bool

@typing.type_check_only
class CandlestickSeries(typing.TypedDict, total=False):
    data: ChartData

@typing.type_check_only
class CellData(typing.TypedDict, total=False):
    chipRuns: _list[ChipRun]
    dataSourceFormula: DataSourceFormula
    dataSourceTable: DataSourceTable
    dataValidation: DataValidationRule
    effectiveFormat: CellFormat
    effectiveValue: ExtendedValue
    formattedValue: str
    hyperlink: str
    note: str
    pivotTable: PivotTable
    textFormatRuns: _list[TextFormatRun]
    userEnteredFormat: CellFormat
    userEnteredValue: ExtendedValue

@typing.type_check_only
class CellFormat(typing.TypedDict, total=False):
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    borders: Borders
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"
    ]
    hyperlinkDisplayType: typing.Literal[
        "HYPERLINK_DISPLAY_TYPE_UNSPECIFIED", "LINKED", "PLAIN_TEXT"
    ]
    numberFormat: NumberFormat
    padding: Padding
    textDirection: typing.Literal[
        "TEXT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    textFormat: TextFormat
    textRotation: TextRotation
    verticalAlignment: typing.Literal[
        "VERTICAL_ALIGN_UNSPECIFIED", "TOP", "MIDDLE", "BOTTOM"
    ]
    wrapStrategy: typing.Literal[
        "WRAP_STRATEGY_UNSPECIFIED", "OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", "WRAP"
    ]

@typing.type_check_only
class ChartAxisViewWindowOptions(typing.TypedDict, total=False):
    viewWindowMax: float
    viewWindowMin: float
    viewWindowMode: typing.Literal[
        "DEFAULT_VIEW_WINDOW_MODE", "VIEW_WINDOW_MODE_UNSUPPORTED", "EXPLICIT", "PRETTY"
    ]

@typing.type_check_only
class ChartCustomNumberFormatOptions(typing.TypedDict, total=False):
    prefix: str
    suffix: str

@typing.type_check_only
class ChartData(typing.TypedDict, total=False):
    aggregateType: typing.Literal[
        "CHART_AGGREGATE_TYPE_UNSPECIFIED",
        "AVERAGE",
        "COUNT",
        "MAX",
        "MEDIAN",
        "MIN",
        "SUM",
    ]
    columnReference: DataSourceColumnReference
    groupRule: ChartGroupRule
    sourceRange: ChartSourceRange

@typing.type_check_only
class ChartDateTimeRule(typing.TypedDict, total=False):
    type: typing.Literal[
        "CHART_DATE_TIME_RULE_TYPE_UNSPECIFIED",
        "SECOND",
        "MINUTE",
        "HOUR",
        "HOUR_MINUTE",
        "HOUR_MINUTE_AMPM",
        "DAY_OF_WEEK",
        "DAY_OF_YEAR",
        "DAY_OF_MONTH",
        "DAY_MONTH",
        "MONTH",
        "QUARTER",
        "YEAR",
        "YEAR_MONTH",
        "YEAR_QUARTER",
        "YEAR_MONTH_DAY",
    ]

@typing.type_check_only
class ChartGroupRule(typing.TypedDict, total=False):
    dateTimeRule: ChartDateTimeRule
    histogramRule: ChartHistogramRule

@typing.type_check_only
class ChartHistogramRule(typing.TypedDict, total=False):
    intervalSize: float
    maxValue: float
    minValue: float

@typing.type_check_only
class ChartSourceRange(typing.TypedDict, total=False):
    sources: _list[GridRange]

@typing.type_check_only
class ChartSpec(typing.TypedDict, total=False):
    altText: str
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    basicChart: BasicChartSpec
    bubbleChart: BubbleChartSpec
    candlestickChart: CandlestickChartSpec
    dataSourceChartProperties: DataSourceChartProperties
    filterSpecs: _list[FilterSpec]
    fontName: str
    hiddenDimensionStrategy: typing.Literal[
        "CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED",
        "SKIP_HIDDEN_ROWS_AND_COLUMNS",
        "SKIP_HIDDEN_ROWS",
        "SKIP_HIDDEN_COLUMNS",
        "SHOW_ALL",
    ]
    histogramChart: HistogramChartSpec
    maximized: bool
    orgChart: OrgChartSpec
    pieChart: PieChartSpec
    scorecardChart: ScorecardChartSpec
    sortSpecs: _list[SortSpec]
    subtitle: str
    subtitleTextFormat: TextFormat
    subtitleTextPosition: TextPosition
    title: str
    titleTextFormat: TextFormat
    titleTextPosition: TextPosition
    treemapChart: TreemapChartSpec
    waterfallChart: WaterfallChartSpec

@typing.type_check_only
class Chip(typing.TypedDict, total=False):
    personProperties: PersonProperties
    richLinkProperties: RichLinkProperties

@typing.type_check_only
class ChipRun(typing.TypedDict, total=False):
    chip: Chip
    startIndex: int

@typing.type_check_only
class ClearBasicFilterRequest(typing.TypedDict, total=False):
    sheetId: int

@typing.type_check_only
class ClearValuesRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClearValuesResponse(typing.TypedDict, total=False):
    clearedRange: str
    spreadsheetId: str

@typing.type_check_only
class Color(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class ColorStyle(typing.TypedDict, total=False):
    rgbColor: Color
    themeColor: typing.Literal[
        "THEME_COLOR_TYPE_UNSPECIFIED",
        "TEXT",
        "BACKGROUND",
        "ACCENT1",
        "ACCENT2",
        "ACCENT3",
        "ACCENT4",
        "ACCENT5",
        "ACCENT6",
        "LINK",
    ]

@typing.type_check_only
class ConditionValue(typing.TypedDict, total=False):
    relativeDate: typing.Literal[
        "RELATIVE_DATE_UNSPECIFIED",
        "PAST_YEAR",
        "PAST_MONTH",
        "PAST_WEEK",
        "YESTERDAY",
        "TODAY",
        "TOMORROW",
    ]
    userEnteredValue: str

@typing.type_check_only
class ConditionalFormatRule(typing.TypedDict, total=False):
    booleanRule: BooleanRule
    gradientRule: GradientRule
    ranges: _list[GridRange]

@typing.type_check_only
class CopyPasteRequest(typing.TypedDict, total=False):
    destination: GridRange
    pasteOrientation: typing.Literal["NORMAL", "TRANSPOSE"]
    pasteType: typing.Literal[
        "PASTE_NORMAL",
        "PASTE_VALUES",
        "PASTE_FORMAT",
        "PASTE_NO_BORDERS",
        "PASTE_FORMULA",
        "PASTE_DATA_VALIDATION",
        "PASTE_CONDITIONAL_FORMATTING",
    ]
    source: GridRange

@typing.type_check_only
class CopySheetToAnotherSpreadsheetRequest(typing.TypedDict, total=False):
    destinationSpreadsheetId: str

@typing.type_check_only
class CreateDeveloperMetadataRequest(typing.TypedDict, total=False):
    developerMetadata: DeveloperMetadata

@typing.type_check_only
class CreateDeveloperMetadataResponse(typing.TypedDict, total=False):
    developerMetadata: DeveloperMetadata

@typing.type_check_only
class CutPasteRequest(typing.TypedDict, total=False):
    destination: GridCoordinate
    pasteType: typing.Literal[
        "PASTE_NORMAL",
        "PASTE_VALUES",
        "PASTE_FORMAT",
        "PASTE_NO_BORDERS",
        "PASTE_FORMULA",
        "PASTE_DATA_VALIDATION",
        "PASTE_CONDITIONAL_FORMATTING",
    ]
    source: GridRange

@typing.type_check_only
class DataExecutionStatus(typing.TypedDict, total=False):
    errorCode: typing.Literal[
        "DATA_EXECUTION_ERROR_CODE_UNSPECIFIED",
        "TIMED_OUT",
        "TOO_MANY_ROWS",
        "TOO_MANY_COLUMNS",
        "TOO_MANY_CELLS",
        "ENGINE",
        "PARAMETER_INVALID",
        "UNSUPPORTED_DATA_TYPE",
        "DUPLICATE_COLUMN_NAMES",
        "INTERRUPTED",
        "CONCURRENT_QUERY",
        "OTHER",
        "TOO_MANY_CHARS_PER_CELL",
        "DATA_NOT_FOUND",
        "PERMISSION_DENIED",
        "MISSING_COLUMN_ALIAS",
        "OBJECT_NOT_FOUND",
        "OBJECT_IN_ERROR_STATE",
        "OBJECT_SPEC_INVALID",
        "DATA_EXECUTION_CANCELLED",
    ]
    errorMessage: str
    lastRefreshTime: str
    state: typing.Literal[
        "DATA_EXECUTION_STATE_UNSPECIFIED",
        "NOT_STARTED",
        "RUNNING",
        "CANCELLING",
        "SUCCEEDED",
        "FAILED",
    ]

@typing.type_check_only
class DataFilter(typing.TypedDict, total=False):
    a1Range: str
    developerMetadataLookup: DeveloperMetadataLookup
    gridRange: GridRange

@typing.type_check_only
class DataFilterValueRange(typing.TypedDict, total=False):
    dataFilter: DataFilter
    majorDimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
    values: _list[_list[typing.Any]]

@typing.type_check_only
class DataLabel(typing.TypedDict, total=False):
    customLabelData: ChartData
    placement: typing.Literal[
        "DATA_LABEL_PLACEMENT_UNSPECIFIED",
        "CENTER",
        "LEFT",
        "RIGHT",
        "ABOVE",
        "BELOW",
        "INSIDE_END",
        "INSIDE_BASE",
        "OUTSIDE_END",
    ]
    textFormat: TextFormat
    type: typing.Literal["DATA_LABEL_TYPE_UNSPECIFIED", "NONE", "DATA", "CUSTOM"]

@typing.type_check_only
class DataSource(typing.TypedDict, total=False):
    calculatedColumns: _list[DataSourceColumn]
    dataSourceId: str
    sheetId: int
    spec: DataSourceSpec

@typing.type_check_only
class DataSourceChartProperties(typing.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str

@typing.type_check_only
class DataSourceColumn(typing.TypedDict, total=False):
    formula: str
    reference: DataSourceColumnReference

@typing.type_check_only
class DataSourceColumnReference(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class DataSourceFormula(typing.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str

@typing.type_check_only
class DataSourceObjectReference(typing.TypedDict, total=False):
    chartId: int
    dataSourceFormulaCell: GridCoordinate
    dataSourcePivotTableAnchorCell: GridCoordinate
    dataSourceTableAnchorCell: GridCoordinate
    sheetId: str

@typing.type_check_only
class DataSourceObjectReferences(typing.TypedDict, total=False):
    references: _list[DataSourceObjectReference]

@typing.type_check_only
class DataSourceParameter(typing.TypedDict, total=False):
    name: str
    namedRangeId: str
    range: GridRange

@typing.type_check_only
class DataSourceRefreshDailySchedule(typing.TypedDict, total=False):
    startTime: TimeOfDay

@typing.type_check_only
class DataSourceRefreshMonthlySchedule(typing.TypedDict, total=False):
    daysOfMonth: _list[int]
    startTime: TimeOfDay

@typing.type_check_only
class DataSourceRefreshSchedule(typing.TypedDict, total=False):
    dailySchedule: DataSourceRefreshDailySchedule
    enabled: bool
    monthlySchedule: DataSourceRefreshMonthlySchedule
    nextRun: Interval
    refreshScope: typing.Literal[
        "DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED", "ALL_DATA_SOURCES"
    ]
    weeklySchedule: DataSourceRefreshWeeklySchedule

@typing.type_check_only
class DataSourceRefreshWeeklySchedule(typing.TypedDict, total=False):
    daysOfWeek: _list[
        typing.Literal[
            "DAY_OF_WEEK_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]
    startTime: TimeOfDay

@typing.type_check_only
class DataSourceSheetDimensionRange(typing.TypedDict, total=False):
    columnReferences: _list[DataSourceColumnReference]
    sheetId: int

@typing.type_check_only
class DataSourceSheetProperties(typing.TypedDict, total=False):
    columns: _list[DataSourceColumn]
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str

@typing.type_check_only
class DataSourceSpec(typing.TypedDict, total=False):
    bigQuery: BigQueryDataSourceSpec
    looker: LookerDataSourceSpec
    parameters: _list[DataSourceParameter]

@typing.type_check_only
class DataSourceTable(typing.TypedDict, total=False):
    columnSelectionType: typing.Literal[
        "DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED", "SELECTED", "SYNC_ALL"
    ]
    columns: _list[DataSourceColumnReference]
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str
    filterSpecs: _list[FilterSpec]
    rowLimit: int
    sortSpecs: _list[SortSpec]

@typing.type_check_only
class DataValidationRule(typing.TypedDict, total=False):
    condition: BooleanCondition
    inputMessage: str
    showCustomUi: bool
    strict: bool

@typing.type_check_only
class DateTimeRule(typing.TypedDict, total=False):
    type: typing.Literal[
        "DATE_TIME_RULE_TYPE_UNSPECIFIED",
        "SECOND",
        "MINUTE",
        "HOUR",
        "HOUR_MINUTE",
        "HOUR_MINUTE_AMPM",
        "DAY_OF_WEEK",
        "DAY_OF_YEAR",
        "DAY_OF_MONTH",
        "DAY_MONTH",
        "MONTH",
        "QUARTER",
        "YEAR",
        "YEAR_MONTH",
        "YEAR_QUARTER",
        "YEAR_MONTH_DAY",
    ]

@typing.type_check_only
class DeleteBandingRequest(typing.TypedDict, total=False):
    bandedRangeId: int

@typing.type_check_only
class DeleteConditionalFormatRuleRequest(typing.TypedDict, total=False):
    index: int
    sheetId: int

@typing.type_check_only
class DeleteConditionalFormatRuleResponse(typing.TypedDict, total=False):
    rule: ConditionalFormatRule

@typing.type_check_only
class DeleteDataSourceRequest(typing.TypedDict, total=False):
    dataSourceId: str

@typing.type_check_only
class DeleteDeveloperMetadataRequest(typing.TypedDict, total=False):
    dataFilter: DataFilter

@typing.type_check_only
class DeleteDeveloperMetadataResponse(typing.TypedDict, total=False):
    deletedDeveloperMetadata: _list[DeveloperMetadata]

@typing.type_check_only
class DeleteDimensionGroupRequest(typing.TypedDict, total=False):
    range: DimensionRange

@typing.type_check_only
class DeleteDimensionGroupResponse(typing.TypedDict, total=False):
    dimensionGroups: _list[DimensionGroup]

@typing.type_check_only
class DeleteDimensionRequest(typing.TypedDict, total=False):
    range: DimensionRange

@typing.type_check_only
class DeleteDuplicatesRequest(typing.TypedDict, total=False):
    comparisonColumns: _list[DimensionRange]
    range: GridRange

@typing.type_check_only
class DeleteDuplicatesResponse(typing.TypedDict, total=False):
    duplicatesRemovedCount: int

@typing.type_check_only
class DeleteEmbeddedObjectRequest(typing.TypedDict, total=False):
    objectId: int

@typing.type_check_only
class DeleteFilterViewRequest(typing.TypedDict, total=False):
    filterId: int

@typing.type_check_only
class DeleteNamedRangeRequest(typing.TypedDict, total=False):
    namedRangeId: str

@typing.type_check_only
class DeleteProtectedRangeRequest(typing.TypedDict, total=False):
    protectedRangeId: int

@typing.type_check_only
class DeleteRangeRequest(typing.TypedDict, total=False):
    range: GridRange
    shiftDimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]

@typing.type_check_only
class DeleteSheetRequest(typing.TypedDict, total=False):
    sheetId: int

@typing.type_check_only
class DeleteTableRequest(typing.TypedDict, total=False):
    tableId: str

@typing.type_check_only
class DeveloperMetadata(typing.TypedDict, total=False):
    location: DeveloperMetadataLocation
    metadataId: int
    metadataKey: str
    metadataValue: str
    visibility: typing.Literal[
        "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED", "DOCUMENT", "PROJECT"
    ]

@typing.type_check_only
class DeveloperMetadataLocation(typing.TypedDict, total=False):
    dimensionRange: DimensionRange
    locationType: typing.Literal[
        "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED",
        "ROW",
        "COLUMN",
        "SHEET",
        "SPREADSHEET",
    ]
    sheetId: int
    spreadsheet: bool

@typing.type_check_only
class DeveloperMetadataLookup(typing.TypedDict, total=False):
    locationMatchingStrategy: typing.Literal[
        "DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED",
        "EXACT_LOCATION",
        "INTERSECTING_LOCATION",
    ]
    locationType: typing.Literal[
        "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED",
        "ROW",
        "COLUMN",
        "SHEET",
        "SPREADSHEET",
    ]
    metadataId: int
    metadataKey: str
    metadataLocation: DeveloperMetadataLocation
    metadataValue: str
    visibility: typing.Literal[
        "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED", "DOCUMENT", "PROJECT"
    ]

@typing.type_check_only
class DimensionGroup(typing.TypedDict, total=False):
    collapsed: bool
    depth: int
    range: DimensionRange

@typing.type_check_only
class DimensionProperties(typing.TypedDict, total=False):
    dataSourceColumnReference: DataSourceColumnReference
    developerMetadata: _list[DeveloperMetadata]
    hiddenByFilter: bool
    hiddenByUser: bool
    pixelSize: int

@typing.type_check_only
class DimensionRange(typing.TypedDict, total=False):
    dimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
    endIndex: int
    sheetId: int
    startIndex: int

@typing.type_check_only
class DuplicateFilterViewRequest(typing.TypedDict, total=False):
    filterId: int

@typing.type_check_only
class DuplicateFilterViewResponse(typing.TypedDict, total=False):
    filter: FilterView

@typing.type_check_only
class DuplicateSheetRequest(typing.TypedDict, total=False):
    insertSheetIndex: int
    newSheetId: int
    newSheetName: str
    sourceSheetId: int

@typing.type_check_only
class DuplicateSheetResponse(typing.TypedDict, total=False):
    properties: SheetProperties

@typing.type_check_only
class Editors(typing.TypedDict, total=False):
    domainUsersCanEdit: bool
    groups: _list[str]
    users: _list[str]

@typing.type_check_only
class EmbeddedChart(typing.TypedDict, total=False):
    border: EmbeddedObjectBorder
    chartId: int
    position: EmbeddedObjectPosition
    spec: ChartSpec

@typing.type_check_only
class EmbeddedObjectBorder(typing.TypedDict, total=False):
    color: Color
    colorStyle: ColorStyle

@typing.type_check_only
class EmbeddedObjectPosition(typing.TypedDict, total=False):
    newSheet: bool
    overlayPosition: OverlayPosition
    sheetId: int

@typing.type_check_only
class ErrorValue(typing.TypedDict, total=False):
    message: str
    type: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "ERROR",
        "NULL_VALUE",
        "DIVIDE_BY_ZERO",
        "VALUE",
        "REF",
        "NAME",
        "NUM",
        "N_A",
        "LOADING",
    ]

@typing.type_check_only
class ExtendedValue(typing.TypedDict, total=False):
    boolValue: bool
    errorValue: ErrorValue
    formulaValue: str
    numberValue: float
    stringValue: str

@typing.type_check_only
class FilterCriteria(typing.TypedDict, total=False):
    condition: BooleanCondition
    hiddenValues: _list[str]
    visibleBackgroundColor: Color
    visibleBackgroundColorStyle: ColorStyle
    visibleForegroundColor: Color
    visibleForegroundColorStyle: ColorStyle

@typing.type_check_only
class FilterSpec(typing.TypedDict, total=False):
    columnIndex: int
    dataSourceColumnReference: DataSourceColumnReference
    filterCriteria: FilterCriteria

@typing.type_check_only
class FilterView(typing.TypedDict, total=False):
    criteria: dict[str, typing.Any]
    filterSpecs: _list[FilterSpec]
    filterViewId: int
    namedRangeId: str
    range: GridRange
    sortSpecs: _list[SortSpec]
    tableId: str
    title: str

@typing.type_check_only
class FindReplaceRequest(typing.TypedDict, total=False):
    allSheets: bool
    find: str
    includeFormulas: bool
    matchCase: bool
    matchEntireCell: bool
    range: GridRange
    replacement: str
    searchByRegex: bool
    sheetId: int

@typing.type_check_only
class FindReplaceResponse(typing.TypedDict, total=False):
    formulasChanged: int
    occurrencesChanged: int
    rowsChanged: int
    sheetsChanged: int
    valuesChanged: int

@typing.type_check_only
class GetSpreadsheetByDataFilterRequest(typing.TypedDict, total=False):
    dataFilters: _list[DataFilter]
    excludeTablesInBandedRanges: bool
    includeGridData: bool

@typing.type_check_only
class GradientRule(typing.TypedDict, total=False):
    maxpoint: InterpolationPoint
    midpoint: InterpolationPoint
    minpoint: InterpolationPoint

@typing.type_check_only
class GridCoordinate(typing.TypedDict, total=False):
    columnIndex: int
    rowIndex: int
    sheetId: int

@typing.type_check_only
class GridData(typing.TypedDict, total=False):
    columnMetadata: _list[DimensionProperties]
    rowData: _list[RowData]
    rowMetadata: _list[DimensionProperties]
    startColumn: int
    startRow: int

@typing.type_check_only
class GridProperties(typing.TypedDict, total=False):
    columnCount: int
    columnGroupControlAfter: bool
    frozenColumnCount: int
    frozenRowCount: int
    hideGridlines: bool
    rowCount: int
    rowGroupControlAfter: bool

@typing.type_check_only
class GridRange(typing.TypedDict, total=False):
    endColumnIndex: int
    endRowIndex: int
    sheetId: int
    startColumnIndex: int
    startRowIndex: int

@typing.type_check_only
class HistogramChartSpec(typing.TypedDict, total=False):
    bucketSize: float
    legendPosition: typing.Literal[
        "HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
        "INSIDE_LEGEND",
    ]
    outlierPercentile: float
    series: _list[HistogramSeries]
    showItemDividers: bool

@typing.type_check_only
class HistogramRule(typing.TypedDict, total=False):
    end: float
    interval: float
    start: float

@typing.type_check_only
class HistogramSeries(typing.TypedDict, total=False):
    barColor: Color
    barColorStyle: ColorStyle
    data: ChartData

@typing.type_check_only
class InsertDimensionRequest(typing.TypedDict, total=False):
    inheritFromBefore: bool
    range: DimensionRange

@typing.type_check_only
class InsertRangeRequest(typing.TypedDict, total=False):
    range: GridRange
    shiftDimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]

@typing.type_check_only
class InterpolationPoint(typing.TypedDict, total=False):
    color: Color
    colorStyle: ColorStyle
    type: typing.Literal[
        "INTERPOLATION_POINT_TYPE_UNSPECIFIED",
        "MIN",
        "MAX",
        "NUMBER",
        "PERCENT",
        "PERCENTILE",
    ]
    value: str

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class IterativeCalculationSettings(typing.TypedDict, total=False):
    convergenceThreshold: float
    maxIterations: int

@typing.type_check_only
class KeyValueFormat(typing.TypedDict, total=False):
    position: TextPosition
    textFormat: TextFormat

@typing.type_check_only
class LineStyle(typing.TypedDict, total=False):
    type: typing.Literal[
        "LINE_DASH_TYPE_UNSPECIFIED",
        "INVISIBLE",
        "CUSTOM",
        "SOLID",
        "DOTTED",
        "MEDIUM_DASHED",
        "MEDIUM_DASHED_DOTTED",
        "LONG_DASHED",
        "LONG_DASHED_DOTTED",
    ]
    width: int

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class LookerDataSourceSpec(typing.TypedDict, total=False):
    explore: str
    instanceUri: str
    model: str

@typing.type_check_only
class ManualRule(typing.TypedDict, total=False):
    groups: _list[ManualRuleGroup]

@typing.type_check_only
class ManualRuleGroup(typing.TypedDict, total=False):
    groupName: ExtendedValue
    items: _list[ExtendedValue]

@typing.type_check_only
class MatchedDeveloperMetadata(typing.TypedDict, total=False):
    dataFilters: _list[DataFilter]
    developerMetadata: DeveloperMetadata

@typing.type_check_only
class MatchedValueRange(typing.TypedDict, total=False):
    dataFilters: _list[DataFilter]
    valueRange: ValueRange

@typing.type_check_only
class MergeCellsRequest(typing.TypedDict, total=False):
    mergeType: typing.Literal["MERGE_ALL", "MERGE_COLUMNS", "MERGE_ROWS"]
    range: GridRange

@typing.type_check_only
class MoveDimensionRequest(typing.TypedDict, total=False):
    destinationIndex: int
    source: DimensionRange

@typing.type_check_only
class NamedRange(typing.TypedDict, total=False):
    name: str
    namedRangeId: str
    range: GridRange

@typing.type_check_only
class NumberFormat(typing.TypedDict, total=False):
    pattern: str
    type: typing.Literal[
        "NUMBER_FORMAT_TYPE_UNSPECIFIED",
        "TEXT",
        "NUMBER",
        "PERCENT",
        "CURRENCY",
        "DATE",
        "TIME",
        "DATE_TIME",
        "SCIENTIFIC",
    ]

@typing.type_check_only
class OrgChartSpec(typing.TypedDict, total=False):
    labels: ChartData
    nodeColor: Color
    nodeColorStyle: ColorStyle
    nodeSize: typing.Literal[
        "ORG_CHART_LABEL_SIZE_UNSPECIFIED", "SMALL", "MEDIUM", "LARGE"
    ]
    parentLabels: ChartData
    selectedNodeColor: Color
    selectedNodeColorStyle: ColorStyle
    tooltips: ChartData

@typing.type_check_only
class OverlayPosition(typing.TypedDict, total=False):
    anchorCell: GridCoordinate
    heightPixels: int
    offsetXPixels: int
    offsetYPixels: int
    widthPixels: int

@typing.type_check_only
class Padding(typing.TypedDict, total=False):
    bottom: int
    left: int
    right: int
    top: int

@typing.type_check_only
class PasteDataRequest(typing.TypedDict, total=False):
    coordinate: GridCoordinate
    data: str
    delimiter: str
    html: bool
    type: typing.Literal[
        "PASTE_NORMAL",
        "PASTE_VALUES",
        "PASTE_FORMAT",
        "PASTE_NO_BORDERS",
        "PASTE_FORMULA",
        "PASTE_DATA_VALIDATION",
        "PASTE_CONDITIONAL_FORMATTING",
    ]

@typing.type_check_only
class PersonProperties(typing.TypedDict, total=False):
    displayFormat: typing.Literal[
        "DISPLAY_FORMAT_UNSPECIFIED", "DEFAULT", "LAST_NAME_COMMA_FIRST_NAME", "EMAIL"
    ]
    email: str

@typing.type_check_only
class PieChartSpec(typing.TypedDict, total=False):
    domain: ChartData
    legendPosition: typing.Literal[
        "PIE_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
        "LABELED_LEGEND",
    ]
    pieHole: float
    series: ChartData
    threeDimensional: bool

@typing.type_check_only
class PivotFilterCriteria(typing.TypedDict, total=False):
    condition: BooleanCondition
    visibleByDefault: bool
    visibleValues: _list[str]

@typing.type_check_only
class PivotFilterSpec(typing.TypedDict, total=False):
    columnOffsetIndex: int
    dataSourceColumnReference: DataSourceColumnReference
    filterCriteria: PivotFilterCriteria

@typing.type_check_only
class PivotGroup(typing.TypedDict, total=False):
    dataSourceColumnReference: DataSourceColumnReference
    groupLimit: PivotGroupLimit
    groupRule: PivotGroupRule
    label: str
    repeatHeadings: bool
    showTotals: bool
    sortOrder: typing.Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]
    sourceColumnOffset: int
    valueBucket: PivotGroupSortValueBucket
    valueMetadata: _list[PivotGroupValueMetadata]

@typing.type_check_only
class PivotGroupLimit(typing.TypedDict, total=False):
    applyOrder: int
    countLimit: int

@typing.type_check_only
class PivotGroupRule(typing.TypedDict, total=False):
    dateTimeRule: DateTimeRule
    histogramRule: HistogramRule
    manualRule: ManualRule

@typing.type_check_only
class PivotGroupSortValueBucket(typing.TypedDict, total=False):
    buckets: _list[ExtendedValue]
    valuesIndex: int

@typing.type_check_only
class PivotGroupValueMetadata(typing.TypedDict, total=False):
    collapsed: bool
    value: ExtendedValue

@typing.type_check_only
class PivotTable(typing.TypedDict, total=False):
    columns: _list[PivotGroup]
    criteria: dict[str, typing.Any]
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str
    filterSpecs: _list[PivotFilterSpec]
    rows: _list[PivotGroup]
    source: GridRange
    valueLayout: typing.Literal["HORIZONTAL", "VERTICAL"]
    values: _list[PivotValue]

@typing.type_check_only
class PivotValue(typing.TypedDict, total=False):
    calculatedDisplayType: typing.Literal[
        "PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED",
        "PERCENT_OF_ROW_TOTAL",
        "PERCENT_OF_COLUMN_TOTAL",
        "PERCENT_OF_GRAND_TOTAL",
    ]
    dataSourceColumnReference: DataSourceColumnReference
    formula: str
    name: str
    sourceColumnOffset: int
    summarizeFunction: typing.Literal[
        "PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED",
        "SUM",
        "COUNTA",
        "COUNT",
        "COUNTUNIQUE",
        "AVERAGE",
        "MAX",
        "MIN",
        "MEDIAN",
        "PRODUCT",
        "STDEV",
        "STDEVP",
        "VAR",
        "VARP",
        "CUSTOM",
        "NONE",
    ]

@typing.type_check_only
class PointStyle(typing.TypedDict, total=False):
    shape: typing.Literal[
        "POINT_SHAPE_UNSPECIFIED",
        "CIRCLE",
        "DIAMOND",
        "HEXAGON",
        "PENTAGON",
        "SQUARE",
        "STAR",
        "TRIANGLE",
        "X_MARK",
    ]
    size: float

@typing.type_check_only
class ProtectedRange(typing.TypedDict, total=False):
    description: str
    editors: Editors
    namedRangeId: str
    protectedRangeId: int
    range: GridRange
    requestingUserCanEdit: bool
    tableId: str
    unprotectedRanges: _list[GridRange]
    warningOnly: bool

@typing.type_check_only
class RandomizeRangeRequest(typing.TypedDict, total=False):
    range: GridRange

@typing.type_check_only
class RefreshCancellationStatus(typing.TypedDict, total=False):
    errorCode: typing.Literal[
        "REFRESH_CANCELLATION_ERROR_CODE_UNSPECIFIED",
        "EXECUTION_NOT_FOUND",
        "CANCEL_PERMISSION_DENIED",
        "QUERY_EXECUTION_COMPLETED",
        "CONCURRENT_CANCELLATION",
        "CANCEL_OTHER_ERROR",
    ]
    state: typing.Literal[
        "REFRESH_CANCELLATION_STATE_UNSPECIFIED", "CANCEL_SUCCEEDED", "CANCEL_FAILED"
    ]

@typing.type_check_only
class RefreshDataSourceObjectExecutionStatus(typing.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    reference: DataSourceObjectReference

@typing.type_check_only
class RefreshDataSourceRequest(typing.TypedDict, total=False):
    dataSourceId: str
    force: bool
    isAll: bool
    references: DataSourceObjectReferences

@typing.type_check_only
class RefreshDataSourceResponse(typing.TypedDict, total=False):
    statuses: _list[RefreshDataSourceObjectExecutionStatus]

@typing.type_check_only
class RepeatCellRequest(typing.TypedDict, total=False):
    cell: CellData
    fields: str
    range: GridRange

@typing.type_check_only
class Request(typing.TypedDict, total=False):
    addBanding: AddBandingRequest
    addChart: AddChartRequest
    addConditionalFormatRule: AddConditionalFormatRuleRequest
    addDataSource: AddDataSourceRequest
    addDimensionGroup: AddDimensionGroupRequest
    addFilterView: AddFilterViewRequest
    addNamedRange: AddNamedRangeRequest
    addProtectedRange: AddProtectedRangeRequest
    addSheet: AddSheetRequest
    addSlicer: AddSlicerRequest
    addTable: AddTableRequest
    appendCells: AppendCellsRequest
    appendDimension: AppendDimensionRequest
    autoFill: AutoFillRequest
    autoResizeDimensions: AutoResizeDimensionsRequest
    cancelDataSourceRefresh: CancelDataSourceRefreshRequest
    clearBasicFilter: ClearBasicFilterRequest
    copyPaste: CopyPasteRequest
    createDeveloperMetadata: CreateDeveloperMetadataRequest
    cutPaste: CutPasteRequest
    deleteBanding: DeleteBandingRequest
    deleteConditionalFormatRule: DeleteConditionalFormatRuleRequest
    deleteDataSource: DeleteDataSourceRequest
    deleteDeveloperMetadata: DeleteDeveloperMetadataRequest
    deleteDimension: DeleteDimensionRequest
    deleteDimensionGroup: DeleteDimensionGroupRequest
    deleteDuplicates: DeleteDuplicatesRequest
    deleteEmbeddedObject: DeleteEmbeddedObjectRequest
    deleteFilterView: DeleteFilterViewRequest
    deleteNamedRange: DeleteNamedRangeRequest
    deleteProtectedRange: DeleteProtectedRangeRequest
    deleteRange: DeleteRangeRequest
    deleteSheet: DeleteSheetRequest
    deleteTable: DeleteTableRequest
    duplicateFilterView: DuplicateFilterViewRequest
    duplicateSheet: DuplicateSheetRequest
    findReplace: FindReplaceRequest
    insertDimension: InsertDimensionRequest
    insertRange: InsertRangeRequest
    mergeCells: MergeCellsRequest
    moveDimension: MoveDimensionRequest
    pasteData: PasteDataRequest
    randomizeRange: RandomizeRangeRequest
    refreshDataSource: RefreshDataSourceRequest
    repeatCell: RepeatCellRequest
    setBasicFilter: SetBasicFilterRequest
    setDataValidation: SetDataValidationRequest
    sortRange: SortRangeRequest
    textToColumns: TextToColumnsRequest
    trimWhitespace: TrimWhitespaceRequest
    unmergeCells: UnmergeCellsRequest
    updateBanding: UpdateBandingRequest
    updateBorders: UpdateBordersRequest
    updateCells: UpdateCellsRequest
    updateChartSpec: UpdateChartSpecRequest
    updateConditionalFormatRule: UpdateConditionalFormatRuleRequest
    updateDataSource: UpdateDataSourceRequest
    updateDeveloperMetadata: UpdateDeveloperMetadataRequest
    updateDimensionGroup: UpdateDimensionGroupRequest
    updateDimensionProperties: UpdateDimensionPropertiesRequest
    updateEmbeddedObjectBorder: UpdateEmbeddedObjectBorderRequest
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionRequest
    updateFilterView: UpdateFilterViewRequest
    updateNamedRange: UpdateNamedRangeRequest
    updateProtectedRange: UpdateProtectedRangeRequest
    updateSheetProperties: UpdateSheetPropertiesRequest
    updateSlicerSpec: UpdateSlicerSpecRequest
    updateSpreadsheetProperties: UpdateSpreadsheetPropertiesRequest
    updateTable: UpdateTableRequest

@typing.type_check_only
class Response(typing.TypedDict, total=False):
    addBanding: AddBandingResponse
    addChart: AddChartResponse
    addDataSource: AddDataSourceResponse
    addDimensionGroup: AddDimensionGroupResponse
    addFilterView: AddFilterViewResponse
    addNamedRange: AddNamedRangeResponse
    addProtectedRange: AddProtectedRangeResponse
    addSheet: AddSheetResponse
    addSlicer: AddSlicerResponse
    addTable: AddTableResponse
    cancelDataSourceRefresh: CancelDataSourceRefreshResponse
    createDeveloperMetadata: CreateDeveloperMetadataResponse
    deleteConditionalFormatRule: DeleteConditionalFormatRuleResponse
    deleteDeveloperMetadata: DeleteDeveloperMetadataResponse
    deleteDimensionGroup: DeleteDimensionGroupResponse
    deleteDuplicates: DeleteDuplicatesResponse
    duplicateFilterView: DuplicateFilterViewResponse
    duplicateSheet: DuplicateSheetResponse
    findReplace: FindReplaceResponse
    refreshDataSource: RefreshDataSourceResponse
    trimWhitespace: TrimWhitespaceResponse
    updateConditionalFormatRule: UpdateConditionalFormatRuleResponse
    updateDataSource: UpdateDataSourceResponse
    updateDeveloperMetadata: UpdateDeveloperMetadataResponse
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionResponse

@typing.type_check_only
class RichLinkProperties(typing.TypedDict, total=False):
    mimeType: str
    uri: str

@typing.type_check_only
class RowData(typing.TypedDict, total=False):
    values: _list[CellData]

@typing.type_check_only
class ScorecardChartSpec(typing.TypedDict, total=False):
    aggregateType: typing.Literal[
        "CHART_AGGREGATE_TYPE_UNSPECIFIED",
        "AVERAGE",
        "COUNT",
        "MAX",
        "MEDIAN",
        "MIN",
        "SUM",
    ]
    baselineValueData: ChartData
    baselineValueFormat: BaselineValueFormat
    customFormatOptions: ChartCustomNumberFormatOptions
    keyValueData: ChartData
    keyValueFormat: KeyValueFormat
    numberFormatSource: typing.Literal[
        "CHART_NUMBER_FORMAT_SOURCE_UNDEFINED", "FROM_DATA", "CUSTOM"
    ]
    scaleFactor: float

@typing.type_check_only
class SearchDeveloperMetadataRequest(typing.TypedDict, total=False):
    dataFilters: _list[DataFilter]

@typing.type_check_only
class SearchDeveloperMetadataResponse(typing.TypedDict, total=False):
    matchedDeveloperMetadata: _list[MatchedDeveloperMetadata]

@typing.type_check_only
class SetBasicFilterRequest(typing.TypedDict, total=False):
    filter: BasicFilter

@typing.type_check_only
class SetDataValidationRequest(typing.TypedDict, total=False):
    filteredRowsIncluded: bool
    range: GridRange
    rule: DataValidationRule

@typing.type_check_only
class Sheet(typing.TypedDict, total=False):
    bandedRanges: _list[BandedRange]
    basicFilter: BasicFilter
    charts: _list[EmbeddedChart]
    columnGroups: _list[DimensionGroup]
    conditionalFormats: _list[ConditionalFormatRule]
    data: _list[GridData]
    developerMetadata: _list[DeveloperMetadata]
    filterViews: _list[FilterView]
    merges: _list[GridRange]
    properties: SheetProperties
    protectedRanges: _list[ProtectedRange]
    rowGroups: _list[DimensionGroup]
    slicers: _list[Slicer]
    tables: _list[Table]

@typing.type_check_only
class SheetProperties(typing.TypedDict, total=False):
    dataSourceSheetProperties: DataSourceSheetProperties
    gridProperties: GridProperties
    hidden: bool
    index: int
    rightToLeft: bool
    sheetId: int
    sheetType: typing.Literal["SHEET_TYPE_UNSPECIFIED", "GRID", "OBJECT", "DATA_SOURCE"]
    tabColor: Color
    tabColorStyle: ColorStyle
    title: str

@typing.type_check_only
class Slicer(typing.TypedDict, total=False):
    position: EmbeddedObjectPosition
    slicerId: int
    spec: SlicerSpec

@typing.type_check_only
class SlicerSpec(typing.TypedDict, total=False):
    applyToPivotTables: bool
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    columnIndex: int
    dataRange: GridRange
    filterCriteria: FilterCriteria
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"
    ]
    textFormat: TextFormat
    title: str

@typing.type_check_only
class SortRangeRequest(typing.TypedDict, total=False):
    range: GridRange
    sortSpecs: _list[SortSpec]

@typing.type_check_only
class SortSpec(typing.TypedDict, total=False):
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    dataSourceColumnReference: DataSourceColumnReference
    dimensionIndex: int
    foregroundColor: Color
    foregroundColorStyle: ColorStyle
    sortOrder: typing.Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class SourceAndDestination(typing.TypedDict, total=False):
    dimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
    fillLength: int
    source: GridRange

@typing.type_check_only
class Spreadsheet(typing.TypedDict, total=False):
    dataSourceSchedules: _list[DataSourceRefreshSchedule]
    dataSources: _list[DataSource]
    developerMetadata: _list[DeveloperMetadata]
    namedRanges: _list[NamedRange]
    properties: SpreadsheetProperties
    sheets: _list[Sheet]
    spreadsheetId: str
    spreadsheetUrl: str

@typing.type_check_only
class SpreadsheetProperties(typing.TypedDict, total=False):
    autoRecalc: typing.Literal[
        "RECALCULATION_INTERVAL_UNSPECIFIED", "ON_CHANGE", "MINUTE", "HOUR"
    ]
    defaultFormat: CellFormat
    importFunctionsExternalUrlAccessAllowed: bool
    iterativeCalculationSettings: IterativeCalculationSettings
    locale: str
    spreadsheetTheme: SpreadsheetTheme
    timeZone: str
    title: str

@typing.type_check_only
class SpreadsheetTheme(typing.TypedDict, total=False):
    primaryFontFamily: str
    themeColors: _list[ThemeColorPair]

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    columnProperties: _list[TableColumnProperties]
    name: str
    range: GridRange
    rowsProperties: TableRowsProperties
    tableId: str

@typing.type_check_only
class TableColumnDataValidationRule(typing.TypedDict, total=False):
    condition: BooleanCondition

@typing.type_check_only
class TableColumnProperties(typing.TypedDict, total=False):
    columnIndex: int
    columnName: str
    columnType: typing.Literal[
        "COLUMN_TYPE_UNSPECIFIED",
        "DOUBLE",
        "CURRENCY",
        "PERCENT",
        "DATE",
        "TIME",
        "DATE_TIME",
        "TEXT",
        "BOOLEAN",
        "DROPDOWN",
        "FILES_CHIP",
        "PEOPLE_CHIP",
        "FINANCE_CHIP",
        "PLACE_CHIP",
        "RATINGS_CHIP",
    ]
    dataValidationRule: TableColumnDataValidationRule

@typing.type_check_only
class TableRowsProperties(typing.TypedDict, total=False):
    firstBandColorStyle: ColorStyle
    footerColorStyle: ColorStyle
    headerColorStyle: ColorStyle
    secondBandColorStyle: ColorStyle

@typing.type_check_only
class TextFormat(typing.TypedDict, total=False):
    bold: bool
    fontFamily: str
    fontSize: int
    foregroundColor: Color
    foregroundColorStyle: ColorStyle
    italic: bool
    link: Link
    strikethrough: bool
    underline: bool

@typing.type_check_only
class TextFormatRun(typing.TypedDict, total=False):
    format: TextFormat
    startIndex: int

@typing.type_check_only
class TextPosition(typing.TypedDict, total=False):
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"
    ]

@typing.type_check_only
class TextRotation(typing.TypedDict, total=False):
    angle: int
    vertical: bool

@typing.type_check_only
class TextToColumnsRequest(typing.TypedDict, total=False):
    delimiter: str
    delimiterType: typing.Literal[
        "DELIMITER_TYPE_UNSPECIFIED",
        "COMMA",
        "SEMICOLON",
        "PERIOD",
        "SPACE",
        "CUSTOM",
        "AUTODETECT",
    ]
    source: GridRange

@typing.type_check_only
class ThemeColorPair(typing.TypedDict, total=False):
    color: ColorStyle
    colorType: typing.Literal[
        "THEME_COLOR_TYPE_UNSPECIFIED",
        "TEXT",
        "BACKGROUND",
        "ACCENT1",
        "ACCENT2",
        "ACCENT3",
        "ACCENT4",
        "ACCENT5",
        "ACCENT6",
        "LINK",
    ]

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TreemapChartColorScale(typing.TypedDict, total=False):
    maxValueColor: Color
    maxValueColorStyle: ColorStyle
    midValueColor: Color
    midValueColorStyle: ColorStyle
    minValueColor: Color
    minValueColorStyle: ColorStyle
    noDataColor: Color
    noDataColorStyle: ColorStyle

@typing.type_check_only
class TreemapChartSpec(typing.TypedDict, total=False):
    colorData: ChartData
    colorScale: TreemapChartColorScale
    headerColor: Color
    headerColorStyle: ColorStyle
    hideTooltips: bool
    hintedLevels: int
    labels: ChartData
    levels: int
    maxValue: float
    minValue: float
    parentLabels: ChartData
    sizeData: ChartData
    textFormat: TextFormat

@typing.type_check_only
class TrimWhitespaceRequest(typing.TypedDict, total=False):
    range: GridRange

@typing.type_check_only
class TrimWhitespaceResponse(typing.TypedDict, total=False):
    cellsChangedCount: int

@typing.type_check_only
class UnmergeCellsRequest(typing.TypedDict, total=False):
    range: GridRange

@typing.type_check_only
class UpdateBandingRequest(typing.TypedDict, total=False):
    bandedRange: BandedRange
    fields: str

@typing.type_check_only
class UpdateBordersRequest(typing.TypedDict, total=False):
    bottom: Border
    innerHorizontal: Border
    innerVertical: Border
    left: Border
    range: GridRange
    right: Border
    top: Border

@typing.type_check_only
class UpdateCellsRequest(typing.TypedDict, total=False):
    fields: str
    range: GridRange
    rows: _list[RowData]
    start: GridCoordinate

@typing.type_check_only
class UpdateChartSpecRequest(typing.TypedDict, total=False):
    chartId: int
    spec: ChartSpec

@typing.type_check_only
class UpdateConditionalFormatRuleRequest(typing.TypedDict, total=False):
    index: int
    newIndex: int
    rule: ConditionalFormatRule
    sheetId: int

@typing.type_check_only
class UpdateConditionalFormatRuleResponse(typing.TypedDict, total=False):
    newIndex: int
    newRule: ConditionalFormatRule
    oldIndex: int
    oldRule: ConditionalFormatRule

@typing.type_check_only
class UpdateDataSourceRequest(typing.TypedDict, total=False):
    dataSource: DataSource
    fields: str

@typing.type_check_only
class UpdateDataSourceResponse(typing.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    dataSource: DataSource

@typing.type_check_only
class UpdateDeveloperMetadataRequest(typing.TypedDict, total=False):
    dataFilters: _list[DataFilter]
    developerMetadata: DeveloperMetadata
    fields: str

@typing.type_check_only
class UpdateDeveloperMetadataResponse(typing.TypedDict, total=False):
    developerMetadata: _list[DeveloperMetadata]

@typing.type_check_only
class UpdateDimensionGroupRequest(typing.TypedDict, total=False):
    dimensionGroup: DimensionGroup
    fields: str

@typing.type_check_only
class UpdateDimensionPropertiesRequest(typing.TypedDict, total=False):
    dataSourceSheetRange: DataSourceSheetDimensionRange
    fields: str
    properties: DimensionProperties
    range: DimensionRange

@typing.type_check_only
class UpdateEmbeddedObjectBorderRequest(typing.TypedDict, total=False):
    border: EmbeddedObjectBorder
    fields: str
    objectId: int

@typing.type_check_only
class UpdateEmbeddedObjectPositionRequest(typing.TypedDict, total=False):
    fields: str
    newPosition: EmbeddedObjectPosition
    objectId: int

@typing.type_check_only
class UpdateEmbeddedObjectPositionResponse(typing.TypedDict, total=False):
    position: EmbeddedObjectPosition

@typing.type_check_only
class UpdateFilterViewRequest(typing.TypedDict, total=False):
    fields: str
    filter: FilterView

@typing.type_check_only
class UpdateNamedRangeRequest(typing.TypedDict, total=False):
    fields: str
    namedRange: NamedRange

@typing.type_check_only
class UpdateProtectedRangeRequest(typing.TypedDict, total=False):
    fields: str
    protectedRange: ProtectedRange

@typing.type_check_only
class UpdateSheetPropertiesRequest(typing.TypedDict, total=False):
    fields: str
    properties: SheetProperties

@typing.type_check_only
class UpdateSlicerSpecRequest(typing.TypedDict, total=False):
    fields: str
    slicerId: int
    spec: SlicerSpec

@typing.type_check_only
class UpdateSpreadsheetPropertiesRequest(typing.TypedDict, total=False):
    fields: str
    properties: SpreadsheetProperties

@typing.type_check_only
class UpdateTableRequest(typing.TypedDict, total=False):
    fields: str
    table: Table

@typing.type_check_only
class UpdateValuesByDataFilterResponse(typing.TypedDict, total=False):
    dataFilter: DataFilter
    updatedCells: int
    updatedColumns: int
    updatedData: ValueRange
    updatedRange: str
    updatedRows: int

@typing.type_check_only
class UpdateValuesResponse(typing.TypedDict, total=False):
    spreadsheetId: str
    updatedCells: int
    updatedColumns: int
    updatedData: ValueRange
    updatedRange: str
    updatedRows: int

@typing.type_check_only
class ValueRange(typing.TypedDict, total=False):
    majorDimension: typing.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
    range: str
    values: _list[_list[typing.Any]]

@typing.type_check_only
class WaterfallChartColumnStyle(typing.TypedDict, total=False):
    color: Color
    colorStyle: ColorStyle
    label: str

@typing.type_check_only
class WaterfallChartCustomSubtotal(typing.TypedDict, total=False):
    dataIsSubtotal: bool
    label: str
    subtotalIndex: int

@typing.type_check_only
class WaterfallChartDomain(typing.TypedDict, total=False):
    data: ChartData
    reversed: bool

@typing.type_check_only
class WaterfallChartSeries(typing.TypedDict, total=False):
    customSubtotals: _list[WaterfallChartCustomSubtotal]
    data: ChartData
    dataLabel: DataLabel
    hideTrailingSubtotal: bool
    negativeColumnsStyle: WaterfallChartColumnStyle
    positiveColumnsStyle: WaterfallChartColumnStyle
    subtotalColumnsStyle: WaterfallChartColumnStyle

@typing.type_check_only
class WaterfallChartSpec(typing.TypedDict, total=False):
    connectorLineStyle: LineStyle
    domain: WaterfallChartDomain
    firstValueIsTotal: bool
    hideConnectorLines: bool
    series: _list[WaterfallChartSeries]
    stackedType: typing.Literal[
        "WATERFALL_STACKED_TYPE_UNSPECIFIED", "STACKED", "SEQUENTIAL"
    ]
    totalDataLabel: DataLabel
