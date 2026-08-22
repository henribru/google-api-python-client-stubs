import typing

_list = list

@typing.type_check_only
class AddDocumentTabRequest(typing.TypedDict, total=False):
    tabProperties: TabProperties

@typing.type_check_only
class AddDocumentTabResponse(typing.TypedDict, total=False):
    tabProperties: TabProperties

@typing.type_check_only
class AutoText(typing.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle
    type: typing.Literal["TYPE_UNSPECIFIED", "PAGE_NUMBER", "PAGE_COUNT"]

@typing.type_check_only
class Background(typing.TypedDict, total=False):
    color: OptionalColor

@typing.type_check_only
class BackgroundSuggestionState(typing.TypedDict, total=False):
    backgroundColorSuggested: bool

@typing.type_check_only
class BatchUpdateDocumentRequest(typing.TypedDict, total=False):
    requests: _list[Request]
    writeControl: WriteControl

@typing.type_check_only
class BatchUpdateDocumentResponse(typing.TypedDict, total=False):
    documentId: str
    replies: _list[Response]
    writeControl: WriteControl

@typing.type_check_only
class Body(typing.TypedDict, total=False):
    content: _list[StructuralElement]

@typing.type_check_only
class BookmarkLink(typing.TypedDict, total=False):
    id: str
    tabId: str

@typing.type_check_only
class Bullet(typing.TypedDict, total=False):
    listId: str
    nestingLevel: int
    textStyle: TextStyle

@typing.type_check_only
class BulletSuggestionState(typing.TypedDict, total=False):
    listIdSuggested: bool
    nestingLevelSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState

@typing.type_check_only
class Color(typing.TypedDict, total=False):
    rgbColor: RgbColor

@typing.type_check_only
class ColumnBreak(typing.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class CreateFooterRequest(typing.TypedDict, total=False):
    sectionBreakLocation: Location
    type: typing.Literal["HEADER_FOOTER_TYPE_UNSPECIFIED", "DEFAULT"]

@typing.type_check_only
class CreateFooterResponse(typing.TypedDict, total=False):
    footerId: str

@typing.type_check_only
class CreateFootnoteRequest(typing.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location

@typing.type_check_only
class CreateFootnoteResponse(typing.TypedDict, total=False):
    footnoteId: str

@typing.type_check_only
class CreateHeaderRequest(typing.TypedDict, total=False):
    sectionBreakLocation: Location
    type: typing.Literal["HEADER_FOOTER_TYPE_UNSPECIFIED", "DEFAULT"]

@typing.type_check_only
class CreateHeaderResponse(typing.TypedDict, total=False):
    headerId: str

@typing.type_check_only
class CreateNamedRangeRequest(typing.TypedDict, total=False):
    name: str
    range: Range

@typing.type_check_only
class CreateNamedRangeResponse(typing.TypedDict, total=False):
    namedRangeId: str

@typing.type_check_only
class CreateParagraphBulletsRequest(typing.TypedDict, total=False):
    bulletPreset: typing.Literal[
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
class CropProperties(typing.TypedDict, total=False):
    angle: float
    offsetBottom: float
    offsetLeft: float
    offsetRight: float
    offsetTop: float

@typing.type_check_only
class CropPropertiesSuggestionState(typing.TypedDict, total=False):
    angleSuggested: bool
    offsetBottomSuggested: bool
    offsetLeftSuggested: bool
    offsetRightSuggested: bool
    offsetTopSuggested: bool

@typing.type_check_only
class DateElement(typing.TypedDict, total=False):
    dateElementProperties: DateElementProperties
    dateId: str
    suggestedDateElementPropertiesChanges: dict[str, typing.Any]
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class DateElementProperties(typing.TypedDict, total=False):
    dateFormat: typing.Literal[
        "DATE_FORMAT_UNSPECIFIED",
        "DATE_FORMAT_CUSTOM",
        "DATE_FORMAT_MONTH_DAY_ABBREVIATED",
        "DATE_FORMAT_MONTH_DAY_FULL",
        "DATE_FORMAT_MONTH_DAY_YEAR_ABBREVIATED",
        "DATE_FORMAT_ISO8601",
    ]
    displayText: str
    locale: str
    timeFormat: typing.Literal[
        "TIME_FORMAT_UNSPECIFIED",
        "TIME_FORMAT_DISABLED",
        "TIME_FORMAT_HOUR_MINUTE",
        "TIME_FORMAT_HOUR_MINUTE_TIMEZONE",
    ]
    timeZoneId: str
    timestamp: str

@typing.type_check_only
class DateElementPropertiesSuggestionState(typing.TypedDict, total=False):
    dateFormatSuggested: bool
    localeSuggested: bool
    timeFormatSuggested: bool
    timeZoneIdSuggested: bool
    timestampSuggested: bool

@typing.type_check_only
class DeleteContentRangeRequest(typing.TypedDict, total=False):
    range: Range

@typing.type_check_only
class DeleteFooterRequest(typing.TypedDict, total=False):
    footerId: str
    tabId: str

@typing.type_check_only
class DeleteHeaderRequest(typing.TypedDict, total=False):
    headerId: str
    tabId: str

@typing.type_check_only
class DeleteNamedRangeRequest(typing.TypedDict, total=False):
    name: str
    namedRangeId: str
    tabsCriteria: TabsCriteria

@typing.type_check_only
class DeleteParagraphBulletsRequest(typing.TypedDict, total=False):
    range: Range

@typing.type_check_only
class DeletePositionedObjectRequest(typing.TypedDict, total=False):
    objectId: str
    tabId: str

@typing.type_check_only
class DeleteTabRequest(typing.TypedDict, total=False):
    tabId: str

@typing.type_check_only
class DeleteTableColumnRequest(typing.TypedDict, total=False):
    tableCellLocation: TableCellLocation

@typing.type_check_only
class DeleteTableRowRequest(typing.TypedDict, total=False):
    tableCellLocation: TableCellLocation

@typing.type_check_only
class Dimension(typing.TypedDict, total=False):
    magnitude: float
    unit: typing.Literal["UNIT_UNSPECIFIED", "PT"]

@typing.type_check_only
class Document(typing.TypedDict, total=False):
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
    suggestionsViewMode: typing.Literal[
        "DEFAULT_FOR_CURRENT_ACCESS",
        "SUGGESTIONS_INLINE",
        "PREVIEW_SUGGESTIONS_ACCEPTED",
        "PREVIEW_WITHOUT_SUGGESTIONS",
    ]
    tabs: _list[Tab]
    title: str

@typing.type_check_only
class DocumentFormat(typing.TypedDict, total=False):
    documentMode: typing.Literal["DOCUMENT_MODE_UNSPECIFIED", "PAGES", "PAGELESS"]

@typing.type_check_only
class DocumentStyle(typing.TypedDict, total=False):
    background: Background
    defaultFooterId: str
    defaultHeaderId: str
    documentFormat: DocumentFormat
    evenPageFooterId: str
    evenPageHeaderId: str
    firstPageFooterId: str
    firstPageHeaderId: str
    flipPageOrientation: bool
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
class DocumentStyleSuggestionState(typing.TypedDict, total=False):
    backgroundSuggestionState: BackgroundSuggestionState
    defaultFooterIdSuggested: bool
    defaultHeaderIdSuggested: bool
    evenPageFooterIdSuggested: bool
    evenPageHeaderIdSuggested: bool
    firstPageFooterIdSuggested: bool
    firstPageHeaderIdSuggested: bool
    flipPageOrientationSuggested: bool
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
class DocumentTab(typing.TypedDict, total=False):
    body: Body
    documentStyle: DocumentStyle
    footers: dict[str, typing.Any]
    footnotes: dict[str, typing.Any]
    headers: dict[str, typing.Any]
    inlineObjects: dict[str, typing.Any]
    lists: dict[str, typing.Any]
    namedRanges: dict[str, typing.Any]
    namedStyles: NamedStyles
    positionedObjects: dict[str, typing.Any]
    suggestedDocumentStyleChanges: dict[str, typing.Any]
    suggestedNamedStylesChanges: dict[str, typing.Any]

@typing.type_check_only
class EmbeddedDrawingProperties(typing.TypedDict, total=False): ...

@typing.type_check_only
class EmbeddedDrawingPropertiesSuggestionState(typing.TypedDict, total=False): ...

@typing.type_check_only
class EmbeddedObject(typing.TypedDict, total=False):
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
class EmbeddedObjectBorder(typing.TypedDict, total=False):
    color: OptionalColor
    dashStyle: typing.Literal["DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"]
    propertyState: typing.Literal["RENDERED", "NOT_RENDERED"]
    width: Dimension

@typing.type_check_only
class EmbeddedObjectBorderSuggestionState(typing.TypedDict, total=False):
    colorSuggested: bool
    dashStyleSuggested: bool
    propertyStateSuggested: bool
    widthSuggested: bool

@typing.type_check_only
class EmbeddedObjectSuggestionState(typing.TypedDict, total=False):
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
class EndOfSegmentLocation(typing.TypedDict, total=False):
    segmentId: str
    tabId: str

@typing.type_check_only
class Equation(typing.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]

@typing.type_check_only
class Footer(typing.TypedDict, total=False):
    content: _list[StructuralElement]
    footerId: str

@typing.type_check_only
class Footnote(typing.TypedDict, total=False):
    content: _list[StructuralElement]
    footnoteId: str

@typing.type_check_only
class FootnoteReference(typing.TypedDict, total=False):
    footnoteId: str
    footnoteNumber: str
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class Header(typing.TypedDict, total=False):
    content: _list[StructuralElement]
    headerId: str

@typing.type_check_only
class HeadingLink(typing.TypedDict, total=False):
    id: str
    tabId: str

@typing.type_check_only
class HorizontalRule(typing.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class ImageProperties(typing.TypedDict, total=False):
    angle: float
    brightness: float
    contentUri: str
    contrast: float
    cropProperties: CropProperties
    sourceUri: str
    transparency: float

@typing.type_check_only
class ImagePropertiesSuggestionState(typing.TypedDict, total=False):
    angleSuggested: bool
    brightnessSuggested: bool
    contentUriSuggested: bool
    contrastSuggested: bool
    cropPropertiesSuggestionState: CropPropertiesSuggestionState
    sourceUriSuggested: bool
    transparencySuggested: bool

@typing.type_check_only
class InlineObject(typing.TypedDict, total=False):
    inlineObjectProperties: InlineObjectProperties
    objectId: str
    suggestedDeletionIds: _list[str]
    suggestedInlineObjectPropertiesChanges: dict[str, typing.Any]
    suggestedInsertionId: str

@typing.type_check_only
class InlineObjectElement(typing.TypedDict, total=False):
    inlineObjectId: str
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class InlineObjectProperties(typing.TypedDict, total=False):
    embeddedObject: EmbeddedObject

@typing.type_check_only
class InlineObjectPropertiesSuggestionState(typing.TypedDict, total=False):
    embeddedObjectSuggestionState: EmbeddedObjectSuggestionState

@typing.type_check_only
class InsertDateRequest(typing.TypedDict, total=False):
    dateElementProperties: DateElementProperties
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location

@typing.type_check_only
class InsertInlineImageRequest(typing.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    objectSize: Size
    uri: str

@typing.type_check_only
class InsertInlineImageResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class InsertInlineSheetsChartResponse(typing.TypedDict, total=False):
    objectId: str

@typing.type_check_only
class InsertPageBreakRequest(typing.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location

@typing.type_check_only
class InsertPersonRequest(typing.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    personProperties: PersonProperties

@typing.type_check_only
class InsertRichLinkRequest(typing.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    richLinkProperties: RichLinkProperties

@typing.type_check_only
class InsertSectionBreakRequest(typing.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    sectionType: typing.Literal["SECTION_TYPE_UNSPECIFIED", "CONTINUOUS", "NEXT_PAGE"]

@typing.type_check_only
class InsertTableColumnRequest(typing.TypedDict, total=False):
    insertRight: bool
    tableCellLocation: TableCellLocation

@typing.type_check_only
class InsertTableRequest(typing.TypedDict, total=False):
    columns: int
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    rows: int

@typing.type_check_only
class InsertTableRowRequest(typing.TypedDict, total=False):
    insertBelow: bool
    tableCellLocation: TableCellLocation

@typing.type_check_only
class InsertTextRequest(typing.TypedDict, total=False):
    endOfSegmentLocation: EndOfSegmentLocation
    location: Location
    text: str

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    bookmark: BookmarkLink
    bookmarkId: str
    heading: HeadingLink
    headingId: str
    tabId: str
    url: str

@typing.type_check_only
class LinkedContentReference(typing.TypedDict, total=False):
    sheetsChartReference: SheetsChartReference

@typing.type_check_only
class LinkedContentReferenceSuggestionState(typing.TypedDict, total=False):
    sheetsChartReferenceSuggestionState: SheetsChartReferenceSuggestionState

@typing.type_check_only
class List(typing.TypedDict, total=False):
    listProperties: ListProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionId: str
    suggestedListPropertiesChanges: dict[str, typing.Any]

@typing.type_check_only
class ListProperties(typing.TypedDict, total=False):
    nestingLevels: _list[NestingLevel]

@typing.type_check_only
class ListPropertiesSuggestionState(typing.TypedDict, total=False):
    nestingLevelsSuggestionStates: _list[NestingLevelSuggestionState]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    index: int
    segmentId: str
    tabId: str

@typing.type_check_only
class MergeTableCellsRequest(typing.TypedDict, total=False):
    tableRange: TableRange

@typing.type_check_only
class NamedRange(typing.TypedDict, total=False):
    name: str
    namedRangeId: str
    ranges: _list[Range]

@typing.type_check_only
class NamedRanges(typing.TypedDict, total=False):
    name: str
    namedRanges: _list[NamedRange]

@typing.type_check_only
class NamedStyle(typing.TypedDict, total=False):
    namedStyleType: typing.Literal[
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
class NamedStyleSuggestionState(typing.TypedDict, total=False):
    namedStyleType: typing.Literal[
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
class NamedStyles(typing.TypedDict, total=False):
    styles: _list[NamedStyle]

@typing.type_check_only
class NamedStylesSuggestionState(typing.TypedDict, total=False):
    stylesSuggestionStates: _list[NamedStyleSuggestionState]

@typing.type_check_only
class NestingLevel(typing.TypedDict, total=False):
    bulletAlignment: typing.Literal[
        "BULLET_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    glyphFormat: str
    glyphSymbol: str
    glyphType: typing.Literal[
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
class NestingLevelSuggestionState(typing.TypedDict, total=False):
    bulletAlignmentSuggested: bool
    glyphFormatSuggested: bool
    glyphSymbolSuggested: bool
    glyphTypeSuggested: bool
    indentFirstLineSuggested: bool
    indentStartSuggested: bool
    startNumberSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState

@typing.type_check_only
class ObjectReferences(typing.TypedDict, total=False):
    objectIds: _list[str]

@typing.type_check_only
class OptionalColor(typing.TypedDict, total=False):
    color: Color

@typing.type_check_only
class PageBreak(typing.TypedDict, total=False):
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class Paragraph(typing.TypedDict, total=False):
    bullet: Bullet
    elements: _list[ParagraphElement]
    paragraphStyle: ParagraphStyle
    positionedObjectIds: _list[str]
    suggestedBulletChanges: dict[str, typing.Any]
    suggestedParagraphStyleChanges: dict[str, typing.Any]
    suggestedPositionedObjectIds: dict[str, typing.Any]

@typing.type_check_only
class ParagraphBorder(typing.TypedDict, total=False):
    color: OptionalColor
    dashStyle: typing.Literal["DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"]
    padding: Dimension
    width: Dimension

@typing.type_check_only
class ParagraphElement(typing.TypedDict, total=False):
    autoText: AutoText
    columnBreak: ColumnBreak
    dateElement: DateElement
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
class ParagraphStyle(typing.TypedDict, total=False):
    alignment: typing.Literal[
        "ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END", "JUSTIFIED"
    ]
    avoidWidowAndOrphan: bool
    borderBetween: ParagraphBorder
    borderBottom: ParagraphBorder
    borderLeft: ParagraphBorder
    borderRight: ParagraphBorder
    borderTop: ParagraphBorder
    direction: typing.Literal[
        "CONTENT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    headingId: str
    indentEnd: Dimension
    indentFirstLine: Dimension
    indentStart: Dimension
    keepLinesTogether: bool
    keepWithNext: bool
    lineSpacing: float
    namedStyleType: typing.Literal[
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
    spacingMode: typing.Literal[
        "SPACING_MODE_UNSPECIFIED", "NEVER_COLLAPSE", "COLLAPSE_LISTS"
    ]
    tabStops: _list[TabStop]

@typing.type_check_only
class ParagraphStyleSuggestionState(typing.TypedDict, total=False):
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
class Person(typing.TypedDict, total=False):
    personId: str
    personProperties: PersonProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class PersonProperties(typing.TypedDict, total=False):
    email: str
    name: str

@typing.type_check_only
class PinTableHeaderRowsRequest(typing.TypedDict, total=False):
    pinnedHeaderRowsCount: int
    tableStartLocation: Location

@typing.type_check_only
class PositionedObject(typing.TypedDict, total=False):
    objectId: str
    positionedObjectProperties: PositionedObjectProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionId: str
    suggestedPositionedObjectPropertiesChanges: dict[str, typing.Any]

@typing.type_check_only
class PositionedObjectPositioning(typing.TypedDict, total=False):
    layout: typing.Literal[
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
class PositionedObjectPositioningSuggestionState(typing.TypedDict, total=False):
    layoutSuggested: bool
    leftOffsetSuggested: bool
    topOffsetSuggested: bool

@typing.type_check_only
class PositionedObjectProperties(typing.TypedDict, total=False):
    embeddedObject: EmbeddedObject
    positioning: PositionedObjectPositioning

@typing.type_check_only
class PositionedObjectPropertiesSuggestionState(typing.TypedDict, total=False):
    embeddedObjectSuggestionState: EmbeddedObjectSuggestionState
    positioningSuggestionState: PositionedObjectPositioningSuggestionState

@typing.type_check_only
class Range(typing.TypedDict, total=False):
    endIndex: int
    segmentId: str
    startIndex: int
    tabId: str

@typing.type_check_only
class ReplaceAllTextRequest(typing.TypedDict, total=False):
    containsText: SubstringMatchCriteria
    replaceText: str
    tabsCriteria: TabsCriteria

@typing.type_check_only
class ReplaceAllTextResponse(typing.TypedDict, total=False):
    occurrencesChanged: int

@typing.type_check_only
class ReplaceImageRequest(typing.TypedDict, total=False):
    imageObjectId: str
    imageReplaceMethod: typing.Literal[
        "IMAGE_REPLACE_METHOD_UNSPECIFIED", "CENTER_CROP"
    ]
    tabId: str
    uri: str

@typing.type_check_only
class ReplaceNamedRangeContentRequest(typing.TypedDict, total=False):
    namedRangeId: str
    namedRangeName: str
    tabsCriteria: TabsCriteria
    text: str

@typing.type_check_only
class Request(typing.TypedDict, total=False):
    addDocumentTab: AddDocumentTabRequest
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
    deleteTab: DeleteTabRequest
    deleteTableColumn: DeleteTableColumnRequest
    deleteTableRow: DeleteTableRowRequest
    insertDate: InsertDateRequest
    insertInlineImage: InsertInlineImageRequest
    insertPageBreak: InsertPageBreakRequest
    insertPerson: InsertPersonRequest
    insertRichLink: InsertRichLinkRequest
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
    updateDocumentTabProperties: UpdateDocumentTabPropertiesRequest
    updateNamedStyle: UpdateNamedStyleRequest
    updateParagraphStyle: UpdateParagraphStyleRequest
    updateSectionStyle: UpdateSectionStyleRequest
    updateTableCellStyle: UpdateTableCellStyleRequest
    updateTableColumnProperties: UpdateTableColumnPropertiesRequest
    updateTableRowStyle: UpdateTableRowStyleRequest
    updateTextStyle: UpdateTextStyleRequest

@typing.type_check_only
class Response(typing.TypedDict, total=False):
    addDocumentTab: AddDocumentTabResponse
    createFooter: CreateFooterResponse
    createFootnote: CreateFootnoteResponse
    createHeader: CreateHeaderResponse
    createNamedRange: CreateNamedRangeResponse
    insertInlineImage: InsertInlineImageResponse
    insertInlineSheetsChart: InsertInlineSheetsChartResponse
    replaceAllText: ReplaceAllTextResponse

@typing.type_check_only
class RgbColor(typing.TypedDict, total=False):
    blue: float
    green: float
    red: float

@typing.type_check_only
class RichLink(typing.TypedDict, total=False):
    richLinkId: str
    richLinkProperties: RichLinkProperties
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class RichLinkProperties(typing.TypedDict, total=False):
    mimeType: str
    title: str
    uri: str

@typing.type_check_only
class SectionBreak(typing.TypedDict, total=False):
    sectionStyle: SectionStyle
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]

@typing.type_check_only
class SectionColumnProperties(typing.TypedDict, total=False):
    paddingEnd: Dimension
    width: Dimension

@typing.type_check_only
class SectionStyle(typing.TypedDict, total=False):
    columnProperties: _list[SectionColumnProperties]
    columnSeparatorStyle: typing.Literal[
        "COLUMN_SEPARATOR_STYLE_UNSPECIFIED", "NONE", "BETWEEN_EACH_COLUMN"
    ]
    contentDirection: typing.Literal[
        "CONTENT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"
    ]
    defaultFooterId: str
    defaultHeaderId: str
    evenPageFooterId: str
    evenPageHeaderId: str
    firstPageFooterId: str
    firstPageHeaderId: str
    flipPageOrientation: bool
    marginBottom: Dimension
    marginFooter: Dimension
    marginHeader: Dimension
    marginLeft: Dimension
    marginRight: Dimension
    marginTop: Dimension
    pageNumberStart: int
    sectionType: typing.Literal["SECTION_TYPE_UNSPECIFIED", "CONTINUOUS", "NEXT_PAGE"]
    useFirstPageHeaderFooter: bool

@typing.type_check_only
class Shading(typing.TypedDict, total=False):
    backgroundColor: OptionalColor

@typing.type_check_only
class ShadingSuggestionState(typing.TypedDict, total=False):
    backgroundColorSuggested: bool

@typing.type_check_only
class SheetsChartReference(typing.TypedDict, total=False):
    chartId: int
    spreadsheetId: str

@typing.type_check_only
class SheetsChartReferenceSuggestionState(typing.TypedDict, total=False):
    chartIdSuggested: bool
    spreadsheetIdSuggested: bool

@typing.type_check_only
class Size(typing.TypedDict, total=False):
    height: Dimension
    width: Dimension

@typing.type_check_only
class SizeSuggestionState(typing.TypedDict, total=False):
    heightSuggested: bool
    widthSuggested: bool

@typing.type_check_only
class StructuralElement(typing.TypedDict, total=False):
    endIndex: int
    paragraph: Paragraph
    sectionBreak: SectionBreak
    startIndex: int
    table: Table
    tableOfContents: TableOfContents

@typing.type_check_only
class SubstringMatchCriteria(typing.TypedDict, total=False):
    matchCase: bool
    searchByRegex: bool
    text: str

@typing.type_check_only
class SuggestedBullet(typing.TypedDict, total=False):
    bullet: Bullet
    bulletSuggestionState: BulletSuggestionState

@typing.type_check_only
class SuggestedDateElementProperties(typing.TypedDict, total=False):
    dateElementProperties: DateElementProperties
    dateElementPropertiesSuggestionState: DateElementPropertiesSuggestionState

@typing.type_check_only
class SuggestedDocumentStyle(typing.TypedDict, total=False):
    documentStyle: DocumentStyle
    documentStyleSuggestionState: DocumentStyleSuggestionState

@typing.type_check_only
class SuggestedInlineObjectProperties(typing.TypedDict, total=False):
    inlineObjectProperties: InlineObjectProperties
    inlineObjectPropertiesSuggestionState: InlineObjectPropertiesSuggestionState

@typing.type_check_only
class SuggestedListProperties(typing.TypedDict, total=False):
    listProperties: ListProperties
    listPropertiesSuggestionState: ListPropertiesSuggestionState

@typing.type_check_only
class SuggestedNamedStyles(typing.TypedDict, total=False):
    namedStyles: NamedStyles
    namedStylesSuggestionState: NamedStylesSuggestionState

@typing.type_check_only
class SuggestedParagraphStyle(typing.TypedDict, total=False):
    paragraphStyle: ParagraphStyle
    paragraphStyleSuggestionState: ParagraphStyleSuggestionState

@typing.type_check_only
class SuggestedPositionedObjectProperties(typing.TypedDict, total=False):
    positionedObjectProperties: PositionedObjectProperties
    positionedObjectPropertiesSuggestionState: PositionedObjectPropertiesSuggestionState

@typing.type_check_only
class SuggestedTableCellStyle(typing.TypedDict, total=False):
    tableCellStyle: TableCellStyle
    tableCellStyleSuggestionState: TableCellStyleSuggestionState

@typing.type_check_only
class SuggestedTableRowStyle(typing.TypedDict, total=False):
    tableRowStyle: TableRowStyle
    tableRowStyleSuggestionState: TableRowStyleSuggestionState

@typing.type_check_only
class SuggestedTextStyle(typing.TypedDict, total=False):
    textStyle: TextStyle
    textStyleSuggestionState: TextStyleSuggestionState

@typing.type_check_only
class Tab(typing.TypedDict, total=False):
    childTabs: _list[Tab]
    documentTab: DocumentTab
    tabProperties: TabProperties

@typing.type_check_only
class TabProperties(typing.TypedDict, total=False):
    iconEmoji: str
    index: int
    nestingLevel: int
    parentTabId: str
    tabId: str
    title: str

@typing.type_check_only
class TabStop(typing.TypedDict, total=False):
    alignment: typing.Literal[
        "TAB_STOP_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    offset: Dimension

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    columns: int
    rows: int
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    tableRows: _list[TableRow]
    tableStyle: TableStyle

@typing.type_check_only
class TableCell(typing.TypedDict, total=False):
    content: _list[StructuralElement]
    endIndex: int
    startIndex: int
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTableCellStyleChanges: dict[str, typing.Any]
    tableCellStyle: TableCellStyle

@typing.type_check_only
class TableCellBorder(typing.TypedDict, total=False):
    color: OptionalColor
    dashStyle: typing.Literal["DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"]
    width: Dimension

@typing.type_check_only
class TableCellLocation(typing.TypedDict, total=False):
    columnIndex: int
    rowIndex: int
    tableStartLocation: Location

@typing.type_check_only
class TableCellStyle(typing.TypedDict, total=False):
    backgroundColor: OptionalColor
    borderBottom: TableCellBorder
    borderLeft: TableCellBorder
    borderRight: TableCellBorder
    borderTop: TableCellBorder
    columnSpan: int
    contentAlignment: typing.Literal[
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
class TableCellStyleSuggestionState(typing.TypedDict, total=False):
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
class TableColumnProperties(typing.TypedDict, total=False):
    width: Dimension
    widthType: typing.Literal[
        "WIDTH_TYPE_UNSPECIFIED", "EVENLY_DISTRIBUTED", "FIXED_WIDTH"
    ]

@typing.type_check_only
class TableOfContents(typing.TypedDict, total=False):
    content: _list[StructuralElement]
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]

@typing.type_check_only
class TableRange(typing.TypedDict, total=False):
    columnSpan: int
    rowSpan: int
    tableCellLocation: TableCellLocation

@typing.type_check_only
class TableRow(typing.TypedDict, total=False):
    endIndex: int
    startIndex: int
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTableRowStyleChanges: dict[str, typing.Any]
    tableCells: _list[TableCell]
    tableRowStyle: TableRowStyle

@typing.type_check_only
class TableRowStyle(typing.TypedDict, total=False):
    minRowHeight: Dimension
    preventOverflow: bool
    tableHeader: bool

@typing.type_check_only
class TableRowStyleSuggestionState(typing.TypedDict, total=False):
    minRowHeightSuggested: bool

@typing.type_check_only
class TableStyle(typing.TypedDict, total=False):
    tableColumnProperties: _list[TableColumnProperties]

@typing.type_check_only
class TabsCriteria(typing.TypedDict, total=False):
    tabIds: _list[str]

@typing.type_check_only
class TextRun(typing.TypedDict, total=False):
    content: str
    suggestedDeletionIds: _list[str]
    suggestedInsertionIds: _list[str]
    suggestedTextStyleChanges: dict[str, typing.Any]
    textStyle: TextStyle

@typing.type_check_only
class TextStyle(typing.TypedDict, total=False):
    backgroundColor: OptionalColor
    baselineOffset: typing.Literal[
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
class TextStyleSuggestionState(typing.TypedDict, total=False):
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
class UnmergeTableCellsRequest(typing.TypedDict, total=False):
    tableRange: TableRange

@typing.type_check_only
class UpdateDocumentStyleRequest(typing.TypedDict, total=False):
    documentStyle: DocumentStyle
    fields: str
    tabId: str

@typing.type_check_only
class UpdateDocumentTabPropertiesRequest(typing.TypedDict, total=False):
    fields: str
    tabProperties: TabProperties

@typing.type_check_only
class UpdateNamedStyleRequest(typing.TypedDict, total=False):
    fields: str
    namedStyle: NamedStyle
    tabId: str

@typing.type_check_only
class UpdateParagraphStyleRequest(typing.TypedDict, total=False):
    fields: str
    paragraphStyle: ParagraphStyle
    range: Range

@typing.type_check_only
class UpdateSectionStyleRequest(typing.TypedDict, total=False):
    fields: str
    range: Range
    sectionStyle: SectionStyle

@typing.type_check_only
class UpdateTableCellStyleRequest(typing.TypedDict, total=False):
    fields: str
    tableCellStyle: TableCellStyle
    tableRange: TableRange
    tableStartLocation: Location

@typing.type_check_only
class UpdateTableColumnPropertiesRequest(typing.TypedDict, total=False):
    columnIndices: _list[int]
    fields: str
    tableColumnProperties: TableColumnProperties
    tableStartLocation: Location

@typing.type_check_only
class UpdateTableRowStyleRequest(typing.TypedDict, total=False):
    fields: str
    rowIndices: _list[int]
    tableRowStyle: TableRowStyle
    tableStartLocation: Location

@typing.type_check_only
class UpdateTextStyleRequest(typing.TypedDict, total=False):
    fields: str
    range: Range
    textStyle: TextStyle

@typing.type_check_only
class WeightedFontFamily(typing.TypedDict, total=False):
    fontFamily: str
    weight: int

@typing.type_check_only
class WriteControl(typing.TypedDict, total=False):
    requiredRevisionId: str
    targetRevisionId: str
