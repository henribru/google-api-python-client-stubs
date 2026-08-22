import typing

_list = list

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInput(
    typing.TypedDict, total=False
):
    validationRules: _list[
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRule
    ]

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRule(
    typing.TypedDict, total=False
):
    childAlignmentRule: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleChildAlignmentRule
    description: str
    entityAlignmentRule: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleEntityAlignmentRule
    fieldOccurrences: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFieldOccurrences
    fieldRegex: (
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFieldRegex
    )
    formValidation: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFormValidation
    name: str
    ruleId: str

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleAlignmentRule(
    typing.TypedDict, total=False
):
    alignmentType: typing.Literal[
        "ALIGNMENT_TYPE_UNSPECIFIED",
        "ALIGNMENT_TYPE_HORIZONTAL",
        "ALIGNMENT_TYPE_VERTICAL",
    ]
    tolerance: float

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleChildAlignmentRule(
    typing.TypedDict, total=False
):
    alignmentRule: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleAlignmentRule
    childFields: _list[
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleField
    ]
    parentField: (
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleField
    )

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleConstant(
    typing.TypedDict, total=False
):
    floatValue: float

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleEntityAlignmentRule(
    typing.TypedDict, total=False
):
    alignmentRule: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleAlignmentRule
    fields: _list[
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleField
    ]

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleField(
    typing.TypedDict, total=False
):
    defaultValue: (
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleConstant
    )
    fieldName: str

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFieldOccurrences(
    typing.TypedDict, total=False
):
    field: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleField
    maxOccurrences: int
    minOccurrences: int

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFieldRegex(
    typing.TypedDict, total=False
):
    field: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleField
    pattern: str

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFormValidation(
    typing.TypedDict, total=False
):
    leftOperand: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFormValidationOperation
    rightOperand: CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFormValidationOperation
    validationOperator: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "OPERATION_TYPE_EQ",
        "OPERATION_TYPE_NE",
        "OPERATION_TYPE_LT",
        "OPERATION_TYPE_LE",
        "OPERATION_TYPE_GT",
        "OPERATION_TYPE_GE",
    ]

@typing.type_check_only
class CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFormValidationOperation(
    typing.TypedDict, total=False
):
    constants: _list[
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleConstant
    ]
    fields: _list[
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleField
    ]
    operationType: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "OPERATION_TYPE_SUM",
        "OPERATION_TYPE_SUB",
        "OPERATION_TYPE_MUL",
        "OPERATION_TYPE_DIV",
        "OPERATION_TYPE_MAX",
        "OPERATION_TYPE_MIN",
        "OPERATION_TYPE_ABS",
        "OPERATION_TYPE_UNIQUE",
        "OPERATION_TYPE_COUNT",
    ]
    operations: _list[
        CloudAiDocumentaiLabHifiaToolsValidationValidatorInputValidationRuleFormValidationOperation
    ]

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
class GoogleCloudDocumentaiUiv1beta3DocumentSchema(typing.TypedDict, total=False):
    description: str
    displayName: str
    documentPrompt: str
    entityTypes: _list[GoogleCloudDocumentaiUiv1beta3DocumentSchemaEntityType]
    metadata: GoogleCloudDocumentaiUiv1beta3DocumentSchemaMetadata

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentSchemaEntityType(
    typing.TypedDict, total=False
):
    baseTypes: _list[str]
    description: str
    displayName: str
    entityTypeMetadata: GoogleCloudDocumentaiUiv1beta3EntityTypeMetadata
    enumValues: GoogleCloudDocumentaiUiv1beta3DocumentSchemaEntityTypeEnumValues
    name: str
    properties: _list[GoogleCloudDocumentaiUiv1beta3DocumentSchemaEntityTypeProperty]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentSchemaEntityTypeEnumValues(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentSchemaEntityTypeProperty(
    typing.TypedDict, total=False
):
    description: str
    displayName: str
    method: typing.Literal["METHOD_UNSPECIFIED", "EXTRACT", "DERIVE", "RELAXED_EXTRACT"]
    name: str
    occurrenceType: typing.Literal[
        "OCCURRENCE_TYPE_UNSPECIFIED",
        "OPTIONAL_ONCE",
        "OPTIONAL_MULTIPLE",
        "REQUIRED_ONCE",
        "REQUIRED_MULTIPLE",
    ]
    propertyMetadata: GoogleCloudDocumentaiUiv1beta3PropertyMetadata
    valueType: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3DocumentSchemaMetadata(
    typing.TypedDict, total=False
):
    documentAllowMultipleLabels: bool
    documentSplitter: bool
    prefixedNamingOnProperties: bool
    skipNamingValidation: bool

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
class GoogleCloudDocumentaiUiv1beta3EntityTypeMetadata(typing.TypedDict, total=False):
    fieldTierMetadata: GoogleCloudDocumentaiUiv1beta3FieldTierMetadata
    humanReviewLabelingMetadata: (
        GoogleCloudDocumentaiUiv1beta3HumanReviewLabelingMetadata
    )
    humanReviewMetadata: GoogleCloudDocumentaiUiv1beta3HumanReviewValidationMetadata
    inactive: bool
    schemaEditabilityMetadata: GoogleCloudDocumentaiUiv1beta3SchemaEditabilityMetadata
    schemaInferenceMetadata: GoogleCloudDocumentaiUiv1beta3SchemaInferenceMetadata

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
class GoogleCloudDocumentaiUiv1beta3EvaluationMetrics(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiUiv1beta3EvaluationReference(typing.TypedDict, total=False):
    aggregateMetrics: GoogleCloudDocumentaiUiv1beta3EvaluationMetrics
    aggregateMetricsExact: GoogleCloudDocumentaiUiv1beta3EvaluationMetrics
    evaluation: str
    operation: str

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
class GoogleCloudDocumentaiUiv1beta3FieldExtractionMetadata(
    typing.TypedDict, total=False
):
    entityQuery: GoogleCloudDocumentaiUiv1beta3FieldExtractionMetadataEntityQuery
    summaryOptions: GoogleCloudDocumentaiUiv1beta3SummaryOptions

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3FieldExtractionMetadataEntityQuery(
    typing.TypedDict, total=False
):
    userEntityQuery: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3FieldTierMetadata(typing.TypedDict, total=False):
    tierLevel: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3HumanReviewLabelingMetadata(
    typing.TypedDict, total=False
):
    enableNormalizationEditing: bool

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3HumanReviewValidationMetadata(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    enableValidation: bool

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
class GoogleCloudDocumentaiUiv1beta3Processor(typing.TypedDict, total=False):
    activeSchemaVersion: str
    createTime: str
    defaultProcessorVersion: str
    displayName: str
    kmsKeyName: str
    name: str
    processEndpoint: str
    processorVersionAliases: _list[GoogleCloudDocumentaiUiv1beta3ProcessorVersionAlias]
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
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
class GoogleCloudDocumentaiUiv1beta3ProcessorVersion(typing.TypedDict, total=False):
    createTime: str
    deploymentAllowed: bool
    deprecationInfo: GoogleCloudDocumentaiUiv1beta3ProcessorVersionDeprecationInfo
    displayName: str
    documentSchema: GoogleCloudDocumentaiUiv1beta3DocumentSchema
    genAiModelInfo: GoogleCloudDocumentaiUiv1beta3ProcessorVersionGenAiModelInfo
    googleManaged: bool
    kmsKeyName: str
    kmsKeyVersionName: str
    latestEvaluation: GoogleCloudDocumentaiUiv1beta3EvaluationReference
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED", "MODEL_TYPE_GENERATIVE", "MODEL_TYPE_CUSTOM"
    ]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    schema: GoogleCloudDocumentaiUiv1beta3Schema
    state: typing.Literal[
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
class GoogleCloudDocumentaiUiv1beta3ProcessorVersionAlias(
    typing.TypedDict, total=False
):
    alias: str
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ProcessorVersionDeprecationInfo(
    typing.TypedDict, total=False
):
    deprecationTime: str
    replacementProcessorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ProcessorVersionGenAiModelInfo(
    typing.TypedDict, total=False
):
    customGenAiModelInfo: (
        GoogleCloudDocumentaiUiv1beta3ProcessorVersionGenAiModelInfoCustomGenAiModelInfo
    )
    foundationGenAiModelInfo: GoogleCloudDocumentaiUiv1beta3ProcessorVersionGenAiModelInfoFoundationGenAiModelInfo

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ProcessorVersionGenAiModelInfoCustomGenAiModelInfo(
    typing.TypedDict, total=False
):
    baseProcessorVersionId: str
    customModelType: typing.Literal[
        "CUSTOM_MODEL_TYPE_UNSPECIFIED", "VERSIONED_FOUNDATION", "FINE_TUNED"
    ]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3ProcessorVersionGenAiModelInfoFoundationGenAiModelInfo(
    typing.TypedDict, total=False
):
    finetuningAllowed: bool
    minTrainLabeledDocuments: int

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3PropertyMetadata(typing.TypedDict, total=False):
    fieldExtractionMetadata: GoogleCloudDocumentaiUiv1beta3FieldExtractionMetadata
    fieldTierMetadata: GoogleCloudDocumentaiUiv1beta3FieldTierMetadata
    humanReviewLabelingMetadata: (
        GoogleCloudDocumentaiUiv1beta3HumanReviewLabelingMetadata
    )
    humanReviewMetadata: GoogleCloudDocumentaiUiv1beta3HumanReviewValidationMetadata
    inactive: bool
    schemaEditabilityMetadata: GoogleCloudDocumentaiUiv1beta3SchemaEditabilityMetadata
    schemaInferenceMetadata: GoogleCloudDocumentaiUiv1beta3SchemaInferenceMetadata

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
class GoogleCloudDocumentaiUiv1beta3Schema(typing.TypedDict, total=False):
    description: str
    displayName: str
    entityTypes: _list[GoogleCloudDocumentaiUiv1beta3SchemaEntityType]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SchemaEditabilityMetadata(
    typing.TypedDict, total=False
):
    editable: bool
    processorVersions: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SchemaEntityType(typing.TypedDict, total=False):
    baseType: str
    description: str
    enumValues: _list[str]
    hide: bool
    method: typing.Literal["METHOD_UNSPECIFIED", "EXTRACT", "DERIVE", "RELAXED_EXTRACT"]
    occurrenceType: typing.Literal[
        "OCCURRENCE_TYPE_UNSPECIFIED",
        "OPTIONAL_ONCE",
        "OPTIONAL_MULTIPLE",
        "REQUIRED_ONCE",
        "REQUIRED_MULTIPLE",
    ]
    properties: _list[GoogleCloudDocumentaiUiv1beta3SchemaEntityType]
    source: typing.Literal["SOURCE_UNSPECIFIED", "PREDEFINED", "USER_INPUT"]
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiUiv1beta3SchemaInferenceMetadata(
    typing.TypedDict, total=False
):
    inferred: bool

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
class GoogleCloudDocumentaiUiv1beta3SummaryOptions(typing.TypedDict, total=False):
    format: typing.Literal["FORMAT_UNSPECIFIED", "PARAGRAPH", "BULLETS"]
    length: typing.Literal["LENGTH_UNSPECIFIED", "BRIEF", "MODERATE", "COMPREHENSIVE"]

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
class GoogleCloudDocumentaiUiv1beta3UpdateProcessorVersionMetadata(
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
class GoogleCloudDocumentaiV1beta3Barcode(typing.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDatasetDocuments(typing.TypedDict, total=False):
    filter: str
    individualDocumentIds: (
        GoogleCloudDocumentaiV1beta3BatchDatasetDocumentsIndividualDocumentIds
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDatasetDocumentsIndividualDocumentIds(
    typing.TypedDict, total=False
):
    documentIds: _list[GoogleCloudDocumentaiV1beta3DocumentId]

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
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsRequest(
    typing.TypedDict, total=False
):
    datasetDocuments: GoogleCloudDocumentaiV1beta3BatchDatasetDocuments

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig(
    typing.TypedDict, total=False
):
    gcsDocuments: GoogleCloudDocumentaiV1beta3GcsDocuments
    gcsPrefix: GoogleCloudDocumentaiV1beta3GcsPrefix

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
class GoogleCloudDocumentaiV1beta3BatchProcessRequest(typing.TypedDict, total=False):
    documentOutputConfig: GoogleCloudDocumentaiV1beta3DocumentOutputConfig
    inputConfigs: _list[GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchInputConfig]
    inputDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig
    labels: dict[str, typing.Any]
    outputConfig: GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchOutputConfig
    processOptions: GoogleCloudDocumentaiV1beta3ProcessOptions
    skipHumanReview: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchInputConfig(
    typing.TypedDict, total=False
):
    gcsSource: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchOutputConfig(
    typing.TypedDict, total=False
):
    gcsDestination: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BatchProcessResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3BoundingPoly(typing.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudDocumentaiV1beta3NormalizedVertex]
    vertices: _list[GoogleCloudDocumentaiV1beta3Vertex]

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
class GoogleCloudDocumentaiV1beta3DatasetSchema(typing.TypedDict, total=False):
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool

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
class GoogleCloudDocumentaiV1beta3DeployProcessorVersionRequest(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDocumentaiV1beta3DisableProcessorRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DisableProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Document(typing.TypedDict, total=False):
    blobAssets: _list[GoogleCloudDocumentaiV1beta3DocumentBlobAsset]
    chunkedDocument: GoogleCloudDocumentaiV1beta3DocumentChunkedDocument
    content: str
    docid: str
    documentLayout: GoogleCloudDocumentaiV1beta3DocumentDocumentLayout
    entities: _list[GoogleCloudDocumentaiV1beta3DocumentEntity]
    entitiesRevisionId: str
    entitiesRevisions: _list[GoogleCloudDocumentaiV1beta3DocumentEntitiesRevision]
    entityRelations: _list[GoogleCloudDocumentaiV1beta3DocumentEntityRelation]
    entityValidationOutput: GoogleCloudDocumentaiV1beta3DocumentEntityValidationOutput
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
class GoogleCloudDocumentaiV1beta3DocumentAnnotations(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentBlobAsset(typing.TypedDict, total=False):
    assetId: str
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocument(
    typing.TypedDict, total=False
):
    chunks: _list[GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunk]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunk(
    typing.TypedDict, total=False
):
    chunkFields: _list[
        GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkField
    ]
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
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkField(
    typing.TypedDict, total=False
):
    imageChunkField: (
        GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkImageChunkField
    )
    tableChunkField: (
        GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkTableChunkField
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageFooter(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageHeader(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkChunkPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkImageChunkField(
    typing.TypedDict, total=False
):
    annotations: GoogleCloudDocumentaiV1beta3DocumentAnnotations
    blobAssetId: str
    dataUri: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentChunkedDocumentChunkTableChunkField(
    typing.TypedDict, total=False
):
    annotations: GoogleCloudDocumentaiV1beta3DocumentAnnotations

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayout(typing.TypedDict, total=False):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock(
    typing.TypedDict, total=False
):
    blockId: str
    boundingBox: GoogleCloudDocumentaiV1beta3BoundingPoly
    imageBlock: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutImageBlock
    listBlock: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock
    pageSpan: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan
    tableBlock: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock
    textBlock: GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutImageBlock(
    typing.TypedDict, total=False
):
    annotations: GoogleCloudDocumentaiV1beta3DocumentAnnotations
    blobAssetId: str
    dataUri: str
    gcsUri: str
    imageText: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock(
    typing.TypedDict, total=False
):
    listEntries: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry
    ]
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock(
    typing.TypedDict, total=False
):
    annotations: GoogleCloudDocumentaiV1beta3DocumentAnnotations
    bodyRows: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]
    caption: str
    headerRows: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]
    colSpan: int
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow(
    typing.TypedDict, total=False
):
    cells: _list[
        GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock(
    typing.TypedDict, total=False
):
    annotations: GoogleCloudDocumentaiV1beta3DocumentAnnotations
    blocks: _list[GoogleCloudDocumentaiV1beta3DocumentDocumentLayoutDocumentLayoutBlock]
    text: str
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntitiesRevision(
    typing.TypedDict, total=False
):
    entities: _list[GoogleCloudDocumentaiV1beta3DocumentEntity]
    entityValidationOutput: GoogleCloudDocumentaiV1beta3DocumentEntityValidationOutput
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance
    revisionId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntity(typing.TypedDict, total=False):
    confidence: float
    id: str
    mentionId: str
    mentionText: str
    method: typing.Literal["METHOD_UNSPECIFIED", "EXTRACT", "DERIVE"]
    normalizedValue: GoogleCloudDocumentaiV1beta3DocumentEntityNormalizedValue
    pageAnchor: GoogleCloudDocumentaiV1beta3DocumentPageAnchor
    properties: _list[GoogleCloudDocumentaiV1beta3DocumentEntity]
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance
    redacted: bool
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntityNormalizedValue(
    typing.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    floatValue: float
    integerValue: int
    moneyValue: GoogleTypeMoney
    signatureValue: bool
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntityRelation(typing.TypedDict, total=False):
    objectId: str
    relation: str
    subjectId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntityValidationOutput(
    typing.TypedDict, total=False
):
    passAllRules: bool
    validationResults: _list[
        GoogleCloudDocumentaiV1beta3DocumentEntityValidationOutputValidationResult
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentEntityValidationOutputValidationResult(
    typing.TypedDict, total=False
):
    rule: str
    ruleDescription: str
    ruleName: str
    validationDetails: str
    validationResultType: typing.Literal[
        "VALIDATION_RESULT_TYPE_UNSPECIFIED",
        "VALIDATION_RESULT_TYPE_VALID",
        "VALIDATION_RESULT_TYPE_INVALID",
        "VALIDATION_RESULT_TYPE_SKIPPED",
        "VALIDATION_RESULT_TYPE_NOT_APPLICABLE",
    ]

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
class GoogleCloudDocumentaiV1beta3DocumentMetadata(typing.TypedDict, total=False):
    datasetType: typing.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    displayName: str
    documentId: GoogleCloudDocumentaiV1beta3DocumentId
    labelingState: typing.Literal[
        "DOCUMENT_LABELING_STATE_UNSPECIFIED",
        "DOCUMENT_LABELED",
        "DOCUMENT_UNLABELED",
        "DOCUMENT_AUTO_LABELED",
    ]
    pageCount: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentOutputConfig(typing.TypedDict, total=False):
    gcsOutputConfig: GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfig(
    typing.TypedDict, total=False
):
    fieldMask: str
    gcsUri: str
    shardingConfig: (
        GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfigShardingConfig
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfigShardingConfig(
    typing.TypedDict, total=False
):
    pagesOverlap: int
    pagesPerShard: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPage(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiV1beta3DocumentPageAnchor(typing.TypedDict, total=False):
    pageRefs: _list[GoogleCloudDocumentaiV1beta3DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageAnchorPageRef(
    typing.TypedDict, total=False
):
    boundingPoly: GoogleCloudDocumentaiV1beta3BoundingPoly
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
class GoogleCloudDocumentaiV1beta3DocumentPageBlock(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageDetectedBarcode(
    typing.TypedDict, total=False
):
    barcode: GoogleCloudDocumentaiV1beta3Barcode
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage(
    typing.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageDimension(typing.TypedDict, total=False):
    height: float
    unit: str
    width: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageFormField(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiV1beta3DocumentPageImage(typing.TypedDict, total=False):
    content: str
    height: int
    mimeType: str
    width: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScores(
    typing.TypedDict, total=False
):
    detectedDefects: _list[
        GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScoresDetectedDefect
    ]
    qualityScore: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageImageQualityScoresDetectedDefect(
    typing.TypedDict, total=False
):
    confidence: float
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageLayout(typing.TypedDict, total=False):
    boundingPoly: GoogleCloudDocumentaiV1beta3BoundingPoly
    confidence: float
    orientation: typing.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageLine(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageMatrix(typing.TypedDict, total=False):
    cols: int
    data: str
    rows: int
    type: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageParagraph(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageSymbol(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTable(typing.TypedDict, total=False):
    bodyRows: _list[GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow]
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    headerRows: _list[GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTableTableCell(
    typing.TypedDict, total=False
):
    colSpan: int
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTableTableRow(
    typing.TypedDict, total=False
):
    cells: _list[GoogleCloudDocumentaiV1beta3DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageToken(typing.TypedDict, total=False):
    detectedBreak: GoogleCloudDocumentaiV1beta3DocumentPageTokenDetectedBreak
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1beta3DocumentProvenance
    styleInfo: GoogleCloudDocumentaiV1beta3DocumentPageTokenStyleInfo

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTokenDetectedBreak(
    typing.TypedDict, total=False
):
    type: typing.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentPageTokenStyleInfo(
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
class GoogleCloudDocumentaiV1beta3DocumentPageVisualElement(
    typing.TypedDict, total=False
):
    detectedLanguages: _list[GoogleCloudDocumentaiV1beta3DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1beta3DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentProvenance(typing.TypedDict, total=False):
    id: int
    parents: _list[GoogleCloudDocumentaiV1beta3DocumentProvenanceParent]
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
class GoogleCloudDocumentaiV1beta3DocumentProvenanceParent(
    typing.TypedDict, total=False
):
    id: int
    index: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentRevision(typing.TypedDict, total=False):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1beta3DocumentRevisionHumanReview
    id: str
    parent: _list[int]
    parentIds: _list[str]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentRevisionHumanReview(
    typing.TypedDict, total=False
):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchema(typing.TypedDict, total=False):
    description: str
    displayName: str
    documentPrompt: str
    entityTypes: _list[GoogleCloudDocumentaiV1beta3DocumentSchemaEntityType]
    metadata: GoogleCloudDocumentaiV1beta3DocumentSchemaMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchemaEntityType(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchemaEntityTypeProperty(
    typing.TypedDict, total=False
):
    description: str
    displayName: str
    method: typing.Literal["METHOD_UNSPECIFIED", "EXTRACT", "DERIVE", "RELAXED_EXTRACT"]
    name: str
    occurrenceType: typing.Literal[
        "OCCURRENCE_TYPE_UNSPECIFIED",
        "OPTIONAL_ONCE",
        "OPTIONAL_MULTIPLE",
        "REQUIRED_ONCE",
        "REQUIRED_MULTIPLE",
    ]
    propertyMetadata: GoogleCloudDocumentaiV1beta3PropertyMetadata
    valueType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentSchemaMetadata(typing.TypedDict, total=False):
    documentAllowMultipleLabels: bool
    documentSplitter: bool
    prefixedNamingOnProperties: bool
    skipNamingValidation: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentShardInfo(typing.TypedDict, total=False):
    pageOffset: int
    shardCount: str
    shardIndex: str
    textOffset: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentStyle(typing.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    color: GoogleTypeColor
    fontFamily: str
    fontSize: GoogleCloudDocumentaiV1beta3DocumentStyleFontSize
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor
    textDecoration: str
    textStyle: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentStyleFontSize(typing.TypedDict, total=False):
    size: float
    unit: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentTextAnchor(typing.TypedDict, total=False):
    content: str
    textSegments: _list[GoogleCloudDocumentaiV1beta3DocumentTextAnchorTextSegment]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentTextAnchorTextSegment(
    typing.TypedDict, total=False
):
    endIndex: str
    startIndex: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DocumentTextChange(typing.TypedDict, total=False):
    changedText: str
    provenance: _list[GoogleCloudDocumentaiV1beta3DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1beta3DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Documents(typing.TypedDict, total=False):
    documents: _list[GoogleCloudDocumentaiV1beta3Document]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EnableProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EntityTypeMetadata(typing.TypedDict, total=False):
    inactive: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionRequest(
    typing.TypedDict, total=False
):
    evaluationDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponse(
    typing.TypedDict, total=False
):
    evaluation: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Evaluation(typing.TypedDict, total=False):
    allEntitiesMetrics: GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics
    createTime: str
    documentCounters: GoogleCloudDocumentaiV1beta3EvaluationCounters
    entityMetrics: dict[str, typing.Any]
    kmsKeyName: str
    kmsKeyVersionName: str
    name: str
    revisions: _list[GoogleCloudDocumentaiV1beta3EvaluationEvaluationRevision]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationConfidenceLevelMetrics(
    typing.TypedDict, total=False
):
    confidenceLevel: float
    metrics: GoogleCloudDocumentaiV1beta3EvaluationMetrics

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationCounters(typing.TypedDict, total=False):
    evaluatedDocumentsCount: int
    failedDocumentsCount: int
    inputDocumentsCount: int
    invalidDocumentsCount: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationEvaluationRevision(
    typing.TypedDict, total=False
):
    allEntitiesMetrics: GoogleCloudDocumentaiV1beta3EvaluationMultiConfidenceMetrics
    documentCounters: GoogleCloudDocumentaiV1beta3EvaluationCounters
    entityMetrics: dict[str, typing.Any]
    revisionId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationMetrics(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
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
    metricsType: typing.Literal["METRICS_TYPE_UNSPECIFIED", "AGGREGATE"]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationReference(typing.TypedDict, total=False):
    aggregateMetrics: GoogleCloudDocumentaiV1beta3EvaluationMetrics
    aggregateMetricsExact: GoogleCloudDocumentaiV1beta3EvaluationMetrics
    evaluation: str
    operation: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponse(
    typing.TypedDict, total=False
):
    processorTypes: _list[GoogleCloudDocumentaiV1beta3ProcessorType]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3FieldExtractionMetadata(
    typing.TypedDict, total=False
):
    summaryOptions: GoogleCloudDocumentaiV1beta3SummaryOptions

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsDocument(typing.TypedDict, total=False):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsDocuments(typing.TypedDict, total=False):
    documents: _list[GoogleCloudDocumentaiV1beta3GcsDocument]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GcsPrefix(typing.TypedDict, total=False):
    gcsUriPrefix: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GenerateSchemaVersionRequest(
    typing.TypedDict, total=False
):
    baseSchemaVersion: str
    gcsDocuments: GoogleCloudDocumentaiV1beta3GcsDocuments
    gcsPrefix: GoogleCloudDocumentaiV1beta3GcsPrefix
    generateSchemaVersionParams: GoogleCloudDocumentaiV1beta3GenerateSchemaVersionRequestGenerateSchemaVersionParams
    inlineDocuments: GoogleCloudDocumentaiV1beta3Documents
    rawDocuments: GoogleCloudDocumentaiV1beta3RawDocuments

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GenerateSchemaVersionRequestGenerateSchemaVersionParams(
    typing.TypedDict, total=False
):
    history: GoogleCloudDocumentaiV1beta3SchemaGenerationHistory
    prompt: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GenerateSchemaVersionResponse(
    typing.TypedDict, total=False
):
    schemaVersion: GoogleCloudDocumentaiV1beta3SchemaVersion

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GetDocumentResponse(typing.TypedDict, total=False):
    document: GoogleCloudDocumentaiV1beta3Document

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
class GoogleCloudDocumentaiV1beta3ImportDocumentsRequest(typing.TypedDict, total=False):
    batchDocumentsImportConfigs: _list[
        GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfig
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfig(
    typing.TypedDict, total=False
):
    autoSplitConfig: GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfigAutoSplitConfig
    batchInputConfig: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig
    datasetSplit: typing.Literal[
        "DATASET_SPLIT_TYPE_UNSPECIFIED",
        "DATASET_SPLIT_TRAIN",
        "DATASET_SPLIT_TEST",
        "DATASET_SPLIT_UNASSIGNED",
    ]
    documentType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfigAutoSplitConfig(
    typing.TypedDict, total=False
):
    trainingSplitRatio: float

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
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequest(
    typing.TypedDict, total=False
):
    externalProcessorVersionSource: GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequestExternalProcessorVersionSource
    processorVersionSource: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequestExternalProcessorVersionSource(
    typing.TypedDict, total=False
):
    processorVersion: str
    serviceEndpoint: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponse(
    typing.TypedDict, total=False
):
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListDocumentsRequest(typing.TypedDict, total=False):
    filter: str
    pageSize: int
    pageToken: str
    returnTotalSize: bool
    skip: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListDocumentsResponse(typing.TypedDict, total=False):
    documentMetadata: _list[GoogleCloudDocumentaiV1beta3DocumentMetadata]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListEvaluationsResponse(
    typing.TypedDict, total=False
):
    evaluations: _list[GoogleCloudDocumentaiV1beta3Evaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorTypesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    processorTypes: _list[GoogleCloudDocumentaiV1beta3ProcessorType]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    processorVersions: _list[GoogleCloudDocumentaiV1beta3ProcessorVersion]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    processors: _list[GoogleCloudDocumentaiV1beta3Processor]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListSchemaVersionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    schemaVersions: _list[GoogleCloudDocumentaiV1beta3SchemaVersion]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListSchemasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[GoogleCloudDocumentaiV1beta3NextSchema]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3NextSchema(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3NormalizedVertex(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3OcrConfig(typing.TypedDict, total=False):
    advancedOcrOptions: _list[str]
    computeStyleInfo: bool
    disableCharacterBoxesDetection: bool
    enableImageQualityScores: bool
    enableNativePdfParsing: bool
    enableSymbol: bool
    hints: GoogleCloudDocumentaiV1beta3OcrConfigHints
    premiumFeatures: GoogleCloudDocumentaiV1beta3OcrConfigPremiumFeatures

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3OcrConfigHints(typing.TypedDict, total=False):
    languageHints: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3OcrConfigPremiumFeatures(
    typing.TypedDict, total=False
):
    computeStyleInfo: bool
    enableMathOcr: bool
    enableSelectionMarkDetection: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessOptions(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    pages: _list[int]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessOptionsLayoutConfig(
    typing.TypedDict, total=False
):
    chunkingConfig: GoogleCloudDocumentaiV1beta3ProcessOptionsLayoutConfigChunkingConfig
    enableImageAnnotation: bool
    enableImageExtraction: bool
    enableLlmLayoutParsing: bool
    enableTableAnnotation: bool
    enableTableSplit: bool
    returnBoundingBoxes: bool
    returnImages: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessOptionsLayoutConfigChunkingConfig(
    typing.TypedDict, total=False
):
    breakpointPercentileThreshold: int
    chunkSize: int
    includeAncestorHeadings: bool
    semanticChunkingGroupSize: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessRequest(typing.TypedDict, total=False):
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
class GoogleCloudDocumentaiV1beta3ProcessResponse(typing.TypedDict, total=False):
    document: GoogleCloudDocumentaiV1beta3Document
    humanReviewOperation: str
    humanReviewStatus: GoogleCloudDocumentaiV1beta3HumanReviewStatus

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Processor(typing.TypedDict, total=False):
    activeSchemaVersion: str
    createTime: str
    defaultProcessorVersion: str
    displayName: str
    kmsKeyName: str
    name: str
    processEndpoint: str
    processorVersionAliases: _list[GoogleCloudDocumentaiV1beta3ProcessorVersionAlias]
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
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
class GoogleCloudDocumentaiV1beta3ProcessorType(typing.TypedDict, total=False):
    allowCreation: bool
    availableLocations: _list[GoogleCloudDocumentaiV1beta3ProcessorTypeLocationInfo]
    category: str
    launchStage: typing.Literal[
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
    typing.TypedDict, total=False
):
    locationId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersion(typing.TypedDict, total=False):
    createTime: str
    deprecationInfo: GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo
    displayName: str
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    genAiModelInfo: GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfo
    googleManaged: bool
    kmsKeyName: str
    kmsKeyVersionName: str
    latestEvaluation: GoogleCloudDocumentaiV1beta3EvaluationReference
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED", "MODEL_TYPE_GENERATIVE", "MODEL_TYPE_CUSTOM"
    ]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
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
class GoogleCloudDocumentaiV1beta3ProcessorVersionAlias(typing.TypedDict, total=False):
    alias: str
    processorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionDeprecationInfo(
    typing.TypedDict, total=False
):
    deprecationTime: str
    replacementProcessorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfo(
    typing.TypedDict, total=False
):
    customGenAiModelInfo: (
        GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoCustomGenAiModelInfo
    )
    foundationGenAiModelInfo: GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoFoundationGenAiModelInfo

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoCustomGenAiModelInfo(
    typing.TypedDict, total=False
):
    baseProcessorVersionId: str
    customModelType: typing.Literal[
        "CUSTOM_MODEL_TYPE_UNSPECIFIED", "VERSIONED_FOUNDATION", "FINE_TUNED"
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionGenAiModelInfoFoundationGenAiModelInfo(
    typing.TypedDict, total=False
):
    finetuningAllowed: bool
    minTrainLabeledDocuments: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3PropertyMetadata(typing.TypedDict, total=False):
    fieldExtractionMetadata: GoogleCloudDocumentaiV1beta3FieldExtractionMetadata
    inactive: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3RawDocument(typing.TypedDict, total=False):
    content: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3RawDocuments(typing.TypedDict, total=False):
    documents: _list[GoogleCloudDocumentaiV1beta3RawDocument]

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
class GoogleCloudDocumentaiV1beta3ReviewDocumentRequest(typing.TypedDict, total=False):
    document: GoogleCloudDocumentaiV1beta3Document
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    enableSchemaValidation: bool
    inlineDocument: GoogleCloudDocumentaiV1beta3Document
    priority: typing.Literal["DEFAULT", "URGENT"]

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
class GoogleCloudDocumentaiV1beta3SchemaGenerationHistory(
    typing.TypedDict, total=False
):
    iterations: _list[GoogleCloudDocumentaiV1beta3SchemaGenerationIteration]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SchemaGenerationIteration(
    typing.TypedDict, total=False
):
    adjustedSchema: GoogleCloudDocumentaiV1beta3SchemaVersion
    generatedSchema: GoogleCloudDocumentaiV1beta3SchemaVersion
    prompt: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SchemaVersion(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    schema: GoogleCloudDocumentaiV1beta3DocumentSchema

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionRequest(
    typing.TypedDict, total=False
):
    defaultProcessorVersion: str

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3SummaryOptions(typing.TypedDict, total=False):
    format: typing.Literal["FORMAT_UNSPECIFIED", "PARAGRAPH", "BULLETS"]
    length: typing.Literal["LENGTH_UNSPECIFIED", "BRIEF", "MODERATE", "COMPREHENSIVE"]

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
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequest(
    typing.TypedDict, total=False
):
    baseProcessorVersion: str
    customDocumentExtractionOptions: GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestCustomDocumentExtractionOptions
    documentSchema: GoogleCloudDocumentaiV1beta3DocumentSchema
    foundationModelTuningOptions: GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestFoundationModelTuningOptions
    inputData: GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestInputData
    processorVersion: GoogleCloudDocumentaiV1beta3ProcessorVersion

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestCustomDocumentExtractionOptions(
    typing.TypedDict, total=False
):
    trainingMethod: typing.Literal[
        "TRAINING_METHOD_UNSPECIFIED", "MODEL_BASED", "TEMPLATE_BASED"
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestFoundationModelTuningOptions(
    typing.TypedDict, total=False
):
    learningRateMultiplier: float
    previousFineTunedProcessorVersionName: str
    trainSteps: int

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestInputData(
    typing.TypedDict, total=False
):
    testDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig
    trainingDocuments: GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig

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
class GoogleCloudDocumentaiV1beta3UndeployProcessorVersionRequest(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDocumentaiV1beta3UpdateProcessorVersionMetadata(
    typing.TypedDict, total=False
):
    commonMetadata: GoogleCloudDocumentaiV1beta3CommonOperationMetadata

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3Vertex(typing.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

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
