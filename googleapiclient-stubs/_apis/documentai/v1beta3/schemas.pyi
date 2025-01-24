import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    individualAutoLabelStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatus(
    typing_extensions.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

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
class GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata
    individualBatchUpdateStatuses: _list[
        GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsMetadataIndividualBatchUpdateStatus
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsMetadataIndividualBatchUpdateStatus(
    typing_extensions.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3BatchUpdateDocumentsResponse(
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
    revisionRef: GoogleCloudDocumentaiUiv1beta3RevisionRef
    unmanagedDocId: GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentId

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentId(
    typing_extensions.TypedDict, total=False
):
    cwDocId: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentId(
    typing_extensions.TypedDict, total=False
):
    docId: str

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
    outputDocumentId: GoogleCloudDocumentaiUiv1beta3DocumentId
    outputGcsDestination: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    processorVersion: str

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
class GoogleCloudDocumentaiUiv1beta3RevisionRef(
    typing_extensions.TypedDict, total=False
):
    latestProcessorVersion: str
    revisionCase: typing_extensions.Literal[
        "REVISION_CASE_UNSPECIFIED",
        "LATEST_HUMAN_REVIEW",
        "LATEST_TIMESTAMP",
        "BASE_OCR_REVISION",
    ]
    revisionId: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    sampleTestStatus: GoogleRpcStatus
    sampleTrainingStatus: GoogleRpcStatus
    selectedDocuments: _list[
        GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocument
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocument(
    typing_extensions.TypedDict, total=False
):
    documentId: str

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
    testDatasetValidation: (
        GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation
    )
    trainingDatasetValidation: (
        GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation
    )

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
class GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1EvaluateProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    evaluation: str

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
class GoogleCloudDocumentaiV1TrainProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    datasetErrorCount: int
    datasetErrors: _list[GoogleRpcStatus]
    documentErrorCount: int
    documentErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDocumentaiV1TrainProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    processorVersion: str

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
class GoogleCloudDocumentaiV1beta3Barcode(typing_extensions.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDatasetDocuments(
    typing_extensions.TypedDict, total=False
):
    filter: str
    individualDocumentIds: (
        GoogleCloudDocumentaiV1beta3BatchDatasetDocumentsIndividualDocumentIds
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDatasetDocumentsIndividualDocumentIds(
    typing_extensions.TypedDict, total=False
):
    documentIds: _list[GoogleCloudDocumentaiV1beta3DocumentId]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata
    errorDocumentCount: int
    individualBatchDeleteStatuses: _list[
        GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus
    ]
    totalDocumentCount: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatus(
    typing_extensions.TypedDict, total=False
):
    documentId: GoogleCloudDocumentaiV1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    datasetDocuments: GoogleCloudDocumentaiV1beta3BatchDatasetDocuments

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

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
    labels: dict[str, typing.Any]
    outputConfig: GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchOutputConfig
    processOptions: GoogleCloudDocumentaiV1beta3ProcessOptions
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
class GoogleCloudDocumentaiV1beta3Dataset(typing_extensions.TypedDict, total=False):
    documentWarehouseConfig: GoogleCloudDocumentaiV1beta3DatasetDocumentWarehouseConfig
    gcsManagedConfig: GoogleCloudDocumentaiV1beta3DatasetGCSManagedConfig
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    spannerIndexingConfig: GoogleCloudDocumentaiV1beta3DatasetSpannerIndexingConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNINITIALIZED", "INITIALIZING", "INITIALIZED"
    ]
    unmanagedDatasetConfig: GoogleCloudDocumentaiV1beta3DatasetUnmanagedDatasetConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetDocumentWarehouseConfig(
    typing_extensions.TypedDict, total=False
):
    collection: str
    schema: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetGCSManagedConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: GoogleCloudDocumentaiV1beta3GcsPrefix

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetSchema(
    typing_extensions.TypedDict, total=False
):
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetSpannerIndexingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetUnmanagedDatasetConfig(
    typing_extensions.TypedDict, total=False
): ...

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
    chunkedDocument: GoogleCloudDocumentaiV1beta3DocumentChunkedDocument
    content: str
    documentLayout: GoogleCloudDocumentaiV1beta3DocumentDocumentLayout
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
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocument(
    typing_extensions.TypedDict, total=False
):
    chunks: _list[GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunk]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunk(
    typing_extensions.TypedDict, total=False
):
    chunkId: str
    content: str
    pageFooters: _list[
        GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageFooter
    ]
    pageHeaders: _list[
        GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageHeader
    ]
    pageSpan: GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageSpan
    sourceBlockIds: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageFooter(
    typing_extensions.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageHeader(
    typing_extensions.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageSpan(
    typing_extensions.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayout(
    typing_extensions.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock(
    typing_extensions.TypedDict, total=False
):
    blockId: str
    listBlock: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock
    pageSpan: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan
    tableBlock: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock
    textBlock: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock(
    typing_extensions.TypedDict, total=False
):
    listEntries: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry
    ]
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry(
    typing_extensions.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan(
    typing_extensions.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock(
    typing_extensions.TypedDict, total=False
):
    bodyRows: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]
    caption: str
    headerRows: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell(
    typing_extensions.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]
    colSpan: int
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow(
    typing_extensions.TypedDict, total=False
):
    cells: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock(
    typing_extensions.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]
    text: str
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntity(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    id: str
    mentionId: str
    mentionText: str
    normalizedValue: GoogleCloudDocumentaiV1beta3DocumentEntityNormalizedValue
    pageAnchor: GoogleCloudDocumentaiV1beta3DocumentPageAnchor
    properties: _list[GoogleCloudDocumentaiV1beta3DocumentEntity]
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance
    redacted: bool
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor
    type: str

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
class GoogleCloudDocumentaiV1beta3DocumentId(typing_extensions.TypedDict, total=False):
    gcsManagedDocId: GoogleCloudDocumentaiV1beta3DocumentIdGCSManagedDocumentId
    revisionRef: GoogleCloudDocumentaiV1beta3RevisionRef
    unmanagedDocId: GoogleCloudDocumentaiV1beta3DocumentIdUnmanagedDocumentId

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentIdGCSManagedDocumentId(
    typing_extensions.TypedDict, total=False
):
    cwDocId: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentIdUnmanagedDocumentId(
    typing_extensions.TypedDict, total=False
):
    docId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    datasetType: typing_extensions.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    displayName: str
    documentId: GoogleCloudDocumentaiV1beta3DocumentId
    labelingState: typing_extensions.Literal[
        "DOCUMENT_LABELING_STATE_UNSPECIFIED",
        "DOCUMENT_LABELED",
        "DOCUMENT_UNLABELED",
        "DOCUMENT_AUTO_LABELED",
    ]
    pageCount: int

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
    shardingConfig: (
        GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfigShardingConfig
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfigShardingConfig(
    typing_extensions.TypedDict, total=False
):
    pagesOverlap: int
    pagesPerShard: int

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
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

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
    styleInfo: GoogleCloudDocumentaiV1beta3DocumentPageTokenStyleInfo

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTokenDetectedBreak(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTokenStyleInfo(
    typing_extensions.TypedDict, total=False
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
        "UPDATE",
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
    description: str
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
    description: str
    displayName: str
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
    inactive: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionRequest(
    typing_extensions.TypedDict, total=False
):
    evaluationDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    evaluation: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Evaluation(typing_extensions.TypedDict, total=False):
    allEntitiesMetrics: GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics
    createTime: str
    documentCounters: GoogleCloudDocumentaiV1beta3EvaluationCounters
    entityMetrics: dict[str, typing.Any]
    kmsKeyName: str
    kmsKeyVersionName: str
    name: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceLevel: float
    metrics: GoogleCloudDocumentaiV1beta3EvaluationMetrics

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationCounters(
    typing_extensions.TypedDict, total=False
):
    evaluatedDocumentsCount: int
    failedDocumentsCount: int
    inputDocumentsCount: int
    invalidDocumentsCount: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    f1Score: float
    falseNegativesCount: int
    falsePositivesCount: int
    groundTruthDocumentCount: int
    groundTruthOccurrencesCount: int
    precision: float
    predictedDocumentCount: int
    predictedOccurrencesCount: int
    recall: float
    totalDocumentsCount: int
    truePositivesCount: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    auprc: float
    auprcExact: float
    confidenceLevelMetrics: _list[
        GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics
    ]
    confidenceLevelMetricsExact: _list[
        GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics
    ]
    estimatedCalibrationError: float
    estimatedCalibrationErrorExact: float
    metricsType: typing_extensions.Literal["METRICS_TYPE_UNSPECIFIED", "AGGREGATE"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationReference(
    typing_extensions.TypedDict, total=False
):
    aggregateMetrics: GoogleCloudDocumentaiV1beta3EvaluationMetrics
    aggregateMetricsExact: GoogleCloudDocumentaiV1beta3EvaluationMetrics
    evaluation: str
    operation: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponse(
    typing_extensions.TypedDict, total=False
):
    processorTypes: _list[GoogleCloudDocumentaiV1beta3ProcessorType]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3FieldExtractionMetadata(
    typing_extensions.TypedDict, total=False
):
    summaryOptions: GoogleCloudDocumentaiV1beta3SummaryOptions

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
class GoogleCloudDocumentaiV1beta3GetDocumentResponse(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDocumentaiV1beta3Document

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
class GoogleCloudDocumentaiV1beta3ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    inputGcsSource: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataIndividualImportStatus(
    typing_extensions.TypedDict, total=False
):
    inputGcsSource: str
    outputDocumentId: GoogleCloudDocumentaiV1beta3DocumentId
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    batchDocumentsImportConfigs: _list[
        GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfig
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfig(
    typing_extensions.TypedDict, total=False
):
    autoSplitConfig: GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfigAutoSplitConfig
    batchInputConfig: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig
    datasetSplit: typing_extensions.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfigAutoSplitConfig(
    typing_extensions.TypedDict, total=False
):
    trainingSplitRatio: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequest(
    typing_extensions.TypedDict, total=False
):
    externalProcessorVersionSource: GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequestExternalProcessorVersionSource
    processorVersionSource: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequestExternalProcessorVersionSource(
    typing_extensions.TypedDict, total=False
):
    processorVersion: str
    serviceEndpoint: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str
    returnTotalSize: bool
    skip: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    documentMetadata: _list[GoogleCloudDocumentaiV1beta3DocumentMetadata]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListEvaluationsResponse(
    typing_extensions.TypedDict, total=False
):
    evaluations: _list[GoogleCloudDocumentaiV1beta3Evaluation]
    nextPageToken: str

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
class GoogleCloudDocumentaiV1beta3OcrConfig(typing_extensions.TypedDict, total=False):
    advancedOcrOptions: _list[str]
    computeStyleInfo: bool
    disableCharacterBoxesDetection: bool
    enableImageQualityScores: bool
    enableNativePdfParsing: bool
    enableSymbol: bool
    hints: GoogleCloudDocumentaiV1beta3OcrConfigHints
    premiumFeatures: GoogleCloudDocumentaiV1beta3OcrConfigPremiumFeatures

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3OcrConfigHints(
    typing_extensions.TypedDict, total=False
):
    languageHints: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3OcrConfigPremiumFeatures(
    typing_extensions.TypedDict, total=False
):
    computeStyleInfo: bool
    enableMathOcr: bool
    enableSelectionMarkDetection: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessOptions(
    typing_extensions.TypedDict, total=False
):
    fromEnd: int
    fromStart: int
    individualPageSelector: (
        GoogleCloudDocumentaiV1beta3ProcessOptionsIndividualPageSelector
    )
    layoutConfig: GoogleCloudDocumentaiV1beta3ProcessOptionsLayoutConfig
    ocrConfig: GoogleCloudDocumentaiV1beta3OcrConfig
    schemaOverride: GoogleCloudDocumentaiV1beta3DocumentSchema

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessOptionsIndividualPageSelector(
    typing_extensions.TypedDict, total=False
):
    pages: _list[int]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessOptionsLayoutConfig(
    typing_extensions.TypedDict, total=False
):
    chunkingConfig: GoogleCloudDocumentaiV1beta3ProcessOptionsLayoutConfigChunkingConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessOptionsLayoutConfigChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    breakpointPercentileThreshold: int
    chunkSize: int
    includeAncestorHeadings: bool
    semanticChunkingGroupSize: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessRequest(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDocumentaiV1beta3Document
    fieldMask: str
    gcsDocument: GoogleCloudDocumentaiV1beta3GcsDocument
    imagelessMode: bool
    inlineDocument: GoogleCloudDocumentaiV1beta3Document
    labels: dict[str, typing.Any]
    processOptions: GoogleCloudDocumentaiV1beta3ProcessOptions
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
    processorVersionAliases: _list[GoogleCloudDocumentaiV1beta3ProcessorVersionAlias]
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    sampleDocumentUris: _list[str]
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
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    genAiModelInfo: GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfo
    googleManaged: bool
    kmsKeyName: str
    kmsKeyVersionName: str
    latestEvaluation: GoogleCloudDocumentaiV1beta3EvaluationReference
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED", "MODEL_TYPE_GENERATIVE", "MODEL_TYPE_CUSTOM"
    ]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "DEPLOYED",
        "DEPLOYING",
        "UNDEPLOYED",
        "UNDEPLOYING",
        "CREATING",
        "DELETING",
        "FAILED",
        "IMPORTING",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionAlias(
    typing_extensions.TypedDict, total=False
):
    alias: str
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo(
    typing_extensions.TypedDict, total=False
):
    deprecationTime: str
    replacementProcessorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfo(
    typing_extensions.TypedDict, total=False
):
    customGenAiModelInfo: (
        GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoCustomGenAiModelInfo
    )
    foundationGenAiModelInfo: GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoFoundationGenAiModelInfo

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoCustomGenAiModelInfo(
    typing_extensions.TypedDict, total=False
):
    baseProcessorVersionId: str
    customModelType: typing_extensions.Literal[
        "CUSTOM_MODEL_TYPE_UNSPECIFIED", "VERSIONED_FOUNDATION", "FINE_TUNED"
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoFoundationGenAiModelInfo(
    typing_extensions.TypedDict, total=False
):
    finetuningAllowed: bool
    minTrainLabeledDocuments: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3PropertyMetadata(
    typing_extensions.TypedDict, total=False
):
    fieldExtractionMetadata: GoogleCloudDocumentaiV1beta3FieldExtractionMetadata
    inactive: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3RawDocument(typing_extensions.TypedDict, total=False):
    content: str
    displayName: str
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
class GoogleCloudDocumentaiV1beta3RevisionRef(typing_extensions.TypedDict, total=False):
    latestProcessorVersion: str
    revisionCase: typing_extensions.Literal[
        "REVISION_CASE_UNSPECIFIED",
        "LATEST_HUMAN_REVIEW",
        "LATEST_TIMESTAMP",
        "BASE_OCR_REVISION",
    ]
    revisionId: str

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
class GoogleCloudDocumentaiV1beta3SummaryOptions(
    typing_extensions.TypedDict, total=False
):
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "PARAGRAPH", "BULLETS"]
    length: typing_extensions.Literal[
        "LENGTH_UNSPECIFIED", "BRIEF", "MODERATE", "COMPREHENSIVE"
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadata(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    datasetErrorCount: int
    datasetErrors: _list[GoogleRpcStatus]
    documentErrorCount: int
    documentErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequest(
    typing_extensions.TypedDict, total=False
):
    baseProcessorVersion: str
    customDocumentExtractionOptions: GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestCustomDocumentExtractionOptions
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    foundationModelTuningOptions: GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestFoundationModelTuningOptions
    inputData: GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestInputData
    processorVersion: GoogleCloudDocumentaiV1beta3ProcessorVersion

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestCustomDocumentExtractionOptions(
    typing_extensions.TypedDict, total=False
):
    trainingMethod: typing_extensions.Literal[
        "TRAINING_METHOD_UNSPECIFIED", "MODEL_BASED", "TEMPLATE_BASED"
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestFoundationModelTuningOptions(
    typing_extensions.TypedDict, total=False
):
    learningRateMultiplier: float
    trainSteps: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestInputData(
    typing_extensions.TypedDict, total=False
):
    testDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig
    trainingDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponse(
    typing_extensions.TypedDict, total=False
):
    processorVersion: str

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
class GoogleCloudDocumentaiV1beta3UpdateDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

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
