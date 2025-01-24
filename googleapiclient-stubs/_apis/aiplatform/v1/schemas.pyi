import typing

import typing_extensions

_list = list

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoResponse(
    typing_extensions.TypedDict, total=False
):
    generatedSamples: _list[CloudAiLargeModelsVisionMedia]
    raiMediaFilteredCount: int
    raiMediaFilteredReasons: _list[str]

@typing.type_check_only
class CloudAiLargeModelsVisionImage(typing_extensions.TypedDict, total=False):
    encoding: str
    generationSeed: int
    image: str
    imageRaiScores: CloudAiLargeModelsVisionImageRAIScores
    imageSize: CloudAiLargeModelsVisionImageImageSize
    raiInfo: CloudAiLargeModelsVisionRaiInfo
    semanticFilterResponse: CloudAiLargeModelsVisionSemanticFilterResponse
    text: str
    uri: str

@typing.type_check_only
class CloudAiLargeModelsVisionImageImageSize(typing_extensions.TypedDict, total=False):
    channels: int
    height: int
    width: int

@typing.type_check_only
class CloudAiLargeModelsVisionImageRAIScores(typing_extensions.TypedDict, total=False):
    agileWatermarkDetectionScore: float

@typing.type_check_only
class CloudAiLargeModelsVisionMedia(typing_extensions.TypedDict, total=False):
    image: CloudAiLargeModelsVisionImage
    video: CloudAiLargeModelsVisionVideo

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
    blockedEntities: _list[str]
    detectedLabels: _list[CloudAiLargeModelsVisionRaiInfoDetectedLabels]
    modelName: str
    raiCategories: _list[str]
    scores: _list[float]

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfoDetectedLabels(
    typing_extensions.TypedDict, total=False
):
    entities: _list[CloudAiLargeModelsVisionRaiInfoDetectedLabelsEntity]
    raiCategory: str

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfoDetectedLabelsBoundingBox(
    typing_extensions.TypedDict, total=False
):
    x1: int
    x2: int
    y1: int
    y2: int

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfoDetectedLabelsEntity(
    typing_extensions.TypedDict, total=False
):
    boundingBox: CloudAiLargeModelsVisionRaiInfoDetectedLabelsBoundingBox
    description: str
    iouScore: float
    mid: str
    score: float

@typing.type_check_only
class CloudAiLargeModelsVisionSemanticFilterResponse(
    typing_extensions.TypedDict, total=False
):
    namedBoundingBoxes: _list[CloudAiLargeModelsVisionNamedBoundingBox]
    passedSemanticFilter: bool

@typing.type_check_only
class CloudAiLargeModelsVisionVideo(typing_extensions.TypedDict, total=False):
    encodedVideo: str
    encoding: str
    uri: str
    video: str

@typing.type_check_only
class CloudAiPlatformCommonCreatePipelineJobApiErrorDetail(
    typing_extensions.TypedDict, total=False
):
    errorCause: typing_extensions.Literal[
        "ERROR_CAUSE_UNSPECIFIED",
        "INVALID_PIPELINE_SPEC_FORMAT",
        "INVALID_PIPELINE_SPEC",
        "INVALID_DEPLOYMENT_CONFIG",
        "INVALID_DEPLOYMENT_SPEC",
        "INVALID_INSTANCE_SCHEMA",
        "INVALID_CUSTOM_JOB",
        "INVALID_CONTAINER_SPEC",
        "INVALID_NOTIFICATION_EMAIL_SETUP",
        "INVALID_SERVICE_ACCOUNT_SETUP",
        "INVALID_KMS_SETUP",
        "INVALID_NETWORK_SETUP",
        "INVALID_PIPELINE_TASK_SPEC",
        "INVALID_PIPELINE_TASK_ARTIFACT",
        "INVALID_IMPORTER_SPEC",
        "INVALID_RESOLVER_SPEC",
        "INVALID_RUNTIME_PARAMETERS",
        "CLOUD_API_NOT_ENABLED",
        "INVALID_GCS_INPUT_URI",
        "INVALID_GCS_OUTPUT_URI",
        "INVALID_COMPONENT_SPEC",
        "INVALID_DAG_OUTPUTS_SPEC",
        "INVALID_DAG_SPEC",
        "INSUFFICIENT_QUOTA",
        "INTERNAL",
    ]
    publicMessage: str

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
class GoogleCloudAiplatformV1ApiAuth(typing_extensions.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1ApiAuthApiKeyConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ApiAuthApiKeyConfig(
    typing_extensions.TypedDict, total=False
):
    apiKeySecretVersion: str

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
class GoogleCloudAiplatformV1AugmentPromptRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1Content]
    model: GoogleCloudAiplatformV1AugmentPromptRequestModel
    vertexRagStore: GoogleCloudAiplatformV1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1AugmentPromptRequestModel(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1AugmentPromptResponse(
    typing_extensions.TypedDict, total=False
):
    augmentedPrompt: _list[GoogleCloudAiplatformV1Content]
    facts: _list[GoogleCloudAiplatformV1Fact]

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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
class GoogleCloudAiplatformV1BleuInput(typing_extensions.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1BleuInstance]
    metricSpec: GoogleCloudAiplatformV1BleuSpec

@typing.type_check_only
class GoogleCloudAiplatformV1BleuInstance(typing_extensions.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1BleuMetricValue(typing_extensions.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1BleuResults(typing_extensions.TypedDict, total=False):
    bleuMetricValues: _list[GoogleCloudAiplatformV1BleuMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1BleuSpec(typing_extensions.TypedDict, total=False):
    useEffectiveOrder: bool

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
class GoogleCloudAiplatformV1CacheConfig(typing_extensions.TypedDict, total=False):
    disableCache: bool
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1CachedContent(typing_extensions.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1Content]
    createTime: str
    displayName: str
    expireTime: str
    model: str
    name: str
    systemInstruction: GoogleCloudAiplatformV1Content
    toolConfig: GoogleCloudAiplatformV1ToolConfig
    tools: _list[GoogleCloudAiplatformV1Tool]
    ttl: str
    updateTime: str
    usageMetadata: GoogleCloudAiplatformV1CachedContentUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CachedContentUsageMetadata(
    typing_extensions.TypedDict, total=False
):
    audioDurationSeconds: int
    imageCount: int
    textCount: int
    totalTokenCount: int
    videoDurationSeconds: int

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
class GoogleCloudAiplatformV1CancelTuningJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1Candidate(typing_extensions.TypedDict, total=False):
    avgLogprobs: float
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
        "BLOCKLIST",
        "PROHIBITED_CONTENT",
        "SPII",
        "MALFORMED_FUNCTION_CALL",
    ]
    groundingMetadata: GoogleCloudAiplatformV1GroundingMetadata
    index: int
    logprobsResult: GoogleCloudAiplatformV1LogprobsResult
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
class GoogleCloudAiplatformV1Claim(typing_extensions.TypedDict, total=False):
    endIndex: int
    factIndexes: _list[int]
    score: float
    startIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1ClientConnectionConfig(
    typing_extensions.TypedDict, total=False
):
    inferenceTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceInput(typing_extensions.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1CoherenceInstance
    metricSpec: GoogleCloudAiplatformV1CoherenceSpec

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceInstance(
    typing_extensions.TypedDict, total=False
):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceResult(typing_extensions.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceSpec(typing_extensions.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1CometInput(typing_extensions.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1CometInstance
    metricSpec: GoogleCloudAiplatformV1CometSpec

@typing.type_check_only
class GoogleCloudAiplatformV1CometInstance(typing_extensions.TypedDict, total=False):
    prediction: str
    reference: str
    source: str

@typing.type_check_only
class GoogleCloudAiplatformV1CometResult(typing_extensions.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1CometSpec(typing_extensions.TypedDict, total=False):
    sourceLanguage: str
    targetLanguage: str
    version: typing_extensions.Literal["COMET_VERSION_UNSPECIFIED", "COMET_22_SRC_REF"]

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
    contents: _list[GoogleCloudAiplatformV1Content]
    instances: _list[typing.Any]
    model: str

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
class GoogleCloudAiplatformV1CorpusStatus(typing_extensions.TypedDict, total=False):
    errorStatus: str
    state: typing_extensions.Literal["UNKNOWN", "INITIALIZED", "ACTIVE", "ERROR"]

@typing.type_check_only
class GoogleCloudAiplatformV1CorroborateContentRequest(
    typing_extensions.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1Content
    facts: _list[GoogleCloudAiplatformV1Fact]
    parameters: GoogleCloudAiplatformV1CorroborateContentRequestParameters

@typing.type_check_only
class GoogleCloudAiplatformV1CorroborateContentRequestParameters(
    typing_extensions.TypedDict, total=False
):
    citationThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1CorroborateContentResponse(
    typing_extensions.TypedDict, total=False
):
    claims: _list[GoogleCloudAiplatformV1Claim]
    corroborationScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1CountTokensRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1Content]
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    instances: _list[typing.Any]
    model: str
    systemInstruction: GoogleCloudAiplatformV1Content
    tools: _list[GoogleCloudAiplatformV1Tool]

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
    nearestNeighborSearchOperationMetadata: (
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1CreateMetadataStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateNotebookExecutionJobOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateNotebookExecutionJobRequest(
    typing_extensions.TypedDict, total=False
):
    notebookExecutionJob: GoogleCloudAiplatformV1NotebookExecutionJob
    notebookExecutionJobId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateNotebookRuntimeTemplateOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreatePersistentResourceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    persistentResourceId: str
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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    modelReference: str
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    savedQueries: _list[GoogleCloudAiplatformV1SavedQuery]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetVersion(typing_extensions.TypedDict, total=False):
    bigQueryDatasetName: str
    createTime: str
    displayName: str
    etag: str
    metadata: typing.Any
    modelReference: str
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1DedicatedResources(
    typing_extensions.TypedDict, total=False
):
    autoscalingMetricSpecs: _list[GoogleCloudAiplatformV1AutoscalingMetricSpec]
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    maxReplicaCount: int
    minReplicaCount: int
    requiredReplicaCount: int
    spot: bool

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
    selectTimeRangeAndFeature: (
        GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectTimeRangeAndFeature
    )

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
    selectTimeRangeAndFeature: (
        GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectTimeRangeAndFeature
    )

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
    pscAutomationConfigs: _list[GoogleCloudAiplatformV1PSCAutomationConfig]
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
    disableExplanations: bool
    displayName: str
    enableAccessLogging: bool
    explanationSpec: GoogleCloudAiplatformV1ExplanationSpec
    fasterDeploymentConfig: GoogleCloudAiplatformV1FasterDeploymentConfig
    id: str
    model: str
    modelVersionId: str
    privateEndpoints: GoogleCloudAiplatformV1PrivateEndpoints
    serviceAccount: str
    sharedResources: str
    status: GoogleCloudAiplatformV1DeployedModelStatus
    systemLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedModelRef(typing_extensions.TypedDict, total=False):
    deployedModelId: str
    endpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedModelStatus(
    typing_extensions.TypedDict, total=False
):
    availableReplicaCount: int
    lastUpdateTime: str
    message: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeploymentResourcePool(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    disableContainerLogging: bool
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceAccount: str

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
class GoogleCloudAiplatformV1DirectUploadSource(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1DiskSpec(typing_extensions.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1DoubleArray(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1DynamicRetrievalConfig(
    typing_extensions.TypedDict, total=False
):
    dynamicThreshold: float
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "MODE_DYNAMIC"]

@typing.type_check_only
class GoogleCloudAiplatformV1EncryptionSpec(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class GoogleCloudAiplatformV1Endpoint(typing_extensions.TypedDict, total=False):
    clientConnectionConfig: GoogleCloudAiplatformV1ClientConnectionConfig
    createTime: str
    dedicatedEndpointDns: str
    dedicatedEndpointEnabled: bool
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
    predictRequestResponseLoggingConfig: (
        GoogleCloudAiplatformV1PredictRequestResponseLoggingConfig
    )
    privateServiceConnectConfig: GoogleCloudAiplatformV1PrivateServiceConnectConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
class GoogleCloudAiplatformV1EvaluateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    bleuInput: GoogleCloudAiplatformV1BleuInput
    coherenceInput: GoogleCloudAiplatformV1CoherenceInput
    cometInput: GoogleCloudAiplatformV1CometInput
    exactMatchInput: GoogleCloudAiplatformV1ExactMatchInput
    fluencyInput: GoogleCloudAiplatformV1FluencyInput
    fulfillmentInput: GoogleCloudAiplatformV1FulfillmentInput
    groundednessInput: GoogleCloudAiplatformV1GroundednessInput
    metricxInput: GoogleCloudAiplatformV1MetricxInput
    pairwiseMetricInput: GoogleCloudAiplatformV1PairwiseMetricInput
    pairwiseQuestionAnsweringQualityInput: (
        GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityInput
    )
    pairwiseSummarizationQualityInput: (
        GoogleCloudAiplatformV1PairwiseSummarizationQualityInput
    )
    pointwiseMetricInput: GoogleCloudAiplatformV1PointwiseMetricInput
    questionAnsweringCorrectnessInput: (
        GoogleCloudAiplatformV1QuestionAnsweringCorrectnessInput
    )
    questionAnsweringHelpfulnessInput: (
        GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessInput
    )
    questionAnsweringQualityInput: GoogleCloudAiplatformV1QuestionAnsweringQualityInput
    questionAnsweringRelevanceInput: (
        GoogleCloudAiplatformV1QuestionAnsweringRelevanceInput
    )
    rougeInput: GoogleCloudAiplatformV1RougeInput
    safetyInput: GoogleCloudAiplatformV1SafetyInput
    summarizationHelpfulnessInput: GoogleCloudAiplatformV1SummarizationHelpfulnessInput
    summarizationQualityInput: GoogleCloudAiplatformV1SummarizationQualityInput
    summarizationVerbosityInput: GoogleCloudAiplatformV1SummarizationVerbosityInput
    toolCallValidInput: GoogleCloudAiplatformV1ToolCallValidInput
    toolNameMatchInput: GoogleCloudAiplatformV1ToolNameMatchInput
    toolParameterKeyMatchInput: GoogleCloudAiplatformV1ToolParameterKeyMatchInput
    toolParameterKvMatchInput: GoogleCloudAiplatformV1ToolParameterKVMatchInput
    trajectoryAnyOrderMatchInput: GoogleCloudAiplatformV1TrajectoryAnyOrderMatchInput
    trajectoryExactMatchInput: GoogleCloudAiplatformV1TrajectoryExactMatchInput
    trajectoryInOrderMatchInput: GoogleCloudAiplatformV1TrajectoryInOrderMatchInput
    trajectoryPrecisionInput: GoogleCloudAiplatformV1TrajectoryPrecisionInput
    trajectoryRecallInput: GoogleCloudAiplatformV1TrajectoryRecallInput
    trajectorySingleToolUseInput: GoogleCloudAiplatformV1TrajectorySingleToolUseInput

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluateInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    bleuResults: GoogleCloudAiplatformV1BleuResults
    coherenceResult: GoogleCloudAiplatformV1CoherenceResult
    cometResult: GoogleCloudAiplatformV1CometResult
    exactMatchResults: GoogleCloudAiplatformV1ExactMatchResults
    fluencyResult: GoogleCloudAiplatformV1FluencyResult
    fulfillmentResult: GoogleCloudAiplatformV1FulfillmentResult
    groundednessResult: GoogleCloudAiplatformV1GroundednessResult
    metricxResult: GoogleCloudAiplatformV1MetricxResult
    pairwiseMetricResult: GoogleCloudAiplatformV1PairwiseMetricResult
    pairwiseQuestionAnsweringQualityResult: (
        GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityResult
    )
    pairwiseSummarizationQualityResult: (
        GoogleCloudAiplatformV1PairwiseSummarizationQualityResult
    )
    pointwiseMetricResult: GoogleCloudAiplatformV1PointwiseMetricResult
    questionAnsweringCorrectnessResult: (
        GoogleCloudAiplatformV1QuestionAnsweringCorrectnessResult
    )
    questionAnsweringHelpfulnessResult: (
        GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessResult
    )
    questionAnsweringQualityResult: (
        GoogleCloudAiplatformV1QuestionAnsweringQualityResult
    )
    questionAnsweringRelevanceResult: (
        GoogleCloudAiplatformV1QuestionAnsweringRelevanceResult
    )
    rougeResults: GoogleCloudAiplatformV1RougeResults
    safetyResult: GoogleCloudAiplatformV1SafetyResult
    summarizationHelpfulnessResult: (
        GoogleCloudAiplatformV1SummarizationHelpfulnessResult
    )
    summarizationQualityResult: GoogleCloudAiplatformV1SummarizationQualityResult
    summarizationVerbosityResult: GoogleCloudAiplatformV1SummarizationVerbosityResult
    toolCallValidResults: GoogleCloudAiplatformV1ToolCallValidResults
    toolNameMatchResults: GoogleCloudAiplatformV1ToolNameMatchResults
    toolParameterKeyMatchResults: GoogleCloudAiplatformV1ToolParameterKeyMatchResults
    toolParameterKvMatchResults: GoogleCloudAiplatformV1ToolParameterKVMatchResults
    trajectoryAnyOrderMatchResults: (
        GoogleCloudAiplatformV1TrajectoryAnyOrderMatchResults
    )
    trajectoryExactMatchResults: GoogleCloudAiplatformV1TrajectoryExactMatchResults
    trajectoryInOrderMatchResults: GoogleCloudAiplatformV1TrajectoryInOrderMatchResults
    trajectoryPrecisionResults: GoogleCloudAiplatformV1TrajectoryPrecisionResults
    trajectoryRecallResults: GoogleCloudAiplatformV1TrajectoryRecallResults
    trajectorySingleToolUseResults: (
        GoogleCloudAiplatformV1TrajectorySingleToolUseResults
    )

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
class GoogleCloudAiplatformV1ExactMatchInput(typing_extensions.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1ExactMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ExactMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchInstance(
    typing_extensions.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchResults(
    typing_extensions.TypedDict, total=False
):
    exactMatchMetricValues: _list[GoogleCloudAiplatformV1ExactMatchMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchSpec(
    typing_extensions.TypedDict, total=False
): ...

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
    featureValueDomain: (
        GoogleCloudAiplatformV1ExplanationMetadataInputMetadataFeatureValueDomain
    )
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
    integratedGradientsAttribution: (
        GoogleCloudAiplatformV1IntegratedGradientsAttribution
    )
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
class GoogleCloudAiplatformV1Fact(typing_extensions.TypedDict, total=False):
    query: str
    score: float
    summary: str
    title: str
    uri: str
    vectorDistance: float

@typing.type_check_only
class GoogleCloudAiplatformV1FasterDeploymentConfig(
    typing_extensions.TypedDict, total=False
):
    fastTryoutEnabled: bool

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
        "STRUCT",
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
    dense: bool
    entityIdColumns: _list[str]
    staticDataSource: bool
    timeSeries: GoogleCloudAiplatformV1FeatureGroupBigQueryTimeSeries

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureGroupBigQueryTimeSeries(
    typing_extensions.TypedDict, total=False
):
    timestampColumn: str

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
    dedicatedServingEndpoint: (
        GoogleCloudAiplatformV1FeatureOnlineStoreDedicatedServingEndpoint
    )
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    optimized: GoogleCloudAiplatformV1FeatureOnlineStoreOptimized
    satisfiesPzi: bool
    satisfiesPzs: bool
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
class GoogleCloudAiplatformV1FeatureOnlineStoreDedicatedServingEndpoint(
    typing_extensions.TypedDict, total=False
):
    privateServiceConnectConfig: GoogleCloudAiplatformV1PrivateServiceConnectConfig
    publicEndpointDomainName: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreOptimized(
    typing_extensions.TypedDict, total=False
): ...

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
    structValue: GoogleCloudAiplatformV1StructValue

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
    indexConfig: GoogleCloudAiplatformV1FeatureViewIndexConfig
    labels: dict[str, typing.Any]
    name: str
    optimizedConfig: GoogleCloudAiplatformV1FeatureViewOptimizedConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    syncConfig: GoogleCloudAiplatformV1FeatureViewSyncConfig
    updateTime: str
    vertexRagSource: GoogleCloudAiplatformV1FeatureViewVertexRagSource

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
class GoogleCloudAiplatformV1FeatureViewIndexConfig(
    typing_extensions.TypedDict, total=False
):
    bruteForceConfig: GoogleCloudAiplatformV1FeatureViewIndexConfigBruteForceConfig
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
    treeAhConfig: GoogleCloudAiplatformV1FeatureViewIndexConfigTreeAHConfig

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewIndexConfigBruteForceConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewIndexConfigTreeAHConfig(
    typing_extensions.TypedDict, total=False
):
    leafNodeEmbeddingCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewOptimizedConfig(
    typing_extensions.TypedDict, total=False
):
    automaticResources: GoogleCloudAiplatformV1AutomaticResources

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSync(typing_extensions.TypedDict, total=False):
    createTime: str
    finalStatus: GoogleRpcStatus
    name: str
    runTime: GoogleTypeInterval
    satisfiesPzi: bool
    satisfiesPzs: bool
    syncSummary: GoogleCloudAiplatformV1FeatureViewSyncSyncSummary

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSyncConfig(
    typing_extensions.TypedDict, total=False
):
    continuous: bool
    cron: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSyncSyncSummary(
    typing_extensions.TypedDict, total=False
):
    rowSynced: str
    systemWatermarkTime: str
    totalSlot: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewVertexRagSource(
    typing_extensions.TypedDict, total=False
):
    ragCorpusId: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1Featurestore(typing_extensions.TypedDict, total=False):
    createTime: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    onlineServingConfig: GoogleCloudAiplatformV1FeaturestoreOnlineServingConfig
    onlineStorageTtlDays: int
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfig(
    typing_extensions.TypedDict, total=False
):
    categoricalThresholdConfig: (
        GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfig
    )
    importFeaturesAnalysis: (
        GoogleCloudAiplatformV1FeaturestoreMonitoringConfigImportFeaturesAnalysis
    )
    numericalThresholdConfig: (
        GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfig
    )
    snapshotAnalysis: (
        GoogleCloudAiplatformV1FeaturestoreMonitoringConfigSnapshotAnalysis
    )

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
    dataKey: GoogleCloudAiplatformV1FeatureViewDataKey
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
class GoogleCloudAiplatformV1FetchPredictOperationRequest(
    typing_extensions.TypedDict, total=False
):
    operationName: str

@typing.type_check_only
class GoogleCloudAiplatformV1FileData(typing_extensions.TypedDict, total=False):
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1FileStatus(typing_extensions.TypedDict, total=False):
    errorStatus: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "ERROR"]

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
    rrf: GoogleCloudAiplatformV1FindNeighborsRequestQueryRRF

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsRequestQueryRRF(
    typing_extensions.TypedDict, total=False
):
    alpha: float

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
    sparseDistance: float

@typing.type_check_only
class GoogleCloudAiplatformV1FluencyInput(typing_extensions.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1FluencyInstance
    metricSpec: GoogleCloudAiplatformV1FluencySpec

@typing.type_check_only
class GoogleCloudAiplatformV1FluencyInstance(typing_extensions.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1FluencyResult(typing_extensions.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1FluencySpec(typing_extensions.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1FractionSplit(typing_extensions.TypedDict, total=False):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentInput(typing_extensions.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1FulfillmentInstance
    metricSpec: GoogleCloudAiplatformV1FulfillmentSpec

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentInstance(
    typing_extensions.TypedDict, total=False
):
    instruction: str
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentSpec(typing_extensions.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionCall(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionCallingConfig(
    typing_extensions.TypedDict, total=False
):
    allowedFunctionNames: _list[str]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "ANY", "NONE"]

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionDeclaration(
    typing_extensions.TypedDict, total=False
):
    description: str
    name: str
    parameters: GoogleCloudAiplatformV1Schema
    response: GoogleCloudAiplatformV1Schema

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
    cachedContent: str
    contents: _list[GoogleCloudAiplatformV1Content]
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    labels: dict[str, typing.Any]
    safetySettings: _list[GoogleCloudAiplatformV1SafetySetting]
    systemInstruction: GoogleCloudAiplatformV1Content
    toolConfig: GoogleCloudAiplatformV1ToolConfig
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponse(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1Candidate]
    modelVersion: str
    promptFeedback: GoogleCloudAiplatformV1GenerateContentResponsePromptFeedback
    usageMetadata: GoogleCloudAiplatformV1GenerateContentResponseUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponsePromptFeedback(
    typing_extensions.TypedDict, total=False
):
    blockReason: typing_extensions.Literal[
        "BLOCKED_REASON_UNSPECIFIED",
        "SAFETY",
        "OTHER",
        "BLOCKLIST",
        "PROHIBITED_CONTENT",
    ]
    blockReasonMessage: str
    safetyRatings: _list[GoogleCloudAiplatformV1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponseUsageMetadata(
    typing_extensions.TypedDict, total=False
):
    cachedContentTokenCount: int
    candidatesTokenCount: int
    promptTokenCount: int
    totalTokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfig(typing_extensions.TypedDict, total=False):
    audioTimestamp: bool
    candidateCount: int
    frequencyPenalty: float
    logprobs: int
    maxOutputTokens: int
    mediaResolution: typing_extensions.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED",
        "MEDIA_RESOLUTION_LOW",
        "MEDIA_RESOLUTION_MEDIUM",
        "MEDIA_RESOLUTION_HIGH",
    ]
    presencePenalty: float
    responseLogprobs: bool
    responseMimeType: str
    responseModalities: _list[
        typing_extensions.Literal["MODALITY_UNSPECIFIED", "TEXT", "IMAGE", "AUDIO"]
    ]
    responseSchema: GoogleCloudAiplatformV1Schema
    routingConfig: GoogleCloudAiplatformV1GenerationConfigRoutingConfig
    seed: int
    speechConfig: GoogleCloudAiplatformV1SpeechConfig
    stopSequences: _list[str]
    temperature: float
    topK: float
    topP: float

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfigRoutingConfig(
    typing_extensions.TypedDict, total=False
):
    autoMode: GoogleCloudAiplatformV1GenerationConfigRoutingConfigAutoRoutingMode
    manualMode: GoogleCloudAiplatformV1GenerationConfigRoutingConfigManualRoutingMode

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfigRoutingConfigAutoRoutingMode(
    typing_extensions.TypedDict, total=False
):
    modelRoutingPreference: typing_extensions.Literal[
        "UNKNOWN", "PRIORITIZE_QUALITY", "BALANCED", "PRIORITIZE_COST"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfigRoutingConfigManualRoutingMode(
    typing_extensions.TypedDict, total=False
):
    modelName: str

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
class GoogleCloudAiplatformV1GoogleDriveSource(
    typing_extensions.TypedDict, total=False
):
    resourceIds: _list[GoogleCloudAiplatformV1GoogleDriveSourceResourceId]

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleDriveSourceResourceId(
    typing_extensions.TypedDict, total=False
):
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "RESOURCE_TYPE_FILE", "RESOURCE_TYPE_FOLDER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleSearchRetrieval(
    typing_extensions.TypedDict, total=False
):
    dynamicRetrievalConfig: GoogleCloudAiplatformV1DynamicRetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1GroundednessInstance
    metricSpec: GoogleCloudAiplatformV1GroundednessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessSpec(typing_extensions.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunk(typing_extensions.TypedDict, total=False):
    retrievedContext: GoogleCloudAiplatformV1GroundingChunkRetrievedContext
    web: GoogleCloudAiplatformV1GroundingChunkWeb

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkRetrievedContext(
    typing_extensions.TypedDict, total=False
):
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkWeb(
    typing_extensions.TypedDict, total=False
):
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingMetadata(
    typing_extensions.TypedDict, total=False
):
    groundingChunks: _list[GoogleCloudAiplatformV1GroundingChunk]
    groundingSupports: _list[GoogleCloudAiplatformV1GroundingSupport]
    retrievalMetadata: GoogleCloudAiplatformV1RetrievalMetadata
    searchEntryPoint: GoogleCloudAiplatformV1SearchEntryPoint
    webSearchQueries: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingSupport(typing_extensions.TypedDict, total=False):
    confidenceScores: _list[float]
    groundingChunkIndices: _list[int]
    segment: GoogleCloudAiplatformV1Segment

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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
class GoogleCloudAiplatformV1ImportRagFilesConfig(
    typing_extensions.TypedDict, total=False
):
    gcsSource: GoogleCloudAiplatformV1GcsSource
    googleDriveSource: GoogleCloudAiplatformV1GoogleDriveSource
    jiraSource: GoogleCloudAiplatformV1JiraSource
    maxEmbeddingRequestsPerMin: int
    partialFailureBigquerySink: GoogleCloudAiplatformV1BigQueryDestination
    partialFailureGcsSink: GoogleCloudAiplatformV1GcsDestination
    ragFileTransformationConfig: GoogleCloudAiplatformV1RagFileTransformationConfig
    sharePointSources: GoogleCloudAiplatformV1SharePointSources
    slackSource: GoogleCloudAiplatformV1SlackSource

@typing.type_check_only
class GoogleCloudAiplatformV1ImportRagFilesRequest(
    typing_extensions.TypedDict, total=False
):
    importRagFilesConfig: GoogleCloudAiplatformV1ImportRagFilesConfig

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
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapoint(typing_extensions.TypedDict, total=False):
    crowdingTag: GoogleCloudAiplatformV1IndexDatapointCrowdingTag
    datapointId: str
    featureVector: _list[float]
    numericRestricts: _list[GoogleCloudAiplatformV1IndexDatapointNumericRestriction]
    restricts: _list[GoogleCloudAiplatformV1IndexDatapointRestriction]
    sparseEmbedding: GoogleCloudAiplatformV1IndexDatapointSparseEmbedding

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
class GoogleCloudAiplatformV1IndexDatapointSparseEmbedding(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    values: _list[float]

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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    sparseVectorsCount: str
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
class GoogleCloudAiplatformV1JiraSource(typing_extensions.TypedDict, total=False):
    jiraQueries: _list[GoogleCloudAiplatformV1JiraSourceJiraQueries]

@typing.type_check_only
class GoogleCloudAiplatformV1JiraSourceJiraQueries(
    typing_extensions.TypedDict, total=False
):
    apiKeyConfig: GoogleCloudAiplatformV1ApiAuthApiKeyConfig
    customQueries: _list[str]
    email: str
    projects: _list[str]
    serverUri: str

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
class GoogleCloudAiplatformV1ListCachedContentsResponse(
    typing_extensions.TypedDict, total=False
):
    cachedContents: _list[GoogleCloudAiplatformV1CachedContent]
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
class GoogleCloudAiplatformV1ListNotebookExecutionJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notebookExecutionJobs: _list[GoogleCloudAiplatformV1NotebookExecutionJob]

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
class GoogleCloudAiplatformV1ListPersistentResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    persistentResources: _list[GoogleCloudAiplatformV1PersistentResource]

@typing.type_check_only
class GoogleCloudAiplatformV1ListPipelineJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pipelineJobs: _list[GoogleCloudAiplatformV1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1ListRagCorporaResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    ragCorpora: _list[GoogleCloudAiplatformV1RagCorpus]

@typing.type_check_only
class GoogleCloudAiplatformV1ListRagFilesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    ragFiles: _list[GoogleCloudAiplatformV1RagFile]

@typing.type_check_only
class GoogleCloudAiplatformV1ListReasoningEnginesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    reasoningEngines: _list[GoogleCloudAiplatformV1ReasoningEngine]

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
class GoogleCloudAiplatformV1ListTuningJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tuningJobs: _list[GoogleCloudAiplatformV1TuningJob]

@typing.type_check_only
class GoogleCloudAiplatformV1LogprobsResult(typing_extensions.TypedDict, total=False):
    chosenCandidates: _list[GoogleCloudAiplatformV1LogprobsResultCandidate]
    topCandidates: _list[GoogleCloudAiplatformV1LogprobsResultTopCandidates]

@typing.type_check_only
class GoogleCloudAiplatformV1LogprobsResultCandidate(
    typing_extensions.TypedDict, total=False
):
    logProbability: float
    token: str
    tokenId: int

@typing.type_check_only
class GoogleCloudAiplatformV1LogprobsResultTopCandidates(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1LogprobsResultCandidate]

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
        "NVIDIA_H100_MEGA_80GB",
        "TPU_V2",
        "TPU_V3",
        "TPU_V4_POD",
        "TPU_V5_LITEPOD",
    ]
    machineType: str
    reservationAffinity: GoogleCloudAiplatformV1ReservationAffinity
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
    dataplexConfig: GoogleCloudAiplatformV1MetadataStoreDataplexConfig
    description: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    name: str
    state: GoogleCloudAiplatformV1MetadataStoreMetadataStoreState
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStoreDataplexConfig(
    typing_extensions.TypedDict, total=False
):
    enabledPipelinesLineage: bool

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStoreMetadataStoreState(
    typing_extensions.TypedDict, total=False
):
    diskUtilizationBytes: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxInput(typing_extensions.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1MetricxInstance
    metricSpec: GoogleCloudAiplatformV1MetricxSpec

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxInstance(typing_extensions.TypedDict, total=False):
    prediction: str
    reference: str
    source: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxResult(typing_extensions.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxSpec(typing_extensions.TypedDict, total=False):
    sourceLanguage: str
    targetLanguage: str
    version: typing_extensions.Literal[
        "METRICX_VERSION_UNSPECIFIED",
        "METRICX_24_REF",
        "METRICX_24_SRC",
        "METRICX_24_SRC_REF",
    ]

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
    migrateAutomlDatasetConfig: (
        GoogleCloudAiplatformV1MigrateResourceRequestMigrateAutomlDatasetConfig
    )
    migrateAutomlModelConfig: (
        GoogleCloudAiplatformV1MigrateResourceRequestMigrateAutomlModelConfig
    )
    migrateDataLabelingDatasetConfig: (
        GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfig
    )
    migrateMlEngineModelVersionConfig: (
        GoogleCloudAiplatformV1MigrateResourceRequestMigrateMlEngineModelVersionConfig
    )

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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    livenessProbe: GoogleCloudAiplatformV1Probe
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
    modelDeploymentMonitoringScheduleConfig: (
        GoogleCloudAiplatformV1ModelDeploymentMonitoringScheduleConfig
    )
    modelMonitoringAlertConfig: GoogleCloudAiplatformV1ModelMonitoringAlertConfig
    name: str
    nextScheduleTime: str
    predictInstanceSchemaUri: str
    samplePredictInstance: typing.Any
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    explanationConfig: (
        GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfig
    )
    predictionDriftDetectionConfig: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig
    trainingDataset: (
        GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingDataset
    )
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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    searchTrialSpec: (
        GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec
    )
    trainTrialSpec: (
        GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec
    )

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
    numericFilters: _list[GoogleCloudAiplatformV1NearestNeighborQueryNumericFilter]
    parameters: GoogleCloudAiplatformV1NearestNeighborQueryParameters
    perCrowdingAttributeNeighborCount: int
    stringFilters: _list[GoogleCloudAiplatformV1NearestNeighborQueryStringFilter]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryEmbedding(
    typing_extensions.TypedDict, total=False
):
    value: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryNumericFilter(
    typing_extensions.TypedDict, total=False
):
    name: str
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
    invalidSparseRecordCount: str
    partialErrors: _list[
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataRecordError
    ]
    sourceGcsUri: str
    validRecordCount: str
    validSparseRecordCount: str

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
        "INVALID_SPARSE_DIMENSIONS",
        "INVALID_TOKEN_VALUE",
        "INVALID_SPARSE_EMBEDDING",
        "INVALID_EMBEDDING",
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
class GoogleCloudAiplatformV1NotebookExecutionJob(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    customEnvironmentSpec: (
        GoogleCloudAiplatformV1NotebookExecutionJobCustomEnvironmentSpec
    )
    dataformRepositorySource: (
        GoogleCloudAiplatformV1NotebookExecutionJobDataformRepositorySource
    )
    directNotebookSource: (
        GoogleCloudAiplatformV1NotebookExecutionJobDirectNotebookSource
    )
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    executionTimeout: str
    executionUser: str
    gcsNotebookSource: GoogleCloudAiplatformV1NotebookExecutionJobGcsNotebookSource
    gcsOutputUri: str
    jobState: typing_extensions.Literal[
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
    kernelName: str
    labels: dict[str, typing.Any]
    name: str
    notebookRuntimeTemplateResourceName: str
    scheduleResourceName: str
    serviceAccount: str
    status: GoogleRpcStatus
    updateTime: str
    workbenchRuntime: GoogleCloudAiplatformV1NotebookExecutionJobWorkbenchRuntime

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobCustomEnvironmentSpec(
    typing_extensions.TypedDict, total=False
):
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    networkSpec: GoogleCloudAiplatformV1NetworkSpec
    persistentDiskSpec: GoogleCloudAiplatformV1PersistentDiskSpec

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobDataformRepositorySource(
    typing_extensions.TypedDict, total=False
):
    commitSha: str
    dataformRepositoryResourceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobDirectNotebookSource(
    typing_extensions.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobGcsNotebookSource(
    typing_extensions.TypedDict, total=False
):
    generation: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobWorkbenchRuntime(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookIdleShutdownConfig(
    typing_extensions.TypedDict, total=False
):
    idleShutdownDisabled: bool
    idleTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntime(typing_extensions.TypedDict, total=False):
    createTime: str
    dataPersistentDiskSpec: GoogleCloudAiplatformV1PersistentDiskSpec
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    eucConfig: GoogleCloudAiplatformV1NotebookEucConfig
    expirationTime: str
    healthState: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED", "HEALTHY", "UNHEALTHY"
    ]
    idleShutdownConfig: GoogleCloudAiplatformV1NotebookIdleShutdownConfig
    isUpgradable: bool
    labels: dict[str, typing.Any]
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    name: str
    networkSpec: GoogleCloudAiplatformV1NetworkSpec
    networkTags: _list[str]
    notebookRuntimeTemplateRef: GoogleCloudAiplatformV1NotebookRuntimeTemplateRef
    notebookRuntimeType: typing_extensions.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    proxyUri: str
    runtimeState: typing_extensions.Literal[
        "RUNTIME_STATE_UNSPECIFIED",
        "RUNNING",
        "BEING_STARTED",
        "BEING_STOPPED",
        "STOPPED",
        "BEING_UPGRADED",
        "ERROR",
        "INVALID",
    ]
    runtimeUser: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceAccount: str
    shieldedVmConfig: GoogleCloudAiplatformV1ShieldedVmConfig
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
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
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
    serviceAccount: str
    shieldedVmConfig: GoogleCloudAiplatformV1ShieldedVmConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeTemplateRef(
    typing_extensions.TypedDict, total=False
):
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1PSCAutomationConfig(
    typing_extensions.TypedDict, total=False
):
    network: str
    projectId: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1PairwiseMetricInstance
    metricSpec: GoogleCloudAiplatformV1PairwiseMetricSpec

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricInstance(
    typing_extensions.TypedDict, total=False
):
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricResult(
    typing_extensions.TypedDict, total=False
):
    explanation: str
    pairwiseChoice: typing_extensions.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricSpec(
    typing_extensions.TypedDict, total=False
):
    metricPromptTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityInstance
    metricSpec: GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityInstance(
    typing_extensions.TypedDict, total=False
):
    baselinePrediction: str
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    pairwiseChoice: typing_extensions.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualitySpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualityInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1PairwiseSummarizationQualityInstance
    metricSpec: GoogleCloudAiplatformV1PairwiseSummarizationQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualityInstance(
    typing_extensions.TypedDict, total=False
):
    baselinePrediction: str
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualityResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    pairwiseChoice: typing_extensions.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualitySpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

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
class GoogleCloudAiplatformV1PersistentResource(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    network: str
    reservedIpRanges: _list[str]
    resourcePools: _list[GoogleCloudAiplatformV1ResourcePool]
    resourceRuntime: GoogleCloudAiplatformV1ResourceRuntime
    resourceRuntimeSpec: GoogleCloudAiplatformV1ResourceRuntimeSpec
    satisfiesPzi: bool
    satisfiesPzs: bool
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "STOPPING",
        "ERROR",
        "REBOOTING",
        "UPDATING",
    ]
    updateTime: str

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
    preflightValidations: bool
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
class GoogleCloudAiplatformV1PointwiseMetricInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1PointwiseMetricInstance
    metricSpec: GoogleCloudAiplatformV1PointwiseMetricSpec

@typing.type_check_only
class GoogleCloudAiplatformV1PointwiseMetricInstance(
    typing_extensions.TypedDict, total=False
):
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1PointwiseMetricResult(
    typing_extensions.TypedDict, total=False
):
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1PointwiseMetricSpec(
    typing_extensions.TypedDict, total=False
):
    metricPromptTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1Port(typing_extensions.TypedDict, total=False):
    containerPort: int

@typing.type_check_only
class GoogleCloudAiplatformV1PrebuiltVoiceConfig(
    typing_extensions.TypedDict, total=False
):
    voiceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1PredefinedSplit(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1PredictLongRunningRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[typing.Any]
    parameters: typing.Any

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
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1Probe(typing_extensions.TypedDict, total=False):
    exec: GoogleCloudAiplatformV1ProbeExecAction
    grpc: GoogleCloudAiplatformV1ProbeGrpcAction
    httpGet: GoogleCloudAiplatformV1ProbeHttpGetAction
    periodSeconds: int
    tcpSocket: GoogleCloudAiplatformV1ProbeTcpSocketAction
    timeoutSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeExecAction(typing_extensions.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeGrpcAction(typing_extensions.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeHttpGetAction(
    typing_extensions.TypedDict, total=False
):
    host: str
    httpHeaders: _list[GoogleCloudAiplatformV1ProbeHttpHeader]
    path: str
    port: int
    scheme: str

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeHttpHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeTcpSocketAction(
    typing_extensions.TypedDict, total=False
):
    host: str
    port: int

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
    createApplication: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    deploy: GoogleCloudAiplatformV1PublisherModelCallToActionDeploy
    deployGke: GoogleCloudAiplatformV1PublisherModelCallToActionDeployGke
    multiDeployVertex: GoogleCloudAiplatformV1PublisherModelCallToActionDeployVertex
    openEvaluationPipeline: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    openFineTuningPipeline: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    openFineTuningPipelines: (
        GoogleCloudAiplatformV1PublisherModelCallToActionOpenFineTuningPipelines
    )
    openGenerationAiStudio: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    openGenie: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    openNotebook: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    openNotebooks: GoogleCloudAiplatformV1PublisherModelCallToActionOpenNotebooks
    openPromptTuningPipeline: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    requestAccess: (
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    )
    viewRestApi: GoogleCloudAiplatformV1PublisherModelCallToActionViewRestApi

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeploy(
    typing_extensions.TypedDict, total=False
):
    artifactUri: str
    automaticResources: GoogleCloudAiplatformV1AutomaticResources
    containerSpec: GoogleCloudAiplatformV1ModelContainerSpec
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    deployMetadata: (
        GoogleCloudAiplatformV1PublisherModelCallToActionDeployDeployMetadata
    )
    deployTaskName: str
    largeModelReference: GoogleCloudAiplatformV1LargeModelReference
    modelDisplayName: str
    publicArtifactUri: str
    sharedResources: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeployDeployMetadata(
    typing_extensions.TypedDict, total=False
):
    labels: dict[str, typing.Any]
    sampleRequest: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeployGke(
    typing_extensions.TypedDict, total=False
):
    gkeYamlConfigs: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeployVertex(
    typing_extensions.TypedDict, total=False
):
    multiDeployVertex: _list[GoogleCloudAiplatformV1PublisherModelCallToActionDeploy]

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
class GoogleCloudAiplatformV1QueryReasoningEngineRequest(
    typing_extensions.TypedDict, total=False
):
    classMethod: str
    input: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1QueryReasoningEngineResponse(
    typing_extensions.TypedDict, total=False
):
    output: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringCorrectnessInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringCorrectnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessSpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessSpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualityInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringQualityInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualityInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualityResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualitySpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringRelevanceInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringRelevanceSpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceSpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagContexts(typing_extensions.TypedDict, total=False):
    contexts: _list[GoogleCloudAiplatformV1RagContextsContext]

@typing.type_check_only
class GoogleCloudAiplatformV1RagContextsContext(
    typing_extensions.TypedDict, total=False
):
    score: float
    sourceDisplayName: str
    sourceUri: str
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagCorpus(typing_extensions.TypedDict, total=False):
    corpusStatus: GoogleCloudAiplatformV1CorpusStatus
    createTime: str
    description: str
    displayName: str
    name: str
    updateTime: str
    vectorDbConfig: GoogleCloudAiplatformV1RagVectorDbConfig

@typing.type_check_only
class GoogleCloudAiplatformV1RagEmbeddingModelConfig(
    typing_extensions.TypedDict, total=False
):
    vertexPredictionEndpoint: (
        GoogleCloudAiplatformV1RagEmbeddingModelConfigVertexPredictionEndpoint
    )

@typing.type_check_only
class GoogleCloudAiplatformV1RagEmbeddingModelConfigVertexPredictionEndpoint(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagFile(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    directUploadSource: GoogleCloudAiplatformV1DirectUploadSource
    displayName: str
    fileStatus: GoogleCloudAiplatformV1FileStatus
    gcsSource: GoogleCloudAiplatformV1GcsSource
    googleDriveSource: GoogleCloudAiplatformV1GoogleDriveSource
    jiraSource: GoogleCloudAiplatformV1JiraSource
    name: str
    sharePointSources: GoogleCloudAiplatformV1SharePointSources
    slackSource: GoogleCloudAiplatformV1SlackSource
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    fixedLengthChunking: GoogleCloudAiplatformV1RagFileChunkingConfigFixedLengthChunking

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileChunkingConfigFixedLengthChunking(
    typing_extensions.TypedDict, total=False
):
    chunkOverlap: int
    chunkSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileTransformationConfig(
    typing_extensions.TypedDict, total=False
):
    ragFileChunkingConfig: GoogleCloudAiplatformV1RagFileChunkingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1RagQuery(typing_extensions.TypedDict, total=False):
    ragRetrievalConfig: GoogleCloudAiplatformV1RagRetrievalConfig
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagRetrievalConfig(
    typing_extensions.TypedDict, total=False
):
    filter: GoogleCloudAiplatformV1RagRetrievalConfigFilter
    topK: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagRetrievalConfigFilter(
    typing_extensions.TypedDict, total=False
):
    metadataFilter: str
    vectorDistanceThreshold: float
    vectorSimilarityThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfig(
    typing_extensions.TypedDict, total=False
):
    apiAuth: GoogleCloudAiplatformV1ApiAuth
    pinecone: GoogleCloudAiplatformV1RagVectorDbConfigPinecone
    ragEmbeddingModelConfig: GoogleCloudAiplatformV1RagEmbeddingModelConfig
    ragManagedDb: GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDb
    vertexVectorSearch: GoogleCloudAiplatformV1RagVectorDbConfigVertexVectorSearch

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigPinecone(
    typing_extensions.TypedDict, total=False
):
    indexName: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDb(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigVertexVectorSearch(
    typing_extensions.TypedDict, total=False
):
    index: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1RawPredictRequest(
    typing_extensions.TypedDict, total=False
):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1RayLogsSpec(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1RayMetricSpec(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1RaySpec(typing_extensions.TypedDict, total=False):
    headNodeResourcePoolId: str
    imageUri: str
    rayLogsSpec: GoogleCloudAiplatformV1RayLogsSpec
    rayMetricSpec: GoogleCloudAiplatformV1RayMetricSpec
    resourcePoolImages: dict[str, typing.Any]

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
class GoogleCloudAiplatformV1ReasoningEngine(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    name: str
    spec: GoogleCloudAiplatformV1ReasoningEngineSpec
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpec(
    typing_extensions.TypedDict, total=False
):
    classMethods: _list[dict[str, typing.Any]]
    packageSpec: GoogleCloudAiplatformV1ReasoningEngineSpecPackageSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecPackageSpec(
    typing_extensions.TypedDict, total=False
):
    dependencyFilesGcsUri: str
    pickleObjectGcsUri: str
    pythonVersion: str
    requirementsGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1RebaseTunedModelRequest(
    typing_extensions.TypedDict, total=False
):
    artifactDestination: GoogleCloudAiplatformV1GcsDestination
    deployToSameEndpoint: bool
    tunedModelRef: GoogleCloudAiplatformV1TunedModelRef
    tuningJob: GoogleCloudAiplatformV1TuningJob

@typing.type_check_only
class GoogleCloudAiplatformV1RebootPersistentResourceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1RebootPersistentResourceRequest(
    typing_extensions.TypedDict, total=False
): ...

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
class GoogleCloudAiplatformV1ReservationAffinity(
    typing_extensions.TypedDict, total=False
):
    key: str
    reservationAffinityType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ResourcePool(typing_extensions.TypedDict, total=False):
    autoscalingSpec: GoogleCloudAiplatformV1ResourcePoolAutoscalingSpec
    diskSpec: GoogleCloudAiplatformV1DiskSpec
    id: str
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    replicaCount: str
    usedReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ResourcePoolAutoscalingSpec(
    typing_extensions.TypedDict, total=False
):
    maxReplicaCount: str
    minReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ResourceRuntime(typing_extensions.TypedDict, total=False):
    accessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ResourceRuntimeSpec(
    typing_extensions.TypedDict, total=False
):
    raySpec: GoogleCloudAiplatformV1RaySpec
    serviceAccountSpec: GoogleCloudAiplatformV1ServiceAccountSpec

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
class GoogleCloudAiplatformV1Retrieval(typing_extensions.TypedDict, total=False):
    disableAttribution: bool
    vertexAiSearch: GoogleCloudAiplatformV1VertexAISearch
    vertexRagStore: GoogleCloudAiplatformV1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1RetrievalConfig(typing_extensions.TypedDict, total=False):
    languageCode: str
    latLng: GoogleTypeLatLng

@typing.type_check_only
class GoogleCloudAiplatformV1RetrievalMetadata(
    typing_extensions.TypedDict, total=False
):
    googleSearchDynamicRetrievalScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsRequest(
    typing_extensions.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1RagQuery
    vertexRagStore: GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStore(
    typing_extensions.TypedDict, total=False
):
    ragResources: _list[
        GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStoreRagResource
    ]
    vectorDistanceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStoreRagResource(
    typing_extensions.TypedDict, total=False
):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsResponse(
    typing_extensions.TypedDict, total=False
):
    contexts: GoogleCloudAiplatformV1RagContexts

@typing.type_check_only
class GoogleCloudAiplatformV1RougeInput(typing_extensions.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1RougeInstance]
    metricSpec: GoogleCloudAiplatformV1RougeSpec

@typing.type_check_only
class GoogleCloudAiplatformV1RougeInstance(typing_extensions.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1RougeMetricValue(typing_extensions.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1RougeResults(typing_extensions.TypedDict, total=False):
    rougeMetricValues: _list[GoogleCloudAiplatformV1RougeMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1RougeSpec(typing_extensions.TypedDict, total=False):
    rougeType: str
    splitSummaries: bool
    useStemmer: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyInput(typing_extensions.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1SafetyInstance
    metricSpec: GoogleCloudAiplatformV1SafetySpec

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyInstance(typing_extensions.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyRating(typing_extensions.TypedDict, total=False):
    blocked: bool
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
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
class GoogleCloudAiplatformV1SafetyResult(typing_extensions.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SafetySetting(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    method: typing_extensions.Literal[
        "HARM_BLOCK_METHOD_UNSPECIFIED", "SEVERITY", "PROBABILITY"
    ]
    threshold: typing_extensions.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SafetySpec(typing_extensions.TypedDict, total=False):
    version: int

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
    createNotebookExecutionJobRequest: (
        GoogleCloudAiplatformV1CreateNotebookExecutionJobRequest
    )
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
    maxWaitDuration: str
    restartJobOnWorkerRestart: bool
    strategy: typing_extensions.Literal[
        "STRATEGY_UNSPECIFIED",
        "ON_DEMAND",
        "LOW_COST",
        "STANDARD",
        "SPOT",
        "FLEX_START",
    ]
    timeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1Schema(typing_extensions.TypedDict, total=False):
    anyOf: _list[GoogleCloudAiplatformV1Schema]
    default: typing.Any
    description: str
    enum: _list[str]
    example: typing.Any
    format: str
    items: GoogleCloudAiplatformV1Schema
    maxItems: str
    maxLength: str
    maxProperties: str
    maximum: float
    minItems: str
    minLength: str
    minProperties: str
    minimum: float
    nullable: bool
    pattern: str
    properties: dict[str, typing.Any]
    propertyOrdering: _list[str]
    required: _list[str]
    title: str
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
    maskAnnotation: (
        GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationMaskAnnotation
    )
    polygonAnnotation: (
        GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolygonAnnotation
    )
    polylineAnnotation: (
        GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolylineAnnotation
    )

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
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsPairwiseTextGenerationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    accuracy: float
    baselineModelWinRate: float
    cohensKappa: float
    f1Score: float
    falseNegativeCount: str
    falsePositiveCount: str
    humanPreferenceBaselineModelWinRate: float
    humanPreferenceModelWinRate: float
    modelWinRate: float
    precision: float
    recall: float
    trueNegativeCount: str
    truePositiveCount: str

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
    tftFeatureImportance: (
        GoogleCloudAiplatformV1SchemaPredictPredictionTftFeatureImportance
    )
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
class GoogleCloudAiplatformV1SchemaPromptApiSchema(
    typing_extensions.TypedDict, total=False
):
    apiSchemaVersion: str
    executions: _list[GoogleCloudAiplatformV1SchemaPromptInstancePromptExecution]
    multimodalPrompt: GoogleCloudAiplatformV1SchemaPromptSpecMultimodalPrompt
    structuredPrompt: GoogleCloudAiplatformV1SchemaPromptSpecStructuredPrompt
    translationPrompt: GoogleCloudAiplatformV1SchemaPromptSpecTranslationPrompt

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptInstancePromptExecution(
    typing_extensions.TypedDict, total=False
):
    arguments: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptInstanceVariableValue(
    typing_extensions.TypedDict, total=False
):
    partList: GoogleCloudAiplatformV1SchemaPromptSpecPartList

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecMultimodalPrompt(
    typing_extensions.TypedDict, total=False
):
    promptMessage: GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecPartList(
    typing_extensions.TypedDict, total=False
):
    parts: _list[GoogleCloudAiplatformV1Part]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1Content]
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    model: str
    safetySettings: _list[GoogleCloudAiplatformV1SafetySetting]
    systemInstruction: GoogleCloudAiplatformV1Content
    toolConfig: GoogleCloudAiplatformV1ToolConfig
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecReferenceSentencePair(
    typing_extensions.TypedDict, total=False
):
    sourceSentence: str
    targetSentence: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecReferenceSentencePairList(
    typing_extensions.TypedDict, total=False
):
    referenceSentencePairs: _list[
        GoogleCloudAiplatformV1SchemaPromptSpecReferenceSentencePair
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecStructuredPrompt(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudAiplatformV1Content
    examples: _list[GoogleCloudAiplatformV1SchemaPromptSpecPartList]
    infillPrefix: str
    infillSuffix: str
    inputPrefixes: _list[str]
    outputPrefixes: _list[str]
    predictionInputs: _list[GoogleCloudAiplatformV1SchemaPromptSpecPartList]
    promptMessage: GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationExample(
    typing_extensions.TypedDict, total=False
):
    referenceSentencePairLists: _list[
        GoogleCloudAiplatformV1SchemaPromptSpecReferenceSentencePairList
    ]
    referenceSentencesFileInputs: _list[
        GoogleCloudAiplatformV1SchemaPromptSpecTranslationSentenceFileInput
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationFileInputSource(
    typing_extensions.TypedDict, total=False
):
    content: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationGcsInputSource(
    typing_extensions.TypedDict, total=False
):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationOption(
    typing_extensions.TypedDict, total=False
):
    numberOfShots: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationPrompt(
    typing_extensions.TypedDict, total=False
):
    example: GoogleCloudAiplatformV1SchemaPromptSpecTranslationExample
    option: GoogleCloudAiplatformV1SchemaPromptSpecTranslationOption
    promptMessage: GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationSentenceFileInput(
    typing_extensions.TypedDict, total=False
):
    fileInputSource: GoogleCloudAiplatformV1SchemaPromptSpecTranslationFileInputSource
    gcsInputSource: GoogleCloudAiplatformV1SchemaPromptSpecTranslationGcsInputSource

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
    hasPromptVariable: bool
    logprobs: bool
    maxOutputTokens: str
    note: str
    promptApiSchema: GoogleCloudAiplatformV1SchemaPromptApiSchema
    promptType: str
    seedEnabled: bool
    seedValue: str
    stopSequences: _list[str]
    systemInstruction: str
    systemInstructionGcsUri: str
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
    metadata: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity
    enableProbabilisticInference: bool
    exportEvaluatedDataItemsConfig: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    )
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
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs
    )
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
    exportEvaluatedDataItemsConfig: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    )
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
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs
    )

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
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec
    )
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs
    )
    metadata: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    )
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
    exportEvaluatedDataItemsConfig: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    )
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
class GoogleCloudAiplatformV1SearchEntryPoint(typing_extensions.TypedDict, total=False):
    renderedContent: str
    sdkBlob: str

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
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1ServiceAccountSpec(
    typing_extensions.TypedDict, total=False
):
    enableCustomServiceAccount: bool
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1SharePointSources(
    typing_extensions.TypedDict, total=False
):
    sharePointSources: _list[GoogleCloudAiplatformV1SharePointSourcesSharePointSource]

@typing.type_check_only
class GoogleCloudAiplatformV1SharePointSourcesSharePointSource(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    clientSecret: GoogleCloudAiplatformV1ApiAuthApiKeyConfig
    driveId: str
    driveName: str
    fileId: str
    sharepointFolderId: str
    sharepointFolderPath: str
    sharepointSiteName: str
    tenantId: str

@typing.type_check_only
class GoogleCloudAiplatformV1ShieldedVmConfig(typing_extensions.TypedDict, total=False):
    enableSecureBoot: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SlackSource(typing_extensions.TypedDict, total=False):
    channels: _list[GoogleCloudAiplatformV1SlackSourceSlackChannels]

@typing.type_check_only
class GoogleCloudAiplatformV1SlackSourceSlackChannels(
    typing_extensions.TypedDict, total=False
):
    apiKeyConfig: GoogleCloudAiplatformV1ApiAuthApiKeyConfig
    channels: _list[GoogleCloudAiplatformV1SlackSourceSlackChannelsSlackChannel]

@typing.type_check_only
class GoogleCloudAiplatformV1SlackSourceSlackChannelsSlackChannel(
    typing_extensions.TypedDict, total=False
):
    channelId: str
    endTime: str
    startTime: str

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
class GoogleCloudAiplatformV1SpeechConfig(typing_extensions.TypedDict, total=False):
    voiceConfig: GoogleCloudAiplatformV1VoiceConfig

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
class GoogleCloudAiplatformV1StopNotebookRuntimeRequest(
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
class GoogleCloudAiplatformV1StreamQueryReasoningEngineRequest(
    typing_extensions.TypedDict, total=False
):
    classMethod: str
    input: dict[str, typing.Any]

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
class GoogleCloudAiplatformV1StructFieldValue(typing_extensions.TypedDict, total=False):
    name: str
    value: GoogleCloudAiplatformV1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1StructValue(typing_extensions.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1StructFieldValue]

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
    convexAutomatedStoppingSpec: (
        GoogleCloudAiplatformV1StudySpecConvexAutomatedStoppingSpec
    )
    decayCurveStoppingSpec: (
        GoogleCloudAiplatformV1StudySpecDecayCurveAutomatedStoppingSpec
    )
    measurementSelectionType: typing_extensions.Literal[
        "MEASUREMENT_SELECTION_TYPE_UNSPECIFIED", "LAST_MEASUREMENT", "BEST_MEASUREMENT"
    ]
    medianAutomatedStoppingSpec: (
        GoogleCloudAiplatformV1StudySpecMedianAutomatedStoppingSpec
    )
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
    categoricalValueSpec: (
        GoogleCloudAiplatformV1StudySpecParameterSpecCategoricalValueSpec
    )
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
class GoogleCloudAiplatformV1SummarizationHelpfulnessInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1SummarizationHelpfulnessInstance
    metricSpec: GoogleCloudAiplatformV1SummarizationHelpfulnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationHelpfulnessInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationHelpfulnessResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationHelpfulnessSpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualityInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1SummarizationQualityInstance
    metricSpec: GoogleCloudAiplatformV1SummarizationQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualityInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualityResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualitySpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbosityInput(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1SummarizationVerbosityInstance
    metricSpec: GoogleCloudAiplatformV1SummarizationVerbositySpec

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbosityInstance(
    typing_extensions.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbosityResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbositySpec(
    typing_extensions.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedHyperParameters(
    typing_extensions.TypedDict, total=False
):
    adapterSize: typing_extensions.Literal[
        "ADAPTER_SIZE_UNSPECIFIED",
        "ADAPTER_SIZE_ONE",
        "ADAPTER_SIZE_FOUR",
        "ADAPTER_SIZE_EIGHT",
        "ADAPTER_SIZE_SIXTEEN",
        "ADAPTER_SIZE_THIRTY_TWO",
    ]
    epochCount: str
    learningRateMultiplier: float

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedTuningDataStats(
    typing_extensions.TypedDict, total=False
):
    droppedExampleReasons: _list[str]
    totalBillableCharacterCount: str
    totalBillableTokenCount: str
    totalTruncatedExampleCount: str
    totalTuningCharacterCount: str
    truncatedExampleIndices: _list[str]
    tuningDatasetExampleCount: str
    tuningStepCount: str
    userDatasetExamples: _list[GoogleCloudAiplatformV1Content]
    userInputTokenDistribution: (
        GoogleCloudAiplatformV1SupervisedTuningDatasetDistribution
    )
    userMessagePerExampleDistribution: (
        GoogleCloudAiplatformV1SupervisedTuningDatasetDistribution
    )
    userOutputTokenDistribution: (
        GoogleCloudAiplatformV1SupervisedTuningDatasetDistribution
    )

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedTuningDatasetDistribution(
    typing_extensions.TypedDict, total=False
):
    billableSum: str
    buckets: _list[
        GoogleCloudAiplatformV1SupervisedTuningDatasetDistributionDatasetBucket
    ]
    max: float
    mean: float
    median: float
    min: float
    p5: float
    p95: float
    sum: str

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedTuningDatasetDistributionDatasetBucket(
    typing_extensions.TypedDict, total=False
):
    count: float
    left: float
    right: float

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedTuningSpec(
    typing_extensions.TypedDict, total=False
):
    hyperParameters: GoogleCloudAiplatformV1SupervisedHyperParameters
    trainingDatasetUri: str
    validationDatasetUri: str

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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    role: str
    tokenIds: _list[str]
    tokens: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1Tool(typing_extensions.TypedDict, total=False):
    functionDeclarations: _list[GoogleCloudAiplatformV1FunctionDeclaration]
    googleSearch: GoogleCloudAiplatformV1ToolGoogleSearch
    googleSearchRetrieval: GoogleCloudAiplatformV1GoogleSearchRetrieval
    retrieval: GoogleCloudAiplatformV1Retrieval

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCall(typing_extensions.TypedDict, total=False):
    toolInput: str
    toolName: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1ToolCallValidInstance]
    metricSpec: GoogleCloudAiplatformV1ToolCallValidSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidInstance(
    typing_extensions.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidResults(
    typing_extensions.TypedDict, total=False
):
    toolCallValidMetricValues: _list[GoogleCloudAiplatformV1ToolCallValidMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolConfig(typing_extensions.TypedDict, total=False):
    functionCallingConfig: GoogleCloudAiplatformV1FunctionCallingConfig
    retrievalConfig: GoogleCloudAiplatformV1RetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ToolGoogleSearch(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1ToolNameMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ToolNameMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchInstance(
    typing_extensions.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchResults(
    typing_extensions.TypedDict, total=False
):
    toolNameMatchMetricValues: _list[GoogleCloudAiplatformV1ToolNameMatchMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1ToolParameterKVMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ToolParameterKVMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchInstance(
    typing_extensions.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchResults(
    typing_extensions.TypedDict, total=False
):
    toolParameterKvMatchMetricValues: _list[
        GoogleCloudAiplatformV1ToolParameterKVMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchSpec(
    typing_extensions.TypedDict, total=False
):
    useStrictStringMatch: bool

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1ToolParameterKeyMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ToolParameterKeyMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchInstance(
    typing_extensions.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchResults(
    typing_extensions.TypedDict, total=False
):
    toolParameterKeyMatchMetricValues: _list[
        GoogleCloudAiplatformV1ToolParameterKeyMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchSpec(
    typing_extensions.TypedDict, total=False
): ...

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
class GoogleCloudAiplatformV1Trajectory(typing_extensions.TypedDict, total=False):
    toolCalls: _list[GoogleCloudAiplatformV1ToolCall]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectoryAnyOrderMatchInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryAnyOrderMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchInstance(
    typing_extensions.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchResults(
    typing_extensions.TypedDict, total=False
):
    trajectoryAnyOrderMatchMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryAnyOrderMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectoryExactMatchInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryExactMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchInstance(
    typing_extensions.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchResults(
    typing_extensions.TypedDict, total=False
):
    trajectoryExactMatchMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryExactMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectoryInOrderMatchInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryInOrderMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchInstance(
    typing_extensions.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchResults(
    typing_extensions.TypedDict, total=False
):
    trajectoryInOrderMatchMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryInOrderMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectoryPrecisionInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryPrecisionSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionInstance(
    typing_extensions.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionResults(
    typing_extensions.TypedDict, total=False
):
    trajectoryPrecisionMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryPrecisionMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectoryRecallInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryRecallSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallInstance(
    typing_extensions.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallResults(
    typing_extensions.TypedDict, total=False
):
    trajectoryRecallMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryRecallMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseInput(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectorySingleToolUseInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectorySingleToolUseSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseInstance(
    typing_extensions.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseMetricValue(
    typing_extensions.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseResults(
    typing_extensions.TypedDict, total=False
):
    trajectorySingleToolUseMetricValues: _list[
        GoogleCloudAiplatformV1TrajectorySingleToolUseMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseSpec(
    typing_extensions.TypedDict, total=False
):
    toolName: str

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
class GoogleCloudAiplatformV1TunedModel(typing_extensions.TypedDict, total=False):
    endpoint: str
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1TunedModelRef(typing_extensions.TypedDict, total=False):
    pipelineJob: str
    tunedModel: str
    tuningJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1TuningDataStats(typing_extensions.TypedDict, total=False):
    supervisedTuningDataStats: GoogleCloudAiplatformV1SupervisedTuningDataStats

@typing.type_check_only
class GoogleCloudAiplatformV1TuningJob(typing_extensions.TypedDict, total=False):
    baseModel: str
    createTime: str
    description: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    experiment: str
    labels: dict[str, typing.Any]
    name: str
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
    supervisedTuningSpec: GoogleCloudAiplatformV1SupervisedTuningSpec
    tunedModel: GoogleCloudAiplatformV1TunedModel
    tunedModelDisplayName: str
    tuningDataStats: GoogleCloudAiplatformV1TuningDataStats
    updateTime: str

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
class GoogleCloudAiplatformV1UpdateEndpointLongRunningRequest(
    typing_extensions.TypedDict, total=False
):
    endpoint: GoogleCloudAiplatformV1Endpoint

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
    nearestNeighborSearchOperationMetadata: (
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateModelDeploymentMonitoringJobOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdatePersistentResourceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

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
class GoogleCloudAiplatformV1UploadRagFileConfig(
    typing_extensions.TypedDict, total=False
):
    ragFileTransformationConfig: GoogleCloudAiplatformV1RagFileTransformationConfig

@typing.type_check_only
class GoogleCloudAiplatformV1UploadRagFileRequest(
    typing_extensions.TypedDict, total=False
):
    ragFile: GoogleCloudAiplatformV1RagFile
    uploadRagFileConfig: GoogleCloudAiplatformV1UploadRagFileConfig

@typing.type_check_only
class GoogleCloudAiplatformV1UploadRagFileResponse(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpcStatus
    ragFile: GoogleCloudAiplatformV1RagFile

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
class GoogleCloudAiplatformV1VertexAISearch(typing_extensions.TypedDict, total=False):
    datastore: str

@typing.type_check_only
class GoogleCloudAiplatformV1VertexRagStore(typing_extensions.TypedDict, total=False):
    ragResources: _list[GoogleCloudAiplatformV1VertexRagStoreRagResource]
    ragRetrievalConfig: GoogleCloudAiplatformV1RagRetrievalConfig
    similarityTopK: int
    vectorDistanceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1VertexRagStoreRagResource(
    typing_extensions.TypedDict, total=False
):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1VideoMetadata(typing_extensions.TypedDict, total=False):
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1VoiceConfig(typing_extensions.TypedDict, total=False):
    prebuiltVoiceConfig: GoogleCloudAiplatformV1PrebuiltVoiceConfig

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
class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
