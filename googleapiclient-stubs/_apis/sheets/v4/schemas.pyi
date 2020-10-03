import typing

import typing_extensions

class DeleteDimensionRequest(typing_extensions.TypedDict, total=False):
    range: DimensionRange

class CutPasteRequest(typing_extensions.TypedDict, total=False):
    destination: GridCoordinate
    source: GridRange
    pasteType: typing_extensions.Literal[
        "PASTE_NORMAL",
        "PASTE_VALUES",
        "PASTE_FORMAT",
        "PASTE_NO_BORDERS",
        "PASTE_FORMULA",
        "PASTE_DATA_VALIDATION",
        "PASTE_CONDITIONAL_FORMATTING",
    ]

class BatchUpdateSpreadsheetResponse(typing_extensions.TypedDict, total=False):
    updatedSpreadsheet: Spreadsheet
    replies: typing.List[Response]
    spreadsheetId: str

class WaterfallChartDomain(typing_extensions.TypedDict, total=False):
    reversed: bool
    data: ChartData

class SheetProperties(typing_extensions.TypedDict, total=False):
    tabColor: Color
    tabColorStyle: ColorStyle
    hidden: bool
    gridProperties: GridProperties
    dataSourceSheetProperties: DataSourceSheetProperties
    sheetType: typing_extensions.Literal[
        "SHEET_TYPE_UNSPECIFIED", "GRID", "OBJECT", "DATA_SOURCE"
    ]
    index: int
    title: str
    rightToLeft: bool
    sheetId: int

class DeleteNamedRangeRequest(typing_extensions.TypedDict, total=False):
    namedRangeId: str

class Response(typing_extensions.TypedDict, total=False):
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionResponse
    addFilterView: AddFilterViewResponse
    addSlicer: AddSlicerResponse
    deleteDeveloperMetadata: DeleteDeveloperMetadataResponse
    addNamedRange: AddNamedRangeResponse
    findReplace: FindReplaceResponse
    addDimensionGroup: AddDimensionGroupResponse
    deleteDuplicates: DeleteDuplicatesResponse
    deleteConditionalFormatRule: DeleteConditionalFormatRuleResponse
    addProtectedRange: AddProtectedRangeResponse
    updateConditionalFormatRule: UpdateConditionalFormatRuleResponse
    trimWhitespace: TrimWhitespaceResponse
    addChart: AddChartResponse
    updateDeveloperMetadata: UpdateDeveloperMetadataResponse
    deleteDimensionGroup: DeleteDimensionGroupResponse
    addBanding: AddBandingResponse
    updateDataSource: UpdateDataSourceResponse
    addDataSource: AddDataSourceResponse
    refreshDataSource: RefreshDataSourceResponse
    createDeveloperMetadata: CreateDeveloperMetadataResponse
    addSheet: AddSheetResponse
    duplicateSheet: DuplicateSheetResponse
    duplicateFilterView: DuplicateFilterViewResponse

class ChartData(typing_extensions.TypedDict, total=False):
    sourceRange: ChartSourceRange
    aggregateType: typing_extensions.Literal[
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

class BasicFilter(typing_extensions.TypedDict, total=False):
    filterSpecs: typing.List[FilterSpec]
    sortSpecs: typing.List[SortSpec]
    criteria: typing.Dict[str, typing.Any]
    range: GridRange

class Editors(typing_extensions.TypedDict, total=False):
    groups: typing.List[str]
    users: typing.List[str]
    domainUsersCanEdit: bool

class SetDataValidationRequest(typing_extensions.TypedDict, total=False):
    range: GridRange
    rule: DataValidationRule

class FindReplaceResponse(typing_extensions.TypedDict, total=False):
    formulasChanged: int
    rowsChanged: int
    sheetsChanged: int
    occurrencesChanged: int
    valuesChanged: int

class FilterCriteria(typing_extensions.TypedDict, total=False):
    visibleBackgroundColorStyle: ColorStyle
    hiddenValues: typing.List[str]
    visibleBackgroundColor: Color
    visibleForegroundColor: Color
    visibleForegroundColorStyle: ColorStyle
    condition: BooleanCondition

class ConditionalFormatRule(typing_extensions.TypedDict, total=False):
    booleanRule: BooleanRule
    gradientRule: GradientRule
    ranges: typing.List[GridRange]

class SpreadsheetTheme(typing_extensions.TypedDict, total=False):
    primaryFontFamily: str
    themeColors: typing.List[ThemeColorPair]

class DeveloperMetadataLocation(typing_extensions.TypedDict, total=False):
    spreadsheet: bool
    locationType: typing_extensions.Literal[
        "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED",
        "ROW",
        "COLUMN",
        "SHEET",
        "SPREADSHEET",
    ]
    sheetId: int
    dimensionRange: DimensionRange

class UpdateNamedRangeRequest(typing_extensions.TypedDict, total=False):
    fields: str
    namedRange: NamedRange

class Padding(typing_extensions.TypedDict, total=False):
    right: int
    left: int
    top: int
    bottom: int

class SlicerSpec(typing_extensions.TypedDict, total=False):
    columnIndex: int
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    dataRange: GridRange
    filterCriteria: FilterCriteria
    title: str
    textFormat: TextFormat
    applyToPivotTables: bool
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"
    ]

class UpdateChartSpecRequest(typing_extensions.TypedDict, total=False):
    spec: ChartSpec
    chartId: int

class DataSourceObjectReferences(typing_extensions.TypedDict, total=False):
    references: typing.List[DataSourceObjectReference]

class BatchClearValuesRequest(typing_extensions.TypedDict, total=False):
    ranges: typing.List[str]

class ClearBasicFilterRequest(typing_extensions.TypedDict, total=False):
    sheetId: int

class DeleteDeveloperMetadataRequest(typing_extensions.TypedDict, total=False):
    dataFilter: DataFilter

class UpdateSpreadsheetPropertiesRequest(typing_extensions.TypedDict, total=False):
    properties: SpreadsheetProperties
    fields: str

class CreateDeveloperMetadataResponse(typing_extensions.TypedDict, total=False):
    developerMetadata: DeveloperMetadata

class Borders(typing_extensions.TypedDict, total=False):
    left: Border
    right: Border
    bottom: Border
    top: Border

class AddConditionalFormatRuleRequest(typing_extensions.TypedDict, total=False):
    rule: ConditionalFormatRule
    index: int

class GridData(typing_extensions.TypedDict, total=False):
    rowMetadata: typing.List[DimensionProperties]
    startColumn: int
    rowData: typing.List[RowData]
    startRow: int
    columnMetadata: typing.List[DimensionProperties]

class CandlestickChartSpec(typing_extensions.TypedDict, total=False):
    data: typing.List[CandlestickData]
    domain: CandlestickDomain

class DeveloperMetadata(typing_extensions.TypedDict, total=False):
    metadataId: int
    location: DeveloperMetadataLocation
    metadataValue: str
    visibility: typing_extensions.Literal[
        "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED", "DOCUMENT", "PROJECT"
    ]
    metadataKey: str

class RefreshDataSourceObjectExecutionStatus(typing_extensions.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    reference: DataSourceObjectReference

class RefreshDataSourceResponse(typing_extensions.TypedDict, total=False):
    statuses: typing.List[RefreshDataSourceObjectExecutionStatus]

class InsertDimensionRequest(typing_extensions.TypedDict, total=False):
    inheritFromBefore: bool
    range: DimensionRange

class LineStyle(typing_extensions.TypedDict, total=False):
    width: int
    type: typing_extensions.Literal[
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

class FilterSpec(typing_extensions.TypedDict, total=False):
    dataSourceColumnReference: DataSourceColumnReference
    filterCriteria: FilterCriteria
    columnIndex: int

class BatchUpdateValuesResponse(typing_extensions.TypedDict, total=False):
    totalUpdatedSheets: int
    totalUpdatedCells: int
    totalUpdatedColumns: int
    responses: typing.List[UpdateValuesResponse]
    totalUpdatedRows: int
    spreadsheetId: str

class PivotFilterCriteria(typing_extensions.TypedDict, total=False):
    visibleValues: typing.List[str]

class ChartSpec(typing_extensions.TypedDict, total=False):
    histogramChart: HistogramChartSpec
    dataSourceChartProperties: DataSourceChartProperties
    titleTextPosition: TextPosition
    fontName: str
    subtitleTextFormat: TextFormat
    basicChart: BasicChartSpec
    treemapChart: TreemapChartSpec
    backgroundColor: Color
    altText: str
    candlestickChart: CandlestickChartSpec
    titleTextFormat: TextFormat
    subtitle: str
    pieChart: PieChartSpec
    filterSpecs: typing.List[FilterSpec]
    backgroundColorStyle: ColorStyle
    waterfallChart: WaterfallChartSpec
    maximized: bool
    bubbleChart: BubbleChartSpec
    hiddenDimensionStrategy: typing_extensions.Literal[
        "CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED",
        "SKIP_HIDDEN_ROWS_AND_COLUMNS",
        "SKIP_HIDDEN_ROWS",
        "SKIP_HIDDEN_COLUMNS",
        "SHOW_ALL",
    ]
    sortSpecs: typing.List[SortSpec]
    orgChart: OrgChartSpec
    scorecardChart: ScorecardChartSpec
    subtitleTextPosition: TextPosition
    title: str

class PasteDataRequest(typing_extensions.TypedDict, total=False):
    delimiter: str
    html: bool
    data: str
    coordinate: GridCoordinate
    type: typing_extensions.Literal[
        "PASTE_NORMAL",
        "PASTE_VALUES",
        "PASTE_FORMAT",
        "PASTE_NO_BORDERS",
        "PASTE_FORMULA",
        "PASTE_DATA_VALIDATION",
        "PASTE_CONDITIONAL_FORMATTING",
    ]

class DeleteDataSourceRequest(typing_extensions.TypedDict, total=False):
    dataSourceId: str

class ErrorValue(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
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
    message: str

class AppendDimensionRequest(typing_extensions.TypedDict, total=False):
    length: int
    sheetId: int
    dimension: typing_extensions.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]

class UpdateCellsRequest(typing_extensions.TypedDict, total=False):
    fields: str
    rows: typing.List[RowData]
    start: GridCoordinate
    range: GridRange

class AddProtectedRangeResponse(typing_extensions.TypedDict, total=False):
    protectedRange: ProtectedRange

class AddSlicerRequest(typing_extensions.TypedDict, total=False):
    slicer: Slicer

class ChartSourceRange(typing_extensions.TypedDict, total=False):
    sources: typing.List[GridRange]

class PivotGroupLimit(typing_extensions.TypedDict, total=False):
    countLimit: int
    applyOrder: int

class MergeCellsRequest(typing_extensions.TypedDict, total=False):
    mergeType: typing_extensions.Literal["MERGE_ALL", "MERGE_COLUMNS", "MERGE_ROWS"]
    range: GridRange

class UpdateConditionalFormatRuleRequest(typing_extensions.TypedDict, total=False):
    sheetId: int
    index: int
    rule: ConditionalFormatRule
    newIndex: int

class BigQueryQuerySpec(typing_extensions.TypedDict, total=False):
    rawQuery: str

class TextRotation(typing_extensions.TypedDict, total=False):
    vertical: bool
    angle: int

class BatchUpdateValuesByDataFilterResponse(typing_extensions.TypedDict, total=False):
    totalUpdatedCells: int
    totalUpdatedRows: int
    responses: typing.List[UpdateValuesByDataFilterResponse]
    totalUpdatedColumns: int
    spreadsheetId: str
    totalUpdatedSheets: int

class OrgChartSpec(typing_extensions.TypedDict, total=False):
    labels: ChartData
    nodeSize: typing_extensions.Literal[
        "ORG_CHART_LABEL_SIZE_UNSPECIFIED", "SMALL", "MEDIUM", "LARGE"
    ]
    tooltips: ChartData
    parentLabels: ChartData
    selectedNodeColorStyle: ColorStyle
    nodeColorStyle: ColorStyle
    selectedNodeColor: Color
    nodeColor: Color

class BandingProperties(typing_extensions.TypedDict, total=False):
    footerColor: Color
    footerColorStyle: ColorStyle
    firstBandColorStyle: ColorStyle
    headerColorStyle: ColorStyle
    secondBandColorStyle: ColorStyle
    secondBandColor: Color
    headerColor: Color
    firstBandColor: Color

class UpdateBandingRequest(typing_extensions.TypedDict, total=False):
    fields: str
    bandedRange: BandedRange

class BigQueryDataSourceSpec(typing_extensions.TypedDict, total=False):
    tableSpec: BigQueryTableSpec
    projectId: str
    querySpec: BigQueryQuerySpec

class Request(typing_extensions.TypedDict, total=False):
    unmergeCells: UnmergeCellsRequest
    updateDimensionGroup: UpdateDimensionGroupRequest
    updateBanding: UpdateBandingRequest
    deleteDuplicates: DeleteDuplicatesRequest
    updateBorders: UpdateBordersRequest
    addChart: AddChartRequest
    mergeCells: MergeCellsRequest
    addSheet: AddSheetRequest
    addBanding: AddBandingRequest
    updateDeveloperMetadata: UpdateDeveloperMetadataRequest
    addConditionalFormatRule: AddConditionalFormatRuleRequest
    deleteDataSource: DeleteDataSourceRequest
    addFilterView: AddFilterViewRequest
    deleteDimension: DeleteDimensionRequest
    pasteData: PasteDataRequest
    updateSlicerSpec: UpdateSlicerSpecRequest
    deleteDimensionGroup: DeleteDimensionGroupRequest
    updateDimensionProperties: UpdateDimensionPropertiesRequest
    setBasicFilter: SetBasicFilterRequest
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionRequest
    deleteFilterView: DeleteFilterViewRequest
    addProtectedRange: AddProtectedRangeRequest
    autoFill: AutoFillRequest
    addDimensionGroup: AddDimensionGroupRequest
    refreshDataSource: RefreshDataSourceRequest
    updateProtectedRange: UpdateProtectedRangeRequest
    clearBasicFilter: ClearBasicFilterRequest
    updateSheetProperties: UpdateSheetPropertiesRequest
    deleteDeveloperMetadata: DeleteDeveloperMetadataRequest
    addSlicer: AddSlicerRequest
    duplicateSheet: DuplicateSheetRequest
    deleteSheet: DeleteSheetRequest
    duplicateFilterView: DuplicateFilterViewRequest
    deleteProtectedRange: DeleteProtectedRangeRequest
    moveDimension: MoveDimensionRequest
    trimWhitespace: TrimWhitespaceRequest
    setDataValidation: SetDataValidationRequest
    updateChartSpec: UpdateChartSpecRequest
    deleteEmbeddedObject: DeleteEmbeddedObjectRequest
    insertRange: InsertRangeRequest
    appendDimension: AppendDimensionRequest
    deleteBanding: DeleteBandingRequest
    updateDataSource: UpdateDataSourceRequest
    sortRange: SortRangeRequest
    addDataSource: AddDataSourceRequest
    updateFilterView: UpdateFilterViewRequest
    createDeveloperMetadata: CreateDeveloperMetadataRequest
    appendCells: AppendCellsRequest
    deleteNamedRange: DeleteNamedRangeRequest
    autoResizeDimensions: AutoResizeDimensionsRequest
    repeatCell: RepeatCellRequest
    insertDimension: InsertDimensionRequest
    updateNamedRange: UpdateNamedRangeRequest
    findReplace: FindReplaceRequest
    cutPaste: CutPasteRequest
    addNamedRange: AddNamedRangeRequest
    copyPaste: CopyPasteRequest
    deleteConditionalFormatRule: DeleteConditionalFormatRuleRequest
    updateCells: UpdateCellsRequest
    deleteRange: DeleteRangeRequest
    textToColumns: TextToColumnsRequest
    updateConditionalFormatRule: UpdateConditionalFormatRuleRequest
    randomizeRange: RandomizeRangeRequest
    updateSpreadsheetProperties: UpdateSpreadsheetPropertiesRequest

class BooleanCondition(typing_extensions.TypedDict, total=False):
    values: typing.List[ConditionValue]
    type: typing_extensions.Literal[
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
    ]

class AppendValuesResponse(typing_extensions.TypedDict, total=False):
    spreadsheetId: str
    tableRange: str
    updates: UpdateValuesResponse

class DeleteDimensionGroupRequest(typing_extensions.TypedDict, total=False):
    range: DimensionRange

class DataFilter(typing_extensions.TypedDict, total=False):
    gridRange: GridRange
    developerMetadataLookup: DeveloperMetadataLookup
    a1Range: str

class BatchUpdateValuesByDataFilterRequest(typing_extensions.TypedDict, total=False):
    valueInputOption: typing_extensions.Literal[
        "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
    ]
    data: typing.List[DataFilterValueRange]
    includeValuesInResponse: bool
    responseDateTimeRenderOption: typing_extensions.Literal[
        "SERIAL_NUMBER", "FORMATTED_STRING"
    ]
    responseValueRenderOption: typing_extensions.Literal[
        "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
    ]

class DimensionGroup(typing_extensions.TypedDict, total=False):
    range: DimensionRange
    collapsed: bool
    depth: int

class ColorStyle(typing_extensions.TypedDict, total=False):
    rgbColor: Color
    themeColor: typing_extensions.Literal[
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

class UpdateFilterViewRequest(typing_extensions.TypedDict, total=False):
    filter: FilterView
    fields: str

class DuplicateSheetResponse(typing_extensions.TypedDict, total=False):
    properties: SheetProperties

class CellData(typing_extensions.TypedDict, total=False):
    effectiveValue: ExtendedValue
    effectiveFormat: CellFormat
    dataSourceFormula: DataSourceFormula
    formattedValue: str
    hyperlink: str
    dataSourceTable: DataSourceTable
    userEnteredFormat: CellFormat
    textFormatRuns: typing.List[TextFormatRun]
    pivotTable: PivotTable
    dataValidation: DataValidationRule
    note: str
    userEnteredValue: ExtendedValue

class TextPosition(typing_extensions.TypedDict, total=False):
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"
    ]

class AddDimensionGroupRequest(typing_extensions.TypedDict, total=False):
    range: DimensionRange

class UpdateDeveloperMetadataRequest(typing_extensions.TypedDict, total=False):
    fields: str
    developerMetadata: DeveloperMetadata
    dataFilters: typing.List[DataFilter]

class Spreadsheet(typing_extensions.TypedDict, total=False):
    dataSourceSchedules: typing.List[DataSourceRefreshSchedule]
    namedRanges: typing.List[NamedRange]
    properties: SpreadsheetProperties
    spreadsheetId: str
    sheets: typing.List[Sheet]
    spreadsheetUrl: str
    dataSources: typing.List[DataSource]
    developerMetadata: typing.List[DeveloperMetadata]

class UpdateValuesResponse(typing_extensions.TypedDict, total=False):
    updatedData: ValueRange
    updatedColumns: int
    spreadsheetId: str
    updatedCells: int
    updatedRange: str
    updatedRows: int

class AddBandingResponse(typing_extensions.TypedDict, total=False):
    bandedRange: BandedRange

class DeleteDimensionGroupResponse(typing_extensions.TypedDict, total=False):
    dimensionGroups: typing.List[DimensionGroup]

class AddSheetResponse(typing_extensions.TypedDict, total=False):
    properties: SheetProperties

class EmbeddedObjectPosition(typing_extensions.TypedDict, total=False):
    sheetId: int
    newSheet: bool
    overlayPosition: OverlayPosition

class Color(typing_extensions.TypedDict, total=False):
    blue: float
    red: float
    green: float
    alpha: float

class DataSourceColumn(typing_extensions.TypedDict, total=False):
    reference: DataSourceColumnReference
    formula: str

class DeleteSheetRequest(typing_extensions.TypedDict, total=False):
    sheetId: int

class TextFormat(typing_extensions.TypedDict, total=False):
    bold: bool
    fontFamily: str
    foregroundColor: Color
    fontSize: int
    foregroundColorStyle: ColorStyle
    underline: bool
    italic: bool
    strikethrough: bool

class AddFilterViewRequest(typing_extensions.TypedDict, total=False):
    filter: FilterView

class AddFilterViewResponse(typing_extensions.TypedDict, total=False):
    filter: FilterView

class UpdateBordersRequest(typing_extensions.TypedDict, total=False):
    left: Border
    bottom: Border
    range: GridRange
    innerVertical: Border
    innerHorizontal: Border
    top: Border
    right: Border

class UnmergeCellsRequest(typing_extensions.TypedDict, total=False):
    range: GridRange

class DeleteRangeRequest(typing_extensions.TypedDict, total=False):
    range: GridRange
    shiftDimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
    ]

class DuplicateSheetRequest(typing_extensions.TypedDict, total=False):
    insertSheetIndex: int
    newSheetId: int
    newSheetName: str
    sourceSheetId: int

class DeleteBandingRequest(typing_extensions.TypedDict, total=False):
    bandedRangeId: int

class MatchedValueRange(typing_extensions.TypedDict, total=False):
    valueRange: ValueRange
    dataFilters: typing.List[DataFilter]

class ChartAxisViewWindowOptions(typing_extensions.TypedDict, total=False):
    viewWindowMode: typing_extensions.Literal[
        "DEFAULT_VIEW_WINDOW_MODE", "VIEW_WINDOW_MODE_UNSUPPORTED", "EXPLICIT", "PRETTY"
    ]
    viewWindowMin: float
    viewWindowMax: float

class AddDataSourceResponse(typing_extensions.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    dataSource: DataSource

class UpdateEmbeddedObjectPositionResponse(typing_extensions.TypedDict, total=False):
    position: EmbeddedObjectPosition

class MoveDimensionRequest(typing_extensions.TypedDict, total=False):
    destinationIndex: int
    source: DimensionRange

class IterativeCalculationSettings(typing_extensions.TypedDict, total=False):
    convergenceThreshold: float
    maxIterations: int

class DataSourceTable(typing_extensions.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    rowLimit: int
    columns: typing.List[DataSourceColumnReference]
    filterSpecs: typing.List[FilterSpec]
    dataSourceId: str
    columnSelectionType: typing_extensions.Literal[
        "DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED", "SELECTED", "SYNC_ALL"
    ]
    sortSpecs: typing.List[SortSpec]

class UpdateDimensionGroupRequest(typing_extensions.TypedDict, total=False):
    fields: str
    dimensionGroup: DimensionGroup

class UpdateSlicerSpecRequest(typing_extensions.TypedDict, total=False):
    fields: str
    slicerId: int
    spec: SlicerSpec

class ChartDateTimeRule(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
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

class DeleteDeveloperMetadataResponse(typing_extensions.TypedDict, total=False):
    deletedDeveloperMetadata: typing.List[DeveloperMetadata]

class DeveloperMetadataLookup(typing_extensions.TypedDict, total=False):
    locationType: typing_extensions.Literal[
        "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED",
        "ROW",
        "COLUMN",
        "SHEET",
        "SPREADSHEET",
    ]
    metadataId: int
    metadataKey: str
    visibility: typing_extensions.Literal[
        "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED", "DOCUMENT", "PROJECT"
    ]
    metadataLocation: DeveloperMetadataLocation
    locationMatchingStrategy: typing_extensions.Literal[
        "DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED",
        "EXACT_LOCATION",
        "INTERSECTING_LOCATION",
    ]
    metadataValue: str

class RefreshDataSourceRequest(typing_extensions.TypedDict, total=False):
    isAll: bool
    force: bool
    references: DataSourceObjectReferences
    dataSourceId: str

class DeleteConditionalFormatRuleResponse(typing_extensions.TypedDict, total=False):
    rule: ConditionalFormatRule

class SetBasicFilterRequest(typing_extensions.TypedDict, total=False):
    filter: BasicFilter

class FindReplaceRequest(typing_extensions.TypedDict, total=False):
    replacement: str
    range: GridRange
    searchByRegex: bool
    allSheets: bool
    matchCase: bool
    sheetId: int
    includeFormulas: bool
    find: str
    matchEntireCell: bool

class AddDataSourceRequest(typing_extensions.TypedDict, total=False):
    dataSource: DataSource

class OverlayPosition(typing_extensions.TypedDict, total=False):
    offsetYPixels: int
    anchorCell: GridCoordinate
    offsetXPixels: int
    heightPixels: int
    widthPixels: int

class ManualRuleGroup(typing_extensions.TypedDict, total=False):
    groupName: ExtendedValue
    items: typing.List[ExtendedValue]

class GridRange(typing_extensions.TypedDict, total=False):
    startColumnIndex: int
    startRowIndex: int
    sheetId: int
    endColumnIndex: int
    endRowIndex: int

class ConditionValue(typing_extensions.TypedDict, total=False):
    relativeDate: typing_extensions.Literal[
        "RELATIVE_DATE_UNSPECIFIED",
        "PAST_YEAR",
        "PAST_MONTH",
        "PAST_WEEK",
        "YESTERDAY",
        "TODAY",
        "TOMORROW",
    ]
    userEnteredValue: str

class TrimWhitespaceRequest(typing_extensions.TypedDict, total=False):
    range: GridRange

class PivotGroup(typing_extensions.TypedDict, total=False):
    label: str
    dataSourceColumnReference: DataSourceColumnReference
    valueBucket: PivotGroupSortValueBucket
    groupRule: PivotGroupRule
    valueMetadata: typing.List[PivotGroupValueMetadata]
    showTotals: bool
    sortOrder: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    repeatHeadings: bool
    sourceColumnOffset: int
    groupLimit: PivotGroupLimit

class AddProtectedRangeRequest(typing_extensions.TypedDict, total=False):
    protectedRange: ProtectedRange

class DataSourceParameter(typing_extensions.TypedDict, total=False):
    namedRangeId: str
    range: GridRange
    name: str

class InterpolationPoint(typing_extensions.TypedDict, total=False):
    colorStyle: ColorStyle
    value: str
    color: Color
    type: typing_extensions.Literal[
        "INTERPOLATION_POINT_TYPE_UNSPECIFIED",
        "MIN",
        "MAX",
        "NUMBER",
        "PERCENT",
        "PERCENTILE",
    ]

class BatchClearValuesResponse(typing_extensions.TypedDict, total=False):
    spreadsheetId: str
    clearedRanges: typing.List[str]

class DataFilterValueRange(typing_extensions.TypedDict, total=False):
    majorDimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
    ]
    values: typing.List[list]
    dataFilter: DataFilter

class ProtectedRange(typing_extensions.TypedDict, total=False):
    unprotectedRanges: typing.List[GridRange]
    editors: Editors
    warningOnly: bool
    requestingUserCanEdit: bool
    description: str
    range: GridRange
    namedRangeId: str
    protectedRangeId: int

class ThemeColorPair(typing_extensions.TypedDict, total=False):
    colorType: typing_extensions.Literal[
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
    color: ColorStyle

class SpreadsheetProperties(typing_extensions.TypedDict, total=False):
    autoRecalc: typing_extensions.Literal[
        "RECALCULATION_INTERVAL_UNSPECIFIED", "ON_CHANGE", "MINUTE", "HOUR"
    ]
    spreadsheetTheme: SpreadsheetTheme
    timeZone: str
    defaultFormat: CellFormat
    iterativeCalculationSettings: IterativeCalculationSettings
    locale: str
    title: str

class DateTimeRule(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
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

class PivotValue(typing_extensions.TypedDict, total=False):
    sourceColumnOffset: int
    dataSourceColumnReference: DataSourceColumnReference
    calculatedDisplayType: typing_extensions.Literal[
        "PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED",
        "PERCENT_OF_ROW_TOTAL",
        "PERCENT_OF_COLUMN_TOTAL",
        "PERCENT_OF_GRAND_TOTAL",
    ]
    summarizeFunction: typing_extensions.Literal[
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
    ]
    name: str
    formula: str

class TreemapChartColorScale(typing_extensions.TypedDict, total=False):
    noDataColorStyle: ColorStyle
    maxValueColorStyle: ColorStyle
    minValueColorStyle: ColorStyle
    midValueColorStyle: ColorStyle
    minValueColor: Color
    maxValueColor: Color
    midValueColor: Color
    noDataColor: Color

class CreateDeveloperMetadataRequest(typing_extensions.TypedDict, total=False):
    developerMetadata: DeveloperMetadata

class CopyPasteRequest(typing_extensions.TypedDict, total=False):
    source: GridRange
    pasteOrientation: typing_extensions.Literal["NORMAL", "TRANSPOSE"]
    pasteType: typing_extensions.Literal[
        "PASTE_NORMAL",
        "PASTE_VALUES",
        "PASTE_FORMAT",
        "PASTE_NO_BORDERS",
        "PASTE_FORMULA",
        "PASTE_DATA_VALIDATION",
        "PASTE_CONDITIONAL_FORMATTING",
    ]
    destination: GridRange

class DuplicateFilterViewResponse(typing_extensions.TypedDict, total=False):
    filter: FilterView

class TextToColumnsRequest(typing_extensions.TypedDict, total=False):
    source: GridRange
    delimiterType: typing_extensions.Literal[
        "DELIMITER_TYPE_UNSPECIFIED",
        "COMMA",
        "SEMICOLON",
        "PERIOD",
        "SPACE",
        "CUSTOM",
        "AUTODETECT",
    ]
    delimiter: str

class BatchUpdateValuesRequest(typing_extensions.TypedDict, total=False):
    valueInputOption: typing_extensions.Literal[
        "INPUT_VALUE_OPTION_UNSPECIFIED", "RAW", "USER_ENTERED"
    ]
    responseDateTimeRenderOption: typing_extensions.Literal[
        "SERIAL_NUMBER", "FORMATTED_STRING"
    ]
    data: typing.List[ValueRange]
    responseValueRenderOption: typing_extensions.Literal[
        "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
    ]
    includeValuesInResponse: bool

class AddSheetRequest(typing_extensions.TypedDict, total=False):
    properties: SheetProperties

class GetSpreadsheetByDataFilterRequest(typing_extensions.TypedDict, total=False):
    includeGridData: bool
    dataFilters: typing.List[DataFilter]

class FilterView(typing_extensions.TypedDict, total=False):
    filterSpecs: typing.List[FilterSpec]
    sortSpecs: typing.List[SortSpec]
    namedRangeId: str
    title: str
    criteria: typing.Dict[str, typing.Any]
    range: GridRange
    filterViewId: int

class SourceAndDestination(typing_extensions.TypedDict, total=False):
    source: GridRange
    fillLength: int
    dimension: typing_extensions.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]

class CandlestickSeries(typing_extensions.TypedDict, total=False):
    data: ChartData

class AddChartResponse(typing_extensions.TypedDict, total=False):
    chart: EmbeddedChart

class RandomizeRangeRequest(typing_extensions.TypedDict, total=False):
    range: GridRange

class CellFormat(typing_extensions.TypedDict, total=False):
    textRotation: TextRotation
    backgroundColor: Color
    padding: Padding
    wrapStrategy: typing_extensions.Literal[
        "WRAP_STRATEGY_UNSPECIFIED", "OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", "WRAP"
    ]
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"
    ]
    backgroundColorStyle: ColorStyle
    hyperlinkDisplayType: typing_extensions.Literal[
        "HYPERLINK_DISPLAY_TYPE_UNSPECIFIED", "LINKED", "PLAIN_TEXT"
    ]
    numberFormat: NumberFormat
    textFormat: TextFormat
    textDirection: typing_extensions.Literal[
        "TEXT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    verticalAlignment: typing_extensions.Literal[
        "VERTICAL_ALIGN_UNSPECIFIED", "TOP", "MIDDLE", "BOTTOM"
    ]
    borders: Borders

class SearchDeveloperMetadataResponse(typing_extensions.TypedDict, total=False):
    matchedDeveloperMetadata: typing.List[MatchedDeveloperMetadata]

class BasicChartAxis(typing_extensions.TypedDict, total=False):
    format: TextFormat
    title: str
    position: typing_extensions.Literal[
        "BASIC_CHART_AXIS_POSITION_UNSPECIFIED",
        "BOTTOM_AXIS",
        "LEFT_AXIS",
        "RIGHT_AXIS",
    ]
    titleTextPosition: TextPosition
    viewWindowOptions: ChartAxisViewWindowOptions

class KeyValueFormat(typing_extensions.TypedDict, total=False):
    position: TextPosition
    textFormat: TextFormat

class UpdateDeveloperMetadataResponse(typing_extensions.TypedDict, total=False):
    developerMetadata: typing.List[DeveloperMetadata]

class DataSourceSheetDimensionRange(typing_extensions.TypedDict, total=False):
    sheetId: int
    columnReferences: typing.List[DataSourceColumnReference]

class DataSourceChartProperties(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    dataExecutionStatus: DataExecutionStatus

class BandedRange(typing_extensions.TypedDict, total=False):
    columnProperties: BandingProperties
    range: GridRange
    rowProperties: BandingProperties
    bandedRangeId: int

class DataSourceRefreshDailySchedule(typing_extensions.TypedDict, total=False):
    startTime: TimeOfDay

class RepeatCellRequest(typing_extensions.TypedDict, total=False):
    fields: str
    range: GridRange
    cell: CellData

class Sheet(typing_extensions.TypedDict, total=False):
    basicFilter: BasicFilter
    rowGroups: typing.List[DimensionGroup]
    data: typing.List[GridData]
    merges: typing.List[GridRange]
    charts: typing.List[EmbeddedChart]
    conditionalFormats: typing.List[ConditionalFormatRule]
    properties: SheetProperties
    protectedRanges: typing.List[ProtectedRange]
    filterViews: typing.List[FilterView]
    bandedRanges: typing.List[BandedRange]
    slicers: typing.List[Slicer]
    columnGroups: typing.List[DimensionGroup]
    developerMetadata: typing.List[DeveloperMetadata]

class PivotGroupValueMetadata(typing_extensions.TypedDict, total=False):
    collapsed: bool
    value: ExtendedValue

class WaterfallChartSeries(typing_extensions.TypedDict, total=False):
    subtotalColumnsStyle: WaterfallChartColumnStyle
    customSubtotals: typing.List[WaterfallChartCustomSubtotal]
    data: ChartData
    negativeColumnsStyle: WaterfallChartColumnStyle
    hideTrailingSubtotal: bool
    positiveColumnsStyle: WaterfallChartColumnStyle

class DataSourceRefreshWeeklySchedule(typing_extensions.TypedDict, total=False):
    daysOfWeek: typing.List[str]
    startTime: TimeOfDay

class WaterfallChartColumnStyle(typing_extensions.TypedDict, total=False):
    label: str
    colorStyle: ColorStyle
    color: Color

class DataSourceRefreshSchedule(typing_extensions.TypedDict, total=False):
    refreshScope: typing_extensions.Literal[
        "DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED", "ALL_DATA_SOURCES"
    ]
    enabled: bool
    weeklySchedule: DataSourceRefreshWeeklySchedule
    dailySchedule: DataSourceRefreshDailySchedule
    monthlySchedule: DataSourceRefreshMonthlySchedule
    nextRun: Interval

class DimensionProperties(typing_extensions.TypedDict, total=False):
    dataSourceColumnReference: DataSourceColumnReference
    hiddenByFilter: bool
    developerMetadata: typing.List[DeveloperMetadata]
    pixelSize: int
    hiddenByUser: bool

class BooleanRule(typing_extensions.TypedDict, total=False):
    format: CellFormat
    condition: BooleanCondition

class BasicChartSeries(typing_extensions.TypedDict, total=False):
    targetAxis: typing_extensions.Literal[
        "BASIC_CHART_AXIS_POSITION_UNSPECIFIED",
        "BOTTOM_AXIS",
        "LEFT_AXIS",
        "RIGHT_AXIS",
    ]
    color: Color
    lineStyle: LineStyle
    colorStyle: ColorStyle
    type: typing_extensions.Literal[
        "BASIC_CHART_TYPE_UNSPECIFIED",
        "BAR",
        "LINE",
        "AREA",
        "COLUMN",
        "SCATTER",
        "COMBO",
        "STEPPED_AREA",
    ]
    series: ChartData

class HistogramRule(typing_extensions.TypedDict, total=False):
    start: float
    interval: float
    end: float

class BatchClearValuesByDataFilterRequest(typing_extensions.TypedDict, total=False):
    dataFilters: typing.List[DataFilter]

class AddSlicerResponse(typing_extensions.TypedDict, total=False):
    slicer: Slicer

class ScorecardChartSpec(typing_extensions.TypedDict, total=False):
    aggregateType: typing_extensions.Literal[
        "CHART_AGGREGATE_TYPE_UNSPECIFIED",
        "AVERAGE",
        "COUNT",
        "MAX",
        "MEDIAN",
        "MIN",
        "SUM",
    ]
    keyValueData: ChartData
    numberFormatSource: typing_extensions.Literal[
        "CHART_NUMBER_FORMAT_SOURCE_UNDEFINED", "FROM_DATA", "CUSTOM"
    ]
    baselineValueData: ChartData
    customFormatOptions: ChartCustomNumberFormatOptions
    baselineValueFormat: BaselineValueFormat
    scaleFactor: float
    keyValueFormat: KeyValueFormat

class ClearValuesRequest(typing_extensions.TypedDict, total=False): ...

class BatchGetValuesResponse(typing_extensions.TypedDict, total=False):
    valueRanges: typing.List[ValueRange]
    spreadsheetId: str

class BubbleChartSpec(typing_extensions.TypedDict, total=False):
    bubbleLabels: ChartData
    bubbleMinRadiusSize: int
    groupIds: ChartData
    bubbleSizes: ChartData
    bubbleOpacity: float
    bubbleBorderColorStyle: ColorStyle
    legendPosition: typing_extensions.Literal[
        "BUBBLE_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
        "INSIDE_LEGEND",
    ]
    bubbleBorderColor: Color
    series: ChartData
    bubbleMaxRadiusSize: int
    bubbleTextStyle: TextFormat
    domain: ChartData

class DeleteConditionalFormatRuleRequest(typing_extensions.TypedDict, total=False):
    sheetId: int
    index: int

class DuplicateFilterViewRequest(typing_extensions.TypedDict, total=False):
    filterId: int

class EmbeddedChart(typing_extensions.TypedDict, total=False):
    spec: ChartSpec
    chartId: int
    position: EmbeddedObjectPosition

class AutoFillRequest(typing_extensions.TypedDict, total=False):
    range: GridRange
    sourceAndDestination: SourceAndDestination
    useAlternateSeries: bool

class Interval(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class BasicChartSpec(typing_extensions.TypedDict, total=False):
    series: typing.List[BasicChartSeries]
    chartType: typing_extensions.Literal[
        "BASIC_CHART_TYPE_UNSPECIFIED",
        "BAR",
        "LINE",
        "AREA",
        "COLUMN",
        "SCATTER",
        "COMBO",
        "STEPPED_AREA",
    ]
    stackedType: typing_extensions.Literal[
        "BASIC_CHART_STACKED_TYPE_UNSPECIFIED",
        "NOT_STACKED",
        "STACKED",
        "PERCENT_STACKED",
    ]
    threeDimensional: bool
    compareMode: typing_extensions.Literal[
        "BASIC_CHART_COMPARE_MODE_UNSPECIFIED", "DATUM", "CATEGORY"
    ]
    domains: typing.List[BasicChartDomain]
    legendPosition: typing_extensions.Literal[
        "BASIC_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
    ]
    lineSmoothing: bool
    headerCount: int
    axis: typing.List[BasicChartAxis]
    interpolateNulls: bool

class DeleteDuplicatesResponse(typing_extensions.TypedDict, total=False):
    duplicatesRemovedCount: int

class Border(typing_extensions.TypedDict, total=False):
    width: int
    style: typing_extensions.Literal[
        "STYLE_UNSPECIFIED",
        "DOTTED",
        "DASHED",
        "SOLID",
        "SOLID_MEDIUM",
        "SOLID_THICK",
        "NONE",
        "DOUBLE",
    ]
    color: Color
    colorStyle: ColorStyle

class ExtendedValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    numberValue: float
    errorValue: ErrorValue
    formulaValue: str
    stringValue: str

class ChartGroupRule(typing_extensions.TypedDict, total=False):
    dateTimeRule: ChartDateTimeRule
    histogramRule: ChartHistogramRule

class DeleteEmbeddedObjectRequest(typing_extensions.TypedDict, total=False):
    objectId: int

class GridCoordinate(typing_extensions.TypedDict, total=False):
    rowIndex: int
    sheetId: int
    columnIndex: int

class DataSourceColumnReference(typing_extensions.TypedDict, total=False):
    name: str

class AddNamedRangeRequest(typing_extensions.TypedDict, total=False):
    namedRange: NamedRange

class UpdateProtectedRangeRequest(typing_extensions.TypedDict, total=False):
    fields: str
    protectedRange: ProtectedRange

class DeleteFilterViewRequest(typing_extensions.TypedDict, total=False):
    filterId: int

class BatchGetValuesByDataFilterRequest(typing_extensions.TypedDict, total=False):
    majorDimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
    ]
    dataFilters: typing.List[DataFilter]
    dateTimeRenderOption: typing_extensions.Literal["SERIAL_NUMBER", "FORMATTED_STRING"]
    valueRenderOption: typing_extensions.Literal[
        "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"
    ]

class TimeOfDay(typing_extensions.TypedDict, total=False):
    minutes: int
    seconds: int
    hours: int
    nanos: int

class PivotTable(typing_extensions.TypedDict, total=False):
    rows: typing.List[PivotGroup]
    values: typing.List[PivotValue]
    dataSourceId: str
    valueLayout: typing_extensions.Literal["HORIZONTAL", "VERTICAL"]
    source: GridRange
    dataExecutionStatus: DataExecutionStatus
    filterSpecs: typing.List[PivotFilterSpec]
    criteria: typing.Dict[str, typing.Any]
    columns: typing.List[PivotGroup]

class AddBandingRequest(typing_extensions.TypedDict, total=False):
    bandedRange: BandedRange

class ChartHistogramRule(typing_extensions.TypedDict, total=False):
    minValue: float
    maxValue: float
    intervalSize: float

class ManualRule(typing_extensions.TypedDict, total=False):
    groups: typing.List[ManualRuleGroup]

class DataValidationRule(typing_extensions.TypedDict, total=False):
    inputMessage: str
    condition: BooleanCondition
    strict: bool
    showCustomUi: bool

class TrimWhitespaceResponse(typing_extensions.TypedDict, total=False):
    cellsChangedCount: int

class MatchedDeveloperMetadata(typing_extensions.TypedDict, total=False):
    dataFilters: typing.List[DataFilter]
    developerMetadata: DeveloperMetadata

class ChartCustomNumberFormatOptions(typing_extensions.TypedDict, total=False):
    prefix: str
    suffix: str

class ClearValuesResponse(typing_extensions.TypedDict, total=False):
    spreadsheetId: str
    clearedRange: str

class SortSpec(typing_extensions.TypedDict, total=False):
    backgroundColor: Color
    dataSourceColumnReference: DataSourceColumnReference
    backgroundColorStyle: ColorStyle
    foregroundColor: Color
    dimensionIndex: int
    sortOrder: typing_extensions.Literal[
        "SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    foregroundColorStyle: ColorStyle

class BatchGetValuesByDataFilterResponse(typing_extensions.TypedDict, total=False):
    valueRanges: typing.List[MatchedValueRange]
    spreadsheetId: str

class NamedRange(typing_extensions.TypedDict, total=False):
    namedRangeId: str
    name: str
    range: GridRange

class DataSourceRefreshMonthlySchedule(typing_extensions.TypedDict, total=False):
    startTime: TimeOfDay
    daysOfMonth: typing.List[int]

class AddDimensionGroupResponse(typing_extensions.TypedDict, total=False):
    dimensionGroups: typing.List[DimensionGroup]

class TreemapChartSpec(typing_extensions.TypedDict, total=False):
    hideTooltips: bool
    labels: ChartData
    headerColorStyle: ColorStyle
    minValue: float
    colorScale: TreemapChartColorScale
    hintedLevels: int
    parentLabels: ChartData
    levels: int
    textFormat: TextFormat
    sizeData: ChartData
    colorData: ChartData
    maxValue: float
    headerColor: Color

class TextFormatRun(typing_extensions.TypedDict, total=False):
    format: TextFormat
    startIndex: int

class UpdateDimensionPropertiesRequest(typing_extensions.TypedDict, total=False):
    fields: str
    range: DimensionRange
    dataSourceSheetRange: DataSourceSheetDimensionRange
    properties: DimensionProperties

class BaselineValueFormat(typing_extensions.TypedDict, total=False):
    textFormat: TextFormat
    comparisonType: typing_extensions.Literal[
        "COMPARISON_TYPE_UNDEFINED", "ABSOLUTE_DIFFERENCE", "PERCENTAGE_DIFFERENCE"
    ]
    negativeColor: Color
    description: str
    negativeColorStyle: ColorStyle
    positiveColorStyle: ColorStyle
    position: TextPosition
    positiveColor: Color

class DimensionRange(typing_extensions.TypedDict, total=False):
    dimension: typing_extensions.Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
    endIndex: int
    sheetId: int
    startIndex: int

class CopySheetToAnotherSpreadsheetRequest(typing_extensions.TypedDict, total=False):
    destinationSpreadsheetId: str

class RowData(typing_extensions.TypedDict, total=False):
    values: typing.List[CellData]

class BatchClearValuesByDataFilterResponse(typing_extensions.TypedDict, total=False):
    spreadsheetId: str
    clearedRanges: typing.List[str]

class HistogramSeries(typing_extensions.TypedDict, total=False):
    barColor: Color
    data: ChartData
    barColorStyle: ColorStyle

class DataSourceSheetProperties(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    columns: typing.List[DataSourceColumn]
    dataExecutionStatus: DataExecutionStatus

class NumberFormat(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
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
    pattern: str

class SortRangeRequest(typing_extensions.TypedDict, total=False):
    sortSpecs: typing.List[SortSpec]
    range: GridRange

class DataExecutionStatus(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "DATA_EXECUTION_STATE_UNSPECIFIED",
        "NOT_STARTED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
    ]
    lastRefreshTime: str
    errorCode: typing_extensions.Literal[
        "DATA_EXECUTION_ERROR_CODE_UNSPECIFIED",
        "TIMED_OUT",
        "TOO_MANY_ROWS",
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
    ]
    errorMessage: str

class DeleteProtectedRangeRequest(typing_extensions.TypedDict, total=False):
    protectedRangeId: int

class BasicChartDomain(typing_extensions.TypedDict, total=False):
    domain: ChartData
    reversed: bool

class WaterfallChartCustomSubtotal(typing_extensions.TypedDict, total=False):
    subtotalIndex: int
    dataIsSubtotal: bool
    label: str

class DeleteDuplicatesRequest(typing_extensions.TypedDict, total=False):
    range: GridRange
    comparisonColumns: typing.List[DimensionRange]

class Slicer(typing_extensions.TypedDict, total=False):
    slicerId: int
    position: EmbeddedObjectPosition
    spec: SlicerSpec

class PivotGroupSortValueBucket(typing_extensions.TypedDict, total=False):
    buckets: typing.List[ExtendedValue]
    valuesIndex: int

class BigQueryTableSpec(typing_extensions.TypedDict, total=False):
    datasetId: str
    tableId: str
    tableProjectId: str

class PieChartSpec(typing_extensions.TypedDict, total=False):
    series: ChartData
    domain: ChartData
    pieHole: float
    legendPosition: typing_extensions.Literal[
        "PIE_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
        "LABELED_LEGEND",
    ]
    threeDimensional: bool

class BatchUpdateSpreadsheetRequest(typing_extensions.TypedDict, total=False):
    includeSpreadsheetInResponse: bool
    requests: typing.List[Request]
    responseIncludeGridData: bool
    responseRanges: typing.List[str]

class DataSourceObjectReference(typing_extensions.TypedDict, total=False):
    chartId: int
    dataSourcePivotTableAnchorCell: GridCoordinate
    dataSourceTableAnchorCell: GridCoordinate
    sheetId: str
    dataSourceFormulaCell: GridCoordinate

class DataSource(typing_extensions.TypedDict, total=False):
    spec: DataSourceSpec
    calculatedColumns: typing.List[DataSourceColumn]
    dataSourceId: str
    sheetId: int

class UpdateSheetPropertiesRequest(typing_extensions.TypedDict, total=False):
    properties: SheetProperties
    fields: str

class GradientRule(typing_extensions.TypedDict, total=False):
    maxpoint: InterpolationPoint
    minpoint: InterpolationPoint
    midpoint: InterpolationPoint

class UpdateConditionalFormatRuleResponse(typing_extensions.TypedDict, total=False):
    oldRule: ConditionalFormatRule
    newRule: ConditionalFormatRule
    newIndex: int
    oldIndex: int

class PivotFilterSpec(typing_extensions.TypedDict, total=False):
    filterCriteria: PivotFilterCriteria
    dataSourceColumnReference: DataSourceColumnReference
    columnOffsetIndex: int

class AddChartRequest(typing_extensions.TypedDict, total=False):
    chart: EmbeddedChart

class HistogramChartSpec(typing_extensions.TypedDict, total=False):
    series: typing.List[HistogramSeries]
    legendPosition: typing_extensions.Literal[
        "HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED",
        "BOTTOM_LEGEND",
        "LEFT_LEGEND",
        "RIGHT_LEGEND",
        "TOP_LEGEND",
        "NO_LEGEND",
        "INSIDE_LEGEND",
    ]
    bucketSize: float
    outlierPercentile: float
    showItemDividers: bool

class PivotGroupRule(typing_extensions.TypedDict, total=False):
    manualRule: ManualRule
    histogramRule: HistogramRule
    dateTimeRule: DateTimeRule

class DataSourceSpec(typing_extensions.TypedDict, total=False):
    parameters: typing.List[DataSourceParameter]
    bigQuery: BigQueryDataSourceSpec

class UpdateDataSourceResponse(typing_extensions.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    dataSource: DataSource

class AppendCellsRequest(typing_extensions.TypedDict, total=False):
    fields: str
    sheetId: int
    rows: typing.List[RowData]

class DataSourceFormula(typing_extensions.TypedDict, total=False):
    dataExecutionStatus: DataExecutionStatus
    dataSourceId: str

class CandlestickDomain(typing_extensions.TypedDict, total=False):
    data: ChartData
    reversed: bool

class UpdateDataSourceRequest(typing_extensions.TypedDict, total=False):
    dataSource: DataSource
    fields: str

class CandlestickData(typing_extensions.TypedDict, total=False):
    closeSeries: CandlestickSeries
    highSeries: CandlestickSeries
    lowSeries: CandlestickSeries
    openSeries: CandlestickSeries

class AddNamedRangeResponse(typing_extensions.TypedDict, total=False):
    namedRange: NamedRange

class GridProperties(typing_extensions.TypedDict, total=False):
    columnGroupControlAfter: bool
    rowGroupControlAfter: bool
    hideGridlines: bool
    frozenRowCount: int
    frozenColumnCount: int
    rowCount: int
    columnCount: int

class SearchDeveloperMetadataRequest(typing_extensions.TypedDict, total=False):
    dataFilters: typing.List[DataFilter]

class UpdateEmbeddedObjectPositionRequest(typing_extensions.TypedDict, total=False):
    newPosition: EmbeddedObjectPosition
    objectId: int
    fields: str

class ValueRange(typing_extensions.TypedDict, total=False):
    range: str
    values: typing.List[list]
    majorDimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
    ]

class WaterfallChartSpec(typing_extensions.TypedDict, total=False):
    series: typing.List[WaterfallChartSeries]
    hideConnectorLines: bool
    stackedType: typing_extensions.Literal[
        "WATERFALL_STACKED_TYPE_UNSPECIFIED", "STACKED", "SEQUENTIAL"
    ]
    domain: WaterfallChartDomain
    firstValueIsTotal: bool
    connectorLineStyle: LineStyle

class UpdateValuesByDataFilterResponse(typing_extensions.TypedDict, total=False):
    updatedCells: int
    updatedData: ValueRange
    updatedColumns: int
    dataFilter: DataFilter
    updatedRange: str
    updatedRows: int

class InsertRangeRequest(typing_extensions.TypedDict, total=False):
    range: GridRange
    shiftDimension: typing_extensions.Literal[
        "DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"
    ]

class AutoResizeDimensionsRequest(typing_extensions.TypedDict, total=False):
    dimensions: DimensionRange
    dataSourceSheetDimensions: DataSourceSheetDimensionRange
