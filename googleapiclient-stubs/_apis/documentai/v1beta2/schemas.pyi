import typing

import typing_extensions

class GoogleCloudDocumentaiV1beta1BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: typing.List[GoogleCloudDocumentaiV1beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudDocumentaiV1beta1Vertex]

class GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    layoutType: typing_extensions.Literal[
        "LAYOUT_TYPE_UNSPECIFIED",
        "BLOCK",
        "PARAGRAPH",
        "LINE",
        "TOKEN",
        "VISUAL_ELEMENT",
        "TABLE",
        "FORM_FIELD",
    ]
    boundingPoly: GoogleCloudDocumentaiV1beta2BoundingPoly
    layoutId: str
    page: str

class GoogleCloudDocumentaiV1beta1DocumentStyleFontSize(
    typing_extensions.TypedDict, total=False
):
    size: float
    unit: str

class GoogleCloudDocumentaiV1beta2DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    revision: int
    id: int

class GoogleCloudDocumentaiV1beta2DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef]

class GoogleCloudDocumentaiV1beta2NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

class GoogleCloudDocumentaiV1beta1DocumentTranslation(
    typing_extensions.TypedDict, total=False
):
    translatedText: str
    provenance: typing.List[GoogleCloudDocumentaiV1beta1DocumentProvenance]
    languageCode: str
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor

class GoogleCloudDocumentaiV1beta2DocumentEntity(typing.Dict[str, typing.Any]): ...

class GoogleCloudDocumentaiV1beta2GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDocumentaiV1beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    stateMessage: str
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACCEPTED",
        "WAITING",
        "RUNNING",
        "SUCCEEDED",
        "CANCELLED",
        "FAILED",
    ]
    createTime: str

class GoogleCloudDocumentaiV1beta1DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    id: int
    revision: int

class GoogleCloudDocumentaiV1beta3ReviewDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: str

class GoogleCloudDocumentaiV1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDocumentaiV1beta2OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    stateMessage: str
    updateTime: str
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACCEPTED",
        "WAITING",
        "RUNNING",
        "SUCCEEDED",
        "CANCELLED",
        "FAILED",
    ]

class GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

class GoogleCloudDocumentaiV1beta1DocumentPageImage(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    content: str
    height: int
    width: int

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudDocumentaiV1beta2BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: typing.List[GoogleCloudDocumentaiV1beta2Vertex]
    normalizedVertices: typing.List[GoogleCloudDocumentaiV1beta2NormalizedVertex]

class GoogleCloudDocumentaiV1beta1DocumentPageVisualElement(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    type: str

class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    version: str
    id: str

class GoogleCloudDocumentaiV1beta2DocumentPage(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    paragraphs: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageParagraph]
    lines: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageLine]
    transforms: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageMatrix]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    tables: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTable]
    blocks: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageBlock]
    image: GoogleCloudDocumentaiV1beta2DocumentPageImage
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    dimension: GoogleCloudDocumentaiV1beta2DocumentPageDimension
    visualElements: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageVisualElement]
    formFields: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageFormField]
    tokens: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageToken]

class GoogleCloudDocumentaiV1beta2GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus(
    typing_extensions.TypedDict, total=False
):
    humanReviewOperation: str
    status: GoogleRpcStatus
    inputGcsSource: str
    outputGcsDestination: str

class GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegment(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    startIndex: str

class GoogleCloudDocumentaiUiv1beta3EnableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDocumentaiV1beta2DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
    ]
    revision: int
    parents: typing.List[GoogleCloudDocumentaiV1beta2DocumentProvenanceParent]
    id: int

class GoogleCloudDocumentaiV1beta1DocumentStyle(
    typing_extensions.TypedDict, total=False
):
    textStyle: str
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor
    fontSize: GoogleCloudDocumentaiV1beta1DocumentStyleFontSize
    color: GoogleTypeColor
    fontWeight: str
    textDecoration: str
    backgroundColor: GoogleTypeColor

class GoogleCloudDocumentaiV1beta2KeyValuePairHint(
    typing_extensions.TypedDict, total=False
):
    valueTypes: typing.List[str]
    key: str

class GoogleCloudDocumentaiV1beta1DocumentTextAnchor(
    typing_extensions.TypedDict, total=False
):
    content: str
    textSegments: typing.List[GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment]

class GoogleCloudDocumentaiV1beta1DocumentPageBlock(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]

class GoogleCloudDocumentaiV1beta2ProcessDocumentRequest(
    typing_extensions.TypedDict, total=False
):
    automlParams: GoogleCloudDocumentaiV1beta2AutoMlParams
    parent: str
    outputConfig: GoogleCloudDocumentaiV1beta2OutputConfig
    inputConfig: GoogleCloudDocumentaiV1beta2InputConfig
    entityExtractionParams: GoogleCloudDocumentaiV1beta2EntityExtractionParams
    ocrParams: GoogleCloudDocumentaiV1beta2OcrParams
    tableExtractionParams: GoogleCloudDocumentaiV1beta2TableExtractionParams
    formExtractionParams: GoogleCloudDocumentaiV1beta2FormExtractionParams
    documentType: str

class GoogleCloudDocumentaiV1beta2DocumentPageVisualElement(
    typing_extensions.TypedDict, total=False
):
    type: str
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]

class GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment(
    typing_extensions.TypedDict, total=False
):
    startIndex: str
    endIndex: str

class GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    stateMessage: str
    createTime: str
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]

class GoogleTypeDateTime(typing_extensions.TypedDict, total=False):
    timeZone: GoogleTypeTimeZone
    nanos: int
    month: int
    minutes: int
    day: int
    utcOffset: str
    year: int
    hours: int
    seconds: int

class GoogleCloudDocumentaiV1beta1Document(typing_extensions.TypedDict, total=False):
    entityRelations: typing.List[GoogleCloudDocumentaiV1beta1DocumentEntityRelation]
    mimeType: str
    entities: typing.List[GoogleCloudDocumentaiV1beta1DocumentEntity]
    translations: typing.List[GoogleCloudDocumentaiV1beta1DocumentTranslation]
    shardInfo: GoogleCloudDocumentaiV1beta1DocumentShardInfo
    uri: str
    textChanges: typing.List[GoogleCloudDocumentaiV1beta1DocumentTextChange]
    revisions: typing.List[GoogleCloudDocumentaiV1beta1DocumentRevision]
    error: GoogleRpcStatus
    textStyles: typing.List[GoogleCloudDocumentaiV1beta1DocumentStyle]
    pages: typing.List[GoogleCloudDocumentaiV1beta1DocumentPage]
    text: str
    content: str

class GoogleCloudDocumentaiV1beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    y: float
    x: float

class GoogleCloudDocumentaiV1beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

class GoogleCloudDocumentaiV1beta1DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    bodyRows: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]
    headerRows: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]

class GoogleCloudDocumentaiV1beta1DocumentPageMatrix(
    typing_extensions.TypedDict, total=False
):
    rows: int
    type: int
    data: str
    cols: int

class GoogleCloudDocumentaiV1beta2ProcessDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudDocumentaiV1beta2InputConfig
    outputConfig: GoogleCloudDocumentaiV1beta2OutputConfig

class GoogleCloudDocumentaiV1beta1DocumentPageLayout(
    typing_extensions.TypedDict, total=False
):
    orientation: typing_extensions.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    boundingPoly: GoogleCloudDocumentaiV1beta1BoundingPoly
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor
    confidence: float

class GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

class GoogleCloudDocumentaiV1beta1DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    agent: str
    parent: typing.List[int]
    humanReview: GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReview
    createTime: str
    processor: str
    id: str

class GoogleCloudDocumentaiV1beta2DocumentEntityRelation(
    typing_extensions.TypedDict, total=False
):
    objectId: str
    relation: str
    subjectId: str

class GoogleCloudDocumentaiV1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudDocumentaiV1beta1OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDocumentaiV1beta1GcsDestination
    pagesPerShard: int

class GoogleCloudDocumentaiV1beta2DocumentLabel(
    typing_extensions.TypedDict, total=False
):
    automlModel: str
    confidence: float
    name: str

class GoogleCloudDocumentaiV1beta1DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
    ]
    id: int
    parents: typing.List[GoogleCloudDocumentaiV1beta1DocumentProvenanceParent]
    revision: int

class GoogleCloudDocumentaiV1beta2DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    parent: typing.List[int]
    agent: str
    processor: str
    id: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReview

class GoogleCloudDocumentaiV1beta2DocumentTranslation(
    typing_extensions.TypedDict, total=False
):
    translatedText: str
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor
    provenance: typing.List[GoogleCloudDocumentaiV1beta2DocumentProvenance]
    languageCode: str

class GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    createTime: str
    stateMessage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]

class GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReview(
    typing_extensions.TypedDict, total=False
):
    stateMessage: str
    state: str

class GoogleCloudDocumentaiV1beta2DocumentTextAnchor(
    typing_extensions.TypedDict, total=False
):
    textSegments: typing.List[GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegment]
    content: str

class GoogleCloudDocumentaiV1beta1DocumentPageLine(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

class GoogleCloudDocumentaiUiv1beta3DisableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDocumentaiV1beta2DocumentPageLayout(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta2BoundingPoly
    orientation: typing_extensions.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor
    confidence: float

class GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    stateMessage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "WAITING",
        "RUNNING",
        "SUCCEEDED",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
    ]
    updateTime: str
    createTime: str

class GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudDocumentaiV1beta2ProcessDocumentResponse]

class GoogleCloudDocumentaiV1beta2DocumentPageLine(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]

class GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str
    stateMessage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]

class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    nanos: int
    units: str
    currencyCode: str

class GoogleCloudDocumentaiV1beta1DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef]

class GoogleCloudDocumentaiV1beta2DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    detectedBreak: GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

class GoogleCloudDocumentaiV1beta1DocumentPageParagraph(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]

class GoogleCloudDocumentaiV1beta2TableExtractionParams(
    typing_extensions.TypedDict, total=False
):
    enabled: bool
    headerHints: typing.List[str]
    tableBoundHints: typing.List[GoogleCloudDocumentaiV1beta2TableBoundHint]
    modelVersion: str

class GoogleCloudDocumentaiV1beta2DocumentPageImage(
    typing_extensions.TypedDict, total=False
):
    content: str
    height: int
    width: int
    mimeType: str

class GoogleCloudDocumentaiV1beta2DocumentStyle(
    typing_extensions.TypedDict, total=False
):
    backgroundColor: GoogleTypeColor
    textStyle: str
    fontSize: GoogleCloudDocumentaiV1beta2DocumentStyleFontSize
    color: GoogleTypeColor
    textDecoration: str
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor

class GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudDocumentaiV1beta1ProcessDocumentResponse]

class GoogleCloudDocumentaiUiv1beta3CreateProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "PREPARING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    updateTime: str
    createTime: str

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class GoogleCloudDocumentaiV1beta2DocumentShardInfo(
    typing_extensions.TypedDict, total=False
):
    shardIndex: str
    textOffset: str
    shardCount: str

class GoogleCloudDocumentaiV1beta2FormExtractionParams(
    typing_extensions.TypedDict, total=False
):
    modelVersion: str
    enabled: bool
    keyValuePairHints: typing.List[GoogleCloudDocumentaiV1beta2KeyValuePairHint]

class GoogleCloudDocumentaiV1beta1DocumentPageFormField(
    typing_extensions.TypedDict, total=False
):
    fieldValue: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    valueType: str
    fieldName: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    nameDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    valueDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]

class GoogleTypePostalAddress(typing_extensions.TypedDict, total=False):
    recipients: typing.List[str]
    revision: int
    sublocality: str
    locality: str
    regionCode: str
    addressLines: typing.List[str]
    sortingCode: str
    administrativeArea: str
    organization: str
    postalCode: str
    languageCode: str

class GoogleTypeColor(typing_extensions.TypedDict, total=False):
    blue: float
    green: float
    alpha: float
    red: float

class GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    createTime: str
    updateTime: str

class GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    moneyValue: GoogleTypeMoney
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    addressValue: GoogleTypePostalAddress
    text: str

class GoogleCloudDocumentaiV1beta2DocumentPageParagraph(
    typing_extensions.TypedDict, total=False
):
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]

class GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "WAITING",
        "RUNNING",
        "SUCCEEDED",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
    ]
    createTime: str
    stateMessage: str

class GoogleCloudDocumentaiV1beta2DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    bodyRows: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    headerRows: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]

class GoogleCloudDocumentaiV1beta2Document(typing_extensions.TypedDict, total=False):
    content: str
    textChanges: typing.List[GoogleCloudDocumentaiV1beta2DocumentTextChange]
    labels: typing.List[GoogleCloudDocumentaiV1beta2DocumentLabel]
    text: str
    translations: typing.List[GoogleCloudDocumentaiV1beta2DocumentTranslation]
    revisions: typing.List[GoogleCloudDocumentaiV1beta2DocumentRevision]
    mimeType: str
    uri: str
    entities: typing.List[GoogleCloudDocumentaiV1beta2DocumentEntity]
    textStyles: typing.List[GoogleCloudDocumentaiV1beta2DocumentStyle]
    pages: typing.List[GoogleCloudDocumentaiV1beta2DocumentPage]
    entityRelations: typing.List[GoogleCloudDocumentaiV1beta2DocumentEntityRelation]
    error: GoogleRpcStatus
    shardInfo: GoogleCloudDocumentaiV1beta2DocumentShardInfo

class GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    stateMessage: str
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "WAITING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

class GoogleCloudDocumentaiV1beta2DocumentTextChange(
    typing_extensions.TypedDict, total=False
):
    changedText: str
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor
    provenance: typing.List[GoogleCloudDocumentaiV1beta2DocumentProvenance]

class GoogleCloudDocumentaiV1beta3BatchProcessMetadata(
    typing_extensions.TypedDict, total=False
):
    individualProcessStatuses: typing.List[
        GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "WAITING",
        "RUNNING",
        "SUCCEEDED",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
    ]
    stateMessage: str
    createTime: str
    updateTime: str

class GoogleCloudDocumentaiV1beta2OcrParams(typing_extensions.TypedDict, total=False):
    languageHints: typing.List[str]

class GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell]

class GoogleCloudDocumentaiV1beta1ProcessDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudDocumentaiV1beta1OutputConfig
    inputConfig: GoogleCloudDocumentaiV1beta1InputConfig

class GoogleCloudDocumentaiV1beta1DocumentPageDimension(
    typing_extensions.TypedDict, total=False
):
    unit: str
    height: float
    width: float

class GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    moneyValue: GoogleTypeMoney
    text: str
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime

class GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    error: GoogleRpcStatus

class GoogleCloudDocumentaiV1beta2AutoMlParams(
    typing_extensions.TypedDict, total=False
):
    model: str

class GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    colSpan: int
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    rowSpan: int

class GoogleCloudDocumentaiV1beta2DocumentPageBlock(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

class GoogleCloudDocumentaiV1beta1DocumentTextChange(
    typing_extensions.TypedDict, total=False
):
    provenance: typing.List[GoogleCloudDocumentaiV1beta1DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor
    changedText: str

class GoogleCloudDocumentaiV1beta1DocumentEntityRelation(
    typing_extensions.TypedDict, total=False
):
    subjectId: str
    relation: str
    objectId: str

class GoogleCloudDocumentaiV1beta3BatchProcessResponse(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDocumentaiV1beta2TableBoundHint(
    typing_extensions.TypedDict, total=False
):
    pageNumber: int
    boundingBox: GoogleCloudDocumentaiV1beta2BoundingPoly

class GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell]

class GoogleCloudDocumentaiV1beta2EntityExtractionParams(
    typing_extensions.TypedDict, total=False
):
    modelVersion: str
    enabled: bool

class GoogleCloudDocumentaiV1beta1DocumentShardInfo(
    typing_extensions.TypedDict, total=False
):
    shardIndex: str
    textOffset: str
    shardCount: str

class GoogleCloudDocumentaiV1beta2DocumentPageMatrix(
    typing_extensions.TypedDict, total=False
):
    rows: int
    cols: int
    type: int
    data: str

class GoogleCloudDocumentaiV1beta1InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudDocumentaiV1beta1GcsSource
    mimeType: str

class GoogleCloudDocumentaiV1beta2DocumentPageFormField(
    typing_extensions.TypedDict, total=False
):
    nameDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    fieldValue: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    valueDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    fieldName: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    valueType: str

class GoogleCloudDocumentaiV1beta1DocumentPage(
    typing_extensions.TypedDict, total=False
):
    paragraphs: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageParagraph]
    lines: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageLine]
    blocks: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageBlock]
    visualElements: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageVisualElement]
    pageNumber: int
    tables: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTable]
    tokens: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageToken]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    transforms: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageMatrix]
    dimension: GoogleCloudDocumentaiV1beta1DocumentPageDimension
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    image: GoogleCloudDocumentaiV1beta1DocumentPageImage
    formFields: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageFormField]

class GoogleCloudDocumentaiV1beta2Vertex(typing_extensions.TypedDict, total=False):
    y: int
    x: int

class GoogleCloudDocumentaiV1beta2BatchProcessDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleCloudDocumentaiV1beta2ProcessDocumentRequest]

class GoogleCloudDocumentaiV1beta1DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    detectedBreak: GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreak
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]

class GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    rowSpan: int
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    colSpan: int

class GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

class GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReview(
    typing_extensions.TypedDict, total=False
):
    stateMessage: str
    state: str

class GoogleCloudDocumentaiV1beta2DocumentPageDimension(
    typing_extensions.TypedDict, total=False
):
    unit: str
    height: float
    width: float

class GoogleCloudDocumentaiV1beta2DocumentStyleFontSize(
    typing_extensions.TypedDict, total=False
):
    size: float
    unit: str

class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    year: int
    month: int
    day: int

class GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    layoutType: typing_extensions.Literal[
        "LAYOUT_TYPE_UNSPECIFIED",
        "BLOCK",
        "PARAGRAPH",
        "LINE",
        "TOKEN",
        "VISUAL_ELEMENT",
        "TABLE",
        "FORM_FIELD",
    ]
    page: str
    boundingPoly: GoogleCloudDocumentaiV1beta1BoundingPoly
    layoutId: str

class GoogleCloudDocumentaiV1beta2OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDocumentaiV1beta2GcsDestination
    pagesPerShard: int

class GoogleCloudDocumentaiV1beta1DocumentEntity(typing.Dict[str, typing.Any]): ...

class GoogleCloudDocumentaiV1beta2InputConfig(typing_extensions.TypedDict, total=False):
    mimeType: str
    contents: str
    gcsSource: GoogleCloudDocumentaiV1beta2GcsSource
