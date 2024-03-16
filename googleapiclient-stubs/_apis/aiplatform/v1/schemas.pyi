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
        "CELEBRITY_IMG",
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
    text: str
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
        "FINISH_REASON_BLOCKLIST",
        "FINISH_REASON_PROHIBITED_CONTENT",
        "FINISH_REASON_SPII",
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
    startOffset: str

@typing.type_check_only
class CloudAiNlLlmProtoServicePromptFeedback(typing_extensions.TypedDict, total=False):
    blockReason: typing_extensions.Literal[
        "BLOCKED_REASON_UNSPECIFIED",
        "SAFETY",
        "OTHER",
        "BLOCKLIST",
        "PROHIBITED_CONTENT",
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
    influentialTerms: _list[CloudAiNlLlmProtoServiceSafetyRatingInfluentialTerm]
    probability: typing_extensions.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]
    probabilityScore: float
    severity: typing_extensions.Literal[
        "HARM_SEVERITY_UNSPECIFIED",
        "HARM_SEVERITY_NEGLIGIBLE",
        "HARM_SEVERITY_LOW",
        "HARM_SEVERITY_MEDIUM",
        "HARM_SEVERITY_HIGH",
    ]
    severityScore: float

@typing.type_check_only
class CloudAiNlLlmProtoServiceSafetyRatingInfluentialTerm(
    typing_extensions.TypedDict, total=False
):
    beginOffset: int
    confidence: float
    source: typing_extensions.Literal["SOURCE_UNSPECIFIED", "PROMPT", "RESPONSE"]
    term: str

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
class GoogleCloudAiplatformV1ActiveLearningConfig(
    typing_extensions.TypedDict, total=False
):
    maxDataItemCount: str
    maxDataItemPercentage: int
    sampleConfig: GoogleCloudAiplatformV1SampleConfig
    trainingConfig: GoogleCloudAiplatformV1TrainingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[str]
    executions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextChildrenRequest(
    typing_extensions.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextChildrenResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddExecutionEventsRequest(
    typing_extensions.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1Event]

@typing.type_check_only
class GoogleCloudAiplatformV1AddExecutionEventsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddTrialMeasurementRequest(
    typing_extensions.TypedDict, total=False
):
    measurement: GoogleCloudAiplatformV1Measurement

@typing.type_check_only
class GoogleCloudAiplatformV1Annotation(typing_extensions.TypedDict, total=False):
    annotationSource: GoogleCloudAiplatformV1UserActionReference
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    payloadSchemaUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1AnnotationSpec(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1Artifact(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAiplatformV1AssignNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1AssignNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
):
    notebookRuntime: GoogleCloudAiplatformV1NotebookRuntime
    notebookRuntimeId: str
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1Attribution(typing_extensions.TypedDict, total=False):
    approximationError: float
    baselineOutputValue: float
    featureAttributions: typing.Any
    instanceOutputValue: float
    outputDisplayName: str
    outputIndex: _list[int]
    outputName: str

@typing.type_check_only
class GoogleCloudAiplatformV1AutomaticResources(
    typing_extensions.TypedDict, total=False
):
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1AutoscalingMetricSpec(
    typing_extensions.TypedDict, total=False
):
    metricName: str
    target: int

@typing.type_check_only
class GoogleCloudAiplatformV1AvroSource(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCancelPipelineJobsRequest(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateFeaturesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateFeaturesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1CreateFeatureRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1Feature]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1CreateTensorboardRunRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse(
    typing_extensions.TypedDict, total=False
):
    tensorboardRuns: _list[GoogleCloudAiplatformV1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1CreateTensorboardTimeSeriesRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse(
    typing_extensions.TypedDict, total=False
):
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchDedicatedResources(
    typing_extensions.TypedDict, total=False
):
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    maxReplicaCount: int
    startingReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1BatchDeletePipelineJobsRequest(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest(
    typing_extensions.TypedDict, total=False
):
    evaluatedAnnotations: _list[GoogleCloudAiplatformV1EvaluatedAnnotation]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse(
    typing_extensions.TypedDict, total=False
):
    importedEvaluatedAnnotationsCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportModelEvaluationSlicesRequest(
    typing_extensions.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1ModelEvaluationSlice]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportModelEvaluationSlicesResponse(
    typing_extensions.TypedDict, total=False
):
    importedModelEvaluationSlices: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    partialResults: _list[
        GoogleCloudAiplatformV1BatchMigrateResourcesOperationMetadataPartialResult
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesOperationMetadataPartialResult(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    error: GoogleRpcStatus
    model: str
    request: GoogleCloudAiplatformV1MigrateResourceRequest

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    migrateResourceRequests: _list[GoogleCloudAiplatformV1MigrateResourceRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    migrateResourceResponses: _list[GoogleCloudAiplatformV1MigrateResourceResponse]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJob(
    typing_extensions.TypedDict, total=False
):
    completionStats: GoogleCloudAiplatformV1CompletionStats
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1BatchDedicatedResources
    disableContainerLogging: bool
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    explanationSpec: GoogleCloudAiplatformV1ExplanationSpec
    generateExplanation: bool
    inputConfig: GoogleCloudAiplatformV1BatchPredictionJobInputConfig
    instanceConfig: GoogleCloudAiplatformV1BatchPredictionJobInstanceConfig
    labels: dict[str, typing.Any]
    manualBatchTuningParameters: GoogleCloudAiplatformV1ManualBatchTuningParameters
    model: str
    modelParameters: typing.Any
    modelVersionId: str
    name: str
    outputConfig: GoogleCloudAiplatformV1BatchPredictionJobOutputConfig
    outputInfo: GoogleCloudAiplatformV1BatchPredictionJobOutputInfo
    partialFailures: _list[GoogleRpcStatus]
    resourcesConsumed: GoogleCloudAiplatformV1ResourcesConsumed
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
    unmanagedContainerModel: GoogleCloudAiplatformV1UnmanagedContainerModel
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1BigQuerySource
    gcsSource: GoogleCloudAiplatformV1GcsSource
    instancesFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobInstanceConfig(
    typing_extensions.TypedDict, total=False
):
    excludedFields: _list[str]
    includedFields: _list[str]
    instanceType: str
    keyField: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobOutputConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    gcsDestination: GoogleCloudAiplatformV1GcsDestination
    predictionsFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobOutputInfo(
    typing_extensions.TypedDict, total=False
):
    bigqueryOutputDataset: str
    bigqueryOutputTable: str
    gcsOutputDirectory: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    bigqueryReadInstances: GoogleCloudAiplatformV1BigQuerySource
    csvReadInstances: GoogleCloudAiplatformV1CsvSource
    destination: GoogleCloudAiplatformV1FeatureValueDestination
    entityTypeSpecs: _list[
        GoogleCloudAiplatformV1BatchReadFeatureValuesRequestEntityTypeSpec
    ]
    passThroughFields: _list[
        GoogleCloudAiplatformV1BatchReadFeatureValuesRequestPassThroughField
    ]
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesRequestEntityTypeSpec(
    typing_extensions.TypedDict, total=False
):
    entityTypeId: str
    featureSelector: GoogleCloudAiplatformV1FeatureSelector
    settings: _list[GoogleCloudAiplatformV1DestinationFeatureSetting]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesRequestPassThroughField(
    typing_extensions.TypedDict, total=False
):
    fieldName: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    timeSeriesData: _list[GoogleCloudAiplatformV1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1BigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1BigQuerySource(typing_extensions.TypedDict, total=False):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1Blob(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1BlurBaselineConfig(
    typing_extensions.TypedDict, total=False
):
    maxBlurSigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1BoolArray(typing_extensions.TypedDict, total=False):
    values: _list[bool]

@typing.type_check_only
class GoogleCloudAiplatformV1CancelBatchPredictionJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelCustomJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelDataLabelingJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelHyperparameterTuningJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelNasJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelPipelineJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelTrainingPipelineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1Candidate(typing_extensions.TypedDict, total=False):
    citationMetadata: GoogleCloudAiplatformV1CitationMetadata
    content: GoogleCloudAiplatformV1Content
    finishMessage: str
    finishReason: typing_extensions.Literal[
        "FINISH_REASON_UNSPECIFIED",
        "STOP",
        "MAX_TOKENS",
        "SAFETY",
        "RECITATION",
        "OTHER",
    ]
    groundingMetadata: GoogleCloudAiplatformV1GroundingMetadata
    index: int
    safetyRatings: _list[GoogleCloudAiplatformV1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateMetatdata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    study: str
    trial: str

@typing.type_check_only
class GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateResponse(
    typing_extensions.TypedDict, total=False
):
    shouldStop: bool

@typing.type_check_only
class GoogleCloudAiplatformV1Citation(typing_extensions.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: GoogleTypeDate
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1CitationMetadata(typing_extensions.TypedDict, total=False):
    citations: _list[GoogleCloudAiplatformV1Citation]

@typing.type_check_only
class GoogleCloudAiplatformV1CompleteTrialRequest(
    typing_extensions.TypedDict, total=False
):
    finalMeasurement: GoogleCloudAiplatformV1Measurement
    infeasibleReason: str
    trialInfeasible: bool

@typing.type_check_only
class GoogleCloudAiplatformV1CompletionStats(typing_extensions.TypedDict, total=False):
    failedCount: str
    incompleteCount: str
    successfulCount: str
    successfulForecastPointCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ComputeTokensRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ComputeTokensResponse(
    typing_extensions.TypedDict, total=False
):
    tokensInfo: _list[GoogleCloudAiplatformV1TokensInfo]

@typing.type_check_only
class GoogleCloudAiplatformV1ContainerRegistryDestination(
    typing_extensions.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1ContainerSpec(typing_extensions.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[GoogleCloudAiplatformV1EnvVar]
    imageUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1Content(typing_extensions.TypedDict, total=False):
    parts: _list[GoogleCloudAiplatformV1Part]
    role: str

@typing.type_check_only
class GoogleCloudAiplatformV1Context(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAiplatformV1CopyModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CopyModelRequest(typing_extensions.TypedDict, total=False):
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    modelId: str
    parentModel: str
    sourceModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1CopyModelResponse(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CountTokensRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1Content]
    instances: _list[typing.Any]
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1CountTokensResponse(
    typing_extensions.TypedDict, total=False
):
    totalBillableCharacters: int
    totalTokens: int

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDatasetVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDeploymentResourcePoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest(
    typing_extensions.TypedDict, total=False
):
    deploymentResourcePool: GoogleCloudAiplatformV1DeploymentResourcePool
    deploymentResourcePoolId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateEntityTypeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureGroupOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureOnlineStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureRequest(
    typing_extensions.TypedDict, total=False
):
    feature: GoogleCloudAiplatformV1Feature
    featureId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureViewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeaturestoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateIndexEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateMetadataStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateNotebookRuntimeTemplateOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreatePipelineJobRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    pipelineJob: GoogleCloudAiplatformV1PipelineJob
    pipelineJobId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateRegistryFeatureOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateSpecialistPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateTensorboardOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateTensorboardRunRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    tensorboardRun: GoogleCloudAiplatformV1TensorboardRun
    tensorboardRunId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateTensorboardTimeSeriesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    tensorboardTimeSeries: GoogleCloudAiplatformV1TensorboardTimeSeries
    tensorboardTimeSeriesId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CsvDestination(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1CsvSource(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1CustomJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobSpec: GoogleCloudAiplatformV1CustomJobSpec
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
class GoogleCloudAiplatformV1CustomJobSpec(typing_extensions.TypedDict, total=False):
    baseOutputDirectory: GoogleCloudAiplatformV1GcsDestination
    enableDashboardAccess: bool
    enableWebAccess: bool
    experiment: str
    experimentRun: str
    models: _list[str]
    network: str
    protectedArtifactLocationId: str
    reservedIpRanges: _list[str]
    scheduling: GoogleCloudAiplatformV1Scheduling
    serviceAccount: str
    tensorboard: str
    workerPoolSpecs: _list[GoogleCloudAiplatformV1WorkerPoolSpec]

@typing.type_check_only
class GoogleCloudAiplatformV1DataItem(typing_extensions.TypedDict, total=False):
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1DataItemView(typing_extensions.TypedDict, total=False):
    annotations: _list[GoogleCloudAiplatformV1Annotation]
    dataItem: GoogleCloudAiplatformV1DataItem
    hasTruncatedAnnotations: bool

@typing.type_check_only
class GoogleCloudAiplatformV1DataLabelingJob(typing_extensions.TypedDict, total=False):
    activeLearningConfig: GoogleCloudAiplatformV1ActiveLearningConfig
    annotationLabels: dict[str, typing.Any]
    createTime: str
    currentSpend: GoogleTypeMoney
    datasets: _list[str]
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
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
class GoogleCloudAiplatformV1Dataset(typing_extensions.TypedDict, total=False):
    createTime: str
    dataItemCount: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataArtifact: str
    metadataSchemaUri: str
    name: str
    savedQueries: _list[GoogleCloudAiplatformV1SavedQuery]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetVersion(typing_extensions.TypedDict, total=False):
    bigQueryDatasetName: str
    createTime: str
    displayName: str
    etag: str
    metadata: typing.Any
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1DedicatedResources(
    typing_extensions.TypedDict, total=False
):
    autoscalingMetricSpecs: _list[GoogleCloudAiplatformV1AutoscalingMetricSpec]
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectEntity
    selectTimeRangeAndFeature: GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectTimeRangeAndFeature

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectEntity(
    typing_extensions.TypedDict, total=False
):
    entityIdSelector: GoogleCloudAiplatformV1EntityIdSelector

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectTimeRangeAndFeature(
    typing_extensions.TypedDict, total=False
):
    featureSelector: GoogleCloudAiplatformV1FeatureSelector
    skipOnlineStorageDelete: bool
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectEntity
    selectTimeRangeAndFeature: GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectTimeRangeAndFeature

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectEntity(
    typing_extensions.TypedDict, total=False
):
    offlineStorageDeletedEntityRowCount: str
    onlineStorageDeletedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectTimeRangeAndFeature(
    typing_extensions.TypedDict, total=False
):
    impactedFeatureCount: str
    offlineStorageModifiedEntityRowCount: str
    onlineStorageModifiedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteMetadataStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeployIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeployIndexRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1DeployIndexResponse(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1DeployModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeployModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1DeployedModel
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployModelResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndex(typing_extensions.TypedDict, total=False):
    automaticResources: GoogleCloudAiplatformV1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    deployedIndexAuthConfig: GoogleCloudAiplatformV1DeployedIndexAuthConfig
    deploymentGroup: str
    displayName: str
    enableAccessLogging: bool
    id: str
    index: str
    indexSyncTime: str
    privateEndpoints: GoogleCloudAiplatformV1IndexPrivateEndpoints
    reservedIpRanges: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndexAuthConfig(
    typing_extensions.TypedDict, total=False
):
    authProvider: GoogleCloudAiplatformV1DeployedIndexAuthConfigAuthProvider

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndexAuthConfigAuthProvider(
    typing_extensions.TypedDict, total=False
):
    allowedIssuers: _list[str]
    audiences: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndexRef(typing_extensions.TypedDict, total=False):
    deployedIndexId: str
    displayName: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedModel(typing_extensions.TypedDict, total=False):
    automaticResources: GoogleCloudAiplatformV1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    disableContainerLogging: bool
    displayName: str
    enableAccessLogging: bool
    explanationSpec: GoogleCloudAiplatformV1ExplanationSpec
    id: str
    model: str
    modelVersionId: str
    privateEndpoints: GoogleCloudAiplatformV1PrivateEndpoints
    serviceAccount: str
    sharedResources: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedModelRef(typing_extensions.TypedDict, total=False):
    deployedModelId: str
    endpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeploymentResourcePool(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1DestinationFeatureSetting(
    typing_extensions.TypedDict, total=False
):
    destinationField: str
    featureId: str

@typing.type_check_only
class GoogleCloudAiplatformV1DirectPredictRequest(
    typing_extensions.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1DirectPredictResponse(
    typing_extensions.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1DirectRawPredictRequest(
    typing_extensions.TypedDict, total=False
):
    input: str
    methodName: str

@typing.type_check_only
class GoogleCloudAiplatformV1DirectRawPredictResponse(
    typing_extensions.TypedDict, total=False
):
    output: str

@typing.type_check_only
class GoogleCloudAiplatformV1DiskSpec(typing_extensions.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1DoubleArray(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1EncryptionSpec(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class GoogleCloudAiplatformV1Endpoint(typing_extensions.TypedDict, total=False):
    createTime: str
    deployedModels: _list[GoogleCloudAiplatformV1DeployedModel]
    description: str
    displayName: str
    enablePrivateServiceConnect: bool
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    modelDeploymentMonitoringJob: str
    name: str
    network: str
    predictRequestResponseLoggingConfig: GoogleCloudAiplatformV1PredictRequestResponseLoggingConfig
    privateServiceConnectConfig: GoogleCloudAiplatformV1PrivateServiceConnectConfig
    trafficSplit: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1EntityIdSelector(typing_extensions.TypedDict, total=False):
    csvSource: GoogleCloudAiplatformV1CsvSource
    entityIdField: str

@typing.type_check_only
class GoogleCloudAiplatformV1EntityType(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    monitoringConfig: GoogleCloudAiplatformV1FeaturestoreMonitoringConfig
    name: str
    offlineStorageTtlDays: int
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1EnvVar(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1ErrorAnalysisAnnotation(
    typing_extensions.TypedDict, total=False
):
    attributedItems: _list[GoogleCloudAiplatformV1ErrorAnalysisAnnotationAttributedItem]
    outlierScore: float
    outlierThreshold: float
    queryType: typing_extensions.Literal[
        "QUERY_TYPE_UNSPECIFIED",
        "ALL_SIMILAR",
        "SAME_CLASS_SIMILAR",
        "SAME_CLASS_DISSIMILAR",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ErrorAnalysisAnnotationAttributedItem(
    typing_extensions.TypedDict, total=False
):
    annotationResourceName: str
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluatedAnnotation(
    typing_extensions.TypedDict, total=False
):
    dataItemPayload: typing.Any
    errorAnalysisAnnotations: _list[GoogleCloudAiplatformV1ErrorAnalysisAnnotation]
    evaluatedDataItemViewId: str
    explanations: _list[GoogleCloudAiplatformV1EvaluatedAnnotationExplanation]
    groundTruths: _list[typing.Any]
    predictions: _list[typing.Any]
    type: typing_extensions.Literal[
        "EVALUATED_ANNOTATION_TYPE_UNSPECIFIED",
        "TRUE_POSITIVE",
        "FALSE_POSITIVE",
        "FALSE_NEGATIVE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluatedAnnotationExplanation(
    typing_extensions.TypedDict, total=False
):
    explanation: GoogleCloudAiplatformV1Explanation
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1Event(typing_extensions.TypedDict, total=False):
    artifact: str
    eventTime: str
    execution: str
    labels: dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INPUT", "OUTPUT"]

@typing.type_check_only
class GoogleCloudAiplatformV1Examples(typing_extensions.TypedDict, total=False):
    exampleGcsSource: GoogleCloudAiplatformV1ExamplesExampleGcsSource
    nearestNeighborSearchConfig: typing.Any
    neighborCount: int
    presets: GoogleCloudAiplatformV1Presets

@typing.type_check_only
class GoogleCloudAiplatformV1ExamplesExampleGcsSource(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal["DATA_FORMAT_UNSPECIFIED", "JSONL"]
    gcsSource: GoogleCloudAiplatformV1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1ExamplesOverride(typing_extensions.TypedDict, total=False):
    crowdingCount: int
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "INSTANCES", "EMBEDDINGS"
    ]
    neighborCount: int
    restrictions: _list[GoogleCloudAiplatformV1ExamplesRestrictionsNamespace]
    returnEmbeddings: bool

@typing.type_check_only
class GoogleCloudAiplatformV1ExamplesRestrictionsNamespace(
    typing_extensions.TypedDict, total=False
):
    allow: _list[str]
    deny: _list[str]
    namespaceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1Execution(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAiplatformV1ExplainRequest(typing_extensions.TypedDict, total=False):
    deployedModelId: str
    explanationSpecOverride: GoogleCloudAiplatformV1ExplanationSpecOverride
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1ExplainResponse(typing_extensions.TypedDict, total=False):
    deployedModelId: str
    explanations: _list[GoogleCloudAiplatformV1Explanation]
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1Explanation(typing_extensions.TypedDict, total=False):
    attributions: _list[GoogleCloudAiplatformV1Attribution]
    neighbors: _list[GoogleCloudAiplatformV1Neighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadata(
    typing_extensions.TypedDict, total=False
):
    featureAttributionsSchemaUri: str
    inputs: dict[str, typing.Any]
    latentSpaceSource: str
    outputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataInputMetadata(
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
    featureValueDomain: GoogleCloudAiplatformV1ExplanationMetadataInputMetadataFeatureValueDomain
    groupName: str
    indexFeatureMapping: _list[str]
    indicesTensorName: str
    inputBaselines: _list[typing.Any]
    inputTensorName: str
    modality: str
    visualization: GoogleCloudAiplatformV1ExplanationMetadataInputMetadataVisualization

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataInputMetadataFeatureValueDomain(
    typing_extensions.TypedDict, total=False
):
    maxValue: float
    minValue: float
    originalMean: float
    originalStddev: float

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataInputMetadataVisualization(
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
class GoogleCloudAiplatformV1ExplanationMetadataOutputMetadata(
    typing_extensions.TypedDict, total=False
):
    displayNameMappingKey: str
    indexDisplayNameMapping: typing.Any
    outputTensorName: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataOverride(
    typing_extensions.TypedDict, total=False
):
    inputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataOverrideInputMetadataOverride(
    typing_extensions.TypedDict, total=False
):
    inputBaselines: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationParameters(
    typing_extensions.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1Examples
    integratedGradientsAttribution: GoogleCloudAiplatformV1IntegratedGradientsAttribution
    outputIndices: _list[typing.Any]
    sampledShapleyAttribution: GoogleCloudAiplatformV1SampledShapleyAttribution
    topK: int
    xraiAttribution: GoogleCloudAiplatformV1XraiAttribution

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationSpec(typing_extensions.TypedDict, total=False):
    metadata: GoogleCloudAiplatformV1ExplanationMetadata
    parameters: GoogleCloudAiplatformV1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationSpecOverride(
    typing_extensions.TypedDict, total=False
):
    examplesOverride: GoogleCloudAiplatformV1ExamplesOverride
    metadata: GoogleCloudAiplatformV1ExplanationMetadataOverride
    parameters: GoogleCloudAiplatformV1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataConfig(typing_extensions.TypedDict, total=False):
    annotationSchemaUri: str
    annotationsFilter: str
    exportUse: typing_extensions.Literal[
        "EXPORT_USE_UNSPECIFIED", "CUSTOM_CODE_TRAINING"
    ]
    filterSplit: GoogleCloudAiplatformV1ExportFilterSplit
    fractionSplit: GoogleCloudAiplatformV1ExportFractionSplit
    gcsDestination: GoogleCloudAiplatformV1GcsDestination
    savedQueryId: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    gcsOutputDirectory: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataRequest(
    typing_extensions.TypedDict, total=False
):
    exportConfig: GoogleCloudAiplatformV1ExportDataConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataResponse(
    typing_extensions.TypedDict, total=False
):
    dataStats: GoogleCloudAiplatformV1ModelDataStats
    exportedFiles: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    destination: GoogleCloudAiplatformV1FeatureValueDestination
    featureSelector: GoogleCloudAiplatformV1FeatureSelector
    fullExport: GoogleCloudAiplatformV1ExportFeatureValuesRequestFullExport
    settings: _list[GoogleCloudAiplatformV1DestinationFeatureSetting]
    snapshotExport: GoogleCloudAiplatformV1ExportFeatureValuesRequestSnapshotExport

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesRequestFullExport(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesRequestSnapshotExport(
    typing_extensions.TypedDict, total=False
):
    snapshotTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFilterSplit(
    typing_extensions.TypedDict, total=False
):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFractionSplit(
    typing_extensions.TypedDict, total=False
):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    outputInfo: GoogleCloudAiplatformV1ExportModelOperationMetadataOutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelOperationMetadataOutputInfo(
    typing_extensions.TypedDict, total=False
):
    artifactOutputUri: str
    imageOutputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelRequest(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudAiplatformV1ExportModelRequestOutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelRequestOutputConfig(
    typing_extensions.TypedDict, total=False
):
    artifactDestination: GoogleCloudAiplatformV1GcsDestination
    exportFormatId: str
    imageDestination: GoogleCloudAiplatformV1ContainerRegistryDestination

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    timeSeriesDataPoints: _list[GoogleCloudAiplatformV1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1Feature(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    disableMonitoring: bool
    etag: str
    labels: dict[str, typing.Any]
    monitoringStatsAnomalies: _list[
        GoogleCloudAiplatformV1FeatureMonitoringStatsAnomaly
    ]
    name: str
    pointOfContact: str
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
class GoogleCloudAiplatformV1FeatureGroup(typing_extensions.TypedDict, total=False):
    bigQuery: GoogleCloudAiplatformV1FeatureGroupBigQuery
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureGroupBigQuery(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudAiplatformV1BigQuerySource
    entityIdColumns: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureMonitoringStatsAnomaly(
    typing_extensions.TypedDict, total=False
):
    featureStatsAnomaly: GoogleCloudAiplatformV1FeatureStatsAnomaly
    objective: typing_extensions.Literal[
        "OBJECTIVE_UNSPECIFIED", "IMPORT_FEATURE_ANALYSIS", "SNAPSHOT_ANALYSIS"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureNoiseSigma(
    typing_extensions.TypedDict, total=False
):
    noiseSigma: _list[GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeature]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeature(
    typing_extensions.TypedDict, total=False
):
    name: str
    sigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStore(
    typing_extensions.TypedDict, total=False
):
    bigtable: GoogleCloudAiplatformV1FeatureOnlineStoreBigtable
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreBigtable(
    typing_extensions.TypedDict, total=False
):
    autoScaling: GoogleCloudAiplatformV1FeatureOnlineStoreBigtableAutoScaling

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreBigtableAutoScaling(
    typing_extensions.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureSelector(typing_extensions.TypedDict, total=False):
    idMatcher: GoogleCloudAiplatformV1IdMatcher

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureStatsAnomaly(
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
class GoogleCloudAiplatformV1FeatureValue(typing_extensions.TypedDict, total=False):
    boolArrayValue: GoogleCloudAiplatformV1BoolArray
    boolValue: bool
    bytesValue: str
    doubleArrayValue: GoogleCloudAiplatformV1DoubleArray
    doubleValue: float
    int64ArrayValue: GoogleCloudAiplatformV1Int64Array
    int64Value: str
    metadata: GoogleCloudAiplatformV1FeatureValueMetadata
    stringArrayValue: GoogleCloudAiplatformV1StringArray
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureValueDestination(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    csvDestination: GoogleCloudAiplatformV1CsvDestination
    tfrecordDestination: GoogleCloudAiplatformV1TFRecordDestination

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureValueList(typing_extensions.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1FeatureValue]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureValueMetadata(
    typing_extensions.TypedDict, total=False
):
    generateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureView(typing_extensions.TypedDict, total=False):
    bigQuerySource: GoogleCloudAiplatformV1FeatureViewBigQuerySource
    createTime: str
    etag: str
    featureRegistrySource: GoogleCloudAiplatformV1FeatureViewFeatureRegistrySource
    labels: dict[str, typing.Any]
    name: str
    syncConfig: GoogleCloudAiplatformV1FeatureViewSyncConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    entityIdColumns: _list[str]
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDataKey(
    typing_extensions.TypedDict, total=False
):
    compositeKey: GoogleCloudAiplatformV1FeatureViewDataKeyCompositeKey
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDataKeyCompositeKey(
    typing_extensions.TypedDict, total=False
):
    parts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewFeatureRegistrySource(
    typing_extensions.TypedDict, total=False
):
    featureGroups: _list[
        GoogleCloudAiplatformV1FeatureViewFeatureRegistrySourceFeatureGroup
    ]
    projectNumber: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewFeatureRegistrySourceFeatureGroup(
    typing_extensions.TypedDict, total=False
):
    featureGroupId: str
    featureIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSync(typing_extensions.TypedDict, total=False):
    createTime: str
    finalStatus: GoogleRpcStatus
    name: str
    runTime: GoogleTypeInterval
    syncSummary: GoogleCloudAiplatformV1FeatureViewSyncSyncSummary

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSyncConfig(
    typing_extensions.TypedDict, total=False
):
    cron: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSyncSyncSummary(
    typing_extensions.TypedDict, total=False
):
    rowSynced: str
    totalSlot: str

@typing.type_check_only
class GoogleCloudAiplatformV1Featurestore(typing_extensions.TypedDict, total=False):
    createTime: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    onlineServingConfig: GoogleCloudAiplatformV1FeaturestoreOnlineServingConfig
    onlineStorageTtlDays: int
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfig(
    typing_extensions.TypedDict, total=False
):
    categoricalThresholdConfig: GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfig
    importFeaturesAnalysis: GoogleCloudAiplatformV1FeaturestoreMonitoringConfigImportFeaturesAnalysis
    numericalThresholdConfig: GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfig
    snapshotAnalysis: GoogleCloudAiplatformV1FeaturestoreMonitoringConfigSnapshotAnalysis

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfigImportFeaturesAnalysis(
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
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfigSnapshotAnalysis(
    typing_extensions.TypedDict, total=False
):
    disabled: bool
    monitoringIntervalDays: int
    stalenessDays: int

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfig(
    typing_extensions.TypedDict, total=False
):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreOnlineServingConfig(
    typing_extensions.TypedDict, total=False
):
    fixedNodeCount: int
    scaling: GoogleCloudAiplatformV1FeaturestoreOnlineServingConfigScaling

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreOnlineServingConfigScaling(
    typing_extensions.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal[
        "FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED", "KEY_VALUE", "PROTO_STRUCT"
    ]
    dataKey: GoogleCloudAiplatformV1FeatureViewDataKey

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    keyValues: GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairList
    protoStruct: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairList(
    typing_extensions.TypedDict, total=False
):
    features: _list[
        GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: GoogleCloudAiplatformV1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1FileData(typing_extensions.TypedDict, total=False):
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1FilterSplit(typing_extensions.TypedDict, total=False):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    queries: _list[GoogleCloudAiplatformV1FindNeighborsRequestQuery]
    returnFullDatapoint: bool

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsRequestQuery(
    typing_extensions.TypedDict, total=False
):
    approximateNeighborCount: int
    datapoint: GoogleCloudAiplatformV1IndexDatapoint
    fractionLeafNodesToSearchOverride: float
    neighborCount: int
    perCrowdingAttributeNeighborCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponse(
    typing_extensions.TypedDict, total=False
):
    nearestNeighbors: _list[
        GoogleCloudAiplatformV1FindNeighborsResponseNearestNeighbors
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponseNearestNeighbors(
    typing_extensions.TypedDict, total=False
):
    id: str
    neighbors: _list[GoogleCloudAiplatformV1FindNeighborsResponseNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponseNeighbor(
    typing_extensions.TypedDict, total=False
):
    datapoint: GoogleCloudAiplatformV1IndexDatapoint
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1FractionSplit(typing_extensions.TypedDict, total=False):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionCall(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionDeclaration(
    typing_extensions.TypedDict, total=False
):
    description: str
    name: str
    parameters: GoogleCloudAiplatformV1Schema

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionResponse(typing_extensions.TypedDict, total=False):
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1GcsDestination(typing_extensions.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudAiplatformV1GcsSource(typing_extensions.TypedDict, total=False):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1Content]
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    safetySettings: _list[GoogleCloudAiplatformV1SafetySetting]
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponse(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1Candidate]
    promptFeedback: GoogleCloudAiplatformV1GenerateContentResponsePromptFeedback
    usageMetadata: GoogleCloudAiplatformV1GenerateContentResponseUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponsePromptFeedback(
    typing_extensions.TypedDict, total=False
):
    blockReason: typing_extensions.Literal[
        "BLOCKED_REASON_UNSPECIFIED", "SAFETY", "OTHER"
    ]
    blockReasonMessage: str
    safetyRatings: _list[GoogleCloudAiplatformV1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponseUsageMetadata(
    typing_extensions.TypedDict, total=False
):
    candidatesTokenCount: int
    promptTokenCount: int
    totalTokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfig(typing_extensions.TypedDict, total=False):
    candidateCount: int
    maxOutputTokens: int
    stopSequences: _list[str]
    temperature: float
    topK: float
    topP: float

@typing.type_check_only
class GoogleCloudAiplatformV1GenericOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    partialFailures: _list[GoogleRpcStatus]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1GenieSource(typing_extensions.TypedDict, total=False):
    baseModelUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingAttribution(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    segment: GoogleCloudAiplatformV1Segment
    web: GoogleCloudAiplatformV1GroundingAttributionWeb

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingAttributionWeb(
    typing_extensions.TypedDict, total=False
):
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingMetadata(
    typing_extensions.TypedDict, total=False
):
    groundingAttributions: _list[GoogleCloudAiplatformV1GroundingAttribution]
    webSearchQueries: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1HyperparameterTuningJob(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
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
    studySpec: GoogleCloudAiplatformV1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1CustomJobSpec
    trials: _list[GoogleCloudAiplatformV1Trial]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1IdMatcher(typing_extensions.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataConfig(typing_extensions.TypedDict, total=False):
    annotationLabels: dict[str, typing.Any]
    dataItemLabels: dict[str, typing.Any]
    gcsSource: GoogleCloudAiplatformV1GcsSource
    importSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataRequest(
    typing_extensions.TypedDict, total=False
):
    importConfigs: _list[GoogleCloudAiplatformV1ImportDataConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ImportFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    blockingOperationIds: _list[str]
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    sourceUris: _list[str]
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    avroSource: GoogleCloudAiplatformV1AvroSource
    bigquerySource: GoogleCloudAiplatformV1BigQuerySource
    csvSource: GoogleCloudAiplatformV1CsvSource
    disableIngestionAnalysis: bool
    disableOnlineServing: bool
    entityIdField: str
    featureSpecs: _list[GoogleCloudAiplatformV1ImportFeatureValuesRequestFeatureSpec]
    featureTime: str
    featureTimeField: str
    workerCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1ImportFeatureValuesRequestFeatureSpec(
    typing_extensions.TypedDict, total=False
):
    id: str
    sourceField: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportModelEvaluationRequest(
    typing_extensions.TypedDict, total=False
):
    modelEvaluation: GoogleCloudAiplatformV1ModelEvaluation

@typing.type_check_only
class GoogleCloudAiplatformV1Index(typing_extensions.TypedDict, total=False):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1DeployedIndexRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    indexStats: GoogleCloudAiplatformV1IndexStats
    indexUpdateMethod: typing_extensions.Literal[
        "INDEX_UPDATE_METHOD_UNSPECIFIED", "BATCH_UPDATE", "STREAM_UPDATE"
    ]
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataSchemaUri: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapoint(typing_extensions.TypedDict, total=False):
    crowdingTag: GoogleCloudAiplatformV1IndexDatapointCrowdingTag
    datapointId: str
    featureVector: _list[float]
    numericRestricts: _list[GoogleCloudAiplatformV1IndexDatapointNumericRestriction]
    restricts: _list[GoogleCloudAiplatformV1IndexDatapointRestriction]

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapointCrowdingTag(
    typing_extensions.TypedDict, total=False
):
    crowdingAttribute: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapointNumericRestriction(
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
        "NOT_EQUAL",
    ]
    valueDouble: float
    valueFloat: float
    valueInt: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapointRestriction(
    typing_extensions.TypedDict, total=False
):
    allowList: _list[str]
    denyList: _list[str]
    namespace: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexEndpoint(typing_extensions.TypedDict, total=False):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1DeployedIndex]
    description: str
    displayName: str
    enablePrivateServiceConnect: bool
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    privateServiceConnectConfig: GoogleCloudAiplatformV1PrivateServiceConnectConfig
    publicEndpointDomainName: str
    publicEndpointEnabled: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexPrivateEndpoints(
    typing_extensions.TypedDict, total=False
):
    matchGrpcAddress: str
    pscAutomatedEndpoints: _list[GoogleCloudAiplatformV1PscAutomatedEndpoints]
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexStats(typing_extensions.TypedDict, total=False):
    shardsCount: int
    vectorsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1InputDataConfig(typing_extensions.TypedDict, total=False):
    annotationSchemaUri: str
    annotationsFilter: str
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    datasetId: str
    filterSplit: GoogleCloudAiplatformV1FilterSplit
    fractionSplit: GoogleCloudAiplatformV1FractionSplit
    gcsDestination: GoogleCloudAiplatformV1GcsDestination
    persistMlUseAssignment: bool
    predefinedSplit: GoogleCloudAiplatformV1PredefinedSplit
    savedQueryId: str
    stratifiedSplit: GoogleCloudAiplatformV1StratifiedSplit
    timestampSplit: GoogleCloudAiplatformV1TimestampSplit

@typing.type_check_only
class GoogleCloudAiplatformV1Int64Array(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1IntegratedGradientsAttribution(
    typing_extensions.TypedDict, total=False
):
    blurBaselineConfig: GoogleCloudAiplatformV1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1SmoothGradConfig
    stepCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1LargeModelReference(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1LineageSubgraph(typing_extensions.TypedDict, total=False):
    artifacts: _list[GoogleCloudAiplatformV1Artifact]
    events: _list[GoogleCloudAiplatformV1Event]
    executions: _list[GoogleCloudAiplatformV1Execution]

@typing.type_check_only
class GoogleCloudAiplatformV1ListAnnotationsResponse(
    typing_extensions.TypedDict, total=False
):
    annotations: _list[GoogleCloudAiplatformV1Annotation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListArtifactsResponse(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1Artifact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListBatchPredictionJobsResponse(
    typing_extensions.TypedDict, total=False
):
    batchPredictionJobs: _list[GoogleCloudAiplatformV1BatchPredictionJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListContextsResponse(
    typing_extensions.TypedDict, total=False
):
    contexts: _list[GoogleCloudAiplatformV1Context]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListCustomJobsResponse(
    typing_extensions.TypedDict, total=False
):
    customJobs: _list[GoogleCloudAiplatformV1CustomJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataItemsResponse(
    typing_extensions.TypedDict, total=False
):
    dataItems: _list[GoogleCloudAiplatformV1DataItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataLabelingJobsResponse(
    typing_extensions.TypedDict, total=False
):
    dataLabelingJobs: _list[GoogleCloudAiplatformV1DataLabelingJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    datasetVersions: _list[GoogleCloudAiplatformV1DatasetVersion]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetsResponse(
    typing_extensions.TypedDict, total=False
):
    datasets: _list[GoogleCloudAiplatformV1Dataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse(
    typing_extensions.TypedDict, total=False
):
    deploymentResourcePools: _list[GoogleCloudAiplatformV1DeploymentResourcePool]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEndpointsResponse(
    typing_extensions.TypedDict, total=False
):
    endpoints: _list[GoogleCloudAiplatformV1Endpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudAiplatformV1EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    executions: _list[GoogleCloudAiplatformV1Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    featureGroups: _list[GoogleCloudAiplatformV1FeatureGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse(
    typing_extensions.TypedDict, total=False
):
    featureOnlineStores: _list[GoogleCloudAiplatformV1FeatureOnlineStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureViewSyncsResponse(
    typing_extensions.TypedDict, total=False
):
    featureViewSyncs: _list[GoogleCloudAiplatformV1FeatureViewSync]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureViewsResponse(
    typing_extensions.TypedDict, total=False
):
    featureViews: _list[GoogleCloudAiplatformV1FeatureView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturestoresResponse(
    typing_extensions.TypedDict, total=False
):
    featurestores: _list[GoogleCloudAiplatformV1Featurestore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse(
    typing_extensions.TypedDict, total=False
):
    hyperparameterTuningJobs: _list[GoogleCloudAiplatformV1HyperparameterTuningJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexEndpointsResponse(
    typing_extensions.TypedDict, total=False
):
    indexEndpoints: _list[GoogleCloudAiplatformV1IndexEndpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: _list[GoogleCloudAiplatformV1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataSchemasResponse(
    typing_extensions.TypedDict, total=False
):
    metadataSchemas: _list[GoogleCloudAiplatformV1MetadataSchema]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataStoresResponse(
    typing_extensions.TypedDict, total=False
):
    metadataStores: _list[GoogleCloudAiplatformV1MetadataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse(
    typing_extensions.TypedDict, total=False
):
    modelDeploymentMonitoringJobs: _list[
        GoogleCloudAiplatformV1ModelDeploymentMonitoringJob
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse(
    typing_extensions.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1ModelEvaluationSlice]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationsResponse(
    typing_extensions.TypedDict, total=False
):
    modelEvaluations: _list[GoogleCloudAiplatformV1ModelEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudAiplatformV1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudAiplatformV1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nasJobs: _list[GoogleCloudAiplatformV1NasJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasTrialDetailsResponse(
    typing_extensions.TypedDict, total=False
):
    nasTrialDetails: _list[GoogleCloudAiplatformV1NasTrialDetail]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimeTemplates: _list[GoogleCloudAiplatformV1NotebookRuntimeTemplate]

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimes: _list[GoogleCloudAiplatformV1NotebookRuntime]

@typing.type_check_only
class GoogleCloudAiplatformV1ListOptimalTrialsRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListOptimalTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    optimalTrials: _list[GoogleCloudAiplatformV1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1ListPipelineJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pipelineJobs: _list[GoogleCloudAiplatformV1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSavedQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    savedQueries: _list[GoogleCloudAiplatformV1SavedQuery]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSchedulesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    schedules: _list[GoogleCloudAiplatformV1Schedule]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSpecialistPoolsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    specialistPools: _list[GoogleCloudAiplatformV1SpecialistPool]

@typing.type_check_only
class GoogleCloudAiplatformV1ListStudiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    studies: _list[GoogleCloudAiplatformV1Study]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardExperimentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardExperiments: _list[GoogleCloudAiplatformV1TensorboardExperiment]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardRunsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardRuns: _list[GoogleCloudAiplatformV1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboards: _list[GoogleCloudAiplatformV1Tensorboard]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrainingPipelinesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    trainingPipelines: _list[GoogleCloudAiplatformV1TrainingPipeline]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    trials: _list[GoogleCloudAiplatformV1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1LookupStudyRequest(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MachineSpec(typing_extensions.TypedDict, total=False):
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
    ]
    machineType: str
    tpuTopology: str

@typing.type_check_only
class GoogleCloudAiplatformV1ManualBatchTuningParameters(
    typing_extensions.TypedDict, total=False
):
    batchSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1Measurement(typing_extensions.TypedDict, total=False):
    elapsedDuration: str
    metrics: _list[GoogleCloudAiplatformV1MeasurementMetric]
    stepCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1MeasurementMetric(
    typing_extensions.TypedDict, total=False
):
    metricId: str
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1MergeVersionAliasesRequest(
    typing_extensions.TypedDict, total=False
):
    versionAliases: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataSchema(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAiplatformV1MetadataStore(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    name: str
    state: GoogleCloudAiplatformV1MetadataStoreMetadataStoreState
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStoreMetadataStoreState(
    typing_extensions.TypedDict, total=False
):
    diskUtilizationBytes: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResource(
    typing_extensions.TypedDict, total=False
):
    automlDataset: GoogleCloudAiplatformV1MigratableResourceAutomlDataset
    automlModel: GoogleCloudAiplatformV1MigratableResourceAutomlModel
    dataLabelingDataset: GoogleCloudAiplatformV1MigratableResourceDataLabelingDataset
    lastMigrateTime: str
    lastUpdateTime: str
    mlEngineModelVersion: GoogleCloudAiplatformV1MigratableResourceMlEngineModelVersion

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceAutomlDataset(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceAutomlModel(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceDataLabelingDataset(
    typing_extensions.TypedDict, total=False
):
    dataLabelingAnnotatedDatasets: _list[
        GoogleCloudAiplatformV1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset
    ]
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    annotatedDatasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceMlEngineModelVersion(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequest(
    typing_extensions.TypedDict, total=False
):
    migrateAutomlDatasetConfig: GoogleCloudAiplatformV1MigrateResourceRequestMigrateAutomlDatasetConfig
    migrateAutomlModelConfig: GoogleCloudAiplatformV1MigrateResourceRequestMigrateAutomlModelConfig
    migrateDataLabelingDatasetConfig: GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfig
    migrateMlEngineModelVersionConfig: GoogleCloudAiplatformV1MigrateResourceRequestMigrateMlEngineModelVersionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateAutomlDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateAutomlModelConfig(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str
    migrateDataLabelingAnnotatedDatasetConfigs: _list[
        GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateMlEngineModelVersionConfig(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    modelDisplayName: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceResponse(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    migratableResource: GoogleCloudAiplatformV1MigratableResource
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1Model(typing_extensions.TypedDict, total=False):
    artifactUri: str
    baseModelSource: GoogleCloudAiplatformV1ModelBaseModelSource
    containerSpec: GoogleCloudAiplatformV1ModelContainerSpec
    createTime: str
    dataStats: GoogleCloudAiplatformV1ModelDataStats
    deployedModels: _list[GoogleCloudAiplatformV1DeployedModelRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    explanationSpec: GoogleCloudAiplatformV1ExplanationSpec
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataArtifact: str
    metadataSchemaUri: str
    modelSourceInfo: GoogleCloudAiplatformV1ModelSourceInfo
    name: str
    originalModelInfo: GoogleCloudAiplatformV1ModelOriginalModelInfo
    pipelineJob: str
    predictSchemata: GoogleCloudAiplatformV1PredictSchemata
    supportedDeploymentResourcesTypes: _list[
        typing_extensions.Literal[
            "DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED",
            "DEDICATED_RESOURCES",
            "AUTOMATIC_RESOURCES",
            "SHARED_RESOURCES",
        ]
    ]
    supportedExportFormats: _list[GoogleCloudAiplatformV1ModelExportFormat]
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
class GoogleCloudAiplatformV1ModelBaseModelSource(
    typing_extensions.TypedDict, total=False
):
    genieSource: GoogleCloudAiplatformV1GenieSource
    modelGardenSource: GoogleCloudAiplatformV1ModelGardenSource

@typing.type_check_only
class GoogleCloudAiplatformV1ModelContainerSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    command: _list[str]
    deploymentTimeout: str
    env: _list[GoogleCloudAiplatformV1EnvVar]
    grpcPorts: _list[GoogleCloudAiplatformV1Port]
    healthProbe: GoogleCloudAiplatformV1Probe
    healthRoute: str
    imageUri: str
    ports: _list[GoogleCloudAiplatformV1Port]
    predictRoute: str
    sharedMemorySizeMb: str
    startupProbe: GoogleCloudAiplatformV1Probe

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDataStats(typing_extensions.TypedDict, total=False):
    testAnnotationsCount: str
    testDataItemsCount: str
    trainingAnnotationsCount: str
    trainingDataItemsCount: str
    validationAnnotationsCount: str
    validationDataItemsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringBigQueryTable(
    typing_extensions.TypedDict, total=False
):
    bigqueryTablePath: str
    logSource: typing_extensions.Literal[
        "LOG_SOURCE_UNSPECIFIED", "TRAINING", "SERVING"
    ]
    logType: typing_extensions.Literal["LOG_TYPE_UNSPECIFIED", "PREDICT", "EXPLAIN"]
    requestResponseLoggingSchemaVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringJob(
    typing_extensions.TypedDict, total=False
):
    analysisInstanceSchemaUri: str
    bigqueryTables: _list[GoogleCloudAiplatformV1ModelDeploymentMonitoringBigQueryTable]
    createTime: str
    displayName: str
    enableMonitoringPipelineLogs: bool
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endpoint: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    latestMonitoringPipelineMetadata: GoogleCloudAiplatformV1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata
    logTtl: str
    loggingSamplingStrategy: GoogleCloudAiplatformV1SamplingStrategy
    modelDeploymentMonitoringObjectiveConfigs: _list[
        GoogleCloudAiplatformV1ModelDeploymentMonitoringObjectiveConfig
    ]
    modelDeploymentMonitoringScheduleConfig: GoogleCloudAiplatformV1ModelDeploymentMonitoringScheduleConfig
    modelMonitoringAlertConfig: GoogleCloudAiplatformV1ModelMonitoringAlertConfig
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
    statsAnomaliesBaseDirectory: GoogleCloudAiplatformV1GcsDestination
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata(
    typing_extensions.TypedDict, total=False
):
    runTime: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    objectiveConfig: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringScheduleConfig(
    typing_extensions.TypedDict, total=False
):
    monitorInterval: str
    monitorWindow: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluation(typing_extensions.TypedDict, total=False):
    annotationSchemaUri: str
    createTime: str
    dataItemSchemaUri: str
    displayName: str
    explanationSpecs: _list[
        GoogleCloudAiplatformV1ModelEvaluationModelEvaluationExplanationSpec
    ]
    metadata: typing.Any
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1ModelExplanation
    name: str
    sliceDimensions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationModelEvaluationExplanationSpec(
    typing_extensions.TypedDict, total=False
):
    explanationSpec: GoogleCloudAiplatformV1ExplanationSpec
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSlice(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1ModelExplanation
    name: str
    slice: GoogleCloudAiplatformV1ModelEvaluationSliceSlice

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSlice(
    typing_extensions.TypedDict, total=False
):
    dimension: str
    sliceSpec: GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpec
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpec(
    typing_extensions.TypedDict, total=False
):
    configs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecRange(
    typing_extensions.TypedDict, total=False
):
    high: float
    low: float

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecSliceConfig(
    typing_extensions.TypedDict, total=False
):
    allValues: bool
    range: GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecRange
    value: GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecValue

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecValue(
    typing_extensions.TypedDict, total=False
):
    floatValue: float
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelExplanation(typing_extensions.TypedDict, total=False):
    meanAttributions: _list[GoogleCloudAiplatformV1Attribution]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelExportFormat(
    typing_extensions.TypedDict, total=False
):
    exportableContents: _list[
        typing_extensions.Literal["EXPORTABLE_CONTENT_UNSPECIFIED", "ARTIFACT", "IMAGE"]
    ]
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelGardenSource(
    typing_extensions.TypedDict, total=False
):
    publicModelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringAlertConfig(
    typing_extensions.TypedDict, total=False
):
    emailAlertConfig: GoogleCloudAiplatformV1ModelMonitoringAlertConfigEmailAlertConfig
    enableLogging: bool
    notificationChannels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringAlertConfigEmailAlertConfig(
    typing_extensions.TypedDict, total=False
):
    userEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    explanationConfig: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfig
    predictionDriftDetectionConfig: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig
    trainingDataset: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingDataset
    trainingPredictionSkewDetectionConfig: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfig(
    typing_extensions.TypedDict, total=False
):
    enableFeatureAttributes: bool
    explanationBaseline: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline(
    typing_extensions.TypedDict, total=False
):
    bigquery: GoogleCloudAiplatformV1BigQueryDestination
    gcs: GoogleCloudAiplatformV1GcsDestination
    predictionFormat: typing_extensions.Literal[
        "PREDICTION_FORMAT_UNSPECIFIED", "JSONL", "BIGQUERY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    attributionScoreDriftThresholds: dict[str, typing.Any]
    defaultDriftThreshold: GoogleCloudAiplatformV1ThresholdConfig
    driftThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingDataset(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1BigQuerySource
    dataFormat: str
    dataset: str
    gcsSource: GoogleCloudAiplatformV1GcsSource
    loggingSamplingStrategy: GoogleCloudAiplatformV1SamplingStrategy
    targetField: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    attributionScoreSkewThresholds: dict[str, typing.Any]
    defaultSkewThreshold: GoogleCloudAiplatformV1ThresholdConfig
    skewThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringStatsAnomalies(
    typing_extensions.TypedDict, total=False
):
    anomalyCount: int
    deployedModelId: str
    featureStats: _list[
        GoogleCloudAiplatformV1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies
    ]
    objective: typing_extensions.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies(
    typing_extensions.TypedDict, total=False
):
    featureDisplayName: str
    predictionStats: _list[GoogleCloudAiplatformV1FeatureStatsAnomaly]
    threshold: GoogleCloudAiplatformV1ThresholdConfig
    trainingStats: GoogleCloudAiplatformV1FeatureStatsAnomaly

@typing.type_check_only
class GoogleCloudAiplatformV1ModelOriginalModelInfo(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelSourceInfo(typing_extensions.TypedDict, total=False):
    copy: bool
    sourceType: typing_extensions.Literal[
        "MODEL_SOURCE_TYPE_UNSPECIFIED",
        "AUTOML",
        "CUSTOM",
        "BQML",
        "MODEL_GARDEN",
        "GENIE",
        "CUSTOM_TEXT_EMBEDDING",
        "MARKETPLACE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedIndexResponse(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1DeployedModel
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedModelResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1NasJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    enableRestrictedImageTraining: bool
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    nasJobOutput: GoogleCloudAiplatformV1NasJobOutput
    nasJobSpec: GoogleCloudAiplatformV1NasJobSpec
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
class GoogleCloudAiplatformV1NasJobOutput(typing_extensions.TypedDict, total=False):
    multiTrialJobOutput: GoogleCloudAiplatformV1NasJobOutputMultiTrialJobOutput

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobOutputMultiTrialJobOutput(
    typing_extensions.TypedDict, total=False
):
    searchTrials: _list[GoogleCloudAiplatformV1NasTrial]
    trainTrials: _list[GoogleCloudAiplatformV1NasTrial]

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpec(typing_extensions.TypedDict, total=False):
    multiTrialAlgorithmSpec: GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpec
    resumeNasJobId: str
    searchSpaceSpec: str

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpec(
    typing_extensions.TypedDict, total=False
):
    metric: GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecMetricSpec
    multiTrialAlgorithm: typing_extensions.Literal[
        "MULTI_TRIAL_ALGORITHM_UNSPECIFIED", "REINFORCEMENT_LEARNING", "GRID_SEARCH"
    ]
    searchTrialSpec: GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec
    trainTrialSpec: GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecMetricSpec(
    typing_extensions.TypedDict, total=False
):
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec(
    typing_extensions.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxParallelTrialCount: int
    maxTrialCount: int
    searchTrialJobSpec: GoogleCloudAiplatformV1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec(
    typing_extensions.TypedDict, total=False
):
    frequency: int
    maxParallelTrialCount: int
    trainTrialJobSpec: GoogleCloudAiplatformV1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1NasTrial(typing_extensions.TypedDict, total=False):
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1Measurement
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
class GoogleCloudAiplatformV1NasTrialDetail(typing_extensions.TypedDict, total=False):
    name: str
    parameters: str
    searchTrial: GoogleCloudAiplatformV1NasTrial
    trainTrial: GoogleCloudAiplatformV1NasTrial

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQuery(
    typing_extensions.TypedDict, total=False
):
    embedding: GoogleCloudAiplatformV1NearestNeighborQueryEmbedding
    entityId: str
    neighborCount: int
    parameters: GoogleCloudAiplatformV1NearestNeighborQueryParameters
    perCrowdingAttributeNeighborCount: int
    stringFilters: _list[GoogleCloudAiplatformV1NearestNeighborQueryStringFilter]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryEmbedding(
    typing_extensions.TypedDict, total=False
):
    value: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryParameters(
    typing_extensions.TypedDict, total=False
):
    approximateNeighborCandidates: int
    leafNodesSearchFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryStringFilter(
    typing_extensions.TypedDict, total=False
):
    allowTokens: _list[str]
    denyTokens: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    contentValidationStats: _list[
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataContentValidationStats
    ]
    dataBytesCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataContentValidationStats(
    typing_extensions.TypedDict, total=False
):
    invalidRecordCount: str
    partialErrors: _list[
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataRecordError
    ]
    sourceGcsUri: str
    validRecordCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataRecordError(
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
        "INVALID_ENCODING",
    ]
    rawRecord: str
    sourceGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighbors(typing_extensions.TypedDict, total=False):
    neighbors: _list[GoogleCloudAiplatformV1NearestNeighborsNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborsNeighbor(
    typing_extensions.TypedDict, total=False
):
    distance: float
    entityId: str
    entityKeyValues: GoogleCloudAiplatformV1FetchFeatureValuesResponse

@typing.type_check_only
class GoogleCloudAiplatformV1Neighbor(typing_extensions.TypedDict, total=False):
    neighborDistance: float
    neighborId: str

@typing.type_check_only
class GoogleCloudAiplatformV1NetworkSpec(typing_extensions.TypedDict, total=False):
    enableInternetAccess: bool
    network: str
    subnetwork: str

@typing.type_check_only
class GoogleCloudAiplatformV1NfsMount(typing_extensions.TypedDict, total=False):
    mountPoint: str
    path: str
    server: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookEucConfig(
    typing_extensions.TypedDict, total=False
):
    bypassActasCheck: bool
    eucDisabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookIdleShutdownConfig(
    typing_extensions.TypedDict, total=False
):
    idleShutdownDisabled: bool
    idleTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookReservationAffinity(
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
class GoogleCloudAiplatformV1NotebookRuntime(typing_extensions.TypedDict, total=False):
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
    notebookRuntimeTemplateRef: GoogleCloudAiplatformV1NotebookRuntimeTemplateRef
    notebookRuntimeType: typing_extensions.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    proxyUri: str
    reservationAffinity: GoogleCloudAiplatformV1NotebookReservationAffinity
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
class GoogleCloudAiplatformV1NotebookRuntimeTemplate(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataPersistentDiskSpec: GoogleCloudAiplatformV1PersistentDiskSpec
    description: str
    displayName: str
    etag: str
    eucConfig: GoogleCloudAiplatformV1NotebookEucConfig
    idleShutdownConfig: GoogleCloudAiplatformV1NotebookIdleShutdownConfig
    isDefault: bool
    labels: dict[str, typing.Any]
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    name: str
    networkSpec: GoogleCloudAiplatformV1NetworkSpec
    networkTags: _list[str]
    notebookRuntimeType: typing_extensions.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    reservationAffinity: GoogleCloudAiplatformV1NotebookReservationAffinity
    serviceAccount: str
    shieldedVmConfig: GoogleCloudAiplatformV1ShieldedVmConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeTemplateRef(
    typing_extensions.TypedDict, total=False
):
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1Part(typing_extensions.TypedDict, total=False):
    fileData: GoogleCloudAiplatformV1FileData
    functionCall: GoogleCloudAiplatformV1FunctionCall
    functionResponse: GoogleCloudAiplatformV1FunctionResponse
    inlineData: GoogleCloudAiplatformV1Blob
    text: str
    videoMetadata: GoogleCloudAiplatformV1VideoMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PauseModelDeploymentMonitoringJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1PauseScheduleRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1PersistentDiskSpec(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: str
    diskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobDetail: GoogleCloudAiplatformV1PipelineJobDetail
    labels: dict[str, typing.Any]
    name: str
    network: str
    pipelineSpec: dict[str, typing.Any]
    reservedIpRanges: _list[str]
    runtimeConfig: GoogleCloudAiplatformV1PipelineJobRuntimeConfig
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
    templateMetadata: GoogleCloudAiplatformV1PipelineTemplateMetadata
    templateUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineJobDetail(
    typing_extensions.TypedDict, total=False
):
    pipelineContext: GoogleCloudAiplatformV1Context
    pipelineRunContext: GoogleCloudAiplatformV1Context
    taskDetails: _list[GoogleCloudAiplatformV1PipelineTaskDetail]

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineJobRuntimeConfig(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudAiplatformV1PipelineJobRuntimeConfigInputArtifact(
    typing_extensions.TypedDict, total=False
):
    artifactId: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskDetail(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    execution: GoogleCloudAiplatformV1Execution
    executorDetail: GoogleCloudAiplatformV1PipelineTaskExecutorDetail
    inputs: dict[str, typing.Any]
    outputs: dict[str, typing.Any]
    parentTaskId: str
    pipelineTaskStatus: _list[
        GoogleCloudAiplatformV1PipelineTaskDetailPipelineTaskStatus
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
class GoogleCloudAiplatformV1PipelineTaskDetailArtifactList(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1Artifact]

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskDetailPipelineTaskStatus(
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
class GoogleCloudAiplatformV1PipelineTaskExecutorDetail(
    typing_extensions.TypedDict, total=False
):
    containerDetail: GoogleCloudAiplatformV1PipelineTaskExecutorDetailContainerDetail
    customJobDetail: GoogleCloudAiplatformV1PipelineTaskExecutorDetailCustomJobDetail

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskExecutorDetailContainerDetail(
    typing_extensions.TypedDict, total=False
):
    failedMainJobs: _list[str]
    failedPreCachingCheckJobs: _list[str]
    mainJob: str
    preCachingCheckJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskExecutorDetailCustomJobDetail(
    typing_extensions.TypedDict, total=False
):
    failedJobs: _list[str]
    job: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTemplateMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1Port(typing_extensions.TypedDict, total=False):
    containerPort: int

@typing.type_check_only
class GoogleCloudAiplatformV1PredefinedSplit(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1PredictRequest(typing_extensions.TypedDict, total=False):
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1PredictRequestResponseLoggingConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    enabled: bool
    samplingRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1PredictResponse(typing_extensions.TypedDict, total=False):
    deployedModelId: str
    metadata: typing.Any
    model: str
    modelDisplayName: str
    modelVersionId: str
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1PredictSchemata(typing_extensions.TypedDict, total=False):
    instanceSchemaUri: str
    parametersSchemaUri: str
    predictionSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1Presets(typing_extensions.TypedDict, total=False):
    modality: typing_extensions.Literal[
        "MODALITY_UNSPECIFIED", "IMAGE", "TEXT", "TABULAR"
    ]
    query: typing_extensions.Literal["PRECISE", "FAST"]

@typing.type_check_only
class GoogleCloudAiplatformV1PrivateEndpoints(typing_extensions.TypedDict, total=False):
    explainHttpUri: str
    healthHttpUri: str
    predictHttpUri: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1PrivateServiceConnectConfig(
    typing_extensions.TypedDict, total=False
):
    enablePrivateServiceConnect: bool
    projectAllowlist: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1Probe(typing_extensions.TypedDict, total=False):
    exec: GoogleCloudAiplatformV1ProbeExecAction
    periodSeconds: int
    timeoutSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeExecAction(typing_extensions.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PscAutomatedEndpoints(
    typing_extensions.TypedDict, total=False
):
    matchAddress: str
    network: str
    projectId: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModel(typing_extensions.TypedDict, total=False):
    frameworks: _list[str]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "DOGFOOD",
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
    predictSchemata: GoogleCloudAiplatformV1PredictSchemata
    publisherModelTemplate: str
    supportedActions: GoogleCloudAiplatformV1PublisherModelCallToAction
    versionId: str
    versionState: typing_extensions.Literal[
        "VERSION_STATE_UNSPECIFIED", "VERSION_STATE_STABLE", "VERSION_STATE_UNSTABLE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToAction(
    typing_extensions.TypedDict, total=False
):
    createApplication: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    deploy: GoogleCloudAiplatformV1PublisherModelCallToActionDeploy
    deployGke: GoogleCloudAiplatformV1PublisherModelCallToActionDeployGke
    openEvaluationPipeline: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    openFineTuningPipeline: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    openFineTuningPipelines: GoogleCloudAiplatformV1PublisherModelCallToActionOpenFineTuningPipelines
    openGenerationAiStudio: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    openGenie: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    openNotebook: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    openNotebooks: GoogleCloudAiplatformV1PublisherModelCallToActionOpenNotebooks
    openPromptTuningPipeline: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    requestAccess: GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    viewRestApi: GoogleCloudAiplatformV1PublisherModelCallToActionViewRestApi

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeploy(
    typing_extensions.TypedDict, total=False
):
    artifactUri: str
    automaticResources: GoogleCloudAiplatformV1AutomaticResources
    containerSpec: GoogleCloudAiplatformV1ModelContainerSpec
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    largeModelReference: GoogleCloudAiplatformV1LargeModelReference
    modelDisplayName: str
    publicArtifactUri: str
    sharedResources: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeployGke(
    typing_extensions.TypedDict, total=False
):
    gkeYamlConfigs: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionOpenFineTuningPipelines(
    typing_extensions.TypedDict, total=False
):
    fineTuningPipelines: _list[
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionOpenNotebooks(
    typing_extensions.TypedDict, total=False
):
    notebooks: _list[
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences(
    typing_extensions.TypedDict, total=False
):
    references: dict[str, typing.Any]
    resourceDescription: str
    resourceTitle: str
    resourceUseCase: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionViewRestApi(
    typing_extensions.TypedDict, total=False
):
    documentations: _list[GoogleCloudAiplatformV1PublisherModelDocumentation]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelDocumentation(
    typing_extensions.TypedDict, total=False
):
    content: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelResourceReference(
    typing_extensions.TypedDict, total=False
):
    description: str
    resourceName: str
    uri: str
    useCase: str

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeArtifactsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeArtifactsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeArtifactsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeContextsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeContextsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeContextsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeExecutionsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeExecutionsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PythonPackageSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    env: _list[GoogleCloudAiplatformV1EnvVar]
    executorImageUri: str
    packageUris: _list[str]
    pythonModule: str

@typing.type_check_only
class GoogleCloudAiplatformV1QueryDeployedModelsResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModelRefs: _list[GoogleCloudAiplatformV1DeployedModelRef]
    deployedModels: _list[GoogleCloudAiplatformV1DeployedModel]
    nextPageToken: str
    totalDeployedModelCount: int
    totalEndpointCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1RawPredictRequest(
    typing_extensions.TypedDict, total=False
):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    featureSelector: GoogleCloudAiplatformV1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    entityView: GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityView
    header: GoogleCloudAiplatformV1ReadFeatureValuesResponseHeader

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityView(
    typing_extensions.TypedDict, total=False
):
    data: _list[GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityViewData]
    entityId: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityViewData(
    typing_extensions.TypedDict, total=False
):
    value: GoogleCloudAiplatformV1FeatureValue
    values: GoogleCloudAiplatformV1FeatureValueList

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseFeatureDescriptor(
    typing_extensions.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseHeader(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    featureDescriptors: _list[
        GoogleCloudAiplatformV1ReadFeatureValuesResponseFeatureDescriptor
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadIndexDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadIndexDatapointsResponse(
    typing_extensions.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1IndexDatapoint]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse(
    typing_extensions.TypedDict, total=False
):
    blobs: _list[GoogleCloudAiplatformV1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardSizeResponse(
    typing_extensions.TypedDict, total=False
):
    storageSizeByte: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    timeSeriesData: GoogleCloudAiplatformV1TimeSeriesData

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponse(
    typing_extensions.TypedDict, total=False
):
    monthlyUsageData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponsePerMonthUsageData(
    typing_extensions.TypedDict, total=False
):
    userUsageData: _list[
        GoogleCloudAiplatformV1ReadTensorboardUsageResponsePerUserUsageData
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponsePerUserUsageData(
    typing_extensions.TypedDict, total=False
):
    username: str
    viewCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveContextChildrenRequest(
    typing_extensions.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveContextChildrenResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    datapointIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveDatapointsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ResourcesConsumed(
    typing_extensions.TypedDict, total=False
):
    replicaHours: float

@typing.type_check_only
class GoogleCloudAiplatformV1RestoreDatasetVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ResumeModelDeploymentMonitoringJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ResumeScheduleRequest(
    typing_extensions.TypedDict, total=False
):
    catchUp: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyRating(typing_extensions.TypedDict, total=False):
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
    probabilityScore: float
    severity: typing_extensions.Literal[
        "HARM_SEVERITY_UNSPECIFIED",
        "HARM_SEVERITY_NEGLIGIBLE",
        "HARM_SEVERITY_LOW",
        "HARM_SEVERITY_MEDIUM",
        "HARM_SEVERITY_HIGH",
    ]
    severityScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1SafetySetting(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAiplatformV1SampleConfig(typing_extensions.TypedDict, total=False):
    followingBatchSamplePercentage: int
    initialBatchSamplePercentage: int
    sampleStrategy: typing_extensions.Literal[
        "SAMPLE_STRATEGY_UNSPECIFIED", "UNCERTAINTY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SampledShapleyAttribution(
    typing_extensions.TypedDict, total=False
):
    pathCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SamplingStrategy(typing_extensions.TypedDict, total=False):
    randomSampleConfig: GoogleCloudAiplatformV1SamplingStrategyRandomSampleConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SamplingStrategyRandomSampleConfig(
    typing_extensions.TypedDict, total=False
):
    sampleRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1SavedQuery(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAiplatformV1Scalar(typing_extensions.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1Schedule(typing_extensions.TypedDict, total=False):
    allowQueueing: bool
    catchUp: bool
    createPipelineJobRequest: GoogleCloudAiplatformV1CreatePipelineJobRequest
    createTime: str
    cron: str
    displayName: str
    endTime: str
    lastPauseTime: str
    lastResumeTime: str
    lastScheduledRunResponse: GoogleCloudAiplatformV1ScheduleRunResponse
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
class GoogleCloudAiplatformV1ScheduleRunResponse(
    typing_extensions.TypedDict, total=False
):
    runResponse: str
    scheduledRunTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1Scheduling(typing_extensions.TypedDict, total=False):
    disableRetries: bool
    restartJobOnWorkerRestart: bool
    timeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1Schema(typing_extensions.TypedDict, total=False):
    description: str
    enum: _list[str]
    example: typing.Any
    format: str
    items: GoogleCloudAiplatformV1Schema
    nullable: bool
    properties: dict[str, typing.Any]
    required: _list[str]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STRING", "NUMBER", "INTEGER", "BOOLEAN", "ARRAY", "OBJECT"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaAnnotationSpecColor(
    typing_extensions.TypedDict, total=False
):
    color: GoogleTypeColor
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageBoundingBoxAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageSegmentationAnnotation(
    typing_extensions.TypedDict, total=False
):
    maskAnnotation: GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationMaskAnnotation
    polygonAnnotation: GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolygonAnnotation
    polylineAnnotation: GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolylineAnnotation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationMaskAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecColors: _list[GoogleCloudAiplatformV1SchemaAnnotationSpecColor]
    maskGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolygonAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolylineAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsClassificationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    auPrc: float
    auRoc: float
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix
    logLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix
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
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix(
    typing_extensions.TypedDict, total=False
):
    annotationSpecs: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef
    ]
    rows: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    quantileMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry
    ]
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float
    rootMeanSquaredPercentageError: float
    weightedAbsolutePercentageError: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    observedQuantile: float
    quantile: float
    scaledPinballLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsGeneralTextGenerationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    bleu: float
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageObjectDetectionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageSegmentationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetricsEntries: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix
    diceScoreCoefficient: float
    iouScore: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsQuestionAnsweringEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    exactMatch: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsRegressionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsSummarizationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextExtractionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextSentimentEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confusionMatrix: GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix
    f1Score: float
    linearKappa: float
    meanAbsoluteError: float
    meanSquaredError: float
    precision: float
    quadraticKappa: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTrackMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanBoundingBoxIou: float
    meanMismatchRate: float
    meanTrackingAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxIou: float
    confidenceThreshold: float
    mismatchRate: float
    trackingPrecision: float
    trackingRecall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics
    ]
    meanAveragePrecision: float
    precisionWindowLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionRecognitionMetrics(
    typing_extensions.TypedDict, total=False
):
    evaluatedActionCount: int
    videoActionMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetrics
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoObjectTrackingMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int
    evaluatedFrameCount: int
    evaluatedTrackCount: int
    trackMeanAveragePrecision: float
    trackMeanBoundingBoxIou: float
    trackMeanMismatchRate: float
    trackMetrics: _list[GoogleCloudAiplatformV1SchemaModelevaluationMetricsTrackMetrics]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceImageClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceImageObjectDetectionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceImageSegmentationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceTextClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceTextExtractionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    key: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceTextSentimentPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceVideoActionRecognitionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceVideoClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceVideoObjectTrackingPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfig(
    typing_extensions.TypedDict, total=False
):
    disableAttribution: bool
    sources: _list[GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfigSourceEntry]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfigSourceEntry(
    typing_extensions.TypedDict, total=False
):
    enterpriseDatastore: str
    inlineContext: str
    type: typing_extensions.Literal[
        "UNSPECIFIED", "WEB", "ENTERPRISE", "VERTEX_AI_SEARCH", "INLINE"
    ]
    vertexAiSearchDatastore: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsImageClassificationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsImageObjectDetectionPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsImageSegmentationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsVideoActionRecognitionPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsVideoClassificationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    oneSecIntervalClassification: bool
    segmentClassification: bool
    shotClassification: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsVideoObjectTrackingPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    minBoundingBoxSize: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionImageObjectDetectionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    bboxes: _list[_list[typing.Any]]
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionImageSegmentationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    categoryMask: str
    confidenceMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTabularClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    classes: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTabularRegressionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    lowerBound: float
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    upperBound: float
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTextExtractionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]
    textSegmentEndOffsets: _list[str]
    textSegmentStartOffsets: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTextSentimentPredictionResult(
    typing_extensions.TypedDict, total=False
):
    sentiment: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTftFeatureImportance(
    typing_extensions.TypedDict, total=False
):
    attributeColumns: _list[str]
    attributeWeights: _list[float]
    contextColumns: _list[str]
    contextWeights: _list[float]
    horizonColumns: _list[str]
    horizonWeights: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTimeSeriesForecastingPredictionResult(
    typing_extensions.TypedDict, total=False
):
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    tftFeatureImportance: GoogleCloudAiplatformV1SchemaPredictPredictionTftFeatureImportance
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionVideoActionRecognitionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionVideoClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionVideoObjectTrackingPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    frames: _list[
        GoogleCloudAiplatformV1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame
    ]
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictionResult(
    typing_extensions.TypedDict, total=False
):
    error: GoogleCloudAiplatformV1SchemaPredictionResultError
    instance: dict[str, typing.Any]
    key: str
    prediction: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictionResultError(
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
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1SchemaTablesDatasetMetadataInputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadataBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadataGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1SchemaTablesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1SchemaTablesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextExtractionAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    textSegment: GoogleCloudAiplatformV1SchemaTextSegment

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextPromptDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    candidateCount: str
    gcsUri: str
    groundingConfig: GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfig
    maxOutputTokens: str
    note: str
    promptType: str
    stopSequences: _list[str]
    temperature: float
    text: str
    topK: str
    topP: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextSegment(
    typing_extensions.TypedDict, total=False
):
    content: str
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextSentimentAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    sentiment: int
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextSentimentSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataInputConfig
    timeColumn: str
    timeSeriesIdentifierColumn: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity
    enableProbabilisticInference: bool
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs(
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
    tunableParameter: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetection(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs(
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
    tunableParameter: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentation(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs(
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
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTables(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    disableEarlyStopping: bool
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    optimizationObjective: str
    optimizationObjectivePrecisionValue: float
    optimizationObjectiveRecallValue: float
    predictionType: str
    targetColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation
    ]
    weightColumnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation
    repeatedCategorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation
    repeatedNumeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation
    repeatedText: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation
    text: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextExtraction(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextSentiment(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs(
    typing_extensions.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoActionRecognition(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs(
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
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoObjectTracking(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs(
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
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter(
    typing_extensions.TypedDict, total=False
):
    checkpointName: str
    datasetConfig: dict[str, typing.Any]
    studySpec: GoogleCloudAiplatformV1StudySpec
    trainerConfig: dict[str, typing.Any]
    trainerType: typing_extensions.Literal[
        "TRAINER_TYPE_UNSPECIFIED", "AUTOML_TRAINER", "MODEL_GARDEN_TRAINER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionCustomJobMetadata(
    typing_extensions.TypedDict, total=False
):
    backingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionCustomTask(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1CustomJobSpec
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionCustomJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig(
    typing_extensions.TypedDict, total=False
):
    destinationBigqueryUri: str
    overrideExistingTable: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHierarchyConfig(
    typing_extensions.TypedDict, total=False
):
    groupColumns: _list[str]
    groupTemporalTotalWeight: float
    groupTotalWeight: float
    temporalTotalWeight: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata(
    typing_extensions.TypedDict, total=False
):
    backingHyperparameterTuningJob: str
    bestTrialBackingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec(
    typing_extensions.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxTrialCount: int
    parallelTrialCount: int
    studySpec: GoogleCloudAiplatformV1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningTask(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionWindowConfig(
    typing_extensions.TypedDict, total=False
):
    column: str
    maxCount: str
    strideLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVertex(typing_extensions.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoActionRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoObjectTrackingAnnotation(
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
class GoogleCloudAiplatformV1SchemaVisualInspectionClassificationLabelSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVisualInspectionMaskSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchDataItemsResponse(
    typing_extensions.TypedDict, total=False
):
    dataItemViews: _list[GoogleCloudAiplatformV1DataItemView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchMigratableResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchMigratableResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    migratableResources: _list[GoogleCloudAiplatformV1MigratableResource]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    endTime: str
    featureDisplayName: str
    objectives: _list[
        GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective
    ]
    pageSize: int
    pageToken: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective(
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
class GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse(
    typing_extensions.TypedDict, total=False
):
    monitoringStats: _list[GoogleCloudAiplatformV1ModelMonitoringStatsAnomalies]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchNearestEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1NearestNeighborQuery
    returnFullEntity: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SearchNearestEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    nearestNeighbors: GoogleCloudAiplatformV1NearestNeighbors

@typing.type_check_only
class GoogleCloudAiplatformV1Segment(typing_extensions.TypedDict, total=False):
    endIndex: int
    partIndex: int
    startIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1ShieldedVmConfig(typing_extensions.TypedDict, total=False):
    enableSecureBoot: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SmoothGradConfig(typing_extensions.TypedDict, total=False):
    featureNoiseSigma: GoogleCloudAiplatformV1FeatureNoiseSigma
    noiseSigma: float
    noisySampleCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SpecialistPool(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    pendingDataLabelingJobs: _list[str]
    specialistManagerEmails: _list[str]
    specialistManagersCount: int
    specialistWorkerEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StartNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1StartNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1StopTrialRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1StratifiedSplit(typing_extensions.TypedDict, total=False):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1StreamRawPredictRequest(
    typing_extensions.TypedDict, total=False
):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingPredictRequest(
    typing_extensions.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingPredictResponse(
    typing_extensions.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    entityIds: _list[str]
    featureSelector: GoogleCloudAiplatformV1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1StringArray(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1Study(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    inactiveReason: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]
    studySpec: GoogleCloudAiplatformV1StudySpec

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpec(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
        "ALGORITHM_UNSPECIFIED", "GRID_SEARCH", "RANDOM_SEARCH"
    ]
    convexAutomatedStoppingSpec: GoogleCloudAiplatformV1StudySpecConvexAutomatedStoppingSpec
    decayCurveStoppingSpec: GoogleCloudAiplatformV1StudySpecDecayCurveAutomatedStoppingSpec
    measurementSelectionType: typing_extensions.Literal[
        "MEASUREMENT_SELECTION_TYPE_UNSPECIFIED", "LAST_MEASUREMENT", "BEST_MEASUREMENT"
    ]
    medianAutomatedStoppingSpec: GoogleCloudAiplatformV1StudySpecMedianAutomatedStoppingSpec
    metrics: _list[GoogleCloudAiplatformV1StudySpecMetricSpec]
    observationNoise: typing_extensions.Literal[
        "OBSERVATION_NOISE_UNSPECIFIED", "LOW", "HIGH"
    ]
    parameters: _list[GoogleCloudAiplatformV1StudySpecParameterSpec]
    studyStoppingConfig: GoogleCloudAiplatformV1StudySpecStudyStoppingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecConvexAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    learningRateParameterName: str
    maxStepCount: str
    minMeasurementCount: str
    minStepCount: str
    updateAllStoppedTrials: bool
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecDecayCurveAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecMedianAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecMetricSpec(
    typing_extensions.TypedDict, total=False
):
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str
    safetyConfig: GoogleCloudAiplatformV1StudySpecMetricSpecSafetyMetricConfig

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecMetricSpecSafetyMetricConfig(
    typing_extensions.TypedDict, total=False
):
    desiredMinSafeTrialsFraction: float
    safetyThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpec(
    typing_extensions.TypedDict, total=False
):
    categoricalValueSpec: GoogleCloudAiplatformV1StudySpecParameterSpecCategoricalValueSpec
    conditionalParameterSpecs: _list[
        GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpec
    ]
    discreteValueSpec: GoogleCloudAiplatformV1StudySpecParameterSpecDiscreteValueSpec
    doubleValueSpec: GoogleCloudAiplatformV1StudySpecParameterSpecDoubleValueSpec
    integerValueSpec: GoogleCloudAiplatformV1StudySpecParameterSpecIntegerValueSpec
    parameterId: str
    scaleType: typing_extensions.Literal[
        "SCALE_TYPE_UNSPECIFIED",
        "UNIT_LINEAR_SCALE",
        "UNIT_LOG_SCALE",
        "UNIT_REVERSE_LOG_SCALE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecCategoricalValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpec(
    typing_extensions.TypedDict, total=False
):
    parameterSpec: GoogleCloudAiplatformV1StudySpecParameterSpec
    parentCategoricalValues: GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition
    parentDiscreteValues: GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition
    parentIntValues: GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecIntValueCondition

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecIntValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecDiscreteValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: float
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecDoubleValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: float
    maxValue: float
    minValue: float

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecIntegerValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: str
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecStudyStoppingConfig(
    typing_extensions.TypedDict, total=False
):
    maxDurationNoProgress: str
    maxNumTrials: int
    maxNumTrialsNoProgress: int
    maximumRuntimeConstraint: GoogleCloudAiplatformV1StudyTimeConstraint
    minNumTrials: int
    minimumRuntimeConstraint: GoogleCloudAiplatformV1StudyTimeConstraint
    shouldStopAsap: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudyTimeConstraint(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    maxDuration: str

@typing.type_check_only
class GoogleCloudAiplatformV1SuggestTrialsMetadata(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SuggestTrialsRequest(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    contexts: _list[GoogleCloudAiplatformV1TrialContext]
    suggestionCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SuggestTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    studyState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]
    trials: _list[GoogleCloudAiplatformV1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1SyncFeatureViewRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SyncFeatureViewResponse(
    typing_extensions.TypedDict, total=False
):
    featureViewSync: str

@typing.type_check_only
class GoogleCloudAiplatformV1TFRecordDestination(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudAiplatformV1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1Tensor(typing_extensions.TypedDict, total=False):
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
    listVal: _list[GoogleCloudAiplatformV1Tensor]
    shape: _list[str]
    stringVal: _list[str]
    structVal: dict[str, typing.Any]
    tensorVal: str
    uint64Val: _list[str]
    uintVal: _list[int]

@typing.type_check_only
class GoogleCloudAiplatformV1Tensorboard(typing_extensions.TypedDict, total=False):
    blobStoragePathPrefix: str
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    isDefault: bool
    labels: dict[str, typing.Any]
    name: str
    runCount: int
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardBlob(typing_extensions.TypedDict, total=False):
    data: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardBlobSequence(
    typing_extensions.TypedDict, total=False
):
    values: _list[GoogleCloudAiplatformV1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardExperiment(
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
class GoogleCloudAiplatformV1TensorboardRun(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTensor(
    typing_extensions.TypedDict, total=False
):
    value: str
    versionNumber: int

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTimeSeries(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    etag: str
    metadata: GoogleCloudAiplatformV1TensorboardTimeSeriesMetadata
    name: str
    pluginData: str
    pluginName: str
    updateTime: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTimeSeriesMetadata(
    typing_extensions.TypedDict, total=False
):
    maxBlobSequenceLength: str
    maxStep: str
    maxWallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ThresholdConfig(typing_extensions.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1TimeSeriesData(typing_extensions.TypedDict, total=False):
    tensorboardTimeSeriesId: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]
    values: _list[GoogleCloudAiplatformV1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1TimeSeriesDataPoint(
    typing_extensions.TypedDict, total=False
):
    blobs: GoogleCloudAiplatformV1TensorboardBlobSequence
    scalar: GoogleCloudAiplatformV1Scalar
    step: str
    tensor: GoogleCloudAiplatformV1TensorboardTensor
    wallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1TimestampSplit(typing_extensions.TypedDict, total=False):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1TokensInfo(typing_extensions.TypedDict, total=False):
    tokenIds: _list[str]
    tokens: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1Tool(typing_extensions.TypedDict, total=False):
    functionDeclarations: _list[GoogleCloudAiplatformV1FunctionDeclaration]

@typing.type_check_only
class GoogleCloudAiplatformV1TrainingConfig(typing_extensions.TypedDict, total=False):
    timeoutTrainingMilliHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1TrainingPipeline(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    inputDataConfig: GoogleCloudAiplatformV1InputDataConfig
    labels: dict[str, typing.Any]
    modelId: str
    modelToUpload: GoogleCloudAiplatformV1Model
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
class GoogleCloudAiplatformV1Trial(typing_extensions.TypedDict, total=False):
    clientId: str
    customJob: str
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1Measurement
    id: str
    infeasibleReason: str
    measurements: _list[GoogleCloudAiplatformV1Measurement]
    name: str
    parameters: _list[GoogleCloudAiplatformV1TrialParameter]
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
class GoogleCloudAiplatformV1TrialContext(typing_extensions.TypedDict, total=False):
    description: str
    parameters: _list[GoogleCloudAiplatformV1TrialParameter]

@typing.type_check_only
class GoogleCloudAiplatformV1TrialParameter(typing_extensions.TypedDict, total=False):
    parameterId: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployIndexRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployIndexResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UnmanagedContainerModel(
    typing_extensions.TypedDict, total=False
):
    artifactUri: str
    containerSpec: GoogleCloudAiplatformV1ModelContainerSpec
    predictSchemata: GoogleCloudAiplatformV1PredictSchemata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateDeploymentResourcePoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateExplanationDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateExplanationDatasetRequest(
    typing_extensions.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1Examples

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateExplanationDatasetResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureGroupOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureOnlineStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureViewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeaturestoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateModelDeploymentMonitoringJobOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateSpecialistPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    specialistPool: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateTensorboardOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpgradeNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpgradeNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UploadModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UploadModelRequest(
    typing_extensions.TypedDict, total=False
):
    model: GoogleCloudAiplatformV1Model
    modelId: str
    parentModel: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1UploadModelResponse(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpsertDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1IndexDatapoint]
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpsertDatapointsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UserActionReference(
    typing_extensions.TypedDict, total=False
):
    dataLabelingJob: str
    method: str
    operation: str

@typing.type_check_only
class GoogleCloudAiplatformV1Value(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1VideoMetadata(typing_extensions.TypedDict, total=False):
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1WorkerPoolSpec(typing_extensions.TypedDict, total=False):
    containerSpec: GoogleCloudAiplatformV1ContainerSpec
    diskSpec: GoogleCloudAiplatformV1DiskSpec
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    nfsMounts: _list[GoogleCloudAiplatformV1NfsMount]
    pythonPackageSpec: GoogleCloudAiplatformV1PythonPackageSpec
    replicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesPayload(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    featureValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    payloads: _list[GoogleCloudAiplatformV1WriteFeatureValuesPayload]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest(
    typing_extensions.TypedDict, total=False
):
    writeRunDataRequests: _list[GoogleCloudAiplatformV1WriteTensorboardRunDataRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardExperimentDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardRunDataRequest(
    typing_extensions.TypedDict, total=False
):
    tensorboardRun: str
    timeSeriesData: _list[GoogleCloudAiplatformV1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardRunDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1XraiAttribution(typing_extensions.TypedDict, total=False):
    blurBaselineConfig: GoogleCloudAiplatformV1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1SmoothGradConfig
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
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy

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
        "GEMINI_V1_CMS_GITHUB_V7",
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
        "CLOUD_SECURITY_RAG_CISA",
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
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "GEMINI_GOOSE_PUBLIC",
        "GEMINI_GOOSE_SILOED",
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
        "CLOUD_GEMIT_CLOUD_FACTUALITY_GROUNDING_MAGI",
        "CLOUD_GEMIT_MT_DIALGUE_LMSYS",
        "CLOUD_GEMIT_MTS_DIALOGUE_V3",
        "CLOUD_GEMIT_COMMIT_MSG_GEN_V3",
        "CLOUD_GEMIT_CODE_IF_V1",
        "CLOUD_GEMIT_CODE_SELF_REPAIR",
        "CLOUD_GEMIT_IDENTITY",
        "CLOUD_GEMIT_SEARCH_AUGMENTED_RESPONSE_GENERATION",
        "CLOUD_GEMIT_AMPS",
        "CLOUD_GEMIT_AQUA",
        "CLOUD_GEMIT_COMMON_SENSE_REASONING_SCHEMA",
        "CLOUD_GEMIT_GSM8K_SCHEMA",
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
        "GEMINI_V1_CMS_GITHUB_V7",
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
        "CLOUD_SECURITY_RAG_CISA",
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
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "GEMINI_GOOSE_PUBLIC",
        "GEMINI_GOOSE_SILOED",
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
        "CLOUD_GEMIT_CLOUD_FACTUALITY_GROUNDING_MAGI",
        "CLOUD_GEMIT_MT_DIALGUE_LMSYS",
        "CLOUD_GEMIT_MTS_DIALOGUE_V3",
        "CLOUD_GEMIT_COMMIT_MSG_GEN_V3",
        "CLOUD_GEMIT_CODE_IF_V1",
        "CLOUD_GEMIT_CODE_SELF_REPAIR",
        "CLOUD_GEMIT_IDENTITY",
        "CLOUD_GEMIT_SEARCH_AUGMENTED_RESPONSE_GENERATION",
        "CLOUD_GEMIT_AMPS",
        "CLOUD_GEMIT_AQUA",
        "CLOUD_GEMIT_COMMON_SENSE_REASONING_SCHEMA",
        "CLOUD_GEMIT_GSM8K_SCHEMA",
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
        "GEMINI_V1_CMS_GITHUB_V7",
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
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "CLOUD_SECURITY_PRETRAINING",
        "CLOUD_SECURITY_FINETUNING",
        "CLOUD_SECURITY_RAG_CISA",
        "GEMINI_GOOSE_PUBLIC",
        "GEMINI_GOOSE_SILOED",
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
        "CLOUD_GEMIT_CLOUD_FACTUALITY_GROUNDING_MAGI",
        "CLOUD_GEMIT_MT_DIALGUE_LMSYS",
        "CLOUD_GEMIT_MTS_DIALOGUE_V3",
        "CLOUD_GEMIT_COMMIT_MSG_GEN_V3",
        "CLOUD_GEMIT_CODE_IF_V1",
        "CLOUD_GEMIT_CODE_SELF_REPAIR",
        "CLOUD_GEMIT_IDENTITY",
        "CLOUD_GEMIT_SEARCH_AUGMENTED_RESPONSE_GENERATION",
        "CLOUD_GEMIT_AMPS",
        "CLOUD_GEMIT_AQUA",
        "CLOUD_GEMIT_COMMON_SENSE_REASONING_SCHEMA",
        "CLOUD_GEMIT_GSM8K_SCHEMA",
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
        "GEMINI_V1_CMS_GITHUB_V7",
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
        "GEMINI_IT_CLOUD_CODE_IF",
        "GEMINI_IT_CLOUD_EUR_LEX_JSON",
        "GEMINI_IT_CLOUD_OASST",
        "GEMINI_IT_CLOUD_SELF_INSTRUCT",
        "GEMINI_IT_CLOUD_UCS_AQUAMUSE",
        "GEMIT_BRIDGE_SUFFIX_FT",
        "CLOUD_SECURITY_PRETRAINING",
        "CLOUD_SECURITY_FINETUNING",
        "CLOUD_SECURITY_RAG_CISA",
        "GEMINI_GOOSE_PUBLIC",
        "GEMINI_GOOSE_SILOED",
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
        "CLOUD_GEMIT_CLOUD_FACTUALITY_GROUNDING_MAGI",
        "CLOUD_GEMIT_MT_DIALGUE_LMSYS",
        "CLOUD_GEMIT_MTS_DIALOGUE_V3",
        "CLOUD_GEMIT_COMMIT_MSG_GEN_V3",
        "CLOUD_GEMIT_CODE_IF_V1",
        "CLOUD_GEMIT_CODE_SELF_REPAIR",
        "CLOUD_GEMIT_IDENTITY",
        "CLOUD_GEMIT_SEARCH_AUGMENTED_RESPONSE_GENERATION",
        "CLOUD_GEMIT_AMPS",
        "CLOUD_GEMIT_AQUA",
        "CLOUD_GEMIT_COMMON_SENSE_REASONING_SCHEMA",
        "CLOUD_GEMIT_GSM8K_SCHEMA",
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
class LearningGenaiRootCodeyChatMetadata(typing_extensions.TypedDict, total=False):
    codeLanguage: typing_extensions.Literal[
        "UNSPECIFIED",
        "ALL",
        "TEXT",
        "CPP",
        "PYTHON",
        "KOTLIN",
        "JAVA",
        "JAVASCRIPT",
        "GO",
        "R",
        "JUPYTER_NOTEBOOK",
        "TYPESCRIPT",
        "HTML",
        "SQL",
        "BASH",
        "C",
        "DART",
        "GRADLE",
        "JAVADOC",
        "JSON",
        "MAKEFILE",
        "MARKDOWN",
        "PROTO",
        "XML",
        "YAML",
    ]

@typing.type_check_only
class LearningGenaiRootCodeyCheckpoint(typing_extensions.TypedDict, total=False):
    codeyTruncatorMetadata: LearningGenaiRootCodeyTruncatorMetadata
    currentSample: str
    postInferenceStep: typing_extensions.Literal[
        "STEP_POST_PROCESSING_STEP_UNSPECIFIED",
        "STEP_ORIGINAL_MODEL_OUTPUT",
        "STEP_MODEL_OUTPUT_DEDUPLICATION",
        "STEP_STOP_SEQUENCE_TRUNCATION",
        "STEP_HEURISTIC_TRUNCATION",
        "STEP_WALD_TRUNCATION",
        "STEP_WHITESPACE_TRUNCATION",
        "STEP_FINAL_DEDUPLICATION",
        "STEP_TOXICITY_CHECK",
        "STEP_RECITATION_CHECK",
        "STEP_RETURNED",
        "STEP_WALKBACK_CORRECTION",
        "STEP_SCORE_THRESHOLDING",
        "STEP_MODEL_CONFIG_STOP_SEQUENCE_TRUNCATION",
        "STEP_CUSTOM_STOP_SEQUENCE_TRUNCATION",
        "STEP_EXPECTED_SAMPLE_SIZE",
    ]

@typing.type_check_only
class LearningGenaiRootCodeyCompletionMetadata(
    typing_extensions.TypedDict, total=False
):
    checkpoints: _list[LearningGenaiRootCodeyCheckpoint]

@typing.type_check_only
class LearningGenaiRootCodeyOutput(typing_extensions.TypedDict, total=False):
    codeyChatMetadata: LearningGenaiRootCodeyChatMetadata
    codeyCompletionMetadata: LearningGenaiRootCodeyCompletionMetadata

@typing.type_check_only
class LearningGenaiRootCodeyTruncatorMetadata(typing_extensions.TypedDict, total=False):
    cutoffIndex: int
    truncatedText: str

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
    codeyOutput: LearningGenaiRootCodeyOutput
    currentStreamTextLength: int
    deleted: bool
    filterMeta: _list[LearningGenaiRootFilterMetadata]
    finalMessageScore: LearningGenaiRootScore
    finishReason: typing_extensions.Literal[
        "UNSPECIFIED", "RETURN", "STOP", "MAX_TOKENS", "FILTER"
    ]
    groundingMetadata: LearningGenaiRootGroundingMetadata
    isCode: bool
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
