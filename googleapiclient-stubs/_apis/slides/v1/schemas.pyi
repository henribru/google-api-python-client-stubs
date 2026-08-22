import typing

_list = list

@typing.type_check_only
class AffineTransform(typing.TypedDict, total=False):
    scaleX: float
    scaleY: float
    shearX: float
    shearY: float
    translateX: float
    translateY: float
    unit: typing.Literal["UNIT_UNSPECIFIED", "EMU", "PT"]

@typing.type_check_only
class AutoText(typing.TypedDict, total=False):
    content: str
    style: TextStyle
    type: typing.Literal["TYPE_UNSPECIFIED", "SLIDE_NUMBER"]

@typing.type_check_only
class Autofit(typing.TypedDict, total=False):
    autofitType: typing.Literal[
        "AUTOFIT_TYPE_UNSPECIFIED", "NONE", "TEXT_AUTOFIT", "SHAPE_AUTOFIT"
    ]
    fontScale: float
    lineSpacingReduction: float

@typing.type_check_only
class BatchUpdatePresentationRequest(typing.TypedDict, total=False):
    requests: _list[Request]
    writeControl: WriteControl

@typing.type_check_only
class BatchUpdatePresentationResponse(typing.TypedDict, total=False):
    presentationId: str
    replies: _list[Response]
    writeControl: WriteControl

@typing.type_check_only
class Bullet(typing.TypedDict, total=False):
    bulletStyle: TextStyle
    glyph: str
    listId: str
    nestingLevel: int

@typing.type_check_only
class ColorScheme(typing.TypedDict, total=False):
    colors: _list[ThemeColorPair]

@typing.type_check_only
class ColorStop(typing.TypedDict, total=False):
    alpha: float
    color: OpaqueColor
    position: float

@typing.type_check_only
class CreateImageRequest(typing.TypedDict, total=False):
    elementProperties: PageElementProperties
    objectId: str
    url: str

@typing.type_check_only
class CreateImageResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class CreateLineRequest(typing.TypedDict, total=False):
    category: typing.Literal["LINE_CATEGORY_UNSPECIFIED", "STRAIGHT", "BENT", "CURVED"]
    elementProperties: PageElementProperties
    lineCategory: typing.Literal["STRAIGHT", "BENT", "CURVED"]
    objectId: str

@typing.type_check_only
class CreateLineResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class CreateParagraphBulletsRequest(typing.TypedDict, total=False):
    bulletPreset: typing.Literal[
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
    cellLocation: TableCellLocation
    objectId: str
    textRange: Range

@typing.type_check_only
class CreateShapeRequest(typing.TypedDict, total=False):
    elementProperties: PageElementProperties
    objectId: str
    shapeType: typing.Literal[
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

@typing.type_check_only
class CreateShapeResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class CreateSheetsChartRequest(typing.TypedDict, total=False):
    chartId: int
    elementProperties: PageElementProperties
    linkingMode: typing.Literal["NOT_LINKED_IMAGE", "LINKED"]
    objectId: str
    spreadsheetId: str

@typing.type_check_only
class CreateSheetsChartResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class CreateSlideRequest(typing.TypedDict, total=False):
    insertionIndex: int
    objectId: str
    placeholderIdMappings: _list[LayoutPlaceholderIdMapping]
    slideLayoutReference: LayoutReference

@typing.type_check_only
class CreateSlideResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class CreateTableRequest(typing.TypedDict, total=False):
    columns: int
    elementProperties: PageElementProperties
    objectId: str
    rows: int

@typing.type_check_only
class CreateTableResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class CreateVideoRequest(typing.TypedDict, total=False):
    elementProperties: PageElementProperties
    id: str
    objectId: str
    source: typing.Literal["SOURCE_UNSPECIFIED", "YOUTUBE", "DRIVE"]

@typing.type_check_only
class CreateVideoResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class CropProperties(typing.TypedDict, total=False):
    angle: float
    bottomOffset: float
    leftOffset: float
    rightOffset: float
    topOffset: float

@typing.type_check_only
class DeleteObjectRequest(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class DeleteParagraphBulletsRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    objectId: str
    textRange: Range

@typing.type_check_only
class DeleteTableColumnRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    tableObjectId: str

@typing.type_check_only
class DeleteTableRowRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    tableObjectId: str

@typing.type_check_only
class DeleteTextRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    objectId: str
    textRange: Range

@typing.type_check_only
class Dimension(typing.TypedDict, total=False):
    magnitude: float
    unit: typing.Literal["UNIT_UNSPECIFIED", "EMU", "PT"]

@typing.type_check_only
class DuplicateObjectRequest(typing.TypedDict, total=False):
    objectId: str
    objectIds: dict[str, typing.Any]

@typing.type_check_only
class DuplicateObjectResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    children: _list[PageElement]

@typing.type_check_only
class GroupObjectsRequest(typing.TypedDict, total=False):
    childrenObjectIds: _list[str]
    groupObjectId: str

@typing.type_check_only
class GroupObjectsResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    contentUrl: str
    imageProperties: ImageProperties
    placeholder: Placeholder
    sourceUrl: str

@typing.type_check_only
class ImageProperties(typing.TypedDict, total=False):
    brightness: float
    contrast: float
    cropProperties: CropProperties
    link: Link
    outline: Outline
    recolor: Recolor
    shadow: Shadow
    transparency: float

@typing.type_check_only
class InsertTableColumnsRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    insertRight: bool
    number: int
    tableObjectId: str

@typing.type_check_only
class InsertTableRowsRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    insertBelow: bool
    number: int
    tableObjectId: str

@typing.type_check_only
class InsertTextRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    insertionIndex: int
    objectId: str
    text: str

@typing.type_check_only
class LayoutPlaceholderIdMapping(typing.TypedDict, total=False):
    layoutPlaceholder: Placeholder
    layoutPlaceholderObjectId: str
    objectId: str

@typing.type_check_only
class LayoutProperties(typing.TypedDict, total=False):
    displayName: str
    masterObjectId: str
    name: str

@typing.type_check_only
class LayoutReference(typing.TypedDict, total=False):
    layoutId: str
    predefinedLayout: typing.Literal[
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

@typing.type_check_only
class Line(typing.TypedDict, total=False):
    lineCategory: typing.Literal[
        "LINE_CATEGORY_UNSPECIFIED", "STRAIGHT", "BENT", "CURVED"
    ]
    lineProperties: LineProperties
    lineType: typing.Literal[
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

@typing.type_check_only
class LineConnection(typing.TypedDict, total=False):
    connectedObjectId: str
    connectionSiteIndex: int

@typing.type_check_only
class LineFill(typing.TypedDict, total=False):
    solidFill: SolidFill

@typing.type_check_only
class LineProperties(typing.TypedDict, total=False):
    dashStyle: typing.Literal[
        "DASH_STYLE_UNSPECIFIED",
        "SOLID",
        "DOT",
        "DASH",
        "DASH_DOT",
        "LONG_DASH",
        "LONG_DASH_DOT",
    ]
    endArrow: typing.Literal[
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
    endConnection: LineConnection
    lineFill: LineFill
    link: Link
    startArrow: typing.Literal[
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
    startConnection: LineConnection
    weight: Dimension

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    pageObjectId: str
    relativeLink: typing.Literal[
        "RELATIVE_SLIDE_LINK_UNSPECIFIED",
        "NEXT_SLIDE",
        "PREVIOUS_SLIDE",
        "FIRST_SLIDE",
        "LAST_SLIDE",
    ]
    slideIndex: int
    url: str

@typing.type_check_only
class List(typing.TypedDict, total=False):
    listId: str
    nestingLevel: dict[str, typing.Any]

@typing.type_check_only
class MasterProperties(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class MergeTableCellsRequest(typing.TypedDict, total=False):
    objectId: str
    tableRange: TableRange

@typing.type_check_only
class NestingLevel(typing.TypedDict, total=False):
    bulletStyle: TextStyle

@typing.type_check_only
class NotesProperties(typing.TypedDict, total=False):
    speakerNotesObjectId: str

@typing.type_check_only
class OpaqueColor(typing.TypedDict, total=False):
    rgbColor: RgbColor
    themeColor: typing.Literal[
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

@typing.type_check_only
class OptionalColor(typing.TypedDict, total=False):
    opaqueColor: OpaqueColor

@typing.type_check_only
class Outline(typing.TypedDict, total=False):
    dashStyle: typing.Literal[
        "DASH_STYLE_UNSPECIFIED",
        "SOLID",
        "DOT",
        "DASH",
        "DASH_DOT",
        "LONG_DASH",
        "LONG_DASH_DOT",
    ]
    outlineFill: OutlineFill
    propertyState: typing.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    weight: Dimension

@typing.type_check_only
class OutlineFill(typing.TypedDict, total=False):
    solidFill: SolidFill

@typing.type_check_only
class Page(typing.TypedDict, total=False):
    layoutProperties: LayoutProperties
    masterProperties: MasterProperties
    notesProperties: NotesProperties
    objectId: str
    pageElements: _list[PageElement]
    pageProperties: PageProperties
    pageType: typing.Literal["SLIDE", "MASTER", "LAYOUT", "NOTES", "NOTES_MASTER"]
    revisionId: str
    slideProperties: SlideProperties

@typing.type_check_only
class PageBackgroundFill(typing.TypedDict, total=False):
    propertyState: typing.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    solidFill: SolidFill
    stretchedPictureFill: StretchedPictureFill

@typing.type_check_only
class PageElement(typing.TypedDict, total=False):
    description: str
    elementGroup: Group
    image: Image
    line: Line
    objectId: str
    shape: Shape
    sheetsChart: SheetsChart
    size: Size
    speakerSpotlight: SpeakerSpotlight
    table: Table
    title: str
    transform: AffineTransform
    video: Video
    wordArt: WordArt

@typing.type_check_only
class PageElementProperties(typing.TypedDict, total=False):
    pageObjectId: str
    size: Size
    transform: AffineTransform

@typing.type_check_only
class PageProperties(typing.TypedDict, total=False):
    colorScheme: ColorScheme
    pageBackgroundFill: PageBackgroundFill

@typing.type_check_only
class ParagraphMarker(typing.TypedDict, total=False):
    bullet: Bullet
    style: ParagraphStyle

@typing.type_check_only
class ParagraphStyle(typing.TypedDict, total=False):
    alignment: typing.Literal[
        "ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END", "JUSTIFIED"
    ]
    direction: typing.Literal[
        "TEXT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    indentEnd: Dimension
    indentFirstLine: Dimension
    indentStart: Dimension
    lineSpacing: float
    spaceAbove: Dimension
    spaceBelow: Dimension
    spacingMode: typing.Literal[
        "SPACING_MODE_UNSPECIFIED", "NEVER_COLLAPSE", "COLLAPSE_LISTS"
    ]

@typing.type_check_only
class Placeholder(typing.TypedDict, total=False):
    index: int
    parentObjectId: str
    type: typing.Literal[
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

@typing.type_check_only
class Presentation(typing.TypedDict, total=False):
    layouts: _list[Page]
    locale: str
    masters: _list[Page]
    notesMaster: Page
    pageSize: Size
    presentationId: str
    revisionId: str
    slides: _list[Page]
    title: str

@typing.type_check_only
class Range(typing.TypedDict, total=False):
    endIndex: int
    startIndex: int
    type: typing.Literal[
        "RANGE_TYPE_UNSPECIFIED", "FIXED_RANGE", "FROM_START_INDEX", "ALL"
    ]

@typing.type_check_only
class Recolor(typing.TypedDict, total=False):
    name: typing.Literal[
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
    recolorStops: _list[ColorStop]

@typing.type_check_only
class RefreshSheetsChartRequest(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class ReplaceAllShapesWithImageRequest(typing.TypedDict, total=False):
    containsText: SubstringMatchCriteria
    imageReplaceMethod: typing.Literal[
        "IMAGE_REPLACE_METHOD_UNSPECIFIED", "CENTER_INSIDE", "CENTER_CROP"
    ]
    imageUrl: str
    pageObjectIds: _list[str]
    replaceMethod: typing.Literal["CENTER_INSIDE", "CENTER_CROP"]

@typing.type_check_only
class ReplaceAllShapesWithImageResponse(typing.TypedDict, total=False):
    occurrencesChanged: int

@typing.type_check_only
class ReplaceAllShapesWithSheetsChartRequest(typing.TypedDict, total=False):
    chartId: int
    containsText: SubstringMatchCriteria
    linkingMode: typing.Literal["NOT_LINKED_IMAGE", "LINKED"]
    pageObjectIds: _list[str]
    spreadsheetId: str

@typing.type_check_only
class ReplaceAllShapesWithSheetsChartResponse(typing.TypedDict, total=False):
    occurrencesChanged: int

@typing.type_check_only
class ReplaceAllTextRequest(typing.TypedDict, total=False):
    containsText: SubstringMatchCriteria
    pageObjectIds: _list[str]
    replaceText: str

@typing.type_check_only
class ReplaceAllTextResponse(typing.TypedDict, total=False):
    occurrencesChanged: int

@typing.type_check_only
class ReplaceImageRequest(typing.TypedDict, total=False):
    imageObjectId: str
    imageReplaceMethod: typing.Literal[
        "IMAGE_REPLACE_METHOD_UNSPECIFIED", "CENTER_INSIDE", "CENTER_CROP"
    ]
    url: str

@typing.type_check_only
class Request(typing.TypedDict, total=False):
    createImage: CreateImageRequest
    createLine: CreateLineRequest
    createParagraphBullets: CreateParagraphBulletsRequest
    createShape: CreateShapeRequest
    createSheetsChart: CreateSheetsChartRequest
    createSlide: CreateSlideRequest
    createTable: CreateTableRequest
    createVideo: CreateVideoRequest
    deleteObject: DeleteObjectRequest
    deleteParagraphBullets: DeleteParagraphBulletsRequest
    deleteTableColumn: DeleteTableColumnRequest
    deleteTableRow: DeleteTableRowRequest
    deleteText: DeleteTextRequest
    duplicateObject: DuplicateObjectRequest
    groupObjects: GroupObjectsRequest
    insertTableColumns: InsertTableColumnsRequest
    insertTableRows: InsertTableRowsRequest
    insertText: InsertTextRequest
    mergeTableCells: MergeTableCellsRequest
    refreshSheetsChart: RefreshSheetsChartRequest
    replaceAllShapesWithImage: ReplaceAllShapesWithImageRequest
    replaceAllShapesWithSheetsChart: ReplaceAllShapesWithSheetsChartRequest
    replaceAllText: ReplaceAllTextRequest
    replaceImage: ReplaceImageRequest
    rerouteLine: RerouteLineRequest
    ungroupObjects: UngroupObjectsRequest
    unmergeTableCells: UnmergeTableCellsRequest
    updateImageProperties: UpdateImagePropertiesRequest
    updateLineCategory: UpdateLineCategoryRequest
    updateLineProperties: UpdateLinePropertiesRequest
    updatePageElementAltText: UpdatePageElementAltTextRequest
    updatePageElementTransform: UpdatePageElementTransformRequest
    updatePageElementsZOrder: UpdatePageElementsZOrderRequest
    updatePageProperties: UpdatePagePropertiesRequest
    updateParagraphStyle: UpdateParagraphStyleRequest
    updateShapeProperties: UpdateShapePropertiesRequest
    updateSlideProperties: UpdateSlidePropertiesRequest
    updateSlidesPosition: UpdateSlidesPositionRequest
    updateTableBorderProperties: UpdateTableBorderPropertiesRequest
    updateTableCellProperties: UpdateTableCellPropertiesRequest
    updateTableColumnProperties: UpdateTableColumnPropertiesRequest
    updateTableRowProperties: UpdateTableRowPropertiesRequest
    updateTextStyle: UpdateTextStyleRequest
    updateVideoProperties: UpdateVideoPropertiesRequest

@typing.type_check_only
class RerouteLineRequest(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class Response(typing.TypedDict, total=False):
    createImage: CreateImageResponse
    createLine: CreateLineResponse
    createShape: CreateShapeResponse
    createSheetsChart: CreateSheetsChartResponse
    createSlide: CreateSlideResponse
    createTable: CreateTableResponse
    createVideo: CreateVideoResponse
    duplicateObject: DuplicateObjectResponse
    groupObjects: GroupObjectsResponse
    replaceAllShapesWithImage: ReplaceAllShapesWithImageResponse
    replaceAllShapesWithSheetsChart: ReplaceAllShapesWithSheetsChartResponse
    replaceAllText: ReplaceAllTextResponse

@typing.type_check_only
class RgbColor(typing.TypedDict, total=False):
    blue: float
    green: float
    red: float

@typing.type_check_only
class Shadow(typing.TypedDict, total=False):
    alignment: typing.Literal[
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
    blurRadius: Dimension
    color: OpaqueColor
    propertyState: typing.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    rotateWithShape: bool
    transform: AffineTransform
    type: typing.Literal["SHADOW_TYPE_UNSPECIFIED", "OUTER"]

@typing.type_check_only
class Shape(typing.TypedDict, total=False):
    placeholder: Placeholder
    shapeProperties: ShapeProperties
    shapeType: typing.Literal[
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

@typing.type_check_only
class ShapeBackgroundFill(typing.TypedDict, total=False):
    propertyState: typing.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    solidFill: SolidFill

@typing.type_check_only
class ShapeProperties(typing.TypedDict, total=False):
    autofit: Autofit
    contentAlignment: typing.Literal[
        "CONTENT_ALIGNMENT_UNSPECIFIED",
        "CONTENT_ALIGNMENT_UNSUPPORTED",
        "TOP",
        "MIDDLE",
        "BOTTOM",
    ]
    link: Link
    outline: Outline
    shadow: Shadow
    shapeBackgroundFill: ShapeBackgroundFill

@typing.type_check_only
class SheetsChart(typing.TypedDict, total=False):
    chartId: int
    contentUrl: str
    sheetsChartProperties: SheetsChartProperties
    spreadsheetId: str

@typing.type_check_only
class SheetsChartProperties(typing.TypedDict, total=False):
    chartImageProperties: ImageProperties

@typing.type_check_only
class Size(typing.TypedDict, total=False):
    height: Dimension
    width: Dimension

@typing.type_check_only
class SlideProperties(typing.TypedDict, total=False):
    isSkipped: bool
    layoutObjectId: str
    masterObjectId: str
    notesPage: Page

@typing.type_check_only
class SolidFill(typing.TypedDict, total=False):
    alpha: float
    color: OpaqueColor

@typing.type_check_only
class SpeakerSpotlight(typing.TypedDict, total=False):
    speakerSpotlightProperties: SpeakerSpotlightProperties

@typing.type_check_only
class SpeakerSpotlightProperties(typing.TypedDict, total=False):
    outline: Outline
    shadow: Shadow

@typing.type_check_only
class StretchedPictureFill(typing.TypedDict, total=False):
    contentUrl: str
    size: Size

@typing.type_check_only
class SubstringMatchCriteria(typing.TypedDict, total=False):
    matchCase: bool
    searchByRegex: bool
    text: str

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    columns: int
    horizontalBorderRows: _list[TableBorderRow]
    rows: int
    tableColumns: _list[TableColumnProperties]
    tableRows: _list[TableRow]
    verticalBorderRows: _list[TableBorderRow]

@typing.type_check_only
class TableBorderCell(typing.TypedDict, total=False):
    location: TableCellLocation
    tableBorderProperties: TableBorderProperties

@typing.type_check_only
class TableBorderFill(typing.TypedDict, total=False):
    solidFill: SolidFill

@typing.type_check_only
class TableBorderProperties(typing.TypedDict, total=False):
    dashStyle: typing.Literal[
        "DASH_STYLE_UNSPECIFIED",
        "SOLID",
        "DOT",
        "DASH",
        "DASH_DOT",
        "LONG_DASH",
        "LONG_DASH_DOT",
    ]
    tableBorderFill: TableBorderFill
    weight: Dimension

@typing.type_check_only
class TableBorderRow(typing.TypedDict, total=False):
    tableBorderCells: _list[TableBorderCell]

@typing.type_check_only
class TableCell(typing.TypedDict, total=False):
    columnSpan: int
    location: TableCellLocation
    rowSpan: int
    tableCellProperties: TableCellProperties
    text: TextContent

@typing.type_check_only
class TableCellBackgroundFill(typing.TypedDict, total=False):
    propertyState: typing.Literal["RENDERED", "NOT_RENDERED", "INHERIT"]
    solidFill: SolidFill

@typing.type_check_only
class TableCellLocation(typing.TypedDict, total=False):
    columnIndex: int
    rowIndex: int

@typing.type_check_only
class TableCellProperties(typing.TypedDict, total=False):
    contentAlignment: typing.Literal[
        "CONTENT_ALIGNMENT_UNSPECIFIED",
        "CONTENT_ALIGNMENT_UNSUPPORTED",
        "TOP",
        "MIDDLE",
        "BOTTOM",
    ]
    tableCellBackgroundFill: TableCellBackgroundFill

@typing.type_check_only
class TableColumnProperties(typing.TypedDict, total=False):
    columnWidth: Dimension

@typing.type_check_only
class TableRange(typing.TypedDict, total=False):
    columnSpan: int
    location: TableCellLocation
    rowSpan: int

@typing.type_check_only
class TableRow(typing.TypedDict, total=False):
    rowHeight: Dimension
    tableCells: _list[TableCell]
    tableRowProperties: TableRowProperties

@typing.type_check_only
class TableRowProperties(typing.TypedDict, total=False):
    minRowHeight: Dimension

@typing.type_check_only
class TextContent(typing.TypedDict, total=False):
    lists: dict[str, typing.Any]
    textElements: _list[TextElement]

@typing.type_check_only
class TextElement(typing.TypedDict, total=False):
    autoText: AutoText
    endIndex: int
    paragraphMarker: ParagraphMarker
    startIndex: int
    textRun: TextRun

@typing.type_check_only
class TextRun(typing.TypedDict, total=False):
    content: str
    style: TextStyle

@typing.type_check_only
class TextStyle(typing.TypedDict, total=False):
    backgroundColor: OptionalColor
    baselineOffset: typing.Literal[
        "BASELINE_OFFSET_UNSPECIFIED", "NONE", "SUPERSCRIPT", "SUBSCRIPT"
    ]
    bold: bool
    fontFamily: str
    fontSize: Dimension
    foregroundColor: OptionalColor
    italic: bool
    link: Link
    smallCaps: bool
    strikethrough: bool
    underline: bool
    weightedFontFamily: WeightedFontFamily

@typing.type_check_only
class ThemeColorPair(typing.TypedDict, total=False):
    color: RgbColor
    type: typing.Literal[
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

@typing.type_check_only
class Thumbnail(typing.TypedDict, total=False):
    contentUrl: str
    height: int
    width: int

@typing.type_check_only
class UngroupObjectsRequest(typing.TypedDict, total=False):
    objectIds: _list[str]

@typing.type_check_only
class UnmergeTableCellsRequest(typing.TypedDict, total=False):
    objectId: str
    tableRange: TableRange

@typing.type_check_only
class UpdateImagePropertiesRequest(typing.TypedDict, total=False):
    fields: str
    imageProperties: ImageProperties
    objectId: str

@typing.type_check_only
class UpdateLineCategoryRequest(typing.TypedDict, total=False):
    lineCategory: typing.Literal[
        "LINE_CATEGORY_UNSPECIFIED", "STRAIGHT", "BENT", "CURVED"
    ]
    objectId: str

@typing.type_check_only
class UpdateLinePropertiesRequest(typing.TypedDict, total=False):
    fields: str
    lineProperties: LineProperties
    objectId: str

@typing.type_check_only
class UpdatePageElementAltTextRequest(typing.TypedDict, total=False):
    description: str
    objectId: str
    title: str

@typing.type_check_only
class UpdatePageElementTransformRequest(typing.TypedDict, total=False):
    applyMode: typing.Literal["APPLY_MODE_UNSPECIFIED", "RELATIVE", "ABSOLUTE"]
    objectId: str
    transform: AffineTransform

@typing.type_check_only
class UpdatePageElementsZOrderRequest(typing.TypedDict, total=False):
    operation: typing.Literal[
        "Z_ORDER_OPERATION_UNSPECIFIED",
        "BRING_TO_FRONT",
        "BRING_FORWARD",
        "SEND_BACKWARD",
        "SEND_TO_BACK",
    ]
    pageElementObjectIds: _list[str]

@typing.type_check_only
class UpdatePagePropertiesRequest(typing.TypedDict, total=False):
    fields: str
    objectId: str
    pageProperties: PageProperties

@typing.type_check_only
class UpdateParagraphStyleRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    fields: str
    objectId: str
    style: ParagraphStyle
    textRange: Range

@typing.type_check_only
class UpdateShapePropertiesRequest(typing.TypedDict, total=False):
    fields: str
    objectId: str
    shapeProperties: ShapeProperties

@typing.type_check_only
class UpdateSlidePropertiesRequest(typing.TypedDict, total=False):
    fields: str
    objectId: str
    slideProperties: SlideProperties

@typing.type_check_only
class UpdateSlidesPositionRequest(typing.TypedDict, total=False):
    insertionIndex: int
    slideObjectIds: _list[str]

@typing.type_check_only
class UpdateTableBorderPropertiesRequest(typing.TypedDict, total=False):
    borderPosition: typing.Literal[
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
    fields: str
    objectId: str
    tableBorderProperties: TableBorderProperties
    tableRange: TableRange

@typing.type_check_only
class UpdateTableCellPropertiesRequest(typing.TypedDict, total=False):
    fields: str
    objectId: str
    tableCellProperties: TableCellProperties
    tableRange: TableRange

@typing.type_check_only
class UpdateTableColumnPropertiesRequest(typing.TypedDict, total=False):
    columnIndices: _list[int]
    fields: str
    objectId: str
    tableColumnProperties: TableColumnProperties

@typing.type_check_only
class UpdateTableRowPropertiesRequest(typing.TypedDict, total=False):
    fields: str
    objectId: str
    rowIndices: _list[int]
    tableRowProperties: TableRowProperties

@typing.type_check_only
class UpdateTextStyleRequest(typing.TypedDict, total=False):
    cellLocation: TableCellLocation
    fields: str
    objectId: str
    style: TextStyle
    textRange: Range

@typing.type_check_only
class UpdateVideoPropertiesRequest(typing.TypedDict, total=False):
    fields: str
    objectId: str
    videoProperties: VideoProperties

@typing.type_check_only
class Video(typing.TypedDict, total=False):
    id: str
    source: typing.Literal["SOURCE_UNSPECIFIED", "YOUTUBE", "DRIVE"]
    url: str
    videoProperties: VideoProperties

@typing.type_check_only
class VideoProperties(typing.TypedDict, total=False):
    autoPlay: bool
    end: int
    mute: bool
    outline: Outline
    start: int

@typing.type_check_only
class WeightedFontFamily(typing.TypedDict, total=False):
    fontFamily: str
    weight: int

@typing.type_check_only
class WordArt(typing.TypedDict, total=False):
    renderedText: str

@typing.type_check_only
class WriteControl(typing.TypedDict, total=False):
    requiredRevisionId: str
