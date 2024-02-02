import typing

import typing_extensions

_list = list

@typing.type_check_only
class CloudAiLargeModelsVisionEmbedVideoResponse(
    typing_extensions.TypedDict, total=False
):
    videoEmbeddings: _list[typing.Any]

@typing.type_check_only
class CloudAiLargeModelsVisionFilteredText(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "RAI_CATEGORY_UNSPECIFIED",
        "OBSCENE",
        "SEXUALLY_EXPLICIT",
        "IDENTITY_ATTACK",
        "VIOLENCE_ABUSE",
        "CSAI",
        "SPII",
        "CELEBRITY",
        "FACE_IMG",
        "WATERMARK_IMG",
        "MEMORIZATION_IMG",
        "CSAI_IMG",
        "PORN_IMG",
        "VIOLENCE_IMG",
        "CHILD_IMG",
        "TOXIC",
        "SENSITIVE_WORD",
        "PERSON_IMG",
        "ICA_IMG",
        "SEXUAL_IMG",
        "IU_IMG",
        "RACY_IMG",
        "PEDO_IMG",
        "DEATH_HARM_TRAGEDY",
        "HEALTH",
        "FIREARMS_WEAPONS",
        "RELIGIOUS_BELIEF",
        "ILLICIT_DRUGS",
        "WAR_CONFLICT",
        "POLITICS",
        "HATE_SYMBOL_IMG",
        "CHILD_TEXT",
        "DANGEROUS_CONTENT",
        "RECITATION_TEXT",
    ]
    confidence: typing_extensions.Literal[
        "CONFIDENCE_UNSPECIFIED",
        "CONFIDENCE_LOW",
        "CONFIDENCE_MEDIUM",
        "CONFIDENCE_HIGH",
    ]
    prompt: str
    score: float

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    generatedSamples: _list[CloudAiLargeModelsVisionMedia]
    raiMediaFilteredCount: int
    raiMediaFilteredReasons: _list[str]
    raiTextFilteredReason: CloudAiLargeModelsVisionFilteredText

@typing.type_check_only
class CloudAiLargeModelsVisionImage(typing_extensions.TypedDict, total=False):
    encoding: str
    image: str
    imageRaiScores: CloudAiLargeModelsVisionImageRAIScores
    raiInfo: CloudAiLargeModelsVisionRaiInfo
    semanticFilterResponse: CloudAiLargeModelsVisionSemanticFilterResponse
    uri: str

@typing.type_check_only
class CloudAiLargeModelsVisionImageRAIScores(typing_extensions.TypedDict, total=False):
    agileWatermarkDetectionScore: float

@typing.type_check_only
class CloudAiLargeModelsVisionMedia(typing_extensions.TypedDict, total=False):
    image: CloudAiLargeModelsVisionImage
    video: CloudAiLargeModelsVisionVideo

@typing.type_check_only
class CloudAiLargeModelsVisionMediaGenerateContentResponse(
    typing_extensions.TypedDict, total=False
):
    response: CloudAiNlLlmProtoServiceGenerateMultiModalResponse

@typing.type_check_only
class CloudAiLargeModelsVisionNamedBoundingBox(
    typing_extensions.TypedDict, total=False
):
    classes: _list[str]
    entities: _list[str]
    scores: _list[float]
    x1: float
    x2: float
    y1: float
    y2: float

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfo(typing_extensions.TypedDict, total=False):
    raiCategories: _list[str]
    scores: _list[float]

@typing.type_check_only
class CloudAiLargeModelsVisionReasonVideoResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[CloudAiLargeModelsVisionReasonVideoResponseTextResponse]

@typing.type_check_only
class CloudAiLargeModelsVisionReasonVideoResponseTextResponse(
    typing_extensions.TypedDict, total=False
):
    relativeTemporalPartition: CloudAiLargeModelsVisionRelativeTemporalPartition
    text: str

@typing.type_check_only
class CloudAiLargeModelsVisionRelativeTemporalPartition(
    typing_extensions.TypedDict, total=False
):
    endOffset: str
    startOffset: str

@typing.type_check_only
class CloudAiLargeModelsVisionSemanticFilterResponse(
    typing_extensions.TypedDict, total=False
):
    namedBoundingBoxes: _list[CloudAiLargeModelsVisionNamedBoundingBox]
    passedSemanticFilter: bool

@typing.type_check_only
class CloudAiLargeModelsVisionVideo(typing_extensions.TypedDict, total=False):
    uri: str
    video: str

@typing.type_check_only
class CloudAiNlLlmProtoServiceCandidate(typing_extensions.TypedDict, total=False):
    citationMetadata: CloudAiNlLlmProtoServiceCitationMetadata
    content: CloudAiNlLlmProtoServiceContent
    finishMessage: str
    finishReason: typing_extensions.Literal[
        "FINISH_REASON_UNSPECIFIED",
        "FINISH_REASON_STOP",
        "FINISH_REASON_MAX_TOKENS",
        "FINISH_REASON_SAFETY",
        "FINISH_REASON_RECITATION",
        "FINISH_REASON_OTHER",
    ]
    groundingMetadata: LearningGenaiRootGroundingMetadata
    index: int
    safetyRatings: _list[CloudAiNlLlmProtoServiceSafetyRating]

@typing.type_check_only
class CloudAiNlLlmProtoServiceCitation(typing_extensions.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: GoogleTypeDate
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class CloudAiNlLlmProtoServiceCitationMetadata(
    typing_extensions.TypedDict, total=False
):
    citations: _list[CloudAiNlLlmProtoServiceCitation]

@typing.type_check_only
class CloudAiNlLlmProtoServiceContent(typing_extensions.TypedDict, total=False):
    parts: _list[CloudAiNlLlmProtoServicePart]
    role: str

@typing.type_check_only
class CloudAiNlLlmProtoServiceFact(typing_extensions.TypedDict, total=False):
    query: str
    summary: str
    title: str
    url: str

@typing.type_check_only
class CloudAiNlLlmProtoServiceFunctionCall(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    name: str

@typing.type_check_only
class CloudAiNlLlmProtoServiceFunctionResponse(
    typing_extensions.TypedDict, total=False
):
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class CloudAiNlLlmProtoServiceGenerateMultiModalResponse(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[CloudAiNlLlmProtoServiceCandidate]
    debugMetadata: CloudAiNlLlmProtoServiceMessageMetadata
    facts: _list[CloudAiNlLlmProtoServiceFact]
    promptFeedback: CloudAiNlLlmProtoServicePromptFeedback
    reportingMetrics: IntelligenceCloudAutomlXpsReportingMetrics
    usageMetadata: CloudAiNlLlmProtoServiceUsageMetadata

@typing.type_check_only
class CloudAiNlLlmProtoServiceMessageMetadata(typing_extensions.TypedDict, total=False):
    inputFilterInfo: LearningServingLlmMessageMetadata
    modelRoutingDecision: LearningGenaiRootRoutingDecision
    outputFilterInfo: _list[LearningServingLlmMessageMetadata]

@typing.type_check_only
class CloudAiNlLlmProtoServicePart(typing_extensions.TypedDict, total=False):
    fileData: CloudAiNlLlmProtoServicePartFileData
    functionCall: CloudAiNlLlmProtoServiceFunctionCall
    functionResponse: CloudAiNlLlmProtoServiceFunctionResponse
    inlineData: CloudAiNlLlmProtoServicePartBlob
    text: str
    videoMetadata: CloudAiNlLlmProtoServicePartVideoMetadata

@typing.type_check_only
class CloudAiNlLlmProtoServicePartBlob(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str
    originalFileData: CloudAiNlLlmProtoServicePartFileData

@typing.type_check_only
class CloudAiNlLlmProtoServicePartFileData(typing_extensions.TypedDict, total=False):
    fileUri: str
    mimeType: str

@typing.type_check_only
class CloudAiNlLlmProtoServicePartVideoMetadata(
    typing_extensions.TypedDict, total=False
):
    endOffset: str
    modelLevelMetaData: CloudAiNlLlmProtoServicePartVideoMetadataModelLevelMetadata
    startOffset: str

@typing.type_check_only
class CloudAiNlLlmProtoServicePartVideoMetadataModelLevelMetadata(
    typing_extensions.TypedDict, total=False
):
    fps: float
    numFrames: int

@typing.type_check_only
class CloudAiNlLlmProtoServicePromptFeedback(typing_extensions.TypedDict, total=False):
    blockReason: typing_extensions.Literal[
        "BLOCKED_REASON_UNSPECIFIED", "SAFETY", "OTHER"
    ]
    blockReasonMessage: str
    safetyRatings: _list[CloudAiNlLlmProtoServiceSafetyRating]

@typing.type_check_only
class CloudAiNlLlmProtoServiceRaiResult(typing_extensions.TypedDict, total=False):
    aidaRecitationResult: LanguageLabsAidaTrustRecitationProtoRecitationResult
    blocked: bool
    errorCodes: _list[int]
    filtered: bool
    languageFilterResult: LearningGenaiRootLanguageFilterResult
    raiSignals: _list[CloudAiNlLlmProtoServiceRaiSignal]
    triggeredBlocklist: bool
    triggeredRecitation: bool
    triggeredSafetyFilter: bool

@typing.type_check_only
class CloudAiNlLlmProtoServiceRaiSignal(typing_extensions.TypedDict, total=False):
    confidence: typing_extensions.Literal[
        "CONFIDENCE_UNSPECIFIED",
        "CONFIDENCE_NONE",
        "CONFIDENCE_LOW",
        "CONFIDENCE_MEDIUM",
        "CONFIDENCE_HIGH",
    ]
    flagged: bool
    raiCategory: typing_extensions.Literal[
        "RAI_CATEGORY_UNSPECIFIED",
        "TOXIC",
        "SEXUALLY_EXPLICIT",
        "HATE_SPEECH",
        "VIOLENT",
        "PROFANITY",
        "HARASSMENT",
        "DEATH_HARM_TRAGEDY",
        "FIREARMS_WEAPONS",
        "PUBLIC_SAFETY",
        "HEALTH",
        "RELIGIOUS_BELIEF",
        "ILLICIT_DRUGS",
        "WAR_CONFLICT",
        "POLITICS",
        "FINANCE",
        "LEGAL",
        "CSAI",
        "FRINGE",
        "THREAT",
        "SEVERE_TOXICITY",
        "TOXICITY",
        "SEXUAL",
        "INSULT",
        "DEROGATORY",
        "IDENTITY_ATTACK",
        "VIOLENCE_ABUSE",
        "OBSCENE",
        "DRUGS",
        "CSAM",
        "SPII",
        "DANGEROUS_CONTENT",
        "DANGEROUS_CONTENT_SEVERITY",
        "INSULT_SEVERITY",
        "DEROGATORY_SEVERITY",
        "SEXUAL_SEVERITY",
    ]
    score: float

@typing.type_check_only
class CloudAiNlLlmProtoServiceSafetyRating(typing_extensions.TypedDict, total=False):
    blocked: bool
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    ]
    probability: typing_extensions.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]

@typing.type_check_only
class CloudAiNlLlmProtoServiceUsageMetadata(typing_extensions.TypedDict, total=False):
    candidatesTokenCount: int
    promptTokenCount: int
    totalTokenCount: int

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ActiveLearningConfig(
    typing_extensions.TypedDict, total=False
):
    maxDataItemCount: str
    maxDataItemPercentage: int
    sampleConfig: GoogleCloudAiplatformV1beta1SampleConfig
    trainingConfig: GoogleCloudAiplatformV1beta1TrainingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsRequest(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[str]
    executions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextChildrenRequest(
    typing_extensions.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextChildrenResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddExecutionEventsRequest(
    typing_extensions.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1beta1Event]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddExecutionEventsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddTrialMeasurementRequest(
    typing_extensions.TypedDict, total=False
):
    measurement: GoogleCloudAiplatformV1beta1Measurement

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Annotation(typing_extensions.TypedDict, total=False):
    annotationSource: GoogleCloudAiplatformV1beta1UserActionReference
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    payloadSchemaUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AnnotationSpec(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Artifact(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    schemaTitle: str
    schemaVersion: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "LIVE"]
    updateTime: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssignNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssignNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
):
    notebookRuntime: GoogleCloudAiplatformV1beta1NotebookRuntime
    notebookRuntimeId: str
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Attribution(typing_extensions.TypedDict, total=False):
    approximationError: float
    baselineOutputValue: float
    featureAttributions: typing.Any
    instanceOutputValue: float
    outputDisplayName: str
    outputIndex: _list[int]
    outputName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AutomaticResources(
    typing_extensions.TypedDict, total=False
):
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AutoscalingMetricSpec(
    typing_extensions.TypedDict, total=False
):
    metricName: str
    target: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AvroSource(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCancelPipelineJobsRequest(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCancelPipelineJobsResponse(
    typing_extensions.TypedDict, total=False
):
    pipelineJobs: _list[GoogleCloudAiplatformV1beta1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateFeatureRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1beta1Feature]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateTensorboardRunRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsResponse(
    typing_extensions.TypedDict, total=False
):
    tensorboardRuns: _list[GoogleCloudAiplatformV1beta1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateTensorboardTimeSeriesRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesResponse(
    typing_extensions.TypedDict, total=False
):
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1beta1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDedicatedResources(
    typing_extensions.TypedDict, total=False
):
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    maxReplicaCount: int
    startingReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDeletePipelineJobsRequest(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDeletePipelineJobsResponse(
    typing_extensions.TypedDict, total=False
):
    pipelineJobs: _list[GoogleCloudAiplatformV1beta1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsRequest(
    typing_extensions.TypedDict, total=False
):
    evaluatedAnnotations: _list[GoogleCloudAiplatformV1beta1EvaluatedAnnotation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsResponse(
    typing_extensions.TypedDict, total=False
):
    importedEvaluatedAnnotationsCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportModelEvaluationSlicesRequest(
    typing_extensions.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1beta1ModelEvaluationSlice]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportModelEvaluationSlicesResponse(
    typing_extensions.TypedDict, total=False
):
    importedModelEvaluationSlices: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    partialResults: _list[
        GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadataPartialResult
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadataPartialResult(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    error: GoogleRpcStatus
    model: str
    request: GoogleCloudAiplatformV1beta1MigrateResourceRequest

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    migrateResourceRequests: _list[GoogleCloudAiplatformV1beta1MigrateResourceRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    migrateResourceResponses: _list[GoogleCloudAiplatformV1beta1MigrateResourceResponse]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJob(
    typing_extensions.TypedDict, total=False
):
    completionStats: GoogleCloudAiplatformV1beta1CompletionStats
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1BatchDedicatedResources
    disableContainerLogging: bool
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    generateExplanation: bool
    inputConfig: GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig
    instanceConfig: GoogleCloudAiplatformV1beta1BatchPredictionJobInstanceConfig
    labels: dict[str, typing.Any]
    manualBatchTuningParameters: GoogleCloudAiplatformV1beta1ManualBatchTuningParameters
    model: str
    modelMonitoringConfig: GoogleCloudAiplatformV1beta1ModelMonitoringConfig
    modelMonitoringStatsAnomalies: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies
    ]
    modelMonitoringStatus: GoogleRpcStatus
    modelParameters: typing.Any
    modelVersionId: str
    name: str
    outputConfig: GoogleCloudAiplatformV1beta1BatchPredictionJobOutputConfig
    outputInfo: GoogleCloudAiplatformV1beta1BatchPredictionJobOutputInfo
    partialFailures: _list[GoogleRpcStatus]
    resourcesConsumed: GoogleCloudAiplatformV1beta1ResourcesConsumed
    serviceAccount: str
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    unmanagedContainerModel: GoogleCloudAiplatformV1beta1UnmanagedContainerModel
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    instancesFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobInstanceConfig(
    typing_extensions.TypedDict, total=False
):
    excludedFields: _list[str]
    includedFields: _list[str]
    instanceType: str
    keyField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobOutputConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination
    predictionsFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobOutputInfo(
    typing_extensions.TypedDict, total=False
):
    bigqueryOutputDataset: str
    bigqueryOutputTable: str
    gcsOutputDirectory: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    bigqueryReadInstances: GoogleCloudAiplatformV1beta1BigQuerySource
    csvReadInstances: GoogleCloudAiplatformV1beta1CsvSource
    destination: GoogleCloudAiplatformV1beta1FeatureValueDestination
    entityTypeSpecs: _list[
        GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestEntityTypeSpec
    ]
    passThroughFields: _list[
        GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestPassThroughField
    ]
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestEntityTypeSpec(
    typing_extensions.TypedDict, total=False
):
    entityTypeId: str
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    settings: _list[GoogleCloudAiplatformV1beta1DestinationFeatureSetting]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestPassThroughField(
    typing_extensions.TypedDict, total=False
):
    fieldName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    timeSeriesData: _list[GoogleCloudAiplatformV1beta1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQuerySource(
    typing_extensions.TypedDict, total=False
):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Blob(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BlurBaselineConfig(
    typing_extensions.TypedDict, total=False
):
    maxBlurSigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BoolArray(typing_extensions.TypedDict, total=False):
    values: _list[bool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelBatchPredictionJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelCustomJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelDataLabelingJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelHyperparameterTuningJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelNasJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelPipelineJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelTrainingPipelineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Candidate(typing_extensions.TypedDict, total=False):
    citationMetadata: GoogleCloudAiplatformV1beta1CitationMetadata
    content: GoogleCloudAiplatformV1beta1Content
    finishMessage: str
    finishReason: typing_extensions.Literal[
        "FINISH_REASON_UNSPECIFIED",
        "STOP",
        "MAX_TOKENS",
        "SAFETY",
        "RECITATION",
        "OTHER",
    ]
    index: int
    safetyRatings: _list[GoogleCloudAiplatformV1beta1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateMetatdata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    study: str
    trial: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateResponse(
    typing_extensions.TypedDict, total=False
):
    shouldStop: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Citation(typing_extensions.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: GoogleTypeDate
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CitationMetadata(
    typing_extensions.TypedDict, total=False
):
    citations: _list[GoogleCloudAiplatformV1beta1Citation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompleteTrialRequest(
    typing_extensions.TypedDict, total=False
):
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
    infeasibleReason: str
    trialInfeasible: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompletionStats(
    typing_extensions.TypedDict, total=False
):
    failedCount: str
    incompleteCount: str
    successfulCount: str
    successfulForecastPointCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ComputeTokensRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ComputeTokensResponse(
    typing_extensions.TypedDict, total=False
):
    tokensInfo: _list[GoogleCloudAiplatformV1beta1TokensInfo]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContainerRegistryDestination(
    typing_extensions.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContainerSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    command: _list[str]
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    imageUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Content(typing_extensions.TypedDict, total=False):
    parts: _list[GoogleCloudAiplatformV1beta1Part]
    role: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Context(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    parentContexts: _list[str]
    schemaTitle: str
    schemaVersion: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelRequest(
    typing_extensions.TypedDict, total=False
):
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    modelId: str
    parentModel: str
    sourceModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelResponse(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    instances: _list[typing.Any]
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensResponse(
    typing_extensions.TypedDict, total=False
):
    totalBillableCharacters: int
    totalTokens: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDatasetVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolRequest(
    typing_extensions.TypedDict, total=False
):
    deploymentResourcePool: GoogleCloudAiplatformV1beta1DeploymentResourcePool
    deploymentResourcePoolId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateEntityTypeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateExtensionControllerOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureGroupOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureOnlineStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureRequest(
    typing_extensions.TypedDict, total=False
):
    feature: GoogleCloudAiplatformV1beta1Feature
    featureId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureViewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeaturestoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateIndexEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateMetadataStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateNotebookRuntimeTemplateOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreatePersistentResourceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreatePipelineJobRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    pipelineJob: GoogleCloudAiplatformV1beta1PipelineJob
    pipelineJobId: str
    preflightValidations: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateRegistryFeatureOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateSolverOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateSpecialistPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardRunRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    tensorboardRun: GoogleCloudAiplatformV1beta1TensorboardRun
    tensorboardRunId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardTimeSeriesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    tensorboardTimeSeries: GoogleCloudAiplatformV1beta1TensorboardTimeSeries
    tensorboardTimeSeriesId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CsvDestination(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CsvSource(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec
    labels: dict[str, typing.Any]
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    updateTime: str
    webAccessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomJobSpec(
    typing_extensions.TypedDict, total=False
):
    baseOutputDirectory: GoogleCloudAiplatformV1beta1GcsDestination
    enableDashboardAccess: bool
    enableWebAccess: bool
    experiment: str
    experimentRun: str
    models: _list[str]
    network: str
    persistentResourceId: str
    protectedArtifactLocationId: str
    reservedIpRanges: _list[str]
    scheduling: GoogleCloudAiplatformV1beta1Scheduling
    serviceAccount: str
    tensorboard: str
    workerPoolSpecs: _list[GoogleCloudAiplatformV1beta1WorkerPoolSpec]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataItem(typing_extensions.TypedDict, total=False):
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataItemView(
    typing_extensions.TypedDict, total=False
):
    annotations: _list[GoogleCloudAiplatformV1beta1Annotation]
    dataItem: GoogleCloudAiplatformV1beta1DataItem
    hasTruncatedAnnotations: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataLabelingJob(
    typing_extensions.TypedDict, total=False
):
    activeLearningConfig: GoogleCloudAiplatformV1beta1ActiveLearningConfig
    annotationLabels: dict[str, typing.Any]
    createTime: str
    currentSpend: GoogleTypeMoney
    datasets: _list[str]
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    error: GoogleRpcStatus
    inputs: typing.Any
    inputsSchemaUri: str
    instructionUri: str
    labelerCount: int
    labelingProgress: int
    labels: dict[str, typing.Any]
    name: str
    specialistPools: _list[str]
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Dataset(typing_extensions.TypedDict, total=False):
    createTime: str
    dataItemCount: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataArtifact: str
    metadataSchemaUri: str
    name: str
    savedQueries: _list[GoogleCloudAiplatformV1beta1SavedQuery]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetVersion(
    typing_extensions.TypedDict, total=False
):
    bigQueryDatasetName: str
    createTime: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DedicatedResources(
    typing_extensions.TypedDict, total=False
):
    autoscalingMetricSpecs: _list[GoogleCloudAiplatformV1beta1AutoscalingMetricSpec]
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectEntity
    selectTimeRangeAndFeature: GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectEntity(
    typing_extensions.TypedDict, total=False
):
    entityIdSelector: GoogleCloudAiplatformV1beta1EntityIdSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature(
    typing_extensions.TypedDict, total=False
):
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    skipOnlineStorageDelete: bool
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectEntity
    selectTimeRangeAndFeature: GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectTimeRangeAndFeature

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectEntity(
    typing_extensions.TypedDict, total=False
):
    offlineStorageDeletedEntityRowCount: str
    onlineStorageDeletedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectTimeRangeAndFeature(
    typing_extensions.TypedDict, total=False
):
    impactedFeatureCount: str
    offlineStorageModifiedEntityRowCount: str
    onlineStorageModifiedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteMetadataStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexResponse(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeploySolverOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndex(
    typing_extensions.TypedDict, total=False
):
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    deployedIndexAuthConfig: GoogleCloudAiplatformV1beta1DeployedIndexAuthConfig
    deploymentGroup: str
    displayName: str
    enableAccessLogging: bool
    id: str
    index: str
    indexSyncTime: str
    privateEndpoints: GoogleCloudAiplatformV1beta1IndexPrivateEndpoints
    reservedIpRanges: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexAuthConfig(
    typing_extensions.TypedDict, total=False
):
    authProvider: GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProvider

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProvider(
    typing_extensions.TypedDict, total=False
):
    allowedIssuers: _list[str]
    audiences: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexRef(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    displayName: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedModel(
    typing_extensions.TypedDict, total=False
):
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    disableExplanations: bool
    displayName: str
    enableAccessLogging: bool
    enableContainerLogging: bool
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    id: str
    model: str
    modelVersionId: str
    privateEndpoints: GoogleCloudAiplatformV1beta1PrivateEndpoints
    serviceAccount: str
    sharedResources: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedModelRef(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    endpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeploymentResourcePool(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DestinationFeatureSetting(
    typing_extensions.TypedDict, total=False
):
    destinationField: str
    featureId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectPredictRequest(
    typing_extensions.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectPredictResponse(
    typing_extensions.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectRawPredictRequest(
    typing_extensions.TypedDict, total=False
):
    input: str
    methodName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectRawPredictResponse(
    typing_extensions.TypedDict, total=False
):
    output: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DiskSpec(typing_extensions.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DoubleArray(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EncryptionSpec(
    typing_extensions.TypedDict, total=False
):
    kmsKeyName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Endpoint(typing_extensions.TypedDict, total=False):
    createTime: str
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModel]
    description: str
    displayName: str
    enablePrivateServiceConnect: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    modelDeploymentMonitoringJob: str
    name: str
    network: str
    predictRequestResponseLoggingConfig: GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfig
    trafficSplit: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EntityIdSelector(
    typing_extensions.TypedDict, total=False
):
    csvSource: GoogleCloudAiplatformV1beta1CsvSource
    entityIdField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EntityType(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    monitoringConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig
    name: str
    offlineStorageTtlDays: int
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnvVar(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotation(
    typing_extensions.TypedDict, total=False
):
    attributedItems: _list[
        GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem
    ]
    outlierScore: float
    outlierThreshold: float
    queryType: typing_extensions.Literal[
        "QUERY_TYPE_UNSPECIFIED",
        "ALL_SIMILAR",
        "SAME_CLASS_SIMILAR",
        "SAME_CLASS_DISSIMILAR",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem(
    typing_extensions.TypedDict, total=False
):
    annotationResourceName: str
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluatedAnnotation(
    typing_extensions.TypedDict, total=False
):
    dataItemPayload: typing.Any
    errorAnalysisAnnotations: _list[GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotation]
    evaluatedDataItemViewId: str
    explanations: _list[GoogleCloudAiplatformV1beta1EvaluatedAnnotationExplanation]
    groundTruths: _list[typing.Any]
    predictions: _list[typing.Any]
    type: typing_extensions.Literal[
        "EVALUATED_ANNOTATION_TYPE_UNSPECIFIED",
        "TRUE_POSITIVE",
        "FALSE_POSITIVE",
        "FALSE_NEGATIVE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluatedAnnotationExplanation(
    typing_extensions.TypedDict, total=False
):
    explanation: GoogleCloudAiplatformV1beta1Explanation
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Event(typing_extensions.TypedDict, total=False):
    artifact: str
    eventTime: str
    execution: str
    labels: dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INPUT", "OUTPUT"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Examples(typing_extensions.TypedDict, total=False):
    exampleGcsSource: GoogleCloudAiplatformV1beta1ExamplesExampleGcsSource
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    nearestNeighborSearchConfig: typing.Any
    neighborCount: int
    presets: GoogleCloudAiplatformV1beta1Presets

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesExampleGcsSource(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal["DATA_FORMAT_UNSPECIFIED", "JSONL"]
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesOverride(
    typing_extensions.TypedDict, total=False
):
    crowdingCount: int
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "INSTANCES", "EMBEDDINGS"
    ]
    neighborCount: int
    restrictions: _list[GoogleCloudAiplatformV1beta1ExamplesRestrictionsNamespace]
    returnEmbeddings: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesRestrictionsNamespace(
    typing_extensions.TypedDict, total=False
):
    allow: _list[str]
    deny: _list[str]
    namespaceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Execution(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    schemaTitle: str
    schemaVersion: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "NEW",
        "RUNNING",
        "COMPLETE",
        "FAILED",
        "CACHED",
        "CANCELLED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainRequest(
    typing_extensions.TypedDict, total=False
):
    concurrentExplanationSpecOverride: dict[str, typing.Any]
    deployedModelId: str
    explanationSpecOverride: GoogleCloudAiplatformV1beta1ExplanationSpecOverride
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainResponse(
    typing_extensions.TypedDict, total=False
):
    concurrentExplanations: dict[str, typing.Any]
    deployedModelId: str
    explanations: _list[GoogleCloudAiplatformV1beta1Explanation]
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainResponseConcurrentExplanation(
    typing_extensions.TypedDict, total=False
):
    explanations: _list[GoogleCloudAiplatformV1beta1Explanation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Explanation(typing_extensions.TypedDict, total=False):
    attributions: _list[GoogleCloudAiplatformV1beta1Attribution]
    neighbors: _list[GoogleCloudAiplatformV1beta1Neighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadata(
    typing_extensions.TypedDict, total=False
):
    featureAttributionsSchemaUri: str
    inputs: dict[str, typing.Any]
    latentSpaceSource: str
    outputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadata(
    typing_extensions.TypedDict, total=False
):
    denseShapeTensorName: str
    encodedBaselines: _list[typing.Any]
    encodedTensorName: str
    encoding: typing_extensions.Literal[
        "ENCODING_UNSPECIFIED",
        "IDENTITY",
        "BAG_OF_FEATURES",
        "BAG_OF_FEATURES_SPARSE",
        "INDICATOR",
        "COMBINED_EMBEDDING",
        "CONCAT_EMBEDDING",
    ]
    featureValueDomain: GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomain
    groupName: str
    indexFeatureMapping: _list[str]
    indicesTensorName: str
    inputBaselines: _list[typing.Any]
    inputTensorName: str
    modality: str
    visualization: GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataVisualization

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomain(
    typing_extensions.TypedDict, total=False
):
    maxValue: float
    minValue: float
    originalMean: float
    originalStddev: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataVisualization(
    typing_extensions.TypedDict, total=False
):
    clipPercentLowerbound: float
    clipPercentUpperbound: float
    colorMap: typing_extensions.Literal[
        "COLOR_MAP_UNSPECIFIED",
        "PINK_GREEN",
        "VIRIDIS",
        "RED",
        "GREEN",
        "RED_GREEN",
        "PINK_WHITE_GREEN",
    ]
    overlayType: typing_extensions.Literal[
        "OVERLAY_TYPE_UNSPECIFIED", "NONE", "ORIGINAL", "GRAYSCALE", "MASK_BLACK"
    ]
    polarity: typing_extensions.Literal[
        "POLARITY_UNSPECIFIED", "POSITIVE", "NEGATIVE", "BOTH"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PIXELS", "OUTLINES"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOutputMetadata(
    typing_extensions.TypedDict, total=False
):
    displayNameMappingKey: str
    indexDisplayNameMapping: typing.Any
    outputTensorName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOverride(
    typing_extensions.TypedDict, total=False
):
    inputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOverrideInputMetadataOverride(
    typing_extensions.TypedDict, total=False
):
    inputBaselines: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationParameters(
    typing_extensions.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1beta1Examples
    integratedGradientsAttribution: GoogleCloudAiplatformV1beta1IntegratedGradientsAttribution
    outputIndices: _list[typing.Any]
    sampledShapleyAttribution: GoogleCloudAiplatformV1beta1SampledShapleyAttribution
    topK: int
    xraiAttribution: GoogleCloudAiplatformV1beta1XraiAttribution

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationSpec(
    typing_extensions.TypedDict, total=False
):
    metadata: GoogleCloudAiplatformV1beta1ExplanationMetadata
    parameters: GoogleCloudAiplatformV1beta1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationSpecOverride(
    typing_extensions.TypedDict, total=False
):
    examplesOverride: GoogleCloudAiplatformV1beta1ExamplesOverride
    metadata: GoogleCloudAiplatformV1beta1ExplanationMetadataOverride
    parameters: GoogleCloudAiplatformV1beta1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataConfig(
    typing_extensions.TypedDict, total=False
):
    annotationsFilter: str
    fractionSplit: GoogleCloudAiplatformV1beta1ExportFractionSplit
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    gcsOutputDirectory: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataRequest(
    typing_extensions.TypedDict, total=False
):
    exportConfig: GoogleCloudAiplatformV1beta1ExportDataConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataResponse(
    typing_extensions.TypedDict, total=False
):
    exportedFiles: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportEndpointResponse(
    typing_extensions.TypedDict, total=False
):
    outputInfo: GoogleCloudAiplatformV1beta1ExportEndpointResponseOutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportEndpointResponseOutputInfo(
    typing_extensions.TypedDict, total=False
):
    bigQueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    destination: GoogleCloudAiplatformV1beta1FeatureValueDestination
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    fullExport: GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestFullExport
    settings: _list[GoogleCloudAiplatformV1beta1DestinationFeatureSetting]
    snapshotExport: GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestSnapshotExport

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestFullExport(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestSnapshotExport(
    typing_extensions.TypedDict, total=False
):
    snapshotTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFractionSplit(
    typing_extensions.TypedDict, total=False
):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    outputInfo: GoogleCloudAiplatformV1beta1ExportModelOperationMetadataOutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelOperationMetadataOutputInfo(
    typing_extensions.TypedDict, total=False
):
    artifactOutputUri: str
    imageOutputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelRequest(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudAiplatformV1beta1ExportModelRequestOutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelRequestOutputConfig(
    typing_extensions.TypedDict, total=False
):
    artifactDestination: GoogleCloudAiplatformV1beta1GcsDestination
    exportFormatId: str
    imageDestination: GoogleCloudAiplatformV1beta1ContainerRegistryDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    timeSeriesDataPoints: _list[GoogleCloudAiplatformV1beta1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Feature(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    disableMonitoring: bool
    etag: str
    labels: dict[str, typing.Any]
    monitoringConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig
    monitoringStats: _list[GoogleCloudAiplatformV1beta1FeatureStatsAnomaly]
    monitoringStatsAnomalies: _list[
        GoogleCloudAiplatformV1beta1FeatureMonitoringStatsAnomaly
    ]
    name: str
    updateTime: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "BOOL_ARRAY",
        "DOUBLE",
        "DOUBLE_ARRAY",
        "INT64",
        "INT64_ARRAY",
        "STRING",
        "STRING_ARRAY",
        "BYTES",
    ]
    versionColumnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureGroup(
    typing_extensions.TypedDict, total=False
):
    bigQuery: GoogleCloudAiplatformV1beta1FeatureGroupBigQuery
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureGroupBigQuery(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    entityIdColumns: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitoringStatsAnomaly(
    typing_extensions.TypedDict, total=False
):
    featureStatsAnomaly: GoogleCloudAiplatformV1beta1FeatureStatsAnomaly
    objective: typing_extensions.Literal[
        "OBJECTIVE_UNSPECIFIED", "IMPORT_FEATURE_ANALYSIS", "SNAPSHOT_ANALYSIS"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureNoiseSigma(
    typing_extensions.TypedDict, total=False
):
    noiseSigma: _list[GoogleCloudAiplatformV1beta1FeatureNoiseSigmaNoiseSigmaForFeature]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureNoiseSigmaNoiseSigmaForFeature(
    typing_extensions.TypedDict, total=False
):
    name: str
    sigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStore(
    typing_extensions.TypedDict, total=False
):
    bigtable: GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtable
    createTime: str
    dedicatedServingEndpoint: GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpoint
    embeddingManagement: GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagement
    etag: str
    labels: dict[str, typing.Any]
    name: str
    optimized: GoogleCloudAiplatformV1beta1FeatureOnlineStoreOptimized
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtable(
    typing_extensions.TypedDict, total=False
):
    autoScaling: GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableAutoScaling

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableAutoScaling(
    typing_extensions.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpoint(
    typing_extensions.TypedDict, total=False
):
    privateServiceConnectConfig: GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig
    publicEndpointDomainName: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagement(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreOptimized(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureSelector(
    typing_extensions.TypedDict, total=False
):
    idMatcher: GoogleCloudAiplatformV1beta1IdMatcher

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureStatsAnomaly(
    typing_extensions.TypedDict, total=False
):
    anomalyDetectionThreshold: float
    anomalyUri: str
    distributionDeviation: float
    endTime: str
    score: float
    startTime: str
    statsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValue(
    typing_extensions.TypedDict, total=False
):
    boolArrayValue: GoogleCloudAiplatformV1beta1BoolArray
    boolValue: bool
    bytesValue: str
    doubleArrayValue: GoogleCloudAiplatformV1beta1DoubleArray
    doubleValue: float
    int64ArrayValue: GoogleCloudAiplatformV1beta1Int64Array
    int64Value: str
    metadata: GoogleCloudAiplatformV1beta1FeatureValueMetadata
    stringArrayValue: GoogleCloudAiplatformV1beta1StringArray
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueDestination(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    csvDestination: GoogleCloudAiplatformV1beta1CsvDestination
    tfrecordDestination: GoogleCloudAiplatformV1beta1TFRecordDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueList(
    typing_extensions.TypedDict, total=False
):
    values: _list[GoogleCloudAiplatformV1beta1FeatureValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueMetadata(
    typing_extensions.TypedDict, total=False
):
    generateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureView(typing_extensions.TypedDict, total=False):
    bigQuerySource: GoogleCloudAiplatformV1beta1FeatureViewBigQuerySource
    createTime: str
    etag: str
    featureRegistrySource: GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySource
    labels: dict[str, typing.Any]
    name: str
    syncConfig: GoogleCloudAiplatformV1beta1FeatureViewSyncConfig
    updateTime: str
    vectorSearchConfig: GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    entityIdColumns: _list[str]
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDataKey(
    typing_extensions.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySource(
    typing_extensions.TypedDict, total=False
):
    featureGroups: _list[
        GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySourceFeatureGroup
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySourceFeatureGroup(
    typing_extensions.TypedDict, total=False
):
    featureGroupId: str
    featureIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewSync(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    finalStatus: GoogleRpcStatus
    name: str
    runTime: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewSyncConfig(
    typing_extensions.TypedDict, total=False
):
    cron: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig(
    typing_extensions.TypedDict, total=False
):
    bruteForceConfig: GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigBruteForceConfig
    crowdingColumn: str
    distanceMeasureType: typing_extensions.Literal[
        "DISTANCE_MEASURE_TYPE_UNSPECIFIED",
        "SQUARED_L2_DISTANCE",
        "COSINE_DISTANCE",
        "DOT_PRODUCT_DISTANCE",
    ]
    embeddingColumn: str
    embeddingDimension: int
    filterColumns: _list[str]
    treeAhConfig: GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigBruteForceConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig(
    typing_extensions.TypedDict, total=False
):
    leafNodeEmbeddingCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Featurestore(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    onlineServingConfig: GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfig
    onlineStorageTtlDays: int
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig(
    typing_extensions.TypedDict, total=False
):
    categoricalThresholdConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig
    importFeaturesAnalysis: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigImportFeaturesAnalysis
    numericalThresholdConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig
    snapshotAnalysis: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigSnapshotAnalysis

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigImportFeaturesAnalysis(
    typing_extensions.TypedDict, total=False
):
    anomalyDetectionBaseline: typing_extensions.Literal[
        "BASELINE_UNSPECIFIED",
        "LATEST_STATS",
        "MOST_RECENT_SNAPSHOT_STATS",
        "PREVIOUS_IMPORT_FEATURES_STATS",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "DEFAULT", "ENABLED", "DISABLED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigSnapshotAnalysis(
    typing_extensions.TypedDict, total=False
):
    disabled: bool
    monitoringInterval: str
    monitoringIntervalDays: int
    stalenessDays: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig(
    typing_extensions.TypedDict, total=False
):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfig(
    typing_extensions.TypedDict, total=False
):
    fixedNodeCount: int
    scaling: GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling(
    typing_extensions.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal[
        "FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED", "KEY_VALUE", "PROTO_STRUCT"
    ]
    dataKey: GoogleCloudAiplatformV1beta1FeatureViewDataKey
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "KEY_VALUE", "PROTO_STRUCT"]
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    keyValues: GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairList
    protoStruct: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairList(
    typing_extensions.TypedDict, total=False
):
    features: _list[
        GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: GoogleCloudAiplatformV1beta1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FileData(typing_extensions.TypedDict, total=False):
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FilterSplit(typing_extensions.TypedDict, total=False):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    queries: _list[GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery]
    returnFullDatapoint: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery(
    typing_extensions.TypedDict, total=False
):
    approximateNeighborCount: int
    datapoint: GoogleCloudAiplatformV1beta1IndexDatapoint
    fractionLeafNodesToSearchOverride: float
    neighborCount: int
    perCrowdingAttributeNeighborCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponse(
    typing_extensions.TypedDict, total=False
):
    nearestNeighbors: _list[
        GoogleCloudAiplatformV1beta1FindNeighborsResponseNearestNeighbors
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponseNearestNeighbors(
    typing_extensions.TypedDict, total=False
):
    id: str
    neighbors: _list[GoogleCloudAiplatformV1beta1FindNeighborsResponseNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponseNeighbor(
    typing_extensions.TypedDict, total=False
):
    datapoint: GoogleCloudAiplatformV1beta1IndexDatapoint
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FractionSplit(
    typing_extensions.TypedDict, total=False
):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionCall(
    typing_extensions.TypedDict, total=False
):
    args: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionDeclaration(
    typing_extensions.TypedDict, total=False
):
    description: str
    name: str
    parameters: GoogleCloudAiplatformV1beta1Schema

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionResponse(
    typing_extensions.TypedDict, total=False
):
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateAccessTokenRequest(
    typing_extensions.TypedDict, total=False
):
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateAccessTokenResponse(
    typing_extensions.TypedDict, total=False
):
    accessToken: str
    expiresIn: int
    scope: str
    tokenType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    safetySettings: _list[GoogleCloudAiplatformV1beta1SafetySetting]
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponse(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1beta1Candidate]
    promptFeedback: GoogleCloudAiplatformV1beta1GenerateContentResponsePromptFeedback
    usageMetadata: GoogleCloudAiplatformV1beta1GenerateContentResponseUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponsePromptFeedback(
    typing_extensions.TypedDict, total=False
):
    blockReason: typing_extensions.Literal[
        "BLOCKED_REASON_UNSPECIFIED", "SAFETY", "OTHER"
    ]
    blockReasonMessage: str
    safetyRatings: _list[GoogleCloudAiplatformV1beta1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponseUsageMetadata(
    typing_extensions.TypedDict, total=False
):
    candidatesTokenCount: int
    promptTokenCount: int
    totalTokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfig(
    typing_extensions.TypedDict, total=False
):
    candidateCount: int
    maxOutputTokens: int
    stopSequences: _list[str]
    temperature: float
    topK: float
    topP: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenericOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    partialFailures: _list[GoogleRpcStatus]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1HyperparameterTuningJob(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    maxFailedTrialCount: int
    maxTrialCount: int
    name: str
    parallelTrialCount: int
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec
    trials: _list[GoogleCloudAiplatformV1beta1Trial]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IdMatcher(typing_extensions.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataConfig(
    typing_extensions.TypedDict, total=False
):
    annotationLabels: dict[str, typing.Any]
    dataItemLabels: dict[str, typing.Any]
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    importSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataRequest(
    typing_extensions.TypedDict, total=False
):
    importConfigs: _list[GoogleCloudAiplatformV1beta1ImportDataConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportExtensionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    blockingOperationIds: _list[str]
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    sourceUris: _list[str]
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    avroSource: GoogleCloudAiplatformV1beta1AvroSource
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    csvSource: GoogleCloudAiplatformV1beta1CsvSource
    disableIngestionAnalysis: bool
    disableOnlineServing: bool
    entityIdField: str
    featureSpecs: _list[
        GoogleCloudAiplatformV1beta1ImportFeatureValuesRequestFeatureSpec
    ]
    featureTime: str
    featureTimeField: str
    workerCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesRequestFeatureSpec(
    typing_extensions.TypedDict, total=False
):
    id: str
    sourceField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportModelEvaluationRequest(
    typing_extensions.TypedDict, total=False
):
    modelEvaluation: GoogleCloudAiplatformV1beta1ModelEvaluation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Index(typing_extensions.TypedDict, total=False):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1beta1DeployedIndexRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    indexStats: GoogleCloudAiplatformV1beta1IndexStats
    indexUpdateMethod: typing_extensions.Literal[
        "INDEX_UPDATE_METHOD_UNSPECIFIED", "BATCH_UPDATE", "STREAM_UPDATE"
    ]
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataSchemaUri: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapoint(
    typing_extensions.TypedDict, total=False
):
    crowdingTag: GoogleCloudAiplatformV1beta1IndexDatapointCrowdingTag
    datapointId: str
    featureVector: _list[float]
    numericRestricts: _list[
        GoogleCloudAiplatformV1beta1IndexDatapointNumericRestriction
    ]
    restricts: _list[GoogleCloudAiplatformV1beta1IndexDatapointRestriction]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointCrowdingTag(
    typing_extensions.TypedDict, total=False
):
    crowdingAttribute: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointNumericRestriction(
    typing_extensions.TypedDict, total=False
):
    namespace: str
    op: typing_extensions.Literal[
        "OPERATOR_UNSPECIFIED",
        "LESS",
        "LESS_EQUAL",
        "EQUAL",
        "GREATER_EQUAL",
        "GREATER",
    ]
    valueDouble: float
    valueFloat: float
    valueInt: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointRestriction(
    typing_extensions.TypedDict, total=False
):
    allowList: _list[str]
    denyList: _list[str]
    namespace: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexEndpoint(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1beta1DeployedIndex]
    description: str
    displayName: str
    enablePrivateServiceConnect: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    privateServiceConnectConfig: GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig
    publicEndpointDomainName: str
    publicEndpointEnabled: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexPrivateEndpoints(
    typing_extensions.TypedDict, total=False
):
    matchGrpcAddress: str
    pscAutomatedEndpoints: _list[GoogleCloudAiplatformV1beta1PscAutomatedEndpoints]
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexStats(typing_extensions.TypedDict, total=False):
    shardsCount: int
    vectorsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1InputDataConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSchemaUri: str
    annotationsFilter: str
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    datasetId: str
    filterSplit: GoogleCloudAiplatformV1beta1FilterSplit
    fractionSplit: GoogleCloudAiplatformV1beta1FractionSplit
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination
    persistMlUseAssignment: bool
    predefinedSplit: GoogleCloudAiplatformV1beta1PredefinedSplit
    savedQueryId: str
    stratifiedSplit: GoogleCloudAiplatformV1beta1StratifiedSplit
    timestampSplit: GoogleCloudAiplatformV1beta1TimestampSplit

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Int64Array(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IntegratedGradientsAttribution(
    typing_extensions.TypedDict, total=False
):
    blurBaselineConfig: GoogleCloudAiplatformV1beta1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1beta1SmoothGradConfig
    stepCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance(
    typing_extensions.TypedDict, total=False
):
    serviceName: typing_extensions.Literal[
        "INTERNAL_OS_SERVICE_ENUM_UNSPECIFIED",
        "DOCKER_SERVICE_STATE",
        "CONTROL_PLANE_API_DNS_STATE",
        "PROXY_REGISTRATION_DNS_STATE",
        "JUPYTER_STATE",
        "JUPYTER_API_STATE",
        "EUC_METADATA_API_STATE",
        "EUC_AGENT_API_STATE",
        "IDLE_SHUTDOWN_AGENT_STATE",
        "PROXY_AGENT_STATE",
    ]
    serviceState: typing_extensions.Literal["UNKNOWN", "HEALTHY", "UNHEALTHY"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LargeModelReference(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LineageSubgraph(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]
    events: _list[GoogleCloudAiplatformV1beta1Event]
    executions: _list[GoogleCloudAiplatformV1beta1Execution]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAnnotationsResponse(
    typing_extensions.TypedDict, total=False
):
    annotations: _list[GoogleCloudAiplatformV1beta1Annotation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListArtifactsResponse(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponse(
    typing_extensions.TypedDict, total=False
):
    batchPredictionJobs: _list[GoogleCloudAiplatformV1beta1BatchPredictionJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListContextsResponse(
    typing_extensions.TypedDict, total=False
):
    contexts: _list[GoogleCloudAiplatformV1beta1Context]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListCustomJobsResponse(
    typing_extensions.TypedDict, total=False
):
    customJobs: _list[GoogleCloudAiplatformV1beta1CustomJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataItemsResponse(
    typing_extensions.TypedDict, total=False
):
    dataItems: _list[GoogleCloudAiplatformV1beta1DataItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponse(
    typing_extensions.TypedDict, total=False
):
    dataLabelingJobs: _list[GoogleCloudAiplatformV1beta1DataLabelingJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    datasetVersions: _list[GoogleCloudAiplatformV1beta1DatasetVersion]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetsResponse(
    typing_extensions.TypedDict, total=False
):
    datasets: _list[GoogleCloudAiplatformV1beta1Dataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponse(
    typing_extensions.TypedDict, total=False
):
    deploymentResourcePools: _list[GoogleCloudAiplatformV1beta1DeploymentResourcePool]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEndpointsResponse(
    typing_extensions.TypedDict, total=False
):
    endpoints: _list[GoogleCloudAiplatformV1beta1Endpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudAiplatformV1beta1EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    executions: _list[GoogleCloudAiplatformV1beta1Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    featureGroups: _list[GoogleCloudAiplatformV1beta1FeatureGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponse(
    typing_extensions.TypedDict, total=False
):
    featureOnlineStores: _list[GoogleCloudAiplatformV1beta1FeatureOnlineStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponse(
    typing_extensions.TypedDict, total=False
):
    featureViewSyncs: _list[GoogleCloudAiplatformV1beta1FeatureViewSync]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureViewsResponse(
    typing_extensions.TypedDict, total=False
):
    featureViews: _list[GoogleCloudAiplatformV1beta1FeatureView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1beta1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturestoresResponse(
    typing_extensions.TypedDict, total=False
):
    featurestores: _list[GoogleCloudAiplatformV1beta1Featurestore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponse(
    typing_extensions.TypedDict, total=False
):
    hyperparameterTuningJobs: _list[GoogleCloudAiplatformV1beta1HyperparameterTuningJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexEndpointsResponse(
    typing_extensions.TypedDict, total=False
):
    indexEndpoints: _list[GoogleCloudAiplatformV1beta1IndexEndpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: _list[GoogleCloudAiplatformV1beta1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataSchemasResponse(
    typing_extensions.TypedDict, total=False
):
    metadataSchemas: _list[GoogleCloudAiplatformV1beta1MetadataSchema]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataStoresResponse(
    typing_extensions.TypedDict, total=False
):
    metadataStores: _list[GoogleCloudAiplatformV1beta1MetadataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponse(
    typing_extensions.TypedDict, total=False
):
    modelDeploymentMonitoringJobs: _list[
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponse(
    typing_extensions.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1beta1ModelEvaluationSlice]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationsResponse(
    typing_extensions.TypedDict, total=False
):
    modelEvaluations: _list[GoogleCloudAiplatformV1beta1ModelEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudAiplatformV1beta1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudAiplatformV1beta1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nasJobs: _list[GoogleCloudAiplatformV1beta1NasJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponse(
    typing_extensions.TypedDict, total=False
):
    nasTrialDetails: _list[GoogleCloudAiplatformV1beta1NasTrialDetail]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimeTemplates: _list[GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimes: _list[GoogleCloudAiplatformV1beta1NotebookRuntime]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOptimalTrialsRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOptimalTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    optimalTrials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPersistentResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    persistentResources: _list[GoogleCloudAiplatformV1beta1PersistentResource]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPipelineJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pipelineJobs: _list[GoogleCloudAiplatformV1beta1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPublisherModelsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    publisherModels: _list[GoogleCloudAiplatformV1beta1PublisherModel]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSavedQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    savedQueries: _list[GoogleCloudAiplatformV1beta1SavedQuery]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSchedulesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    schedules: _list[GoogleCloudAiplatformV1beta1Schedule]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    specialistPools: _list[GoogleCloudAiplatformV1beta1SpecialistPool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListStudiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    studies: _list[GoogleCloudAiplatformV1beta1Study]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardExperiments: _list[GoogleCloudAiplatformV1beta1TensorboardExperiment]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardRunsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardRuns: _list[GoogleCloudAiplatformV1beta1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1beta1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboards: _list[GoogleCloudAiplatformV1beta1Tensorboard]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    trainingPipelines: _list[GoogleCloudAiplatformV1beta1TrainingPipeline]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    trials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LookupStudyRequest(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MachineSpec(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_A100_80GB",
        "NVIDIA_L4",
        "NVIDIA_H100_80GB",
        "TPU_V2",
        "TPU_V3",
        "TPU_V4_POD",
        "TPU_V5_LITEPOD",
    ]
    machineType: str
    tpuTopology: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ManualBatchTuningParameters(
    typing_extensions.TypedDict, total=False
):
    batchSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Measurement(typing_extensions.TypedDict, total=False):
    elapsedDuration: str
    metrics: _list[GoogleCloudAiplatformV1beta1MeasurementMetric]
    stepCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MeasurementMetric(
    typing_extensions.TypedDict, total=False
):
    metricId: str
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MergeVersionAliasesRequest(
    typing_extensions.TypedDict, total=False
):
    versionAliases: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataSchema(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    name: str
    schema: str
    schemaType: typing_extensions.Literal[
        "METADATA_SCHEMA_TYPE_UNSPECIFIED",
        "ARTIFACT_TYPE",
        "EXECUTION_TYPE",
        "CONTEXT_TYPE",
    ]
    schemaVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataStore(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    name: str
    state: GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreState
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreState(
    typing_extensions.TypedDict, total=False
):
    diskUtilizationBytes: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResource(
    typing_extensions.TypedDict, total=False
):
    automlDataset: GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset
    automlModel: GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel
    dataLabelingDataset: GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset
    lastMigrateTime: str
    lastUpdateTime: str
    mlEngineModelVersion: GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset(
    typing_extensions.TypedDict, total=False
):
    dataLabelingAnnotatedDatasets: _list[
        GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset
    ]
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    annotatedDatasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequest(
    typing_extensions.TypedDict, total=False
):
    migrateAutomlDatasetConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlDatasetConfig
    migrateAutomlModelConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlModelConfig
    migrateDataLabelingDatasetConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfig
    migrateMlEngineModelVersionConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateMlEngineModelVersionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlModelConfig(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str
    migrateDataLabelingAnnotatedDatasetConfigs: _list[
        GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateMlEngineModelVersionConfig(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    modelDisplayName: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceResponse(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    migratableResource: GoogleCloudAiplatformV1beta1MigratableResource
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Model(typing_extensions.TypedDict, total=False):
    artifactUri: str
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    createTime: str
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModelRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataArtifact: str
    metadataSchemaUri: str
    modelSourceInfo: GoogleCloudAiplatformV1beta1ModelSourceInfo
    name: str
    originalModelInfo: GoogleCloudAiplatformV1beta1ModelOriginalModelInfo
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata
    supportedDeploymentResourcesTypes: _list[
        typing_extensions.Literal[
            "DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED",
            "DEDICATED_RESOURCES",
            "AUTOMATIC_RESOURCES",
            "SHARED_RESOURCES",
        ]
    ]
    supportedExportFormats: _list[GoogleCloudAiplatformV1beta1ModelExportFormat]
    supportedInputStorageFormats: _list[str]
    supportedOutputStorageFormats: _list[str]
    trainingPipeline: str
    updateTime: str
    versionAliases: _list[str]
    versionCreateTime: str
    versionDescription: str
    versionId: str
    versionUpdateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelContainerSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    command: _list[str]
    deploymentTimeout: str
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    grpcPorts: _list[GoogleCloudAiplatformV1beta1Port]
    healthProbe: GoogleCloudAiplatformV1beta1Probe
    healthRoute: str
    imageUri: str
    ports: _list[GoogleCloudAiplatformV1beta1Port]
    predictRoute: str
    sharedMemorySizeMb: str
    startupProbe: GoogleCloudAiplatformV1beta1Probe

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable(
    typing_extensions.TypedDict, total=False
):
    bigqueryTablePath: str
    logSource: typing_extensions.Literal[
        "LOG_SOURCE_UNSPECIFIED", "TRAINING", "SERVING"
    ]
    logType: typing_extensions.Literal["LOG_TYPE_UNSPECIFIED", "PREDICT", "EXPLAIN"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob(
    typing_extensions.TypedDict, total=False
):
    analysisInstanceSchemaUri: str
    bigqueryTables: _list[
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable
    ]
    createTime: str
    displayName: str
    enableMonitoringPipelineLogs: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endpoint: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    latestMonitoringPipelineMetadata: GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata
    logTtl: str
    loggingSamplingStrategy: GoogleCloudAiplatformV1beta1SamplingStrategy
    modelDeploymentMonitoringObjectiveConfigs: _list[
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfig
    ]
    modelDeploymentMonitoringScheduleConfig: GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig
    modelMonitoringAlertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig
    name: str
    nextScheduleTime: str
    predictInstanceSchemaUri: str
    samplePredictInstance: typing.Any
    scheduleState: typing_extensions.Literal[
        "MONITORING_SCHEDULE_STATE_UNSPECIFIED", "PENDING", "OFFLINE", "RUNNING"
    ]
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    statsAnomaliesBaseDirectory: GoogleCloudAiplatformV1beta1GcsDestination
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata(
    typing_extensions.TypedDict, total=False
):
    runTime: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    objectiveConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig(
    typing_extensions.TypedDict, total=False
):
    monitorInterval: str
    monitorWindow: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluation(
    typing_extensions.TypedDict, total=False
):
    biasConfigs: GoogleCloudAiplatformV1beta1ModelEvaluationBiasConfig
    createTime: str
    displayName: str
    explanationSpecs: _list[
        GoogleCloudAiplatformV1beta1ModelEvaluationModelEvaluationExplanationSpec
    ]
    metadata: typing.Any
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1beta1ModelExplanation
    name: str
    sliceDimensions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationBiasConfig(
    typing_extensions.TypedDict, total=False
):
    biasSlices: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec
    labels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationModelEvaluationExplanationSpec(
    typing_extensions.TypedDict, total=False
):
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSlice(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1beta1ModelExplanation
    name: str
    slice: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice(
    typing_extensions.TypedDict, total=False
):
    dimension: str
    sliceSpec: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec(
    typing_extensions.TypedDict, total=False
):
    configs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange(
    typing_extensions.TypedDict, total=False
):
    high: float
    low: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecSliceConfig(
    typing_extensions.TypedDict, total=False
):
    allValues: bool
    range: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange
    value: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue(
    typing_extensions.TypedDict, total=False
):
    floatValue: float
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelExplanation(
    typing_extensions.TypedDict, total=False
):
    meanAttributions: _list[GoogleCloudAiplatformV1beta1Attribution]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelExportFormat(
    typing_extensions.TypedDict, total=False
):
    exportableContents: _list[
        typing_extensions.Literal["EXPORTABLE_CONTENT_UNSPECIFIED", "ARTIFACT", "IMAGE"]
    ]
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig(
    typing_extensions.TypedDict, total=False
):
    emailAlertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig
    enableLogging: bool
    notificationChannels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig(
    typing_extensions.TypedDict, total=False
):
    userEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringConfig(
    typing_extensions.TypedDict, total=False
):
    alertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig
    analysisInstanceSchemaUri: str
    objectiveConfigs: _list[GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig]
    statsAnomaliesBaseDirectory: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    explanationConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfig
    predictionDriftDetectionConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig
    trainingDataset: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDataset
    trainingPredictionSkewDetectionConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfig(
    typing_extensions.TypedDict, total=False
):
    enableFeatureAttributes: bool
    explanationBaseline: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline(
    typing_extensions.TypedDict, total=False
):
    bigquery: GoogleCloudAiplatformV1beta1BigQueryDestination
    gcs: GoogleCloudAiplatformV1beta1GcsDestination
    predictionFormat: typing_extensions.Literal[
        "PREDICTION_FORMAT_UNSPECIFIED", "JSONL", "BIGQUERY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    attributionScoreDriftThresholds: dict[str, typing.Any]
    defaultDriftThreshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    driftThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDataset(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    dataFormat: str
    dataset: str
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    loggingSamplingStrategy: GoogleCloudAiplatformV1beta1SamplingStrategy
    targetField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    attributionScoreSkewThresholds: dict[str, typing.Any]
    defaultSkewThreshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    skewThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies(
    typing_extensions.TypedDict, total=False
):
    anomalyCount: int
    deployedModelId: str
    featureStats: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies
    ]
    objective: typing_extensions.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies(
    typing_extensions.TypedDict, total=False
):
    featureDisplayName: str
    predictionStats: _list[GoogleCloudAiplatformV1beta1FeatureStatsAnomaly]
    threshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    trainingStats: GoogleCloudAiplatformV1beta1FeatureStatsAnomaly

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelOriginalModelInfo(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelSourceInfo(
    typing_extensions.TypedDict, total=False
):
    copy: bool
    sourceType: typing_extensions.Literal[
        "MODEL_SOURCE_TYPE_UNSPECIFIED",
        "AUTOML",
        "CUSTOM",
        "BQML",
        "MODEL_GARDEN",
        "GENIE",
        "CUSTOM_TEXT_EMBEDDING",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedIndexResponse(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    enableRestrictedImageTraining: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    nasJobOutput: GoogleCloudAiplatformV1beta1NasJobOutput
    nasJobSpec: GoogleCloudAiplatformV1beta1NasJobSpec
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobOutput(
    typing_extensions.TypedDict, total=False
):
    multiTrialJobOutput: GoogleCloudAiplatformV1beta1NasJobOutputMultiTrialJobOutput

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobOutputMultiTrialJobOutput(
    typing_extensions.TypedDict, total=False
):
    searchTrials: _list[GoogleCloudAiplatformV1beta1NasTrial]
    trainTrials: _list[GoogleCloudAiplatformV1beta1NasTrial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpec(typing_extensions.TypedDict, total=False):
    multiTrialAlgorithmSpec: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec
    resumeNasJobId: str
    searchSpaceSpec: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec(
    typing_extensions.TypedDict, total=False
):
    metric: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec
    multiTrialAlgorithm: typing_extensions.Literal[
        "MULTI_TRIAL_ALGORITHM_UNSPECIFIED", "REINFORCEMENT_LEARNING", "GRID_SEARCH"
    ]
    searchTrialSpec: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec
    trainTrialSpec: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec(
    typing_extensions.TypedDict, total=False
):
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec(
    typing_extensions.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxParallelTrialCount: int
    maxTrialCount: int
    searchTrialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec(
    typing_extensions.TypedDict, total=False
):
    frequency: int
    maxParallelTrialCount: int
    trainTrialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasTrial(typing_extensions.TypedDict, total=False):
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
    id: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "REQUESTED",
        "ACTIVE",
        "STOPPING",
        "SUCCEEDED",
        "INFEASIBLE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasTrialDetail(
    typing_extensions.TypedDict, total=False
):
    name: str
    parameters: str
    searchTrial: GoogleCloudAiplatformV1beta1NasTrial
    trainTrial: GoogleCloudAiplatformV1beta1NasTrial

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQuery(
    typing_extensions.TypedDict, total=False
):
    embedding: GoogleCloudAiplatformV1beta1NearestNeighborQueryEmbedding
    entityId: str
    neighborCount: int
    parameters: GoogleCloudAiplatformV1beta1NearestNeighborQueryParameters
    perCrowdingAttributeNeighborCount: int
    stringFilters: _list[GoogleCloudAiplatformV1beta1NearestNeighborQueryStringFilter]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQueryEmbedding(
    typing_extensions.TypedDict, total=False
):
    value: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQueryParameters(
    typing_extensions.TypedDict, total=False
):
    approximateNeighborCandidates: int
    leafNodesSearchFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQueryStringFilter(
    typing_extensions.TypedDict, total=False
):
    allowTokens: _list[str]
    denyTokens: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    contentValidationStats: _list[
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataContentValidationStats
    ]
    dataBytesCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataContentValidationStats(
    typing_extensions.TypedDict, total=False
):
    invalidRecordCount: str
    partialErrors: _list[
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataRecordError
    ]
    sourceGcsUri: str
    validRecordCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataRecordError(
    typing_extensions.TypedDict, total=False
):
    embeddingId: str
    errorMessage: str
    errorType: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "EMPTY_LINE",
        "INVALID_JSON_SYNTAX",
        "INVALID_CSV_SYNTAX",
        "INVALID_AVRO_SYNTAX",
        "INVALID_EMBEDDING_ID",
        "EMBEDDING_SIZE_MISMATCH",
        "NAMESPACE_MISSING",
        "PARSING_ERROR",
        "DUPLICATE_NAMESPACE",
        "OP_IN_DATAPOINT",
        "MULTIPLE_VALUES",
        "INVALID_NUMERIC_VALUE",
    ]
    rawRecord: str
    sourceGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighbors(
    typing_extensions.TypedDict, total=False
):
    neighbors: _list[GoogleCloudAiplatformV1beta1NearestNeighborsNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborsNeighbor(
    typing_extensions.TypedDict, total=False
):
    distance: float
    entityId: str
    entityKeyValues: GoogleCloudAiplatformV1beta1FetchFeatureValuesResponse

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Neighbor(typing_extensions.TypedDict, total=False):
    neighborDistance: float
    neighborId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NetworkSpec(typing_extensions.TypedDict, total=False):
    enableInternetAccess: bool
    network: str
    subnetwork: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NfsMount(typing_extensions.TypedDict, total=False):
    mountPoint: str
    path: str
    server: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookEucConfig(
    typing_extensions.TypedDict, total=False
):
    bypassActasCheck: bool
    eucDisabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig(
    typing_extensions.TypedDict, total=False
):
    idleShutdownDisabled: bool
    idleTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookReservationAffinity(
    typing_extensions.TypedDict, total=False
):
    consumeReservationType: typing_extensions.Literal[
        "RESERVATION_AFFINITY_TYPE_UNSPECIFIED",
        "RESERVATION_NONE",
        "RESERVATION_ANY",
        "RESERVATION_SPECIFIC",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntime(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    expirationTime: str
    healthState: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED", "HEALTHY", "UNHEALTHY"
    ]
    isUpgradable: bool
    labels: dict[str, typing.Any]
    name: str
    networkTags: _list[str]
    notebookRuntimeTemplateRef: GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateRef
    notebookRuntimeType: typing_extensions.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    proxyUri: str
    reservationAffinity: GoogleCloudAiplatformV1beta1NotebookReservationAffinity
    runtimeState: typing_extensions.Literal[
        "RUNTIME_STATE_UNSPECIFIED",
        "RUNNING",
        "BEING_STARTED",
        "BEING_STOPPED",
        "STOPPED",
        "BEING_UPGRADED",
    ]
    runtimeUser: str
    serviceAccount: str
    updateTime: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataPersistentDiskSpec: GoogleCloudAiplatformV1beta1PersistentDiskSpec
    description: str
    displayName: str
    etag: str
    eucConfig: GoogleCloudAiplatformV1beta1NotebookEucConfig
    idleShutdownConfig: GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig
    isDefault: bool
    labels: dict[str, typing.Any]
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    name: str
    networkSpec: GoogleCloudAiplatformV1beta1NetworkSpec
    networkTags: _list[str]
    notebookRuntimeType: typing_extensions.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    reservationAffinity: GoogleCloudAiplatformV1beta1NotebookReservationAffinity
    serviceAccount: str
    shieldedVmConfig: GoogleCloudAiplatformV1beta1ShieldedVmConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateRef(
    typing_extensions.TypedDict, total=False
):
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Part(typing_extensions.TypedDict, total=False):
    fileData: GoogleCloudAiplatformV1beta1FileData
    functionCall: GoogleCloudAiplatformV1beta1FunctionCall
    functionResponse: GoogleCloudAiplatformV1beta1FunctionResponse
    inlineData: GoogleCloudAiplatformV1beta1Blob
    text: str
    videoMetadata: GoogleCloudAiplatformV1beta1VideoMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PauseModelDeploymentMonitoringJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PauseScheduleRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PersistentDiskSpec(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: str
    diskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PersistentResource(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    network: str
    reservedIpRanges: _list[str]
    resourcePools: _list[GoogleCloudAiplatformV1beta1ResourcePool]
    resourceRuntime: GoogleCloudAiplatformV1beta1ResourceRuntime
    resourceRuntimeSpec: GoogleCloudAiplatformV1beta1ResourceRuntimeSpec
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROVISIONING", "RUNNING", "STOPPING", "ERROR"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobDetail: GoogleCloudAiplatformV1beta1PipelineJobDetail
    labels: dict[str, typing.Any]
    name: str
    network: str
    pipelineSpec: dict[str, typing.Any]
    reservedIpRanges: _list[str]
    runtimeConfig: GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfig
    scheduleName: str
    serviceAccount: str
    startTime: str
    state: typing_extensions.Literal[
        "PIPELINE_STATE_UNSPECIFIED",
        "PIPELINE_STATE_QUEUED",
        "PIPELINE_STATE_PENDING",
        "PIPELINE_STATE_RUNNING",
        "PIPELINE_STATE_SUCCEEDED",
        "PIPELINE_STATE_FAILED",
        "PIPELINE_STATE_CANCELLING",
        "PIPELINE_STATE_CANCELLED",
        "PIPELINE_STATE_PAUSED",
    ]
    templateMetadata: GoogleCloudAiplatformV1beta1PipelineTemplateMetadata
    templateUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobDetail(
    typing_extensions.TypedDict, total=False
):
    pipelineContext: GoogleCloudAiplatformV1beta1Context
    pipelineRunContext: GoogleCloudAiplatformV1beta1Context
    taskDetails: _list[GoogleCloudAiplatformV1beta1PipelineTaskDetail]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfig(
    typing_extensions.TypedDict, total=False
):
    defaultRuntime: GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigDefaultRuntime
    failurePolicy: typing_extensions.Literal[
        "PIPELINE_FAILURE_POLICY_UNSPECIFIED",
        "PIPELINE_FAILURE_POLICY_FAIL_SLOW",
        "PIPELINE_FAILURE_POLICY_FAIL_FAST",
    ]
    gcsOutputDirectory: str
    inputArtifacts: dict[str, typing.Any]
    parameterValues: dict[str, typing.Any]
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigDefaultRuntime(
    typing_extensions.TypedDict, total=False
):
    persistentResourceRuntimeDetail: GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigPersistentResourceRuntimeDetail

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigInputArtifact(
    typing_extensions.TypedDict, total=False
):
    artifactId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigPersistentResourceRuntimeDetail(
    typing_extensions.TypedDict, total=False
):
    persistentResourceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetail(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    execution: GoogleCloudAiplatformV1beta1Execution
    executorDetail: GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetail
    inputs: dict[str, typing.Any]
    outputs: dict[str, typing.Any]
    parentTaskId: str
    pipelineTaskStatus: _list[
        GoogleCloudAiplatformV1beta1PipelineTaskDetailPipelineTaskStatus
    ]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "CANCEL_PENDING",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
        "SKIPPED",
        "NOT_TRIGGERED",
    ]
    taskId: str
    taskName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetailArtifactList(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetailPipelineTaskStatus(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "CANCEL_PENDING",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
        "SKIPPED",
        "NOT_TRIGGERED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetail(
    typing_extensions.TypedDict, total=False
):
    containerDetail: GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailContainerDetail
    customJobDetail: GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailCustomJobDetail

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailContainerDetail(
    typing_extensions.TypedDict, total=False
):
    failedMainJobs: _list[str]
    failedPreCachingCheckJobs: _list[str]
    mainJob: str
    preCachingCheckJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailCustomJobDetail(
    typing_extensions.TypedDict, total=False
):
    failedJobs: _list[str]
    job: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTemplateMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Port(typing_extensions.TypedDict, total=False):
    containerPort: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredefinedSplit(
    typing_extensions.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    enabled: bool
    samplingRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    metadata: typing.Any
    model: str
    modelDisplayName: str
    modelVersionId: str
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictSchemata(
    typing_extensions.TypedDict, total=False
):
    instanceSchemaUri: str
    parametersSchemaUri: str
    predictionSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Presets(typing_extensions.TypedDict, total=False):
    modality: typing_extensions.Literal[
        "MODALITY_UNSPECIFIED", "IMAGE", "TEXT", "TABULAR"
    ]
    query: typing_extensions.Literal["PRECISE", "FAST"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrivateEndpoints(
    typing_extensions.TypedDict, total=False
):
    explainHttpUri: str
    healthHttpUri: str
    predictHttpUri: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig(
    typing_extensions.TypedDict, total=False
):
    enablePrivateServiceConnect: bool
    projectAllowlist: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Probe(typing_extensions.TypedDict, total=False):
    exec: GoogleCloudAiplatformV1beta1ProbeExecAction
    periodSeconds: int
    timeoutSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProbeExecAction(
    typing_extensions.TypedDict, total=False
):
    command: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PscAutomatedEndpoints(
    typing_extensions.TypedDict, total=False
):
    matchAddress: str
    network: str
    projectId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModel(
    typing_extensions.TypedDict, total=False
):
    frameworks: _list[str]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "EXPERIMENTAL",
        "PRIVATE_PREVIEW",
        "PUBLIC_PREVIEW",
        "GA",
    ]
    name: str
    openSourceCategory: typing_extensions.Literal[
        "OPEN_SOURCE_CATEGORY_UNSPECIFIED",
        "PROPRIETARY",
        "GOOGLE_OWNED_OSS_WITH_GOOGLE_CHECKPOINT",
        "THIRD_PARTY_OWNED_OSS_WITH_GOOGLE_CHECKPOINT",
        "GOOGLE_OWNED_OSS",
        "THIRD_PARTY_OWNED_OSS",
    ]
    parent: GoogleCloudAiplatformV1beta1PublisherModelParent
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata
    publisherModelTemplate: str
    supportedActions: GoogleCloudAiplatformV1beta1PublisherModelCallToAction
    versionId: str
    versionState: typing_extensions.Literal[
        "VERSION_STATE_UNSPECIFIED", "VERSION_STATE_STABLE", "VERSION_STATE_UNSTABLE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToAction(
    typing_extensions.TypedDict, total=False
):
    createApplication: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    deploy: GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy
    openEvaluationPipeline: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openFineTuningPipeline: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openFineTuningPipelines: GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenFineTuningPipelines
    openGenerationAiStudio: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openGenie: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openNotebook: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openNotebooks: GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenNotebooks
    openPromptTuningPipeline: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    requestAccess: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    viewRestApi: GoogleCloudAiplatformV1beta1PublisherModelCallToActionViewRestApi

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy(
    typing_extensions.TypedDict, total=False
):
    artifactUri: str
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    largeModelReference: GoogleCloudAiplatformV1beta1LargeModelReference
    modelDisplayName: str
    publicArtifactUri: str
    sharedResources: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenFineTuningPipelines(
    typing_extensions.TypedDict, total=False
):
    fineTuningPipelines: _list[
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenNotebooks(
    typing_extensions.TypedDict, total=False
):
    notebooks: _list[
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences(
    typing_extensions.TypedDict, total=False
):
    references: dict[str, typing.Any]
    resourceDescription: str
    resourceTitle: str
    resourceUseCase: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionViewRestApi(
    typing_extensions.TypedDict, total=False
):
    documentations: _list[GoogleCloudAiplatformV1beta1PublisherModelDocumentation]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelDocumentation(
    typing_extensions.TypedDict, total=False
):
    content: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelParent(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    reference: GoogleCloudAiplatformV1beta1PublisherModelResourceReference

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelResourceReference(
    typing_extensions.TypedDict, total=False
):
    description: str
    resourceName: str
    uri: str
    useCase: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PythonPackageSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    executorImageUri: str
    packageUris: _list[str]
    pythonModule: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryDeployedModelsResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModelRefs: _list[GoogleCloudAiplatformV1beta1DeployedModelRef]
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModel]
    nextPageToken: str
    totalDeployedModelCount: int
    totalEndpointCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RawPredictRequest(
    typing_extensions.TypedDict, total=False
):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RaySpec(typing_extensions.TypedDict, total=False):
    headNodeResourcePoolId: str
    imageUri: str
    resourcePoolImages: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    entityView: GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityView
    header: GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHeader

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityView(
    typing_extensions.TypedDict, total=False
):
    data: _list[GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData]
    entityId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData(
    typing_extensions.TypedDict, total=False
):
    value: GoogleCloudAiplatformV1beta1FeatureValue
    values: GoogleCloudAiplatformV1beta1FeatureValueList

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor(
    typing_extensions.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHeader(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    featureDescriptors: _list[
        GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadIndexDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadIndexDatapointsResponse(
    typing_extensions.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1beta1IndexDatapoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardBlobDataResponse(
    typing_extensions.TypedDict, total=False
):
    blobs: _list[GoogleCloudAiplatformV1beta1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardSizeResponse(
    typing_extensions.TypedDict, total=False
):
    storageSizeByte: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    timeSeriesData: GoogleCloudAiplatformV1beta1TimeSeriesData

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponse(
    typing_extensions.TypedDict, total=False
):
    monthlyUsageData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerMonthUsageData(
    typing_extensions.TypedDict, total=False
):
    userUsageData: _list[
        GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerUserUsageData
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerUserUsageData(
    typing_extensions.TypedDict, total=False
):
    username: str
    viewCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveContextChildrenRequest(
    typing_extensions.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveContextChildrenResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    datapointIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveDatapointsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportExecutionEventRequest(
    typing_extensions.TypedDict, total=False
):
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED", "ACTIVE", "DONE", "FAILED"
    ]
    status: GoogleRpcStatus
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportExecutionEventResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportRuntimeEventRequest(
    typing_extensions.TypedDict, total=False
):
    eventDetails: dict[str, typing.Any]
    eventType: typing_extensions.Literal["EVENT_TYPE_UNSPECIFIED", "HEARTBEAT", "IDLE"]
    internalOsServiceStateInstance: _list[
        GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance
    ]
    internalOsServiceStateInstances: _list[
        GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance
    ]
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportRuntimeEventResponse(
    typing_extensions.TypedDict, total=False
):
    idleShutdownMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcePool(
    typing_extensions.TypedDict, total=False
):
    autoscalingSpec: GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec
    diskSpec: GoogleCloudAiplatformV1beta1DiskSpec
    id: str
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    replicaCount: str
    usedReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec(
    typing_extensions.TypedDict, total=False
):
    maxReplicaCount: str
    minReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourceRuntime(
    typing_extensions.TypedDict, total=False
):
    accessUris: dict[str, typing.Any]
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourceRuntimeSpec(
    typing_extensions.TypedDict, total=False
):
    raySpec: GoogleCloudAiplatformV1beta1RaySpec
    serviceAccountSpec: GoogleCloudAiplatformV1beta1ServiceAccountSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcesConsumed(
    typing_extensions.TypedDict, total=False
):
    replicaHours: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RestoreDatasetVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResumeModelDeploymentMonitoringJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResumeScheduleRequest(
    typing_extensions.TypedDict, total=False
):
    catchUp: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SafetyRating(
    typing_extensions.TypedDict, total=False
):
    blocked: bool
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    ]
    probability: typing_extensions.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SafetySetting(
    typing_extensions.TypedDict, total=False
):
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    ]
    threshold: typing_extensions.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SampleConfig(
    typing_extensions.TypedDict, total=False
):
    followingBatchSamplePercentage: int
    initialBatchSamplePercentage: int
    sampleStrategy: typing_extensions.Literal[
        "SAMPLE_STRATEGY_UNSPECIFIED", "UNCERTAINTY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SampledShapleyAttribution(
    typing_extensions.TypedDict, total=False
):
    pathCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SamplingStrategy(
    typing_extensions.TypedDict, total=False
):
    randomSampleConfig: GoogleCloudAiplatformV1beta1SamplingStrategyRandomSampleConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SamplingStrategyRandomSampleConfig(
    typing_extensions.TypedDict, total=False
):
    sampleRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SavedQuery(typing_extensions.TypedDict, total=False):
    annotationFilter: str
    annotationSpecCount: int
    createTime: str
    displayName: str
    etag: str
    metadata: typing.Any
    name: str
    problemType: str
    supportAutomlTraining: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Scalar(typing_extensions.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Schedule(typing_extensions.TypedDict, total=False):
    allowQueueing: bool
    catchUp: bool
    createPipelineJobRequest: GoogleCloudAiplatformV1beta1CreatePipelineJobRequest
    createTime: str
    cron: str
    displayName: str
    endTime: str
    lastPauseTime: str
    lastResumeTime: str
    lastScheduledRunResponse: GoogleCloudAiplatformV1beta1ScheduleRunResponse
    maxConcurrentRunCount: str
    maxRunCount: str
    name: str
    nextRunTime: str
    startTime: str
    startedRunCount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "PAUSED", "COMPLETED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ScheduleRunResponse(
    typing_extensions.TypedDict, total=False
):
    runResponse: str
    scheduledRunTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Scheduling(typing_extensions.TypedDict, total=False):
    disableRetries: bool
    maxWaitDuration: str
    restartJobOnWorkerRestart: bool
    timeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Schema(typing_extensions.TypedDict, total=False):
    description: str
    enum: _list[str]
    example: typing.Any
    format: str
    items: GoogleCloudAiplatformV1beta1Schema
    nullable: bool
    properties: dict[str, typing.Any]
    required: _list[str]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STRING", "NUMBER", "INTEGER", "BOOLEAN", "ARRAY", "OBJECT"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor(
    typing_extensions.TypedDict, total=False
):
    color: GoogleTypeColor
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageBoundingBoxAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotation(
    typing_extensions.TypedDict, total=False
):
    maskAnnotation: GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationMaskAnnotation
    polygonAnnotation: GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolygonAnnotation
    polylineAnnotation: GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolylineAnnotation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationMaskAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecColors: _list[GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor]
    maskGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolygonAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1beta1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolylineAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1beta1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    auPrc: float
    auRoc: float
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    logLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    f1Score: float
    f1ScoreAt1: float
    f1ScoreMacro: float
    f1ScoreMicro: float
    falseNegativeCount: str
    falsePositiveCount: str
    falsePositiveRate: float
    falsePositiveRateAt1: float
    maxPredictions: int
    precision: float
    precisionAt1: float
    recall: float
    recallAt1: float
    trueNegativeCount: str
    truePositiveCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix(
    typing_extensions.TypedDict, total=False
):
    annotationSpecs: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef
    ]
    rows: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsForecastingEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    quantileMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry
    ]
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float
    rootMeanSquaredPercentageError: float
    weightedAbsolutePercentageError: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    observedQuantile: float
    quantile: float
    scaledPinballLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsGeneralTextGenerationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    bleu: float
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageObjectDetectionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetricsEntries: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    diceScoreCoefficient: float
    iouScore: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsQuestionAnsweringEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    exactMatch: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsRegressionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsSummarizationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextSentimentEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    f1Score: float
    linearKappa: float
    meanAbsoluteError: float
    meanSquaredError: float
    precision: float
    quadraticKappa: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanBoundingBoxIou: float
    meanMismatchRate: float
    meanTrackingAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxIou: float
    confidenceThreshold: float
    mismatchRate: float
    trackingPrecision: float
    trackingRecall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics
    ]
    meanAveragePrecision: float
    precisionWindowLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionRecognitionMetrics(
    typing_extensions.TypedDict, total=False
):
    evaluatedActionCount: int
    videoActionMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetrics
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoObjectTrackingMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int
    evaluatedFrameCount: int
    evaluatedTrackCount: int
    trackMeanAveragePrecision: float
    trackMeanBoundingBoxIou: float
    trackMeanMismatchRate: float
    trackMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageObjectDetectionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageSegmentationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextExtractionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    key: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextSentimentPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoActionRecognitionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoObjectTrackingPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageClassificationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageObjectDetectionPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageSegmentationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoActionRecognitionPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoClassificationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    oneSecIntervalClassification: bool
    segmentClassification: bool
    shotClassification: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoObjectTrackingPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    minBoundingBoxSize: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionImageObjectDetectionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    bboxes: _list[_list[typing.Any]]
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionImageSegmentationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    categoryMask: str
    confidenceMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTabularClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    classes: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTabularRegressionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    lowerBound: float
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    upperBound: float
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTextExtractionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]
    textSegmentEndOffsets: _list[str]
    textSegmentStartOffsets: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTextSentimentPredictionResult(
    typing_extensions.TypedDict, total=False
):
    sentiment: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTftFeatureImportance(
    typing_extensions.TypedDict, total=False
):
    attributeColumns: _list[str]
    attributeWeights: _list[float]
    contextColumns: _list[str]
    contextWeights: _list[float]
    horizonColumns: _list[str]
    horizonWeights: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTimeSeriesForecastingPredictionResult(
    typing_extensions.TypedDict, total=False
):
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    tftFeatureImportance: GoogleCloudAiplatformV1beta1SchemaPredictPredictionTftFeatureImportance
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoActionRecognitionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    frames: _list[
        GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame
    ]
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictionResult(
    typing_extensions.TypedDict, total=False
):
    error: GoogleCloudAiplatformV1beta1SchemaPredictionResultError
    instance: dict[str, typing.Any]
    key: str
    prediction: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictionResultError(
    typing_extensions.TypedDict, total=False
):
    message: str
    status: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataInputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextExtractionAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    textSegment: GoogleCloudAiplatformV1beta1SchemaTextSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSegment(
    typing_extensions.TypedDict, total=False
):
    content: str
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSentimentAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    sentiment: int
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSentimentSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataInputConfig
    timeColumn: str
    timeSeriesIdentifierColumn: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity
    enableProbabilisticInference: bool
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    baseModelId: str
    budgetMilliNodeHours: str
    disableEarlyStopping: bool
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "CLOUD_1",
        "MOBILE_TF_LOW_LATENCY_1",
        "MOBILE_TF_VERSATILE_1",
        "MOBILE_TF_HIGH_ACCURACY_1",
        "EFFICIENTNET",
        "MAXVIT",
        "VIT",
        "COCA",
    ]
    multiLabel: bool
    tunableParameter: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetection(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs(
    typing_extensions.TypedDict, total=False
):
    budgetMilliNodeHours: str
    disableEarlyStopping: bool
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD_HIGH_ACCURACY_1",
        "CLOUD_LOW_LATENCY_1",
        "CLOUD_1",
        "MOBILE_TF_LOW_LATENCY_1",
        "MOBILE_TF_VERSATILE_1",
        "MOBILE_TF_HIGH_ACCURACY_1",
        "CLOUD_STREAMING_1",
        "SPINENET",
        "YOLO",
    ]
    tunableParameter: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentation(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs(
    typing_extensions.TypedDict, total=False
):
    baseModelId: str
    budgetMilliNodeHours: str
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD_HIGH_ACCURACY_1",
        "CLOUD_LOW_ACCURACY_1",
        "MOBILE_TF_LOW_LATENCY_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTables(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    disableEarlyStopping: bool
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    optimizationObjective: str
    optimizationObjectivePrecisionValue: float
    optimizationObjectiveRecallValue: float
    predictionType: str
    targetColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation
    ]
    weightColumnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation
    repeatedCategorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation
    repeatedNumeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation
    repeatedText: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtraction(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentiment(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs(
    typing_extensions.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognition(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
        "MOBILE_CORAL_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTracking(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_CORAL_VERSATILE_1",
        "MOBILE_CORAL_LOW_LATENCY_1",
        "MOBILE_JETSON_VERSATILE_1",
        "MOBILE_JETSON_LOW_LATENCY_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter(
    typing_extensions.TypedDict, total=False
):
    checkpointName: str
    datasetConfig: dict[str, typing.Any]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trainerConfig: dict[str, typing.Any]
    trainerType: typing_extensions.Literal[
        "TRAINER_TYPE_UNSPECIFIED", "AUTOML_TRAINER", "MODEL_GARDEN_TRAINER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomJobMetadata(
    typing_extensions.TypedDict, total=False
):
    backingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomTask(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1CustomJobSpec
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig(
    typing_extensions.TypedDict, total=False
):
    destinationBigqueryUri: str
    overrideExistingTable: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig(
    typing_extensions.TypedDict, total=False
):
    groupColumns: _list[str]
    groupTemporalTotalWeight: float
    groupTotalWeight: float
    temporalTotalWeight: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata(
    typing_extensions.TypedDict, total=False
):
    backingHyperparameterTuningJob: str
    bestTrialBackingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec(
    typing_extensions.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxTrialCount: int
    parallelTrialCount: int
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningTask(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig(
    typing_extensions.TypedDict, total=False
):
    column: str
    maxCount: str
    strideLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoActionRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1beta1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1beta1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    instanceId: str
    timeOffset: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVisualInspectionClassificationLabelSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVisualInspectionMaskSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchDataItemsResponse(
    typing_extensions.TypedDict, total=False
):
    dataItemViews: _list[GoogleCloudAiplatformV1beta1DataItemView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1beta1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchMigratableResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    migratableResources: _list[GoogleCloudAiplatformV1beta1MigratableResource]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    endTime: str
    featureDisplayName: str
    objectives: _list[
        GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective
    ]
    pageSize: int
    pageToken: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective(
    typing_extensions.TypedDict, total=False
):
    topFeatureCount: int
    type: typing_extensions.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponse(
    typing_extensions.TypedDict, total=False
):
    monitoringStats: _list[GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchNearestEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1beta1NearestNeighborQuery
    returnFullEntity: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchNearestEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    nearestNeighbors: GoogleCloudAiplatformV1beta1NearestNeighbors

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ServiceAccountSpec(
    typing_extensions.TypedDict, total=False
):
    enableCustomServiceAccount: bool
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ShieldedVmConfig(
    typing_extensions.TypedDict, total=False
):
    enableSecureBoot: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SmoothGradConfig(
    typing_extensions.TypedDict, total=False
):
    featureNoiseSigma: GoogleCloudAiplatformV1beta1FeatureNoiseSigma
    noiseSigma: float
    noisySampleCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpecialistPool(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    pendingDataLabelingJobs: _list[str]
    specialistManagerEmails: _list[str]
    specialistManagersCount: int
    specialistWorkerEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StartNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StartNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StopTrialRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StratifiedSplit(
    typing_extensions.TypedDict, total=False
):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingPredictRequest(
    typing_extensions.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingPredictResponse(
    typing_extensions.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    entityIds: _list[str]
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StringArray(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Study(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    inactiveReason: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpec(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
        "ALGORITHM_UNSPECIFIED", "GRID_SEARCH", "RANDOM_SEARCH"
    ]
    convexAutomatedStoppingSpec: GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec
    convexStopConfig: GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig
    decayCurveStoppingSpec: GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec
    measurementSelectionType: typing_extensions.Literal[
        "MEASUREMENT_SELECTION_TYPE_UNSPECIFIED", "LAST_MEASUREMENT", "BEST_MEASUREMENT"
    ]
    medianAutomatedStoppingSpec: GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec
    metrics: _list[GoogleCloudAiplatformV1beta1StudySpecMetricSpec]
    observationNoise: typing_extensions.Literal[
        "OBSERVATION_NOISE_UNSPECIFIED", "LOW", "HIGH"
    ]
    parameters: _list[GoogleCloudAiplatformV1beta1StudySpecParameterSpec]
    studyStoppingConfig: GoogleCloudAiplatformV1beta1StudySpecStudyStoppingConfig
    transferLearningConfig: GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    learningRateParameterName: str
    maxStepCount: str
    minMeasurementCount: str
    minStepCount: str
    updateAllStoppedTrials: bool
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig(
    typing_extensions.TypedDict, total=False
):
    autoregressiveOrder: str
    learningRateParameterName: str
    maxNumSteps: str
    minNumSteps: str
    useSeconds: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMetricSpec(
    typing_extensions.TypedDict, total=False
):
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str
    safetyConfig: GoogleCloudAiplatformV1beta1StudySpecMetricSpecSafetyMetricConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMetricSpecSafetyMetricConfig(
    typing_extensions.TypedDict, total=False
):
    desiredMinSafeTrialsFraction: float
    safetyThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpec(
    typing_extensions.TypedDict, total=False
):
    categoricalValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec
    conditionalParameterSpecs: _list[
        GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec
    ]
    discreteValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec
    doubleValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec
    integerValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec
    parameterId: str
    scaleType: typing_extensions.Literal[
        "SCALE_TYPE_UNSPECIFIED",
        "UNIT_LINEAR_SCALE",
        "UNIT_LOG_SCALE",
        "UNIT_REVERSE_LOG_SCALE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec(
    typing_extensions.TypedDict, total=False
):
    parameterSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpec
    parentCategoricalValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition
    parentDiscreteValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition
    parentIntValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecIntValueCondition

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecIntValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: float
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: float
    maxValue: float
    minValue: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: str
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecStudyStoppingConfig(
    typing_extensions.TypedDict, total=False
):
    maxDurationNoProgress: str
    maxNumTrials: int
    maxNumTrialsNoProgress: int
    maximumRuntimeConstraint: GoogleCloudAiplatformV1beta1StudyTimeConstraint
    minNumTrials: int
    minimumRuntimeConstraint: GoogleCloudAiplatformV1beta1StudyTimeConstraint
    shouldStopAsap: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig(
    typing_extensions.TypedDict, total=False
):
    disableTransferLearning: bool
    priorStudyNames: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudyTimeConstraint(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    maxDuration: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsMetadata(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsRequest(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    contexts: _list[GoogleCloudAiplatformV1beta1TrialContext]
    suggestionCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    studyState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]
    trials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SyncFeatureViewRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SyncFeatureViewResponse(
    typing_extensions.TypedDict, total=False
):
    featureViewSync: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TFRecordDestination(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tensor(typing_extensions.TypedDict, total=False):
    boolVal: _list[bool]
    bytesVal: _list[str]
    doubleVal: _list[float]
    dtype: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "BOOL",
        "STRING",
        "FLOAT",
        "DOUBLE",
        "INT8",
        "INT16",
        "INT32",
        "INT64",
        "UINT8",
        "UINT16",
        "UINT32",
        "UINT64",
    ]
    floatVal: _list[float]
    int64Val: _list[str]
    intVal: _list[int]
    listVal: _list[GoogleCloudAiplatformV1beta1Tensor]
    shape: _list[str]
    stringVal: _list[str]
    structVal: dict[str, typing.Any]
    tensorVal: str
    uint64Val: _list[str]
    uintVal: _list[int]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tensorboard(typing_extensions.TypedDict, total=False):
    blobStoragePathPrefix: str
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    isDefault: bool
    labels: dict[str, typing.Any]
    name: str
    runCount: int
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardBlob(
    typing_extensions.TypedDict, total=False
):
    data: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardBlobSequence(
    typing_extensions.TypedDict, total=False
):
    values: _list[GoogleCloudAiplatformV1beta1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardExperiment(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    source: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardRun(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTensor(
    typing_extensions.TypedDict, total=False
):
    value: str
    versionNumber: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTimeSeries(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    etag: str
    metadata: GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata
    name: str
    pluginData: str
    pluginName: str
    updateTime: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata(
    typing_extensions.TypedDict, total=False
):
    maxBlobSequenceLength: str
    maxStep: str
    maxWallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ThresholdConfig(
    typing_extensions.TypedDict, total=False
):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimeSeriesData(
    typing_extensions.TypedDict, total=False
):
    tensorboardTimeSeriesId: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]
    values: _list[GoogleCloudAiplatformV1beta1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimeSeriesDataPoint(
    typing_extensions.TypedDict, total=False
):
    blobs: GoogleCloudAiplatformV1beta1TensorboardBlobSequence
    scalar: GoogleCloudAiplatformV1beta1Scalar
    step: str
    tensor: GoogleCloudAiplatformV1beta1TensorboardTensor
    wallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimestampSplit(
    typing_extensions.TypedDict, total=False
):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TokensInfo(typing_extensions.TypedDict, total=False):
    tokenIds: _list[str]
    tokens: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tool(typing_extensions.TypedDict, total=False):
    functionDeclarations: _list[GoogleCloudAiplatformV1beta1FunctionDeclaration]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrainingConfig(
    typing_extensions.TypedDict, total=False
):
    timeoutTrainingMilliHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrainingPipeline(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    inputDataConfig: GoogleCloudAiplatformV1beta1InputDataConfig
    labels: dict[str, typing.Any]
    modelId: str
    modelToUpload: GoogleCloudAiplatformV1beta1Model
    name: str
    parentModel: str
    startTime: str
    state: typing_extensions.Literal[
        "PIPELINE_STATE_UNSPECIFIED",
        "PIPELINE_STATE_QUEUED",
        "PIPELINE_STATE_PENDING",
        "PIPELINE_STATE_RUNNING",
        "PIPELINE_STATE_SUCCEEDED",
        "PIPELINE_STATE_FAILED",
        "PIPELINE_STATE_CANCELLING",
        "PIPELINE_STATE_CANCELLED",
        "PIPELINE_STATE_PAUSED",
    ]
    trainingTaskDefinition: str
    trainingTaskInputs: typing.Any
    trainingTaskMetadata: typing.Any
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Trial(typing_extensions.TypedDict, total=False):
    clientId: str
    customJob: str
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
    id: str
    infeasibleReason: str
    measurements: _list[GoogleCloudAiplatformV1beta1Measurement]
    name: str
    parameters: _list[GoogleCloudAiplatformV1beta1TrialParameter]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "REQUESTED",
        "ACTIVE",
        "STOPPING",
        "SUCCEEDED",
        "INFEASIBLE",
    ]
    webAccessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrialContext(
    typing_extensions.TypedDict, total=False
):
    description: str
    parameters: _list[GoogleCloudAiplatformV1beta1TrialParameter]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrialParameter(
    typing_extensions.TypedDict, total=False
):
    parameterId: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeploySolverOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UnmanagedContainerModel(
    typing_extensions.TypedDict, total=False
):
    artifactUri: str
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateDeploymentResourcePoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetRequest(
    typing_extensions.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1beta1Examples

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureGroupOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureOnlineStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureViewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeaturestoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateModelDeploymentMonitoringJobOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdatePersistentResourceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateSpecialistPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    specialistPool: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateTensorboardOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpgradeNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpgradeNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelRequest(
    typing_extensions.TypedDict, total=False
):
    model: GoogleCloudAiplatformV1beta1Model
    modelId: str
    parentModel: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelResponse(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1beta1IndexDatapoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertDatapointsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UserActionReference(
    typing_extensions.TypedDict, total=False
):
    dataLabelingJob: str
    method: str
    operation: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Value(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VideoMetadata(
    typing_extensions.TypedDict, total=False
):
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WorkerPoolSpec(
    typing_extensions.TypedDict, total=False
):
    containerSpec: GoogleCloudAiplatformV1beta1ContainerSpec
    diskSpec: GoogleCloudAiplatformV1beta1DiskSpec
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    nfsMounts: _list[GoogleCloudAiplatformV1beta1NfsMount]
    pythonPackageSpec: GoogleCloudAiplatformV1beta1PythonPackageSpec
    replicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesPayload(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    featureValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    payloads: _list[GoogleCloudAiplatformV1beta1WriteFeatureValuesPayload]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataRequest(
    typing_extensions.TypedDict, total=False
):
    writeRunDataRequests: _list[
        GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest(
    typing_extensions.TypedDict, total=False
):
    tensorboardRun: str
    timeSeriesData: _list[GoogleCloudAiplatformV1beta1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardRunDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1XraiAttribution(
    typing_extensions.TypedDict, total=False
):
    blurBaselineConfig: GoogleCloudAiplatformV1beta1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1beta1SmoothGradConfig
    stepCount: int

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
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GoogleIamV1GetPolicyOptions

@typing.type_check_only
class GoogleIamV1GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

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
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleTypeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class IntelligenceCloudAutomlXpsMetricEntry(typing_extensions.TypedDict, total=False):
    argentumMetricId: str
    doubleValue: float
    int64Value: str
    metricName: str
    systemLabels: _list[IntelligenceCloudAutomlXpsMetricEntryLabel]

@typing.type_check_only
class IntelligenceCloudAutomlXpsMetricEntryLabel(
    typing_extensions.TypedDict, total=False
):
    labelName: str
    labelValue: str

@typing.type_check_only
class IntelligenceCloudAutomlXpsReportingMetrics(
    typing_extensions.TypedDict, total=False
):
    effectiveTrainingDuration: str
    metricEntries: _list[IntelligenceCloudAutomlXpsMetricEntry]

@typing.type_check_only
class LanguageLabsAidaTrustRecitationProtoDocAttribution(
    typing_extensions.TypedDict, total=False
):
    amarnaId: str
    arxivId: str
    author: str
    bibkey: str
    biorxivId: str
    bookTitle: str
    bookVolumeId: str
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED",
        "CATEGORY_NEWS",
        "CATEGORY_NON_NEWS_WEBDOC",
        "CATEGORY_UNKNOWN_MISSING_SIGNAL",
    ]
    conversationId: str
    dataset: typing_extensions.Literal[
        "DATASET_UNSPECIFIED",
        "WIKIPEDIA",
        "WEBDOCS",
        "WEBDOCS_FINETUNE",
        "GITHUB_MIRROR",
        "BOOKS_FULL_VIEW",
        "BOOKS_PRIVATE",
        "GNEWS",
        "ULM_DOCJOINS",
        "ULM_DOCJOINS_DEDUPED",
        "MEENA_FC",
        "PODCAST",
        "AQUA",
        "WEB_ASR",
        "BARD_GOLDEN",
        "COMMON_SENSE_REASONING",
        "MATH",
        "MATH_REASONING",
        "CLEAN_ARXIV",
        "LAMDA_FACTUALITY_E2E_QUERY_GENERATION",
        "LAMDA_FACTUALITY_E2E_RESPONSE_GENERATION",
        "MASSIVE_FORUM_THREAD_SCORED_BARD",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_200",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_500",
        "DOCUMENT_CHUNKS",
        "MEENA_RESEARCH_PHASE_GOLDEN_MARKDOWN",
        "MEENA_RESEARCH_PHASE_GOOGLERS",
        "MEENA_RESPONSE_SAFETY_HUMAN_GEN",
        "MEENA_RESPONSE_SAFETY_SCHEMA_NO_BROADCAST",
        "MEENA_RESPONSE_SAFETY_V3_HUMAN_GEN2",
        "MEENA_RESPONSE_SAFETY_V3_SCHEMA_NO_BROADCAST",
        "LAMDA_FACTUALITY_TRIGGER",
        "LAMDA_SAFETY_V2_SCHEMA_NO_BROADCAST",
        "LAMDA_SSI_DISCRIMINATIVE",
        "ASSISTANT_PERSONALITY_SAFETY",
        "PODCAST_FINETUNE_DIALOG",
        "WORLD_QUERY_GENERATOR",
        "C4_JOINED_DOCJOINS",
        "HOL4_THEORIES",
        "HOL_LIGHT_THEORIES",
        "HOLSTEPS",
        "ISABELLE_STEP",
        "ISABELLE_THEORIES",
        "LEAN_MATHLIB_THEORIES",
        "LEAN_STEP",
        "MIZAR_THEORIES",
        "COQ_STEP",
        "COQ_THEORIES",
        "AMPS_KHAN",
        "AMPS_MATHEMATICA",
        "CODEY_CODE",
        "CODE_QA_SE",
        "CODE_QA_SO",
        "CODE_QA_FT_FORMAT",
        "CODE_QA_FT_KNOWLEDGE",
        "CODE_QA_GITHUB_FILTERED_CODE",
        "BARD_PERSONALITY_GOLDEN",
        "ULM_DOCJOINS_WITH_URLS_EN",
        "ULM_DOCJOINS_WITH_URLS_I18N",
        "GOODALL_MTV5_GITHUB",
        "GOODALL_MTV5_BOOKS",
        "GOODALL_MTV5_C4",
        "GOODALL_MTV5_WIKIPEDIA",
        "GOODALL_MW_TOP_100B",
        "GOODALL_MW_STACK_EXCHANGE",
        "GOODALL_MW_TOP_0_10B",
        "GOODALL_MW_TOP_10B_20B",
        "CODEY_NOTEBOOK_LM_PRETRAINING",
        "VERTEX_SAFE_FLAN",
        "GITHUB_MIRROR_V1_0_1",
        "GITHUB_MIRROR_V2_1_0",
        "CMS_WIKIPEDIA_LANG_FILTERED",
        "CMS_STACKOVERFLOW_MULTILINGUAL",
        "CMS_STACKEXCHANGE",
        "PUBMED",
        "GEMINI_DOCJOINS_EN_TOP10B_GCC",
        "GEMINI_DOCJOINS_EN_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_EN_TOP20B_TOP100B_GCC",
        "GEMINI_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP20B_TOP100B_GCC",
        "SIMPLIFIED_HTML_V1_GCC",
        "GEMINI_DOCJOINS_TOXICITY_TAGGED_GCC",
        "CMS_GITHUB_V4",
        "GITHUB_HTML_V4",
        "GITHUB_OTHER_V4",
        "GITHUB_LONG_TAIL_V4",
        "CMS_GITHUB_MULTIFILE_V4",
        "GITHUB_DIFFS_WITH_COMMIT_MESSAGE",
        "ULM_ARXIV",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_ENONLY",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_NONENONLY",
        "QUORA",
        "PODCASTS_ROBOTSTXT",
        "COMBINED_REDDIT",
        "CANARIES_SHUFFLED",
        "CLM_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "TECHDOCS_DATA_SOURCE",
        "SCIENCE_PDF_70M_DOCS_FILTERED",
        "GEMINI_V1_CMS_WIKIPEDIA_LANG_FILTERED",
        "GEMINI_V1_WIKIPEDIA_DIFFS",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_TOP20B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP20B_TOP100B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_TOP20B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP20B_TOP100B_GCC_050523",
        "GEMINI_V1_SIMPLIFIED_HTML_V2_GCC",
        "GEMINI_V1_CMS_STACKOVERFLOW_MULTILINGUAL_V2",
        "GEMINI_V1_CMS_STACKEXCHANGE_DECONT",
        "GEMINI_V1_QUORA",
        "GEMINI_V1_COMBINED_REDDIT",
        "GEMINI_V1_DOCJOIN_100B_EN_TOXICITY_TAGGED_GCC_FIXED_TAGS",
        "GEMINI_V1_PUBMED",
        "GEMINI_V1_WEB_MATH_V2",
        "GEMINI_V1_CMS_GITHUB_DECONTAMINATED_V_7",
        "GEMINI_V1_GITHUB_DIFF_WITH_COMMIT_MESSAGE_V2",
        "GEMINI_V1_GITHUB_HTML_CSS_XML_V4",
        "GEMINI_V1_GITHUB_OTHER_V4",
        "GEMINI_V1_GITHUB_LONG_TAIL_V4",
        "GEMINI_V1_GITHUB_JUPTYER_NOTEBOOKS_SSTABLE",
        "GEMINI_V1_ULM_ARXIV_SSTABLE",
        "GEMINI_V1_PODCASTS_ROBOTSTXT",
        "GEMINI_V1_SCIENCE_PDF_68M_HQ_DOCS_GCC",
        "GEMINI_V1_GITHUB_TECHDOCS_V2",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_EN",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_NONEN",
        "GEMINI_V1_STEM_BOOKS_650K_TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_M3W_V2_FILTERED",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_WEBLI_EN_V4_350M_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_SCREENAI_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CULTURE_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_EN_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_I18N_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_NON_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_VTP_4F_VIDEO2TEXT_PREFIX",
        "GEMINI_V1_FORMAL_MATH_WITHOUT_HOLSTEPS_AND_MIZAR",
        "GEMINI_V1_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "GEMINI_V1_CANARIES_SHUFFLED_DOCJOIN_EN_NONEN_CODE_ARXIV_TRANSLATE",
        "DUET_CLOUD_SECURITY_DOCS",
        "DUET_GITHUB_CODE_SNIPPETS",
        "DUET_GITHUB_FILES",
        "DUET_GOBYEXAMPLE",
        "DUET_GOLANG_DOCS",
        "DUET_CLOUD_DOCS_TROUBLESHOOTING_TABLES",
        "DUET_DEVSITE_DOCS",
        "DUET_CLOUD_BLOG_POSTS",
        "DUET_CLOUD_PODCAST_EPISODES",
        "DUET_YOUTUBE_VIDEOS",
        "DUET_CLOUD_SKILLS_BOOST",
        "DUET_CLOUD_DOCS",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_GENERATED",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_HANDWRITTEN",
        "DUET_GOOGLESQL_GENERATION",
        "DUET_CLOUD_IX_PROMPTS",
        "DUET_RAD",
        "BARD_ARCADE_GITHUB",
        "MOBILE_ASSISTANT_MAGI_FILTERED_0825_373K",
        "MOBILE_ASSISTANT_PALM24B_FILTERED_400K",
        "GENESIS_NEWS_INSIGHTS",
        "CLOUD_SECURITY_PRETRAINING",
        "CLOUD_SECURITY_FINETUNING",
        "LABS_AQA_DSCOUT",
        "LABS_AQA_TAILWIND",
        "LABS_AQA_DELEWARE",
        "GEMINI_MULTIMODAL_FT_URL",
        "GEMINI_MULTIMODAL_FT_YT",
        "GEMINI_MULTIMODAL_FT_SHUTTERSTOCK",
        "GEMINI_MULTIMODAL_FT_NONE",
        "GEMINI_MULTIMODAL_FT_OTHER",
        "GEMINI_MULTIMODAL_FT_INK",
        "GEMINI_MULTIMODAL_IT",
        "GEMINI_IT_SHUTTERSTOCK",
        "GEMINI_IT_M3W",
        "GEMINI_IT_HEDGING",
        "GEMINI_IT_DSCOUT_FACTUALITY",
        "GEMINI_IT_AQUAMUSE",
        "GEMINI_IT_SHOTGUN",
        "GEMINI_IT_ACI_BENCH",
        "GEMINI_IT_SPIDER_FILTERED",
        "GEMINI_IT_TAB_SUM_BQ",
        "GEMINI_IT_QA_WITH_URL",
        "GEMINI_IT_CODE_INSTRUCT",
        "GEMINI_IT_MED_PALM",
        "GEMINI_IT_TASK_ORIENTED_DIALOG",
        "GEMINI_IT_NIMBUS_GROUNDING_TO_PROMPT",
        "GEMINI_IT_EITL_GEN",
        "GEMINI_IT_HITL_GEN",
        "GEMINI_IT_MECH",
        "GEMINI_IT_TABLE_GEN",
        "GEMINI_IT_NIMBUS_DECIBEL",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMINI_V2_CMS_WIKIPEDIA_LANG_FILTERED_GCC_PII",
        "GEMINI_V2_WIKIPEDIA_DIFFS_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_QUORA_COMPLIANT",
        "GEMINI_V2_FORUMS_V2_COMPLIANT",
        "GEMINI_V2_CMS_STACKOVERFLOW_MULTILINGUAL_V2_COMPLIANT",
        "GEMINI_V2_SIMPLIFIED_HTML_V2_CORRECT_FORMAT_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_TOXICITY_TAGGED_FIXED_TAGS_COMPLIANT",
        "GEMINI_V2_CODEWEB_V1_COMPLIANT",
        "GEMINI_V2_LEETCODE_GCC_PII",
        "GEMINI_V2_CODE_CONTESTS_COMPLIANT",
        "GEMINI_V2_CMS_GITHUB_MULTI_FILE_FOR_FIM_GEMBAGZ_FIXED_BYTES_LENGTHS",
        "GEMINI_V2_GITHUB_EVALED_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_NON_EVAL_HIGH_PRI_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_LOW_PRI_LANGUAGES_AND_CONFIGS_COMPLIANT",
        "GEMINI_V2_GITHUB_LONG_TAIL_AND_STRUCTURED_DATA_COMPLIANT",
        "GEMINI_V2_GITHUB_PYTHON_NOTEBOOKS_COMPLIANT",
        "GEMINI_V2_GITHUB_DIFFS_COMPLIANT",
        "GEMINI_V2_GITHUB_TECHDOCS_COMPLIANT",
        "GEMINI_V2_HIGH_QUALITY_CODE_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_SCIENCE_PDF_68M_HQ_DOCS_DEDUP_COMPLIANT_CLEAN_TEX",
        "GEMINI_V2_ARXIV_2023_COMPLIANT",
        "GEMINI_V2_FORMAL_COMPLIANT",
        "GEMINI_V2_CMS_STACKEXCHANGE_COMPLIANT",
        "GEMINI_V2_PUBMED_COMPLIANT",
        "GEMINI_V2_WEB_MATH_V3_COMPLIANT",
        "GEMINI_V2_SCIENCEWEB_V0_GCC_PII",
        "GEMINI_V2_WEB_POLYMATH_V1_COMPLIANT",
        "GEMINI_V2_MATH_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_BIOLOGY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_PHYSICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHEMISTRY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MACHINE_LEARNING_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_QA_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_ECONOMICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MEDICAL_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHESS_COMPLIANT",
        "GEMINI_V2_YOUTUBE_SCIENCE_V4_FILTERED_COMPLIANT",
        "GEMINI_V2_GOALDMINE_XL_GENERATED_PLUS_GT_NO_DM_MATH_COMPLIANT",
        "GEMINI_V2_FIRSTTIMES_SCIENCE_PDF_DEDUP_HQ_LENGTH_FILTERED_COMPLIANT",
        "GEMINI_V2_PODCASTS_COMPLIANT",
        "GEMINI_V2_EN_NONSCIENCE_PDF_DEDUP_46M_DOCS_COMPLIANT",
        "GEMINI_V2_NONPUB_COPYRIGHT_BOOKS_V3_70_CONF_082323_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_COPYRIGHT_BOOKS_V3_111823_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_BOOKS_318K_TEXT_COMPLIANT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_T2I_TEXT_TO_IMAGE_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_I18N_680M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_FULL_HTML_75M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_V1_1_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_DOC_240M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_VIDEO_VIDEO_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M4W_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CULTURE_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_DETECTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_ALT_TEXT_NONEN_500M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SPATIAL_AWARE_PALI_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_3D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_NON_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_3D_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CC3M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_INFOGRAPHICS_LARGE_WEB_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_BIORXIV_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_IM2SOL_PROBLEM_AND_SOLUTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PLOT2TABLE_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TIKZ_DERENDERING_MERGED_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_2D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WIKIPEDIA_EQUATIONS_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_EQ2LATEX_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_ARXIV_EQUATIONS_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_HEAD_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_CLM_TRANSLATE_DATAV3_WEB_UNWMT_INCR_MIX",
        "GEMINI_V2_NTL_NTLV4A_MONOLINGUAL_DEDUP_N5",
        "GEMINI_V2_NTL_STT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_TRANSLIT_BILEX_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_BT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_FT_FIXED_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_CANARIES_SHUFFLED_COMPLIANT",
    ]
    filepath: str
    geminiId: str
    gnewsArticleTitle: str
    goodallExampleId: str
    isOptOut: bool
    isPrompt: bool
    lamdaExampleId: str
    license: str
    meenaConversationId: str
    naturalLanguageCode: str
    noAttribution: bool
    podcastUtteranceId: str
    publicationDate: GoogleTypeDate
    qualityScoreExperimentOnly: float
    repo: str
    url: str
    volumeId: str
    wikipediaArticleTitle: str
    youtubeVideoId: str

@typing.type_check_only
class LanguageLabsAidaTrustRecitationProtoRecitationResult(
    typing_extensions.TypedDict, total=False
):
    dynamicSegmentResults: _list[LanguageLabsAidaTrustRecitationProtoSegmentResult]
    recitationAction: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "CITE", "BLOCK", "NO_ACTION", "EXEMPT_FOUND_IN_PROMPT"
    ]
    trainingSegmentResults: _list[LanguageLabsAidaTrustRecitationProtoSegmentResult]

@typing.type_check_only
class LanguageLabsAidaTrustRecitationProtoSegmentResult(
    typing_extensions.TypedDict, total=False
):
    attributionDataset: typing_extensions.Literal[
        "DATASET_UNSPECIFIED",
        "WIKIPEDIA",
        "WEBDOCS",
        "WEBDOCS_FINETUNE",
        "GITHUB_MIRROR",
        "BOOKS_FULL_VIEW",
        "BOOKS_PRIVATE",
        "GNEWS",
        "ULM_DOCJOINS",
        "ULM_DOCJOINS_DEDUPED",
        "MEENA_FC",
        "PODCAST",
        "AQUA",
        "WEB_ASR",
        "BARD_GOLDEN",
        "COMMON_SENSE_REASONING",
        "MATH",
        "MATH_REASONING",
        "CLEAN_ARXIV",
        "LAMDA_FACTUALITY_E2E_QUERY_GENERATION",
        "LAMDA_FACTUALITY_E2E_RESPONSE_GENERATION",
        "MASSIVE_FORUM_THREAD_SCORED_BARD",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_200",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_500",
        "DOCUMENT_CHUNKS",
        "MEENA_RESEARCH_PHASE_GOLDEN_MARKDOWN",
        "MEENA_RESEARCH_PHASE_GOOGLERS",
        "MEENA_RESPONSE_SAFETY_HUMAN_GEN",
        "MEENA_RESPONSE_SAFETY_SCHEMA_NO_BROADCAST",
        "MEENA_RESPONSE_SAFETY_V3_HUMAN_GEN2",
        "MEENA_RESPONSE_SAFETY_V3_SCHEMA_NO_BROADCAST",
        "LAMDA_FACTUALITY_TRIGGER",
        "LAMDA_SAFETY_V2_SCHEMA_NO_BROADCAST",
        "LAMDA_SSI_DISCRIMINATIVE",
        "ASSISTANT_PERSONALITY_SAFETY",
        "PODCAST_FINETUNE_DIALOG",
        "WORLD_QUERY_GENERATOR",
        "C4_JOINED_DOCJOINS",
        "HOL4_THEORIES",
        "HOL_LIGHT_THEORIES",
        "HOLSTEPS",
        "ISABELLE_STEP",
        "ISABELLE_THEORIES",
        "LEAN_MATHLIB_THEORIES",
        "LEAN_STEP",
        "MIZAR_THEORIES",
        "COQ_STEP",
        "COQ_THEORIES",
        "AMPS_KHAN",
        "AMPS_MATHEMATICA",
        "CODEY_CODE",
        "CODE_QA_SE",
        "CODE_QA_SO",
        "CODE_QA_FT_FORMAT",
        "CODE_QA_FT_KNOWLEDGE",
        "CODE_QA_GITHUB_FILTERED_CODE",
        "BARD_PERSONALITY_GOLDEN",
        "ULM_DOCJOINS_WITH_URLS_EN",
        "ULM_DOCJOINS_WITH_URLS_I18N",
        "GOODALL_MTV5_GITHUB",
        "GOODALL_MTV5_BOOKS",
        "GOODALL_MTV5_C4",
        "GOODALL_MTV5_WIKIPEDIA",
        "GOODALL_MW_TOP_100B",
        "GOODALL_MW_STACK_EXCHANGE",
        "GOODALL_MW_TOP_0_10B",
        "GOODALL_MW_TOP_10B_20B",
        "CODEY_NOTEBOOK_LM_PRETRAINING",
        "VERTEX_SAFE_FLAN",
        "GITHUB_MIRROR_V1_0_1",
        "GITHUB_MIRROR_V2_1_0",
        "CMS_WIKIPEDIA_LANG_FILTERED",
        "CMS_STACKOVERFLOW_MULTILINGUAL",
        "CMS_STACKEXCHANGE",
        "PUBMED",
        "GEMINI_DOCJOINS_EN_TOP10B_GCC",
        "GEMINI_DOCJOINS_EN_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_EN_TOP20B_TOP100B_GCC",
        "GEMINI_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP20B_TOP100B_GCC",
        "SIMPLIFIED_HTML_V1_GCC",
        "GEMINI_DOCJOINS_TOXICITY_TAGGED_GCC",
        "CMS_GITHUB_V4",
        "GITHUB_HTML_V4",
        "GITHUB_OTHER_V4",
        "GITHUB_LONG_TAIL_V4",
        "CMS_GITHUB_MULTIFILE_V4",
        "GITHUB_DIFFS_WITH_COMMIT_MESSAGE",
        "ULM_ARXIV",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_ENONLY",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_NONENONLY",
        "QUORA",
        "PODCASTS_ROBOTSTXT",
        "COMBINED_REDDIT",
        "CANARIES_SHUFFLED",
        "CLM_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "TECHDOCS_DATA_SOURCE",
        "SCIENCE_PDF_70M_DOCS_FILTERED",
        "GEMINI_V1_CMS_WIKIPEDIA_LANG_FILTERED",
        "GEMINI_V1_WIKIPEDIA_DIFFS",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_TOP20B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP20B_TOP100B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_TOP20B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP20B_TOP100B_GCC_050523",
        "GEMINI_V1_SIMPLIFIED_HTML_V2_GCC",
        "GEMINI_V1_CMS_STACKOVERFLOW_MULTILINGUAL_V2",
        "GEMINI_V1_CMS_STACKEXCHANGE_DECONT",
        "GEMINI_V1_QUORA",
        "GEMINI_V1_COMBINED_REDDIT",
        "GEMINI_V1_DOCJOIN_100B_EN_TOXICITY_TAGGED_GCC_FIXED_TAGS",
        "GEMINI_V1_PUBMED",
        "GEMINI_V1_WEB_MATH_V2",
        "GEMINI_V1_CMS_GITHUB_DECONTAMINATED_V_7",
        "GEMINI_V1_GITHUB_DIFF_WITH_COMMIT_MESSAGE_V2",
        "GEMINI_V1_GITHUB_HTML_CSS_XML_V4",
        "GEMINI_V1_GITHUB_OTHER_V4",
        "GEMINI_V1_GITHUB_LONG_TAIL_V4",
        "GEMINI_V1_GITHUB_JUPTYER_NOTEBOOKS_SSTABLE",
        "GEMINI_V1_ULM_ARXIV_SSTABLE",
        "GEMINI_V1_PODCASTS_ROBOTSTXT",
        "GEMINI_V1_SCIENCE_PDF_68M_HQ_DOCS_GCC",
        "GEMINI_V1_GITHUB_TECHDOCS_V2",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_EN",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_NONEN",
        "GEMINI_V1_STEM_BOOKS_650K_TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_M3W_V2_FILTERED",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_WEBLI_EN_V4_350M_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_SCREENAI_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CULTURE_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_EN_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_I18N_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_NON_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_VTP_4F_VIDEO2TEXT_PREFIX",
        "GEMINI_V1_FORMAL_MATH_WITHOUT_HOLSTEPS_AND_MIZAR",
        "GEMINI_V1_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "GEMINI_V1_CANARIES_SHUFFLED_DOCJOIN_EN_NONEN_CODE_ARXIV_TRANSLATE",
        "DUET_CLOUD_SECURITY_DOCS",
        "DUET_GITHUB_CODE_SNIPPETS",
        "DUET_GITHUB_FILES",
        "DUET_GOBYEXAMPLE",
        "DUET_GOLANG_DOCS",
        "DUET_CLOUD_DOCS_TROUBLESHOOTING_TABLES",
        "DUET_DEVSITE_DOCS",
        "DUET_CLOUD_BLOG_POSTS",
        "DUET_CLOUD_PODCAST_EPISODES",
        "DUET_YOUTUBE_VIDEOS",
        "DUET_CLOUD_SKILLS_BOOST",
        "DUET_CLOUD_DOCS",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_GENERATED",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_HANDWRITTEN",
        "DUET_GOOGLESQL_GENERATION",
        "DUET_CLOUD_IX_PROMPTS",
        "DUET_RAD",
        "BARD_ARCADE_GITHUB",
        "MOBILE_ASSISTANT_MAGI_FILTERED_0825_373K",
        "MOBILE_ASSISTANT_PALM24B_FILTERED_400K",
        "GENESIS_NEWS_INSIGHTS",
        "CLOUD_SECURITY_PRETRAINING",
        "CLOUD_SECURITY_FINETUNING",
        "LABS_AQA_DSCOUT",
        "LABS_AQA_TAILWIND",
        "LABS_AQA_DELEWARE",
        "GEMINI_MULTIMODAL_FT_URL",
        "GEMINI_MULTIMODAL_FT_YT",
        "GEMINI_MULTIMODAL_FT_SHUTTERSTOCK",
        "GEMINI_MULTIMODAL_FT_NONE",
        "GEMINI_MULTIMODAL_FT_OTHER",
        "GEMINI_MULTIMODAL_FT_INK",
        "GEMINI_MULTIMODAL_IT",
        "GEMINI_IT_SHUTTERSTOCK",
        "GEMINI_IT_M3W",
        "GEMINI_IT_HEDGING",
        "GEMINI_IT_DSCOUT_FACTUALITY",
        "GEMINI_IT_AQUAMUSE",
        "GEMINI_IT_SHOTGUN",
        "GEMINI_IT_ACI_BENCH",
        "GEMINI_IT_SPIDER_FILTERED",
        "GEMINI_IT_TAB_SUM_BQ",
        "GEMINI_IT_QA_WITH_URL",
        "GEMINI_IT_CODE_INSTRUCT",
        "GEMINI_IT_MED_PALM",
        "GEMINI_IT_TASK_ORIENTED_DIALOG",
        "GEMINI_IT_NIMBUS_GROUNDING_TO_PROMPT",
        "GEMINI_IT_EITL_GEN",
        "GEMINI_IT_HITL_GEN",
        "GEMINI_IT_MECH",
        "GEMINI_IT_TABLE_GEN",
        "GEMINI_IT_NIMBUS_DECIBEL",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMINI_V2_CMS_WIKIPEDIA_LANG_FILTERED_GCC_PII",
        "GEMINI_V2_WIKIPEDIA_DIFFS_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_QUORA_COMPLIANT",
        "GEMINI_V2_FORUMS_V2_COMPLIANT",
        "GEMINI_V2_CMS_STACKOVERFLOW_MULTILINGUAL_V2_COMPLIANT",
        "GEMINI_V2_SIMPLIFIED_HTML_V2_CORRECT_FORMAT_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_TOXICITY_TAGGED_FIXED_TAGS_COMPLIANT",
        "GEMINI_V2_CODEWEB_V1_COMPLIANT",
        "GEMINI_V2_LEETCODE_GCC_PII",
        "GEMINI_V2_CODE_CONTESTS_COMPLIANT",
        "GEMINI_V2_CMS_GITHUB_MULTI_FILE_FOR_FIM_GEMBAGZ_FIXED_BYTES_LENGTHS",
        "GEMINI_V2_GITHUB_EVALED_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_NON_EVAL_HIGH_PRI_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_LOW_PRI_LANGUAGES_AND_CONFIGS_COMPLIANT",
        "GEMINI_V2_GITHUB_LONG_TAIL_AND_STRUCTURED_DATA_COMPLIANT",
        "GEMINI_V2_GITHUB_PYTHON_NOTEBOOKS_COMPLIANT",
        "GEMINI_V2_GITHUB_DIFFS_COMPLIANT",
        "GEMINI_V2_GITHUB_TECHDOCS_COMPLIANT",
        "GEMINI_V2_HIGH_QUALITY_CODE_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_SCIENCE_PDF_68M_HQ_DOCS_DEDUP_COMPLIANT_CLEAN_TEX",
        "GEMINI_V2_ARXIV_2023_COMPLIANT",
        "GEMINI_V2_FORMAL_COMPLIANT",
        "GEMINI_V2_CMS_STACKEXCHANGE_COMPLIANT",
        "GEMINI_V2_PUBMED_COMPLIANT",
        "GEMINI_V2_WEB_MATH_V3_COMPLIANT",
        "GEMINI_V2_SCIENCEWEB_V0_GCC_PII",
        "GEMINI_V2_WEB_POLYMATH_V1_COMPLIANT",
        "GEMINI_V2_MATH_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_BIOLOGY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_PHYSICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHEMISTRY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MACHINE_LEARNING_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_QA_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_ECONOMICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MEDICAL_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHESS_COMPLIANT",
        "GEMINI_V2_YOUTUBE_SCIENCE_V4_FILTERED_COMPLIANT",
        "GEMINI_V2_GOALDMINE_XL_GENERATED_PLUS_GT_NO_DM_MATH_COMPLIANT",
        "GEMINI_V2_FIRSTTIMES_SCIENCE_PDF_DEDUP_HQ_LENGTH_FILTERED_COMPLIANT",
        "GEMINI_V2_PODCASTS_COMPLIANT",
        "GEMINI_V2_EN_NONSCIENCE_PDF_DEDUP_46M_DOCS_COMPLIANT",
        "GEMINI_V2_NONPUB_COPYRIGHT_BOOKS_V3_70_CONF_082323_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_COPYRIGHT_BOOKS_V3_111823_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_BOOKS_318K_TEXT_COMPLIANT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_T2I_TEXT_TO_IMAGE_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_I18N_680M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_FULL_HTML_75M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_V1_1_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_DOC_240M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_VIDEO_VIDEO_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M4W_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CULTURE_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_DETECTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_ALT_TEXT_NONEN_500M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SPATIAL_AWARE_PALI_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_3D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_NON_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_3D_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CC3M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_INFOGRAPHICS_LARGE_WEB_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_BIORXIV_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_IM2SOL_PROBLEM_AND_SOLUTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PLOT2TABLE_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TIKZ_DERENDERING_MERGED_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_2D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WIKIPEDIA_EQUATIONS_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_EQ2LATEX_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_ARXIV_EQUATIONS_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_HEAD_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_CLM_TRANSLATE_DATAV3_WEB_UNWMT_INCR_MIX",
        "GEMINI_V2_NTL_NTLV4A_MONOLINGUAL_DEDUP_N5",
        "GEMINI_V2_NTL_STT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_TRANSLIT_BILEX_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_BT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_FT_FIXED_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_CANARIES_SHUFFLED_COMPLIANT",
    ]
    displayAttributionMessage: str
    docAttribution: LanguageLabsAidaTrustRecitationProtoDocAttribution
    docOccurrences: int
    endIndex: int
    rawText: str
    segmentRecitationAction: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "CITE", "BLOCK", "NO_ACTION", "EXEMPT_FOUND_IN_PROMPT"
    ]
    startIndex: int

@typing.type_check_only
class LanguageLabsAidaTrustRecitationProtoStreamRecitationResult(
    typing_extensions.TypedDict, total=False
):
    dynamicSegmentResults: _list[LanguageLabsAidaTrustRecitationProtoSegmentResult]
    fullyCheckedTextIndex: int
    recitationAction: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "CITE", "BLOCK", "NO_ACTION", "EXEMPT_FOUND_IN_PROMPT"
    ]
    trainingSegmentResults: _list[LanguageLabsAidaTrustRecitationProtoSegmentResult]

@typing.type_check_only
class LearningGenaiRecitationDocAttribution(typing_extensions.TypedDict, total=False):
    amarnaId: str
    arxivId: str
    author: str
    bibkey: str
    biorxivId: str
    bookTitle: str
    bookVolumeId: str
    conversationId: str
    dataset: typing_extensions.Literal[
        "DATASET_UNSPECIFIED",
        "WIKIPEDIA",
        "WEBDOCS",
        "WEBDOCS_FINETUNE",
        "GITHUB_MIRROR",
        "BOOKS_FULL_VIEW",
        "BOOKS_PRIVATE",
        "GNEWS",
        "ULM_DOCJOINS",
        "ULM_DOCJOINS_DEDUPED",
        "MEENA_FC",
        "PODCAST",
        "AQUA",
        "WEB_ASR",
        "BARD_GOLDEN",
        "COMMON_SENSE_REASONING",
        "MATH",
        "MATH_REASONING",
        "CLEAN_ARXIV",
        "LAMDA_FACTUALITY_E2E_QUERY_GENERATION",
        "LAMDA_FACTUALITY_E2E_RESPONSE_GENERATION",
        "MASSIVE_FORUM_THREAD_SCORED_BARD",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_200",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_500",
        "DOCUMENT_CHUNKS",
        "MEENA_RESEARCH_PHASE_GOLDEN_MARKDOWN",
        "MEENA_RESEARCH_PHASE_GOOGLERS",
        "MEENA_RESPONSE_SAFETY_HUMAN_GEN",
        "MEENA_RESPONSE_SAFETY_SCHEMA_NO_BROADCAST",
        "MEENA_RESPONSE_SAFETY_V3_HUMAN_GEN2",
        "MEENA_RESPONSE_SAFETY_V3_SCHEMA_NO_BROADCAST",
        "LAMDA_FACTUALITY_TRIGGER",
        "LAMDA_SAFETY_V2_SCHEMA_NO_BROADCAST",
        "LAMDA_SSI_DISCRIMINATIVE",
        "ASSISTANT_PERSONALITY_SAFETY",
        "PODCAST_FINETUNE_DIALOG",
        "WORLD_QUERY_GENERATOR",
        "C4_JOINED_DOCJOINS",
        "HOL4_THEORIES",
        "HOL_LIGHT_THEORIES",
        "HOLSTEPS",
        "ISABELLE_STEP",
        "ISABELLE_THEORIES",
        "LEAN_MATHLIB_THEORIES",
        "LEAN_STEP",
        "MIZAR_THEORIES",
        "COQ_STEP",
        "COQ_THEORIES",
        "AMPS_KHAN",
        "AMPS_MATHEMATICA",
        "CODEY_CODE",
        "CODE_QA_SE",
        "CODE_QA_SO",
        "CODE_QA_FT_FORMAT",
        "CODE_QA_FT_KNOWLEDGE",
        "CODE_QA_GITHUB_FILTERED_CODE",
        "BARD_PERSONALITY_GOLDEN",
        "ULM_DOCJOINS_WITH_URLS_EN",
        "ULM_DOCJOINS_WITH_URLS_I18N",
        "GOODALL_MTV5_GITHUB",
        "GOODALL_MTV5_BOOKS",
        "GOODALL_MTV5_C4",
        "GOODALL_MTV5_WIKIPEDIA",
        "GOODALL_MW_TOP_100B",
        "GOODALL_MW_STACK_EXCHANGE",
        "GOODALL_MW_TOP_0_10B",
        "GOODALL_MW_TOP_10B_20B",
        "CODEY_NOTEBOOK_LM_PRETRAINING",
        "VERTEX_SAFE_FLAN",
        "GITHUB_MIRROR_V1_0_1",
        "GITHUB_MIRROR_V2_1_0",
        "CMS_WIKIPEDIA_LANG_FILTERED",
        "CMS_STACKOVERFLOW_MULTILINGUAL",
        "CMS_STACKEXCHANGE",
        "PUBMED",
        "GEMINI_DOCJOINS_EN_TOP10B_GCC",
        "GEMINI_DOCJOINS_EN_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_EN_TOP20B_TOP100B_GCC",
        "GEMINI_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP20B_TOP100B_GCC",
        "SIMPLIFIED_HTML_V1_GCC",
        "GEMINI_DOCJOINS_TOXICITY_TAGGED_GCC",
        "CMS_GITHUB_V4",
        "GITHUB_HTML_V4",
        "GITHUB_OTHER_V4",
        "GITHUB_LONG_TAIL_V4",
        "CMS_GITHUB_MULTIFILE_V4",
        "GITHUB_DIFFS_WITH_COMMIT_MESSAGE",
        "ULM_ARXIV",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_ENONLY",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_NONENONLY",
        "QUORA",
        "PODCASTS_ROBOTSTXT",
        "COMBINED_REDDIT",
        "CANARIES_SHUFFLED",
        "CLM_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "TECHDOCS_DATA_SOURCE",
        "SCIENCE_PDF_70M_DOCS_FILTERED",
        "GEMINI_V1_CMS_WIKIPEDIA_LANG_FILTERED",
        "GEMINI_V1_WIKIPEDIA_DIFFS",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_TOP20B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP20B_TOP100B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_TOP20B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP20B_TOP100B_GCC_050523",
        "GEMINI_V1_SIMPLIFIED_HTML_V2_GCC",
        "GEMINI_V1_CMS_STACKOVERFLOW_MULTILINGUAL_V2",
        "GEMINI_V1_CMS_STACKEXCHANGE_DECONT",
        "GEMINI_V1_QUORA",
        "GEMINI_V1_COMBINED_REDDIT",
        "GEMINI_V1_DOCJOIN_100B_EN_TOXICITY_TAGGED_GCC_FIXED_TAGS",
        "GEMINI_V1_PUBMED",
        "GEMINI_V1_WEB_MATH_V2",
        "GEMINI_V1_CMS_GITHUB_DECONTAMINATED_V_7",
        "GEMINI_V1_GITHUB_DIFF_WITH_COMMIT_MESSAGE_V2",
        "GEMINI_V1_GITHUB_HTML_CSS_XML_V4",
        "GEMINI_V1_GITHUB_OTHER_V4",
        "GEMINI_V1_GITHUB_LONG_TAIL_V4",
        "GEMINI_V1_GITHUB_JUPTYER_NOTEBOOKS_SSTABLE",
        "GEMINI_V1_ULM_ARXIV_SSTABLE",
        "GEMINI_V1_PODCASTS_ROBOTSTXT",
        "GEMINI_V1_SCIENCE_PDF_68M_HQ_DOCS_GCC",
        "GEMINI_V1_GITHUB_TECHDOCS_V2",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_EN",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_NONEN",
        "GEMINI_V1_STEM_BOOKS_650K_TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_M3W_V2_FILTERED",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_WEBLI_EN_V4_350M_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_SCREENAI_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CULTURE_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_EN_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_I18N_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_NON_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_VTP_4F_VIDEO2TEXT_PREFIX",
        "GEMINI_V1_FORMAL_MATH_WITHOUT_HOLSTEPS_AND_MIZAR",
        "GEMINI_V1_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "GEMINI_V1_CANARIES_SHUFFLED_DOCJOIN_EN_NONEN_CODE_ARXIV_TRANSLATE",
        "DUET_CLOUD_SECURITY_DOCS",
        "DUET_GITHUB_CODE_SNIPPETS",
        "DUET_GITHUB_FILES",
        "DUET_GOBYEXAMPLE",
        "DUET_GOLANG_DOCS",
        "DUET_CLOUD_DOCS_TROUBLESHOOTING_TABLES",
        "DUET_DEVSITE_DOCS",
        "DUET_CLOUD_BLOG_POSTS",
        "DUET_CLOUD_PODCAST_EPISODES",
        "DUET_YOUTUBE_VIDEOS",
        "DUET_CLOUD_SKILLS_BOOST",
        "DUET_CLOUD_DOCS",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_GENERATED",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_HANDWRITTEN",
        "DUET_GOOGLESQL_GENERATION",
        "DUET_CLOUD_IX_PROMPTS",
        "DUET_RAD",
        "BARD_ARCADE_GITHUB",
        "MOBILE_ASSISTANT_MAGI_FILTERED_0825_373K",
        "MOBILE_ASSISTANT_PALM24B_FILTERED_400K",
        "GENESIS_NEWS_INSIGHTS",
        "CLOUD_SECURITY_PRETRAINING",
        "CLOUD_SECURITY_FINETUNING",
        "LABS_AQA_DSCOUT",
        "LABS_AQA_TAILWIND",
        "LABS_AQA_DELEWARE",
        "GEMINI_MULTIMODAL_FT_URL",
        "GEMINI_MULTIMODAL_FT_YT",
        "GEMINI_MULTIMODAL_FT_SHUTTERSTOCK",
        "GEMINI_MULTIMODAL_FT_NONE",
        "GEMINI_MULTIMODAL_FT_OTHER",
        "GEMINI_MULTIMODAL_FT_INK",
        "GEMINI_MULTIMODAL_IT",
        "GEMINI_IT_SHUTTERSTOCK",
        "GEMINI_IT_M3W",
        "GEMINI_IT_HEDGING",
        "GEMINI_IT_DSCOUT_FACTUALITY",
        "GEMINI_IT_AQUAMUSE",
        "GEMINI_IT_SHOTGUN",
        "GEMINI_IT_ACI_BENCH",
        "GEMINI_IT_SPIDER_FILTERED",
        "GEMINI_IT_TAB_SUM_BQ",
        "GEMINI_IT_QA_WITH_URL",
        "GEMINI_IT_CODE_INSTRUCT",
        "GEMINI_IT_MED_PALM",
        "GEMINI_IT_TASK_ORIENTED_DIALOG",
        "GEMINI_IT_NIMBUS_GROUNDING_TO_PROMPT",
        "GEMINI_IT_EITL_GEN",
        "GEMINI_IT_HITL_GEN",
        "GEMINI_IT_MECH",
        "GEMINI_IT_TABLE_GEN",
        "GEMINI_IT_NIMBUS_DECIBEL",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMINI_V2_CMS_WIKIPEDIA_LANG_FILTERED_GCC_PII",
        "GEMINI_V2_WIKIPEDIA_DIFFS_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_QUORA_COMPLIANT",
        "GEMINI_V2_FORUMS_V2_COMPLIANT",
        "GEMINI_V2_CMS_STACKOVERFLOW_MULTILINGUAL_V2_COMPLIANT",
        "GEMINI_V2_SIMPLIFIED_HTML_V2_CORRECT_FORMAT_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_TOXICITY_TAGGED_FIXED_TAGS_COMPLIANT",
        "GEMINI_V2_CODEWEB_V1_COMPLIANT",
        "GEMINI_V2_LEETCODE_GCC_PII",
        "GEMINI_V2_CODE_CONTESTS_COMPLIANT",
        "GEMINI_V2_CMS_GITHUB_MULTI_FILE_FOR_FIM_GEMBAGZ_FIXED_BYTES_LENGTHS",
        "GEMINI_V2_GITHUB_EVALED_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_NON_EVAL_HIGH_PRI_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_LOW_PRI_LANGUAGES_AND_CONFIGS_COMPLIANT",
        "GEMINI_V2_GITHUB_LONG_TAIL_AND_STRUCTURED_DATA_COMPLIANT",
        "GEMINI_V2_GITHUB_PYTHON_NOTEBOOKS_COMPLIANT",
        "GEMINI_V2_GITHUB_DIFFS_COMPLIANT",
        "GEMINI_V2_GITHUB_TECHDOCS_COMPLIANT",
        "GEMINI_V2_HIGH_QUALITY_CODE_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_SCIENCE_PDF_68M_HQ_DOCS_DEDUP_COMPLIANT_CLEAN_TEX",
        "GEMINI_V2_ARXIV_2023_COMPLIANT",
        "GEMINI_V2_FORMAL_COMPLIANT",
        "GEMINI_V2_CMS_STACKEXCHANGE_COMPLIANT",
        "GEMINI_V2_PUBMED_COMPLIANT",
        "GEMINI_V2_WEB_MATH_V3_COMPLIANT",
        "GEMINI_V2_SCIENCEWEB_V0_GCC_PII",
        "GEMINI_V2_WEB_POLYMATH_V1_COMPLIANT",
        "GEMINI_V2_MATH_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_BIOLOGY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_PHYSICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHEMISTRY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MACHINE_LEARNING_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_QA_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_ECONOMICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MEDICAL_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHESS_COMPLIANT",
        "GEMINI_V2_YOUTUBE_SCIENCE_V4_FILTERED_COMPLIANT",
        "GEMINI_V2_GOALDMINE_XL_GENERATED_PLUS_GT_NO_DM_MATH_COMPLIANT",
        "GEMINI_V2_FIRSTTIMES_SCIENCE_PDF_DEDUP_HQ_LENGTH_FILTERED_COMPLIANT",
        "GEMINI_V2_PODCASTS_COMPLIANT",
        "GEMINI_V2_EN_NONSCIENCE_PDF_DEDUP_46M_DOCS_COMPLIANT",
        "GEMINI_V2_NONPUB_COPYRIGHT_BOOKS_V3_70_CONF_082323_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_COPYRIGHT_BOOKS_V3_111823_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_BOOKS_318K_TEXT_COMPLIANT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_T2I_TEXT_TO_IMAGE_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_I18N_680M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_FULL_HTML_75M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_V1_1_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_DOC_240M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_VIDEO_VIDEO_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M4W_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CULTURE_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_DETECTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_ALT_TEXT_NONEN_500M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SPATIAL_AWARE_PALI_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_3D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_NON_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_3D_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CC3M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_INFOGRAPHICS_LARGE_WEB_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_BIORXIV_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_IM2SOL_PROBLEM_AND_SOLUTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PLOT2TABLE_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TIKZ_DERENDERING_MERGED_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_2D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WIKIPEDIA_EQUATIONS_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_EQ2LATEX_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_ARXIV_EQUATIONS_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_HEAD_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_CLM_TRANSLATE_DATAV3_WEB_UNWMT_INCR_MIX",
        "GEMINI_V2_NTL_NTLV4A_MONOLINGUAL_DEDUP_N5",
        "GEMINI_V2_NTL_STT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_TRANSLIT_BILEX_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_BT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_FT_FIXED_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_CANARIES_SHUFFLED_COMPLIANT",
    ]
    filepath: str
    geminiId: str
    gnewsArticleTitle: str
    goodallExampleId: str
    isOptOut: bool
    isPrompt: bool
    lamdaExampleId: str
    license: str
    meenaConversationId: str
    naturalLanguageCode: str
    noAttribution: bool
    podcastUtteranceId: str
    publicationDate: GoogleTypeDate
    qualityScoreExperimentOnly: float
    repo: str
    url: str
    volumeId: str
    wikipediaArticleTitle: str
    youtubeVideoId: str

@typing.type_check_only
class LearningGenaiRecitationRecitationResult(typing_extensions.TypedDict, total=False):
    dynamicSegmentResults: _list[LearningGenaiRecitationSegmentResult]
    recitationAction: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "CITE", "BLOCK", "NO_ACTION", "EXEMPT_FOUND_IN_PROMPT"
    ]
    trainingSegmentResults: _list[LearningGenaiRecitationSegmentResult]

@typing.type_check_only
class LearningGenaiRecitationSegmentResult(typing_extensions.TypedDict, total=False):
    attributionDataset: typing_extensions.Literal[
        "DATASET_UNSPECIFIED",
        "WIKIPEDIA",
        "WEBDOCS",
        "WEBDOCS_FINETUNE",
        "GITHUB_MIRROR",
        "BOOKS_FULL_VIEW",
        "BOOKS_PRIVATE",
        "GNEWS",
        "ULM_DOCJOINS",
        "ULM_DOCJOINS_DEDUPED",
        "MEENA_FC",
        "PODCAST",
        "AQUA",
        "WEB_ASR",
        "BARD_GOLDEN",
        "COMMON_SENSE_REASONING",
        "MATH",
        "MATH_REASONING",
        "CLEAN_ARXIV",
        "LAMDA_FACTUALITY_E2E_QUERY_GENERATION",
        "LAMDA_FACTUALITY_E2E_RESPONSE_GENERATION",
        "MASSIVE_FORUM_THREAD_SCORED_BARD",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_200",
        "MASSIVE_FORUM_THREAD_SCORED_LONG_500",
        "DOCUMENT_CHUNKS",
        "MEENA_RESEARCH_PHASE_GOLDEN_MARKDOWN",
        "MEENA_RESEARCH_PHASE_GOOGLERS",
        "MEENA_RESPONSE_SAFETY_HUMAN_GEN",
        "MEENA_RESPONSE_SAFETY_SCHEMA_NO_BROADCAST",
        "MEENA_RESPONSE_SAFETY_V3_HUMAN_GEN2",
        "MEENA_RESPONSE_SAFETY_V3_SCHEMA_NO_BROADCAST",
        "LAMDA_FACTUALITY_TRIGGER",
        "LAMDA_SAFETY_V2_SCHEMA_NO_BROADCAST",
        "LAMDA_SSI_DISCRIMINATIVE",
        "ASSISTANT_PERSONALITY_SAFETY",
        "PODCAST_FINETUNE_DIALOG",
        "WORLD_QUERY_GENERATOR",
        "C4_JOINED_DOCJOINS",
        "HOL4_THEORIES",
        "HOL_LIGHT_THEORIES",
        "HOLSTEPS",
        "ISABELLE_STEP",
        "ISABELLE_THEORIES",
        "LEAN_MATHLIB_THEORIES",
        "LEAN_STEP",
        "MIZAR_THEORIES",
        "COQ_STEP",
        "COQ_THEORIES",
        "AMPS_KHAN",
        "AMPS_MATHEMATICA",
        "CODEY_CODE",
        "CODE_QA_SE",
        "CODE_QA_SO",
        "CODE_QA_FT_FORMAT",
        "CODE_QA_FT_KNOWLEDGE",
        "CODE_QA_GITHUB_FILTERED_CODE",
        "BARD_PERSONALITY_GOLDEN",
        "ULM_DOCJOINS_WITH_URLS_EN",
        "ULM_DOCJOINS_WITH_URLS_I18N",
        "GOODALL_MTV5_GITHUB",
        "GOODALL_MTV5_BOOKS",
        "GOODALL_MTV5_C4",
        "GOODALL_MTV5_WIKIPEDIA",
        "GOODALL_MW_TOP_100B",
        "GOODALL_MW_STACK_EXCHANGE",
        "GOODALL_MW_TOP_0_10B",
        "GOODALL_MW_TOP_10B_20B",
        "CODEY_NOTEBOOK_LM_PRETRAINING",
        "VERTEX_SAFE_FLAN",
        "GITHUB_MIRROR_V1_0_1",
        "GITHUB_MIRROR_V2_1_0",
        "CMS_WIKIPEDIA_LANG_FILTERED",
        "CMS_STACKOVERFLOW_MULTILINGUAL",
        "CMS_STACKEXCHANGE",
        "PUBMED",
        "GEMINI_DOCJOINS_EN_TOP10B_GCC",
        "GEMINI_DOCJOINS_EN_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_EN_TOP20B_TOP100B_GCC",
        "GEMINI_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP10B_TOP20B_GCC",
        "GEMINI_DOCJOINS_I18N_TOP20B_TOP100B_GCC",
        "SIMPLIFIED_HTML_V1_GCC",
        "GEMINI_DOCJOINS_TOXICITY_TAGGED_GCC",
        "CMS_GITHUB_V4",
        "GITHUB_HTML_V4",
        "GITHUB_OTHER_V4",
        "GITHUB_LONG_TAIL_V4",
        "CMS_GITHUB_MULTIFILE_V4",
        "GITHUB_DIFFS_WITH_COMMIT_MESSAGE",
        "ULM_ARXIV",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_ENONLY",
        "NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_040623_LONG_DEDUP_NONENONLY",
        "QUORA",
        "PODCASTS_ROBOTSTXT",
        "COMBINED_REDDIT",
        "CANARIES_SHUFFLED",
        "CLM_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "TECHDOCS_DATA_SOURCE",
        "SCIENCE_PDF_70M_DOCS_FILTERED",
        "GEMINI_V1_CMS_WIKIPEDIA_LANG_FILTERED",
        "GEMINI_V1_WIKIPEDIA_DIFFS",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP10B_TOP20B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP20B_TOP100B_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_EN_TOP100B_ALL_INDEXED_GCC_NODEDUP_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP10B_TOP20B_GCC_050523",
        "GEMINI_V1_DOCJOINS_I18N_TOP20B_TOP100B_GCC_050523",
        "GEMINI_V1_SIMPLIFIED_HTML_V2_GCC",
        "GEMINI_V1_CMS_STACKOVERFLOW_MULTILINGUAL_V2",
        "GEMINI_V1_CMS_STACKEXCHANGE_DECONT",
        "GEMINI_V1_QUORA",
        "GEMINI_V1_COMBINED_REDDIT",
        "GEMINI_V1_DOCJOIN_100B_EN_TOXICITY_TAGGED_GCC_FIXED_TAGS",
        "GEMINI_V1_PUBMED",
        "GEMINI_V1_WEB_MATH_V2",
        "GEMINI_V1_CMS_GITHUB_DECONTAMINATED_V_7",
        "GEMINI_V1_GITHUB_DIFF_WITH_COMMIT_MESSAGE_V2",
        "GEMINI_V1_GITHUB_HTML_CSS_XML_V4",
        "GEMINI_V1_GITHUB_OTHER_V4",
        "GEMINI_V1_GITHUB_LONG_TAIL_V4",
        "GEMINI_V1_GITHUB_JUPTYER_NOTEBOOKS_SSTABLE",
        "GEMINI_V1_ULM_ARXIV_SSTABLE",
        "GEMINI_V1_PODCASTS_ROBOTSTXT",
        "GEMINI_V1_SCIENCE_PDF_68M_HQ_DOCS_GCC",
        "GEMINI_V1_GITHUB_TECHDOCS_V2",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_EN",
        "GEMINI_V1_NONPUB_COPYRIGHT_BOOKS_V2_70_CONF_LONG_DEDUP_NONEN",
        "GEMINI_V1_STEM_BOOKS_650K_TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_M3W_V2_FILTERED",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_WEBLI_EN_V4_350M_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_SCREENAI_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CULTURE_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_EN_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_CC3M_I18N_PREFIXED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_OCR_NON_EN_PREFIXED_FILTERED_IMAGE2TEXT",
        "GEMINI_V1_VQCOCA_1B_MULTIRES_VTP_4F_VIDEO2TEXT_PREFIX",
        "GEMINI_V1_FORMAL_MATH_WITHOUT_HOLSTEPS_AND_MIZAR",
        "GEMINI_V1_TRANSLATE_DATAV2_ALLTIERS_GCC_MIX",
        "GEMINI_V1_CANARIES_SHUFFLED_DOCJOIN_EN_NONEN_CODE_ARXIV_TRANSLATE",
        "DUET_CLOUD_SECURITY_DOCS",
        "DUET_GITHUB_CODE_SNIPPETS",
        "DUET_GITHUB_FILES",
        "DUET_GOBYEXAMPLE",
        "DUET_GOLANG_DOCS",
        "DUET_CLOUD_DOCS_TROUBLESHOOTING_TABLES",
        "DUET_DEVSITE_DOCS",
        "DUET_CLOUD_BLOG_POSTS",
        "DUET_CLOUD_PODCAST_EPISODES",
        "DUET_YOUTUBE_VIDEOS",
        "DUET_CLOUD_SKILLS_BOOST",
        "DUET_CLOUD_DOCS",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_GENERATED",
        "DUET_CLOUD_GITHUB_CODE_SNIPPETS_HANDWRITTEN",
        "DUET_GOOGLESQL_GENERATION",
        "DUET_CLOUD_IX_PROMPTS",
        "DUET_RAD",
        "BARD_ARCADE_GITHUB",
        "MOBILE_ASSISTANT_MAGI_FILTERED_0825_373K",
        "MOBILE_ASSISTANT_PALM24B_FILTERED_400K",
        "GENESIS_NEWS_INSIGHTS",
        "CLOUD_SECURITY_PRETRAINING",
        "CLOUD_SECURITY_FINETUNING",
        "LABS_AQA_DSCOUT",
        "LABS_AQA_TAILWIND",
        "LABS_AQA_DELEWARE",
        "GEMINI_MULTIMODAL_FT_URL",
        "GEMINI_MULTIMODAL_FT_YT",
        "GEMINI_MULTIMODAL_FT_SHUTTERSTOCK",
        "GEMINI_MULTIMODAL_FT_NONE",
        "GEMINI_MULTIMODAL_FT_OTHER",
        "GEMINI_MULTIMODAL_FT_INK",
        "GEMINI_MULTIMODAL_IT",
        "GEMINI_IT_SHUTTERSTOCK",
        "GEMINI_IT_M3W",
        "GEMINI_IT_HEDGING",
        "GEMINI_IT_DSCOUT_FACTUALITY",
        "GEMINI_IT_AQUAMUSE",
        "GEMINI_IT_SHOTGUN",
        "GEMINI_IT_ACI_BENCH",
        "GEMINI_IT_SPIDER_FILTERED",
        "GEMINI_IT_TAB_SUM_BQ",
        "GEMINI_IT_QA_WITH_URL",
        "GEMINI_IT_CODE_INSTRUCT",
        "GEMINI_IT_MED_PALM",
        "GEMINI_IT_TASK_ORIENTED_DIALOG",
        "GEMINI_IT_NIMBUS_GROUNDING_TO_PROMPT",
        "GEMINI_IT_EITL_GEN",
        "GEMINI_IT_HITL_GEN",
        "GEMINI_IT_MECH",
        "GEMINI_IT_TABLE_GEN",
        "GEMINI_IT_NIMBUS_DECIBEL",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMINI_V2_CMS_WIKIPEDIA_LANG_FILTERED_GCC_PII",
        "GEMINI_V2_WIKIPEDIA_DIFFS_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP10B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP10B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP20B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP20B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP100B_211123_PII_FILTERED",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_NONARTICLES_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_NONEN_TOP100B_111323_WITHOUT_CJKT_STOP_ARTICLES_COMPLIANT",
        "GEMINI_V2_ENGLISH_ARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_ENGLISH_NONARTICLES_TOP500B_211123_PII_FILTERED",
        "GEMINI_V2_QUORA_COMPLIANT",
        "GEMINI_V2_FORUMS_V2_COMPLIANT",
        "GEMINI_V2_CMS_STACKOVERFLOW_MULTILINGUAL_V2_COMPLIANT",
        "GEMINI_V2_SIMPLIFIED_HTML_V2_CORRECT_FORMAT_COMPLIANT",
        "GEMINI_V2_GEMINI_DOCJOINS_TOXICITY_TAGGED_FIXED_TAGS_COMPLIANT",
        "GEMINI_V2_CODEWEB_V1_COMPLIANT",
        "GEMINI_V2_LEETCODE_GCC_PII",
        "GEMINI_V2_CODE_CONTESTS_COMPLIANT",
        "GEMINI_V2_CMS_GITHUB_MULTI_FILE_FOR_FIM_GEMBAGZ_FIXED_BYTES_LENGTHS",
        "GEMINI_V2_GITHUB_EVALED_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_NON_EVAL_HIGH_PRI_LANGUAGES_COMPLIANT",
        "GEMINI_V2_GITHUB_LOW_PRI_LANGUAGES_AND_CONFIGS_COMPLIANT",
        "GEMINI_V2_GITHUB_LONG_TAIL_AND_STRUCTURED_DATA_COMPLIANT",
        "GEMINI_V2_GITHUB_PYTHON_NOTEBOOKS_COMPLIANT",
        "GEMINI_V2_GITHUB_DIFFS_COMPLIANT",
        "GEMINI_V2_GITHUB_TECHDOCS_COMPLIANT",
        "GEMINI_V2_HIGH_QUALITY_CODE_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_SCIENCE_PDF_68M_HQ_DOCS_DEDUP_COMPLIANT_CLEAN_TEX",
        "GEMINI_V2_ARXIV_2023_COMPLIANT",
        "GEMINI_V2_FORMAL_COMPLIANT",
        "GEMINI_V2_CMS_STACKEXCHANGE_COMPLIANT",
        "GEMINI_V2_PUBMED_COMPLIANT",
        "GEMINI_V2_WEB_MATH_V3_COMPLIANT",
        "GEMINI_V2_SCIENCEWEB_V0_GCC_PII",
        "GEMINI_V2_WEB_POLYMATH_V1_COMPLIANT",
        "GEMINI_V2_MATH_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_BIOLOGY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_PHYSICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHEMISTRY_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MACHINE_LEARNING_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_QA_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_ECONOMICS_V2_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_MEDICAL_TARGETED_DATA_COMPLIANT2",
        "GEMINI_V2_CHESS_COMPLIANT",
        "GEMINI_V2_YOUTUBE_SCIENCE_V4_FILTERED_COMPLIANT",
        "GEMINI_V2_GOALDMINE_XL_GENERATED_PLUS_GT_NO_DM_MATH_COMPLIANT",
        "GEMINI_V2_FIRSTTIMES_SCIENCE_PDF_DEDUP_HQ_LENGTH_FILTERED_COMPLIANT",
        "GEMINI_V2_PODCASTS_COMPLIANT",
        "GEMINI_V2_EN_NONSCIENCE_PDF_DEDUP_46M_DOCS_COMPLIANT",
        "GEMINI_V2_NONPUB_COPYRIGHT_BOOKS_V3_70_CONF_082323_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_COPYRIGHT_BOOKS_V3_111823_LONG_DEDUP_ENONLY_COMPLIANT",
        "GEMINI_V2_STEM_BOOKS_318K_TEXT_COMPLIANT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M3W_WITH_IMAGE_TOKENS_INSERTED_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_T2I_TEXT_TO_IMAGE_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_EN_V4_350M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_I18N_680M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_FULL_HTML_75M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SCREENAI_V1_1_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_OCR_DOC_240M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SHUTTERSTOCK_VIDEO_VIDEO_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_M4W_INTERLEAVED_COMPLIANT_PII_FILTERED_SOFT",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CULTURE_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_DETECTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WEBLI_ALT_TEXT_NONEN_500M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_SPATIAL_AWARE_PALI_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_3D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TABLE2MD_V2_NON_EN_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_3D_DOC_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CC3M_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_INFOGRAPHICS_LARGE_WEB_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_BIORXIV_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_IM2SOL_PROBLEM_AND_SOLUTION_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PLOT2TABLE_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_TIKZ_DERENDERING_MERGED_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_CLOUDAI_TABLE2HTML_2D_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_WIKIPEDIA_EQUATIONS_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_PHOTOMATH_EQ2LATEX_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_CACHED_VQCOCA_MMFT_17T_ARXIV_EQUATIONS_V2_IMAGE_TO_TEXT_COMPLIANT_PII_FILTERED",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_ASR_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_SUP_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_TTS_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_PODIOSET_INTERLEAVE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_ENUS_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_SCIENCE_I18N_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_1P5M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_USM2B_MLPV5_YT_INTERLEAVE_HEAD_4M_GEMBAGZ_V2_COMPLIANT",
        "GEMINI_V2_CLM_TRANSLATE_DATAV3_WEB_UNWMT_INCR_MIX",
        "GEMINI_V2_NTL_NTLV4A_MONOLINGUAL_DEDUP_N5",
        "GEMINI_V2_NTL_STT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_TRANSLIT_BILEX_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_BT_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_NTL_SYN_FT_FIXED_TRANSLATE_DEDUP_N5",
        "GEMINI_V2_CANARIES_SHUFFLED_COMPLIANT",
    ]
    displayAttributionMessage: str
    docAttribution: LearningGenaiRecitationDocAttribution
    docOccurrences: int
    endIndex: int
    rawText: str
    segmentRecitationAction: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "CITE", "BLOCK", "NO_ACTION", "EXEMPT_FOUND_IN_PROMPT"
    ]
    startIndex: int

@typing.type_check_only
class LearningGenaiRootCalculationType(typing_extensions.TypedDict, total=False):
    scoreType: typing_extensions.Literal[
        "TYPE_UNKNOWN", "TYPE_SAFE", "TYPE_POLICY", "TYPE_GENERATION"
    ]
    weights: float

@typing.type_check_only
class LearningGenaiRootClassifierOutput(typing_extensions.TypedDict, total=False):
    ruleOutput: LearningGenaiRootRuleOutput
    ruleOutputs: _list[LearningGenaiRootRuleOutput]
    state: LearningGenaiRootClassifierState

@typing.type_check_only
class LearningGenaiRootClassifierOutputSummary(
    typing_extensions.TypedDict, total=False
):
    metrics: _list[LearningGenaiRootMetricOutput]
    ruleOutput: LearningGenaiRootRuleOutput
    ruleOutputs: _list[LearningGenaiRootRuleOutput]

@typing.type_check_only
class LearningGenaiRootClassifierState(typing_extensions.TypedDict, total=False):
    dataProviderOutput: _list[LearningGenaiRootDataProviderOutput]
    metricOutput: _list[LearningGenaiRootMetricOutput]

@typing.type_check_only
class LearningGenaiRootDataProviderOutput(typing_extensions.TypedDict, total=False):
    name: str
    status: UtilStatusProto

@typing.type_check_only
class LearningGenaiRootFilterMetadata(typing_extensions.TypedDict, total=False):
    confidence: typing_extensions.Literal[
        "FILTER_CONFIDENCE_UNKNOWN",
        "FILTER_CONFIDENCE_VERY_LOW",
        "FILTER_CONFIDENCE_LOW",
        "FILTER_CONFIDENCE_MEDIUM",
        "FILTER_CONFIDENCE_HIGH",
        "FILTER_CONFIDENCE_VERY_HIGH",
    ]
    debugInfo: LearningGenaiRootFilterMetadataFilterDebugInfo
    fallback: str
    info: str
    name: str
    reason: typing_extensions.Literal[
        "FILTER_REASON_UNKNOWN",
        "FILTER_REASON_NOT_FILTERED",
        "FILTER_REASON_SENSITIVE",
        "FILTER_REASON_RECITATION",
        "FILTER_REASON_LANGUAGE",
        "FILTER_REASON_TAKEDOWN",
        "FILTER_REASON_CLASSIFIER",
        "FILTER_REASON_EMPTY_RESPONSE",
        "FILTER_REASON_SIMILARITY_TAKEDOWN",
        "FILTER_REASON_UNSAFE",
        "FILTER_REASON_PAIRWISE_CLASSIFIER",
        "FILTER_REASON_CODEY",
        "FILTER_REASON_URL",
        "FILTER_REASON_EMAIL",
        "FILTER_REASON_SAFETY_CAT",
        "FILTER_REASON_REQUEST_RESPONSE_TAKEDOWN",
        "FILTER_REASON_RAI_PQC",
        "FILTER_REASON_ATLAS",
        "FILTER_REASON_RAI_CSAM",
        "FILTER_REASON_RAI_FRINGE",
        "FILTER_REASON_RAI_SPII",
        "FILTER_REASON_RAI_IMAGE_VIOLENCE",
        "FILTER_REASON_RAI_IMAGE_PORN",
        "FILTER_REASON_RAI_IMAGE_CSAM",
        "FILTER_REASON_RAI_IMAGE_PEDO",
        "FILTER_REASON_RAI_VIDEO_FRAME_VIOLENCE",
        "FILTER_REASON_RAI_VIDEO_FRAME_PORN",
        "FILTER_REASON_RAI_VIDEO_FRAME_CSAM",
        "FILTER_REASON_RAI_VIDEO_FRAME_PEDO",
        "FILTER_REASON_RAI_CONTEXTUAL_DANGEROUS",
        "FILTER_REASON_RAI_GRAIL_TEXT",
        "FILTER_REASON_RAI_GRAIL_IMAGE",
        "FILTER_REASON_RAI_SAFETYCAT",
        "FILTER_REASON_TOXICITY",
        "FILTER_REASON_ATLAS_PRICING",
        "FILTER_REASON_ATLAS_BILLING",
        "FILTER_REASON_ATLAS_NON_ENGLISH_QUESTION",
        "FILTER_REASON_ATLAS_NOT_RELATED_TO_GCP",
        "FILTER_REASON_ATLAS_AWS_AZURE_RELATED",
    ]
    text: str

@typing.type_check_only
class LearningGenaiRootFilterMetadataFilterDebugInfo(
    typing_extensions.TypedDict, total=False
):
    classifierOutput: LearningGenaiRootClassifierOutput
    defaultMetadata: str
    languageFilterResult: LearningGenaiRootLanguageFilterResult
    raiOutput: LearningGenaiRootRAIOutput
    raiResult: CloudAiNlLlmProtoServiceRaiResult
    raiSignal: CloudAiNlLlmProtoServiceRaiSignal
    streamRecitationResult: LanguageLabsAidaTrustRecitationProtoStreamRecitationResult
    takedownResult: LearningGenaiRootTakedownResult
    toxicityResult: LearningGenaiRootToxicityResult

@typing.type_check_only
class LearningGenaiRootGroundingMetadata(typing_extensions.TypedDict, total=False):
    citations: _list[LearningGenaiRootGroundingMetadataCitation]
    groundingCancelled: bool
    searchQueries: _list[str]

@typing.type_check_only
class LearningGenaiRootGroundingMetadataCitation(
    typing_extensions.TypedDict, total=False
):
    endIndex: int
    factIndex: int
    score: float
    startIndex: int

@typing.type_check_only
class LearningGenaiRootHarm(typing_extensions.TypedDict, total=False):
    contextualDangerous: bool
    csam: bool
    fringe: bool
    grailImageHarmType: LearningGenaiRootHarmGrailImageHarmType
    grailTextHarmType: LearningGenaiRootHarmGrailTextHarmType
    imageCsam: bool
    imagePedo: bool
    imagePorn: bool
    imageViolence: bool
    pqc: bool
    safetycat: LearningGenaiRootHarmSafetyCatCategories
    spii: LearningGenaiRootHarmSpiiFilter
    threshold: float
    videoFrameCsam: bool
    videoFramePedo: bool
    videoFramePorn: bool
    videoFrameViolence: bool

@typing.type_check_only
class LearningGenaiRootHarmGrailImageHarmType(typing_extensions.TypedDict, total=False):
    imageHarmType: _list[
        typing_extensions.Literal[
            "IMAGE_HARM_TYPE_UNSPECIFIED",
            "IMAGE_HARM_TYPE_PORN",
            "IMAGE_HARM_TYPE_VIOLENCE",
            "IMAGE_HARM_TYPE_CSAI",
            "IMAGE_HARM_TYPE_PEDO",
            "IMAGE_HARM_TYPE_MINORS",
            "IMAGE_HARM_TYPE_DANGEROUS",
            "IMAGE_HARM_TYPE_MEDICAL",
            "IMAGE_HARM_TYPE_RACY",
            "IMAGE_HARM_TYPE_OBSCENE",
            "IMAGE_HARM_TYPE_MINOR_PRESENCE",
            "IMAGE_HARM_TYPE_GENERATIVE_MINOR_PRESENCE",
            "IMAGE_HARM_TYPE_GENERATIVE_REALISTIC_VISIBLE_FACE",
        ]
    ]

@typing.type_check_only
class LearningGenaiRootHarmGrailTextHarmType(typing_extensions.TypedDict, total=False):
    harmType: _list[
        typing_extensions.Literal[
            "HARM_TYPE_UNSPECIFIED",
            "HARM_TYPE_HATE",
            "HARM_TYPE_TOXICITY",
            "HARM_TYPE_VIOLENCE",
            "HARM_TYPE_CSAI",
            "HARM_TYPE_SEXUAL",
            "HARM_TYPE_FRINGE",
            "HARM_TYPE_POLITICAL",
            "HARM_TYPE_MEMORIZATION",
            "HARM_TYPE_SPII",
            "HARM_TYPE_NEW_DANGEROUS",
            "HARM_TYPE_MEDICAL",
            "HARM_TYPE_HARASSMENT",
        ]
    ]

@typing.type_check_only
class LearningGenaiRootHarmSafetyCatCategories(
    typing_extensions.TypedDict, total=False
):
    categories: _list[
        typing_extensions.Literal[
            "SAFETYCAT_CATEGORY_UNSPECIFIED",
            "TOXICITY",
            "OBSCENE",
            "SEXUAL",
            "INSULT",
            "IDENTITY_HATE",
            "DEATH_HARM_TRAGEDY",
            "VIOLENCE_ABUSE",
            "FIREARMS_WEAPONS",
            "PUBLIC_SAFETY",
            "HEALTH",
            "RELIGION_BELIEF",
            "DRUGS",
            "WAR_CONFLICT",
            "POLITICS",
            "FINANCE",
            "LEGAL",
            "DANGEROUS",
            "DANGEROUS_SEVERITY",
            "HARASSMENT_SEVERITY",
            "HATE_SEVERITY",
            "SEXUAL_SEVERITY",
        ]
    ]

@typing.type_check_only
class LearningGenaiRootHarmSpiiFilter(typing_extensions.TypedDict, total=False):
    usBankRoutingMicr: bool
    usEmployerIdentificationNumber: bool
    usSocialSecurityNumber: bool

@typing.type_check_only
class LearningGenaiRootInternalMetadata(typing_extensions.TypedDict, total=False):
    scoredTokens: _list[LearningGenaiRootScoredToken]

@typing.type_check_only
class LearningGenaiRootLanguageFilterResult(typing_extensions.TypedDict, total=False):
    allowed: bool
    detectedLanguage: str
    detectedLanguageProbability: float

@typing.type_check_only
class LearningGenaiRootMetricOutput(typing_extensions.TypedDict, total=False):
    debug: str
    name: str
    numericValue: float
    status: UtilStatusProto
    stringValue: str

@typing.type_check_only
class LearningGenaiRootRAIOutput(typing_extensions.TypedDict, total=False):
    allowed: bool
    harm: LearningGenaiRootHarm
    name: str
    score: float

@typing.type_check_only
class LearningGenaiRootRegexTakedownResult(typing_extensions.TypedDict, total=False):
    allowed: bool
    takedownRegex: str

@typing.type_check_only
class LearningGenaiRootRequestResponseTakedownResult(
    typing_extensions.TypedDict, total=False
):
    allowed: bool
    requestTakedownRegex: str
    responseTakedownRegex: str

@typing.type_check_only
class LearningGenaiRootRoutingDecision(typing_extensions.TypedDict, total=False):
    metadata: LearningGenaiRootRoutingDecisionMetadata
    modelConfigId: str

@typing.type_check_only
class LearningGenaiRootRoutingDecisionMetadata(
    typing_extensions.TypedDict, total=False
):
    scoreBasedRoutingMetadata: LearningGenaiRootRoutingDecisionMetadataScoreBased
    tokenLengthBasedRoutingMetadata: LearningGenaiRootRoutingDecisionMetadataTokenLengthBased

@typing.type_check_only
class LearningGenaiRootRoutingDecisionMetadataScoreBased(
    typing_extensions.TypedDict, total=False
):
    matchedRule: LearningGenaiRootScoreBasedRoutingConfigRule
    score: LearningGenaiRootScore
    usedDefaultFallback: bool

@typing.type_check_only
class LearningGenaiRootRoutingDecisionMetadataTokenLengthBased(
    typing_extensions.TypedDict, total=False
):
    modelInputTokenMetadata: _list[
        LearningGenaiRootRoutingDecisionMetadataTokenLengthBasedModelInputTokenMetadata
    ]
    modelMaxTokenMetadata: _list[
        LearningGenaiRootRoutingDecisionMetadataTokenLengthBasedModelMaxTokenMetadata
    ]

@typing.type_check_only
class LearningGenaiRootRoutingDecisionMetadataTokenLengthBasedModelInputTokenMetadata(
    typing_extensions.TypedDict, total=False
):
    computedInputTokenLength: int
    modelId: str

@typing.type_check_only
class LearningGenaiRootRoutingDecisionMetadataTokenLengthBasedModelMaxTokenMetadata(
    typing_extensions.TypedDict, total=False
):
    maxNumInputTokens: int
    maxNumOutputTokens: int
    modelId: str

@typing.type_check_only
class LearningGenaiRootRuleOutput(typing_extensions.TypedDict, total=False):
    decision: typing_extensions.Literal["NO_MATCH", "MATCH"]
    name: str

@typing.type_check_only
class LearningGenaiRootScore(typing_extensions.TypedDict, total=False):
    calculationType: LearningGenaiRootCalculationType
    internalMetadata: LearningGenaiRootInternalMetadata
    thresholdType: LearningGenaiRootThresholdType
    tokensAndLogprobPerDecodingStep: LearningGenaiRootTokensAndLogProbPerDecodingStep
    value: float

@typing.type_check_only
class LearningGenaiRootScoreBasedRoutingConfigRule(
    typing_extensions.TypedDict, total=False
):
    equalOrGreaterThan: LearningGenaiRootScore
    lessThan: LearningGenaiRootScore
    modelConfigId: str

@typing.type_check_only
class LearningGenaiRootScoredSimilarityTakedownPhrase(
    typing_extensions.TypedDict, total=False
):
    phrase: LearningGenaiRootSimilarityTakedownPhrase
    similarityScore: float

@typing.type_check_only
class LearningGenaiRootScoredToken(typing_extensions.TypedDict, total=False):
    endTokenScore: float
    score: float
    token: str

@typing.type_check_only
class LearningGenaiRootSimilarityTakedownPhrase(
    typing_extensions.TypedDict, total=False
):
    blockedPhrase: str

@typing.type_check_only
class LearningGenaiRootSimilarityTakedownResult(
    typing_extensions.TypedDict, total=False
):
    allowed: bool
    scoredPhrases: _list[LearningGenaiRootScoredSimilarityTakedownPhrase]

@typing.type_check_only
class LearningGenaiRootTakedownResult(typing_extensions.TypedDict, total=False):
    allowed: bool
    regexTakedownResult: LearningGenaiRootRegexTakedownResult
    requestResponseTakedownResult: LearningGenaiRootRequestResponseTakedownResult
    similarityTakedownResult: LearningGenaiRootSimilarityTakedownResult

@typing.type_check_only
class LearningGenaiRootThresholdType(typing_extensions.TypedDict, total=False):
    scoreType: typing_extensions.Literal[
        "TYPE_UNKNOWN", "TYPE_SAFE", "TYPE_POLICY", "TYPE_GENERATION"
    ]
    threshold: float

@typing.type_check_only
class LearningGenaiRootTokensAndLogProbPerDecodingStep(
    typing_extensions.TypedDict, total=False
):
    chosenCandidates: _list[LearningGenaiRootTokensAndLogProbPerDecodingStepCandidate]
    topCandidates: _list[LearningGenaiRootTokensAndLogProbPerDecodingStepTopCandidates]

@typing.type_check_only
class LearningGenaiRootTokensAndLogProbPerDecodingStepCandidate(
    typing_extensions.TypedDict, total=False
):
    logProbability: float
    token: str

@typing.type_check_only
class LearningGenaiRootTokensAndLogProbPerDecodingStepTopCandidates(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[LearningGenaiRootTokensAndLogProbPerDecodingStepCandidate]

@typing.type_check_only
class LearningGenaiRootToxicityResult(typing_extensions.TypedDict, total=False):
    signals: _list[LearningGenaiRootToxicitySignal]

@typing.type_check_only
class LearningGenaiRootToxicitySignal(typing_extensions.TypedDict, total=False):
    allowed: bool
    label: typing_extensions.Literal[
        "LABEL_UNSPECIFIED",
        "NOT_SENSITIVE",
        "SENSITIVE",
        "ACCIDENTS_DISASTERS",
        "ADULT",
        "COMPUTER_SECURITY",
        "CONTROVERSIAL_SOCIAL_ISSUES",
        "DEATH_TRAGEDY",
        "DRUGS",
        "IDENTITY_ETHNICITY",
        "FINANCIAL_HARDSHIP",
        "FIREARMS_WEAPONS",
        "HEALTH",
        "INSULT",
        "LEGAL",
        "MENTAL_HEALTH",
        "POLITICS",
        "RELIGION_BELIEFS",
        "SAFETY",
        "SELF_HARM",
        "SPECIAL_NEEDS",
        "TERRORISM",
        "TOXIC",
        "TROUBLED_RELATIONSHIP",
        "VIOLENCE_ABUSE",
        "VULGAR",
        "WAR_CONFLICT",
    ]
    score: float

@typing.type_check_only
class LearningServingLlmMessageMetadata(typing_extensions.TypedDict, total=False):
    classifierSummary: LearningGenaiRootClassifierOutputSummary
    currentStreamTextLength: int
    deleted: bool
    filterMeta: _list[LearningGenaiRootFilterMetadata]
    finalMessageScore: LearningGenaiRootScore
    finishReason: typing_extensions.Literal[
        "UNSPECIFIED", "RETURN", "STOP", "MAX_TOKENS", "FILTER"
    ]
    groundingMetadata: LearningGenaiRootGroundingMetadata
    isFallback: bool
    langidResult: NlpSaftLangIdResult
    language: str
    lmPrefix: str
    originalText: str
    perStreamDecodedTokenCount: int
    raiOutputs: _list[LearningGenaiRootRAIOutput]
    recitationResult: LearningGenaiRecitationRecitationResult
    returnTokenCount: int
    scores: _list[LearningGenaiRootScore]
    streamTerminated: bool
    totalDecodedTokenCount: int
    translatedUserPrompts: _list[str]
    vertexRaiResult: CloudAiNlLlmProtoServiceRaiResult

@typing.type_check_only
class NlpSaftLangIdLocalesResult(typing_extensions.TypedDict, total=False):
    predictions: _list[NlpSaftLangIdLocalesResultLocale]

@typing.type_check_only
class NlpSaftLangIdLocalesResultLocale(typing_extensions.TypedDict, total=False):
    languageCode: str

@typing.type_check_only
class NlpSaftLangIdResult(typing_extensions.TypedDict, total=False):
    modelVersion: typing_extensions.Literal[
        "VERSION_UNSPECIFIED",
        "INDEXING_20181017",
        "INDEXING_20191206",
        "INDEXING_20200313",
        "INDEXING_20210618",
        "STANDARD_20220516",
    ]
    predictions: _list[NlpSaftLanguageSpan]
    spanPredictions: _list[NlpSaftLanguageSpanSequence]

@typing.type_check_only
class NlpSaftLanguageSpan(typing_extensions.TypedDict, total=False):
    end: int
    languageCode: str
    locales: NlpSaftLangIdLocalesResult
    probability: float
    start: int

@typing.type_check_only
class NlpSaftLanguageSpanSequence(typing_extensions.TypedDict, total=False):
    languageSpans: _list[NlpSaftLanguageSpan]
    probability: float

@typing.type_check_only
class Proto2BridgeMessageSet(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UtilStatusProto(typing_extensions.TypedDict, total=False):
    canonicalCode: int
    code: int
    message: str
    messageSet: Proto2BridgeMessageSet
    space: str
