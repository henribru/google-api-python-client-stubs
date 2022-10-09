import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    errorDocumentCount: int
    individualBatchDeleteStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus(
    typing_extensions.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    destDatasetType: typing_extensions.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    destSplitType: typing_extensions.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    individualBatchMoveStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatus
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatus(
    typing_extensions.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    resource: str
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
class GoogleCloudDocumentaiUiv1beta3DeleteDataLabelingJobOperationMetadata(
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
class GoogleCloudDocumentaiUiv1beta3DocumentId(
    typing_extensions.TypedDict, total=False
):
    gcsManagedDocId: GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentId
    revisionReference: GoogleCloudDocumentaiUiv1beta3RevisionReference

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentId(
    typing_extensions.TypedDict, total=False
):
    cwDocId: str
    gcsUri: str

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
class GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    individualExportStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatus
    ]
    splitExportStats: _list[
        GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStat
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatus(
    typing_extensions.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStat(
    typing_extensions.TypedDict, total=False
):
    splitType: typing_extensions.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    importConfigValidationResults: _list[
        GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResult
    ]
    individualImportStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResult(
    typing_extensions.TypedDict, total=False
):
    inputGcsSource: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatus(
    typing_extensions.TypedDict, total=False
):
    inputGcsSource: str
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    datasetResyncStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatus
    ]
    individualDocumentResyncStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatus
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatus(
    typing_extensions.TypedDict, total=False
):
    datasetInconsistencyType: typing_extensions.Literal[
        "DATASET_INCONSISTENCY_TYPE_UNSPECIFIED",
        "DATASET_INCONSISTENCY_TYPE_NO_STORAGE_MARKER",
    ]
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatus(
    typing_extensions.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    documentInconsistencyType: typing_extensions.Literal[
        "DOCUMENT_INCONSISTENCY_TYPE_UNSPECIFIED",
        "DOCUMENT_INCONSISTENCY_TYPE_INVALID_DOCPROTO",
        "DOCUMENT_INCONSISTENCY_TYPE_MISMATCHED_METADATA",
        "DOCUMENT_INCONSISTENCY_TYPE_NO_PAGE_IMAGE",
    ]
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3RevisionReference(
    typing_extensions.TypedDict, total=False
):
    latestProcessorVersion: str
    revisionCase: typing_extensions.Literal[
        "REVISION_CASE_UNSPECIFIED", "LATEST_HUMAN_REVIEW", "LATEST_TIMESTAMP"
    ]
    revisionId: str

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
    datasetErrorCount: int
    datasetErrors: _list[GoogleRpcStatus]
    documentErrorCount: int
    documentErrors: _list[GoogleRpcStatus]

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
class GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

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
    individualProcessStatuses: _list[
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
    resource: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DeleteProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DeleteProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DeployProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DeployProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1DisableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DisableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1EnableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1EnableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

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
    questionId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1ReviewDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: str
    rejectionReason: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "REJECTED", "SUCCEEDED"]

@typing.type_check_only
class GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1UndeployProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1UndeployProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1alpha1AnalyzeHitlDataMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1alpha1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1alpha1CommonOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    resource: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1Barcode(typing_extensions.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudDocumentaiV1beta1ProcessDocumentResponse]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: _list[GoogleCloudDocumentaiV1beta1NormalizedVertex]
    vertices: _list[GoogleCloudDocumentaiV1beta1Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1Document(typing_extensions.TypedDict, total=False):
    content: str
    entities: _list[GoogleCloudDocumentaiV1beta1DocumentEntity]
    entityRelations: _list[GoogleCloudDocumentaiV1beta1DocumentEntityRelation]
    error: GoogleRpcStatus
    mimeType: str
    pages: _list[GoogleCloudDocumentaiV1beta1DocumentPage]
    revisions: _list[GoogleCloudDocumentaiV1beta1DocumentRevision]
    shardInfo: GoogleCloudDocumentaiV1beta1DocumentShardInfo
    text: str
    textChanges: _list[GoogleCloudDocumentaiV1beta1DocumentTextChange]
    textStyles: _list[GoogleCloudDocumentaiV1beta1DocumentStyle]
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentEntity(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    floatValue: float
    integerValue: int
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
    blocks: _list[GoogleCloudDocumentaiV1beta1DocumentPageBlock]
    detectedBarcodes: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcode]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    dimension: GoogleCloudDocumentaiV1beta1DocumentPageDimension
    formFields: _list[GoogleCloudDocumentaiV1beta1DocumentPageFormField]
    image: GoogleCloudDocumentaiV1beta1DocumentPageImage
    imageQualityScores: GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScores
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    lines: _list[GoogleCloudDocumentaiV1beta1DocumentPageLine]
    pageNumber: int
    paragraphs: _list[GoogleCloudDocumentaiV1beta1DocumentPageParagraph]
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance
    symbols: _list[GoogleCloudDocumentaiV1beta1DocumentPageSymbol]
    tables: _list[GoogleCloudDocumentaiV1beta1DocumentPageTable]
    tokens: _list[GoogleCloudDocumentaiV1beta1DocumentPageToken]
    transforms: _list[GoogleCloudDocumentaiV1beta1DocumentPageMatrix]
    visualElements: _list[GoogleCloudDocumentaiV1beta1DocumentPageVisualElement]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: _list[GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta1BoundingPoly
    confidence: float
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcode(
    typing_extensions.TypedDict, total=False
):
    barcode: GoogleCloudDocumentaiV1beta1Barcode
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout

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
    correctedKeyText: str
    correctedValueText: str
    fieldName: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    fieldValue: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    nameDetectedLanguages: _list[
        GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage
    ]
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance
    valueDetectedLanguages: _list[
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
class GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScores(
    typing_extensions.TypedDict, total=False
):
    detectedDefects: _list[
        GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefect
    ]
    qualityScore: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefect(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    type: str

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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageSymbol(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    bodyRows: _list[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    headerRows: _list[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: _list[GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreak
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    id: int
    parents: _list[GoogleCloudDocumentaiV1beta1DocumentProvenanceParent]
    revision: int
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
        "EVAL_SKIPPED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    id: int
    index: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReview
    id: str
    parent: _list[int]
    parentIds: _list[str]
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
    fontFamily: str
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
    textSegments: _list[GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment]

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
    provenance: _list[GoogleCloudDocumentaiV1beta1DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor

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
class GoogleCloudDocumentaiV1beta2Barcode(typing_extensions.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleCloudDocumentaiV1beta2ProcessDocumentResponse]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: _list[GoogleCloudDocumentaiV1beta2NormalizedVertex]
    vertices: _list[GoogleCloudDocumentaiV1beta2Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2Document(typing_extensions.TypedDict, total=False):
    content: str
    entities: _list[GoogleCloudDocumentaiV1beta2DocumentEntity]
    entityRelations: _list[GoogleCloudDocumentaiV1beta2DocumentEntityRelation]
    error: GoogleRpcStatus
    labels: _list[GoogleCloudDocumentaiV1beta2DocumentLabel]
    mimeType: str
    pages: _list[GoogleCloudDocumentaiV1beta2DocumentPage]
    revisions: _list[GoogleCloudDocumentaiV1beta2DocumentRevision]
    shardInfo: GoogleCloudDocumentaiV1beta2DocumentShardInfo
    text: str
    textChanges: _list[GoogleCloudDocumentaiV1beta2DocumentTextChange]
    textStyles: _list[GoogleCloudDocumentaiV1beta2DocumentStyle]
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentEntity(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    floatValue: float
    integerValue: int
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
    blocks: _list[GoogleCloudDocumentaiV1beta2DocumentPageBlock]
    detectedBarcodes: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcode]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    dimension: GoogleCloudDocumentaiV1beta2DocumentPageDimension
    formFields: _list[GoogleCloudDocumentaiV1beta2DocumentPageFormField]
    image: GoogleCloudDocumentaiV1beta2DocumentPageImage
    imageQualityScores: GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScores
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    lines: _list[GoogleCloudDocumentaiV1beta2DocumentPageLine]
    pageNumber: int
    paragraphs: _list[GoogleCloudDocumentaiV1beta2DocumentPageParagraph]
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance
    symbols: _list[GoogleCloudDocumentaiV1beta2DocumentPageSymbol]
    tables: _list[GoogleCloudDocumentaiV1beta2DocumentPageTable]
    tokens: _list[GoogleCloudDocumentaiV1beta2DocumentPageToken]
    transforms: _list[GoogleCloudDocumentaiV1beta2DocumentPageMatrix]
    visualElements: _list[GoogleCloudDocumentaiV1beta2DocumentPageVisualElement]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: _list[GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta2BoundingPoly
    confidence: float
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcode(
    typing_extensions.TypedDict, total=False
):
    barcode: GoogleCloudDocumentaiV1beta2Barcode
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout

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
    correctedKeyText: str
    correctedValueText: str
    fieldName: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    fieldValue: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    nameDetectedLanguages: _list[
        GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage
    ]
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance
    valueDetectedLanguages: _list[
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
class GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScores(
    typing_extensions.TypedDict, total=False
):
    detectedDefects: _list[
        GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefect
    ]
    qualityScore: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefect(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    type: str

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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageSymbol(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    bodyRows: _list[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    headerRows: _list[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: _list[GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreak
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    id: int
    parents: _list[GoogleCloudDocumentaiV1beta2DocumentProvenanceParent]
    revision: int
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
        "EVAL_SKIPPED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    id: int
    index: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReview
    id: str
    parent: _list[int]
    parentIds: _list[str]
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
    fontFamily: str
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
    textSegments: _list[GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegment]

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
    provenance: _list[GoogleCloudDocumentaiV1beta2DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor

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
class GoogleCloudDocumentaiV1beta3Barcode(typing_extensions.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

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
    individualProcessStatuses: _list[
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
    inputConfigs: _list[GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchInputConfig]
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
    normalizedVertices: _list[GoogleCloudDocumentaiV1beta3NormalizedVertex]
    vertices: _list[GoogleCloudDocumentaiV1beta3Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3CommonOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    resource: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeleteProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeployProcessorVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DisableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DisableProcessorRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DisableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Document(typing_extensions.TypedDict, total=False):
    content: str
    entities: _list[GoogleCloudDocumentaiV1beta3DocumentEntity]
    entityRelations: _list[GoogleCloudDocumentaiV1beta3DocumentEntityRelation]
    error: GoogleRpcStatus
    mimeType: str
    pages: _list[GoogleCloudDocumentaiV1beta3DocumentPage]
    revisions: _list[GoogleCloudDocumentaiV1beta3DocumentRevision]
    shardInfo: GoogleCloudDocumentaiV1beta3DocumentShardInfo
    text: str
    textChanges: _list[GoogleCloudDocumentaiV1beta3DocumentTextChange]
    textStyles: _list[GoogleCloudDocumentaiV1beta3DocumentStyle]
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntity(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntityNormalizedValue(
    typing_extensions.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    floatValue: float
    integerValue: int
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
    fieldMask: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPage(
    typing_extensions.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentPageBlock]
    detectedBarcodes: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedBarcode]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    dimension: GoogleCloudDocumentaiV1beta3DocumentPageDimension
    formFields: _list[GoogleCloudDocumentaiV1beta3DocumentPageFormField]
    image: GoogleCloudDocumentaiV1beta3DocumentPageImage
    imageQualityScores: GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScores
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    lines: _list[GoogleCloudDocumentaiV1beta3DocumentPageLine]
    pageNumber: int
    paragraphs: _list[GoogleCloudDocumentaiV1beta3DocumentPageParagraph]
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance
    symbols: _list[GoogleCloudDocumentaiV1beta3DocumentPageSymbol]
    tables: _list[GoogleCloudDocumentaiV1beta3DocumentPageTable]
    tokens: _list[GoogleCloudDocumentaiV1beta3DocumentPageToken]
    transforms: _list[GoogleCloudDocumentaiV1beta3DocumentPageMatrix]
    visualElements: _list[GoogleCloudDocumentaiV1beta3DocumentPageVisualElement]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageAnchor(
    typing_extensions.TypedDict, total=False
):
    pageRefs: _list[GoogleCloudDocumentaiV1beta3DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageAnchorPageRef(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta3BoundingPoly
    confidence: float
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageDetectedBarcode(
    typing_extensions.TypedDict, total=False
):
    barcode: GoogleCloudDocumentaiV1beta3Barcode
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout

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
    correctedKeyText: str
    correctedValueText: str
    fieldName: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    fieldValue: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    nameDetectedLanguages: _list[
        GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage
    ]
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance
    valueDetectedLanguages: _list[
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
class GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScores(
    typing_extensions.TypedDict, total=False
):
    detectedDefects: _list[
        GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScoresDetectedDefect
    ]
    qualityScore: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScoresDetectedDefect(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    type: str

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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageSymbol(
    typing_extensions.TypedDict, total=False
):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTable(
    typing_extensions.TypedDict, total=False
):
    bodyRows: _list[GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    headerRows: _list[GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTableTableCell(
    typing_extensions.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: _list[GoogleCloudDocumentaiV1beta3DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageToken(
    typing_extensions.TypedDict, total=False
):
    detectedBreak: GoogleCloudDocumentaiV1beta3DocumentPageTokenDetectedBreak
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
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
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentProvenance(
    typing_extensions.TypedDict, total=False
):
    id: int
    parents: _list[GoogleCloudDocumentaiV1beta3DocumentProvenanceParent]
    revision: int
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
        "EVAL_SKIPPED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentProvenanceParent(
    typing_extensions.TypedDict, total=False
):
    id: int
    index: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentRevision(
    typing_extensions.TypedDict, total=False
):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta3DocumentRevisionHumanReview
    id: str
    parent: _list[int]
    parentIds: _list[str]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentRevisionHumanReview(
    typing_extensions.TypedDict, total=False
):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchema(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    entityTypes: _list[GoogleCloudDocumentaiV1beta3DocumentSchemaEntityType]
    metadata: GoogleCloudDocumentaiV1beta3DocumentSchemaMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchemaEntityType(
    typing_extensions.TypedDict, total=False
):
    baseTypes: _list[str]
    displayName: str
    entityTypeMetadata: GoogleCloudDocumentaiV1beta3EntityTypeMetadata
    enumValues: GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeEnumValues
    name: str
    properties: _list[GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeProperty]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeEnumValues(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeProperty(
    typing_extensions.TypedDict, total=False
):
    name: str
    occurrenceType: typing_extensions.Literal[
        "OCCURRENCE_TYPE_UNSPECIFIED",
        "OPTIONAL_ONCE",
        "OPTIONAL_MULTIPLE",
        "REQUIRED_ONCE",
        "REQUIRED_MULTIPLE",
    ]
    propertyMetadata: GoogleCloudDocumentaiV1beta3PropertyMetadata
    valueType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    documentAllowMultipleLabels: bool
    documentSplitter: bool
    prefixedNamingOnProperties: bool
    skipNamingValidation: bool

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
    fontFamily: str
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
    textSegments: _list[GoogleCloudDocumentaiV1beta3DocumentTextAnchorTextSegment]

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
    provenance: _list[GoogleCloudDocumentaiV1beta3DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EntityTypeMetadata(
    typing_extensions.TypedDict, total=False
):
    humanReviewLabelingMetadata: GoogleCloudDocumentaiV1beta3HumanReviewLabelingMetadata
    humanReviewMetadata: GoogleCloudDocumentaiV1beta3HumanReviewValidationMetadata
    inactive: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponse(
    typing_extensions.TypedDict, total=False
):
    processorTypes: _list[GoogleCloudDocumentaiV1beta3ProcessorType]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsDocument(typing_extensions.TypedDict, total=False):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsDocuments(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDocumentaiV1beta3GcsDocument]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsPrefix(typing_extensions.TypedDict, total=False):
    gcsUriPrefix: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3HumanReviewLabelingMetadata(
    typing_extensions.TypedDict, total=False
):
    enableNormalizationEditing: bool

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
class GoogleCloudDocumentaiV1beta3HumanReviewValidationMetadata(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    enableValidation: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    processorTypes: _list[GoogleCloudDocumentaiV1beta3ProcessorType]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    processorVersions: _list[GoogleCloudDocumentaiV1beta3ProcessorVersion]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    processors: _list[GoogleCloudDocumentaiV1beta3Processor]

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
    fieldMask: str
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
class GoogleCloudDocumentaiV1beta3Processor(typing_extensions.TypedDict, total=False):
    createTime: str
    defaultProcessorVersion: str
    displayName: str
    kmsKeyName: str
    name: str
    processEndpoint: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ENABLED",
        "DISABLED",
        "ENABLING",
        "DISABLING",
        "CREATING",
        "FAILED",
        "DELETING",
    ]
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorType(
    typing_extensions.TypedDict, total=False
):
    allowCreation: bool
    availableLocations: _list[GoogleCloudDocumentaiV1beta3ProcessorTypeLocationInfo]
    category: str
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    name: str
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorTypeLocationInfo(
    typing_extensions.TypedDict, total=False
):
    locationId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersion(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    deprecationInfo: GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo
    displayName: str
    googleManaged: bool
    kmsKeyName: str
    kmsKeyVersionName: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "DEPLOYED",
        "DEPLOYING",
        "UNDEPLOYED",
        "UNDEPLOYING",
        "CREATING",
        "DELETING",
        "FAILED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo(
    typing_extensions.TypedDict, total=False
):
    deprecationTime: str
    replacementProcessorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3PropertyMetadata(
    typing_extensions.TypedDict, total=False
):
    humanReviewLabelingMetadata: GoogleCloudDocumentaiV1beta3HumanReviewLabelingMetadata
    humanReviewMetadata: GoogleCloudDocumentaiV1beta3HumanReviewValidationMetadata
    inactive: bool

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
    questionId: str
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
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    enableSchemaValidation: bool
    inlineDocument: GoogleCloudDocumentaiV1beta3Document
    priority: typing_extensions.Literal["DEFAULT", "URGENT"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ReviewDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: str
    rejectionReason: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "REJECTED", "SUCCEEDED"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionRequest(
    typing_extensions.TypedDict, total=False
):
    defaultProcessorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3UndeployProcessorVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
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
    addressLines: _list[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: _list[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str
