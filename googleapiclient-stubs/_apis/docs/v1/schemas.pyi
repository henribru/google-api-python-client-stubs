import typing

import typing_extensions

class AutoText(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PAGE_NUMBER", "PAGE_COUNT"]
    suggestedInsertionIds: typing.List[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: typing.Dict[str, typing.Any]
    suggestedDeletionIds: typing.List[str]

class CreateFootnoteRequest(typing_extensions.TypedDict, total=False):
    location: Location
    endOfSegmentLocation: EndOfSegmentLocation

class InlineObjectPropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    embeddedObjectSuggestionState: EmbeddedObjectSuggestionState

class Response(typing_extensions.TypedDict, total=False):
    createHeader: CreateHeaderResponse
    insertInlineSheetsChart: InsertInlineSheetsChartResponse
    createNamedRange: CreateNamedRangeResponse
    createFooter: CreateFooterResponse
    insertInlineImage: InsertInlineImageResponse
    replaceAllText: ReplaceAllTextResponse
    createFootnote: CreateFootnoteResponse

class ObjectReferences(typing_extensions.TypedDict, total=False):
    objectIds: typing.List[str]

class TableCellBorder(typing_extensions.TypedDict, total=False):
    color: OptionalColor
    width: Dimension
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"
    ]

class DocumentStyle(typing_extensions.TypedDict, total=False):
    defaultHeaderId: str
    marginHeader: Dimension
    evenPageFooterId: str
    useFirstPageHeaderFooter: bool
    marginFooter: Dimension
    defaultFooterId: str
    marginRight: Dimension
    background: Background
    pageSize: Size
    marginTop: Dimension
    useCustomHeaderFooterMargins: bool
    evenPageHeaderId: str
    firstPageFooterId: str
    useEvenPageHeaderFooter: bool
    pageNumberStart: int
    marginBottom: Dimension
    marginLeft: Dimension
    firstPageHeaderId: str

class DeleteFooterRequest(typing_extensions.TypedDict, total=False):
    footerId: str

class PageBreak(typing_extensions.TypedDict, total=False):
    suggestedTextStyleChanges: typing.Dict[str, typing.Any]
    textStyle: TextStyle
    suggestedInsertionIds: typing.List[str]
    suggestedDeletionIds: typing.List[str]

class CreateFooterResponse(typing_extensions.TypedDict, total=False):
    footerId: str

class InsertSectionBreakRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "CONTINUOUS", "NEXT_PAGE"
    ]

class MergeTableCellsRequest(typing_extensions.TypedDict, total=False):
    tableRange: TableRange

class EmbeddedObjectBorderSuggestionState(typing_extensions.TypedDict, total=False):
    dashStyleSuggested: bool
    colorSuggested: bool
    propertyStateSuggested: bool
    widthSuggested: bool

class CreateFooterRequest(typing_extensions.TypedDict, total=False):
    sectionBreakLocation: Location
    type: typing_extensions.Literal["HEADER_FOOTER_TYPE_UNSPECIFIED", "DEFAULT"]

class ParagraphElement(typing_extensions.TypedDict, total=False):
    startIndex: int
    inlineObjectElement: InlineObjectElement
    horizontalRule: HorizontalRule
    columnBreak: ColumnBreak
    endIndex: int
    autoText: AutoText
    pageBreak: PageBreak
    equation: Equation
    textRun: TextRun
    footnoteReference: FootnoteReference

class ReplaceImageRequest(typing_extensions.TypedDict, total=False):
    imageReplaceMethod: typing_extensions.Literal[
        "IMAGE_REPLACE_METHOD_UNSPECIFIED", "CENTER_CROP"
    ]
    uri: str
    imageObjectId: str

class InsertInlineImageResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class Bullet(typing_extensions.TypedDict, total=False):
    listId: str
    textStyle: TextStyle
    nestingLevel: int

class InsertPageBreakRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location

class Color(typing_extensions.TypedDict, total=False):
    rgbColor: RgbColor

class CreateParagraphBulletsRequest(typing_extensions.TypedDict, total=False):
    range: Range
    bulletPreset: typing_extensions.Literal[
        "BULLET_GLYPH_PRESET_UNSPECIFIED",
        "BULLET_DISC_CIRCLE_SQUARE",
        "BULLET_DIAMONDX_ARROW3D_SQUARE",
        "BULLET_CHECKBOX",
        "BULLET_ARROW_DIAMOND_DISC",
        "BULLET_STAR_CIRCLE_SQUARE",
        "BULLET_ARROW3D_CIRCLE_SQUARE",
        "BULLET_LEFTTRIANGLE_DIAMOND_DISC",
        "BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE",
        "BULLET_DIAMOND_CIRCLE_SQUARE",
        "NUMBERED_DECIMAL_ALPHA_ROMAN",
        "NUMBERED_DECIMAL_ALPHA_ROMAN_PARENS",
        "NUMBERED_DECIMAL_NESTED",
        "NUMBERED_UPPERALPHA_ALPHA_ROMAN",
        "NUMBERED_UPPERROMAN_UPPERALPHA_DECIMAL",
        "NUMBERED_ZERODECIMAL_ALPHA_ROMAN",
    ]

class Footer(typing_extensions.TypedDict, total=False):
    content: typing.List[StructuralElement]
    footerId: str

class NamedStylesSuggestionState(typing_extensions.TypedDict, total=False):
    stylesSuggestionStates: typing.List[NamedStyleSuggestionState]

class SuggestedNamedStyles(typing_extensions.TypedDict, total=False):
    namedStylesSuggestionState: NamedStylesSuggestionState
    namedStyles: NamedStyles

class TableOfContents(typing_extensions.TypedDict, total=False):
    content: typing.List[StructuralElement]
    suggestedInsertionIds: typing.List[str]
    suggestedDeletionIds: typing.List[str]

class NamedStyles(typing_extensions.TypedDict, total=False):
    styles: typing.List[NamedStyle]

class HorizontalRule(typing_extensions.TypedDict, total=False):
    suggestedInsertionIds: typing.List[str]
    suggestedTextStyleChanges: typing.Dict[str, typing.Any]
    suggestedDeletionIds: typing.List[str]
    textStyle: TextStyle

class TableRowStyle(typing_extensions.TypedDict, total=False):
    minRowHeight: Dimension

class DocumentStyleSuggestionState(typing_extensions.TypedDict, total=False):
    evenPageHeaderIdSuggested: bool
    pageNumberStartSuggested: bool
    firstPageHeaderIdSuggested: bool
    defaultFooterIdSuggested: bool
    pageSizeSuggestionState: SizeSuggestionState
    marginHeaderSuggested: bool
    firstPageFooterIdSuggested: bool
    evenPageFooterIdSuggested: bool
    useFirstPageHeaderFooterSuggested: bool
    backgroundSuggestionState: BackgroundSuggestionState
    defaultHeaderIdSuggested: bool
    marginBottomSuggested: bool
    useEvenPageHeaderFooterSuggested: bool
    marginTopSuggested: bool
    marginLeftSuggested: bool
    useCustomHeaderFooterMarginsSuggested: bool
    marginRightSuggested: bool
    marginFooterSuggested: bool

class ParagraphBorder(typing_extensions.TypedDict, total=False):
    padding: Dimension
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"
    ]
    color: OptionalColor
    width: Dimension

class Link(typing_extensions.TypedDict, total=False):
    url: str
    headingId: str
    bookmarkId: str

class DeleteNamedRangeRequest(typing_extensions.TypedDict, total=False):
    namedRangeId: str
    name: str

class List(typing_extensions.TypedDict, total=False):
    suggestedInsertionId: str
    suggestedDeletionIds: typing.List[str]
    suggestedListPropertiesChanges: typing.Dict[str, typing.Any]
    listProperties: ListProperties

class TextRun(typing_extensions.TypedDict, total=False):
    content: str
    textStyle: TextStyle
    suggestedTextStyleChanges: typing.Dict[str, typing.Any]
    suggestedDeletionIds: typing.List[str]
    suggestedInsertionIds: typing.List[str]

class SectionColumnProperties(typing_extensions.TypedDict, total=False):
    paddingEnd: Dimension
    width: Dimension

class ImageProperties(typing_extensions.TypedDict, total=False):
    brightness: float
    contrast: float
    cropProperties: CropProperties
    contentUri: str
    sourceUri: str
    angle: float
    transparency: float

class SectionStyle(typing_extensions.TypedDict, total=False):
    evenPageHeaderId: str
    useFirstPageHeaderFooter: bool
    columnProperties: typing.List[SectionColumnProperties]
    pageNumberStart: int
    defaultFooterId: str
    defaultHeaderId: str
    marginFooter: Dimension
    contentDirection: typing_extensions.Literal[
        "CONTENT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    marginBottom: Dimension
    marginRight: Dimension
    marginLeft: Dimension
    firstPageHeaderId: str
    firstPageFooterId: str
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "CONTINUOUS", "NEXT_PAGE"
    ]
    evenPageFooterId: str
    marginTop: Dimension
    columnSeparatorStyle: typing_extensions.Literal[
        "COLUMN_SEPARATOR_STYLE_UNSPECIFIED", "NONE", "BETWEEN_EACH_COLUMN"
    ]
    marginHeader: Dimension

class Background(typing_extensions.TypedDict, total=False):
    color: OptionalColor

class InlineObjectProperties(typing_extensions.TypedDict, total=False):
    embeddedObject: EmbeddedObject

class RgbColor(typing_extensions.TypedDict, total=False):
    green: float
    blue: float
    red: float

class InsertTableColumnRequest(typing_extensions.TypedDict, total=False):
    tableCellLocation: TableCellLocation
    insertRight: bool

class PositionedObjectPositioningSuggestionState(
    typing_extensions.TypedDict, total=False
):
    layoutSuggested: bool
    topOffsetSuggested: bool
    leftOffsetSuggested: bool

class Shading(typing_extensions.TypedDict, total=False):
    backgroundColor: OptionalColor

class Paragraph(typing_extensions.TypedDict, total=False):
    elements: typing.List[ParagraphElement]
    suggestedPositionedObjectIds: typing.Dict[str, typing.Any]
    paragraphStyle: ParagraphStyle
    bullet: Bullet
    positionedObjectIds: typing.List[str]
    suggestedParagraphStyleChanges: typing.Dict[str, typing.Any]
    suggestedBulletChanges: typing.Dict[str, typing.Any]

class ListPropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    nestingLevelsSuggestionStates: typing.List[NestingLevelSuggestionState]

class DeletePositionedObjectRequest(typing_extensions.TypedDict, total=False):
    objectId: str

class SuggestedParagraphStyle(typing_extensions.TypedDict, total=False):
    paragraphStyleSuggestionState: ParagraphStyleSuggestionState
    paragraphStyle: ParagraphStyle

class ParagraphStyle(typing_extensions.TypedDict, total=False):
    namedStyleType: typing_extensions.Literal[
        "NAMED_STYLE_TYPE_UNSPECIFIED",
        "NORMAL_TEXT",
        "TITLE",
        "SUBTITLE",
        "HEADING_1",
        "HEADING_2",
        "HEADING_3",
        "HEADING_4",
        "HEADING_5",
        "HEADING_6",
    ]
    keepWithNext: bool
    lineSpacing: float
    shading: Shading
    alignment: typing_extensions.Literal[
        "ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END", "JUSTIFIED"
    ]
    direction: typing_extensions.Literal[
        "CONTENT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    indentEnd: Dimension
    borderLeft: ParagraphBorder
    tabStops: typing.List[TabStop]
    keepLinesTogether: bool
    borderBottom: ParagraphBorder
    spacingMode: typing_extensions.Literal[
        "SPACING_MODE_UNSPECIFIED", "NEVER_COLLAPSE", "COLLAPSE_LISTS"
    ]
    headingId: str
    borderBetween: ParagraphBorder
    spaceBelow: Dimension
    indentStart: Dimension
    borderRight: ParagraphBorder
    spaceAbove: Dimension
    borderTop: ParagraphBorder
    avoidWidowAndOrphan: bool
    indentFirstLine: Dimension

class InsertInlineImageRequest(typing_extensions.TypedDict, total=False):
    location: Location
    objectSize: Size
    endOfSegmentLocation: EndOfSegmentLocation
    uri: str

class SuggestedBullet(typing_extensions.TypedDict, total=False):
    bullet: Bullet
    bulletSuggestionState: BulletSuggestionState

class TextStyleSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundColorSuggested: bool
    italicSuggested: bool
    baselineOffsetSuggested: bool
    strikethroughSuggested: bool
    weightedFontFamilySuggested: bool
    underlineSuggested: bool
    fontSizeSuggested: bool
    foregroundColorSuggested: bool
    boldSuggested: bool
    smallCapsSuggested: bool
    linkSuggested: bool

class TableStyle(typing_extensions.TypedDict, total=False):
    tableColumnProperties: typing.List[TableColumnProperties]

class BatchUpdateDocumentRequest(typing_extensions.TypedDict, total=False):
    requests: typing.List[Request]
    writeControl: WriteControl

class InsertTableRequest(typing_extensions.TypedDict, total=False):
    rows: int
    location: Location
    columns: int
    endOfSegmentLocation: EndOfSegmentLocation

class SuggestedListProperties(typing_extensions.TypedDict, total=False):
    listPropertiesSuggestionState: ListPropertiesSuggestionState
    listProperties: ListProperties

class CropProperties(typing_extensions.TypedDict, total=False):
    offsetLeft: float
    offsetRight: float
    offsetBottom: float
    offsetTop: float
    angle: float

class ListProperties(typing_extensions.TypedDict, total=False):
    nestingLevels: typing.List[NestingLevel]

class CropPropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    offsetBottomSuggested: bool
    angleSuggested: bool
    offsetLeftSuggested: bool
    offsetRightSuggested: bool
    offsetTopSuggested: bool

class NestingLevelSuggestionState(typing_extensions.TypedDict, total=False):
    bulletAlignmentSuggested: bool
    glyphTypeSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState
    indentFirstLineSuggested: bool
    glyphSymbolSuggested: bool
    glyphFormatSuggested: bool
    indentStartSuggested: bool
    startNumberSuggested: bool

class DeleteHeaderRequest(typing_extensions.TypedDict, total=False):
    headerId: str

class TableCellLocation(typing_extensions.TypedDict, total=False):
    tableStartLocation: Location
    rowIndex: int
    columnIndex: int

class NestingLevel(typing_extensions.TypedDict, total=False):
    glyphType: typing_extensions.Literal[
        "GLYPH_TYPE_UNSPECIFIED",
        "NONE",
        "DECIMAL",
        "ZERO_DECIMAL",
        "UPPER_ALPHA",
        "ALPHA",
        "UPPER_ROMAN",
        "ROMAN",
    ]
    indentStart: Dimension
    glyphFormat: str
    startNumber: int
    indentFirstLine: Dimension
    textStyle: TextStyle
    glyphSymbol: str
    bulletAlignment: typing_extensions.Literal[
        "BULLET_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]

class InsertTextRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    text: str

class NamedStyleSuggestionState(typing_extensions.TypedDict, total=False):
    textStyleSuggestionState: TextStyleSuggestionState
    namedStyleType: typing_extensions.Literal[
        "NAMED_STYLE_TYPE_UNSPECIFIED",
        "NORMAL_TEXT",
        "TITLE",
        "SUBTITLE",
        "HEADING_1",
        "HEADING_2",
        "HEADING_3",
        "HEADING_4",
        "HEADING_5",
        "HEADING_6",
    ]
    paragraphStyleSuggestionState: ParagraphStyleSuggestionState

class SizeSuggestionState(typing_extensions.TypedDict, total=False):
    heightSuggested: bool
    widthSuggested: bool

class SuggestedInlineObjectProperties(typing_extensions.TypedDict, total=False):
    inlineObjectPropertiesSuggestionState: InlineObjectPropertiesSuggestionState
    inlineObjectProperties: InlineObjectProperties

class UpdateTableRowStyleRequest(typing_extensions.TypedDict, total=False):
    tableRowStyle: TableRowStyle
    tableStartLocation: Location
    fields: str
    rowIndices: typing.List[int]

class Equation(typing_extensions.TypedDict, total=False):
    suggestedDeletionIds: typing.List[str]
    suggestedInsertionIds: typing.List[str]

class UpdateTableColumnPropertiesRequest(typing_extensions.TypedDict, total=False):
    tableStartLocation: Location
    columnIndices: typing.List[int]
    tableColumnProperties: TableColumnProperties
    fields: str

class SuggestedTableCellStyle(typing_extensions.TypedDict, total=False):
    tableCellStyleSuggestionState: TableCellStyleSuggestionState
    tableCellStyle: TableCellStyle

class EmbeddedObjectSuggestionState(typing_extensions.TypedDict, total=False):
    marginLeftSuggested: bool
    marginRightSuggested: bool
    embeddedObjectBorderSuggestionState: EmbeddedObjectBorderSuggestionState
    imagePropertiesSuggestionState: ImagePropertiesSuggestionState
    sizeSuggestionState: SizeSuggestionState
    titleSuggested: bool
    embeddedDrawingPropertiesSuggestionState: EmbeddedDrawingPropertiesSuggestionState
    marginBottomSuggested: bool
    descriptionSuggested: bool
    linkedContentReferenceSuggestionState: LinkedContentReferenceSuggestionState
    marginTopSuggested: bool

class UpdateSectionStyleRequest(typing_extensions.TypedDict, total=False):
    range: Range
    fields: str
    sectionStyle: SectionStyle

class CreateHeaderRequest(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["HEADER_FOOTER_TYPE_UNSPECIFIED", "DEFAULT"]
    sectionBreakLocation: Location

class SubstringMatchCriteria(typing_extensions.TypedDict, total=False):
    matchCase: bool
    text: str

class SectionBreak(typing_extensions.TypedDict, total=False):
    suggestedInsertionIds: typing.List[str]
    suggestedDeletionIds: typing.List[str]
    sectionStyle: SectionStyle

class SuggestedPositionedObjectProperties(typing_extensions.TypedDict, total=False):
    positionedObjectPropertiesSuggestionState: PositionedObjectPropertiesSuggestionState
    positionedObjectProperties: PositionedObjectProperties

class BackgroundSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundColorSuggested: bool

class InsertTableRowRequest(typing_extensions.TypedDict, total=False):
    tableCellLocation: TableCellLocation
    insertBelow: bool

class PositionedObjectPropertiesSuggestionState(
    typing_extensions.TypedDict, total=False
):
    positioningSuggestionState: PositionedObjectPositioningSuggestionState
    embeddedObjectSuggestionState: EmbeddedObjectSuggestionState

class SheetsChartReference(typing_extensions.TypedDict, total=False):
    spreadsheetId: str
    chartId: int

class ShadingSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundColorSuggested: bool

class SuggestedTableRowStyle(typing_extensions.TypedDict, total=False):
    tableRowStyleSuggestionState: TableRowStyleSuggestionState
    tableRowStyle: TableRowStyle

class NamedRange(typing_extensions.TypedDict, total=False):
    name: str
    ranges: typing.List[Range]
    namedRangeId: str

class UpdateParagraphStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    paragraphStyle: ParagraphStyle
    range: Range

class InlineObject(typing_extensions.TypedDict, total=False):
    suggestedInlineObjectPropertiesChanges: typing.Dict[str, typing.Any]
    suggestedInsertionId: str
    objectId: str
    suggestedDeletionIds: typing.List[str]
    inlineObjectProperties: InlineObjectProperties

class TableRow(typing_extensions.TypedDict, total=False):
    suggestedTableRowStyleChanges: typing.Dict[str, typing.Any]
    tableCells: typing.List[TableCell]
    tableRowStyle: TableRowStyle
    startIndex: int
    suggestedInsertionIds: typing.List[str]
    suggestedDeletionIds: typing.List[str]
    endIndex: int

class DeleteTableColumnRequest(typing_extensions.TypedDict, total=False):
    tableCellLocation: TableCellLocation

class TabStop(typing_extensions.TypedDict, total=False):
    offset: Dimension
    alignment: typing_extensions.Literal[
        "TAB_STOP_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]

class UpdateDocumentStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    documentStyle: DocumentStyle

class ColumnBreak(typing_extensions.TypedDict, total=False):
    suggestedTextStyleChanges: typing.Dict[str, typing.Any]
    suggestedDeletionIds: typing.List[str]
    suggestedInsertionIds: typing.List[str]
    textStyle: TextStyle

class CreateFootnoteResponse(typing_extensions.TypedDict, total=False):
    footnoteId: str

class FootnoteReference(typing_extensions.TypedDict, total=False):
    footnoteId: str
    textStyle: TextStyle
    footnoteNumber: str
    suggestedDeletionIds: typing.List[str]
    suggestedTextStyleChanges: typing.Dict[str, typing.Any]
    suggestedInsertionIds: typing.List[str]

class EmbeddedDrawingProperties(typing_extensions.TypedDict, total=False): ...

class EmbeddedObject(typing_extensions.TypedDict, total=False):
    embeddedDrawingProperties: EmbeddedDrawingProperties
    imageProperties: ImageProperties
    marginLeft: Dimension
    description: str
    linkedContentReference: LinkedContentReference
    marginRight: Dimension
    marginBottom: Dimension
    marginTop: Dimension
    embeddedObjectBorder: EmbeddedObjectBorder
    size: Size
    title: str

class OptionalColor(typing_extensions.TypedDict, total=False):
    color: Color

class ReplaceAllTextRequest(typing_extensions.TypedDict, total=False):
    replaceText: str
    containsText: SubstringMatchCriteria

class EndOfSegmentLocation(typing_extensions.TypedDict, total=False):
    segmentId: str

class EmbeddedDrawingPropertiesSuggestionState(
    typing_extensions.TypedDict, total=False
): ...

class TextStyle(typing_extensions.TypedDict, total=False):
    foregroundColor: OptionalColor
    baselineOffset: typing_extensions.Literal[
        "BASELINE_OFFSET_UNSPECIFIED", "NONE", "SUPERSCRIPT", "SUBSCRIPT"
    ]
    bold: bool
    link: Link
    fontSize: Dimension
    underline: bool
    weightedFontFamily: WeightedFontFamily
    italic: bool
    smallCaps: bool
    backgroundColor: OptionalColor
    strikethrough: bool

class TableCellStyleSuggestionState(typing_extensions.TypedDict, total=False):
    paddingTopSuggested: bool
    contentAlignmentSuggested: bool
    paddingRightSuggested: bool
    paddingBottomSuggested: bool
    backgroundColorSuggested: bool
    borderTopSuggested: bool
    rowSpanSuggested: bool
    borderBottomSuggested: bool
    columnSpanSuggested: bool
    paddingLeftSuggested: bool
    borderLeftSuggested: bool
    borderRightSuggested: bool

class Range(typing_extensions.TypedDict, total=False):
    segmentId: str
    startIndex: int
    endIndex: int

class Document(typing_extensions.TypedDict, total=False):
    body: Body
    footers: typing.Dict[str, typing.Any]
    suggestionsViewMode: typing_extensions.Literal[
        "DEFAULT_FOR_CURRENT_ACCESS",
        "SUGGESTIONS_INLINE",
        "PREVIEW_SUGGESTIONS_ACCEPTED",
        "PREVIEW_WITHOUT_SUGGESTIONS",
    ]
    documentId: str
    namedStyles: NamedStyles
    documentStyle: DocumentStyle
    suggestedDocumentStyleChanges: typing.Dict[str, typing.Any]
    footnotes: typing.Dict[str, typing.Any]
    namedRanges: typing.Dict[str, typing.Any]
    title: str
    suggestedNamedStylesChanges: typing.Dict[str, typing.Any]
    lists: typing.Dict[str, typing.Any]
    headers: typing.Dict[str, typing.Any]
    positionedObjects: typing.Dict[str, typing.Any]
    revisionId: str
    inlineObjects: typing.Dict[str, typing.Any]

class Request(typing_extensions.TypedDict, total=False):
    deleteNamedRange: DeleteNamedRangeRequest
    insertTableColumn: InsertTableColumnRequest
    updateSectionStyle: UpdateSectionStyleRequest
    createFooter: CreateFooterRequest
    createHeader: CreateHeaderRequest
    insertInlineImage: InsertInlineImageRequest
    updateTableCellStyle: UpdateTableCellStyleRequest
    replaceNamedRangeContent: ReplaceNamedRangeContentRequest
    insertPageBreak: InsertPageBreakRequest
    updateDocumentStyle: UpdateDocumentStyleRequest
    deleteTableRow: DeleteTableRowRequest
    unmergeTableCells: UnmergeTableCellsRequest
    createParagraphBullets: CreateParagraphBulletsRequest
    deleteContentRange: DeleteContentRangeRequest
    deleteHeader: DeleteHeaderRequest
    insertSectionBreak: InsertSectionBreakRequest
    updateTextStyle: UpdateTextStyleRequest
    deleteParagraphBullets: DeleteParagraphBulletsRequest
    createNamedRange: CreateNamedRangeRequest
    deletePositionedObject: DeletePositionedObjectRequest
    updateParagraphStyle: UpdateParagraphStyleRequest
    deleteTableColumn: DeleteTableColumnRequest
    updateTableRowStyle: UpdateTableRowStyleRequest
    replaceImage: ReplaceImageRequest
    insertTable: InsertTableRequest
    replaceAllText: ReplaceAllTextRequest
    deleteFooter: DeleteFooterRequest
    insertText: InsertTextRequest
    insertTableRow: InsertTableRowRequest
    createFootnote: CreateFootnoteRequest
    updateTableColumnProperties: UpdateTableColumnPropertiesRequest
    mergeTableCells: MergeTableCellsRequest

class SuggestedDocumentStyle(typing_extensions.TypedDict, total=False):
    documentStyleSuggestionState: DocumentStyleSuggestionState
    documentStyle: DocumentStyle

class Header(typing_extensions.TypedDict, total=False):
    content: typing.List[StructuralElement]
    headerId: str

class DeleteTableRowRequest(typing_extensions.TypedDict, total=False):
    tableCellLocation: TableCellLocation

class InlineObjectElement(typing_extensions.TypedDict, total=False):
    suggestedTextStyleChanges: typing.Dict[str, typing.Any]
    textStyle: TextStyle
    suggestedInsertionIds: typing.List[str]
    suggestedDeletionIds: typing.List[str]
    inlineObjectId: str

class TableColumnProperties(typing_extensions.TypedDict, total=False):
    widthType: typing_extensions.Literal[
        "WIDTH_TYPE_UNSPECIFIED", "EVENLY_DISTRIBUTED", "FIXED_WIDTH"
    ]
    width: Dimension

class TableCellStyle(typing_extensions.TypedDict, total=False):
    paddingLeft: Dimension
    paddingBottom: Dimension
    borderBottom: TableCellBorder
    borderLeft: TableCellBorder
    rowSpan: int
    borderTop: TableCellBorder
    columnSpan: int
    paddingRight: Dimension
    contentAlignment: typing_extensions.Literal[
        "CONTENT_ALIGNMENT_UNSPECIFIED",
        "CONTENT_ALIGNMENT_UNSUPPORTED",
        "TOP",
        "MIDDLE",
        "BOTTOM",
    ]
    borderRight: TableCellBorder
    backgroundColor: OptionalColor
    paddingTop: Dimension

class NamedStyle(typing_extensions.TypedDict, total=False):
    paragraphStyle: ParagraphStyle
    namedStyleType: typing_extensions.Literal[
        "NAMED_STYLE_TYPE_UNSPECIFIED",
        "NORMAL_TEXT",
        "TITLE",
        "SUBTITLE",
        "HEADING_1",
        "HEADING_2",
        "HEADING_3",
        "HEADING_4",
        "HEADING_5",
        "HEADING_6",
    ]
    textStyle: TextStyle

class ParagraphStyleSuggestionState(typing_extensions.TypedDict, total=False):
    indentFirstLineSuggested: bool
    borderBottomSuggested: bool
    indentStartSuggested: bool
    indentEndSuggested: bool
    borderTopSuggested: bool
    borderRightSuggested: bool
    borderBetweenSuggested: bool
    spaceAboveSuggested: bool
    headingIdSuggested: bool
    borderLeftSuggested: bool
    spacingModeSuggested: bool
    keepLinesTogetherSuggested: bool
    alignmentSuggested: bool
    spaceBelowSuggested: bool
    avoidWidowAndOrphanSuggested: bool
    shadingSuggestionState: ShadingSuggestionState
    keepWithNextSuggested: bool
    lineSpacingSuggested: bool
    namedStyleTypeSuggested: bool
    directionSuggested: bool

class UpdateTextStyleRequest(typing_extensions.TypedDict, total=False):
    textStyle: TextStyle
    fields: str
    range: Range

class LinkedContentReference(typing_extensions.TypedDict, total=False):
    sheetsChartReference: SheetsChartReference

class CreateHeaderResponse(typing_extensions.TypedDict, total=False):
    headerId: str

class UpdateTableCellStyleRequest(typing_extensions.TypedDict, total=False):
    tableStartLocation: Location
    tableRange: TableRange
    fields: str
    tableCellStyle: TableCellStyle

class NamedRanges(typing_extensions.TypedDict, total=False):
    namedRanges: typing.List[NamedRange]
    name: str

class Body(typing.Dict[str, typing.Any]): ...

class ReplaceNamedRangeContentRequest(typing_extensions.TypedDict, total=False):
    text: str
    namedRangeName: str
    namedRangeId: str

class WeightedFontFamily(typing_extensions.TypedDict, total=False):
    weight: int
    fontFamily: str

class PositionedObjectPositioning(typing_extensions.TypedDict, total=False):
    layout: typing_extensions.Literal[
        "POSITIONED_OBJECT_LAYOUT_UNSPECIFIED",
        "WRAP_TEXT",
        "BREAK_LEFT",
        "BREAK_RIGHT",
        "BREAK_LEFT_RIGHT",
        "IN_FRONT_OF_TEXT",
    ]
    leftOffset: Dimension
    topOffset: Dimension

class PositionedObject(typing_extensions.TypedDict, total=False):
    positionedObjectProperties: PositionedObjectProperties
    suggestedPositionedObjectPropertiesChanges: typing.Dict[str, typing.Any]
    suggestedDeletionIds: typing.List[str]
    objectId: str
    suggestedInsertionId: str

class EmbeddedObjectBorder(typing_extensions.TypedDict, total=False):
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"
    ]
    propertyState: typing_extensions.Literal["RENDERED", "NOT_RENDERED"]
    color: OptionalColor
    width: Dimension

class PositionedObjectProperties(typing_extensions.TypedDict, total=False):
    positioning: PositionedObjectPositioning
    embeddedObject: EmbeddedObject

class WriteControl(typing_extensions.TypedDict, total=False):
    requiredRevisionId: str
    targetRevisionId: str

class Location(typing_extensions.TypedDict, total=False):
    segmentId: str
    index: int

class Dimension(typing_extensions.TypedDict, total=False):
    magnitude: float
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "PT"]

class TableRowStyleSuggestionState(typing_extensions.TypedDict, total=False):
    minRowHeightSuggested: bool

class ImagePropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    cropPropertiesSuggestionState: CropPropertiesSuggestionState
    contentUriSuggested: bool
    brightnessSuggested: bool
    sourceUriSuggested: bool
    contrastSuggested: bool
    transparencySuggested: bool
    angleSuggested: bool

class SheetsChartReferenceSuggestionState(typing_extensions.TypedDict, total=False):
    chartIdSuggested: bool
    spreadsheetIdSuggested: bool

class SuggestedTextStyle(typing_extensions.TypedDict, total=False):
    textStyleSuggestionState: TextStyleSuggestionState
    textStyle: TextStyle

class TableRange(typing_extensions.TypedDict, total=False):
    tableCellLocation: TableCellLocation
    rowSpan: int
    columnSpan: int

class CreateNamedRangeRequest(typing_extensions.TypedDict, total=False):
    range: Range
    name: str

class InsertInlineSheetsChartResponse(typing_extensions.TypedDict, total=False):
    objectId: str

class TableCell(typing.Dict[str, typing.Any]): ...

class DeleteContentRangeRequest(typing_extensions.TypedDict, total=False):
    range: Range

class Footnote(typing_extensions.TypedDict, total=False):
    footnoteId: str
    content: typing.List[StructuralElement]

class ReplaceAllTextResponse(typing_extensions.TypedDict, total=False):
    occurrencesChanged: int

class CreateNamedRangeResponse(typing_extensions.TypedDict, total=False):
    namedRangeId: str

class BulletSuggestionState(typing_extensions.TypedDict, total=False):
    nestingLevelSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState
    listIdSuggested: bool

class Table(typing_extensions.TypedDict, total=False):
    suggestedInsertionIds: typing.List[str]
    suggestedDeletionIds: typing.List[str]
    rows: int
    tableStyle: TableStyle
    columns: int
    tableRows: typing.List[TableRow]

class StructuralElement(typing.Dict[str, typing.Any]): ...

class LinkedContentReferenceSuggestionState(typing_extensions.TypedDict, total=False):
    sheetsChartReferenceSuggestionState: SheetsChartReferenceSuggestionState

class DeleteParagraphBulletsRequest(typing_extensions.TypedDict, total=False):
    range: Range

class UnmergeTableCellsRequest(typing_extensions.TypedDict, total=False):
    tableRange: TableRange

class BatchUpdateDocumentResponse(typing_extensions.TypedDict, total=False):
    writeControl: WriteControl
    replies: typing.List[Response]
    documentId: str

class Size(typing_extensions.TypedDict, total=False):
    width: Dimension
    height: Dimension
