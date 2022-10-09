import typing

import typing_extensions

_list = list

@typing.type_check_only
class AutoText(typing_extensions.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PAGE_NUMBER", "PAGE_COUNT"]

@typing.type_check_only
class Background(typing_extensions.TypedDict, total=False):
    color: OptionalColor

@typing.type_check_only
class BackgroundSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundColorSuggested: bool

@typing.type_check_only
class BatchUpdateDocumentRequest(typing_extensions.TypedDict, total=False):
    requests: _list[Request]
    writeControl: WriteControl

@typing.type_check_only
class BatchUpdateDocumentResponse(typing_extensions.TypedDict, total=False):
    documentId: str
    replies: _list[Response]
    writeControl: WriteControl

@typing.type_check_only
class Body(typing_extensions.TypedDict, total=False):
    content: _list[StructuralElement]

@typing.type_check_only
class Bullet(typing_extensions.TypedDict, total=False):
    listId: str
    nestingLevel: int
    textStyle: TextStyle

@typing.type_check_only
class BulletSuggestionState(typing_extensions.TypedDict, total=False):
    listIdSuggested: bool
    nestingLevelSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    rgbColor: RgbColor

@typing.type_check_only
class ColumnBreak(typing_extensions.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class CreateFooterRequest(typing_extensions.TypedDict, total=False):
    sectionBreakLocation: Location
    type: typing_extensions.Literal["HEADER_FOOTER_TYPE_UNSPECIFIED", "DEFAULT"]

@typing.type_check_only
class CreateFooterResponse(typing_extensions.TypedDict, total=False):
    footerId: str

@typing.type_check_only
class CreateFootnoteRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location

@typing.type_check_only
class CreateFootnoteResponse(typing_extensions.TypedDict, total=False):
    footnoteId: str

@typing.type_check_only
class CreateHeaderRequest(typing_extensions.TypedDict, total=False):
    sectionBreakLocation: Location
    type: typing_extensions.Literal["HEADER_FOOTER_TYPE_UNSPECIFIED", "DEFAULT"]

@typing.type_check_only
class CreateHeaderResponse(typing_extensions.TypedDict, total=False):
    headerId: str

@typing.type_check_only
class CreateNamedRangeRequest(typing_extensions.TypedDict, total=False):
    name: str
    range: Range

@typing.type_check_only
class CreateNamedRangeResponse(typing_extensions.TypedDict, total=False):
    namedRangeId: str

@typing.type_check_only
class CreateParagraphBulletsRequest(typing_extensions.TypedDict, total=False):
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
    range: Range

@typing.type_check_only
class CropProperties(typing_extensions.TypedDict, total=False):
    angle: float
    offsetBottom: float
    offsetLeft: float
    offsetRight: float
    offsetTop: float

@typing.type_check_only
class CropPropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    angleSuggested: bool
    offsetBottomSuggested: bool
    offsetLeftSuggested: bool
    offsetRightSuggested: bool
    offsetTopSuggested: bool

@typing.type_check_only
class DeleteContentRangeRequest(typing_extensions.TypedDict, total=False):
    range: Range

@typing.type_check_only
class DeleteFooterRequest(typing_extensions.TypedDict, total=False):
    footerId: str

@typing.type_check_only
class DeleteHeaderRequest(typing_extensions.TypedDict, total=False):
    headerId: str

@typing.type_check_only
class DeleteNamedRangeRequest(typing_extensions.TypedDict, total=False):
    name: str
    namedRangeId: str

@typing.type_check_only
class DeleteParagraphBulletsRequest(typing_extensions.TypedDict, total=False):
    range: Range

@typing.type_check_only
class DeletePositionedObjectRequest(typing_extensions.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class DeleteTableColumnRequest(typing_extensions.TypedDict, total=False):
    tableCellLocation: TableCellLocation

@typing.type_check_only
class DeleteTableRowRequest(typing_extensions.TypedDict, total=False):
    tableCellLocation: TableCellLocation

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    magnitude: float
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "PT"]

@typing.type_check_only
class Document(typing_extensions.TypedDict, total=False):
    body: Body
    documentId: str
    documentStyle: DocumentStyle
    footers: dict[str, typing.Any]
    footnotes: dict[str, typing.Any]
    headers: dict[str, typing.Any]
    inlineObjects: dict[str, typing.Any]
    lists: dict[str, typing.Any]
    namedRanges: dict[str, typing.Any]
    namedStyles: NamedStyles
    positionedObjects: dict[str, typing.Any]
    revisionId: str
    suggestedDocumentStyleChanges: dict[str, typing.Any]
    suggestedNamedStylesChanges: dict[str, typing.Any]
    suggestionsViewMode: typing_extensions.Literal[
        "DEFAULT_FOR_CURRENT_ACCESS",
        "SUGGESTIONS_INLINE",
        "PREVIEW_SUGGESTIONS_ACCEPTED",
        "PREVIEW_WITHOUT_SUGGESTIONS",
    ]
    title: str

@typing.type_check_only
class DocumentStyle(typing_extensions.TypedDict, total=False):
    background: Background
    defaultFooterId: str
    defaultHeaderId: str
    evenPageFooterId: str
    evenPageHeaderId: str
    firstPageFooterId: str
    firstPageHeaderId: str
    marginBottom: Dimension
    marginFooter: Dimension
    marginHeader: Dimension
    marginLeft: Dimension
    marginRight: Dimension
    marginTop: Dimension
    pageNumberStart: int
    pageSize: Size
    useCustomHeaderFooterMargins: bool
    useEvenPageHeaderFooter: bool
    useFirstPageHeaderFooter: bool

@typing.type_check_only
class DocumentStyleSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundSuggestionState: BackgroundSuggestionState
    defaultFooterIdSuggested: bool
    defaultHeaderIdSuggested: bool
    evenPageFooterIdSuggested: bool
    evenPageHeaderIdSuggested: bool
    firstPageFooterIdSuggested: bool
    firstPageHeaderIdSuggested: bool
    marginBottomSuggested: bool
    marginFooterSuggested: bool
    marginHeaderSuggested: bool
    marginLeftSuggested: bool
    marginRightSuggested: bool
    marginTopSuggested: bool
    pageNumberStartSuggested: bool
    pageSizeSuggestionState: SizeSuggestionState
    useCustomHeaderFooterMarginsSuggested: bool
    useEvenPageHeaderFooterSuggested: bool
    useFirstPageHeaderFooterSuggested: bool

@typing.type_check_only
class EmbeddedDrawingProperties(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EmbeddedDrawingPropertiesSuggestionState(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class EmbeddedObject(typing_extensions.TypedDict, total=False):
    description: str
    embeddedDrawingProperties: EmbeddedDrawingProperties
    embeddedObjectBorder: EmbeddedObjectBorder
    imageProperties: ImageProperties
    linkedContentReference: LinkedContentReference
    marginBottom: Dimension
    marginLeft: Dimension
    marginRight: Dimension
    marginTop: Dimension
    size: Size
    title: str

@typing.type_check_only
class EmbeddedObjectBorder(typing_extensions.TypedDict, total=False):
    color: OptionalColor
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"
    ]
    propertyState: typing_extensions.Literal["RENDERED", "NOT_RENDERED"]
    width: Dimension

@typing.type_check_only
class EmbeddedObjectBorderSuggestionState(typing_extensions.TypedDict, total=False):
    colorSuggested: bool
    dashStyleSuggested: bool
    propertyStateSuggested: bool
    widthSuggested: bool

@typing.type_check_only
class EmbeddedObjectSuggestionState(typing_extensions.TypedDict, total=False):
    descriptionSuggested: bool
    embeddedDrawingPropertiesSuggestionState: EmbeddedDrawingPropertiesSuggestionState
    embeddedObjectBorderSuggestionState: EmbeddedObjectBorderSuggestionState
    imagePropertiesSuggestionState: ImagePropertiesSuggestionState
    linkedContentReferenceSuggestionState: LinkedContentReferenceSuggestionState
    marginBottomSuggested: bool
    marginLeftSuggested: bool
    marginRightSuggested: bool
    marginTopSuggested: bool
    sizeSuggestionState: SizeSuggestionState
    titleSuggested: bool

@typing.type_check_only
class EndOfSegmentLocation(typing_extensions.TypedDict, total=False):
    segmentId: str

@typing.type_check_only
class Equation(typing_extensions.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]

@typing.type_check_only
class Footer(typing_extensions.TypedDict, total=False):
    content: _list[StructuralElement]
    footerId: str

@typing.type_check_only
class Footnote(typing_extensions.TypedDict, total=False):
    content: _list[StructuralElement]
    footnoteId: str

@typing.type_check_only
class FootnoteReference(typing_extensions.TypedDict, total=False):
    footnoteId: str
    footnoteNumber: str
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class Header(typing_extensions.TypedDict, total=False):
    content: _list[StructuralElement]
    headerId: str

@typing.type_check_only
class HorizontalRule(typing_extensions.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class ImageProperties(typing_extensions.TypedDict, total=False):
    angle: float
    brightness: float
    contentUri: str
    contrast: float
    cropProperties: CropProperties
    sourceUri: str
    transparency: float

@typing.type_check_only
class ImagePropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    angleSuggested: bool
    brightnessSuggested: bool
    contentUriSuggested: bool
    contrastSuggested: bool
    cropPropertiesSuggestionState: CropPropertiesSuggestionState
    sourceUriSuggested: bool
    transparencySuggested: bool

@typing.type_check_only
class InlineObject(typing_extensions.TypedDict, total=False):
    inlineObjectProperties: InlineObjectProperties
    objectId: str
    suggestedDeletionIds: _list[str]
    suggestedInlineObjectPropertiesChanges: dict[str, typing.Any]
    suggestedInsertionId: str

@typing.type_check_only
class InlineObjectElement(typing_extensions.TypedDict, total=False):
    inlineObjectId: str
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class InlineObjectProperties(typing_extensions.TypedDict, total=False):
    embeddedObject: EmbeddedObject

@typing.type_check_only
class InlineObjectPropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    embeddedObjectSuggestionState: EmbeddedObjectSuggestionState

@typing.type_check_only
class InsertInlineImageRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    objectSize: Size
    uri: str

@typing.type_check_only
class InsertInlineImageResponse(typing_extensions.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class InsertInlineSheetsChartResponse(typing_extensions.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class InsertPageBreakRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location

@typing.type_check_only
class InsertSectionBreakRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "CONTINUOUS", "NEXT_PAGE"
    ]

@typing.type_check_only
class InsertTableColumnRequest(typing_extensions.TypedDict, total=False):
    insertRight: bool
    tableCellLocation: TableCellLocation

@typing.type_check_only
class InsertTableRequest(typing_extensions.TypedDict, total=False):
    columns: int
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    rows: int

@typing.type_check_only
class InsertTableRowRequest(typing_extensions.TypedDict, total=False):
    insertBelow: bool
    tableCellLocation: TableCellLocation

@typing.type_check_only
class InsertTextRequest(typing_extensions.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    text: str

@typing.type_check_only
class Link(typing_extensions.TypedDict, total=False):
    bookmarkId: str
    headingId: str
    url: str

@typing.type_check_only
class LinkedContentReference(typing_extensions.TypedDict, total=False):
    sheetsChartReference: SheetsChartReference

@typing.type_check_only
class LinkedContentReferenceSuggestionState(typing_extensions.TypedDict, total=False):
    sheetsChartReferenceSuggestionState: SheetsChartReferenceSuggestionState

@typing.type_check_only
class List(typing_extensions.TypedDict, total=False):
    listProperties: ListProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionId: str
    suggestedListPropertiesChanges: dict[str, typing.Any]

@typing.type_check_only
class ListProperties(typing_extensions.TypedDict, total=False):
    nestingLevels: _list[NestingLevel]

@typing.type_check_only
class ListPropertiesSuggestionState(typing_extensions.TypedDict, total=False):
    nestingLevelsSuggestionStates: _list[NestingLevelSuggestionState]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    index: int
    segmentId: str

@typing.type_check_only
class MergeTableCellsRequest(typing_extensions.TypedDict, total=False):
    tableRange: TableRange

@typing.type_check_only
class NamedRange(typing_extensions.TypedDict, total=False):
    name: str
    namedRangeId: str
    ranges: _list[Range]

@typing.type_check_only
class NamedRanges(typing_extensions.TypedDict, total=False):
    name: str
    namedRanges: _list[NamedRange]

@typing.type_check_only
class NamedStyle(typing_extensions.TypedDict, total=False):
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
    paragraphStyle: ParagraphStyle
    textStyle: TextStyle

@typing.type_check_only
class NamedStyleSuggestionState(typing_extensions.TypedDict, total=False):
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
    textStyleSuggestionState: TextStyleSuggestionState

@typing.type_check_only
class NamedStyles(typing_extensions.TypedDict, total=False):
    styles: _list[NamedStyle]

@typing.type_check_only
class NamedStylesSuggestionState(typing_extensions.TypedDict, total=False):
    stylesSuggestionStates: _list[NamedStyleSuggestionState]

@typing.type_check_only
class NestingLevel(typing_extensions.TypedDict, total=False):
    bulletAlignment: typing_extensions.Literal[
        "BULLET_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    glyphFormat: str
    glyphSymbol: str
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
    indentFirstLine: Dimension
    indentStart: Dimension
    startNumber: int
    textStyle: TextStyle

@typing.type_check_only
class NestingLevelSuggestionState(typing_extensions.TypedDict, total=False):
    bulletAlignmentSuggested: bool
    glyphFormatSuggested: bool
    glyphSymbolSuggested: bool
    glyphTypeSuggested: bool
    indentFirstLineSuggested: bool
    indentStartSuggested: bool
    startNumberSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState

@typing.type_check_only
class ObjectReferences(typing_extensions.TypedDict, total=False):
    objectIds: _list[str]

@typing.type_check_only
class OptionalColor(typing_extensions.TypedDict, total=False):
    color: Color

@typing.type_check_only
class PageBreak(typing_extensions.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class Paragraph(typing_extensions.TypedDict, total=False):
    bullet: Bullet
    elements: _list[ParagraphElement]
    paragraphStyle: ParagraphStyle
    positionedObjectIds: _list[str]
    suggestedBulletChanges: dict[str, typing.Any]
    suggestedParagraphStyleChanges: dict[str, typing.Any]
    suggestedPositionedObjectIds: dict[str, typing.Any]

@typing.type_check_only
class ParagraphBorder(typing_extensions.TypedDict, total=False):
    color: OptionalColor
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"
    ]
    padding: Dimension
    width: Dimension

@typing.type_check_only
class ParagraphElement(typing_extensions.TypedDict, total=False):
    autoText: AutoText
    columnBreak: ColumnBreak
    endIndex: int
    equation: Equation
    footnoteReference: FootnoteReference
    horizontalRule: HorizontalRule
    inlineObjectElement: InlineObjectElement
    pageBreak: PageBreak
    person: Person
    richLink: RichLink
    startIndex: int
    textRun: TextRun

@typing.type_check_only
class ParagraphStyle(typing_extensions.TypedDict, total=False):
    alignment: typing_extensions.Literal[
        "ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END", "JUSTIFIED"
    ]
    avoidWidowAndOrphan: bool
    borderBetween: ParagraphBorder
    borderBottom: ParagraphBorder
    borderLeft: ParagraphBorder
    borderRight: ParagraphBorder
    borderTop: ParagraphBorder
    direction: typing_extensions.Literal[
        "CONTENT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    headingId: str
    indentEnd: Dimension
    indentFirstLine: Dimension
    indentStart: Dimension
    keepLinesTogether: bool
    keepWithNext: bool
    lineSpacing: float
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
    pageBreakBefore: bool
    shading: Shading
    spaceAbove: Dimension
    spaceBelow: Dimension
    spacingMode: typing_extensions.Literal[
        "SPACING_MODE_UNSPECIFIED", "NEVER_COLLAPSE", "COLLAPSE_LISTS"
    ]
    tabStops: _list[TabStop]

@typing.type_check_only
class ParagraphStyleSuggestionState(typing_extensions.TypedDict, total=False):
    alignmentSuggested: bool
    avoidWidowAndOrphanSuggested: bool
    borderBetweenSuggested: bool
    borderBottomSuggested: bool
    borderLeftSuggested: bool
    borderRightSuggested: bool
    borderTopSuggested: bool
    directionSuggested: bool
    headingIdSuggested: bool
    indentEndSuggested: bool
    indentFirstLineSuggested: bool
    indentStartSuggested: bool
    keepLinesTogetherSuggested: bool
    keepWithNextSuggested: bool
    lineSpacingSuggested: bool
    namedStyleTypeSuggested: bool
    pageBreakBeforeSuggested: bool
    shadingSuggestionState: ShadingSuggestionState
    spaceAboveSuggested: bool
    spaceBelowSuggested: bool
    spacingModeSuggested: bool

@typing.type_check_only
class Person(typing_extensions.TypedDict, total=False):
    personId: str
    personProperties: PersonProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class PersonProperties(typing_extensions.TypedDict, total=False):
    email: str
    name: str

@typing.type_check_only
class PinTableHeaderRowsRequest(typing_extensions.TypedDict, total=False):
    pinnedHeaderRowsCount: int
    tableStartLocation: Location

@typing.type_check_only
class PositionedObject(typing_extensions.TypedDict, total=False):
    objectId: str
    positionedObjectProperties: PositionedObjectProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionId: str
    suggestedPositionedObjectPropertiesChanges: dict[str, typing.Any]

@typing.type_check_only
class PositionedObjectPositioning(typing_extensions.TypedDict, total=False):
    layout: typing_extensions.Literal[
        "POSITIONED_OBJECT_LAYOUT_UNSPECIFIED",
        "WRAP_TEXT",
        "BREAK_LEFT",
        "BREAK_RIGHT",
        "BREAK_LEFT_RIGHT",
        "IN_FRONT_OF_TEXT",
        "BEHIND_TEXT",
    ]
    leftOffset: Dimension
    topOffset: Dimension

@typing.type_check_only
class PositionedObjectPositioningSuggestionState(
    typing_extensions.TypedDict, total=False
):
    layoutSuggested: bool
    leftOffsetSuggested: bool
    topOffsetSuggested: bool

@typing.type_check_only
class PositionedObjectProperties(typing_extensions.TypedDict, total=False):
    embeddedObject: EmbeddedObject
    positioning: PositionedObjectPositioning

@typing.type_check_only
class PositionedObjectPropertiesSuggestionState(
    typing_extensions.TypedDict, total=False
):
    embeddedObjectSuggestionState: EmbeddedObjectSuggestionState
    positioningSuggestionState: PositionedObjectPositioningSuggestionState

@typing.type_check_only
class Range(typing_extensions.TypedDict, total=False):
    endIndex: int
    segmentId: str
    startIndex: int

@typing.type_check_only
class ReplaceAllTextRequest(typing_extensions.TypedDict, total=False):
    containsText: SubstringMatchCriteria
    replaceText: str

@typing.type_check_only
class ReplaceAllTextResponse(typing_extensions.TypedDict, total=False):
    occurrencesChanged: int

@typing.type_check_only
class ReplaceImageRequest(typing_extensions.TypedDict, total=False):
    imageObjectId: str
    imageReplaceMethod: typing_extensions.Literal[
        "IMAGE_REPLACE_METHOD_UNSPECIFIED", "CENTER_CROP"
    ]
    uri: str

@typing.type_check_only
class ReplaceNamedRangeContentRequest(typing_extensions.TypedDict, total=False):
    namedRangeId: str
    namedRangeName: str
    text: str

@typing.type_check_only
class Request(typing_extensions.TypedDict, total=False):
    createFooter: CreateFooterRequest
    createFootnote: CreateFootnoteRequest
    createHeader: CreateHeaderRequest
    createNamedRange: CreateNamedRangeRequest
    createParagraphBullets: CreateParagraphBulletsRequest
    deleteContentRange: DeleteContentRangeRequest
    deleteFooter: DeleteFooterRequest
    deleteHeader: DeleteHeaderRequest
    deleteNamedRange: DeleteNamedRangeRequest
    deleteParagraphBullets: DeleteParagraphBulletsRequest
    deletePositionedObject: DeletePositionedObjectRequest
    deleteTableColumn: DeleteTableColumnRequest
    deleteTableRow: DeleteTableRowRequest
    insertInlineImage: InsertInlineImageRequest
    insertPageBreak: InsertPageBreakRequest
    insertSectionBreak: InsertSectionBreakRequest
    insertTable: InsertTableRequest
    insertTableColumn: InsertTableColumnRequest
    insertTableRow: InsertTableRowRequest
    insertText: InsertTextRequest
    mergeTableCells: MergeTableCellsRequest
    pinTableHeaderRows: PinTableHeaderRowsRequest
    replaceAllText: ReplaceAllTextRequest
    replaceImage: ReplaceImageRequest
    replaceNamedRangeContent: ReplaceNamedRangeContentRequest
    unmergeTableCells: UnmergeTableCellsRequest
    updateDocumentStyle: UpdateDocumentStyleRequest
    updateParagraphStyle: UpdateParagraphStyleRequest
    updateSectionStyle: UpdateSectionStyleRequest
    updateTableCellStyle: UpdateTableCellStyleRequest
    updateTableColumnProperties: UpdateTableColumnPropertiesRequest
    updateTableRowStyle: UpdateTableRowStyleRequest
    updateTextStyle: UpdateTextStyleRequest

@typing.type_check_only
class Response(typing_extensions.TypedDict, total=False):
    createFooter: CreateFooterResponse
    createFootnote: CreateFootnoteResponse
    createHeader: CreateHeaderResponse
    createNamedRange: CreateNamedRangeResponse
    insertInlineImage: InsertInlineImageResponse
    insertInlineSheetsChart: InsertInlineSheetsChartResponse
    replaceAllText: ReplaceAllTextResponse

@typing.type_check_only
class RgbColor(typing_extensions.TypedDict, total=False):
    blue: float
    green: float
    red: float

@typing.type_check_only
class RichLink(typing_extensions.TypedDict, total=False):
    richLinkId: str
    richLinkProperties: RichLinkProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class RichLinkProperties(typing_extensions.TypedDict, total=False):
    mimeType: str
    title: str
    uri: str

@typing.type_check_only
class SectionBreak(typing_extensions.TypedDict, total=False):
    sectionStyle: SectionStyle
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]

@typing.type_check_only
class SectionColumnProperties(typing_extensions.TypedDict, total=False):
    paddingEnd: Dimension
    width: Dimension

@typing.type_check_only
class SectionStyle(typing_extensions.TypedDict, total=False):
    columnProperties: _list[SectionColumnProperties]
    columnSeparatorStyle: typing_extensions.Literal[
        "COLUMN_SEPARATOR_STYLE_UNSPECIFIED", "NONE", "BETWEEN_EACH_COLUMN"
    ]
    contentDirection: typing_extensions.Literal[
        "CONTENT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    defaultFooterId: str
    defaultHeaderId: str
    evenPageFooterId: str
    evenPageHeaderId: str
    firstPageFooterId: str
    firstPageHeaderId: str
    marginBottom: Dimension
    marginFooter: Dimension
    marginHeader: Dimension
    marginLeft: Dimension
    marginRight: Dimension
    marginTop: Dimension
    pageNumberStart: int
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "CONTINUOUS", "NEXT_PAGE"
    ]
    useFirstPageHeaderFooter: bool

@typing.type_check_only
class Shading(typing_extensions.TypedDict, total=False):
    backgroundColor: OptionalColor

@typing.type_check_only
class ShadingSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundColorSuggested: bool

@typing.type_check_only
class SheetsChartReference(typing_extensions.TypedDict, total=False):
    chartId: int
    spreadsheetId: str

@typing.type_check_only
class SheetsChartReferenceSuggestionState(typing_extensions.TypedDict, total=False):
    chartIdSuggested: bool
    spreadsheetIdSuggested: bool

@typing.type_check_only
class Size(typing_extensions.TypedDict, total=False):
    height: Dimension
    width: Dimension

@typing.type_check_only
class SizeSuggestionState(typing_extensions.TypedDict, total=False):
    heightSuggested: bool
    widthSuggested: bool

@typing.type_check_only
class StructuralElement(dict[str, typing.Any]): ...

@typing.type_check_only
class SubstringMatchCriteria(typing_extensions.TypedDict, total=False):
    matchCase: bool
    text: str

@typing.type_check_only
class SuggestedBullet(typing_extensions.TypedDict, total=False):
    bullet: Bullet
    bulletSuggestionState: BulletSuggestionState

@typing.type_check_only
class SuggestedDocumentStyle(typing_extensions.TypedDict, total=False):
    documentStyle: DocumentStyle
    documentStyleSuggestionState: DocumentStyleSuggestionState

@typing.type_check_only
class SuggestedInlineObjectProperties(typing_extensions.TypedDict, total=False):
    inlineObjectProperties: InlineObjectProperties
    inlineObjectPropertiesSuggestionState: InlineObjectPropertiesSuggestionState

@typing.type_check_only
class SuggestedListProperties(typing_extensions.TypedDict, total=False):
    listProperties: ListProperties
    listPropertiesSuggestionState: ListPropertiesSuggestionState

@typing.type_check_only
class SuggestedNamedStyles(typing_extensions.TypedDict, total=False):
    namedStyles: NamedStyles
    namedStylesSuggestionState: NamedStylesSuggestionState

@typing.type_check_only
class SuggestedParagraphStyle(typing_extensions.TypedDict, total=False):
    paragraphStyle: ParagraphStyle
    paragraphStyleSuggestionState: ParagraphStyleSuggestionState

@typing.type_check_only
class SuggestedPositionedObjectProperties(typing_extensions.TypedDict, total=False):
    positionedObjectProperties: PositionedObjectProperties
    positionedObjectPropertiesSuggestionState: PositionedObjectPropertiesSuggestionState

@typing.type_check_only
class SuggestedTableCellStyle(typing_extensions.TypedDict, total=False):
    tableCellStyle: TableCellStyle
    tableCellStyleSuggestionState: TableCellStyleSuggestionState

@typing.type_check_only
class SuggestedTableRowStyle(typing_extensions.TypedDict, total=False):
    tableRowStyle: TableRowStyle
    tableRowStyleSuggestionState: TableRowStyleSuggestionState

@typing.type_check_only
class SuggestedTextStyle(typing_extensions.TypedDict, total=False):
    textStyle: TextStyle
    textStyleSuggestionState: TextStyleSuggestionState

@typing.type_check_only
class TabStop(typing_extensions.TypedDict, total=False):
    alignment: typing_extensions.Literal[
        "TAB_STOP_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    offset: Dimension

@typing.type_check_only
class Table(dict[str, typing.Any]): ...

@typing.type_check_only
class TableCell(typing_extensions.TypedDict, total=False):
    content: _list[StructuralElement]
    endIndex: int
    startIndex: int
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTableCellStyleChanges: dict[str, typing.Any]
    tableCellStyle: TableCellStyle

@typing.type_check_only
class TableCellBorder(typing_extensions.TypedDict, total=False):
    color: OptionalColor
    dashStyle: typing_extensions.Literal[
        "DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"
    ]
    width: Dimension

@typing.type_check_only
class TableCellLocation(typing_extensions.TypedDict, total=False):
    columnIndex: int
    rowIndex: int
    tableStartLocation: Location

@typing.type_check_only
class TableCellStyle(typing_extensions.TypedDict, total=False):
    backgroundColor: OptionalColor
    borderBottom: TableCellBorder
    borderLeft: TableCellBorder
    borderRight: TableCellBorder
    borderTop: TableCellBorder
    columnSpan: int
    contentAlignment: typing_extensions.Literal[
        "CONTENT_ALIGNMENT_UNSPECIFIED",
        "CONTENT_ALIGNMENT_UNSUPPORTED",
        "TOP",
        "MIDDLE",
        "BOTTOM",
    ]
    paddingBottom: Dimension
    paddingLeft: Dimension
    paddingRight: Dimension
    paddingTop: Dimension
    rowSpan: int

@typing.type_check_only
class TableCellStyleSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundColorSuggested: bool
    borderBottomSuggested: bool
    borderLeftSuggested: bool
    borderRightSuggested: bool
    borderTopSuggested: bool
    columnSpanSuggested: bool
    contentAlignmentSuggested: bool
    paddingBottomSuggested: bool
    paddingLeftSuggested: bool
    paddingRightSuggested: bool
    paddingTopSuggested: bool
    rowSpanSuggested: bool

@typing.type_check_only
class TableColumnProperties(typing_extensions.TypedDict, total=False):
    width: Dimension
    widthType: typing_extensions.Literal[
        "WIDTH_TYPE_UNSPECIFIED", "EVENLY_DISTRIBUTED", "FIXED_WIDTH"
    ]

@typing.type_check_only
class TableOfContents(dict[str, typing.Any]): ...

@typing.type_check_only
class TableRange(typing_extensions.TypedDict, total=False):
    columnSpan: int
    rowSpan: int
    tableCellLocation: TableCellLocation

@typing.type_check_only
class TableRow(dict[str, typing.Any]): ...

@typing.type_check_only
class TableRowStyle(typing_extensions.TypedDict, total=False):
    minRowHeight: Dimension
    preventOverflow: bool
    tableHeader: bool

@typing.type_check_only
class TableRowStyleSuggestionState(typing_extensions.TypedDict, total=False):
    minRowHeightSuggested: bool

@typing.type_check_only
class TableStyle(typing_extensions.TypedDict, total=False):
    tableColumnProperties: _list[TableColumnProperties]

@typing.type_check_only
class TextRun(typing_extensions.TypedDict, total=False):
    content: str
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class TextStyle(typing_extensions.TypedDict, total=False):
    backgroundColor: OptionalColor
    baselineOffset: typing_extensions.Literal[
        "BASELINE_OFFSET_UNSPECIFIED", "NONE", "SUPERSCRIPT", "SUBSCRIPT"
    ]
    bold: bool
    fontSize: Dimension
    foregroundColor: OptionalColor
    italic: bool
    link: Link
    smallCaps: bool
    strikethrough: bool
    underline: bool
    weightedFontFamily: WeightedFontFamily

@typing.type_check_only
class TextStyleSuggestionState(typing_extensions.TypedDict, total=False):
    backgroundColorSuggested: bool
    baselineOffsetSuggested: bool
    boldSuggested: bool
    fontSizeSuggested: bool
    foregroundColorSuggested: bool
    italicSuggested: bool
    linkSuggested: bool
    smallCapsSuggested: bool
    strikethroughSuggested: bool
    underlineSuggested: bool
    weightedFontFamilySuggested: bool

@typing.type_check_only
class UnmergeTableCellsRequest(typing_extensions.TypedDict, total=False):
    tableRange: TableRange

@typing.type_check_only
class UpdateDocumentStyleRequest(typing_extensions.TypedDict, total=False):
    documentStyle: DocumentStyle
    fields: str

@typing.type_check_only
class UpdateParagraphStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    paragraphStyle: ParagraphStyle
    range: Range

@typing.type_check_only
class UpdateSectionStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    range: Range
    sectionStyle: SectionStyle

@typing.type_check_only
class UpdateTableCellStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    tableCellStyle: TableCellStyle
    tableRange: TableRange
    tableStartLocation: Location

@typing.type_check_only
class UpdateTableColumnPropertiesRequest(typing_extensions.TypedDict, total=False):
    columnIndices: _list[int]
    fields: str
    tableColumnProperties: TableColumnProperties
    tableStartLocation: Location

@typing.type_check_only
class UpdateTableRowStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    rowIndices: _list[int]
    tableRowStyle: TableRowStyle
    tableStartLocation: Location

@typing.type_check_only
class UpdateTextStyleRequest(typing_extensions.TypedDict, total=False):
    fields: str
    range: Range
    textStyle: TextStyle

@typing.type_check_only
class WeightedFontFamily(typing_extensions.TypedDict, total=False):
    fontFamily: str
    weight: int

@typing.type_check_only
class WriteControl(typing_extensions.TypedDict, total=False):
    requiredRevisionId: str
    targetRevisionId: str
