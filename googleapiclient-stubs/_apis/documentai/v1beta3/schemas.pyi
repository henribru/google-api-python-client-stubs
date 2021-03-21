import typing

import typing_extensions
@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DisableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EnableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    evaluation: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    testDatasetValidation: GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation
    trainingDatasetValidation: GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation(
    typing_extensions.TypedDict, total=False
):
    datasetErrors: typing.List[GoogleRpcStatus]
    documentErrors: typing.List[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1BatchProcessMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    individualProcessStatuses: typing.List[
        GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatus
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
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatus(
    typing_extensions.TypedDict, total=False
):
    humanReviewStatus: GoogleCloudDocumentaiV1HumanReviewStatus
    inputGcsSource: str
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1BatchProcessResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1CommonOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1HumanReviewStatus(
    typing_extensions.TypedDict, total=False
):
    humanReviewOperation: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "SKIPPED", "VALIDATION_PASSED", "IN_PROGRESS", "ERROR"
    ]
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1ReviewDocumentOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1ReviewDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudDocumentaiV1beta1ProcessDocumentResponse]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: typing.List[GoogleCloudDocumentaiV1beta1NormalizedVertex]
    vertices: typing.List[GoogleCloudDocumentaiV1beta1Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1Document(typing_extensions.TypedDict, total=False):
    content: str
    entities: typing.List[GoogleCloudDocumentaiV1beta1DocumentEntity]
    entityRelations: typing.List[GoogleCloudDocumentaiV1beta1DocumentEntityRelation]
    error: GoogleRpcStatus
    mimeType: str
    pages: typing.List[GoogleCloudDocumentaiV1beta1DocumentPage]
    revisions: typing.List[GoogleCloudDocumentaiV1beta1DocumentRevision]
    shardInfo: GoogleCloudDocumentaiV1beta1DocumentShardInfo
    text: str
    textChanges: typing.List[GoogleCloudDocumentaiV1beta1DocumentTextChange]
    textStyles: typing.List[GoogleCloudDocumentaiV1beta1DocumentStyle]
    translations: typing.List[GoogleCloudDocumentaiV1beta1DocumentTranslation]
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentEntity(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    moneyValue: GoogleTypeMoney
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentEntityRelation(
    typing_extensions.TypedDict, total=False
):
    objectId: str
    relation: str
    subjectId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPage(
    typing_extensions.TypedDict, total=False
):
    blocks: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageBlock]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    dimension: GoogleCloudDocumentaiV1beta1DocumentPageDimension
    formFields: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageFormField]
    image: GoogleCloudDocumentaiV1beta1DocumentPageImage
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    lines: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageLine]
    pageNumber: int
    paragraphs: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageParagraph]
    tables: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTable]
    tokens: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageToken]
    transforms: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageMatrix]
    visualElements: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageVisualElement]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta1BoundingPoly
    layoutId: str
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

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageBlock(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageDimension(
    typing_extensions.TypedDict, total=False
):
    height: float
    unit: str
    width: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageFormField(
    typing_extensions.TypedDict, total=False
):
    fieldName: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    fieldValue: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    nameDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    valueDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    valueType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageImage(
    typing_extensions.TypedDict, total=False
):
    content: str
    height: int
    mimeType: str
    width: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageLayout(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta1BoundingPoly
    confidence: float
    orientation: typing_extensions.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageLine(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageMatrix(
    typing_extensions.TypedDict, total=False
):
    cols: int
    data: str
    rows: int
    type: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageParagraph(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    bodyRows: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    headerRows: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: typing.List[GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageVisualElement(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    id: int
    parents: typing.List[GoogleCloudDocumentaiV1beta1DocumentProvenanceParent]
    revision: int
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    id: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReview
    id: str
    parent: typing.List[int]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReview(
    typing_extensions.TypedDict, total=False
):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentShardInfo(
    typing_extensions.TypedDict, total=False
):
    shardCount: str
    shardIndex: str
    textOffset: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentStyle(
    typing_extensions.TypedDict, total=False
):
    backgroundColor: GoogleTypeColor
    color: GoogleTypeColor
    fontSize: GoogleCloudDocumentaiV1beta1DocumentStyleFontSize
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor
    textDecoration: str
    textStyle: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentStyleFontSize(
    typing_extensions.TypedDict, total=False
):
    size: float
    unit: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentTextAnchor(
    typing_extensions.TypedDict, total=False
):
    content: str
    textSegments: typing.List[GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    startIndex: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentTextChange(
    typing_extensions.TypedDict, total=False
):
    changedText: str
    provenance: typing.List[GoogleCloudDocumentaiV1beta1DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentTranslation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    provenance: typing.List[GoogleCloudDocumentaiV1beta1DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor
    translatedText: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudDocumentaiV1beta1GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
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
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDocumentaiV1beta1GcsDestination
    pagesPerShard: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1ProcessDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudDocumentaiV1beta1InputConfig
    outputConfig: GoogleCloudDocumentaiV1beta1OutputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[GoogleCloudDocumentaiV1beta2ProcessDocumentResponse]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: typing.List[GoogleCloudDocumentaiV1beta2NormalizedVertex]
    vertices: typing.List[GoogleCloudDocumentaiV1beta2Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2Document(typing_extensions.TypedDict, total=False):
    content: str
    entities: typing.List[GoogleCloudDocumentaiV1beta2DocumentEntity]
    entityRelations: typing.List[GoogleCloudDocumentaiV1beta2DocumentEntityRelation]
    error: GoogleRpcStatus
    labels: typing.List[GoogleCloudDocumentaiV1beta2DocumentLabel]
    mimeType: str
    pages: typing.List[GoogleCloudDocumentaiV1beta2DocumentPage]
    revisions: typing.List[GoogleCloudDocumentaiV1beta2DocumentRevision]
    shardInfo: GoogleCloudDocumentaiV1beta2DocumentShardInfo
    text: str
    textChanges: typing.List[GoogleCloudDocumentaiV1beta2DocumentTextChange]
    textStyles: typing.List[GoogleCloudDocumentaiV1beta2DocumentStyle]
    translations: typing.List[GoogleCloudDocumentaiV1beta2DocumentTranslation]
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentEntity(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    moneyValue: GoogleTypeMoney
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentEntityRelation(
    typing_extensions.TypedDict, total=False
):
    objectId: str
    relation: str
    subjectId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentLabel(
    typing_extensions.TypedDict, total=False
):
    automlModel: str
    confidence: float
    name: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPage(
    typing_extensions.TypedDict, total=False
):
    blocks: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageBlock]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    dimension: GoogleCloudDocumentaiV1beta2DocumentPageDimension
    formFields: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageFormField]
    image: GoogleCloudDocumentaiV1beta2DocumentPageImage
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    lines: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageLine]
    pageNumber: int
    paragraphs: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageParagraph]
    tables: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTable]
    tokens: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageToken]
    transforms: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageMatrix]
    visualElements: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageVisualElement]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta2BoundingPoly
    layoutId: str
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

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageBlock(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageDimension(
    typing_extensions.TypedDict, total=False
):
    height: float
    unit: str
    width: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageFormField(
    typing_extensions.TypedDict, total=False
):
    fieldName: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    fieldValue: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    nameDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    valueDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    valueType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageImage(
    typing_extensions.TypedDict, total=False
):
    content: str
    height: int
    mimeType: str
    width: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageLayout(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta2BoundingPoly
    confidence: float
    orientation: typing_extensions.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageLine(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageMatrix(
    typing_extensions.TypedDict, total=False
):
    cols: int
    data: str
    rows: int
    type: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageParagraph(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    bodyRows: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    headerRows: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: typing.List[GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageVisualElement(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    id: int
    parents: typing.List[GoogleCloudDocumentaiV1beta2DocumentProvenanceParent]
    revision: int
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    id: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReview
    id: str
    parent: typing.List[int]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReview(
    typing_extensions.TypedDict, total=False
):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentShardInfo(
    typing_extensions.TypedDict, total=False
):
    shardCount: str
    shardIndex: str
    textOffset: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentStyle(
    typing_extensions.TypedDict, total=False
):
    backgroundColor: GoogleTypeColor
    color: GoogleTypeColor
    fontSize: GoogleCloudDocumentaiV1beta2DocumentStyleFontSize
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor
    textDecoration: str
    textStyle: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentStyleFontSize(
    typing_extensions.TypedDict, total=False
):
    size: float
    unit: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentTextAnchor(
    typing_extensions.TypedDict, total=False
):
    content: str
    textSegments: typing.List[GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegment]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegment(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    startIndex: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentTextChange(
    typing_extensions.TypedDict, total=False
):
    changedText: str
    provenance: typing.List[GoogleCloudDocumentaiV1beta2DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentTranslation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    provenance: typing.List[GoogleCloudDocumentaiV1beta2DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor
    translatedText: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2InputConfig(typing_extensions.TypedDict, total=False):
    contents: str
    gcsSource: GoogleCloudDocumentaiV1beta2GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2OperationMetadata(
    typing_extensions.TypedDict, total=False
):
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
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDocumentaiV1beta2GcsDestination
    pagesPerShard: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2ProcessDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudDocumentaiV1beta2InputConfig
    outputConfig: GoogleCloudDocumentaiV1beta2OutputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDocuments: GoogleCloudDocumentaiV1beta3GcsDocuments
    gcsPrefix: GoogleCloudDocumentaiV1beta3GcsPrefix

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
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
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus(
    typing_extensions.TypedDict, total=False
):
    humanReviewOperation: str
    humanReviewStatus: GoogleCloudDocumentaiV1beta3HumanReviewStatus
    inputGcsSource: str
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessRequest(
    typing_extensions.TypedDict, total=False
):
    documentOutputConfig: GoogleCloudDocumentaiV1beta3DocumentOutputConfig
    inputConfigs: typing.List[
        GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchInputConfig
    ]
    inputDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig
    outputConfig: GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchOutputConfig
    skipHumanReview: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchInputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsSource: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchOutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: typing.List[GoogleCloudDocumentaiV1beta3NormalizedVertex]
    vertices: typing.List[GoogleCloudDocumentaiV1beta3Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3CommonOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Document(typing_extensions.TypedDict, total=False):
    content: str
    entities: typing.List[GoogleCloudDocumentaiV1beta3DocumentEntity]
    entityRelations: typing.List[GoogleCloudDocumentaiV1beta3DocumentEntityRelation]
    error: GoogleRpcStatus
    mimeType: str
    pages: typing.List[GoogleCloudDocumentaiV1beta3DocumentPage]
    revisions: typing.List[GoogleCloudDocumentaiV1beta3DocumentRevision]
    shardInfo: GoogleCloudDocumentaiV1beta3DocumentShardInfo
    text: str
    textChanges: typing.List[GoogleCloudDocumentaiV1beta3DocumentTextChange]
    textStyles: typing.List[GoogleCloudDocumentaiV1beta3DocumentStyle]
    translations: typing.List[GoogleCloudDocumentaiV1beta3DocumentTranslation]
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntity(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    moneyValue: GoogleTypeMoney
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntityRelation(
    typing_extensions.TypedDict, total=False
):
    objectId: str
    relation: str
    subjectId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentOutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsOutputConfig: GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPage(
    typing_extensions.TypedDict, total=False
):
    blocks: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageBlock]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    dimension: GoogleCloudDocumentaiV1beta3DocumentPageDimension
    formFields: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageFormField]
    image: GoogleCloudDocumentaiV1beta3DocumentPageImage
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    lines: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageLine]
    pageNumber: int
    paragraphs: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageParagraph]
    tables: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageTable]
    tokens: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageToken]
    transforms: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageMatrix]
    visualElements: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageVisualElement]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta3BoundingPoly
    layoutId: str
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

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageBlock(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageDimension(
    typing_extensions.TypedDict, total=False
):
    height: float
    unit: str
    width: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageFormField(
    typing_extensions.TypedDict, total=False
):
    fieldName: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    fieldValue: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    nameDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    valueDetectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    valueType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageImage(
    typing_extensions.TypedDict, total=False
):
    content: str
    height: int
    mimeType: str
    width: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageLayout(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta3BoundingPoly
    confidence: float
    orientation: typing_extensions.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageLine(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageMatrix(
    typing_extensions.TypedDict, total=False
):
    cols: int
    data: str
    rows: int
    type: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageParagraph(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    bodyRows: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow]
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    headerRows: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: typing.List[GoogleCloudDocumentaiV1beta3DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudDocumentaiV1beta3DocumentPageTokenDetectedBreak
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTokenDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageVisualElement(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: typing.List[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    id: int
    parents: typing.List[GoogleCloudDocumentaiV1beta3DocumentProvenanceParent]
    revision: int
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    id: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta3DocumentRevisionHumanReview
    id: str
    parent: typing.List[int]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentRevisionHumanReview(
    typing_extensions.TypedDict, total=False
):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentShardInfo(
    typing_extensions.TypedDict, total=False
):
    shardCount: str
    shardIndex: str
    textOffset: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentStyle(
    typing_extensions.TypedDict, total=False
):
    backgroundColor: GoogleTypeColor
    color: GoogleTypeColor
    fontSize: GoogleCloudDocumentaiV1beta3DocumentStyleFontSize
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor
    textDecoration: str
    textStyle: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentStyleFontSize(
    typing_extensions.TypedDict, total=False
):
    size: float
    unit: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentTextAnchor(
    typing_extensions.TypedDict, total=False
):
    content: str
    textSegments: typing.List[GoogleCloudDocumentaiV1beta3DocumentTextAnchorTextSegment]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentTextAnchorTextSegment(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    startIndex: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentTextChange(
    typing_extensions.TypedDict, total=False
):
    changedText: str
    provenance: typing.List[GoogleCloudDocumentaiV1beta3DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentTranslation(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    provenance: typing.List[GoogleCloudDocumentaiV1beta3DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor
    translatedText: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsDocument(typing_extensions.TypedDict, total=False):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsDocuments(
    typing_extensions.TypedDict, total=False
):
    documents: typing.List[GoogleCloudDocumentaiV1beta3GcsDocument]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsPrefix(typing_extensions.TypedDict, total=False):
    gcsUriPrefix: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3HumanReviewStatus(
    typing_extensions.TypedDict, total=False
):
    humanReviewOperation: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "SKIPPED", "VALIDATION_PASSED", "IN_PROGRESS", "ERROR"
    ]
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessRequest(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDocumentaiV1beta3Document
    inlineDocument: GoogleCloudDocumentaiV1beta3Document
    rawDocument: GoogleCloudDocumentaiV1beta3RawDocument
    skipHumanReview: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessResponse(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDocumentaiV1beta3Document
    humanReviewOperation: str
    humanReviewStatus: GoogleCloudDocumentaiV1beta3HumanReviewStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3RawDocument(typing_extensions.TypedDict, total=False):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ReviewDocumentRequest(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDocumentaiV1beta3Document
    inlineDocument: GoogleCloudDocumentaiV1beta3Document

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ReviewDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locations: typing.List[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeColor(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeDateTime(typing_extensions.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: GoogleTypeTimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class GoogleTypePostalAddress(typing_extensions.TypedDict, total=False):
    addressLines: typing.List[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: typing.List[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str
