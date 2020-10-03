import typing

import typing_extensions

class StretchedPictureFill(typing_extensions.TypedDict, total=False):
    contentUrl: str
    size: Size

class LineProperties(typing_extensions.TypedDict, total=False):
    endConnection: LineConnection
    lineFill: LineFill
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED",
        "SOLID",
        "DOT",
        "DASH",
        "DASH_DOT",
        "LONG_DASH",
        "LONG_DASH_DOT",
    ]
    startConnection: LineConnection
    startArrow: typing_extensions.Literal[
        "ARROW_STYLE_UNSPECIFIED",
        "NONE",
        "STEALTH_ARROW",
        "FILL_ARROW",
        "FILL_CIRCLE",
        "FILL_SQUARE",
        "FILL_DIAMOND",
        "OPEN_ARROW",
        "OPEN_CIRCLE",
        "OPEN_SQUARE",
        "OPEN_DIAMOND",
    ]
    weight: Dimension
    endArrow: typing_extensions.Literal[
        "ARROW_STYLE_UNSPECIFIED",
        "NONE",
        "STEALTH_ARROW",
        "FILL_ARROW",
        "FILL_CIRCLE",
        "FILL_SQUARE",
        "FILL_DIAMOND",
        "OPEN_ARROW",
        "OPEN_CIRCLE",
        "OPEN_SQUARE",
        "OPEN_DIAMOND",
    ]
    link: Link

class Size(typing_extensions.TypedDict, total=False):
    width: Dimension
    height: Dimension

class Range(typing_extensions.TypedDict, total=False):
    endIndex: int
    type: typing_extensions.Literal[
        "RANGE_TYPE_UNSPECIFIED", "FIXED_RANGE", "FROM_START_INDEX", "ALL"
    ]
    startIndex: int

class ReplaceAllTextResponse(typing_extensions.TypedDict, total=False):
    occurrencesChanged: int

class NotesProperties(typing_extensions.TypedDict, total=False):
    speakerNotesObjectId: str

class UpdateTableColumnPropertiesRequest(typing_extensions.TypedDict, total=False):
    fields: str
    columnIndices: typing.List[int]
    tableColumnProperties: TableColumnProperties
    objectId: str

class SheetsChartProperties(typing_extensions.TypedDict, total=False):
    chartImageProperties: ImageProperties

class Video(typing_extensions.TypedDict, total=False):
    videoProperties: VideoProperties
    url: str
    id: str
    source: typing_extensions.Literal["SOURCE_UNSPECIFIED", "YOUTUBE", "DRIVE"]

class WriteControl(typing_extensions.TypedDict, total=False):
    requiredRevisionId: str

class Group(typing_extensions.TypedDict, total=False):
    children: typing.List[PageElement]

class UpdateTableBorderPropertiesRequest(typing_extensions.TypedDict, total=False):
    tableBorderProperties: TableBorderProperties
    objectId: str
    tableRange: TableRange
    fields: str
    borderPosition: typing_extensions.Literal[
        "ALL",
        "BOTTOM",
        "INNER",
        "INNER_HORIZONTAL",
        "INNER_VERTICAL",
        "LEFT",
        "OUTER",
        "RIGHT",
        "TOP",
    ]

class TextStyle(typing_extensions.TypedDict, total=False):
    baselineOffset: typing_extensions.Literal[
        "BASELINE_OFFSET_UNSPECIFIED", "NONE", "SUPERSCRIPT", "SUBSCRIPT"
    ]
    italic: bool
    underline: bool
    fontSize: Dimension
    fontFamily: str
    weightedFontFamily: WeightedFontFamily
    backgroundColor: OptionalColor
    strikethrough: bool
    foregroundColor: OptionalColor
    smallCaps: bool
    bold: bool
    link: Link

class InsertTextRequest(typing_extensions.TypedDict, total=False):
    insertionIndex: int
    cellLocation: TableCellLocation
    text: str
    objectId: str

class Outline(typing_extensions.TypedDict, total=False):
    weight: Dimension
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED",
        "SOLID",
        "DOT",
        "DASH",
        "DASH_DOT",
        "LONG_DASH",
        "LONG_DASH_DOT",
    ]
    outlineFill: OutlineFill
    propertyState: typing_extensions.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]

class ReplaceAllShapesWithImageRequest(typing_extensions.TypedDict, total=False):
    imageUrl: str
    replaceMethod: typing_extensions.Literal["CENTER_INSIDE", "CENTER_CROP"]
    containsText: SubstringMatchCriteria
    pageObjectIds: typing.List[str]
    imageReplaceMethod: typing_extensions.Literal[
        "IMAGE_REPLACE_METHOD_UNSPECIFIED", "CENTER_INSIDE", "CENTER_CROP"
    ]

class TableBorderCell(typing_extensions.TypedDict, total=False):
    tableBorderProperties: TableBorderProperties
    location: TableCellLocation

class UpdateSlidesPositionRequest(typing_extensions.TypedDict, total=False):
    slideObjectIds: typing.List[str]
    insertionIndex: int

class CreateSheetsChartResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class LineConnection(typing_extensions.TypedDict, total=False):
    connectedObjectId: str
    connectionSiteIndex: int

class UpdateTextStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    textRange: Range
    style: TextStyle
    objectId: str
    cellLocation: TableCellLocation

class CreateTableRequest(typing_extensions.TypedDict, total=False):
    rows: int
    columns: int
    elementProperties: PageElementProperties
    objectId: str

class SubstringMatchCriteria(typing_extensions.TypedDict, total=False):
    matchCase: bool
    text: str

class PageProperties(typing_extensions.TypedDict, total=False):
    colorScheme: ColorScheme
    pageBackgroundFill: PageBackgroundFill

class Shadow(typing_extensions.TypedDict, total=False):
    rotateWithShape: bool
    propertyState: typing_extensions.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    transform: AffineTransform
    blurRadius: Dimension
    type: typing_extensions.Literal["SHADOW_TYPE_UNSPECIFIED", "OUTER"]
    color: OpaqueColor
    alignment: typing_extensions.Literal[
        "RECTANGLE_POSITION_UNSPECIFIED",
        "TOP_LEFT",
        "TOP_CENTER",
        "TOP_RIGHT",
        "LEFT_CENTER",
        "CENTER",
        "RIGHT_CENTER",
        "BOTTOM_LEFT",
        "BOTTOM_CENTER",
        "BOTTOM_RIGHT",
    ]
    alpha: float

class Bullet(typing_extensions.TypedDict, total=False):
    glyph: str
    listId: str
    nestingLevel: int
    bulletStyle: TextStyle

class CreateVideoResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class CreateLineResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class CreateVideoRequest(typing_extensions.TypedDict, total=False):
    elementProperties: PageElementProperties
    id: str
    source: typing_extensions.Literal["SOURCE_UNSPECIFIED", "YOUTUBE", "DRIVE"]
    objectId: str

class OpaqueColor(typing_extensions.TypedDict, total=False):
    themeColor: typing_extensions.Literal[
        "THEME_COLOR_TYPE_UNSPECIFIED",
        "DARK1",
        "LIGHT1",
        "DARK2",
        "LIGHT2",
        "ACCENT1",
        "ACCENT2",
        "ACCENT3",
        "ACCENT4",
        "ACCENT5",
        "ACCENT6",
        "HYPERLINK",
        "FOLLOWED_HYPERLINK",
        "TEXT1",
        "BACKGROUND1",
        "TEXT2",
        "BACKGROUND2",
    ]
    rgbColor: RgbColor

class Page(typing_extensions.TypedDict, total=False):
    pageElements: typing.List[PageElement]
    pageType: typing_extensions.Literal[
        "SLIDE", "MASTER", "LAYOUT", "NOTES", "NOTES_MASTER"
    ]
    objectId: str
    layoutProperties: LayoutProperties
    slideProperties: SlideProperties
    masterProperties: MasterProperties
    notesProperties: NotesProperties
    pageProperties: PageProperties
    revisionId: str

class UpdateShapePropertiesRequest(typing_extensions.TypedDict, total=False):
    fields: str
    shapeProperties: ShapeProperties
    objectId: str

class TableCellBackgroundFill(typing_extensions.TypedDict, total=False):
    solidFill: SolidFill
    propertyState: typing_extensions.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]

class InsertTableRowsRequest(typing_extensions.TypedDict, total=False):
    cellLocation: TableCellLocation
    number: int
    tableObjectId: str
    insertBelow: bool

class GroupObjectsRequest(typing_extensions.TypedDict, total=False):
    childrenObjectIds: typing.List[str]
    groupObjectId: str

class ImageProperties(typing_extensions.TypedDict, total=False):
    link: Link
    outline: Outline
    recolor: Recolor
    shadow: Shadow
    contrast: float
    cropProperties: CropProperties
    brightness: float
    transparency: float

class TableBorderFill(typing_extensions.TypedDict, total=False):
    solidFill: SolidFill

class Shape(typing_extensions.TypedDict, total=False):
    shapeProperties: ShapeProperties
    shapeType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TEXT_BOX",
        "RECTANGLE",
        "ROUND_RECTANGLE",
        "ELLIPSE",
        "ARC",
        "BENT_ARROW",
        "BENT_UP_ARROW",
        "BEVEL",
        "BLOCK_ARC",
        "BRACE_PAIR",
        "BRACKET_PAIR",
        "CAN",
        "CHEVRON",
        "CHORD",
        "CLOUD",
        "CORNER",
        "CUBE",
        "CURVED_DOWN_ARROW",
        "CURVED_LEFT_ARROW",
        "CURVED_RIGHT_ARROW",
        "CURVED_UP_ARROW",
        "DECAGON",
        "DIAGONAL_STRIPE",
        "DIAMOND",
        "DODECAGON",
        "DONUT",
        "DOUBLE_WAVE",
        "DOWN_ARROW",
        "DOWN_ARROW_CALLOUT",
        "FOLDED_CORNER",
        "FRAME",
        "HALF_FRAME",
        "HEART",
        "HEPTAGON",
        "HEXAGON",
        "HOME_PLATE",
        "HORIZONTAL_SCROLL",
        "IRREGULAR_SEAL_1",
        "IRREGULAR_SEAL_2",
        "LEFT_ARROW",
        "LEFT_ARROW_CALLOUT",
        "LEFT_BRACE",
        "LEFT_BRACKET",
        "LEFT_RIGHT_ARROW",
        "LEFT_RIGHT_ARROW_CALLOUT",
        "LEFT_RIGHT_UP_ARROW",
        "LEFT_UP_ARROW",
        "LIGHTNING_BOLT",
        "MATH_DIVIDE",
        "MATH_EQUAL",
        "MATH_MINUS",
        "MATH_MULTIPLY",
        "MATH_NOT_EQUAL",
        "MATH_PLUS",
        "MOON",
        "NO_SMOKING",
        "NOTCHED_RIGHT_ARROW",
        "OCTAGON",
        "PARALLELOGRAM",
        "PENTAGON",
        "PIE",
        "PLAQUE",
        "PLUS",
        "QUAD_ARROW",
        "QUAD_ARROW_CALLOUT",
        "RIBBON",
        "RIBBON_2",
        "RIGHT_ARROW",
        "RIGHT_ARROW_CALLOUT",
        "RIGHT_BRACE",
        "RIGHT_BRACKET",
        "ROUND_1_RECTANGLE",
        "ROUND_2_DIAGONAL_RECTANGLE",
        "ROUND_2_SAME_RECTANGLE",
        "RIGHT_TRIANGLE",
        "SMILEY_FACE",
        "SNIP_1_RECTANGLE",
        "SNIP_2_DIAGONAL_RECTANGLE",
        "SNIP_2_SAME_RECTANGLE",
        "SNIP_ROUND_RECTANGLE",
        "STAR_10",
        "STAR_12",
        "STAR_16",
        "STAR_24",
        "STAR_32",
        "STAR_4",
        "STAR_5",
        "STAR_6",
        "STAR_7",
        "STAR_8",
        "STRIPED_RIGHT_ARROW",
        "SUN",
        "TRAPEZOID",
        "TRIANGLE",
        "UP_ARROW",
        "UP_ARROW_CALLOUT",
        "UP_DOWN_ARROW",
        "UTURN_ARROW",
        "VERTICAL_SCROLL",
        "WAVE",
        "WEDGE_ELLIPSE_CALLOUT",
        "WEDGE_RECTANGLE_CALLOUT",
        "WEDGE_ROUND_RECTANGLE_CALLOUT",
        "FLOW_CHART_ALTERNATE_PROCESS",
        "FLOW_CHART_COLLATE",
        "FLOW_CHART_CONNECTOR",
        "FLOW_CHART_DECISION",
        "FLOW_CHART_DELAY",
        "FLOW_CHART_DISPLAY",
        "FLOW_CHART_DOCUMENT",
        "FLOW_CHART_EXTRACT",
        "FLOW_CHART_INPUT_OUTPUT",
        "FLOW_CHART_INTERNAL_STORAGE",
        "FLOW_CHART_MAGNETIC_DISK",
        "FLOW_CHART_MAGNETIC_DRUM",
        "FLOW_CHART_MAGNETIC_TAPE",
        "FLOW_CHART_MANUAL_INPUT",
        "FLOW_CHART_MANUAL_OPERATION",
        "FLOW_CHART_MERGE",
        "FLOW_CHART_MULTIDOCUMENT",
        "FLOW_CHART_OFFLINE_STORAGE",
        "FLOW_CHART_OFFPAGE_CONNECTOR",
        "FLOW_CHART_ONLINE_STORAGE",
        "FLOW_CHART_OR",
        "FLOW_CHART_PREDEFINED_PROCESS",
        "FLOW_CHART_PREPARATION",
        "FLOW_CHART_PROCESS",
        "FLOW_CHART_PUNCHED_CARD",
        "FLOW_CHART_PUNCHED_TAPE",
        "FLOW_CHART_SORT",
        "FLOW_CHART_SUMMING_JUNCTION",
        "FLOW_CHART_TERMINATOR",
        "ARROW_EAST",
        "ARROW_NORTH_EAST",
        "ARROW_NORTH",
        "SPEECH",
        "STARBURST",
        "TEARDROP",
        "ELLIPSE_RIBBON",
        "ELLIPSE_RIBBON_2",
        "CLOUD_CALLOUT",
        "CUSTOM",
    ]
    text: TextContent
    placeholder: Placeholder

class Presentation(typing_extensions.TypedDict, total=False):
    masters: typing.List[Page]
    locale: str
    presentationId: str
    notesMaster: Page
    revisionId: str
    layouts: typing.List[Page]
    title: str
    pageSize: Size
    slides: typing.List[Page]

class SolidFill(typing_extensions.TypedDict, total=False):
    alpha: float
    color: OpaqueColor

class MergeTableCellsRequest(typing_extensions.TypedDict, total=False):
    tableRange: TableRange
    objectId: str

class Table(typing_extensions.TypedDict, total=False):
    columns: int
    horizontalBorderRows: typing.List[TableBorderRow]
    tableColumns: typing.List[TableColumnProperties]
    rows: int
    verticalBorderRows: typing.List[TableBorderRow]
    tableRows: typing.List[TableRow]

class TableCell(typing_extensions.TypedDict, total=False):
    rowSpan: int
    tableCellProperties: TableCellProperties
    columnSpan: int
    text: TextContent
    location: TableCellLocation

class LayoutReference(typing_extensions.TypedDict, total=False):
    layoutId: str
    predefinedLayout: typing_extensions.Literal[
        "PREDEFINED_LAYOUT_UNSPECIFIED",
        "BLANK",
        "CAPTION_ONLY",
        "TITLE",
        "TITLE_AND_BODY",
        "TITLE_AND_TWO_COLUMNS",
        "TITLE_ONLY",
        "SECTION_HEADER",
        "SECTION_TITLE_AND_DESCRIPTION",
        "ONE_COLUMN_TEXT",
        "MAIN_POINT",
        "BIG_NUMBER",
    ]

class ShapeBackgroundFill(typing_extensions.TypedDict, total=False):
    propertyState: typing_extensions.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    solidFill: SolidFill

class DeleteTableRowRequest(typing_extensions.TypedDict, total=False):
    tableObjectId: str
    cellLocation: TableCellLocation

class CreateImageResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class RerouteLineRequest(typing_extensions.TypedDict, total=False):
    objectId: str

class Thumbnail(typing_extensions.TypedDict, total=False):
    contentUrl: str
    height: int
    width: int

class ReplaceImageRequest(typing_extensions.TypedDict, total=False):
    imageReplaceMethod: typing_extensions.Literal[
        "IMAGE_REPLACE_METHOD_UNSPECIFIED", "CENTER_INSIDE", "CENTER_CROP"
    ]
    imageObjectId: str
    url: str

class RefreshSheetsChartRequest(typing_extensions.TypedDict, total=False):
    objectId: str

class CropProperties(typing_extensions.TypedDict, total=False):
    bottomOffset: float
    angle: float
    leftOffset: float
    rightOffset: float
    topOffset: float

class ColorScheme(typing_extensions.TypedDict, total=False):
    colors: typing.List[ThemeColorPair]

class ReplaceAllTextRequest(typing_extensions.TypedDict, total=False):
    replaceText: str
    pageObjectIds: typing.List[str]
    containsText: SubstringMatchCriteria

class RgbColor(typing_extensions.TypedDict, total=False):
    red: float
    blue: float
    green: float

class CreateSlideRequest(typing_extensions.TypedDict, total=False):
    objectId: str
    insertionIndex: int
    slideLayoutReference: LayoutReference
    placeholderIdMappings: typing.List[LayoutPlaceholderIdMapping]

class PageElementProperties(typing_extensions.TypedDict, total=False):
    transform: AffineTransform
    pageObjectId: str
    size: Size

class GroupObjectsResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class Image(typing_extensions.TypedDict, total=False):
    contentUrl: str
    imageProperties: ImageProperties
    sourceUrl: str

class LayoutPlaceholderIdMapping(typing_extensions.TypedDict, total=False):
    layoutPlaceholderObjectId: str
    objectId: str
    layoutPlaceholder: Placeholder

class ReplaceAllShapesWithSheetsChartResponse(typing_extensions.TypedDict, total=False):
    occurrencesChanged: int

class UpdateVideoPropertiesRequest(typing_extensions.TypedDict, total=False):
    fields: str
    videoProperties: VideoProperties
    objectId: str

class ThemeColorPair(typing_extensions.TypedDict, total=False):
    color: RgbColor
    type: typing_extensions.Literal[
        "THEME_COLOR_TYPE_UNSPECIFIED",
        "DARK1",
        "LIGHT1",
        "DARK2",
        "LIGHT2",
        "ACCENT1",
        "ACCENT2",
        "ACCENT3",
        "ACCENT4",
        "ACCENT5",
        "ACCENT6",
        "HYPERLINK",
        "FOLLOWED_HYPERLINK",
        "TEXT1",
        "BACKGROUND1",
        "TEXT2",
        "BACKGROUND2",
    ]

class LineFill(typing_extensions.TypedDict, total=False):
    solidFill: SolidFill

class UpdateLineCategoryRequest(typing_extensions.TypedDict, total=False):
    lineCategory: typing_extensions.Literal[
        "LINE_CATEGORY_UNSPECIFIED", "STRAIGHT", "BENT", "CURVED"
    ]
    objectId: str

class BatchUpdatePresentationRequest(typing_extensions.TypedDict, total=False):
    requests: typing.List[Request]
    writeControl: WriteControl

class WordArt(typing_extensions.TypedDict, total=False):
    renderedText: str

class DeleteTableColumnRequest(typing_extensions.TypedDict, total=False):
    tableObjectId: str
    cellLocation: TableCellLocation

class UpdatePageElementsZOrderRequest(typing_extensions.TypedDict, total=False):
    operation: typing_extensions.Literal[
        "Z_ORDER_OPERATION_UNSPECIFIED",
        "BRING_TO_FRONT",
        "BRING_FORWARD",
        "SEND_BACKWARD",
        "SEND_TO_BACK",
    ]
    pageElementObjectIds: typing.List[str]

class ReplaceAllShapesWithImageResponse(typing_extensions.TypedDict, total=False):
    occurrencesChanged: int

class ShapeProperties(typing_extensions.TypedDict, total=False):
    contentAlignment: typing_extensions.Literal[
        "CONTENT_ALIGNMENT_UNSPECIFIED",
        "CONTENT_ALIGNMENT_UNSUPPORTED",
        "TOP",
        "MIDDLE",
        "BOTTOM",
    ]
    outline: Outline
    shapeBackgroundFill: ShapeBackgroundFill
    shadow: Shadow
    link: Link

class Response(typing_extensions.TypedDict, total=False):
    createShape: CreateShapeResponse
    createSlide: CreateSlideResponse
    replaceAllShapesWithImage: ReplaceAllShapesWithImageResponse
    createVideo: CreateVideoResponse
    groupObjects: GroupObjectsResponse
    createSheetsChart: CreateSheetsChartResponse
    createTable: CreateTableResponse
    replaceAllText: ReplaceAllTextResponse
    duplicateObject: DuplicateObjectResponse
    createImage: CreateImageResponse
    replaceAllShapesWithSheetsChart: ReplaceAllShapesWithSheetsChartResponse
    createLine: CreateLineResponse

class DeleteObjectRequest(typing_extensions.TypedDict, total=False):
    objectId: str

class LayoutProperties(typing_extensions.TypedDict, total=False):
    masterObjectId: str
    displayName: str
    name: str

class CreateShapeRequest(typing_extensions.TypedDict, total=False):
    elementProperties: PageElementProperties
    objectId: str
    shapeType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TEXT_BOX",
        "RECTANGLE",
        "ROUND_RECTANGLE",
        "ELLIPSE",
        "ARC",
        "BENT_ARROW",
        "BENT_UP_ARROW",
        "BEVEL",
        "BLOCK_ARC",
        "BRACE_PAIR",
        "BRACKET_PAIR",
        "CAN",
        "CHEVRON",
        "CHORD",
        "CLOUD",
        "CORNER",
        "CUBE",
        "CURVED_DOWN_ARROW",
        "CURVED_LEFT_ARROW",
        "CURVED_RIGHT_ARROW",
        "CURVED_UP_ARROW",
        "DECAGON",
        "DIAGONAL_STRIPE",
        "DIAMOND",
        "DODECAGON",
        "DONUT",
        "DOUBLE_WAVE",
        "DOWN_ARROW",
        "DOWN_ARROW_CALLOUT",
        "FOLDED_CORNER",
        "FRAME",
        "HALF_FRAME",
        "HEART",
        "HEPTAGON",
        "HEXAGON",
        "HOME_PLATE",
        "HORIZONTAL_SCROLL",
        "IRREGULAR_SEAL_1",
        "IRREGULAR_SEAL_2",
        "LEFT_ARROW",
        "LEFT_ARROW_CALLOUT",
        "LEFT_BRACE",
        "LEFT_BRACKET",
        "LEFT_RIGHT_ARROW",
        "LEFT_RIGHT_ARROW_CALLOUT",
        "LEFT_RIGHT_UP_ARROW",
        "LEFT_UP_ARROW",
        "LIGHTNING_BOLT",
        "MATH_DIVIDE",
        "MATH_EQUAL",
        "MATH_MINUS",
        "MATH_MULTIPLY",
        "MATH_NOT_EQUAL",
        "MATH_PLUS",
        "MOON",
        "NO_SMOKING",
        "NOTCHED_RIGHT_ARROW",
        "OCTAGON",
        "PARALLELOGRAM",
        "PENTAGON",
        "PIE",
        "PLAQUE",
        "PLUS",
        "QUAD_ARROW",
        "QUAD_ARROW_CALLOUT",
        "RIBBON",
        "RIBBON_2",
        "RIGHT_ARROW",
        "RIGHT_ARROW_CALLOUT",
        "RIGHT_BRACE",
        "RIGHT_BRACKET",
        "ROUND_1_RECTANGLE",
        "ROUND_2_DIAGONAL_RECTANGLE",
        "ROUND_2_SAME_RECTANGLE",
        "RIGHT_TRIANGLE",
        "SMILEY_FACE",
        "SNIP_1_RECTANGLE",
        "SNIP_2_DIAGONAL_RECTANGLE",
        "SNIP_2_SAME_RECTANGLE",
        "SNIP_ROUND_RECTANGLE",
        "STAR_10",
        "STAR_12",
        "STAR_16",
        "STAR_24",
        "STAR_32",
        "STAR_4",
        "STAR_5",
        "STAR_6",
        "STAR_7",
        "STAR_8",
        "STRIPED_RIGHT_ARROW",
        "SUN",
        "TRAPEZOID",
        "TRIANGLE",
        "UP_ARROW",
        "UP_ARROW_CALLOUT",
        "UP_DOWN_ARROW",
        "UTURN_ARROW",
        "VERTICAL_SCROLL",
        "WAVE",
        "WEDGE_ELLIPSE_CALLOUT",
        "WEDGE_RECTANGLE_CALLOUT",
        "WEDGE_ROUND_RECTANGLE_CALLOUT",
        "FLOW_CHART_ALTERNATE_PROCESS",
        "FLOW_CHART_COLLATE",
        "FLOW_CHART_CONNECTOR",
        "FLOW_CHART_DECISION",
        "FLOW_CHART_DELAY",
        "FLOW_CHART_DISPLAY",
        "FLOW_CHART_DOCUMENT",
        "FLOW_CHART_EXTRACT",
        "FLOW_CHART_INPUT_OUTPUT",
        "FLOW_CHART_INTERNAL_STORAGE",
        "FLOW_CHART_MAGNETIC_DISK",
        "FLOW_CHART_MAGNETIC_DRUM",
        "FLOW_CHART_MAGNETIC_TAPE",
        "FLOW_CHART_MANUAL_INPUT",
        "FLOW_CHART_MANUAL_OPERATION",
        "FLOW_CHART_MERGE",
        "FLOW_CHART_MULTIDOCUMENT",
        "FLOW_CHART_OFFLINE_STORAGE",
        "FLOW_CHART_OFFPAGE_CONNECTOR",
        "FLOW_CHART_ONLINE_STORAGE",
        "FLOW_CHART_OR",
        "FLOW_CHART_PREDEFINED_PROCESS",
        "FLOW_CHART_PREPARATION",
        "FLOW_CHART_PROCESS",
        "FLOW_CHART_PUNCHED_CARD",
        "FLOW_CHART_PUNCHED_TAPE",
        "FLOW_CHART_SORT",
        "FLOW_CHART_SUMMING_JUNCTION",
        "FLOW_CHART_TERMINATOR",
        "ARROW_EAST",
        "ARROW_NORTH_EAST",
        "ARROW_NORTH",
        "SPEECH",
        "STARBURST",
        "TEARDROP",
        "ELLIPSE_RIBBON",
        "ELLIPSE_RIBBON_2",
        "CLOUD_CALLOUT",
        "CUSTOM",
    ]

class DuplicateObjectResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class PageElement(typing.Dict[str, typing.Any]): ...

class TextElement(typing_extensions.TypedDict, total=False):
    startIndex: int
    autoText: AutoText
    endIndex: int
    textRun: TextRun
    paragraphMarker: ParagraphMarker

class TextRun(typing_extensions.TypedDict, total=False):
    style: TextStyle
    content: str

class CreateParagraphBulletsRequest(typing_extensions.TypedDict, total=False):
    cellLocation: TableCellLocation
    bulletPreset: typing_extensions.Literal[
        "BULLET_DISC_CIRCLE_SQUARE",
        "BULLET_DIAMONDX_ARROW3D_SQUARE",
        "BULLET_CHECKBOX",
        "BULLET_ARROW_DIAMOND_DISC",
        "BULLET_STAR_CIRCLE_SQUARE",
        "BULLET_ARROW3D_CIRCLE_SQUARE",
        "BULLET_LEFTTRIANGLE_DIAMOND_DISC",
        "BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE",
        "BULLET_DIAMOND_CIRCLE_SQUARE",
        "NUMBERED_DIGIT_ALPHA_ROMAN",
        "NUMBERED_DIGIT_ALPHA_ROMAN_PARENS",
        "NUMBERED_DIGIT_NESTED",
        "NUMBERED_UPPERALPHA_ALPHA_ROMAN",
        "NUMBERED_UPPERROMAN_UPPERALPHA_DIGIT",
        "NUMBERED_ZERODIGIT_ALPHA_ROMAN",
    ]
    objectId: str
    textRange: Range

class TableRow(typing_extensions.TypedDict, total=False):
    rowHeight: Dimension
    tableCells: typing.List[TableCell]
    tableRowProperties: TableRowProperties

class InsertTableColumnsRequest(typing_extensions.TypedDict, total=False):
    insertRight: bool
    tableObjectId: str
    cellLocation: TableCellLocation
    number: int

class Request(typing_extensions.TypedDict, total=False):
    rerouteLine: RerouteLineRequest
    updateTableColumnProperties: UpdateTableColumnPropertiesRequest
    createSheetsChart: CreateSheetsChartRequest
    duplicateObject: DuplicateObjectRequest
    updatePageElementTransform: UpdatePageElementTransformRequest
    updateVideoProperties: UpdateVideoPropertiesRequest
    replaceAllShapesWithImage: ReplaceAllShapesWithImageRequest
    createLine: CreateLineRequest
    insertTableColumns: InsertTableColumnsRequest
    createTable: CreateTableRequest
    updateShapeProperties: UpdateShapePropertiesRequest
    createImage: CreateImageRequest
    deleteParagraphBullets: DeleteParagraphBulletsRequest
    updateTableCellProperties: UpdateTableCellPropertiesRequest
    insertText: InsertTextRequest
    replaceAllText: ReplaceAllTextRequest
    updatePageElementAltText: UpdatePageElementAltTextRequest
    updateTextStyle: UpdateTextStyleRequest
    unmergeTableCells: UnmergeTableCellsRequest
    replaceImage: ReplaceImageRequest
    createShape: CreateShapeRequest
    createSlide: CreateSlideRequest
    updatePageElementsZOrder: UpdatePageElementsZOrderRequest
    deleteTableColumn: DeleteTableColumnRequest
    deleteText: DeleteTextRequest
    refreshSheetsChart: RefreshSheetsChartRequest
    mergeTableCells: MergeTableCellsRequest
    updateLineCategory: UpdateLineCategoryRequest
    createParagraphBullets: CreateParagraphBulletsRequest
    createVideo: CreateVideoRequest
    updateParagraphStyle: UpdateParagraphStyleRequest
    updateImageProperties: UpdateImagePropertiesRequest
    deleteTableRow: DeleteTableRowRequest
    updateTableRowProperties: UpdateTableRowPropertiesRequest
    replaceAllShapesWithSheetsChart: ReplaceAllShapesWithSheetsChartRequest
    updateTableBorderProperties: UpdateTableBorderPropertiesRequest
    ungroupObjects: UngroupObjectsRequest
    groupObjects: GroupObjectsRequest
    updatePageProperties: UpdatePagePropertiesRequest
    deleteObject: DeleteObjectRequest
    insertTableRows: InsertTableRowsRequest
    updateLineProperties: UpdateLinePropertiesRequest
    updateSlidesPosition: UpdateSlidesPositionRequest

class AffineTransform(typing_extensions.TypedDict, total=False):
    translateX: float
    scaleX: float
    shearX: float
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "EMU", "PT"]
    shearY: float
    translateY: float
    scaleY: float

class ReplaceAllShapesWithSheetsChartRequest(typing_extensions.TypedDict, total=False):
    linkingMode: typing_extensions.Literal["NOT_LINKED_IMAGE", "LINKED"]
    chartId: int
    pageObjectIds: typing.List[str]
    containsText: SubstringMatchCriteria
    spreadsheetId: str

class TableRowProperties(typing_extensions.TypedDict, total=False):
    minRowHeight: Dimension

class UpdateParagraphStyleRequest(typing_extensions.TypedDict, total=False):
    textRange: Range
    objectId: str
    fields: str
    style: ParagraphStyle
    cellLocation: TableCellLocation

class OptionalColor(typing_extensions.TypedDict, total=False):
    opaqueColor: OpaqueColor

class AutoText(typing_extensions.TypedDict, total=False):
    style: TextStyle
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SLIDE_NUMBER"]
    content: str

class OutlineFill(typing_extensions.TypedDict, total=False):
    solidFill: SolidFill

class UpdatePageElementTransformRequest(typing_extensions.TypedDict, total=False):
    transform: AffineTransform
    objectId: str
    applyMode: typing_extensions.Literal[
        "APPLY_MODE_UNSPECIFIED", "RELATIVE", "ABSOLUTE"
    ]

class CreateLineRequest(typing_extensions.TypedDict, total=False):
    lineCategory: typing_extensions.Literal["STRAIGHT", "BENT", "CURVED"]
    elementProperties: PageElementProperties
    category: typing_extensions.Literal[
        "LINE_CATEGORY_UNSPECIFIED", "STRAIGHT", "BENT", "CURVED"
    ]
    objectId: str

class CreateTableResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class UpdatePagePropertiesRequest(typing_extensions.TypedDict, total=False):
    objectId: str
    pageProperties: PageProperties
    fields: str

class BatchUpdatePresentationResponse(typing_extensions.TypedDict, total=False):
    writeControl: WriteControl
    presentationId: str
    replies: typing.List[Response]

class UpdateTableRowPropertiesRequest(typing_extensions.TypedDict, total=False):
    rowIndices: typing.List[int]
    objectId: str
    tableRowProperties: TableRowProperties
    fields: str

class VideoProperties(typing_extensions.TypedDict, total=False):
    autoPlay: bool
    end: int
    start: int
    mute: bool
    outline: Outline

class UpdateLinePropertiesRequest(typing_extensions.TypedDict, total=False):
    lineProperties: LineProperties
    fields: str
    objectId: str

class TableColumnProperties(typing_extensions.TypedDict, total=False):
    columnWidth: Dimension

class NestingLevel(typing_extensions.TypedDict, total=False):
    bulletStyle: TextStyle

class UnmergeTableCellsRequest(typing_extensions.TypedDict, total=False):
    tableRange: TableRange
    objectId: str

class Placeholder(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "NONE",
        "BODY",
        "CHART",
        "CLIP_ART",
        "CENTERED_TITLE",
        "DIAGRAM",
        "DATE_AND_TIME",
        "FOOTER",
        "HEADER",
        "MEDIA",
        "OBJECT",
        "PICTURE",
        "SLIDE_NUMBER",
        "SUBTITLE",
        "TABLE",
        "TITLE",
        "SLIDE_IMAGE",
    ]
    index: int
    parentObjectId: str

class Recolor(typing_extensions.TypedDict, total=False):
    name: typing_extensions.Literal[
        "NONE",
        "LIGHT1",
        "LIGHT2",
        "LIGHT3",
        "LIGHT4",
        "LIGHT5",
        "LIGHT6",
        "LIGHT7",
        "LIGHT8",
        "LIGHT9",
        "LIGHT10",
        "DARK1",
        "DARK2",
        "DARK3",
        "DARK4",
        "DARK5",
        "DARK6",
        "DARK7",
        "DARK8",
        "DARK9",
        "DARK10",
        "GRAYSCALE",
        "NEGATIVE",
        "SEPIA",
        "CUSTOM",
    ]
    recolorStops: typing.List[ColorStop]

class TableBorderRow(typing_extensions.TypedDict, total=False):
    tableBorderCells: typing.List[TableBorderCell]

class TableBorderProperties(typing_extensions.TypedDict, total=False):
    tableBorderFill: TableBorderFill
    weight: Dimension
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED",
        "SOLID",
        "DOT",
        "DASH",
        "DASH_DOT",
        "LONG_DASH",
        "LONG_DASH_DOT",
    ]

class CreateSlideResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class UpdateImagePropertiesRequest(typing_extensions.TypedDict, total=False):
    objectId: str
    imageProperties: ImageProperties
    fields: str

class DuplicateObjectRequest(typing_extensions.TypedDict, total=False):
    objectId: str
    objectIds: typing.Dict[str, typing.Any]

class TextContent(typing_extensions.TypedDict, total=False):
    lists: typing.Dict[str, typing.Any]
    textElements: typing.List[TextElement]

class List(typing_extensions.TypedDict, total=False):
    nestingLevel: typing.Dict[str, typing.Any]
    listId: str

class Dimension(typing_extensions.TypedDict, total=False):
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "EMU", "PT"]
    magnitude: float

class CreateSheetsChartRequest(typing_extensions.TypedDict, total=False):
    objectId: str
    linkingMode: typing_extensions.Literal["NOT_LINKED_IMAGE", "LINKED"]
    elementProperties: PageElementProperties
    spreadsheetId: str
    chartId: int

class CreateShapeResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class Link(typing_extensions.TypedDict, total=False):
    url: str
    slideIndex: int
    relativeLink: typing_extensions.Literal[
        "RELATIVE_SLIDE_LINK_UNSPECIFIED",
        "NEXT_SLIDE",
        "PREVIOUS_SLIDE",
        "FIRST_SLIDE",
        "LAST_SLIDE",
    ]
    pageObjectId: str

class CreateImageRequest(typing_extensions.TypedDict, total=False):
    elementProperties: PageElementProperties
    objectId: str
    url: str

class TableCellLocation(typing_extensions.TypedDict, total=False):
    columnIndex: int
    rowIndex: int

class PageBackgroundFill(typing_extensions.TypedDict, total=False):
    stretchedPictureFill: StretchedPictureFill
    propertyState: typing_extensions.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    solidFill: SolidFill

class MasterProperties(typing_extensions.TypedDict, total=False):
    displayName: str

class SlideProperties(typing.Dict[str, typing.Any]): ...

class WeightedFontFamily(typing_extensions.TypedDict, total=False):
    weight: int
    fontFamily: str

class ParagraphMarker(typing_extensions.TypedDict, total=False):
    bullet: Bullet
    style: ParagraphStyle

class TableCellProperties(typing_extensions.TypedDict, total=False):
    tableCellBackgroundFill: TableCellBackgroundFill
    contentAlignment: typing_extensions.Literal[
        "CONTENT_ALIGNMENT_UNSPECIFIED",
        "CONTENT_ALIGNMENT_UNSUPPORTED",
        "TOP",
        "MIDDLE",
        "BOTTOM",
    ]

class TableRange(typing_extensions.TypedDict, total=False):
    columnSpan: int
    rowSpan: int
    location: TableCellLocation

class DeleteTextRequest(typing_extensions.TypedDict, total=False):
    textRange: Range
    objectId: str
    cellLocation: TableCellLocation

class Line(typing_extensions.TypedDict, total=False):
    lineCategory: typing_extensions.Literal[
        "LINE_CATEGORY_UNSPECIFIED", "STRAIGHT", "BENT", "CURVED"
    ]
    lineProperties: LineProperties
    lineType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "STRAIGHT_CONNECTOR_1",
        "BENT_CONNECTOR_2",
        "BENT_CONNECTOR_3",
        "BENT_CONNECTOR_4",
        "BENT_CONNECTOR_5",
        "CURVED_CONNECTOR_2",
        "CURVED_CONNECTOR_3",
        "CURVED_CONNECTOR_4",
        "CURVED_CONNECTOR_5",
        "STRAIGHT_LINE",
    ]

class UpdatePageElementAltTextRequest(typing_extensions.TypedDict, total=False):
    description: str
    objectId: str
    title: str

class UpdateTableCellPropertiesRequest(typing_extensions.TypedDict, total=False):
    fields: str
    tableCellProperties: TableCellProperties
    tableRange: TableRange
    objectId: str

class SheetsChart(typing_extensions.TypedDict, total=False):
    spreadsheetId: str
    contentUrl: str
    chartId: int
    sheetsChartProperties: SheetsChartProperties

class UngroupObjectsRequest(typing_extensions.TypedDict, total=False):
    objectIds: typing.List[str]

class ColorStop(typing_extensions.TypedDict, total=False):
    position: float
    color: OpaqueColor
    alpha: float

class DeleteParagraphBulletsRequest(typing_extensions.TypedDict, total=False):
    cellLocation: TableCellLocation
    objectId: str
    textRange: Range

class ParagraphStyle(typing_extensions.TypedDict, total=False):
    lineSpacing: float
    spaceBelow: Dimension
    indentEnd: Dimension
    direction: typing_extensions.Literal[
        "TEXT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    indentStart: Dimension
    spaceAbove: Dimension
    alignment: typing_extensions.Literal[
        "ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END", "JUSTIFIED"
    ]
    indentFirstLine: Dimension
    spacingMode: typing_extensions.Literal[
        "SPACING_MODE_UNSPECIFIED", "NEVER_COLLAPSE", "COLLAPSE_LISTS"
    ]
