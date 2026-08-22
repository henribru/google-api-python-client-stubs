import typing

_list = list

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    individualAutoLabelStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatus(
    typing.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    errorDocumentCount: int
    individualBatchDeleteStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus(
    typing.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    destDatasetType: typing.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    destSplitType: typing.Literal[
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
    typing.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    individualBatchUpdateStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsMetadataIndividualBatchUpdateStatus
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsMetadataIndividualBatchUpdateStatus(
    typing.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    resource: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DisableProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentId(typing.TypedDict, total=False):
    gcsManagedDocId: GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentId
    revisionRef: GoogleCloudDocumentaiUiv1beta3RevisionRef
    unmanagedDocId: GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentId

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentId(
    typing.TypedDict, total=False
):
    cwDocId: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentId(
    typing.TypedDict, total=False
):
    docId: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EnableProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponse(
    typing.TypedDict, total=False
):
    evaluation: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStat(
    typing.TypedDict, total=False
):
    splitType: typing.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponse(
    typing.TypedDict, total=False
):
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    inputGcsSource: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatus(
    typing.TypedDict, total=False
):
    inputGcsSource: str
    outputDocumentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponse(
    typing.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    datasetInconsistencyType: typing.Literal[
        "DATASET_INCONSISTENCY_TYPE_UNSPECIFIED",
        "DATASET_INCONSISTENCY_TYPE_NO_STORAGE_MARKER",
    ]
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatus(
    typing.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    documentInconsistencyType: typing.Literal[
        "DOCUMENT_INCONSISTENCY_TYPE_UNSPECIFIED",
        "DOCUMENT_INCONSISTENCY_TYPE_INVALID_DOCPROTO",
        "DOCUMENT_INCONSISTENCY_TYPE_MISMATCHED_METADATA",
        "DOCUMENT_INCONSISTENCY_TYPE_NO_PAGE_IMAGE",
    ]
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3RevisionRef(typing.TypedDict, total=False):
    latestProcessorVersion: str
    revisionCase: typing.Literal[
        "REVISION_CASE_UNSPECIFIED",
        "LATEST_HUMAN_REVIEW",
        "LATEST_TIMESTAMP",
        "BASE_OCR_REVISION",
    ]
    revisionId: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponse(
    typing.TypedDict, total=False
):
    sampleTestStatus: GoogleRpcStatus
    sampleTrainingStatus: GoogleRpcStatus
    selectedDocuments: _list[
        GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocument
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocument(
    typing.TypedDict, total=False
):
    documentId: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    testDatasetValidation: (
        GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation
    )
    trainingDatasetValidation: (
        GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation
    )

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation(
    typing.TypedDict, total=False
):
    datasetErrorCount: int
    datasetErrors: _list[GoogleRpcStatus]
    documentErrorCount: int
    documentErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponse(
    typing.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1BatchProcessMetadata(typing.TypedDict, total=False):
    createTime: str
    individualProcessStatuses: _list[
        GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatus
    ]
    state: typing.Literal[
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
    typing.TypedDict, total=False
):
    humanReviewStatus: GoogleCloudDocumentaiV1HumanReviewStatus
    inputGcsSource: str
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1BatchProcessResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1CommonOperationMetadata(typing.TypedDict, total=False):
    createTime: str
    resource: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DeleteProcessorMetadata(typing.TypedDict, total=False):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DeleteProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DeployProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DeployProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1DisableProcessorMetadata(typing.TypedDict, total=False):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1DisableProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1EnableProcessorMetadata(typing.TypedDict, total=False):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1EnableProcessorResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1EvaluateProcessorVersionResponse(
    typing.TypedDict, total=False
):
    evaluation: str

@typing.type_check_only
class GoogleCloudDocumentaiV1HumanReviewStatus(typing.TypedDict, total=False):
    humanReviewOperation: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SKIPPED", "VALIDATION_PASSED", "IN_PROGRESS", "ERROR"
    ]
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1ReviewDocumentOperationMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata
    questionId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1ReviewDocumentResponse(typing.TypedDict, total=False):
    gcsDestination: str
    rejectionReason: str
    state: typing.Literal["STATE_UNSPECIFIED", "REJECTED", "SUCCEEDED"]

@typing.type_check_only
class GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1TrainProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata
    testDatasetValidation: (
        GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidation
    )
    trainingDatasetValidation: (
        GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidation
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidation(
    typing.TypedDict, total=False
):
    datasetErrorCount: int
    datasetErrors: _list[GoogleRpcStatus]
    documentErrorCount: int
    documentErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDocumentaiV1TrainProcessorVersionResponse(
    typing.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1UndeployProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1UndeployProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1Barcode(typing.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponse(
    typing.TypedDict, total=False
):
    responses: _list[GoogleCloudDocumentaiV1beta1ProcessDocumentResponse]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1BoundingPoly(typing.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudDocumentaiV1beta1NormalizedVertex]
    vertices: _list[GoogleCloudDocumentaiV1beta1Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1Document(typing.TypedDict, total=False):
    chunkedDocument: GoogleCloudDocumentaiV1beta1DocumentChunkedDocument
    content: str
    documentLayout: GoogleCloudDocumentaiV1beta1DocumentDocumentLayout
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
class GoogleCloudDocumentaiV1beta1DocumentChunkedDocument(
    typing.TypedDict, total=False
):
    chunks: _list[GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunk]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunk(
    typing.TypedDict, total=False
):
    chunkId: str
    content: str
    pageFooters: _list[
        GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageFooter
    ]
    pageHeaders: _list[
        GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageHeader
    ]
    pageSpan: GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageSpan
    sourceBlockIds: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageFooter(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageHeader(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentChunkedDocumentChunkChunkPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayout(typing.TypedDict, total=False):
    blocks: _list[GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlock(
    typing.TypedDict, total=False
):
    blockId: str
    listBlock: GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock
    pageSpan: GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan
    tableBlock: GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock
    textBlock: GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock(
    typing.TypedDict, total=False
):
    listEntries: _list[
        GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry
    ]
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock(
    typing.TypedDict, total=False
):
    bodyRows: _list[
        GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]
    caption: str
    headerRows: _list[
        GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlock]
    colSpan: int
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow(
    typing.TypedDict, total=False
):
    cells: _list[
        GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta1DocumentDocumentLayoutDocumentLayoutBlock]
    text: str
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentEntity(typing.TypedDict, total=False):
    confidence: float
    id: str
    mentionId: str
    mentionText: str
    normalizedValue: GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValue
    pageAnchor: GoogleCloudDocumentaiV1beta1DocumentPageAnchor
    properties: _list[GoogleCloudDocumentaiV1beta1DocumentEntity]
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance
    redacted: bool
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValue(
    typing.TypedDict, total=False
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
class GoogleCloudDocumentaiV1beta1DocumentEntityRelation(typing.TypedDict, total=False):
    objectId: str
    relation: str
    subjectId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPage(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiV1beta1DocumentPageAnchor(typing.TypedDict, total=False):
    pageRefs: _list[GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRef(
    typing.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta1BoundingPoly
    confidence: float
    layoutId: str
    layoutType: typing.Literal[
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
class GoogleCloudDocumentaiV1beta1DocumentPageBlock(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcode(
    typing.TypedDict, total=False
):
    barcode: GoogleCloudDocumentaiV1beta1Barcode
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage(
    typing.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageDimension(typing.TypedDict, total=False):
    height: float
    unit: str
    width: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageFormField(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiV1beta1DocumentPageImage(typing.TypedDict, total=False):
    content: str
    height: int
    mimeType: str
    width: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScores(
    typing.TypedDict, total=False
):
    detectedDefects: _list[
        GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefect
    ]
    qualityScore: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefect(
    typing.TypedDict, total=False
):
    confidence: float
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageLayout(typing.TypedDict, total=False):
    boundingPoly: GoogleCloudDocumentaiV1beta1BoundingPoly
    confidence: float
    orientation: typing.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageLine(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageMatrix(typing.TypedDict, total=False):
    cols: int
    data: str
    rows: int
    type: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageParagraph(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageSymbol(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTable(typing.TypedDict, total=False):
    bodyRows: _list[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    headerRows: _list[GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell(
    typing.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTableTableRow(
    typing.TypedDict, total=False
):
    cells: _list[GoogleCloudDocumentaiV1beta1DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageToken(typing.TypedDict, total=False):
    detectedBreak: GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreak
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta1DocumentProvenance
    styleInfo: GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfo

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreak(
    typing.TypedDict, total=False
):
    type: typing.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfo(
    typing.TypedDict, total=False
):
    backgroundColor: GoogleTypeColor
    bold: bool
    fontSize: int
    fontType: str
    fontWeight: int
    handwritten: bool
    italic: bool
    letterSpacing: float
    pixelFontSize: float
    smallcaps: bool
    strikeout: bool
    subscript: bool
    superscript: bool
    textColor: GoogleTypeColor
    underlined: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentPageVisualElement(
    typing.TypedDict, total=False
):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta1DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentProvenance(typing.TypedDict, total=False):
    id: int
    parents: _list[GoogleCloudDocumentaiV1beta1DocumentProvenanceParent]
    revision: int
    type: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "UPDATE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
        "EVAL_SKIPPED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentProvenanceParent(
    typing.TypedDict, total=False
):
    id: int
    index: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentRevision(typing.TypedDict, total=False):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReview
    id: str
    parent: _list[int]
    parentIds: _list[str]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReview(
    typing.TypedDict, total=False
):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentShardInfo(typing.TypedDict, total=False):
    shardCount: str
    shardIndex: str
    textOffset: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentStyle(typing.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    color: GoogleTypeColor
    fontFamily: str
    fontSize: GoogleCloudDocumentaiV1beta1DocumentStyleFontSize
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor
    textDecoration: str
    textStyle: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentStyleFontSize(typing.TypedDict, total=False):
    size: float
    unit: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentTextAnchor(typing.TypedDict, total=False):
    content: str
    textSegments: _list[GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment(
    typing.TypedDict, total=False
):
    endIndex: str
    startIndex: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1DocumentTextChange(typing.TypedDict, total=False):
    changedText: str
    provenance: _list[GoogleCloudDocumentaiV1beta1DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta1DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1GcsDestination(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1GcsSource(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1InputConfig(typing.TypedDict, total=False):
    gcsSource: GoogleCloudDocumentaiV1beta1GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1NormalizedVertex(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1OperationMetadata(typing.TypedDict, total=False):
    createTime: str
    state: typing.Literal[
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
class GoogleCloudDocumentaiV1beta1OutputConfig(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudDocumentaiV1beta1GcsDestination
    pagesPerShard: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1ProcessDocumentResponse(
    typing.TypedDict, total=False
):
    inputConfig: GoogleCloudDocumentaiV1beta1InputConfig
    outputConfig: GoogleCloudDocumentaiV1beta1OutputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta1Vertex(typing.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2AutoMlParams(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2Barcode(typing.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2BatchProcessDocumentsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudDocumentaiV1beta2ProcessDocumentRequest]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponse(
    typing.TypedDict, total=False
):
    responses: _list[GoogleCloudDocumentaiV1beta2ProcessDocumentResponse]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2BoundingPoly(typing.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudDocumentaiV1beta2NormalizedVertex]
    vertices: _list[GoogleCloudDocumentaiV1beta2Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2Document(typing.TypedDict, total=False):
    chunkedDocument: GoogleCloudDocumentaiV1beta2DocumentChunkedDocument
    content: str
    documentLayout: GoogleCloudDocumentaiV1beta2DocumentDocumentLayout
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
class GoogleCloudDocumentaiV1beta2DocumentChunkedDocument(
    typing.TypedDict, total=False
):
    chunks: _list[GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunk]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunk(
    typing.TypedDict, total=False
):
    chunkId: str
    content: str
    pageFooters: _list[
        GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageFooter
    ]
    pageHeaders: _list[
        GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageHeader
    ]
    pageSpan: GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageSpan
    sourceBlockIds: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageFooter(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageHeader(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentChunkedDocumentChunkChunkPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayout(typing.TypedDict, total=False):
    blocks: _list[GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlock(
    typing.TypedDict, total=False
):
    blockId: str
    listBlock: GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock
    pageSpan: GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan
    tableBlock: GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock
    textBlock: GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock(
    typing.TypedDict, total=False
):
    listEntries: _list[
        GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry
    ]
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock(
    typing.TypedDict, total=False
):
    bodyRows: _list[
        GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]
    caption: str
    headerRows: _list[
        GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlock]
    colSpan: int
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow(
    typing.TypedDict, total=False
):
    cells: _list[
        GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta2DocumentDocumentLayoutDocumentLayoutBlock]
    text: str
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentEntity(typing.TypedDict, total=False):
    confidence: float
    id: str
    mentionId: str
    mentionText: str
    normalizedValue: GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValue
    pageAnchor: GoogleCloudDocumentaiV1beta2DocumentPageAnchor
    properties: _list[GoogleCloudDocumentaiV1beta2DocumentEntity]
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance
    redacted: bool
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValue(
    typing.TypedDict, total=False
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
class GoogleCloudDocumentaiV1beta2DocumentEntityRelation(typing.TypedDict, total=False):
    objectId: str
    relation: str
    subjectId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentLabel(typing.TypedDict, total=False):
    automlModel: str
    confidence: float
    name: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPage(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiV1beta2DocumentPageAnchor(typing.TypedDict, total=False):
    pageRefs: _list[GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRef(
    typing.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta2BoundingPoly
    confidence: float
    layoutId: str
    layoutType: typing.Literal[
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
class GoogleCloudDocumentaiV1beta2DocumentPageBlock(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcode(
    typing.TypedDict, total=False
):
    barcode: GoogleCloudDocumentaiV1beta2Barcode
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage(
    typing.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageDimension(typing.TypedDict, total=False):
    height: float
    unit: str
    width: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageFormField(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiV1beta2DocumentPageImage(typing.TypedDict, total=False):
    content: str
    height: int
    mimeType: str
    width: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScores(
    typing.TypedDict, total=False
):
    detectedDefects: _list[
        GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefect
    ]
    qualityScore: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefect(
    typing.TypedDict, total=False
):
    confidence: float
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageLayout(typing.TypedDict, total=False):
    boundingPoly: GoogleCloudDocumentaiV1beta2BoundingPoly
    confidence: float
    orientation: typing.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageLine(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageMatrix(typing.TypedDict, total=False):
    cols: int
    data: str
    rows: int
    type: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageParagraph(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageSymbol(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTable(typing.TypedDict, total=False):
    bodyRows: _list[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    headerRows: _list[GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell(
    typing.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTableTableRow(
    typing.TypedDict, total=False
):
    cells: _list[GoogleCloudDocumentaiV1beta2DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageToken(typing.TypedDict, total=False):
    detectedBreak: GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreak
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta2DocumentProvenance
    styleInfo: GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfo

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreak(
    typing.TypedDict, total=False
):
    type: typing.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfo(
    typing.TypedDict, total=False
):
    backgroundColor: GoogleTypeColor
    bold: bool
    fontSize: int
    fontType: str
    fontWeight: int
    handwritten: bool
    italic: bool
    letterSpacing: float
    pixelFontSize: float
    smallcaps: bool
    strikeout: bool
    subscript: bool
    superscript: bool
    textColor: GoogleTypeColor
    underlined: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentPageVisualElement(
    typing.TypedDict, total=False
):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta2DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentProvenance(typing.TypedDict, total=False):
    id: int
    parents: _list[GoogleCloudDocumentaiV1beta2DocumentProvenanceParent]
    revision: int
    type: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "UPDATE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
        "EVAL_SKIPPED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentProvenanceParent(
    typing.TypedDict, total=False
):
    id: int
    index: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentRevision(typing.TypedDict, total=False):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReview
    id: str
    parent: _list[int]
    parentIds: _list[str]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReview(
    typing.TypedDict, total=False
):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentShardInfo(typing.TypedDict, total=False):
    shardCount: str
    shardIndex: str
    textOffset: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentStyle(typing.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    color: GoogleTypeColor
    fontFamily: str
    fontSize: GoogleCloudDocumentaiV1beta2DocumentStyleFontSize
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor
    textDecoration: str
    textStyle: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentStyleFontSize(typing.TypedDict, total=False):
    size: float
    unit: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentTextAnchor(typing.TypedDict, total=False):
    content: str
    textSegments: _list[GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegment]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegment(
    typing.TypedDict, total=False
):
    endIndex: str
    startIndex: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentTextChange(typing.TypedDict, total=False):
    changedText: str
    provenance: _list[GoogleCloudDocumentaiV1beta2DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta2DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2EntityExtractionParams(typing.TypedDict, total=False):
    enabled: bool
    modelVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2FormExtractionParams(typing.TypedDict, total=False):
    enabled: bool
    keyValuePairHints: _list[GoogleCloudDocumentaiV1beta2KeyValuePairHint]
    modelVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2GcsDestination(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2GcsSource(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2InputConfig(typing.TypedDict, total=False):
    contents: str
    gcsSource: GoogleCloudDocumentaiV1beta2GcsSource
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2KeyValuePairHint(typing.TypedDict, total=False):
    key: str
    valueTypes: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2NormalizedVertex(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2OcrParams(typing.TypedDict, total=False):
    languageHints: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2OperationMetadata(typing.TypedDict, total=False):
    createTime: str
    state: typing.Literal[
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
class GoogleCloudDocumentaiV1beta2OutputConfig(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudDocumentaiV1beta2GcsDestination
    pagesPerShard: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2ProcessDocumentRequest(typing.TypedDict, total=False):
    automlParams: GoogleCloudDocumentaiV1beta2AutoMlParams
    documentType: str
    entityExtractionParams: GoogleCloudDocumentaiV1beta2EntityExtractionParams
    formExtractionParams: GoogleCloudDocumentaiV1beta2FormExtractionParams
    inputConfig: GoogleCloudDocumentaiV1beta2InputConfig
    ocrParams: GoogleCloudDocumentaiV1beta2OcrParams
    outputConfig: GoogleCloudDocumentaiV1beta2OutputConfig
    parent: str
    tableExtractionParams: GoogleCloudDocumentaiV1beta2TableExtractionParams

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2ProcessDocumentResponse(
    typing.TypedDict, total=False
):
    inputConfig: GoogleCloudDocumentaiV1beta2InputConfig
    outputConfig: GoogleCloudDocumentaiV1beta2OutputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2TableBoundHint(typing.TypedDict, total=False):
    boundingBox: GoogleCloudDocumentaiV1beta2BoundingPoly
    pageNumber: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2TableExtractionParams(typing.TypedDict, total=False):
    enabled: bool
    headerHints: _list[str]
    modelVersion: str
    tableBoundHints: _list[GoogleCloudDocumentaiV1beta2TableBoundHint]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2Vertex(typing.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata
    errorDocumentCount: int
    individualBatchDeleteStatuses: _list[
        GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus(
    typing.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiV1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessMetadata(typing.TypedDict, total=False):
    createTime: str
    individualProcessStatuses: _list[
        GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus
    ]
    state: typing.Literal[
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
    typing.TypedDict, total=False
):
    humanReviewOperation: str
    humanReviewStatus: GoogleCloudDocumentaiV1beta3HumanReviewStatus
    inputGcsSource: str
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3CommonOperationMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    resource: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Dataset(typing.TypedDict, total=False):
    documentWarehouseConfig: GoogleCloudDocumentaiV1beta3DatasetDocumentWarehouseConfig
    gcsManagedConfig: GoogleCloudDocumentaiV1beta3DatasetGCSManagedConfig
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    spannerIndexingConfig: GoogleCloudDocumentaiV1beta3DatasetSpannerIndexingConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED", "UNINITIALIZED", "INITIALIZING", "INITIALIZED"
    ]
    unmanagedDatasetConfig: GoogleCloudDocumentaiV1beta3DatasetUnmanagedDatasetConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetDocumentWarehouseConfig(
    typing.TypedDict, total=False
):
    collection: str
    schema: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetGCSManagedConfig(
    typing.TypedDict, total=False
):
    gcsPrefix: GoogleCloudDocumentaiV1beta3GcsPrefix

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetSpannerIndexingConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetUnmanagedDatasetConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeleteProcessorMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DisableProcessorMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DisableProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentId(typing.TypedDict, total=False):
    gcsManagedDocId: GoogleCloudDocumentaiV1beta3DocumentIdGCSManagedDocumentId
    revisionRef: GoogleCloudDocumentaiV1beta3RevisionRef
    unmanagedDocId: GoogleCloudDocumentaiV1beta3DocumentIdUnmanagedDocumentId

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentIdGCSManagedDocumentId(
    typing.TypedDict, total=False
):
    cwDocId: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentIdUnmanagedDocumentId(
    typing.TypedDict, total=False
):
    docId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponse(
    typing.TypedDict, total=False
):
    evaluation: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsPrefix(typing.TypedDict, total=False):
    gcsUriPrefix: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3HumanReviewStatus(typing.TypedDict, total=False):
    humanReviewOperation: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SKIPPED", "VALIDATION_PASSED", "IN_PROGRESS", "ERROR"
    ]
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata
    importConfigValidationResults: _list[
        GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataImportConfigValidationResult
    ]
    individualImportStatuses: _list[
        GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataIndividualImportStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataImportConfigValidationResult(
    typing.TypedDict, total=False
):
    inputGcsSource: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataIndividualImportStatus(
    typing.TypedDict, total=False
):
    inputGcsSource: str
    outputDocumentId: GoogleCloudDocumentaiV1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponse(
    typing.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata
    createTime: str
    questionId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ReviewDocumentResponse(typing.TypedDict, total=False):
    gcsDestination: str
    rejectionReason: str
    state: typing.Literal["STATE_UNSPECIFIED", "REJECTED", "SUCCEEDED"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3RevisionRef(typing.TypedDict, total=False):
    latestProcessorVersion: str
    revisionCase: typing.Literal[
        "REVISION_CASE_UNSPECIFIED",
        "LATEST_HUMAN_REVIEW",
        "LATEST_TIMESTAMP",
        "BASE_OCR_REVISION",
    ]
    revisionId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata
    testDatasetValidation: (
        GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidation
    )
    trainingDatasetValidation: (
        GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidation
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidation(
    typing.TypedDict, total=False
):
    datasetErrorCount: int
    datasetErrors: _list[GoogleRpcStatus]
    documentErrorCount: int
    documentErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponse(
    typing.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3UpdateDatasetOperationMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeColor(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeDateTime(typing.TypedDict, total=False):
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
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class GoogleTypePostalAddress(typing.TypedDict, total=False):
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
class GoogleTypeTimeZone(typing.TypedDict, total=False):
    id: str
    version: str
