import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1CreateInstructionMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    instruction: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1ExportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1ExportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    dataset: str
    exportCount: int
    labelStats: GoogleCloudDatalabelingV1alpha1LabelStats
    outputConfig: GoogleCloudDatalabelingV1alpha1OutputConfig
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    outputUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1GcsFolderDestination(
    typing_extensions.TypedDict, total=False
):
    outputFolderUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig(
    typing_extensions.TypedDict, total=False
):
    annotatedDatasetDescription: str
    annotatedDatasetDisplayName: str
    contributorEmails: _list[str]
    instruction: str
    labelGroup: str
    languageCode: str
    questionDuration: str
    replicaCount: int
    userEmailAddress: str

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1ImportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1ImportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    importCount: int
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    imageBoundingBoxDetails: GoogleCloudDatalabelingV1alpha1LabelImageBoundingBoxOperationMetadata
    imageBoundingPolyDetails: GoogleCloudDatalabelingV1alpha1LabelImageBoundingPolyOperationMetadata
    imageClassificationDetails: GoogleCloudDatalabelingV1alpha1LabelImageClassificationOperationMetadata
    imageOrientedBoundingBoxDetails: GoogleCloudDatalabelingV1alpha1LabelImageOrientedBoundingBoxOperationMetadata
    imagePolylineDetails: GoogleCloudDatalabelingV1alpha1LabelImagePolylineOperationMetadata
    imageSegmentationDetails: GoogleCloudDatalabelingV1alpha1LabelImageSegmentationOperationMetadata
    partialFailures: _list[GoogleRpcStatus]
    progressPercent: int
    textClassificationDetails: GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadata
    textEntityExtractionDetails: GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadata
    videoClassificationDetails: GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadata
    videoEventDetails: GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadata
    videoObjectDetectionDetails: GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadata
    videoObjectTrackingDetails: GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadata

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelStats(
    typing_extensions.TypedDict, total=False
):
    exampleCount: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelTextClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelTextEntityExtractionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelVideoClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelVideoEventOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelVideoObjectDetectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1LabelVideoObjectTrackingOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1alpha1OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDatalabelingV1alpha1GcsDestination
    gcsFolderDestination: GoogleCloudDatalabelingV1alpha1GcsFolderDestination

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotatedDataset(
    typing_extensions.TypedDict, total=False
):
    annotationSource: typing_extensions.Literal[
        "ANNOTATION_SOURCE_UNSPECIFIED", "OPERATOR"
    ]
    annotationType: typing_extensions.Literal[
        "ANNOTATION_TYPE_UNSPECIFIED",
        "IMAGE_CLASSIFICATION_ANNOTATION",
        "IMAGE_BOUNDING_BOX_ANNOTATION",
        "IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION",
        "IMAGE_BOUNDING_POLY_ANNOTATION",
        "IMAGE_POLYLINE_ANNOTATION",
        "IMAGE_SEGMENTATION_ANNOTATION",
        "VIDEO_SHOTS_CLASSIFICATION_ANNOTATION",
        "VIDEO_OBJECT_TRACKING_ANNOTATION",
        "VIDEO_OBJECT_DETECTION_ANNOTATION",
        "VIDEO_EVENT_ANNOTATION",
        "TEXT_CLASSIFICATION_ANNOTATION",
        "TEXT_ENTITY_EXTRACTION_ANNOTATION",
        "GENERAL_CLASSIFICATION_ANNOTATION",
    ]
    blockingResources: _list[str]
    completedExampleCount: str
    createTime: str
    description: str
    displayName: str
    exampleCount: str
    labelStats: GoogleCloudDatalabelingV1beta1LabelStats
    metadata: GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadata
    name: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotatedDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    boundingPolyConfig: GoogleCloudDatalabelingV1beta1BoundingPolyConfig
    eventConfig: GoogleCloudDatalabelingV1beta1EventConfig
    humanAnnotationConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig
    imageClassificationConfig: GoogleCloudDatalabelingV1beta1ImageClassificationConfig
    objectDetectionConfig: GoogleCloudDatalabelingV1beta1ObjectDetectionConfig
    objectTrackingConfig: GoogleCloudDatalabelingV1beta1ObjectTrackingConfig
    polylineConfig: GoogleCloudDatalabelingV1beta1PolylineConfig
    segmentationConfig: GoogleCloudDatalabelingV1beta1SegmentationConfig
    textClassificationConfig: GoogleCloudDatalabelingV1beta1TextClassificationConfig
    textEntityExtractionConfig: GoogleCloudDatalabelingV1beta1TextEntityExtractionConfig
    videoClassificationConfig: GoogleCloudDatalabelingV1beta1VideoClassificationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Annotation(
    typing_extensions.TypedDict, total=False
):
    annotationMetadata: GoogleCloudDatalabelingV1beta1AnnotationMetadata
    annotationSentiment: typing_extensions.Literal[
        "ANNOTATION_SENTIMENT_UNSPECIFIED", "NEGATIVE", "POSITIVE"
    ]
    annotationSource: typing_extensions.Literal[
        "ANNOTATION_SOURCE_UNSPECIFIED", "OPERATOR"
    ]
    annotationValue: GoogleCloudDatalabelingV1beta1AnnotationValue
    name: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotationMetadata(
    typing_extensions.TypedDict, total=False
):
    operatorMetadata: GoogleCloudDatalabelingV1beta1OperatorMetadata

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotationSpec(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    index: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotationSpecSet(
    typing_extensions.TypedDict, total=False
):
    annotationSpecs: _list[GoogleCloudDatalabelingV1beta1AnnotationSpec]
    blockingResources: _list[str]
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfig(
    typing_extensions.TypedDict, total=False
):
    allowMultiLabel: bool
    annotationSpecSet: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotationValue(
    typing_extensions.TypedDict, total=False
):
    imageBoundingPolyAnnotation: GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotation
    imageClassificationAnnotation: GoogleCloudDatalabelingV1beta1ImageClassificationAnnotation
    imagePolylineAnnotation: GoogleCloudDatalabelingV1beta1ImagePolylineAnnotation
    imageSegmentationAnnotation: GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotation
    textClassificationAnnotation: GoogleCloudDatalabelingV1beta1TextClassificationAnnotation
    textEntityExtractionAnnotation: GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotation
    videoClassificationAnnotation: GoogleCloudDatalabelingV1beta1VideoClassificationAnnotation
    videoEventAnnotation: GoogleCloudDatalabelingV1beta1VideoEventAnnotation
    videoObjectTrackingAnnotation: GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotation

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Attempt(typing_extensions.TypedDict, total=False):
    attemptTime: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1BigQuerySource(
    typing_extensions.TypedDict, total=False
):
    inputUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptions(
    typing_extensions.TypedDict, total=False
):
    iouThreshold: float

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1BoundingPoly(
    typing_extensions.TypedDict, total=False
):
    vertices: _list[GoogleCloudDatalabelingV1beta1Vertex]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1BoundingPolyConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: str
    instructionMessage: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ClassificationMetadata(
    typing_extensions.TypedDict, total=False
):
    isMultiLabel: bool

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ClassificationMetrics(
    typing_extensions.TypedDict, total=False
):
    confusionMatrix: GoogleCloudDatalabelingV1beta1ConfusionMatrix
    prCurve: GoogleCloudDatalabelingV1beta1PrCurve

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    f1ScoreAt1: float
    f1ScoreAt5: float
    precision: float
    precisionAt1: float
    precisionAt5: float
    recall: float
    recallAt1: float
    recallAt5: float

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ConfusionMatrix(
    typing_extensions.TypedDict, total=False
):
    row: _list[GoogleCloudDatalabelingV1beta1Row]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ConfusionMatrixEntry(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    itemCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequest(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: GoogleCloudDatalabelingV1beta1AnnotationSpecSet

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1CreateDatasetRequest(
    typing_extensions.TypedDict, total=False
):
    dataset: GoogleCloudDatalabelingV1beta1Dataset

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequest(
    typing_extensions.TypedDict, total=False
):
    job: GoogleCloudDatalabelingV1beta1EvaluationJob

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1CreateInstructionMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    instruction: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1CreateInstructionRequest(
    typing_extensions.TypedDict, total=False
):
    instruction: GoogleCloudDatalabelingV1beta1Instruction

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1CsvInstruction(
    typing_extensions.TypedDict, total=False
):
    gcsFileUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1DataItem(typing_extensions.TypedDict, total=False):
    imagePayload: GoogleCloudDatalabelingV1beta1ImagePayload
    name: str
    textPayload: GoogleCloudDatalabelingV1beta1TextPayload
    videoPayload: GoogleCloudDatalabelingV1beta1VideoPayload

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Dataset(typing_extensions.TypedDict, total=False):
    blockingResources: _list[str]
    createTime: str
    dataItemCount: str
    description: str
    displayName: str
    inputConfigs: _list[GoogleCloudDatalabelingV1beta1InputConfig]
    lastMigrateTime: str
    name: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Evaluation(
    typing_extensions.TypedDict, total=False
):
    annotationType: typing_extensions.Literal[
        "ANNOTATION_TYPE_UNSPECIFIED",
        "IMAGE_CLASSIFICATION_ANNOTATION",
        "IMAGE_BOUNDING_BOX_ANNOTATION",
        "IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION",
        "IMAGE_BOUNDING_POLY_ANNOTATION",
        "IMAGE_POLYLINE_ANNOTATION",
        "IMAGE_SEGMENTATION_ANNOTATION",
        "VIDEO_SHOTS_CLASSIFICATION_ANNOTATION",
        "VIDEO_OBJECT_TRACKING_ANNOTATION",
        "VIDEO_OBJECT_DETECTION_ANNOTATION",
        "VIDEO_EVENT_ANNOTATION",
        "TEXT_CLASSIFICATION_ANNOTATION",
        "TEXT_ENTITY_EXTRACTION_ANNOTATION",
        "GENERAL_CLASSIFICATION_ANNOTATION",
    ]
    config: GoogleCloudDatalabelingV1beta1EvaluationConfig
    createTime: str
    evaluatedItemCount: str
    evaluationJobRunTime: str
    evaluationMetrics: GoogleCloudDatalabelingV1beta1EvaluationMetrics
    name: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EvaluationConfig(
    typing_extensions.TypedDict, total=False
):
    boundingBoxEvaluationOptions: GoogleCloudDatalabelingV1beta1BoundingBoxEvaluationOptions

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EvaluationJob(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: str
    attempts: _list[GoogleCloudDatalabelingV1beta1Attempt]
    createTime: str
    description: str
    evaluationJobConfig: GoogleCloudDatalabelingV1beta1EvaluationJobConfig
    labelMissingGroundTruth: bool
    modelVersion: str
    name: str
    schedule: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "SCHEDULED", "RUNNING", "PAUSED", "STOPPED"
    ]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfig(
    typing_extensions.TypedDict, total=False
):
    email: str
    minAcceptableMeanAveragePrecision: float

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EvaluationJobConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryImportKeys: dict[str, typing.Any]
    boundingPolyConfig: GoogleCloudDatalabelingV1beta1BoundingPolyConfig
    evaluationConfig: GoogleCloudDatalabelingV1beta1EvaluationConfig
    evaluationJobAlertConfig: GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfig
    exampleCount: int
    exampleSamplePercentage: float
    humanAnnotationConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig
    imageClassificationConfig: GoogleCloudDatalabelingV1beta1ImageClassificationConfig
    inputConfig: GoogleCloudDatalabelingV1beta1InputConfig
    textClassificationConfig: GoogleCloudDatalabelingV1beta1TextClassificationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    classificationMetrics: GoogleCloudDatalabelingV1beta1ClassificationMetrics
    objectDetectionMetrics: GoogleCloudDatalabelingV1beta1ObjectDetectionMetrics

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EventConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSets: _list[str]
    clipLength: int
    overlapLength: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Example(typing_extensions.TypedDict, total=False):
    annotations: _list[GoogleCloudDatalabelingV1beta1Annotation]
    imagePayload: GoogleCloudDatalabelingV1beta1ImagePayload
    name: str
    textPayload: GoogleCloudDatalabelingV1beta1TextPayload
    videoPayload: GoogleCloudDatalabelingV1beta1VideoPayload

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ExampleComparison(
    typing_extensions.TypedDict, total=False
):
    groundTruthExample: GoogleCloudDatalabelingV1beta1Example
    modelCreatedExamples: _list[GoogleCloudDatalabelingV1beta1Example]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ExportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ExportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    dataset: str
    exportCount: int
    labelStats: GoogleCloudDatalabelingV1beta1LabelStats
    outputConfig: GoogleCloudDatalabelingV1beta1OutputConfig
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ExportDataRequest(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    filter: str
    outputConfig: GoogleCloudDatalabelingV1beta1OutputConfig
    userEmailAddress: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1FeedbackMessage(
    typing_extensions.TypedDict, total=False
):
    body: str
    createTime: str
    image: str
    name: str
    operatorFeedbackMetadata: GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadata
    requesterFeedbackMetadata: GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadata

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1FeedbackThread(
    typing_extensions.TypedDict, total=False
):
    feedbackThreadMetadata: GoogleCloudDatalabelingV1beta1FeedbackThreadMetadata
    name: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1FeedbackThreadMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    lastUpdateTime: str
    status: typing_extensions.Literal[
        "FEEDBACK_THREAD_STATUS_UNSPECIFIED", "NEW", "REPLIED"
    ]
    thumbnail: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    outputUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1GcsFolderDestination(
    typing_extensions.TypedDict, total=False
):
    outputFolderUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1GcsSource(typing_extensions.TypedDict, total=False):
    inputUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1HumanAnnotationConfig(
    typing_extensions.TypedDict, total=False
):
    annotatedDatasetDescription: str
    annotatedDatasetDisplayName: str
    contributorEmails: _list[str]
    instruction: str
    labelGroup: str
    languageCode: str
    questionDuration: str
    replicaCount: int
    userEmailAddress: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImageBoundingPolyAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    boundingPoly: GoogleCloudDatalabelingV1beta1BoundingPoly
    normalizedBoundingPoly: GoogleCloudDatalabelingV1beta1NormalizedBoundingPoly

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImageClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImageClassificationConfig(
    typing_extensions.TypedDict, total=False
):
    allowMultiLabel: bool
    annotationSpecSet: str
    answerAggregationType: typing_extensions.Literal[
        "STRING_AGGREGATION_TYPE_UNSPECIFIED",
        "MAJORITY_VOTE",
        "UNANIMOUS_VOTE",
        "NO_AGGREGATION",
    ]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImagePayload(
    typing_extensions.TypedDict, total=False
):
    imageThumbnail: str
    imageUri: str
    mimeType: str
    signedUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImagePolylineAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    normalizedPolyline: GoogleCloudDatalabelingV1beta1NormalizedPolyline
    polyline: GoogleCloudDatalabelingV1beta1Polyline

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImageSegmentationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationColors: dict[str, typing.Any]
    imageBytes: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    importCount: int
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ImportDataRequest(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudDatalabelingV1beta1InputConfig
    userEmailAddress: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1InputConfig(
    typing_extensions.TypedDict, total=False
):
    annotationType: typing_extensions.Literal[
        "ANNOTATION_TYPE_UNSPECIFIED",
        "IMAGE_CLASSIFICATION_ANNOTATION",
        "IMAGE_BOUNDING_BOX_ANNOTATION",
        "IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION",
        "IMAGE_BOUNDING_POLY_ANNOTATION",
        "IMAGE_POLYLINE_ANNOTATION",
        "IMAGE_SEGMENTATION_ANNOTATION",
        "VIDEO_SHOTS_CLASSIFICATION_ANNOTATION",
        "VIDEO_OBJECT_TRACKING_ANNOTATION",
        "VIDEO_OBJECT_DETECTION_ANNOTATION",
        "VIDEO_EVENT_ANNOTATION",
        "TEXT_CLASSIFICATION_ANNOTATION",
        "TEXT_ENTITY_EXTRACTION_ANNOTATION",
        "GENERAL_CLASSIFICATION_ANNOTATION",
    ]
    bigquerySource: GoogleCloudDatalabelingV1beta1BigQuerySource
    classificationMetadata: GoogleCloudDatalabelingV1beta1ClassificationMetadata
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "IMAGE", "VIDEO", "TEXT", "GENERAL_DATA"
    ]
    gcsSource: GoogleCloudDatalabelingV1beta1GcsSource
    textMetadata: GoogleCloudDatalabelingV1beta1TextMetadata

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Instruction(
    typing_extensions.TypedDict, total=False
):
    blockingResources: _list[str]
    createTime: str
    csvInstruction: GoogleCloudDatalabelingV1beta1CsvInstruction
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "IMAGE", "VIDEO", "TEXT", "GENERAL_DATA"
    ]
    description: str
    displayName: str
    name: str
    pdfInstruction: GoogleCloudDatalabelingV1beta1PdfInstruction
    updateTime: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelImageRequest(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig
    boundingPolyConfig: GoogleCloudDatalabelingV1beta1BoundingPolyConfig
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "CLASSIFICATION",
        "BOUNDING_BOX",
        "ORIENTED_BOUNDING_BOX",
        "BOUNDING_POLY",
        "POLYLINE",
        "SEGMENTATION",
    ]
    imageClassificationConfig: GoogleCloudDatalabelingV1beta1ImageClassificationConfig
    polylineConfig: GoogleCloudDatalabelingV1beta1PolylineConfig
    segmentationConfig: GoogleCloudDatalabelingV1beta1SegmentationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    imageBoundingBoxDetails: GoogleCloudDatalabelingV1beta1LabelImageBoundingBoxOperationMetadata
    imageBoundingPolyDetails: GoogleCloudDatalabelingV1beta1LabelImageBoundingPolyOperationMetadata
    imageClassificationDetails: GoogleCloudDatalabelingV1beta1LabelImageClassificationOperationMetadata
    imageOrientedBoundingBoxDetails: GoogleCloudDatalabelingV1beta1LabelImageOrientedBoundingBoxOperationMetadata
    imagePolylineDetails: GoogleCloudDatalabelingV1beta1LabelImagePolylineOperationMetadata
    imageSegmentationDetails: GoogleCloudDatalabelingV1beta1LabelImageSegmentationOperationMetadata
    partialFailures: _list[GoogleRpcStatus]
    progressPercent: int
    textClassificationDetails: GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadata
    textEntityExtractionDetails: GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadata
    videoClassificationDetails: GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadata
    videoEventDetails: GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadata
    videoObjectDetectionDetails: GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadata
    videoObjectTrackingDetails: GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadata

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelStats(
    typing_extensions.TypedDict, total=False
):
    exampleCount: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelTextClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelTextEntityExtractionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelTextRequest(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED", "TEXT_CLASSIFICATION", "TEXT_ENTITY_EXTRACTION"
    ]
    textClassificationConfig: GoogleCloudDatalabelingV1beta1TextClassificationConfig
    textEntityExtractionConfig: GoogleCloudDatalabelingV1beta1TextEntityExtractionConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelVideoClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelVideoEventOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelVideoObjectDetectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelVideoObjectTrackingOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1LabelVideoRequest(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1beta1HumanAnnotationConfig
    eventConfig: GoogleCloudDatalabelingV1beta1EventConfig
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "CLASSIFICATION",
        "OBJECT_DETECTION",
        "OBJECT_TRACKING",
        "EVENT",
    ]
    objectDetectionConfig: GoogleCloudDatalabelingV1beta1ObjectDetectionConfig
    objectTrackingConfig: GoogleCloudDatalabelingV1beta1ObjectTrackingConfig
    videoClassificationConfig: GoogleCloudDatalabelingV1beta1VideoClassificationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedDatasets: _list[GoogleCloudDatalabelingV1beta1AnnotatedDataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponse(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSets: _list[GoogleCloudDatalabelingV1beta1AnnotationSpecSet]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListDataItemsResponse(
    typing_extensions.TypedDict, total=False
):
    dataItems: _list[GoogleCloudDatalabelingV1beta1DataItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListDatasetsResponse(
    typing_extensions.TypedDict, total=False
):
    datasets: _list[GoogleCloudDatalabelingV1beta1Dataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponse(
    typing_extensions.TypedDict, total=False
):
    evaluationJobs: _list[GoogleCloudDatalabelingV1beta1EvaluationJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListExamplesResponse(
    typing_extensions.TypedDict, total=False
):
    examples: _list[GoogleCloudDatalabelingV1beta1Example]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponse(
    typing_extensions.TypedDict, total=False
):
    feedbackMessages: _list[GoogleCloudDatalabelingV1beta1FeedbackMessage]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponse(
    typing_extensions.TypedDict, total=False
):
    feedbackThreads: _list[GoogleCloudDatalabelingV1beta1FeedbackThread]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListInstructionsResponse(
    typing_extensions.TypedDict, total=False
):
    instructions: _list[GoogleCloudDatalabelingV1beta1Instruction]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1NormalizedBoundingPoly(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: _list[GoogleCloudDatalabelingV1beta1NormalizedVertex]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1NormalizedPolyline(
    typing_extensions.TypedDict, total=False
):
    normalizedVertices: _list[GoogleCloudDatalabelingV1beta1NormalizedVertex]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1NormalizedVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ObjectDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: str
    extractionFrameRate: float

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ObjectDetectionMetrics(
    typing_extensions.TypedDict, total=False
):
    prCurve: GoogleCloudDatalabelingV1beta1PrCurve

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ObjectTrackingConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: str
    clipLength: int
    overlapLength: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ObjectTrackingFrame(
    typing_extensions.TypedDict, total=False
):
    boundingPoly: GoogleCloudDatalabelingV1beta1BoundingPoly
    normalizedBoundingPoly: GoogleCloudDatalabelingV1beta1NormalizedBoundingPoly
    timeOffset: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1OperatorFeedbackMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1OperatorMetadata(
    typing_extensions.TypedDict, total=False
):
    comments: _list[str]
    labelVotes: int
    score: float
    totalVotes: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDatalabelingV1beta1GcsDestination
    gcsFolderDestination: GoogleCloudDatalabelingV1beta1GcsFolderDestination

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1PdfInstruction(
    typing_extensions.TypedDict, total=False
):
    gcsFileUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Polyline(typing_extensions.TypedDict, total=False):
    vertices: _list[GoogleCloudDatalabelingV1beta1Vertex]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1PolylineConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: str
    instructionMessage: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1PrCurve(typing_extensions.TypedDict, total=False):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    areaUnderCurve: float
    confidenceMetricsEntries: _list[
        GoogleCloudDatalabelingV1beta1ConfidenceMetricsEntry
    ]
    meanAveragePrecision: float

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1RequesterFeedbackMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Row(typing_extensions.TypedDict, total=False):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    entries: _list[GoogleCloudDatalabelingV1beta1ConfusionMatrixEntry]

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SearchEvaluationsResponse(
    typing_extensions.TypedDict, total=False
):
    evaluations: _list[GoogleCloudDatalabelingV1beta1Evaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponse(
    typing_extensions.TypedDict, total=False
):
    exampleComparisons: _list[GoogleCloudDatalabelingV1beta1ExampleComparison]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SegmentationConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: str
    instructionMessage: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SentimentConfig(
    typing_extensions.TypedDict, total=False
):
    enableLabelSentimentSelection: bool

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SequentialSegment(
    typing_extensions.TypedDict, total=False
):
    end: int
    start: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1TextClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1TextClassificationConfig(
    typing_extensions.TypedDict, total=False
):
    allowMultiLabel: bool
    annotationSpecSet: str
    sentimentConfig: GoogleCloudDatalabelingV1beta1SentimentConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1TextEntityExtractionAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    sequentialSegment: GoogleCloudDatalabelingV1beta1SequentialSegment

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1TextEntityExtractionConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSet: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1TextMetadata(
    typing_extensions.TypedDict, total=False
):
    languageCode: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1TextPayload(
    typing_extensions.TypedDict, total=False
):
    textContent: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1TimeSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1Vertex(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1VideoClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    timeSegment: GoogleCloudDatalabelingV1beta1TimeSegment

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1VideoClassificationConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSpecSetConfigs: _list[
        GoogleCloudDatalabelingV1beta1AnnotationSpecSetConfig
    ]
    applyShotDetection: bool

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1VideoEventAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    timeSegment: GoogleCloudDatalabelingV1beta1TimeSegment

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1VideoObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpec: GoogleCloudDatalabelingV1beta1AnnotationSpec
    objectTrackingFrames: _list[GoogleCloudDatalabelingV1beta1ObjectTrackingFrame]
    timeSegment: GoogleCloudDatalabelingV1beta1TimeSegment

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1VideoPayload(
    typing_extensions.TypedDict, total=False
):
    frameRate: float
    mimeType: str
    signedUri: str
    videoThumbnails: _list[GoogleCloudDatalabelingV1beta1VideoThumbnail]
    videoUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1VideoThumbnail(
    typing_extensions.TypedDict, total=False
):
    thumbnail: str
    timeOffset: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    instruction: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1ExportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1ExportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    dataset: str
    exportCount: int
    labelStats: GoogleCloudDatalabelingV1p1alpha1LabelStats
    outputConfig: GoogleCloudDatalabelingV1p1alpha1OutputConfig
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    outputUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1GcsFolderDestination(
    typing_extensions.TypedDict, total=False
):
    outputFolderUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1GenerateAnalysisReportOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataset: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig(
    typing_extensions.TypedDict, total=False
):
    annotatedDatasetDescription: str
    annotatedDatasetDisplayName: str
    contributorEmails: _list[str]
    instruction: str
    labelGroup: str
    languageCode: str
    questionDuration: str
    replicaCount: int
    userEmailAddress: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1ImportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1ImportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    importCount: int
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    imageBoundingBoxDetails: GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingBoxOperationMetadata
    imageBoundingPolyDetails: GoogleCloudDatalabelingV1p1alpha1LabelImageBoundingPolyOperationMetadata
    imageClassificationDetails: GoogleCloudDatalabelingV1p1alpha1LabelImageClassificationOperationMetadata
    imageOrientedBoundingBoxDetails: GoogleCloudDatalabelingV1p1alpha1LabelImageOrientedBoundingBoxOperationMetadata
    imagePolylineDetails: GoogleCloudDatalabelingV1p1alpha1LabelImagePolylineOperationMetadata
    imageSegmentationDetails: GoogleCloudDatalabelingV1p1alpha1LabelImageSegmentationOperationMetadata
    partialFailures: _list[GoogleRpcStatus]
    progressPercent: int
    textClassificationDetails: GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadata
    textEntityExtractionDetails: GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadata
    videoClassificationDetails: GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadata
    videoEventDetails: GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadata
    videoObjectDetectionDetails: GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadata
    videoObjectTrackingDetails: GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadata

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelStats(
    typing_extensions.TypedDict, total=False
):
    exampleCount: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelTextClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelTextEntityExtractionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelVideoClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelVideoEventOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectDetectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1LabelVideoObjectTrackingOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p1alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p1alpha1OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDatalabelingV1p1alpha1GcsDestination
    gcsFolderDestination: GoogleCloudDatalabelingV1p1alpha1GcsFolderDestination

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1CreateInstructionMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    instruction: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1ExportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    dataset: str
    exportCount: int
    labelStats: GoogleCloudDatalabelingV1p2alpha1LabelStats
    outputConfig: GoogleCloudDatalabelingV1p2alpha1OutputConfig
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    outputUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1GcsFolderDestination(
    typing_extensions.TypedDict, total=False
):
    outputFolderUri: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig(
    typing_extensions.TypedDict, total=False
):
    annotatedDatasetDescription: str
    annotatedDatasetDisplayName: str
    contributorEmails: _list[str]
    instruction: str
    labelGroup: str
    languageCode: str
    questionDuration: str
    replicaCount: int
    userEmailAddress: str

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataset: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1ImportDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    importCount: int
    totalCount: int

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    createTime: str
    dataset: str
    imageBoundingBoxDetails: GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingBoxOperationMetadata
    imageBoundingPolyDetails: GoogleCloudDatalabelingV1p2alpha1LabelImageBoundingPolyOperationMetadata
    imageClassificationDetails: GoogleCloudDatalabelingV1p2alpha1LabelImageClassificationOperationMetadata
    imageOrientedBoundingBoxDetails: GoogleCloudDatalabelingV1p2alpha1LabelImageOrientedBoundingBoxOperationMetadata
    imagePolylineDetails: GoogleCloudDatalabelingV1p2alpha1LabelImagePolylineOperationMetadata
    imageSegmentationDetails: GoogleCloudDatalabelingV1p2alpha1LabelImageSegmentationOperationMetadata
    partialFailures: _list[GoogleRpcStatus]
    progressPercent: int
    textClassificationDetails: GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadata
    textEntityExtractionDetails: GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadata
    videoClassificationDetails: GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadata
    videoEventDetails: GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadata
    videoObjectDetectionDetails: GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadata
    videoObjectTrackingDetails: GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadata

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelStats(
    typing_extensions.TypedDict, total=False
):
    exampleCount: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelTextClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelTextEntityExtractionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelVideoClassificationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelVideoEventOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectDetectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1LabelVideoObjectTrackingOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    basicConfig: GoogleCloudDatalabelingV1p2alpha1HumanAnnotationConfig

@typing.type_check_only
class GoogleCloudDatalabelingV1p2alpha1OutputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudDatalabelingV1p2alpha1GcsDestination
    gcsFolderDestination: GoogleCloudDatalabelingV1p2alpha1GcsFolderDestination

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
