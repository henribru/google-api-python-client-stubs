import typing

_list = list

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperiments(typing.TypedDict, total=False):
    anchorLastFrame: bool
    audioControl: CloudAiLargeModelsVisionGenerateVideoExperimentsAudioControlConfig
    cfgScale: float
    codec: typing.Literal[
        "VIDEO_CODEC_UNSPECIFIED",
        "VIDEO_CODEC_H264",
        "VIDEO_CODEC_PRORES",
        "VIDEO_CODEC_DNXHR",
    ]
    colorAlignment: CloudAiLargeModelsVisionGenerateVideoExperimentsColorAlignmentConfig
    conditioningFrames: _list[
        CloudAiLargeModelsVisionGenerateVideoExperimentsConditioningFrame
    ]
    customParameters: dict[str, typing.Any]
    exrColorSpaceOverride: str
    humanPose: CloudAiLargeModelsVisionHumanPose
    modelName: str
    numDiffusionSteps: int
    omniRewriter: CloudAiLargeModelsVisionGenerateVideoExperimentsOmniRewriterConfig
    originalRequestJson: str
    outpaintConfig: CloudAiLargeModelsVisionGenerateVideoExperimentsOutpaintConfig
    promptInputs: CloudAiLargeModelsVisionPromptInputs
    requestOriginTag: str
    schedulingConfig: CloudAiLargeModelsVisionGenerateVideoExperimentsVESchedulingConfig
    seamless: CloudAiLargeModelsVisionSeamless
    spatialAlignment: (
        CloudAiLargeModelsVisionGenerateVideoExperimentsSpatialAlignmentConfig
    )
    truncateInputVideo: bool
    videoTransform: CloudAiLargeModelsVisionGenerateVideoExperimentsVideoTransform
    videoTransformMaskGcsUri: str
    videoTransformStrength: float

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsAudioControlConfig(
    typing.TypedDict, total=False
):
    targetAudio: CloudAiLargeModelsVisionGenerateVideoRequestAudio
    useTargetAudioFromVideo: bool

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsColorAlignmentConfig(
    typing.TypedDict, total=False
):
    enable: bool

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsConditioningFrame(
    typing.TypedDict, total=False
):
    frameNum: int
    image: CloudAiLargeModelsVisionGenerateVideoRequestImage

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsOmniRewriterConfig(
    typing.TypedDict, total=False
):
    maxChunkDuration: float
    rewriterInputFps: int

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsOutpaintConfig(
    typing.TypedDict, total=False
):
    inputFrames: _list[
        CloudAiLargeModelsVisionGenerateVideoExperimentsOutpaintConfigFrameSource
    ]
    outputSpec: typing.Literal[
        "OUTPUT_SPEC_UNSPECIFIED",
        "OUTPUT_SPEC_1920X1072x72",
        "OUTPUT_SPEC_1280X720x192",
        "OUTPUT_SPEC_960X544x432",
    ]

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsOutpaintConfigFrameSource(
    typing.TypedDict, total=False
):
    globPattern: str
    horizontalOffset: int
    verticalOffset: int

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsSpatialAlignmentConfig(
    typing.TypedDict, total=False
):
    enable: bool

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsVESchedulingConfig(
    typing.TypedDict, total=False
):
    enableRetry: bool

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoExperimentsVideoTransform(
    typing.TypedDict, total=False
):
    initializationVideo: CloudAiLargeModelsVisionGenerateVideoRequestVideo
    mask: CloudAiLargeModelsVisionGenerateVideoRequestVideo
    noiseStrength: float

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoRequestAudio(typing.TypedDict, total=False):
    blobId: str
    bytesBase64Encoded: str
    gcsUri: str
    mimeType: str

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoRequestImage(typing.TypedDict, total=False):
    blobId: str
    bytesBase64Encoded: str
    gcsUri: str
    mimeType: str

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoRequestVideo(typing.TypedDict, total=False):
    blobId: str
    bytesBase64Encoded: str
    gcsUri: str
    mimeType: str

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoResponse(typing.TypedDict, total=False):
    generatedSamples: _list[CloudAiLargeModelsVisionMedia]
    raiMediaFilteredCount: int
    raiMediaFilteredReasons: _list[str]
    videos: _list[CloudAiLargeModelsVisionGenerateVideoResponseVideo]

@typing.type_check_only
class CloudAiLargeModelsVisionGenerateVideoResponseVideo(typing.TypedDict, total=False):
    bytesBase64Encoded: str
    experimentsMetadata: CloudAiLargeModelsVisionGenerateVideoExperiments
    gcsUri: str
    mimeType: str

@typing.type_check_only
class CloudAiLargeModelsVisionHumanPose(typing.TypedDict, total=False):
    bodyLandmarksGcsUri: str
    faceLandmarksGcsUri: str
    perfMeshGcsUri: str

@typing.type_check_only
class CloudAiLargeModelsVisionImage(typing.TypedDict, total=False):
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
class CloudAiLargeModelsVisionImageImageSize(typing.TypedDict, total=False):
    channels: int
    height: int
    width: int

@typing.type_check_only
class CloudAiLargeModelsVisionImageRAIScores(typing.TypedDict, total=False):
    agileWatermarkDetectionScore: float

@typing.type_check_only
class CloudAiLargeModelsVisionMedia(typing.TypedDict, total=False):
    image: CloudAiLargeModelsVisionImage
    video: CloudAiLargeModelsVisionVideo

@typing.type_check_only
class CloudAiLargeModelsVisionNamedBoundingBox(typing.TypedDict, total=False):
    classes: _list[str]
    entities: _list[str]
    scores: _list[float]
    x1: float
    x2: float
    y1: float
    y2: float

@typing.type_check_only
class CloudAiLargeModelsVisionPromptInputs(typing.TypedDict, total=False):
    audioPrompt: str
    negativeAudioPrompt: str
    negativePrompt: str
    promptChunks: _list[str]
    transcript: str

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfo(typing.TypedDict, total=False):
    blockedEntities: _list[str]
    detectedLabels: _list[CloudAiLargeModelsVisionRaiInfoDetectedLabels]
    modelName: str
    raiCategories: _list[str]
    scores: _list[float]

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfoDetectedLabels(typing.TypedDict, total=False):
    entities: _list[CloudAiLargeModelsVisionRaiInfoDetectedLabelsEntity]
    raiCategory: str

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfoDetectedLabelsBoundingBox(
    typing.TypedDict, total=False
):
    x1: int
    x2: int
    y1: int
    y2: int

@typing.type_check_only
class CloudAiLargeModelsVisionRaiInfoDetectedLabelsEntity(
    typing.TypedDict, total=False
):
    boundingBox: CloudAiLargeModelsVisionRaiInfoDetectedLabelsBoundingBox
    description: str
    iouScore: float
    mid: str
    score: float

@typing.type_check_only
class CloudAiLargeModelsVisionSeamless(typing.TypedDict, total=False):
    loop: bool
    tessellateHorizontal: bool
    tessellateVertical: bool

@typing.type_check_only
class CloudAiLargeModelsVisionSemanticFilterResponse(typing.TypedDict, total=False):
    namedBoundingBoxes: _list[CloudAiLargeModelsVisionNamedBoundingBox]
    passedSemanticFilter: bool

@typing.type_check_only
class CloudAiLargeModelsVisionVideo(typing.TypedDict, total=False):
    encodedVideo: str
    encoding: str
    text: str
    uri: str
    video: str

@typing.type_check_only
class CloudAiPlatformCommonCreatePipelineJobApiErrorDetail(
    typing.TypedDict, total=False
):
    errorCause: typing.Literal[
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
class GoogleApiHttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1ActivateOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ActivateOnlineEvaluatorRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ActiveLearningConfig(typing.TypedDict, total=False):
    maxDataItemCount: str
    maxDataItemPercentage: int
    sampleConfig: GoogleCloudAiplatformV1SampleConfig
    trainingConfig: GoogleCloudAiplatformV1TrainingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest(
    typing.TypedDict, total=False
):
    artifacts: _list[str]
    executions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextChildrenRequest(typing.TypedDict, total=False):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextChildrenResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddExecutionEventsRequest(typing.TypedDict, total=False):
    events: _list[GoogleCloudAiplatformV1Event]

@typing.type_check_only
class GoogleCloudAiplatformV1AddExecutionEventsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddTrialMeasurementRequest(typing.TypedDict, total=False):
    measurement: GoogleCloudAiplatformV1Measurement

@typing.type_check_only
class GoogleCloudAiplatformV1Agent(typing.TypedDict, total=False):
    base_agent: str
    base_environment: typing.Any
    created: str
    description: str
    id: str
    metadata: dict[str, typing.Any]
    name: str
    object: str
    system_instruction: str
    tools: _list[GoogleCloudAiplatformV1AgentTool]
    updated: str

@typing.type_check_only
class GoogleCloudAiplatformV1AgentConfig(typing.TypedDict, total=False):
    agentId: str
    agentType: str
    description: str
    instruction: str
    subAgents: _list[str]
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1AgentData(typing.TypedDict, total=False):
    agents: dict[str, typing.Any]
    turns: _list[GoogleCloudAiplatformV1ConversationTurn]

@typing.type_check_only
class GoogleCloudAiplatformV1AgentEvent(typing.TypedDict, total=False):
    activeTools: _list[GoogleCloudAiplatformV1Tool]
    author: str
    content: GoogleCloudAiplatformV1Content
    eventTime: str
    stateDelta: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1AgentTool(typing.TypedDict, total=False):
    headers: dict[str, typing.Any]
    name: str
    type: str
    url: str

@typing.type_check_only
class GoogleCloudAiplatformV1AggregationOutput(typing.TypedDict, total=False):
    aggregationResults: _list[GoogleCloudAiplatformV1AggregationResult]
    dataset: GoogleCloudAiplatformV1EvaluationDataset

@typing.type_check_only
class GoogleCloudAiplatformV1AggregationResult(typing.TypedDict, total=False):
    aggregationMetric: typing.Literal[
        "AGGREGATION_METRIC_UNSPECIFIED",
        "AVERAGE",
        "MODE",
        "STANDARD_DEVIATION",
        "VARIANCE",
        "MINIMUM",
        "MAXIMUM",
        "MEDIAN",
        "PERCENTILE_P90",
        "PERCENTILE_P95",
        "PERCENTILE_P99",
    ]
    bleuMetricValue: GoogleCloudAiplatformV1BleuMetricValue
    customCodeExecutionResult: GoogleCloudAiplatformV1CustomCodeExecutionResult
    exactMatchMetricValue: GoogleCloudAiplatformV1ExactMatchMetricValue
    pairwiseMetricResult: GoogleCloudAiplatformV1PairwiseMetricResult
    pointwiseMetricResult: GoogleCloudAiplatformV1PointwiseMetricResult
    rougeMetricValue: GoogleCloudAiplatformV1RougeMetricValue

@typing.type_check_only
class GoogleCloudAiplatformV1Annotation(typing.TypedDict, total=False):
    annotationSource: GoogleCloudAiplatformV1UserActionReference
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    payloadSchemaUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1AnnotationSpec(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ApiAuth(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1ApiAuthApiKeyConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ApiAuthApiKeyConfig(typing.TypedDict, total=False):
    apiKeySecretVersion: str
    apiKeyString: str

@typing.type_check_only
class GoogleCloudAiplatformV1AppendEventResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1Artifact(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    schemaTitle: str
    schemaVersion: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "LIVE"]
    updateTime: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1AskContextsRequest(typing.TypedDict, total=False):
    query: GoogleCloudAiplatformV1RagQuery
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1AskContextsResponse(typing.TypedDict, total=False):
    contexts: GoogleCloudAiplatformV1RagContexts
    response: str

@typing.type_check_only
class GoogleCloudAiplatformV1AssignNotebookRuntimeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1AssignNotebookRuntimeRequest(
    typing.TypedDict, total=False
):
    notebookRuntime: GoogleCloudAiplatformV1NotebookRuntime
    notebookRuntimeId: str
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1AsyncQueryReasoningEngineRequest(
    typing.TypedDict, total=False
):
    inputGcsUri: str
    outputGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1AsyncRetrieveContextsRequest(
    typing.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1RagQuery
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1Attribution(typing.TypedDict, total=False):
    approximationError: float
    baselineOutputValue: float
    featureAttributions: typing.Any
    instanceOutputValue: float
    outputDisplayName: str
    outputIndex: _list[int]
    outputName: str

@typing.type_check_only
class GoogleCloudAiplatformV1AudioResponseFormat(typing.TypedDict, total=False):
    bitRate: int
    delivery: typing.Literal["DELIVERY_UNSPECIFIED", "INLINE", "URI"]
    mimeType: typing.Literal[
        "MIME_TYPE_UNSPECIFIED",
        "AUDIO_MP3",
        "AUDIO_OGG_OPUS",
        "AUDIO_L16",
        "AUDIO_WAV",
        "AUDIO_ALAW",
        "AUDIO_MULAW",
    ]
    sampleRate: int

@typing.type_check_only
class GoogleCloudAiplatformV1AudioTranscription(typing.TypedDict, total=False):
    speakerLabel: str
    text: str
    words: _list[GoogleCloudAiplatformV1AudioTranscriptionWordInfo]

@typing.type_check_only
class GoogleCloudAiplatformV1AudioTranscriptionConfig(typing.TypedDict, total=False):
    adaptationPhrases: _list[str]
    customVocabulary: _list[str]
    diarization: bool
    languageAuto: GoogleCloudAiplatformV1AudioTranscriptionConfigLanguageAuto
    languageCodes: _list[str]
    languageHints: GoogleCloudAiplatformV1AudioTranscriptionConfigLanguageHints
    wordTimestamp: bool

@typing.type_check_only
class GoogleCloudAiplatformV1AudioTranscriptionConfigLanguageAuto(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1AudioTranscriptionConfigLanguageHints(
    typing.TypedDict, total=False
):
    languageCodes: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1AudioTranscriptionWordInfo(typing.TypedDict, total=False):
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudAiplatformV1AugmentPromptRequest(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1Content]
    model: GoogleCloudAiplatformV1AugmentPromptRequestModel
    vertexRagStore: GoogleCloudAiplatformV1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1AugmentPromptRequestModel(typing.TypedDict, total=False):
    model: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1AugmentPromptResponse(typing.TypedDict, total=False):
    augmentedPrompt: _list[GoogleCloudAiplatformV1Content]
    facts: _list[GoogleCloudAiplatformV1Fact]

@typing.type_check_only
class GoogleCloudAiplatformV1AuthConfig(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1AuthConfigApiKeyConfig
    authType: typing.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "NO_AUTH",
        "API_KEY_AUTH",
        "HTTP_BASIC_AUTH",
        "GOOGLE_SERVICE_ACCOUNT_AUTH",
        "OAUTH",
        "OIDC_AUTH",
    ]
    googleServiceAccountConfig: (
        GoogleCloudAiplatformV1AuthConfigGoogleServiceAccountConfig
    )
    httpBasicAuthConfig: GoogleCloudAiplatformV1AuthConfigHttpBasicAuthConfig
    oauthConfig: GoogleCloudAiplatformV1AuthConfigOauthConfig
    oidcConfig: GoogleCloudAiplatformV1AuthConfigOidcConfig

@typing.type_check_only
class GoogleCloudAiplatformV1AuthConfigApiKeyConfig(typing.TypedDict, total=False):
    apiKeySecret: str
    apiKeyString: str
    httpElementLocation: typing.Literal[
        "HTTP_IN_UNSPECIFIED",
        "HTTP_IN_QUERY",
        "HTTP_IN_HEADER",
        "HTTP_IN_PATH",
        "HTTP_IN_BODY",
        "HTTP_IN_COOKIE",
    ]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1AuthConfigGoogleServiceAccountConfig(
    typing.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1AuthConfigHttpBasicAuthConfig(
    typing.TypedDict, total=False
):
    credentialSecret: str

@typing.type_check_only
class GoogleCloudAiplatformV1AuthConfigOauthConfig(typing.TypedDict, total=False):
    accessToken: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1AuthConfigOidcConfig(typing.TypedDict, total=False):
    idToken: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1AutomaticResources(typing.TypedDict, total=False):
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1AutoraterConfig(typing.TypedDict, total=False):
    autoraterModel: str
    flipEnabled: bool
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    samplingCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1AutoscalingMetricSpec(typing.TypedDict, total=False):
    metricName: str
    target: int

@typing.type_check_only
class GoogleCloudAiplatformV1AvroSource(typing.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCancelPipelineJobsRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateFeaturesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateFeaturesRequest(typing.TypedDict, total=False):
    requests: _list[GoogleCloudAiplatformV1CreateFeatureRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateFeaturesResponse(typing.TypedDict, total=False):
    features: _list[GoogleCloudAiplatformV1Feature]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1CreateTensorboardRunRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse(
    typing.TypedDict, total=False
):
    tensorboardRuns: _list[GoogleCloudAiplatformV1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1CreateTensorboardTimeSeriesRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse(
    typing.TypedDict, total=False
):
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchDedicatedResources(typing.TypedDict, total=False):
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    maxReplicaCount: int
    startingReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1BatchDeletePipelineJobsRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest(
    typing.TypedDict, total=False
):
    evaluatedAnnotations: _list[GoogleCloudAiplatformV1EvaluatedAnnotation]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse(
    typing.TypedDict, total=False
):
    importedEvaluatedAnnotationsCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportModelEvaluationSlicesRequest(
    typing.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1ModelEvaluationSlice]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportModelEvaluationSlicesResponse(
    typing.TypedDict, total=False
):
    importedModelEvaluationSlices: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    partialResults: _list[
        GoogleCloudAiplatformV1BatchMigrateResourcesOperationMetadataPartialResult
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesOperationMetadataPartialResult(
    typing.TypedDict, total=False
):
    dataset: str
    error: GoogleRpcStatus
    model: str
    request: GoogleCloudAiplatformV1MigrateResourceRequest

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesRequest(
    typing.TypedDict, total=False
):
    migrateResourceRequests: _list[GoogleCloudAiplatformV1MigrateResourceRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchMigrateResourcesResponse(
    typing.TypedDict, total=False
):
    migrateResourceResponses: _list[GoogleCloudAiplatformV1MigrateResourceResponse]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJob(typing.TypedDict, total=False):
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
    state: typing.Literal[
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
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1BigQuerySource
    gcsSource: GoogleCloudAiplatformV1GcsSource
    instancesFormat: str
    vertexMultimodalDatasetSource: GoogleCloudAiplatformV1VertexMultimodalDatasetSource

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobInstanceConfig(
    typing.TypedDict, total=False
):
    excludedFields: _list[str]
    includedFields: _list[str]
    instanceType: str
    keyField: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobOutputConfig(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    gcsDestination: GoogleCloudAiplatformV1GcsDestination
    predictionsFormat: str
    vertexMultimodalDatasetDestination: (
        GoogleCloudAiplatformV1VertexMultimodalDatasetDestination
    )

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobOutputInfo(
    typing.TypedDict, total=False
):
    bigqueryOutputDataset: str
    bigqueryOutputTable: str
    gcsOutputDirectory: str
    vertexMultimodalDatasetName: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesRequest(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    entityTypeId: str
    featureSelector: GoogleCloudAiplatformV1FeatureSelector
    settings: _list[GoogleCloudAiplatformV1DestinationFeatureSetting]

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesRequestPassThroughField(
    typing.TypedDict, total=False
):
    fieldName: str

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadFeatureValuesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse(
    typing.TypedDict, total=False
):
    timeSeriesData: _list[GoogleCloudAiplatformV1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1BigQueryDestination(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1BigQueryRequestSet(typing.TypedDict, total=False):
    candidateResponseColumns: dict[str, typing.Any]
    promptColumn: str
    rubricsColumn: str
    samplingConfig: GoogleCloudAiplatformV1BigQueryRequestSetSamplingConfig
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1BigQueryRequestSetSamplingConfig(
    typing.TypedDict, total=False
):
    samplingCount: int
    samplingDuration: str
    samplingMethod: typing.Literal["SAMPLING_METHOD_UNSPECIFIED", "RANDOM"]

@typing.type_check_only
class GoogleCloudAiplatformV1BigQuerySource(typing.TypedDict, total=False):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1BleuInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1BleuInstance]
    metricSpec: GoogleCloudAiplatformV1BleuSpec

@typing.type_check_only
class GoogleCloudAiplatformV1BleuInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1BleuMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1BleuResults(typing.TypedDict, total=False):
    bleuMetricValues: _list[GoogleCloudAiplatformV1BleuMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1BleuSpec(typing.TypedDict, total=False):
    useEffectiveOrder: bool

@typing.type_check_only
class GoogleCloudAiplatformV1Blob(typing.TypedDict, total=False):
    data: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1BlurBaselineConfig(typing.TypedDict, total=False):
    maxBlurSigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1BoolArray(typing.TypedDict, total=False):
    values: _list[bool]

@typing.type_check_only
class GoogleCloudAiplatformV1CacheConfig(typing.TypedDict, total=False):
    disableCache: bool
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1CachedContent(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1Content]
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
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
class GoogleCloudAiplatformV1CachedContentUsageMetadata(typing.TypedDict, total=False):
    audioDurationSeconds: int
    imageCount: int
    textCount: int
    totalTokenCount: int
    videoDurationSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1CancelAsyncQueryReasoningEngineRequest(
    typing.TypedDict, total=False
):
    operationName: str

@typing.type_check_only
class GoogleCloudAiplatformV1CancelAsyncQueryReasoningEngineResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelBatchPredictionJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelCustomJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelDataLabelingJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelEvaluationRunRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelHyperparameterTuningJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelNasJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelPipelineJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelTrainingPipelineRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CancelTuningJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1Candidate(typing.TypedDict, total=False):
    avgLogprobs: float
    citationMetadata: GoogleCloudAiplatformV1CitationMetadata
    content: GoogleCloudAiplatformV1Content
    finishMessage: str
    finishReason: typing.Literal[
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
        "MODEL_ARMOR",
        "IMAGE_SAFETY",
        "IMAGE_PROHIBITED_CONTENT",
        "IMAGE_RECITATION",
        "IMAGE_OTHER",
        "UNEXPECTED_TOOL_CALL",
        "NO_IMAGE",
    ]
    groundingMetadata: GoogleCloudAiplatformV1GroundingMetadata
    index: int
    logprobsResult: GoogleCloudAiplatformV1LogprobsResult
    safetyRatings: _list[GoogleCloudAiplatformV1SafetyRating]
    urlContextMetadata: GoogleCloudAiplatformV1UrlContextMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CandidateResponse(typing.TypedDict, total=False):
    agentData: GoogleCloudAiplatformV1AgentData
    candidate: str
    error: GoogleRpcStatus
    text: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1CandidateResult(typing.TypedDict, total=False):
    additionalResults: typing.Any
    candidate: str
    error: GoogleRpcStatus
    explanation: str
    metric: str
    rubricVerdicts: _list[GoogleCloudAiplatformV1RubricVerdict]
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateMetatdata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    study: str
    trial: str

@typing.type_check_only
class GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateResponse(
    typing.TypedDict, total=False
):
    shouldStop: bool

@typing.type_check_only
class GoogleCloudAiplatformV1Checkpoint(typing.TypedDict, total=False):
    checkpointId: str
    epoch: str
    step: str

@typing.type_check_only
class GoogleCloudAiplatformV1Chunk(typing.TypedDict, total=False):
    data: str
    metadata: GoogleCloudAiplatformV1Metadata
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1Citation(typing.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: GoogleTypeDate
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1CitationMetadata(typing.TypedDict, total=False):
    citations: _list[GoogleCloudAiplatformV1Citation]

@typing.type_check_only
class GoogleCloudAiplatformV1Claim(typing.TypedDict, total=False):
    endIndex: int
    factIndexes: _list[int]
    score: float
    startIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1ClientConnectionConfig(typing.TypedDict, total=False):
    inferenceTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1CloudLoggingConfig(typing.TypedDict, total=False):
    project: str
    resourceLabels: dict[str, typing.Any]
    resourceType: str
    tracingContext: GoogleCloudAiplatformV1CloudLoggingConfigTracingContext

@typing.type_check_only
class GoogleCloudAiplatformV1CloudLoggingConfigTracingContext(
    typing.TypedDict, total=False
):
    conversationId: str
    spanId: str
    traceId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CodeExecutionResult(typing.TypedDict, total=False):
    id: str
    outcome: typing.Literal[
        "OUTCOME_UNSPECIFIED",
        "OUTCOME_OK",
        "OUTCOME_FAILED",
        "OUTCOME_DEADLINE_EXCEEDED",
    ]
    output: str

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1CoherenceInstance
    metricSpec: GoogleCloudAiplatformV1CoherenceSpec

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceInstance(typing.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1CoherenceSpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1ColabImage(typing.TypedDict, total=False):
    description: str
    releaseName: str

@typing.type_check_only
class GoogleCloudAiplatformV1CometInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1CometInstance
    metricSpec: GoogleCloudAiplatformV1CometSpec

@typing.type_check_only
class GoogleCloudAiplatformV1CometInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str
    source: str

@typing.type_check_only
class GoogleCloudAiplatformV1CometResult(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1CometSpec(typing.TypedDict, total=False):
    sourceLanguage: str
    targetLanguage: str
    version: typing.Literal["COMET_VERSION_UNSPECIFIED", "COMET_22_SRC_REF"]

@typing.type_check_only
class GoogleCloudAiplatformV1CompactSessionRequest(typing.TypedDict, total=False):
    compaction: GoogleCloudAiplatformV1CompactionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1CompactionConfig(typing.TypedDict, total=False):
    eventEditing: GoogleCloudAiplatformV1CompactionConfigEventEditingConfig
    summarization: GoogleCloudAiplatformV1CompactionConfigLlmSummarizationConfig

@typing.type_check_only
class GoogleCloudAiplatformV1CompactionConfigEventEditingConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO"]

@typing.type_check_only
class GoogleCloudAiplatformV1CompactionConfigLlmSummarizationConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO"]

@typing.type_check_only
class GoogleCloudAiplatformV1CompleteTrialRequest(typing.TypedDict, total=False):
    finalMeasurement: GoogleCloudAiplatformV1Measurement
    infeasibleReason: str
    trialInfeasible: bool

@typing.type_check_only
class GoogleCloudAiplatformV1CompletionStats(typing.TypedDict, total=False):
    failedCount: str
    incompleteCount: str
    successfulCount: str
    successfulForecastPointCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ComputationBasedMetricSpec(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    type: typing.Literal[
        "COMPUTATION_BASED_METRIC_TYPE_UNSPECIFIED", "EXACT_MATCH", "BLEU", "ROUGE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ComputeTokensRequest(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1Content]
    instances: _list[typing.Any]
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1ComputeTokensResponse(typing.TypedDict, total=False):
    tokensInfo: _list[GoogleCloudAiplatformV1TokensInfo]

@typing.type_check_only
class GoogleCloudAiplatformV1ContainerRegistryDestination(
    typing.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1ContainerSpec(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[GoogleCloudAiplatformV1EnvVar]
    imageUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1Content(typing.TypedDict, total=False):
    parts: _list[GoogleCloudAiplatformV1Part]
    role: str

@typing.type_check_only
class GoogleCloudAiplatformV1ContentMap(typing.TypedDict, total=False):
    values: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ContentMapContents(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1Context(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1ConversationTurn(typing.TypedDict, total=False):
    events: _list[GoogleCloudAiplatformV1AgentEvent]
    turnId: str
    turnIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1CopyModelOperationMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CopyModelRequest(typing.TypedDict, total=False):
    customServiceAccount: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    modelId: str
    parentModel: str
    sourceModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1CopyModelResponse(typing.TypedDict, total=False):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CorpusStatus(typing.TypedDict, total=False):
    errorStatus: str
    state: typing.Literal["UNKNOWN", "INITIALIZED", "ACTIVE", "ERROR"]

@typing.type_check_only
class GoogleCloudAiplatformV1CorroborateContentRequest(typing.TypedDict, total=False):
    content: GoogleCloudAiplatformV1Content
    facts: _list[GoogleCloudAiplatformV1Fact]
    parameters: GoogleCloudAiplatformV1CorroborateContentRequestParameters

@typing.type_check_only
class GoogleCloudAiplatformV1CorroborateContentRequestParameters(
    typing.TypedDict, total=False
):
    citationThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1CorroborateContentResponse(typing.TypedDict, total=False):
    claims: _list[GoogleCloudAiplatformV1Claim]
    corroborationScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1CountTokensRequest(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1Content]
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    instances: _list[typing.Any]
    model: str
    systemInstruction: GoogleCloudAiplatformV1Content
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1CountTokensResponse(typing.TypedDict, total=False):
    promptTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    totalBillableCharacters: int
    totalTokens: int

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDatasetOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDatasetVersionOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDeploymentResourcePoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest(
    typing.TypedDict, total=False
):
    deploymentResourcePool: GoogleCloudAiplatformV1DeploymentResourcePool
    deploymentResourcePoolId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateEndpointOperationMetadata(
    typing.TypedDict, total=False
):
    deploymentStage: typing.Literal[
        "DEPLOYMENT_STAGE_UNSPECIFIED",
        "STARTING_DEPLOYMENT",
        "PREPARING_MODEL",
        "CREATING_SERVING_CLUSTER",
        "ADDING_NODES_TO_CLUSTER",
        "GETTING_CONTAINER_IMAGE",
        "STARTING_MODEL_SERVER",
        "FINISHING_UP",
        "DEPLOYMENT_TERMINATED",
        "SUCCESSFULLY_DEPLOYED",
        "FAILED_TO_DEPLOY",
    ]
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateEntityTypeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureGroupOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureOnlineStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureRequest(typing.TypedDict, total=False):
    feature: GoogleCloudAiplatformV1Feature
    featureId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeatureViewOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateFeaturestoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateIndexEndpointOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateIndexOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: (
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1CreateMetadataStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateNotebookExecutionJobOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateNotebookExecutionJobRequest(
    typing.TypedDict, total=False
):
    notebookExecutionJob: GoogleCloudAiplatformV1NotebookExecutionJob
    notebookExecutionJobId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateNotebookRuntimeTemplateOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreatePersistentResourceOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreatePipelineJobRequest(typing.TypedDict, total=False):
    parent: str
    pipelineJob: GoogleCloudAiplatformV1PipelineJob
    pipelineJobId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateRegistryFeatureOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateServingProfileOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateSpecialistPoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateTensorboardOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1CreateTensorboardRunRequest(typing.TypedDict, total=False):
    parent: str
    tensorboardRun: GoogleCloudAiplatformV1TensorboardRun
    tensorboardRunId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CreateTensorboardTimeSeriesRequest(
    typing.TypedDict, total=False
):
    parent: str
    tensorboardTimeSeries: GoogleCloudAiplatformV1TensorboardTimeSeries
    tensorboardTimeSeriesId: str

@typing.type_check_only
class GoogleCloudAiplatformV1CsvDestination(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1CsvSource(typing.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1CustomCodeExecutionResult(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1CustomCodeExecutionSpec(typing.TypedDict, total=False):
    evaluationFunction: str

@typing.type_check_only
class GoogleCloudAiplatformV1CustomJob(typing.TypedDict, total=False):
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
    state: typing.Literal[
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
class GoogleCloudAiplatformV1CustomJobSpec(typing.TypedDict, total=False):
    baseOutputDirectory: GoogleCloudAiplatformV1GcsDestination
    enableDashboardAccess: bool
    enableWebAccess: bool
    experiment: str
    experimentRun: str
    models: _list[str]
    network: str
    persistentResourceId: str
    protectedArtifactLocationId: str
    pscInterfaceConfig: GoogleCloudAiplatformV1PscInterfaceConfig
    reservedIpRanges: _list[str]
    scheduling: GoogleCloudAiplatformV1Scheduling
    serviceAccount: str
    tensorboard: str
    workerPoolSpecs: _list[GoogleCloudAiplatformV1WorkerPoolSpec]

@typing.type_check_only
class GoogleCloudAiplatformV1CustomOutput(typing.TypedDict, total=False):
    rawOutputs: GoogleCloudAiplatformV1RawOutput

@typing.type_check_only
class GoogleCloudAiplatformV1CustomOutputFormatConfig(typing.TypedDict, total=False):
    returnRawOutput: bool

@typing.type_check_only
class GoogleCloudAiplatformV1DataItem(typing.TypedDict, total=False):
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1DataItemView(typing.TypedDict, total=False):
    annotations: _list[GoogleCloudAiplatformV1Annotation]
    dataItem: GoogleCloudAiplatformV1DataItem
    hasTruncatedAnnotations: bool

@typing.type_check_only
class GoogleCloudAiplatformV1DataLabelingJob(typing.TypedDict, total=False):
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
    state: typing.Literal[
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
class GoogleCloudAiplatformV1Dataset(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1DatasetCustomMetric(typing.TypedDict, total=False):
    aggregationFunction: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetDistribution(typing.TypedDict, total=False):
    buckets: _list[GoogleCloudAiplatformV1DatasetDistributionDistributionBucket]
    max: float
    mean: float
    median: float
    min: float
    p5: float
    p95: float
    sum: float

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetDistributionDistributionBucket(
    typing.TypedDict, total=False
):
    count: str
    left: float
    right: float

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetVersion(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1DedicatedResources(typing.TypedDict, total=False):
    autoscalingMetricSpecs: _list[GoogleCloudAiplatformV1AutoscalingMetricSpec]
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    maxReplicaCount: int
    minReplicaCount: int
    requiredReplicaCount: int
    spot: bool

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesRequest(typing.TypedDict, total=False):
    selectEntity: GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectEntity
    selectTimeRangeAndFeature: (
        GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectTimeRangeAndFeature
    )

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectEntity(
    typing.TypedDict, total=False
):
    entityIdSelector: GoogleCloudAiplatformV1EntityIdSelector

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesRequestSelectTimeRangeAndFeature(
    typing.TypedDict, total=False
):
    featureSelector: GoogleCloudAiplatformV1FeatureSelector
    skipOnlineStorageDelete: bool
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesResponse(typing.TypedDict, total=False):
    selectEntity: GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectEntity
    selectTimeRangeAndFeature: (
        GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectTimeRangeAndFeature
    )

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectEntity(
    typing.TypedDict, total=False
):
    offlineStorageDeletedEntityRowCount: str
    onlineStorageDeletedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteFeatureValuesResponseSelectTimeRangeAndFeature(
    typing.TypedDict, total=False
):
    impactedFeatureCount: str
    offlineStorageModifiedEntityRowCount: str
    onlineStorageModifiedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteMetadataStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeleteOperationMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeployIndexOperationMetadata(
    typing.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeployIndexRequest(typing.TypedDict, total=False):
    deployedIndex: GoogleCloudAiplatformV1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1DeployIndexResponse(typing.TypedDict, total=False):
    deployedIndex: GoogleCloudAiplatformV1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1DeployModelOperationMetadata(
    typing.TypedDict, total=False
):
    deploymentStage: typing.Literal[
        "DEPLOYMENT_STAGE_UNSPECIFIED",
        "STARTING_DEPLOYMENT",
        "PREPARING_MODEL",
        "CREATING_SERVING_CLUSTER",
        "ADDING_NODES_TO_CLUSTER",
        "GETTING_CONTAINER_IMAGE",
        "STARTING_MODEL_SERVER",
        "FINISHING_UP",
        "DEPLOYMENT_TERMINATED",
        "SUCCESSFULLY_DEPLOYED",
        "FAILED_TO_DEPLOY",
    ]
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1DeployModelRequest(typing.TypedDict, total=False):
    deployedModel: GoogleCloudAiplatformV1DeployedModel
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployModelResponse(typing.TypedDict, total=False):
    deployedModel: GoogleCloudAiplatformV1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1DeployOperationMetadata(typing.TypedDict, total=False):
    destination: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    modelId: str
    projectNumber: str
    publisherModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployRequest(typing.TypedDict, total=False):
    deployConfig: GoogleCloudAiplatformV1DeployRequestDeployConfig
    endpointConfig: GoogleCloudAiplatformV1DeployRequestEndpointConfig
    huggingFaceModelId: str
    modelConfig: GoogleCloudAiplatformV1DeployRequestModelConfig
    publisherModelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployRequestDeployConfig(typing.TypedDict, total=False):
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    fastTryoutEnabled: bool
    systemLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployRequestEndpointConfig(typing.TypedDict, total=False):
    dedicatedEndpointDisabled: bool
    dedicatedEndpointEnabled: bool
    endpointDisplayName: str
    endpointUserId: str
    labels: dict[str, typing.Any]
    privateServiceConnectConfig: GoogleCloudAiplatformV1PrivateServiceConnectConfig

@typing.type_check_only
class GoogleCloudAiplatformV1DeployRequestModelConfig(typing.TypedDict, total=False):
    acceptEula: bool
    containerSpec: GoogleCloudAiplatformV1ModelContainerSpec
    huggingFaceAccessToken: str
    huggingFaceCacheEnabled: bool
    modelDisplayName: str
    modelUserId: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployResponse(typing.TypedDict, total=False):
    endpoint: str
    model: str
    publisherModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndex(typing.TypedDict, total=False):
    automaticResources: GoogleCloudAiplatformV1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    deployedIndexAuthConfig: GoogleCloudAiplatformV1DeployedIndexAuthConfig
    deploymentGroup: str
    deploymentTier: typing.Literal["DEPLOYMENT_TIER_UNSPECIFIED", "STORAGE"]
    displayName: str
    enableAccessLogging: bool
    enableDatapointUpsertLogging: bool
    id: str
    index: str
    indexSyncTime: str
    privateEndpoints: GoogleCloudAiplatformV1IndexPrivateEndpoints
    pscAutomationConfigs: _list[GoogleCloudAiplatformV1PSCAutomationConfig]
    reservedIpRanges: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndexAuthConfig(typing.TypedDict, total=False):
    authProvider: GoogleCloudAiplatformV1DeployedIndexAuthConfigAuthProvider

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndexAuthConfigAuthProvider(
    typing.TypedDict, total=False
):
    allowedIssuers: _list[str]
    audiences: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedIndexRef(typing.TypedDict, total=False):
    deployedIndexId: str
    displayName: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedModel(typing.TypedDict, total=False):
    automaticResources: GoogleCloudAiplatformV1AutomaticResources
    checkpointId: str
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    disableContainerLogging: bool
    disableExplanations: bool
    displayName: str
    enableAccessLogging: bool
    explanationSpec: GoogleCloudAiplatformV1ExplanationSpec
    fasterDeploymentConfig: GoogleCloudAiplatformV1FasterDeploymentConfig
    gdcConnectedModel: str
    id: str
    model: str
    modelVersionId: str
    privateEndpoints: GoogleCloudAiplatformV1PrivateEndpoints
    serviceAccount: str
    sharedResources: str
    speculativeDecodingSpec: GoogleCloudAiplatformV1SpeculativeDecodingSpec
    status: GoogleCloudAiplatformV1DeployedModelStatus
    systemLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedModelRef(typing.TypedDict, total=False):
    checkpointId: str
    deployedModelId: str
    endpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeployedModelStatus(typing.TypedDict, total=False):
    availableReplicaCount: int
    lastUpdateTime: str
    message: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeploymentResourcePool(typing.TypedDict, total=False):
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1DedicatedResources
    disableContainerLogging: bool
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1DeprovisionSemanticGovernancePolicyEngineRequest(
    typing.TypedDict, total=False
):
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1DestinationFeatureSetting(typing.TypedDict, total=False):
    destinationField: str
    featureId: str

@typing.type_check_only
class GoogleCloudAiplatformV1DirectPredictRequest(typing.TypedDict, total=False):
    inputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1DirectPredictResponse(typing.TypedDict, total=False):
    outputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1DirectRawPredictRequest(typing.TypedDict, total=False):
    input: str
    methodName: str

@typing.type_check_only
class GoogleCloudAiplatformV1DirectRawPredictResponse(typing.TypedDict, total=False):
    output: str

@typing.type_check_only
class GoogleCloudAiplatformV1DirectUploadSource(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1DiskSpec(typing.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1DnsPeeringConfig(typing.TypedDict, total=False):
    domain: str
    targetNetwork: str
    targetProject: str

@typing.type_check_only
class GoogleCloudAiplatformV1DoubleArray(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1DynamicRetrievalConfig(typing.TypedDict, total=False):
    dynamicThreshold: float
    mode: typing.Literal["MODE_UNSPECIFIED", "MODE_DYNAMIC"]

@typing.type_check_only
class GoogleCloudAiplatformV1EmbedContentRequest(typing.TypedDict, total=False):
    autoTruncate: bool
    content: GoogleCloudAiplatformV1Content
    embedContentConfig: GoogleCloudAiplatformV1EmbedContentRequestEmbedContentConfig
    outputDimensionality: int
    taskType: typing.Literal[
        "UNSPECIFIED",
        "RETRIEVAL_QUERY",
        "RETRIEVAL_DOCUMENT",
        "SEMANTIC_SIMILARITY",
        "CLASSIFICATION",
        "CLUSTERING",
        "QUESTION_ANSWERING",
        "FACT_VERIFICATION",
        "CODE_RETRIEVAL_QUERY",
    ]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1EmbedContentRequestEmbedContentConfig(
    typing.TypedDict, total=False
):
    audioTrackExtraction: bool
    autoTruncate: bool
    documentOcr: bool
    outputDimensionality: int
    taskType: typing.Literal[
        "UNSPECIFIED",
        "RETRIEVAL_QUERY",
        "RETRIEVAL_DOCUMENT",
        "SEMANTIC_SIMILARITY",
        "CLASSIFICATION",
        "CLUSTERING",
        "QUESTION_ANSWERING",
        "FACT_VERIFICATION",
        "CODE_RETRIEVAL_QUERY",
    ]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1EmbedContentResponse(typing.TypedDict, total=False):
    embedding: GoogleCloudAiplatformV1EmbedContentResponseEmbedding
    truncated: bool
    usageMetadata: GoogleCloudAiplatformV1UsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1EmbedContentResponseEmbedding(
    typing.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1EncryptionSpec(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class GoogleCloudAiplatformV1Endpoint(typing.TypedDict, total=False):
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
    gdcConfig: GoogleCloudAiplatformV1GdcConfig
    genAiAdvancedFeaturesConfig: GoogleCloudAiplatformV1GenAiAdvancedFeaturesConfig
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
class GoogleCloudAiplatformV1EnterpriseWebSearch(typing.TypedDict, total=False):
    blockingConfidence: typing.Literal[
        "PHISH_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_HIGH_AND_ABOVE",
        "BLOCK_HIGHER_AND_ABOVE",
        "BLOCK_VERY_HIGH_AND_ABOVE",
        "BLOCK_ONLY_EXTREMELY_HIGH",
    ]
    excludeDomains: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1EntityIdSelector(typing.TypedDict, total=False):
    csvSource: GoogleCloudAiplatformV1CsvSource
    entityIdField: str

@typing.type_check_only
class GoogleCloudAiplatformV1EntityType(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1EnvVar(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1ErrorAnalysisAnnotation(typing.TypedDict, total=False):
    attributedItems: _list[GoogleCloudAiplatformV1ErrorAnalysisAnnotationAttributedItem]
    outlierScore: float
    outlierThreshold: float
    queryType: typing.Literal[
        "QUERY_TYPE_UNSPECIFIED",
        "ALL_SIMILAR",
        "SAME_CLASS_SIMILAR",
        "SAME_CLASS_DISSIMILAR",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ErrorAnalysisAnnotationAttributedItem(
    typing.TypedDict, total=False
):
    annotationResourceName: str
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluateDatasetRequest(typing.TypedDict, total=False):
    autoraterConfig: GoogleCloudAiplatformV1AutoraterConfig
    dataset: GoogleCloudAiplatformV1EvaluationDataset
    location: str
    metrics: _list[GoogleCloudAiplatformV1Metric]
    outputConfig: GoogleCloudAiplatformV1OutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluateDatasetResponse(typing.TypedDict, total=False):
    aggregationOutput: GoogleCloudAiplatformV1AggregationOutput
    outputInfo: GoogleCloudAiplatformV1OutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluateDatasetRun(typing.TypedDict, total=False):
    checkpointId: str
    error: GoogleRpcStatus
    evaluateDatasetResponse: GoogleCloudAiplatformV1EvaluateDatasetResponse
    evaluationRun: str
    operationName: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluateInstancesRequest(typing.TypedDict, total=False):
    autoraterConfig: GoogleCloudAiplatformV1AutoraterConfig
    bleuInput: GoogleCloudAiplatformV1BleuInput
    coherenceInput: GoogleCloudAiplatformV1CoherenceInput
    cometInput: GoogleCloudAiplatformV1CometInput
    exactMatchInput: GoogleCloudAiplatformV1ExactMatchInput
    fluencyInput: GoogleCloudAiplatformV1FluencyInput
    fulfillmentInput: GoogleCloudAiplatformV1FulfillmentInput
    groundednessInput: GoogleCloudAiplatformV1GroundednessInput
    instance: GoogleCloudAiplatformV1EvaluationInstance
    location: str
    metricSources: _list[GoogleCloudAiplatformV1MetricSource]
    metrics: _list[GoogleCloudAiplatformV1Metric]
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
    rubricBasedInstructionFollowingInput: (
        GoogleCloudAiplatformV1RubricBasedInstructionFollowingInput
    )
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
class GoogleCloudAiplatformV1EvaluateInstancesResponse(typing.TypedDict, total=False):
    bleuResults: GoogleCloudAiplatformV1BleuResults
    coherenceResult: GoogleCloudAiplatformV1CoherenceResult
    cometResult: GoogleCloudAiplatformV1CometResult
    exactMatchResults: GoogleCloudAiplatformV1ExactMatchResults
    fluencyResult: GoogleCloudAiplatformV1FluencyResult
    fulfillmentResult: GoogleCloudAiplatformV1FulfillmentResult
    groundednessResult: GoogleCloudAiplatformV1GroundednessResult
    metricResults: _list[GoogleCloudAiplatformV1MetricResult]
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
    rubricBasedInstructionFollowingResult: (
        GoogleCloudAiplatformV1RubricBasedInstructionFollowingResult
    )
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
class GoogleCloudAiplatformV1EvaluatedAnnotation(typing.TypedDict, total=False):
    dataItemPayload: typing.Any
    errorAnalysisAnnotations: _list[GoogleCloudAiplatformV1ErrorAnalysisAnnotation]
    evaluatedDataItemViewId: str
    explanations: _list[GoogleCloudAiplatformV1EvaluatedAnnotationExplanation]
    groundTruths: _list[typing.Any]
    predictions: _list[typing.Any]
    type: typing.Literal[
        "EVALUATED_ANNOTATION_TYPE_UNSPECIFIED",
        "TRUE_POSITIVE",
        "FALSE_POSITIVE",
        "FALSE_NEGATIVE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluatedAnnotationExplanation(
    typing.TypedDict, total=False
):
    explanation: GoogleCloudAiplatformV1Explanation
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationConfig(typing.TypedDict, total=False):
    autoraterConfig: GoogleCloudAiplatformV1AutoraterConfig
    datasetCustomMetrics: _list[GoogleCloudAiplatformV1DatasetCustomMetric]
    inferenceGenerationConfig: GoogleCloudAiplatformV1GenerationConfig
    metrics: _list[GoogleCloudAiplatformV1Metric]
    outputConfig: GoogleCloudAiplatformV1OutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationDataset(typing.TypedDict, total=False):
    bigquerySource: GoogleCloudAiplatformV1BigQuerySource
    gcsSource: GoogleCloudAiplatformV1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstance(typing.TypedDict, total=False):
    agentData: GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentData
    interactionsDataSource: (
        GoogleCloudAiplatformV1EvaluationInstanceInteractionsDataSource
    )
    otherData: GoogleCloudAiplatformV1EvaluationInstanceMapInstance
    prompt: GoogleCloudAiplatformV1EvaluationInstanceInstanceData
    reference: GoogleCloudAiplatformV1EvaluationInstanceInstanceData
    response: GoogleCloudAiplatformV1EvaluationInstanceInstanceData
    rubricGroups: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentConfig(
    typing.TypedDict, total=False
):
    agentId: str
    agentType: str
    description: str
    developerInstruction: GoogleCloudAiplatformV1EvaluationInstanceInstanceData
    subAgents: _list[str]
    tools: GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentConfigTools
    toolsText: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentConfigTools(
    typing.TypedDict, total=False
):
    tool: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentData(
    typing.TypedDict, total=False
):
    agentConfig: GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentConfig
    agents: dict[str, typing.Any]
    developerInstruction: GoogleCloudAiplatformV1EvaluationInstanceInstanceData
    events: GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataEvents
    tools: GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataTools
    toolsText: str
    turns: _list[
        GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataConversationTurn
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataAgentEvent(
    typing.TypedDict, total=False
):
    activeTools: _list[GoogleCloudAiplatformV1Tool]
    author: str
    content: GoogleCloudAiplatformV1Content
    eventTime: str
    stateDelta: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataConversationTurn(
    typing.TypedDict, total=False
):
    events: _list[
        GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataAgentEvent
    ]
    turnId: str
    turnIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataEvents(
    typing.TypedDict, total=False
):
    event: _list[GoogleCloudAiplatformV1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentDataTools(
    typing.TypedDict, total=False
):
    tool: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceInstanceData(
    typing.TypedDict, total=False
):
    contents: GoogleCloudAiplatformV1EvaluationInstanceInstanceDataContents
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceInstanceDataContents(
    typing.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceInteractionsDataSource(
    typing.TypedDict, total=False
):
    geminiAgentConfig: GoogleCloudAiplatformV1GeminiAgentConfig
    interaction: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationInstanceMapInstance(
    typing.TypedDict, total=False
):
    mapInstance: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationItem(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    error: GoogleRpcStatus
    evaluationItemType: typing.Literal[
        "EVALUATION_ITEM_TYPE_UNSPECIFIED", "REQUEST", "RESULT"
    ]
    evaluationRequest: GoogleCloudAiplatformV1EvaluationRequest
    evaluationResponse: GoogleCloudAiplatformV1EvaluationResult
    gcsUri: str
    labels: dict[str, typing.Any]
    metadata: typing.Any
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationMetric(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    gcsUri: str
    labels: dict[str, typing.Any]
    metric: GoogleCloudAiplatformV1Metric
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationParserConfig(typing.TypedDict, total=False):
    customCodeParserConfig: (
        GoogleCloudAiplatformV1EvaluationParserConfigCustomCodeParserConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationParserConfigCustomCodeParserConfig(
    typing.TypedDict, total=False
):
    parsingFunction: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationPrompt(typing.TypedDict, total=False):
    agentData: GoogleCloudAiplatformV1AgentData
    promptTemplateData: GoogleCloudAiplatformV1EvaluationPromptPromptTemplateData
    text: str
    userScenario: GoogleCloudAiplatformV1EvaluationPromptUserScenario
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationPromptPromptTemplateData(
    typing.TypedDict, total=False
):
    values: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationPromptUserScenario(
    typing.TypedDict, total=False
):
    conversationPlan: str
    startingPrompt: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRequest(typing.TypedDict, total=False):
    candidateResponses: _list[GoogleCloudAiplatformV1CandidateResponse]
    goldenResponse: GoogleCloudAiplatformV1CandidateResponse
    prompt: GoogleCloudAiplatformV1EvaluationPrompt
    rubrics: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationResult(typing.TypedDict, total=False):
    candidateResults: _list[GoogleCloudAiplatformV1CandidateResult]
    evaluationRequest: str
    evaluationRun: str
    metadata: typing.Any
    metric: str
    request: GoogleCloudAiplatformV1EvaluationRequest

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationResults(typing.TypedDict, total=False):
    evaluationSet: str
    summaryMetrics: GoogleCloudAiplatformV1SummaryMetrics

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRubricConfig(typing.TypedDict, total=False):
    predefinedRubricGenerationSpec: (
        GoogleCloudAiplatformV1EvaluationRunMetricPredefinedMetricSpec
    )
    rubricGenerationSpec: GoogleCloudAiplatformV1EvaluationRunMetricRubricGenerationSpec
    rubricGroupKey: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRun(typing.TypedDict, total=False):
    completionTime: str
    createTime: str
    dataSource: GoogleCloudAiplatformV1EvaluationRunDataSource
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    error: GoogleRpcStatus
    evaluationConfig: GoogleCloudAiplatformV1EvaluationRunEvaluationConfig
    evaluationResults: GoogleCloudAiplatformV1EvaluationResults
    evaluationSetSnapshot: str
    inferenceConfigs: dict[str, typing.Any]
    labels: dict[str, typing.Any]
    metadata: typing.Any
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "INFERENCE",
        "GENERATING_RUBRICS",
        "GENERATING_LOSS_CLUSTERS",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunDataSource(typing.TypedDict, total=False):
    bigqueryRequestSet: GoogleCloudAiplatformV1BigQueryRequestSet
    evaluationSet: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunEvaluationConfig(
    typing.TypedDict, total=False
):
    autoraterConfig: GoogleCloudAiplatformV1EvaluationRunEvaluationConfigAutoraterConfig
    cloudLoggingConfig: GoogleCloudAiplatformV1CloudLoggingConfig
    datasetCustomMetrics: _list[GoogleCloudAiplatformV1DatasetCustomMetric]
    lossAnalysisConfig: _list[GoogleCloudAiplatformV1LossAnalysisConfig]
    metrics: _list[GoogleCloudAiplatformV1EvaluationRunMetric]
    outputConfig: GoogleCloudAiplatformV1EvaluationRunEvaluationConfigOutputConfig
    promptTemplate: GoogleCloudAiplatformV1EvaluationRunEvaluationConfigPromptTemplate
    rubricConfigs: _list[GoogleCloudAiplatformV1EvaluationRubricConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunEvaluationConfigAutoraterConfig(
    typing.TypedDict, total=False
):
    autoraterModel: str
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    sampleCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunEvaluationConfigOutputConfig(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    gcsDestination: GoogleCloudAiplatformV1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunEvaluationConfigPromptTemplate(
    typing.TypedDict, total=False
):
    gcsUri: str
    promptTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunInferenceConfig(
    typing.TypedDict, total=False
):
    agentRunConfig: GoogleCloudAiplatformV1EvaluationRunInferenceConfigAgentRunConfig
    agents: dict[str, typing.Any]
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    model: str
    parallelism: int
    promptTemplate: GoogleCloudAiplatformV1EvaluationRunEvaluationConfigPromptTemplate

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunInferenceConfigAgentRunConfig(
    typing.TypedDict, total=False
):
    agentEngine: str
    geminiAgentConfig: GoogleCloudAiplatformV1GeminiAgentConfig
    sessionInput: GoogleCloudAiplatformV1EvaluationRunInferenceConfigSessionInput
    userSimulatorConfig: GoogleCloudAiplatformV1EvaluationRunInferenceConfigAgentRunConfigUserSimulatorConfig

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunInferenceConfigAgentRunConfigUserSimulatorConfig(
    typing.TypedDict, total=False
):
    maxTurn: int
    modelConfig: GoogleCloudAiplatformV1GenerationConfig
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunInferenceConfigSessionInput(
    typing.TypedDict, total=False
):
    parameters: dict[str, typing.Any]
    sessionState: dict[str, typing.Any]
    userId: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunMetric(typing.TypedDict, total=False):
    computationBasedMetricSpec: (
        GoogleCloudAiplatformV1EvaluationRunMetricComputationBasedMetricSpec
    )
    llmBasedMetricSpec: GoogleCloudAiplatformV1EvaluationRunMetricLLMBasedMetricSpec
    metric: str
    metricConfig: GoogleCloudAiplatformV1Metric
    metricResourceName: str
    predefinedMetricSpec: GoogleCloudAiplatformV1EvaluationRunMetricPredefinedMetricSpec
    rubricBasedMetricSpec: (
        GoogleCloudAiplatformV1EvaluationRunMetricRubricBasedMetricSpec
    )

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunMetricComputationBasedMetricSpec(
    typing.TypedDict, total=False
):
    parameters: dict[str, typing.Any]
    type: typing.Literal[
        "COMPUTATION_BASED_METRIC_TYPE_UNSPECIFIED", "EXACT_MATCH", "BLEU", "ROUGE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunMetricLLMBasedMetricSpec(
    typing.TypedDict, total=False
):
    additionalConfig: dict[str, typing.Any]
    judgeAutoraterConfig: (
        GoogleCloudAiplatformV1EvaluationRunEvaluationConfigAutoraterConfig
    )
    metricPromptTemplate: str
    predefinedRubricGenerationSpec: (
        GoogleCloudAiplatformV1EvaluationRunMetricPredefinedMetricSpec
    )
    rubricGenerationSpec: GoogleCloudAiplatformV1EvaluationRunMetricRubricGenerationSpec
    rubricGroupKey: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunMetricPredefinedMetricSpec(
    typing.TypedDict, total=False
):
    metricSpecName: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunMetricRubricBasedMetricSpec(
    typing.TypedDict, total=False
):
    inlineRubrics: (
        GoogleCloudAiplatformV1EvaluationRunMetricRubricBasedMetricSpecRepeatedRubrics
    )
    judgeAutoraterConfig: (
        GoogleCloudAiplatformV1EvaluationRunEvaluationConfigAutoraterConfig
    )
    metricPromptTemplate: str
    rubricGenerationSpec: GoogleCloudAiplatformV1EvaluationRunMetricRubricGenerationSpec
    rubricGroupKey: str

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunMetricRubricBasedMetricSpecRepeatedRubrics(
    typing.TypedDict, total=False
):
    rubrics: _list[GoogleCloudAiplatformV1Rubric]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationRunMetricRubricGenerationSpec(
    typing.TypedDict, total=False
):
    metricResourceName: str
    modelConfig: GoogleCloudAiplatformV1EvaluationRunEvaluationConfigAutoraterConfig
    promptTemplate: str
    rubricContentType: typing.Literal[
        "RUBRIC_CONTENT_TYPE_UNSPECIFIED",
        "PROPERTY",
        "NL_QUESTION_ANSWER",
        "PYTHON_CODE_ASSERTION",
    ]
    rubricTypeOntology: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluationSet(typing.TypedDict, total=False):
    agentConfigs: dict[str, typing.Any]
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    evaluationItems: _list[str]
    metadata: typing.Any
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1Event(typing.TypedDict, total=False):
    artifact: str
    eventTime: str
    execution: str
    labels: dict[str, typing.Any]
    type: typing.Literal["TYPE_UNSPECIFIED", "INPUT", "OUTPUT"]

@typing.type_check_only
class GoogleCloudAiplatformV1EventActions(typing.TypedDict, total=False):
    artifactDelta: dict[str, typing.Any]
    escalate: bool
    requestedAuthConfigs: dict[str, typing.Any]
    skipSummarization: bool
    stateDelta: dict[str, typing.Any]
    transferAgent: str

@typing.type_check_only
class GoogleCloudAiplatformV1EventMetadata(typing.TypedDict, total=False):
    branch: str
    customMetadata: dict[str, typing.Any]
    groundingMetadata: GoogleCloudAiplatformV1GroundingMetadata
    inputTranscription: GoogleCloudAiplatformV1Transcription
    interrupted: bool
    longRunningToolIds: _list[str]
    outputTranscription: GoogleCloudAiplatformV1Transcription
    partial: bool
    turnComplete: bool

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1ExactMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ExactMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchResults(typing.TypedDict, total=False):
    exactMatchMetricValues: _list[GoogleCloudAiplatformV1ExactMatchMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1ExactMatchSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1Examples(typing.TypedDict, total=False):
    exampleGcsSource: GoogleCloudAiplatformV1ExamplesExampleGcsSource
    nearestNeighborSearchConfig: typing.Any
    neighborCount: int
    presets: GoogleCloudAiplatformV1Presets

@typing.type_check_only
class GoogleCloudAiplatformV1ExamplesExampleGcsSource(typing.TypedDict, total=False):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "JSONL"]
    gcsSource: GoogleCloudAiplatformV1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1ExamplesOverride(typing.TypedDict, total=False):
    crowdingCount: int
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "INSTANCES", "EMBEDDINGS"]
    neighborCount: int
    restrictions: _list[GoogleCloudAiplatformV1ExamplesRestrictionsNamespace]
    returnEmbeddings: bool

@typing.type_check_only
class GoogleCloudAiplatformV1ExamplesRestrictionsNamespace(
    typing.TypedDict, total=False
):
    allow: _list[str]
    deny: _list[str]
    namespaceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExecutableCode(typing.TypedDict, total=False):
    code: str
    id: str
    language: typing.Literal["LANGUAGE_UNSPECIFIED", "PYTHON"]

@typing.type_check_only
class GoogleCloudAiplatformV1ExecuteCodeRequest(typing.TypedDict, total=False):
    inputs: _list[GoogleCloudAiplatformV1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1ExecuteCodeResponse(typing.TypedDict, total=False):
    outputs: _list[GoogleCloudAiplatformV1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1ExecuteSandboxEnvironmentRequest(
    typing.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1ExecuteSandboxEnvironmentResponse(
    typing.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1Execution(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    schemaTitle: str
    schemaVersion: str
    state: typing.Literal[
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
class GoogleCloudAiplatformV1ExplainRequest(typing.TypedDict, total=False):
    deployedModelId: str
    explanationSpecOverride: GoogleCloudAiplatformV1ExplanationSpecOverride
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1ExplainResponse(typing.TypedDict, total=False):
    deployedModelId: str
    explanations: _list[GoogleCloudAiplatformV1Explanation]
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1Explanation(typing.TypedDict, total=False):
    attributions: _list[GoogleCloudAiplatformV1Attribution]
    neighbors: _list[GoogleCloudAiplatformV1Neighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadata(typing.TypedDict, total=False):
    featureAttributionsSchemaUri: str
    inputs: dict[str, typing.Any]
    latentSpaceSource: str
    outputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataInputMetadata(
    typing.TypedDict, total=False
):
    denseShapeTensorName: str
    encodedBaselines: _list[typing.Any]
    encodedTensorName: str
    encoding: typing.Literal[
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
    typing.TypedDict, total=False
):
    maxValue: float
    minValue: float
    originalMean: float
    originalStddev: float

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataInputMetadataVisualization(
    typing.TypedDict, total=False
):
    clipPercentLowerbound: float
    clipPercentUpperbound: float
    colorMap: typing.Literal[
        "COLOR_MAP_UNSPECIFIED",
        "PINK_GREEN",
        "VIRIDIS",
        "RED",
        "GREEN",
        "RED_GREEN",
        "PINK_WHITE_GREEN",
    ]
    overlayType: typing.Literal[
        "OVERLAY_TYPE_UNSPECIFIED", "NONE", "ORIGINAL", "GRAYSCALE", "MASK_BLACK"
    ]
    polarity: typing.Literal["POLARITY_UNSPECIFIED", "POSITIVE", "NEGATIVE", "BOTH"]
    type: typing.Literal["TYPE_UNSPECIFIED", "PIXELS", "OUTLINES"]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataOutputMetadata(
    typing.TypedDict, total=False
):
    displayNameMappingKey: str
    indexDisplayNameMapping: typing.Any
    outputTensorName: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataOverride(typing.TypedDict, total=False):
    inputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationMetadataOverrideInputMetadataOverride(
    typing.TypedDict, total=False
):
    inputBaselines: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationParameters(typing.TypedDict, total=False):
    examples: GoogleCloudAiplatformV1Examples
    integratedGradientsAttribution: (
        GoogleCloudAiplatformV1IntegratedGradientsAttribution
    )
    outputIndices: _list[typing.Any]
    sampledShapleyAttribution: GoogleCloudAiplatformV1SampledShapleyAttribution
    topK: int
    xraiAttribution: GoogleCloudAiplatformV1XraiAttribution

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationSpec(typing.TypedDict, total=False):
    metadata: GoogleCloudAiplatformV1ExplanationMetadata
    parameters: GoogleCloudAiplatformV1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1ExplanationSpecOverride(typing.TypedDict, total=False):
    examplesOverride: GoogleCloudAiplatformV1ExamplesOverride
    metadata: GoogleCloudAiplatformV1ExplanationMetadataOverride
    parameters: GoogleCloudAiplatformV1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataConfig(typing.TypedDict, total=False):
    annotationSchemaUri: str
    annotationsFilter: str
    exportUse: typing.Literal["EXPORT_USE_UNSPECIFIED", "CUSTOM_CODE_TRAINING"]
    filterSplit: GoogleCloudAiplatformV1ExportFilterSplit
    fractionSplit: GoogleCloudAiplatformV1ExportFractionSplit
    gcsDestination: GoogleCloudAiplatformV1GcsDestination
    savedQueryId: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataOperationMetadata(typing.TypedDict, total=False):
    gcsOutputDirectory: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataRequest(typing.TypedDict, total=False):
    exportConfig: GoogleCloudAiplatformV1ExportDataConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ExportDataResponse(typing.TypedDict, total=False):
    dataStats: GoogleCloudAiplatformV1ModelDataStats
    exportedFiles: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesRequest(typing.TypedDict, total=False):
    destination: GoogleCloudAiplatformV1FeatureValueDestination
    featureSelector: GoogleCloudAiplatformV1FeatureSelector
    fullExport: GoogleCloudAiplatformV1ExportFeatureValuesRequestFullExport
    settings: _list[GoogleCloudAiplatformV1DestinationFeatureSetting]
    snapshotExport: GoogleCloudAiplatformV1ExportFeatureValuesRequestSnapshotExport

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesRequestFullExport(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesRequestSnapshotExport(
    typing.TypedDict, total=False
):
    snapshotTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFeatureValuesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFilterSplit(typing.TypedDict, total=False):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportFractionSplit(typing.TypedDict, total=False):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    outputInfo: GoogleCloudAiplatformV1ExportModelOperationMetadataOutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelOperationMetadataOutputInfo(
    typing.TypedDict, total=False
):
    artifactOutputUri: str
    imageOutputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelRequest(typing.TypedDict, total=False):
    outputConfig: GoogleCloudAiplatformV1ExportModelRequestOutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelRequestOutputConfig(
    typing.TypedDict, total=False
):
    artifactDestination: GoogleCloudAiplatformV1GcsDestination
    exportFormatId: str
    imageDestination: GoogleCloudAiplatformV1ContainerRegistryDestination

@typing.type_check_only
class GoogleCloudAiplatformV1ExportModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest(
    typing.TypedDict, total=False
):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    timeSeriesDataPoints: _list[GoogleCloudAiplatformV1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1ExternalApi(typing.TypedDict, total=False):
    apiAuth: GoogleCloudAiplatformV1ApiAuth
    apiSpec: typing.Literal["API_SPEC_UNSPECIFIED", "SIMPLE_SEARCH", "ELASTIC_SEARCH"]
    authConfig: GoogleCloudAiplatformV1AuthConfig
    elasticSearchParams: GoogleCloudAiplatformV1ExternalApiElasticSearchParams
    endpoint: str
    simpleSearchParams: GoogleCloudAiplatformV1ExternalApiSimpleSearchParams

@typing.type_check_only
class GoogleCloudAiplatformV1ExternalApiElasticSearchParams(
    typing.TypedDict, total=False
):
    index: str
    numHits: int
    searchTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1ExternalApiSimpleSearchParams(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1Fact(typing.TypedDict, total=False):
    chunk: GoogleCloudAiplatformV1RagChunk
    query: str
    score: float
    summary: str
    title: str
    uri: str
    vectorDistance: float

@typing.type_check_only
class GoogleCloudAiplatformV1FasterDeploymentConfig(typing.TypedDict, total=False):
    fastTryoutEnabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1Feature(typing.TypedDict, total=False):
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
    valueType: typing.Literal[
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
class GoogleCloudAiplatformV1FeatureGroup(typing.TypedDict, total=False):
    bigQuery: GoogleCloudAiplatformV1FeatureGroupBigQuery
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    serviceAccountEmail: str
    serviceAgentType: typing.Literal[
        "SERVICE_AGENT_TYPE_UNSPECIFIED",
        "SERVICE_AGENT_TYPE_PROJECT",
        "SERVICE_AGENT_TYPE_FEATURE_GROUP",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureGroupBigQuery(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudAiplatformV1BigQuerySource
    dense: bool
    entityIdColumns: _list[str]
    staticDataSource: bool
    timeSeries: GoogleCloudAiplatformV1FeatureGroupBigQueryTimeSeries

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureGroupBigQueryTimeSeries(
    typing.TypedDict, total=False
):
    timestampColumn: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureMonitoringStatsAnomaly(
    typing.TypedDict, total=False
):
    featureStatsAnomaly: GoogleCloudAiplatformV1FeatureStatsAnomaly
    objective: typing.Literal[
        "OBJECTIVE_UNSPECIFIED", "IMPORT_FEATURE_ANALYSIS", "SNAPSHOT_ANALYSIS"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureNoiseSigma(typing.TypedDict, total=False):
    noiseSigma: _list[GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeature]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeature(
    typing.TypedDict, total=False
):
    name: str
    sigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStore(typing.TypedDict, total=False):
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
    state: typing.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreBigtable(typing.TypedDict, total=False):
    autoScaling: GoogleCloudAiplatformV1FeatureOnlineStoreBigtableAutoScaling
    bigtableMetadata: GoogleCloudAiplatformV1FeatureOnlineStoreBigtableBigtableMetadata
    enableDirectBigtableAccess: bool
    zone: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreBigtableAutoScaling(
    typing.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreBigtableBigtableMetadata(
    typing.TypedDict, total=False
):
    instanceId: str
    tableId: str
    tenantProjectId: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreDedicatedServingEndpoint(
    typing.TypedDict, total=False
):
    privateServiceConnectConfig: GoogleCloudAiplatformV1PrivateServiceConnectConfig
    publicEndpointDomainName: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreOptimized(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureSelector(typing.TypedDict, total=False):
    idMatcher: GoogleCloudAiplatformV1IdMatcher

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureStatsAnomaly(typing.TypedDict, total=False):
    anomalyDetectionThreshold: float
    anomalyUri: str
    distributionDeviation: float
    endTime: str
    score: float
    startTime: str
    statsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureValue(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1FeatureValueDestination(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    csvDestination: GoogleCloudAiplatformV1CsvDestination
    tfrecordDestination: GoogleCloudAiplatformV1TFRecordDestination

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureValueList(typing.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1FeatureValue]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureValueMetadata(typing.TypedDict, total=False):
    generateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureView(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudAiplatformV1FeatureViewBigQuerySource
    bigtableMetadata: GoogleCloudAiplatformV1FeatureViewBigtableMetadata
    createTime: str
    etag: str
    featureRegistrySource: GoogleCloudAiplatformV1FeatureViewFeatureRegistrySource
    indexConfig: GoogleCloudAiplatformV1FeatureViewIndexConfig
    labels: dict[str, typing.Any]
    name: str
    optimizedConfig: GoogleCloudAiplatformV1FeatureViewOptimizedConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceAccountEmail: str
    serviceAgentType: typing.Literal[
        "SERVICE_AGENT_TYPE_UNSPECIFIED",
        "SERVICE_AGENT_TYPE_PROJECT",
        "SERVICE_AGENT_TYPE_FEATURE_VIEW",
    ]
    syncConfig: GoogleCloudAiplatformV1FeatureViewSyncConfig
    updateTime: str
    vertexRagSource: GoogleCloudAiplatformV1FeatureViewVertexRagSource

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewBigQuerySource(typing.TypedDict, total=False):
    entityIdColumns: _list[str]
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewBigtableMetadata(typing.TypedDict, total=False):
    readAppProfile: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDataKey(typing.TypedDict, total=False):
    compositeKey: GoogleCloudAiplatformV1FeatureViewDataKeyCompositeKey
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDataKeyCompositeKey(
    typing.TypedDict, total=False
):
    parts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDirectWriteRequest(
    typing.TypedDict, total=False
):
    dataKeyAndFeatureValues: _list[
        GoogleCloudAiplatformV1FeatureViewDirectWriteRequestDataKeyAndFeatureValues
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDirectWriteRequestDataKeyAndFeatureValues(
    typing.TypedDict, total=False
):
    dataKey: GoogleCloudAiplatformV1FeatureViewDataKey
    features: _list[
        GoogleCloudAiplatformV1FeatureViewDirectWriteRequestDataKeyAndFeatureValuesFeature
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDirectWriteRequestDataKeyAndFeatureValuesFeature(
    typing.TypedDict, total=False
):
    name: str
    value: GoogleCloudAiplatformV1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDirectWriteResponse(
    typing.TypedDict, total=False
):
    status: GoogleRpcStatus
    writeResponses: _list[
        GoogleCloudAiplatformV1FeatureViewDirectWriteResponseWriteResponse
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewDirectWriteResponseWriteResponse(
    typing.TypedDict, total=False
):
    dataKey: GoogleCloudAiplatformV1FeatureViewDataKey
    onlineStoreWriteTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewFeatureRegistrySource(
    typing.TypedDict, total=False
):
    featureGroups: _list[
        GoogleCloudAiplatformV1FeatureViewFeatureRegistrySourceFeatureGroup
    ]
    projectNumber: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewFeatureRegistrySourceFeatureGroup(
    typing.TypedDict, total=False
):
    featureGroupId: str
    featureIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewIndexConfig(typing.TypedDict, total=False):
    bruteForceConfig: GoogleCloudAiplatformV1FeatureViewIndexConfigBruteForceConfig
    crowdingColumn: str
    distanceMeasureType: typing.Literal[
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
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewIndexConfigTreeAHConfig(
    typing.TypedDict, total=False
):
    leafNodeEmbeddingCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewOptimizedConfig(typing.TypedDict, total=False):
    automaticResources: GoogleCloudAiplatformV1AutomaticResources

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSync(typing.TypedDict, total=False):
    createTime: str
    finalStatus: GoogleRpcStatus
    name: str
    runTime: GoogleTypeInterval
    satisfiesPzi: bool
    satisfiesPzs: bool
    syncSummary: GoogleCloudAiplatformV1FeatureViewSyncSyncSummary

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSyncConfig(typing.TypedDict, total=False):
    continuous: bool
    cron: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSyncSyncSummary(typing.TypedDict, total=False):
    rowSynced: str
    systemWatermarkTime: str
    totalSlot: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewVertexRagSource(typing.TypedDict, total=False):
    ragCorpusId: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1Featurestore(typing.TypedDict, total=False):
    createTime: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    onlineServingConfig: GoogleCloudAiplatformV1FeaturestoreOnlineServingConfig
    onlineStorageTtlDays: int
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfig(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    anomalyDetectionBaseline: typing.Literal[
        "BASELINE_UNSPECIFIED",
        "LATEST_STATS",
        "MOST_RECENT_SNAPSHOT_STATS",
        "PREVIOUS_IMPORT_FEATURES_STATS",
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "DEFAULT", "ENABLED", "DISABLED"]

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfigSnapshotAnalysis(
    typing.TypedDict, total=False
):
    disabled: bool
    monitoringIntervalDays: int
    stalenessDays: int

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreMonitoringConfigThresholdConfig(
    typing.TypedDict, total=False
):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreOnlineServingConfig(
    typing.TypedDict, total=False
):
    fixedNodeCount: int
    scaling: GoogleCloudAiplatformV1FeaturestoreOnlineServingConfigScaling

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreOnlineServingConfigScaling(
    typing.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesRequest(typing.TypedDict, total=False):
    dataFormat: typing.Literal[
        "FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED", "KEY_VALUE", "PROTO_STRUCT"
    ]
    dataKey: GoogleCloudAiplatformV1FeatureViewDataKey

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesResponse(typing.TypedDict, total=False):
    dataKey: GoogleCloudAiplatformV1FeatureViewDataKey
    keyValues: GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairList
    protoStruct: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairList(
    typing.TypedDict, total=False
):
    features: _list[
        GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair(
    typing.TypedDict, total=False
):
    name: str
    value: GoogleCloudAiplatformV1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1FetchPredictOperationRequest(
    typing.TypedDict, total=False
):
    operationName: str

@typing.type_check_only
class GoogleCloudAiplatformV1FileData(typing.TypedDict, total=False):
    displayName: str
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1FileStatus(typing.TypedDict, total=False):
    errorStatus: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ERROR"]

@typing.type_check_only
class GoogleCloudAiplatformV1FilterSplit(typing.TypedDict, total=False):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsRequest(typing.TypedDict, total=False):
    deployedIndexId: str
    queries: _list[GoogleCloudAiplatformV1FindNeighborsRequestQuery]
    returnFullDatapoint: bool

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsRequestQuery(typing.TypedDict, total=False):
    approximateNeighborCount: int
    datapoint: GoogleCloudAiplatformV1IndexDatapoint
    fractionLeafNodesToSearchOverride: float
    neighborCount: int
    perCrowdingAttributeNeighborCount: int
    rrf: GoogleCloudAiplatformV1FindNeighborsRequestQueryRRF

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsRequestQueryRRF(
    typing.TypedDict, total=False
):
    alpha: float

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponse(typing.TypedDict, total=False):
    nearestNeighbors: _list[
        GoogleCloudAiplatformV1FindNeighborsResponseNearestNeighbors
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponseNearestNeighbors(
    typing.TypedDict, total=False
):
    id: str
    neighbors: _list[GoogleCloudAiplatformV1FindNeighborsResponseNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponseNeighbor(
    typing.TypedDict, total=False
):
    datapoint: GoogleCloudAiplatformV1IndexDatapoint
    distance: float
    sparseDistance: float

@typing.type_check_only
class GoogleCloudAiplatformV1FluencyInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1FluencyInstance
    metricSpec: GoogleCloudAiplatformV1FluencySpec

@typing.type_check_only
class GoogleCloudAiplatformV1FluencyInstance(typing.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1FluencyResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1FluencySpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1FractionSplit(typing.TypedDict, total=False):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1FulfillmentInstance
    metricSpec: GoogleCloudAiplatformV1FulfillmentSpec

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentInstance(typing.TypedDict, total=False):
    instruction: str
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1FulfillmentSpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionCall(typing.TypedDict, total=False):
    args: dict[str, typing.Any]
    id: str
    name: str
    partialArgs: _list[GoogleCloudAiplatformV1PartialArg]
    willContinue: bool

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionCallingConfig(typing.TypedDict, total=False):
    allowedFunctionNames: _list[str]
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO", "ANY", "NONE", "VALIDATED"]
    streamFunctionCallArguments: bool

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionDeclaration(typing.TypedDict, total=False):
    behavior: typing.Literal["UNSPECIFIED", "BLOCKING", "NON_BLOCKING"]
    description: str
    name: str
    parameters: GoogleCloudAiplatformV1Schema
    parametersJsonSchema: typing.Any
    response: GoogleCloudAiplatformV1Schema
    responseJsonSchema: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionResponse(typing.TypedDict, total=False):
    id: str
    name: str
    parts: _list[GoogleCloudAiplatformV1FunctionResponsePart]
    response: dict[str, typing.Any]
    scheduling: typing.Literal[
        "SCHEDULING_UNSPECIFIED", "SILENT", "WHEN_IDLE", "INTERRUPT"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionResponseBlob(typing.TypedDict, total=False):
    data: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionResponseFileData(typing.TypedDict, total=False):
    displayName: str
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1FunctionResponsePart(typing.TypedDict, total=False):
    fileData: GoogleCloudAiplatformV1FunctionResponseFileData
    inlineData: GoogleCloudAiplatformV1FunctionResponseBlob

@typing.type_check_only
class GoogleCloudAiplatformV1GatewayConfig(typing.TypedDict, total=False):
    allowedProjects: _list[str]
    dnsRecord: str
    dnsZoneName: str
    ipAddress: str
    network: str
    pscEndpoint: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "ACTIVE",
        "DEPROVISIONING",
        "INACTIVE",
        "FAILED",
    ]
    subnetwork: str

@typing.type_check_only
class GoogleCloudAiplatformV1GcsDestination(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudAiplatformV1GcsSource(typing.TypedDict, total=False):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1GdcConfig(typing.TypedDict, total=False):
    zone: str

@typing.type_check_only
class GoogleCloudAiplatformV1GeminiAgentConfig(typing.TypedDict, total=False):
    geminiAgent: str

@typing.type_check_only
class GoogleCloudAiplatformV1GeminiPreferenceExample(typing.TypedDict, total=False):
    completions: _list[GoogleCloudAiplatformV1GeminiPreferenceExampleCompletion]
    contents: _list[GoogleCloudAiplatformV1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1GeminiPreferenceExampleCompletion(
    typing.TypedDict, total=False
):
    completion: GoogleCloudAiplatformV1Content
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1GenAiAdvancedFeaturesConfig(typing.TypedDict, total=False):
    ragConfig: GoogleCloudAiplatformV1GenAiAdvancedFeaturesConfigRagConfig

@typing.type_check_only
class GoogleCloudAiplatformV1GenAiAdvancedFeaturesConfigRagConfig(
    typing.TypedDict, total=False
):
    enableRag: bool

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentRequest(typing.TypedDict, total=False):
    cachedContent: str
    contents: _list[GoogleCloudAiplatformV1Content]
    generationConfig: GoogleCloudAiplatformV1GenerationConfig
    labels: dict[str, typing.Any]
    modelArmorConfig: GoogleCloudAiplatformV1ModelArmorConfig
    safetySettings: _list[GoogleCloudAiplatformV1SafetySetting]
    systemInstruction: GoogleCloudAiplatformV1Content
    toolConfig: GoogleCloudAiplatformV1ToolConfig
    tools: _list[GoogleCloudAiplatformV1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponse(typing.TypedDict, total=False):
    candidates: _list[GoogleCloudAiplatformV1Candidate]
    createTime: str
    modelVersion: str
    promptFeedback: GoogleCloudAiplatformV1GenerateContentResponsePromptFeedback
    responseId: str
    usageMetadata: GoogleCloudAiplatformV1GenerateContentResponseUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponsePromptFeedback(
    typing.TypedDict, total=False
):
    blockReason: typing.Literal[
        "BLOCKED_REASON_UNSPECIFIED",
        "SAFETY",
        "OTHER",
        "BLOCKLIST",
        "PROHIBITED_CONTENT",
        "MODEL_ARMOR",
        "IMAGE_SAFETY",
        "JAILBREAK",
    ]
    blockReasonMessage: str
    safetyRatings: _list[GoogleCloudAiplatformV1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponseUsageMetadata(
    typing.TypedDict, total=False
):
    cacheTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    cachedContentTokenCount: int
    candidatesTokenCount: int
    candidatesTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    promptTokenCount: int
    promptTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    thoughtsTokenCount: int
    toolUsePromptTokenCount: int
    toolUsePromptTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    totalTokenCount: int
    trafficType: typing.Literal[
        "TRAFFIC_TYPE_UNSPECIFIED",
        "ON_DEMAND",
        "ON_DEMAND_PRIORITY",
        "ON_DEMAND_FLEX",
        "ON_DEMAND_OFFPEAK",
        "PROVISIONED_THROUGHPUT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateFetchAccessTokenRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateFetchAccessTokenResponse(
    typing.TypedDict, total=False
):
    accessToken: str
    expireTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateInstanceRubricsRequest(
    typing.TypedDict, total=False
):
    agentConfig: GoogleCloudAiplatformV1EvaluationInstanceDeprecatedAgentConfig
    contents: _list[GoogleCloudAiplatformV1Content]
    location: str
    metricResourceName: str
    predefinedRubricGenerationSpec: GoogleCloudAiplatformV1PredefinedMetricSpec
    rubricGenerationSpec: GoogleCloudAiplatformV1RubricGenerationSpec

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateInstanceRubricsResponse(
    typing.TypedDict, total=False
):
    generatedRubrics: _list[GoogleCloudAiplatformV1Rubric]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateLossClustersRequest(typing.TypedDict, total=False):
    configs: _list[GoogleCloudAiplatformV1LossAnalysisConfig]
    evaluationSet: str
    inlineResults: (
        GoogleCloudAiplatformV1GenerateLossClustersRequestEvaluationResultList
    )

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateLossClustersRequestEvaluationResultList(
    typing.TypedDict, total=False
):
    evaluationResults: _list[GoogleCloudAiplatformV1EvaluationResult]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateMemoriesRequest(typing.TypedDict, total=False):
    allowedTopics: _list[GoogleCloudAiplatformV1MemoryTopicId]
    directContentsSource: (
        GoogleCloudAiplatformV1GenerateMemoriesRequestDirectContentsSource
    )
    directMemoriesSource: (
        GoogleCloudAiplatformV1GenerateMemoriesRequestDirectMemoriesSource
    )
    disableConsolidation: bool
    disableMemoryRevisions: bool
    metadata: dict[str, typing.Any]
    metadataMergeStrategy: typing.Literal[
        "METADATA_MERGE_STRATEGY_UNSPECIFIED",
        "OVERWRITE",
        "MERGE",
        "REQUIRE_EXACT_MATCH",
    ]
    revisionExpireTime: str
    revisionLabels: dict[str, typing.Any]
    revisionTtl: str
    scope: dict[str, typing.Any]
    vertexSessionSource: (
        GoogleCloudAiplatformV1GenerateMemoriesRequestVertexSessionSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateMemoriesRequestDirectContentsSource(
    typing.TypedDict, total=False
):
    events: _list[
        GoogleCloudAiplatformV1GenerateMemoriesRequestDirectContentsSourceEvent
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateMemoriesRequestDirectContentsSourceEvent(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1Content

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateMemoriesRequestDirectMemoriesSource(
    typing.TypedDict, total=False
):
    directMemories: _list[
        GoogleCloudAiplatformV1GenerateMemoriesRequestDirectMemoriesSourceDirectMemory
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateMemoriesRequestDirectMemoriesSourceDirectMemory(
    typing.TypedDict, total=False
):
    fact: str
    topics: _list[GoogleCloudAiplatformV1MemoryTopicId]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateMemoriesRequestVertexSessionSource(
    typing.TypedDict, total=False
):
    endTime: str
    session: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateSyntheticDataRequest(
    typing.TypedDict, total=False
):
    count: int
    examples: _list[GoogleCloudAiplatformV1SyntheticExample]
    outputFieldSpecs: _list[GoogleCloudAiplatformV1OutputFieldSpec]
    taskDescription: GoogleCloudAiplatformV1TaskDescriptionStrategy

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateSyntheticDataResponse(
    typing.TypedDict, total=False
):
    syntheticExamples: _list[GoogleCloudAiplatformV1SyntheticExample]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateUserScenariosRequest(
    typing.TypedDict, total=False
):
    agents: dict[str, typing.Any]
    allowCrossRegionModel: bool
    geminiAgentConfig: GoogleCloudAiplatformV1GeminiAgentConfig
    rootAgentId: str
    userScenarioGenerationConfig: GoogleCloudAiplatformV1UserScenarioGenerationConfig

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateUserScenariosResponse(
    typing.TypedDict, total=False
):
    userScenarios: _list[GoogleCloudAiplatformV1UserScenario]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateVideoResponse(typing.TypedDict, total=False):
    generatedSamples: _list[str]
    raiMediaFilteredCount: int
    raiMediaFilteredReasons: _list[str]
    videos: _list[GoogleCloudAiplatformV1GenerateVideoResponseVideo]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateVideoResponseVideo(typing.TypedDict, total=False):
    bytesBase64Encoded: str
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfig(typing.TypedDict, total=False):
    audioTimestamp: bool
    audioTranscriptionConfig: GoogleCloudAiplatformV1AudioTranscriptionConfig
    candidateCount: int
    enableAffectiveDialog: bool
    frequencyPenalty: float
    imageConfig: GoogleCloudAiplatformV1ImageConfig
    logprobs: int
    maxOutputTokens: int
    mediaResolution: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED",
        "MEDIA_RESOLUTION_LOW",
        "MEDIA_RESOLUTION_MEDIUM",
        "MEDIA_RESOLUTION_HIGH",
    ]
    presencePenalty: float
    responseFormat: _list[GoogleCloudAiplatformV1ResponseFormat]
    responseJsonSchema: typing.Any
    responseLogprobs: bool
    responseMimeType: str
    responseModalities: _list[
        typing.Literal["MODALITY_UNSPECIFIED", "TEXT", "IMAGE", "AUDIO", "VIDEO"]
    ]
    responseSchema: GoogleCloudAiplatformV1Schema
    routingConfig: GoogleCloudAiplatformV1GenerationConfigRoutingConfig
    seed: int
    speechConfig: GoogleCloudAiplatformV1SpeechConfig
    stopSequences: _list[str]
    temperature: float
    thinkingConfig: GoogleCloudAiplatformV1GenerationConfigThinkingConfig
    topK: float
    topP: float

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfigRoutingConfig(
    typing.TypedDict, total=False
):
    autoMode: GoogleCloudAiplatformV1GenerationConfigRoutingConfigAutoRoutingMode
    manualMode: GoogleCloudAiplatformV1GenerationConfigRoutingConfigManualRoutingMode

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfigRoutingConfigAutoRoutingMode(
    typing.TypedDict, total=False
):
    modelRoutingPreference: typing.Literal[
        "UNKNOWN", "PRIORITIZE_QUALITY", "BALANCED", "PRIORITIZE_COST"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfigRoutingConfigManualRoutingMode(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1GenerationConfigThinkingConfig(
    typing.TypedDict, total=False
):
    includeThoughts: bool
    thinkingBudget: int
    thinkingLevel: typing.Literal[
        "THINKING_LEVEL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "MINIMAL"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GenericOperationMetadata(typing.TypedDict, total=False):
    createTime: str
    partialFailures: _list[GoogleRpcStatus]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1GenieSource(typing.TypedDict, total=False):
    baseModelUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleDriveSource(typing.TypedDict, total=False):
    resourceIds: _list[GoogleCloudAiplatformV1GoogleDriveSourceResourceId]

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleDriveSourceResourceId(typing.TypedDict, total=False):
    resourceId: str
    resourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "RESOURCE_TYPE_FILE", "RESOURCE_TYPE_FOLDER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleMaps(typing.TypedDict, total=False):
    enableWidget: bool
    groundingTypes: GoogleCloudAiplatformV1GoogleMapsGroundingTypes

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleMapsGroundingTypes(typing.TypedDict, total=False):
    places: GoogleCloudAiplatformV1GoogleMapsPlaces
    routing: GoogleCloudAiplatformV1GoogleMapsRouting

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleMapsPlaces(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleMapsRouting(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1GoogleSearchRetrieval(typing.TypedDict, total=False):
    dynamicRetrievalConfig: GoogleCloudAiplatformV1DynamicRetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1GroundednessInstance
    metricSpec: GoogleCloudAiplatformV1GroundednessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessInstance(typing.TypedDict, total=False):
    context: str
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1GroundednessSpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunk(typing.TypedDict, total=False):
    image: GoogleCloudAiplatformV1GroundingChunkImage
    maps: GoogleCloudAiplatformV1GroundingChunkMaps
    retrievedContext: GoogleCloudAiplatformV1GroundingChunkRetrievedContext
    web: GoogleCloudAiplatformV1GroundingChunkWeb

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkImage(typing.TypedDict, total=False):
    domain: str
    imageUri: str
    sourceUri: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkMaps(typing.TypedDict, total=False):
    placeAnswerSources: GoogleCloudAiplatformV1GroundingChunkMapsPlaceAnswerSources
    placeId: str
    route: GoogleCloudAiplatformV1GroundingChunkMapsRoute
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkMapsPlaceAnswerSources(
    typing.TypedDict, total=False
):
    reviewSnippets: _list[
        GoogleCloudAiplatformV1GroundingChunkMapsPlaceAnswerSourcesReviewSnippet
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkMapsPlaceAnswerSourcesReviewSnippet(
    typing.TypedDict, total=False
):
    googleMapsUri: str
    reviewId: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkMapsRoute(typing.TypedDict, total=False):
    distanceMeters: int
    duration: str
    encodedPolyline: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkRetrievedContext(
    typing.TypedDict, total=False
):
    documentName: str
    ragChunk: GoogleCloudAiplatformV1RagChunk
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingChunkWeb(typing.TypedDict, total=False):
    domain: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingMetadata(typing.TypedDict, total=False):
    googleMapsWidgetContextToken: str
    groundingChunks: _list[GoogleCloudAiplatformV1GroundingChunk]
    groundingSupports: _list[GoogleCloudAiplatformV1GroundingSupport]
    imageSearchQueries: _list[str]
    retrievalMetadata: GoogleCloudAiplatformV1RetrievalMetadata
    retrievalQueries: _list[str]
    searchEntryPoint: GoogleCloudAiplatformV1SearchEntryPoint
    sourceFlaggingUris: _list[GoogleCloudAiplatformV1GroundingMetadataSourceFlaggingUri]
    webSearchQueries: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingMetadataSourceFlaggingUri(
    typing.TypedDict, total=False
):
    flagContentUri: str
    sourceId: str

@typing.type_check_only
class GoogleCloudAiplatformV1GroundingSupport(typing.TypedDict, total=False):
    confidenceScores: _list[float]
    groundingChunkIndices: _list[int]
    renderedParts: _list[int]
    segment: GoogleCloudAiplatformV1Segment

@typing.type_check_only
class GoogleCloudAiplatformV1HyperparameterTuningJob(typing.TypedDict, total=False):
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
    state: typing.Literal[
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
class GoogleCloudAiplatformV1IdMatcher(typing.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ImageConfig(typing.TypedDict, total=False):
    aspectRatio: str
    imageOutputOptions: GoogleCloudAiplatformV1ImageConfigImageOutputOptions
    imageSize: str
    personGeneration: typing.Literal[
        "PERSON_GENERATION_UNSPECIFIED", "ALLOW_ALL", "ALLOW_ADULT", "ALLOW_NONE"
    ]
    prominentPeople: typing.Literal[
        "PROMINENT_PEOPLE_UNSPECIFIED",
        "ALLOW_PROMINENT_PEOPLE",
        "BLOCK_PROMINENT_PEOPLE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ImageConfigImageOutputOptions(
    typing.TypedDict, total=False
):
    compressionQuality: int
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImageResponseFormat(typing.TypedDict, total=False):
    aspectRatio: typing.Literal[
        "ASPECT_RATIO_UNSPECIFIED",
        "ASPECT_RATIO_ONE_BY_ONE",
        "ASPECT_RATIO_TWO_BY_THREE",
        "ASPECT_RATIO_THREE_BY_TWO",
        "ASPECT_RATIO_THREE_BY_FOUR",
        "ASPECT_RATIO_FOUR_BY_THREE",
        "ASPECT_RATIO_FOUR_BY_FIVE",
        "ASPECT_RATIO_FIVE_BY_FOUR",
        "ASPECT_RATIO_NINE_BY_SIXTEEN",
        "ASPECT_RATIO_SIXTEEN_BY_NINE",
        "ASPECT_RATIO_TWENTY_ONE_BY_NINE",
        "ASPECT_RATIO_ONE_BY_EIGHT",
        "ASPECT_RATIO_EIGHT_BY_ONE",
        "ASPECT_RATIO_ONE_BY_FOUR",
        "ASPECT_RATIO_FOUR_BY_ONE",
    ]
    delivery: typing.Literal["DELIVERY_UNSPECIFIED", "INLINE", "URI"]
    imageSize: typing.Literal[
        "IMAGE_SIZE_UNSPECIFIED",
        "IMAGE_SIZE_FIVE_TWELVE",
        "IMAGE_SIZE_ONE_K",
        "IMAGE_SIZE_TWO_K",
        "IMAGE_SIZE_FOUR_K",
    ]
    mimeType: typing.Literal["MIME_TYPE_UNSPECIFIED", "IMAGE_JPEG"]

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataConfig(typing.TypedDict, total=False):
    annotationLabels: dict[str, typing.Any]
    dataItemLabels: dict[str, typing.Any]
    gcsSource: GoogleCloudAiplatformV1GcsSource
    importSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataOperationMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataRequest(typing.TypedDict, total=False):
    importConfigs: _list[GoogleCloudAiplatformV1ImportDataConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1ImportDataResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ImportEvaluationSetRequest(typing.TypedDict, total=False):
    agentEngineSource: (
        GoogleCloudAiplatformV1ImportEvaluationSetRequestAgentEngineSource
    )
    bigquerySource: GoogleCloudAiplatformV1BigQueryRequestSet
    cloudTraceSource: GoogleCloudAiplatformV1ImportEvaluationSetRequestCloudTraceSource
    evaluationSet: GoogleCloudAiplatformV1EvaluationSet
    gcsDestination: GoogleCloudAiplatformV1GcsDestination
    gcsSource: GoogleCloudAiplatformV1ImportEvaluationSetRequestGcsSource
    inlineSource: GoogleCloudAiplatformV1ImportEvaluationSetRequestInlineSource
    interactionsSource: (
        GoogleCloudAiplatformV1ImportEvaluationSetRequestInteractionsSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1ImportEvaluationSetRequestAgentEngineSource(
    typing.TypedDict, total=False
):
    location: str
    projectId: str
    reasoningEngineId: str
    sessionIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ImportEvaluationSetRequestCloudTraceSource(
    typing.TypedDict, total=False
):
    projectId: str
    sessionIds: _list[str]
    traceIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ImportEvaluationSetRequestGcsSource(
    typing.TypedDict, total=False
):
    gcsUri: str
    importSchemaConfig: (
        GoogleCloudAiplatformV1ImportEvaluationSetRequestImportSchemaConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1ImportEvaluationSetRequestImportSchemaConfig(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal[
        "DATA_FORMAT_UNSPECIFIED", "OTEL_PROTO", "OTEL_JSON", "JSONL"
    ]
    dataFormatVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportEvaluationSetRequestInlineSource(
    typing.TypedDict, total=False
):
    content: str
    importSchemaConfig: (
        GoogleCloudAiplatformV1ImportEvaluationSetRequestImportSchemaConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1ImportEvaluationSetRequestInteractionsSource(
    typing.TypedDict, total=False
):
    geminiAgentConfig: GoogleCloudAiplatformV1GeminiAgentConfig
    interactions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ImportFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
):
    blockingOperationIds: _list[str]
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    sourceUris: _list[str]
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportFeatureValuesRequest(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    id: str
    sourceField: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportFeatureValuesResponse(typing.TypedDict, total=False):
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ImportModelEvaluationRequest(
    typing.TypedDict, total=False
):
    modelEvaluation: GoogleCloudAiplatformV1ModelEvaluation

@typing.type_check_only
class GoogleCloudAiplatformV1ImportRagFilesConfig(typing.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1GcsSource
    googleDriveSource: GoogleCloudAiplatformV1GoogleDriveSource
    importResultBigquerySink: GoogleCloudAiplatformV1BigQueryDestination
    importResultGcsSink: GoogleCloudAiplatformV1GcsDestination
    jiraSource: GoogleCloudAiplatformV1JiraSource
    maxEmbeddingRequestsPerMin: int
    partialFailureBigquerySink: GoogleCloudAiplatformV1BigQueryDestination
    partialFailureGcsSink: GoogleCloudAiplatformV1GcsDestination
    ragFileParsingConfig: GoogleCloudAiplatformV1RagFileParsingConfig
    ragFileTransformationConfig: GoogleCloudAiplatformV1RagFileTransformationConfig
    rebuildAnnIndex: bool
    sharePointSources: GoogleCloudAiplatformV1SharePointSources
    slackSource: GoogleCloudAiplatformV1SlackSource

@typing.type_check_only
class GoogleCloudAiplatformV1ImportRagFilesRequest(typing.TypedDict, total=False):
    importRagFilesConfig: GoogleCloudAiplatformV1ImportRagFilesConfig

@typing.type_check_only
class GoogleCloudAiplatformV1Index(typing.TypedDict, total=False):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1DeployedIndexRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    indexStats: GoogleCloudAiplatformV1IndexStats
    indexUpdateMethod: typing.Literal[
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
class GoogleCloudAiplatformV1IndexDatapoint(typing.TypedDict, total=False):
    crowdingTag: GoogleCloudAiplatformV1IndexDatapointCrowdingTag
    datapointId: str
    embeddingMetadata: dict[str, typing.Any]
    featureVector: _list[float]
    numericRestricts: _list[GoogleCloudAiplatformV1IndexDatapointNumericRestriction]
    restricts: _list[GoogleCloudAiplatformV1IndexDatapointRestriction]
    sparseEmbedding: GoogleCloudAiplatformV1IndexDatapointSparseEmbedding

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapointCrowdingTag(typing.TypedDict, total=False):
    crowdingAttribute: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapointNumericRestriction(
    typing.TypedDict, total=False
):
    namespace: str
    op: typing.Literal[
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
class GoogleCloudAiplatformV1IndexDatapointRestriction(typing.TypedDict, total=False):
    allowList: _list[str]
    denyList: _list[str]
    namespace: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexDatapointSparseEmbedding(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1IndexEndpoint(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1IndexPrivateEndpoints(typing.TypedDict, total=False):
    matchGrpcAddress: str
    pscAutomatedEndpoints: _list[GoogleCloudAiplatformV1PscAutomatedEndpoints]
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1IndexStats(typing.TypedDict, total=False):
    shardsCount: int
    sparseVectorsCount: str
    vectorsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1IngestEventsRequest(typing.TypedDict, total=False):
    directContentsSource: GoogleCloudAiplatformV1IngestionDirectContentsSource
    disableMemoryRevisions: bool
    forceFlush: bool
    generationTriggerConfig: GoogleCloudAiplatformV1MemoryGenerationTriggerConfig
    metadata: dict[str, typing.Any]
    metadataMergeStrategy: typing.Literal[
        "METADATA_MERGE_STRATEGY_UNSPECIFIED",
        "OVERWRITE",
        "MERGE",
        "REQUIRE_EXACT_MATCH",
    ]
    revisionExpireTime: str
    revisionLabels: dict[str, typing.Any]
    revisionTtl: str
    scope: dict[str, typing.Any]
    streamId: str

@typing.type_check_only
class GoogleCloudAiplatformV1IngestionDirectContentsSource(
    typing.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1IngestionDirectContentsSourceEvent]

@typing.type_check_only
class GoogleCloudAiplatformV1IngestionDirectContentsSourceEvent(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1Content
    eventId: str
    eventTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1InputDataConfig(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1Int64Array(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1IntegratedGradientsAttribution(
    typing.TypedDict, total=False
):
    blurBaselineConfig: GoogleCloudAiplatformV1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1SmoothGradConfig
    stepCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1IntermediateExtractedMemory(typing.TypedDict, total=False):
    context: str
    fact: str
    structuredData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1InvokeRequest(typing.TypedDict, total=False):
    deployedModelId: str
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1JiraSource(typing.TypedDict, total=False):
    jiraQueries: _list[GoogleCloudAiplatformV1JiraSourceJiraQueries]

@typing.type_check_only
class GoogleCloudAiplatformV1JiraSourceJiraQueries(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1ApiAuthApiKeyConfig
    customQueries: _list[str]
    email: str
    projects: _list[str]
    serverUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1KeepAliveProbe(typing.TypedDict, total=False):
    httpGet: GoogleCloudAiplatformV1KeepAliveProbeHttpGet
    maxSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1KeepAliveProbeHttpGet(typing.TypedDict, total=False):
    path: str
    port: int

@typing.type_check_only
class GoogleCloudAiplatformV1LLMBasedMetricSpec(typing.TypedDict, total=False):
    additionalConfig: dict[str, typing.Any]
    judgeAutoraterConfig: GoogleCloudAiplatformV1AutoraterConfig
    metricPromptTemplate: str
    predefinedRubricGenerationSpec: GoogleCloudAiplatformV1PredefinedMetricSpec
    resultParserConfig: GoogleCloudAiplatformV1EvaluationParserConfig
    rubricGenerationSpec: GoogleCloudAiplatformV1RubricGenerationSpec
    rubricGroupKey: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1LargeModelReference(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1LineageSubgraph(typing.TypedDict, total=False):
    artifacts: _list[GoogleCloudAiplatformV1Artifact]
    events: _list[GoogleCloudAiplatformV1Event]
    executions: _list[GoogleCloudAiplatformV1Execution]

@typing.type_check_only
class GoogleCloudAiplatformV1ListAgentsResponse(typing.TypedDict, total=False):
    agents: _list[GoogleCloudAiplatformV1Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListAnnotationsResponse(typing.TypedDict, total=False):
    annotations: _list[GoogleCloudAiplatformV1Annotation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListArtifactsResponse(typing.TypedDict, total=False):
    artifacts: _list[GoogleCloudAiplatformV1Artifact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListBatchPredictionJobsResponse(
    typing.TypedDict, total=False
):
    batchPredictionJobs: _list[GoogleCloudAiplatformV1BatchPredictionJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListCachedContentsResponse(typing.TypedDict, total=False):
    cachedContents: _list[GoogleCloudAiplatformV1CachedContent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListContextsResponse(typing.TypedDict, total=False):
    contexts: _list[GoogleCloudAiplatformV1Context]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListCustomJobsResponse(typing.TypedDict, total=False):
    customJobs: _list[GoogleCloudAiplatformV1CustomJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataItemsResponse(typing.TypedDict, total=False):
    dataItems: _list[GoogleCloudAiplatformV1DataItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataLabelingJobsResponse(
    typing.TypedDict, total=False
):
    dataLabelingJobs: _list[GoogleCloudAiplatformV1DataLabelingJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetVersionsResponse(typing.TypedDict, total=False):
    datasetVersions: _list[GoogleCloudAiplatformV1DatasetVersion]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetsResponse(typing.TypedDict, total=False):
    datasets: _list[GoogleCloudAiplatformV1Dataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse(
    typing.TypedDict, total=False
):
    deploymentResourcePools: _list[GoogleCloudAiplatformV1DeploymentResourcePool]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEndpointsResponse(typing.TypedDict, total=False):
    endpoints: _list[GoogleCloudAiplatformV1Endpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEntityTypesResponse(typing.TypedDict, total=False):
    entityTypes: _list[GoogleCloudAiplatformV1EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEvaluationItemsResponse(typing.TypedDict, total=False):
    evaluationItems: _list[GoogleCloudAiplatformV1EvaluationItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEvaluationMetricsResponse(
    typing.TypedDict, total=False
):
    evaluationMetrics: _list[GoogleCloudAiplatformV1EvaluationMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEvaluationRunsResponse(typing.TypedDict, total=False):
    evaluationRuns: _list[GoogleCloudAiplatformV1EvaluationRun]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEvaluationSetsResponse(typing.TypedDict, total=False):
    evaluationSets: _list[GoogleCloudAiplatformV1EvaluationSet]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListEventsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessionEvents: _list[GoogleCloudAiplatformV1SessionEvent]

@typing.type_check_only
class GoogleCloudAiplatformV1ListExecutionsResponse(typing.TypedDict, total=False):
    executions: _list[GoogleCloudAiplatformV1Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureGroupsResponse(typing.TypedDict, total=False):
    featureGroups: _list[GoogleCloudAiplatformV1FeatureGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse(
    typing.TypedDict, total=False
):
    featureOnlineStores: _list[GoogleCloudAiplatformV1FeatureOnlineStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureViewSyncsResponse(
    typing.TypedDict, total=False
):
    featureViewSyncs: _list[GoogleCloudAiplatformV1FeatureViewSync]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureViewsResponse(typing.TypedDict, total=False):
    featureViews: _list[GoogleCloudAiplatformV1FeatureView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturesResponse(typing.TypedDict, total=False):
    features: _list[GoogleCloudAiplatformV1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturestoresResponse(typing.TypedDict, total=False):
    featurestores: _list[GoogleCloudAiplatformV1Featurestore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse(
    typing.TypedDict, total=False
):
    hyperparameterTuningJobs: _list[GoogleCloudAiplatformV1HyperparameterTuningJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexEndpointsResponse(typing.TypedDict, total=False):
    indexEndpoints: _list[GoogleCloudAiplatformV1IndexEndpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexesResponse(typing.TypedDict, total=False):
    indexes: _list[GoogleCloudAiplatformV1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListMemoriesResponse(typing.TypedDict, total=False):
    memories: _list[GoogleCloudAiplatformV1Memory]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListMemoryRevisionsResponse(typing.TypedDict, total=False):
    memoryRevisions: _list[GoogleCloudAiplatformV1MemoryRevision]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataSchemasResponse(typing.TypedDict, total=False):
    metadataSchemas: _list[GoogleCloudAiplatformV1MetadataSchema]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataStoresResponse(typing.TypedDict, total=False):
    metadataStores: _list[GoogleCloudAiplatformV1MetadataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse(
    typing.TypedDict, total=False
):
    modelDeploymentMonitoringJobs: _list[
        GoogleCloudAiplatformV1ModelDeploymentMonitoringJob
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse(
    typing.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1ModelEvaluationSlice]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationsResponse(
    typing.TypedDict, total=False
):
    modelEvaluations: _list[GoogleCloudAiplatformV1ModelEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelVersionCheckpointsResponse(
    typing.TypedDict, total=False
):
    checkpoints: _list[GoogleCloudAiplatformV1ModelVersionCheckpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelVersionsResponse(typing.TypedDict, total=False):
    models: _list[GoogleCloudAiplatformV1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelsResponse(typing.TypedDict, total=False):
    models: _list[GoogleCloudAiplatformV1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasJobsResponse(typing.TypedDict, total=False):
    nasJobs: _list[GoogleCloudAiplatformV1NasJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasTrialDetailsResponse(typing.TypedDict, total=False):
    nasTrialDetails: _list[GoogleCloudAiplatformV1NasTrialDetail]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookExecutionJobsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notebookExecutionJobs: _list[GoogleCloudAiplatformV1NotebookExecutionJob]

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimeTemplates: _list[GoogleCloudAiplatformV1NotebookRuntimeTemplate]

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimes: _list[GoogleCloudAiplatformV1NotebookRuntime]

@typing.type_check_only
class GoogleCloudAiplatformV1ListOnlineEvaluatorsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    onlineEvaluators: _list[GoogleCloudAiplatformV1OnlineEvaluator]

@typing.type_check_only
class GoogleCloudAiplatformV1ListOptimalTrialsRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListOptimalTrialsResponse(typing.TypedDict, total=False):
    optimalTrials: _list[GoogleCloudAiplatformV1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1ListPersistentResourcesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    persistentResources: _list[GoogleCloudAiplatformV1PersistentResource]

@typing.type_check_only
class GoogleCloudAiplatformV1ListPipelineJobsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pipelineJobs: _list[GoogleCloudAiplatformV1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1ListRagCorporaResponse(typing.TypedDict, total=False):
    nextPageToken: str
    ragCorpora: _list[GoogleCloudAiplatformV1RagCorpus]

@typing.type_check_only
class GoogleCloudAiplatformV1ListRagFilesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    ragFiles: _list[GoogleCloudAiplatformV1RagFile]

@typing.type_check_only
class GoogleCloudAiplatformV1ListReasoningEnginesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    reasoningEngines: _list[GoogleCloudAiplatformV1ReasoningEngine]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSandboxEnvironmentSnapshotsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sandboxEnvironmentSnapshots: _list[
        GoogleCloudAiplatformV1SandboxEnvironmentSnapshot
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSandboxEnvironmentTemplatesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sandboxEnvironmentTemplates: _list[
        GoogleCloudAiplatformV1SandboxEnvironmentTemplate
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSandboxEnvironmentsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sandboxEnvironments: _list[GoogleCloudAiplatformV1SandboxEnvironment]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSavedQueriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    savedQueries: _list[GoogleCloudAiplatformV1SavedQuery]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSchedulesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schedules: _list[GoogleCloudAiplatformV1Schedule]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSemanticGovernancePoliciesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    semanticGovernancePolicies: _list[GoogleCloudAiplatformV1SemanticGovernancePolicy]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[GoogleCloudAiplatformV1Session]

@typing.type_check_only
class GoogleCloudAiplatformV1ListSpecialistPoolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    specialistPools: _list[GoogleCloudAiplatformV1SpecialistPool]

@typing.type_check_only
class GoogleCloudAiplatformV1ListStudiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    studies: _list[GoogleCloudAiplatformV1Study]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardExperimentsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    tensorboardExperiments: _list[GoogleCloudAiplatformV1TensorboardExperiment]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardRunsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tensorboardRuns: _list[GoogleCloudAiplatformV1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tensorboards: _list[GoogleCloudAiplatformV1Tensorboard]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrainingPipelinesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    trainingPipelines: _list[GoogleCloudAiplatformV1TrainingPipeline]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrialsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    trials: _list[GoogleCloudAiplatformV1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1ListTuningJobsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tuningJobs: _list[GoogleCloudAiplatformV1TuningJob]

@typing.type_check_only
class GoogleCloudAiplatformV1LogprobsResult(typing.TypedDict, total=False):
    chosenCandidates: _list[GoogleCloudAiplatformV1LogprobsResultCandidate]
    topCandidates: _list[GoogleCloudAiplatformV1LogprobsResultTopCandidates]

@typing.type_check_only
class GoogleCloudAiplatformV1LogprobsResultCandidate(typing.TypedDict, total=False):
    logProbability: float
    token: str
    tokenId: int

@typing.type_check_only
class GoogleCloudAiplatformV1LogprobsResultTopCandidates(typing.TypedDict, total=False):
    candidates: _list[GoogleCloudAiplatformV1LogprobsResultCandidate]

@typing.type_check_only
class GoogleCloudAiplatformV1LookupStudyRequest(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1LossAnalysisConfig(typing.TypedDict, total=False):
    candidate: str
    metric: str

@typing.type_check_only
class GoogleCloudAiplatformV1LustreMount(typing.TypedDict, total=False):
    filesystem: str
    instanceIp: str
    mountPoint: str
    volumeHandle: str

@typing.type_check_only
class GoogleCloudAiplatformV1MachineSpec(typing.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: typing.Literal[
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
        "NVIDIA_H200_141GB",
        "NVIDIA_B200",
        "NVIDIA_GB200",
        "NVIDIA_RTX_PRO_6000",
        "TPU_V2",
        "TPU_V3",
        "TPU_V4_POD",
        "TPU_V5_LITEPOD",
    ]
    gpuPartitionSize: str
    machineType: str
    reservationAffinity: GoogleCloudAiplatformV1ReservationAffinity
    tpuTopology: str

@typing.type_check_only
class GoogleCloudAiplatformV1ManualBatchTuningParameters(typing.TypedDict, total=False):
    batchSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1Measurement(typing.TypedDict, total=False):
    elapsedDuration: str
    metrics: _list[GoogleCloudAiplatformV1MeasurementMetric]
    stepCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1MeasurementMetric(typing.TypedDict, total=False):
    metricId: str
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1Memory(typing.TypedDict, total=False):
    createTime: str
    description: str
    disableMemoryRevisions: bool
    displayName: str
    expireTime: str
    fact: str
    metadata: dict[str, typing.Any]
    name: str
    revisionExpireTime: str
    revisionLabels: dict[str, typing.Any]
    revisionTtl: str
    scope: dict[str, typing.Any]
    topics: _list[GoogleCloudAiplatformV1MemoryTopicId]
    ttl: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfig(
    typing.TypedDict, total=False
):
    consolidationConfig: (
        GoogleCloudAiplatformV1MemoryBankCustomizationConfigConsolidationConfig
    )
    disableNaturalLanguageMemories: bool
    enableThirdPersonMemories: bool
    generateMemoriesExamples: _list[
        GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExample
    ]
    memoryTopics: _list[GoogleCloudAiplatformV1MemoryBankCustomizationConfigMemoryTopic]
    scopeKeys: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigConsolidationConfig(
    typing.TypedDict, total=False
):
    revisionsPerCandidateCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExample(
    typing.TypedDict, total=False
):
    conversationSource: GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource
    generatedMemories: _list[
        GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource(
    typing.TypedDict, total=False
):
    events: _list[
        GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1Content

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory(
    typing.TypedDict, total=False
):
    fact: str
    topics: _list[GoogleCloudAiplatformV1MemoryTopicId]

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigMemoryTopic(
    typing.TypedDict, total=False
):
    customMemoryTopic: (
        GoogleCloudAiplatformV1MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic
    )
    managedMemoryTopic: GoogleCloudAiplatformV1MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic(
    typing.TypedDict, total=False
):
    description: str
    label: str

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic(
    typing.TypedDict, total=False
):
    managedTopicEnum: typing.Literal[
        "MANAGED_TOPIC_ENUM_UNSPECIFIED",
        "USER_PERSONAL_INFO",
        "USER_PREFERENCES",
        "KEY_CONVERSATION_DETAILS",
        "EXPLICIT_INSTRUCTIONS",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryConjunctionFilter(typing.TypedDict, total=False):
    filters: _list[GoogleCloudAiplatformV1MemoryFilter]

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryFilter(typing.TypedDict, total=False):
    key: str
    negate: bool
    op: typing.Literal["OPERATOR_UNSPECIFIED", "EQUAL", "GREATER_THAN", "LESS_THAN"]
    value: GoogleCloudAiplatformV1MemoryMetadataValue

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryGenerationTriggerConfig(
    typing.TypedDict, total=False
):
    generationRule: (
        GoogleCloudAiplatformV1MemoryGenerationTriggerConfigGenerationTriggerRule
    )

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryGenerationTriggerConfigGenerationTriggerRule(
    typing.TypedDict, total=False
):
    eventCount: int
    fixedInterval: str
    idleDuration: str
    overlapEventCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryMetadataValue(typing.TypedDict, total=False):
    boolValue: bool
    doubleValue: float
    stringValue: str
    timestampValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryRevision(typing.TypedDict, total=False):
    createTime: str
    expireTime: str
    extractedMemories: _list[GoogleCloudAiplatformV1IntermediateExtractedMemory]
    fact: str
    labels: dict[str, typing.Any]
    name: str
    structuredData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1MemoryTopicId(typing.TypedDict, total=False):
    customMemoryTopicLabel: str
    managedMemoryTopic: typing.Literal[
        "MANAGED_TOPIC_ENUM_UNSPECIFIED",
        "USER_PERSONAL_INFO",
        "USER_PREFERENCES",
        "KEY_CONVERSATION_DETAILS",
        "EXPLICIT_INSTRUCTIONS",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MergeVersionAliasesRequest(typing.TypedDict, total=False):
    versionAliases: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1Metadata(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataSchema(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    schema: str
    schemaType: typing.Literal[
        "METADATA_SCHEMA_TYPE_UNSPECIFIED",
        "ARTIFACT_TYPE",
        "EXECUTION_TYPE",
        "CONTEXT_TYPE",
    ]
    schemaVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStore(typing.TypedDict, total=False):
    createTime: str
    dataplexConfig: GoogleCloudAiplatformV1MetadataStoreDataplexConfig
    description: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    name: str
    state: GoogleCloudAiplatformV1MetadataStoreMetadataStoreState
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStoreDataplexConfig(typing.TypedDict, total=False):
    enabledPipelinesLineage: bool

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStoreMetadataStoreState(
    typing.TypedDict, total=False
):
    diskUtilizationBytes: str

@typing.type_check_only
class GoogleCloudAiplatformV1Metric(typing.TypedDict, total=False):
    aggregationMetrics: _list[
        typing.Literal[
            "AGGREGATION_METRIC_UNSPECIFIED",
            "AVERAGE",
            "MODE",
            "STANDARD_DEVIATION",
            "VARIANCE",
            "MINIMUM",
            "MAXIMUM",
            "MEDIAN",
            "PERCENTILE_P90",
            "PERCENTILE_P95",
            "PERCENTILE_P99",
        ]
    ]
    bleuSpec: GoogleCloudAiplatformV1BleuSpec
    computationBasedMetricSpec: GoogleCloudAiplatformV1ComputationBasedMetricSpec
    customCodeExecutionSpec: GoogleCloudAiplatformV1CustomCodeExecutionSpec
    exactMatchSpec: GoogleCloudAiplatformV1ExactMatchSpec
    llmBasedMetricSpec: GoogleCloudAiplatformV1LLMBasedMetricSpec
    metadata: GoogleCloudAiplatformV1MetricMetadata
    pairwiseMetricSpec: GoogleCloudAiplatformV1PairwiseMetricSpec
    pointwiseMetricSpec: GoogleCloudAiplatformV1PointwiseMetricSpec
    predefinedMetricSpec: GoogleCloudAiplatformV1PredefinedMetricSpec
    rougeSpec: GoogleCloudAiplatformV1RougeSpec

@typing.type_check_only
class GoogleCloudAiplatformV1MetricMetadata(typing.TypedDict, total=False):
    otherMetadata: dict[str, typing.Any]
    scoreRange: GoogleCloudAiplatformV1MetricMetadataScoreRange
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetricMetadataScoreRange(typing.TypedDict, total=False):
    description: str
    max: float
    min: float
    step: float

@typing.type_check_only
class GoogleCloudAiplatformV1MetricResult(typing.TypedDict, total=False):
    error: GoogleRpcStatus
    explanation: str
    rubricVerdicts: _list[GoogleCloudAiplatformV1RubricVerdict]
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1MetricSource(typing.TypedDict, total=False):
    metric: GoogleCloudAiplatformV1Metric
    metricResourceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1MetricxInstance
    metricSpec: GoogleCloudAiplatformV1MetricxSpec

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str
    source: str

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxResult(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1MetricxSpec(typing.TypedDict, total=False):
    sourceLanguage: str
    targetLanguage: str
    version: typing.Literal[
        "METRICX_VERSION_UNSPECIFIED",
        "METRICX_24_REF",
        "METRICX_24_SRC",
        "METRICX_24_SRC_REF",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResource(typing.TypedDict, total=False):
    automlDataset: GoogleCloudAiplatformV1MigratableResourceAutomlDataset
    automlModel: GoogleCloudAiplatformV1MigratableResourceAutomlModel
    dataLabelingDataset: GoogleCloudAiplatformV1MigratableResourceDataLabelingDataset
    lastMigrateTime: str
    lastUpdateTime: str
    mlEngineModelVersion: GoogleCloudAiplatformV1MigratableResourceMlEngineModelVersion

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceAutomlDataset(
    typing.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceAutomlModel(
    typing.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceDataLabelingDataset(
    typing.TypedDict, total=False
):
    dataLabelingAnnotatedDatasets: _list[
        GoogleCloudAiplatformV1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset
    ]
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset(
    typing.TypedDict, total=False
):
    annotatedDataset: str
    annotatedDatasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigratableResourceMlEngineModelVersion(
    typing.TypedDict, total=False
):
    endpoint: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequest(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateAutomlModelConfig(
    typing.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfig(
    typing.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str
    migrateDataLabelingAnnotatedDatasetConfigs: _list[
        GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig(
    typing.TypedDict, total=False
):
    annotatedDataset: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceRequestMigrateMlEngineModelVersionConfig(
    typing.TypedDict, total=False
):
    endpoint: str
    modelDisplayName: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1MigrateResourceResponse(typing.TypedDict, total=False):
    dataset: str
    migratableResource: GoogleCloudAiplatformV1MigratableResource
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModalityTokenCount(typing.TypedDict, total=False):
    modality: typing.Literal[
        "MODALITY_UNSPECIFIED", "TEXT", "IMAGE", "VIDEO", "AUDIO", "DOCUMENT"
    ]
    tokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1Model(typing.TypedDict, total=False):
    artifactUri: str
    baseModelSource: GoogleCloudAiplatformV1ModelBaseModelSource
    checkpoints: _list[GoogleCloudAiplatformV1Checkpoint]
    containerSpec: GoogleCloudAiplatformV1ModelContainerSpec
    createTime: str
    dataStats: GoogleCloudAiplatformV1ModelDataStats
    defaultCheckpointId: str
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
        typing.Literal[
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
class GoogleCloudAiplatformV1ModelArmorConfig(typing.TypedDict, total=False):
    promptTemplateName: str
    responseTemplateName: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelBaseModelSource(typing.TypedDict, total=False):
    genieSource: GoogleCloudAiplatformV1GenieSource
    modelGardenSource: GoogleCloudAiplatformV1ModelGardenSource

@typing.type_check_only
class GoogleCloudAiplatformV1ModelContainerSpec(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    deploymentTimeout: str
    env: _list[GoogleCloudAiplatformV1EnvVar]
    grpcPorts: _list[GoogleCloudAiplatformV1Port]
    healthProbe: GoogleCloudAiplatformV1Probe
    healthRoute: str
    imageUri: str
    invokeRoutePrefix: str
    livenessProbe: GoogleCloudAiplatformV1Probe
    ports: _list[GoogleCloudAiplatformV1Port]
    predictRoute: str
    sharedMemorySizeMb: str
    startupProbe: GoogleCloudAiplatformV1Probe

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDataStats(typing.TypedDict, total=False):
    testAnnotationsCount: str
    testDataItemsCount: str
    trainingAnnotationsCount: str
    trainingDataItemsCount: str
    validationAnnotationsCount: str
    validationDataItemsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringBigQueryTable(
    typing.TypedDict, total=False
):
    bigqueryTablePath: str
    logSource: typing.Literal["LOG_SOURCE_UNSPECIFIED", "TRAINING", "SERVING"]
    logType: typing.Literal["LOG_TYPE_UNSPECIFIED", "PREDICT", "EXPLAIN"]
    requestResponseLoggingSchemaVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringJob(
    typing.TypedDict, total=False
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
    scheduleState: typing.Literal[
        "MONITORING_SCHEDULE_STATE_UNSPECIFIED", "PENDING", "OFFLINE", "RUNNING"
    ]
    state: typing.Literal[
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
    typing.TypedDict, total=False
):
    runTime: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringObjectiveConfig(
    typing.TypedDict, total=False
):
    deployedModelId: str
    objectiveConfig: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringScheduleConfig(
    typing.TypedDict, total=False
):
    monitorInterval: str
    monitorWindow: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluation(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    explanationSpec: GoogleCloudAiplatformV1ExplanationSpec
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSlice(typing.TypedDict, total=False):
    createTime: str
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1ModelExplanation
    name: str
    slice: GoogleCloudAiplatformV1ModelEvaluationSliceSlice

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSlice(typing.TypedDict, total=False):
    dimension: str
    sliceSpec: GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpec
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpec(
    typing.TypedDict, total=False
):
    configs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecRange(
    typing.TypedDict, total=False
):
    high: float
    low: float

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecSliceConfig(
    typing.TypedDict, total=False
):
    allValues: bool
    range: GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecRange
    value: GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecValue

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceSliceSliceSpecValue(
    typing.TypedDict, total=False
):
    floatValue: float
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelExplanation(typing.TypedDict, total=False):
    meanAttributions: _list[GoogleCloudAiplatformV1Attribution]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelExportFormat(typing.TypedDict, total=False):
    exportableContents: _list[
        typing.Literal["EXPORTABLE_CONTENT_UNSPECIFIED", "ARTIFACT", "IMAGE"]
    ]
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelGardenSource(typing.TypedDict, total=False):
    publicModelName: str
    skipHfModelCache: bool
    versionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringAlertConfig(typing.TypedDict, total=False):
    emailAlertConfig: GoogleCloudAiplatformV1ModelMonitoringAlertConfigEmailAlertConfig
    enableLogging: bool
    notificationChannels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringAlertConfigEmailAlertConfig(
    typing.TypedDict, total=False
):
    userEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfig(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    enableFeatureAttributes: bool
    explanationBaseline: GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline(
    typing.TypedDict, total=False
):
    bigquery: GoogleCloudAiplatformV1BigQueryDestination
    gcs: GoogleCloudAiplatformV1GcsDestination
    predictionFormat: typing.Literal[
        "PREDICTION_FORMAT_UNSPECIFIED", "JSONL", "BIGQUERY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig(
    typing.TypedDict, total=False
):
    attributionScoreDriftThresholds: dict[str, typing.Any]
    defaultDriftThreshold: GoogleCloudAiplatformV1ThresholdConfig
    driftThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingDataset(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1BigQuerySource
    dataFormat: str
    dataset: str
    gcsSource: GoogleCloudAiplatformV1GcsSource
    loggingSamplingStrategy: GoogleCloudAiplatformV1SamplingStrategy
    targetField: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig(
    typing.TypedDict, total=False
):
    attributionScoreSkewThresholds: dict[str, typing.Any]
    defaultSkewThreshold: GoogleCloudAiplatformV1ThresholdConfig
    skewThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringStatsAnomalies(
    typing.TypedDict, total=False
):
    anomalyCount: int
    deployedModelId: str
    featureStats: _list[
        GoogleCloudAiplatformV1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies
    ]
    objective: typing.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies(
    typing.TypedDict, total=False
):
    featureDisplayName: str
    predictionStats: _list[GoogleCloudAiplatformV1FeatureStatsAnomaly]
    threshold: GoogleCloudAiplatformV1ThresholdConfig
    trainingStats: GoogleCloudAiplatformV1FeatureStatsAnomaly

@typing.type_check_only
class GoogleCloudAiplatformV1ModelOriginalModelInfo(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1ModelSourceInfo(typing.TypedDict, total=False):
    copy: bool
    sourceType: typing.Literal[
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
class GoogleCloudAiplatformV1ModelVersionCheckpoint(typing.TypedDict, total=False):
    checkpointId: str
    epoch: str
    step: str

@typing.type_check_only
class GoogleCloudAiplatformV1MultiSpeakerVoiceConfig(typing.TypedDict, total=False):
    speakerVoiceConfigs: _list[GoogleCloudAiplatformV1SpeakerVoiceConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedIndexOperationMetadata(
    typing.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedIndexResponse(typing.TypedDict, total=False):
    deployedIndex: GoogleCloudAiplatformV1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedModelRequest(typing.TypedDict, total=False):
    deployedModel: GoogleCloudAiplatformV1DeployedModel
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1MutateDeployedModelResponse(typing.TypedDict, total=False):
    deployedModel: GoogleCloudAiplatformV1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1NasJob(typing.TypedDict, total=False):
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
    state: typing.Literal[
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
class GoogleCloudAiplatformV1NasJobOutput(typing.TypedDict, total=False):
    multiTrialJobOutput: GoogleCloudAiplatformV1NasJobOutputMultiTrialJobOutput

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobOutputMultiTrialJobOutput(
    typing.TypedDict, total=False
):
    searchTrials: _list[GoogleCloudAiplatformV1NasTrial]
    trainTrials: _list[GoogleCloudAiplatformV1NasTrial]

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpec(typing.TypedDict, total=False):
    multiTrialAlgorithmSpec: GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpec
    resumeNasJobId: str
    searchSpaceSpec: str

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpec(
    typing.TypedDict, total=False
):
    metric: GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecMetricSpec
    multiTrialAlgorithm: typing.Literal[
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
    typing.TypedDict, total=False
):
    goal: typing.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec(
    typing.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxParallelTrialCount: int
    maxTrialCount: int
    searchTrialJobSpec: GoogleCloudAiplatformV1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec(
    typing.TypedDict, total=False
):
    frequency: int
    maxParallelTrialCount: int
    trainTrialJobSpec: GoogleCloudAiplatformV1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1NasTrial(typing.TypedDict, total=False):
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1Measurement
    id: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "REQUESTED",
        "ACTIVE",
        "STOPPING",
        "SUCCEEDED",
        "INFEASIBLE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1NasTrialDetail(typing.TypedDict, total=False):
    name: str
    parameters: str
    searchTrial: GoogleCloudAiplatformV1NasTrial
    trainTrial: GoogleCloudAiplatformV1NasTrial

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQuery(typing.TypedDict, total=False):
    embedding: GoogleCloudAiplatformV1NearestNeighborQueryEmbedding
    entityId: str
    neighborCount: int
    numericFilters: _list[GoogleCloudAiplatformV1NearestNeighborQueryNumericFilter]
    parameters: GoogleCloudAiplatformV1NearestNeighborQueryParameters
    perCrowdingAttributeNeighborCount: int
    stringFilters: _list[GoogleCloudAiplatformV1NearestNeighborQueryStringFilter]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryEmbedding(
    typing.TypedDict, total=False
):
    value: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryNumericFilter(
    typing.TypedDict, total=False
):
    name: str
    op: typing.Literal[
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
    typing.TypedDict, total=False
):
    approximateNeighborCandidates: int
    leafNodesSearchFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborQueryStringFilter(
    typing.TypedDict, total=False
):
    allowTokens: _list[str]
    denyTokens: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata(
    typing.TypedDict, total=False
):
    contentValidationStats: _list[
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataContentValidationStats
    ]
    dataBytesCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataContentValidationStats(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    embeddingId: str
    errorMessage: str
    errorType: typing.Literal[
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
        "INVALID_EMBEDDING_METADATA",
        "EMBEDDING_METADATA_EXCEEDS_SIZE_LIMIT",
        "DUPLICATE_ID",
    ]
    rawRecord: str
    sourceGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighbors(typing.TypedDict, total=False):
    neighbors: _list[GoogleCloudAiplatformV1NearestNeighborsNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1NearestNeighborsNeighbor(typing.TypedDict, total=False):
    distance: float
    entityId: str
    entityKeyValues: GoogleCloudAiplatformV1FetchFeatureValuesResponse

@typing.type_check_only
class GoogleCloudAiplatformV1Neighbor(typing.TypedDict, total=False):
    neighborDistance: float
    neighborId: str

@typing.type_check_only
class GoogleCloudAiplatformV1NetworkSpec(typing.TypedDict, total=False):
    enableInternetAccess: bool
    network: str
    subnetwork: str

@typing.type_check_only
class GoogleCloudAiplatformV1NfsMount(typing.TypedDict, total=False):
    mountPoint: str
    path: str
    server: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookEucConfig(typing.TypedDict, total=False):
    bypassActasCheck: bool
    eucDisabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJob(typing.TypedDict, total=False):
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
    jobState: typing.Literal[
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
    typing.TypedDict, total=False
):
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    networkSpec: GoogleCloudAiplatformV1NetworkSpec
    persistentDiskSpec: GoogleCloudAiplatformV1PersistentDiskSpec
    shieldedInstanceConfig: GoogleCloudAiplatformV1NotebookExecutionJobCustomEnvironmentSpecShieldedInstanceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobCustomEnvironmentSpecShieldedInstanceConfig(
    typing.TypedDict, total=False
):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobDataformRepositorySource(
    typing.TypedDict, total=False
):
    commitSha: str
    dataformRepositoryResourceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobDirectNotebookSource(
    typing.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobGcsNotebookSource(
    typing.TypedDict, total=False
):
    generation: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobWorkbenchRuntime(
    typing.TypedDict, total=False
):
    customContainerImage: (
        GoogleCloudAiplatformV1NotebookExecutionJobWorkbenchRuntimeContainerImage
    )
    vmImage: GoogleCloudAiplatformV1NotebookExecutionJobWorkbenchRuntimeVmImage

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobWorkbenchRuntimeContainerImage(
    typing.TypedDict, total=False
):
    repository: str
    tag: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobWorkbenchRuntimeVmImage(
    typing.TypedDict, total=False
):
    family: str
    name: str
    project: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookIdleShutdownConfig(typing.TypedDict, total=False):
    idleShutdownDisabled: bool
    idleTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "RESERVATION_AFFINITY_TYPE_UNSPECIFIED",
        "RESERVATION_NONE",
        "RESERVATION_ANY",
        "RESERVATION_SPECIFIC",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntime(typing.TypedDict, total=False):
    createTime: str
    dataPersistentDiskSpec: GoogleCloudAiplatformV1PersistentDiskSpec
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    eucConfig: GoogleCloudAiplatformV1NotebookEucConfig
    expirationTime: str
    healthState: typing.Literal["HEALTH_STATE_UNSPECIFIED", "HEALTHY", "UNHEALTHY"]
    idleShutdownConfig: GoogleCloudAiplatformV1NotebookIdleShutdownConfig
    isUpgradable: bool
    labels: dict[str, typing.Any]
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    name: str
    networkSpec: GoogleCloudAiplatformV1NetworkSpec
    networkTags: _list[str]
    notebookRuntimeTemplateRef: GoogleCloudAiplatformV1NotebookRuntimeTemplateRef
    notebookRuntimeType: typing.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    proxyUri: str
    reservationAffinity: GoogleCloudAiplatformV1NotebookReservationAffinity
    runtimeState: typing.Literal[
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
    softwareConfig: GoogleCloudAiplatformV1NotebookSoftwareConfig
    updateTime: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeTemplate(typing.TypedDict, total=False):
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
    notebookRuntimeType: typing.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    reservationAffinity: GoogleCloudAiplatformV1NotebookReservationAffinity
    serviceAccount: str
    shieldedVmConfig: GoogleCloudAiplatformV1ShieldedVmConfig
    softwareConfig: GoogleCloudAiplatformV1NotebookSoftwareConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeTemplateRef(typing.TypedDict, total=False):
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookSoftwareConfig(typing.TypedDict, total=False):
    colabImage: GoogleCloudAiplatformV1ColabImage
    env: _list[GoogleCloudAiplatformV1EnvVar]
    postStartupScriptConfig: GoogleCloudAiplatformV1PostStartupScriptConfig

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluator(typing.TypedDict, total=False):
    agentResource: str
    cloudObservability: GoogleCloudAiplatformV1OnlineEvaluatorCloudObservability
    config: GoogleCloudAiplatformV1OnlineEvaluatorConfig
    createTime: str
    displayName: str
    metricSources: _list[GoogleCloudAiplatformV1MetricSource]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED", "FAILED", "WARNING"
    ]
    stateDetails: _list[GoogleCloudAiplatformV1OnlineEvaluatorStateDetails]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorCloudObservability(
    typing.TypedDict, total=False
):
    logView: str
    openTelemetry: GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityOpenTelemetry
    traceScope: GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityTraceScope
    traceView: str

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityNumericPredicate(
    typing.TypedDict, total=False
):
    comparisonOperator: typing.Literal[
        "COMPARISON_OPERATOR_UNSPECIFIED",
        "LESS",
        "LESS_OR_EQUAL",
        "EQUAL",
        "NOT_EQUAL",
        "GREATER_OR_EQUAL",
        "GREATER",
    ]
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityOpenTelemetry(
    typing.TypedDict, total=False
):
    semconvVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityTraceScope(
    typing.TypedDict, total=False
):
    filter: _list[
        GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityTraceScopePredicate
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityTraceScopePredicate(
    typing.TypedDict, total=False
):
    duration: GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityNumericPredicate
    totalTokenUsage: (
        GoogleCloudAiplatformV1OnlineEvaluatorCloudObservabilityNumericPredicate
    )

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorConfig(typing.TypedDict, total=False):
    maxEvaluatedSamplesPerRun: str
    randomSampling: GoogleCloudAiplatformV1OnlineEvaluatorConfigRandomSampling

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorConfigRandomSampling(
    typing.TypedDict, total=False
):
    percentage: int

@typing.type_check_only
class GoogleCloudAiplatformV1OnlineEvaluatorStateDetails(typing.TypedDict, total=False):
    message: str

@typing.type_check_only
class GoogleCloudAiplatformV1OutputConfig(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1OutputFieldSpec(typing.TypedDict, total=False):
    fieldName: str
    fieldType: typing.Literal[
        "FIELD_TYPE_UNSPECIFIED", "CONTENT", "TEXT", "IMAGE", "AUDIO"
    ]
    guidance: str

@typing.type_check_only
class GoogleCloudAiplatformV1OutputInfo(typing.TypedDict, total=False):
    gcsOutputDirectory: str

@typing.type_check_only
class GoogleCloudAiplatformV1PSCAutomationConfig(typing.TypedDict, total=False):
    errorMessage: str
    forwardingRule: str
    ipAddress: str
    network: str
    projectId: str
    state: typing.Literal[
        "PSC_AUTOMATION_STATE_UNSPECIFIED",
        "PSC_AUTOMATION_STATE_SUCCESSFUL",
        "PSC_AUTOMATION_STATE_FAILED",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1PairwiseMetricInstance
    metricSpec: GoogleCloudAiplatformV1PairwiseMetricSpec

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricInstance(typing.TypedDict, total=False):
    contentMapInstance: GoogleCloudAiplatformV1ContentMap
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricResult(typing.TypedDict, total=False):
    customOutput: GoogleCloudAiplatformV1CustomOutput
    explanation: str
    pairwiseChoice: typing.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseMetricSpec(typing.TypedDict, total=False):
    baselineResponseFieldName: str
    candidateResponseFieldName: str
    customOutputFormatConfig: GoogleCloudAiplatformV1CustomOutputFormatConfig
    metricPromptTemplate: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityInstance
    metricSpec: GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityInstance(
    typing.TypedDict, total=False
):
    baselinePrediction: str
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    pairwiseChoice: typing.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseQuestionAnsweringQualitySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1PairwiseSummarizationQualityInstance
    metricSpec: GoogleCloudAiplatformV1PairwiseSummarizationQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualityInstance(
    typing.TypedDict, total=False
):
    baselinePrediction: str
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    pairwiseChoice: typing.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PairwiseSummarizationQualitySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1Part(typing.TypedDict, total=False):
    audioTranscription: GoogleCloudAiplatformV1AudioTranscription
    codeExecutionResult: GoogleCloudAiplatformV1CodeExecutionResult
    executableCode: GoogleCloudAiplatformV1ExecutableCode
    fileData: GoogleCloudAiplatformV1FileData
    functionCall: GoogleCloudAiplatformV1FunctionCall
    functionResponse: GoogleCloudAiplatformV1FunctionResponse
    inlineData: GoogleCloudAiplatformV1Blob
    mediaResolution: GoogleCloudAiplatformV1PartMediaResolution
    text: str
    thought: bool
    thoughtSignature: str
    videoMetadata: GoogleCloudAiplatformV1VideoMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PartMediaResolution(typing.TypedDict, total=False):
    level: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED",
        "MEDIA_RESOLUTION_LOW",
        "MEDIA_RESOLUTION_MEDIUM",
        "MEDIA_RESOLUTION_HIGH",
        "MEDIA_RESOLUTION_ULTRA_HIGH",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PartialArg(typing.TypedDict, total=False):
    boolValue: bool
    jsonPath: str
    nullValue: typing.Literal["NULL_VALUE"]
    numberValue: float
    stringValue: str
    willContinue: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PauseModelDeploymentMonitoringJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1PauseSandboxEnvironmentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1PauseScheduleRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1PersistentDiskSpec(typing.TypedDict, total=False):
    diskSizeGb: str
    diskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1PersistentResource(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    network: str
    pscInterfaceConfig: GoogleCloudAiplatformV1PscInterfaceConfig
    reservedIpRanges: _list[str]
    resourcePools: _list[GoogleCloudAiplatformV1ResourcePool]
    resourceRuntime: GoogleCloudAiplatformV1ResourceRuntime
    resourceRuntimeSpec: GoogleCloudAiplatformV1ResourceRuntimeSpec
    satisfiesPzi: bool
    satisfiesPzs: bool
    startTime: str
    state: typing.Literal[
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
class GoogleCloudAiplatformV1PipelineJob(typing.TypedDict, total=False):
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
    pscInterfaceConfig: GoogleCloudAiplatformV1PscInterfaceConfig
    reservedIpRanges: _list[str]
    runtimeConfig: GoogleCloudAiplatformV1PipelineJobRuntimeConfig
    scheduleName: str
    serviceAccount: str
    startTime: str
    state: typing.Literal[
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
class GoogleCloudAiplatformV1PipelineJobDetail(typing.TypedDict, total=False):
    pipelineContext: GoogleCloudAiplatformV1Context
    pipelineRunContext: GoogleCloudAiplatformV1Context
    taskDetails: _list[GoogleCloudAiplatformV1PipelineTaskDetail]

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineJobRuntimeConfig(typing.TypedDict, total=False):
    failurePolicy: typing.Literal[
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
    typing.TypedDict, total=False
):
    artifactId: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskDetail(typing.TypedDict, total=False):
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
    state: typing.Literal[
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
    taskUniqueName: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskDetailArtifactList(
    typing.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1Artifact]

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskDetailPipelineTaskStatus(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing.Literal[
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
class GoogleCloudAiplatformV1PipelineTaskExecutorDetail(typing.TypedDict, total=False):
    containerDetail: GoogleCloudAiplatformV1PipelineTaskExecutorDetailContainerDetail
    customJobDetail: GoogleCloudAiplatformV1PipelineTaskExecutorDetailCustomJobDetail

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskExecutorDetailContainerDetail(
    typing.TypedDict, total=False
):
    failedMainJobs: _list[str]
    failedPreCachingCheckJobs: _list[str]
    mainJob: str
    preCachingCheckJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTaskExecutorDetailCustomJobDetail(
    typing.TypedDict, total=False
):
    failedJobs: _list[str]
    job: str

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineTemplateMetadata(typing.TypedDict, total=False):
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1PointwiseMetricInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1PointwiseMetricInstance
    metricSpec: GoogleCloudAiplatformV1PointwiseMetricSpec

@typing.type_check_only
class GoogleCloudAiplatformV1PointwiseMetricInstance(typing.TypedDict, total=False):
    contentMapInstance: GoogleCloudAiplatformV1ContentMap
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1PointwiseMetricResult(typing.TypedDict, total=False):
    customOutput: GoogleCloudAiplatformV1CustomOutput
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1PointwiseMetricSpec(typing.TypedDict, total=False):
    customOutputFormatConfig: GoogleCloudAiplatformV1CustomOutputFormatConfig
    metricPromptTemplate: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1Port(typing.TypedDict, total=False):
    containerPort: int

@typing.type_check_only
class GoogleCloudAiplatformV1PostStartupScriptConfig(typing.TypedDict, total=False):
    postStartupScript: str
    postStartupScriptBehavior: typing.Literal[
        "POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED",
        "RUN_ONCE",
        "RUN_EVERY_START",
        "DOWNLOAD_AND_RUN_EVERY_START",
    ]
    postStartupScriptUrl: str

@typing.type_check_only
class GoogleCloudAiplatformV1PreTunedModel(typing.TypedDict, total=False):
    baseModel: str
    checkpointId: str
    tunedModelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1PrebuiltVoiceConfig(typing.TypedDict, total=False):
    voiceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1PredefinedMetricSpec(typing.TypedDict, total=False):
    metricSpecName: str
    metricSpecParameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1PredefinedSplit(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1PredictLongRunningRequest(typing.TypedDict, total=False):
    instances: _list[typing.Any]
    labels: dict[str, typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1PredictRequest(typing.TypedDict, total=False):
    instances: _list[typing.Any]
    labels: dict[str, typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1PredictRequestResponseLoggingConfig(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    enabled: bool
    samplingRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1PredictResponse(typing.TypedDict, total=False):
    deployedModelId: str
    metadata: typing.Any
    model: str
    modelDisplayName: str
    modelVersionId: str
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1PredictSchemata(typing.TypedDict, total=False):
    instanceSchemaUri: str
    parametersSchemaUri: str
    predictionSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1PreferenceOptimizationDataStats(
    typing.TypedDict, total=False
):
    droppedExampleIndices: _list[str]
    droppedExampleReasons: _list[str]
    scoreVariancePerExampleDistribution: GoogleCloudAiplatformV1DatasetDistribution
    scoresDistribution: GoogleCloudAiplatformV1DatasetDistribution
    totalBillableTokenCount: str
    tuningDatasetExampleCount: str
    tuningStepCount: str
    userDatasetExamples: _list[GoogleCloudAiplatformV1GeminiPreferenceExample]
    userInputTokenDistribution: GoogleCloudAiplatformV1DatasetDistribution
    userOutputTokenDistribution: GoogleCloudAiplatformV1DatasetDistribution

@typing.type_check_only
class GoogleCloudAiplatformV1PreferenceOptimizationHyperParameters(
    typing.TypedDict, total=False
):
    adapterSize: typing.Literal[
        "ADAPTER_SIZE_UNSPECIFIED",
        "ADAPTER_SIZE_ONE",
        "ADAPTER_SIZE_TWO",
        "ADAPTER_SIZE_FOUR",
        "ADAPTER_SIZE_EIGHT",
        "ADAPTER_SIZE_SIXTEEN",
        "ADAPTER_SIZE_THIRTY_TWO",
    ]
    beta: float
    epochCount: str
    learningRateMultiplier: float

@typing.type_check_only
class GoogleCloudAiplatformV1PreferenceOptimizationSpec(typing.TypedDict, total=False):
    exportLastCheckpointOnly: bool
    hyperParameters: GoogleCloudAiplatformV1PreferenceOptimizationHyperParameters
    trainingDatasetUri: str
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1Presets(typing.TypedDict, total=False):
    modality: typing.Literal["MODALITY_UNSPECIFIED", "IMAGE", "TEXT", "TABULAR"]
    query: typing.Literal["PRECISE", "FAST"]

@typing.type_check_only
class GoogleCloudAiplatformV1PrivateEndpoints(typing.TypedDict, total=False):
    explainHttpUri: str
    healthHttpUri: str
    predictHttpUri: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1PrivateServiceConnectConfig(typing.TypedDict, total=False):
    enablePrivateServiceConnect: bool
    projectAllowlist: _list[str]
    pscAutomationConfigs: _list[GoogleCloudAiplatformV1PSCAutomationConfig]
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1Probe(typing.TypedDict, total=False):
    exec: GoogleCloudAiplatformV1ProbeExecAction
    failureThreshold: int
    grpc: GoogleCloudAiplatformV1ProbeGrpcAction
    httpGet: GoogleCloudAiplatformV1ProbeHttpGetAction
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: GoogleCloudAiplatformV1ProbeTcpSocketAction
    timeoutSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeExecAction(typing.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeGrpcAction(typing.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeHttpGetAction(typing.TypedDict, total=False):
    host: str
    httpHeaders: _list[GoogleCloudAiplatformV1ProbeHttpHeader]
    path: str
    port: int
    scheme: str

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeHttpHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1ProbeTcpSocketAction(typing.TypedDict, total=False):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudAiplatformV1PscAutomatedEndpoints(typing.TypedDict, total=False):
    matchAddress: str
    network: str
    projectId: str

@typing.type_check_only
class GoogleCloudAiplatformV1PscInterfaceConfig(typing.TypedDict, total=False):
    dnsPeeringConfigs: _list[GoogleCloudAiplatformV1DnsPeeringConfig]
    networkAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModel(typing.TypedDict, total=False):
    frameworks: _list[str]
    launchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "EXPERIMENTAL",
        "PRIVATE_PREVIEW",
        "PUBLIC_PREVIEW",
        "GA",
    ]
    name: str
    openSourceCategory: typing.Literal[
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
    versionState: typing.Literal[
        "VERSION_STATE_UNSPECIFIED", "VERSION_STATE_STABLE", "VERSION_STATE_UNSTABLE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToAction(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    labels: dict[str, typing.Any]
    sampleRequest: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeployGke(
    typing.TypedDict, total=False
):
    gkeYamlConfigs: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionDeployVertex(
    typing.TypedDict, total=False
):
    multiDeployVertex: _list[GoogleCloudAiplatformV1PublisherModelCallToActionDeploy]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionOpenFineTuningPipelines(
    typing.TypedDict, total=False
):
    fineTuningPipelines: _list[
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionOpenNotebooks(
    typing.TypedDict, total=False
):
    notebooks: _list[
        GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionRegionalResourceReferences(
    typing.TypedDict, total=False
):
    colabNotebookDisabled: bool
    references: dict[str, typing.Any]
    resourceDescription: str
    resourceTitle: str
    resourceUseCase: str
    supportsWorkbench: bool
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelCallToActionViewRestApi(
    typing.TypedDict, total=False
):
    documentations: _list[GoogleCloudAiplatformV1PublisherModelDocumentation]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelDocumentation(typing.TypedDict, total=False):
    content: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelResourceReference(
    typing.TypedDict, total=False
):
    description: str
    resourceName: str
    uri: str
    useCase: str

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeArtifactsMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeArtifactsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeArtifactsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeContextsMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeContextsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeContextsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeExecutionsMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeExecutionsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeExecutionsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1PurgeMemoriesRequest(typing.TypedDict, total=False):
    filter: str
    filterGroups: _list[GoogleCloudAiplatformV1MemoryConjunctionFilter]
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1PythonPackageSpec(typing.TypedDict, total=False):
    args: _list[str]
    env: _list[GoogleCloudAiplatformV1EnvVar]
    executorImageUri: str
    packageUris: _list[str]
    pythonModule: str

@typing.type_check_only
class GoogleCloudAiplatformV1QueryDeployedModelsResponse(typing.TypedDict, total=False):
    deployedModelRefs: _list[GoogleCloudAiplatformV1DeployedModelRef]
    deployedModels: _list[GoogleCloudAiplatformV1DeployedModel]
    nextPageToken: str
    totalDeployedModelCount: int
    totalEndpointCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1QueryReasoningEngineRequest(typing.TypedDict, total=False):
    classMethod: str
    input: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1QueryReasoningEngineResponse(
    typing.TypedDict, total=False
):
    output: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringCorrectnessInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringCorrectnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringCorrectnessSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringHelpfulnessSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringQualityInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualityInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringQualitySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1QuestionAnsweringRelevanceInstance
    metricSpec: GoogleCloudAiplatformV1QuestionAnsweringRelevanceSpec

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1QuestionAnsweringRelevanceSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagChunk(typing.TypedDict, total=False):
    pageSpan: GoogleCloudAiplatformV1RagChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagChunkPageSpan(typing.TypedDict, total=False):
    firstPage: int
    lastPage: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagContexts(typing.TypedDict, total=False):
    contexts: _list[GoogleCloudAiplatformV1RagContextsContext]

@typing.type_check_only
class GoogleCloudAiplatformV1RagContextsContext(typing.TypedDict, total=False):
    chunk: GoogleCloudAiplatformV1RagChunk
    score: float
    sourceDisplayName: str
    sourceUri: str
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagCorpus(typing.TypedDict, total=False):
    corpusStatus: GoogleCloudAiplatformV1CorpusStatus
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str
    vectorDbConfig: GoogleCloudAiplatformV1RagVectorDbConfig
    vertexAiSearchConfig: GoogleCloudAiplatformV1VertexAiSearchConfig

@typing.type_check_only
class GoogleCloudAiplatformV1RagEmbeddingModelConfig(typing.TypedDict, total=False):
    vertexPredictionEndpoint: (
        GoogleCloudAiplatformV1RagEmbeddingModelConfigVertexPredictionEndpoint
    )

@typing.type_check_only
class GoogleCloudAiplatformV1RagEmbeddingModelConfigVertexPredictionEndpoint(
    typing.TypedDict, total=False
):
    endpoint: str
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagEngineConfig(typing.TypedDict, total=False):
    name: str
    ragManagedDbConfig: GoogleCloudAiplatformV1RagManagedDbConfig

@typing.type_check_only
class GoogleCloudAiplatformV1RagFile(typing.TypedDict, total=False):
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
    userMetadata: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileChunkingConfig(typing.TypedDict, total=False):
    fixedLengthChunking: GoogleCloudAiplatformV1RagFileChunkingConfigFixedLengthChunking

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileChunkingConfigFixedLengthChunking(
    typing.TypedDict, total=False
):
    chunkOverlap: int
    chunkSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileParsingConfig(typing.TypedDict, total=False):
    layoutParser: GoogleCloudAiplatformV1RagFileParsingConfigLayoutParser
    llmParser: GoogleCloudAiplatformV1RagFileParsingConfigLlmParser

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileParsingConfigLayoutParser(
    typing.TypedDict, total=False
):
    maxParsingRequestsPerMin: int
    processorName: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileParsingConfigLlmParser(
    typing.TypedDict, total=False
):
    customParsingPrompt: str
    maxParsingRequestsPerMin: int
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileTransformationConfig(typing.TypedDict, total=False):
    ragFileChunkingConfig: GoogleCloudAiplatformV1RagFileChunkingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1RagManagedDbConfig(typing.TypedDict, total=False):
    basic: GoogleCloudAiplatformV1RagManagedDbConfigBasic
    scaled: GoogleCloudAiplatformV1RagManagedDbConfigScaled
    serverless: GoogleCloudAiplatformV1RagManagedDbConfigServerless
    spanner: GoogleCloudAiplatformV1RagManagedDbConfigSpanner
    unprovisioned: GoogleCloudAiplatformV1RagManagedDbConfigUnprovisioned

@typing.type_check_only
class GoogleCloudAiplatformV1RagManagedDbConfigBasic(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagManagedDbConfigScaled(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagManagedDbConfigServerless(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagManagedDbConfigSpanner(typing.TypedDict, total=False):
    basic: GoogleCloudAiplatformV1RagManagedDbConfigBasic
    scaled: GoogleCloudAiplatformV1RagManagedDbConfigScaled
    unprovisioned: GoogleCloudAiplatformV1RagManagedDbConfigUnprovisioned

@typing.type_check_only
class GoogleCloudAiplatformV1RagManagedDbConfigUnprovisioned(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagQuery(typing.TypedDict, total=False):
    ragRetrievalConfig: GoogleCloudAiplatformV1RagRetrievalConfig
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagRetrievalConfig(typing.TypedDict, total=False):
    filter: GoogleCloudAiplatformV1RagRetrievalConfigFilter
    ranking: GoogleCloudAiplatformV1RagRetrievalConfigRanking
    topK: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagRetrievalConfigFilter(typing.TypedDict, total=False):
    metadataFilter: str
    vectorDistanceThreshold: float
    vectorSimilarityThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1RagRetrievalConfigRanking(typing.TypedDict, total=False):
    llmRanker: GoogleCloudAiplatformV1RagRetrievalConfigRankingLlmRanker
    rankService: GoogleCloudAiplatformV1RagRetrievalConfigRankingRankService

@typing.type_check_only
class GoogleCloudAiplatformV1RagRetrievalConfigRankingLlmRanker(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagRetrievalConfigRankingRankService(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfig(typing.TypedDict, total=False):
    apiAuth: GoogleCloudAiplatformV1ApiAuth
    pinecone: GoogleCloudAiplatformV1RagVectorDbConfigPinecone
    ragEmbeddingModelConfig: GoogleCloudAiplatformV1RagEmbeddingModelConfig
    ragManagedDb: GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDb
    vertexVectorSearch: GoogleCloudAiplatformV1RagVectorDbConfigVertexVectorSearch

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigPinecone(typing.TypedDict, total=False):
    indexName: str

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDb(
    typing.TypedDict, total=False
):
    ann: GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDbANN
    knn: GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDbKNN

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDbANN(
    typing.TypedDict, total=False
):
    leafCount: int
    treeDepth: int

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigRagManagedDbKNN(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagVectorDbConfigVertexVectorSearch(
    typing.TypedDict, total=False
):
    index: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1RawOutput(typing.TypedDict, total=False):
    rawOutput: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RawPredictRequest(typing.TypedDict, total=False):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1RayLogsSpec(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1RayMetricSpec(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1RaySpec(typing.TypedDict, total=False):
    headNodeResourcePoolId: str
    imageUri: str
    rayLogsSpec: GoogleCloudAiplatformV1RayLogsSpec
    rayMetricSpec: GoogleCloudAiplatformV1RayMetricSpec
    resourcePoolImages: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesRequest(typing.TypedDict, total=False):
    entityId: str
    featureSelector: GoogleCloudAiplatformV1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponse(typing.TypedDict, total=False):
    entityView: GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityView
    header: GoogleCloudAiplatformV1ReadFeatureValuesResponseHeader

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityView(
    typing.TypedDict, total=False
):
    data: _list[GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityViewData]
    entityId: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseEntityViewData(
    typing.TypedDict, total=False
):
    value: GoogleCloudAiplatformV1FeatureValue
    values: GoogleCloudAiplatformV1FeatureValueList

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseFeatureDescriptor(
    typing.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseHeader(
    typing.TypedDict, total=False
):
    entityType: str
    featureDescriptors: _list[
        GoogleCloudAiplatformV1ReadFeatureValuesResponseFeatureDescriptor
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadIndexDatapointsRequest(typing.TypedDict, total=False):
    deployedIndexId: str
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadIndexDatapointsResponse(typing.TypedDict, total=False):
    datapoints: _list[GoogleCloudAiplatformV1IndexDatapoint]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse(
    typing.TypedDict, total=False
):
    blobs: _list[GoogleCloudAiplatformV1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardSizeResponse(typing.TypedDict, total=False):
    storageSizeByte: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse(
    typing.TypedDict, total=False
):
    timeSeriesData: GoogleCloudAiplatformV1TimeSeriesData

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponse(
    typing.TypedDict, total=False
):
    monthlyUsageData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponsePerMonthUsageData(
    typing.TypedDict, total=False
):
    userUsageData: _list[
        GoogleCloudAiplatformV1ReadTensorboardUsageResponsePerUserUsageData
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponsePerUserUsageData(
    typing.TypedDict, total=False
):
    username: str
    viewCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngine(typing.TypedDict, total=False):
    contextSpec: GoogleCloudAiplatformV1ReasoningEngineContextSpec
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    spec: GoogleCloudAiplatformV1ReasoningEngineSpec
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineContextSpec(typing.TypedDict, total=False):
    memoryBankConfig: GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfig(
    typing.TypedDict, total=False
):
    customizationConfigs: _list[GoogleCloudAiplatformV1MemoryBankCustomizationConfig]
    disableMemoryRevisions: bool
    generationConfig: GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigGenerationConfig
    similaritySearchConfig: GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig
    ttlConfig: (
        GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigTtlConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigGenerationConfig(
    typing.TypedDict, total=False
):
    generationTriggerConfig: GoogleCloudAiplatformV1MemoryGenerationTriggerConfig
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig(
    typing.TypedDict, total=False
):
    embeddingModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigTtlConfig(
    typing.TypedDict, total=False
):
    defaultTtl: str
    granularTtlConfig: GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig
    memoryRevisionDefaultTtl: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig(
    typing.TypedDict, total=False
):
    createTtl: str
    generateCreatedTtl: str
    generateUpdatedTtl: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpec(typing.TypedDict, total=False):
    agentFramework: str
    buildSpec: GoogleCloudAiplatformV1ReasoningEngineSpecBuildSpec
    classMethods: _list[dict[str, typing.Any]]
    containerSpec: GoogleCloudAiplatformV1ReasoningEngineSpecContainerSpec
    deploymentSpec: GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpec
    effectiveIdentity: str
    identityType: typing.Literal[
        "IDENTITY_TYPE_UNSPECIFIED", "SERVICE_ACCOUNT", "AGENT_IDENTITY"
    ]
    packageSpec: GoogleCloudAiplatformV1ReasoningEngineSpecPackageSpec
    serviceAccount: str
    sourceCodeSpec: GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecBuildSpec(
    typing.TypedDict, total=False
):
    serviceAccount: str
    workerPool: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecContainerSpec(
    typing.TypedDict, total=False
):
    imageUri: str
    port: int

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpec(
    typing.TypedDict, total=False
):
    agentGatewayConfig: (
        GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpecAgentGatewayConfig
    )
    containerConcurrency: int
    env: _list[GoogleCloudAiplatformV1EnvVar]
    keepAliveProbe: GoogleCloudAiplatformV1KeepAliveProbe
    maxInstances: int
    minInstances: int
    pscInterfaceConfig: GoogleCloudAiplatformV1PscInterfaceConfig
    resourceLimits: dict[str, typing.Any]
    secretEnv: _list[GoogleCloudAiplatformV1SecretEnvVar]

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpecAgentGatewayConfig(
    typing.TypedDict, total=False
):
    agentToAnywhereConfig: GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig
    clientToAgentConfig: GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig(
    typing.TypedDict, total=False
):
    agentGateway: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig(
    typing.TypedDict, total=False
):
    agentGateway: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecPackageSpec(
    typing.TypedDict, total=False
):
    dependencyFilesGcsUri: str
    pickleObjectGcsUri: str
    pythonVersion: str
    requirementsGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpec(
    typing.TypedDict, total=False
):
    agentConfigSource: (
        GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecAgentConfigSource
    )
    developerConnectSource: (
        GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource
    )
    imageSpec: GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecImageSpec
    inlineSource: GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecInlineSource
    pythonSpec: GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecPythonSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecAgentConfigSource(
    typing.TypedDict, total=False
):
    adkConfig: GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig
    inlineSource: GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecInlineSource

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig(
    typing.TypedDict, total=False
):
    jsonConfig: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig(
    typing.TypedDict, total=False
):
    dir: str
    gitRepositoryLink: str
    revision: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource(
    typing.TypedDict, total=False
):
    config: (
        GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecImageSpec(
    typing.TypedDict, total=False
):
    buildArgs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecInlineSource(
    typing.TypedDict, total=False
):
    sourceArchive: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineSpecSourceCodeSpecPythonSpec(
    typing.TypedDict, total=False
):
    entrypointModule: str
    entrypointObject: str
    requirementsFile: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1RebaseTunedModelRequest(typing.TypedDict, total=False):
    artifactDestination: GoogleCloudAiplatformV1GcsDestination
    deployToSameEndpoint: bool
    tunedModelRef: GoogleCloudAiplatformV1TunedModelRef
    tuningJob: GoogleCloudAiplatformV1TuningJob

@typing.type_check_only
class GoogleCloudAiplatformV1RebootPersistentResourceOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1RebootPersistentResourceRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveContextChildrenRequest(
    typing.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveContextChildrenResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveDatapointsRequest(typing.TypedDict, total=False):
    datapointIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveDatapointsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReplicatedVoiceConfig(typing.TypedDict, total=False):
    mimeType: str
    voiceSampleAudio: str

@typing.type_check_only
class GoogleCloudAiplatformV1ReservationAffinity(typing.TypedDict, total=False):
    key: str
    reservationAffinityType: typing.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ResourcePool(typing.TypedDict, total=False):
    autoscalingSpec: GoogleCloudAiplatformV1ResourcePoolAutoscalingSpec
    diskSpec: GoogleCloudAiplatformV1DiskSpec
    id: str
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    replicaCount: str
    usedReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ResourcePoolAutoscalingSpec(typing.TypedDict, total=False):
    maxReplicaCount: str
    minReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1ResourceRuntime(typing.TypedDict, total=False):
    accessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ResourceRuntimeSpec(typing.TypedDict, total=False):
    raySpec: GoogleCloudAiplatformV1RaySpec
    serviceAccountSpec: GoogleCloudAiplatformV1ServiceAccountSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ResourcesConsumed(typing.TypedDict, total=False):
    replicaHours: float

@typing.type_check_only
class GoogleCloudAiplatformV1ResponseFormat(typing.TypedDict, total=False):
    audio: GoogleCloudAiplatformV1AudioResponseFormat
    image: GoogleCloudAiplatformV1ImageResponseFormat
    text: GoogleCloudAiplatformV1TextResponseFormat
    video: GoogleCloudAiplatformV1VideoResponseFormat

@typing.type_check_only
class GoogleCloudAiplatformV1RestoreDatasetVersionOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1ResumeModelDeploymentMonitoringJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ResumeSandboxEnvironmentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ResumeScheduleRequest(typing.TypedDict, total=False):
    catchUp: bool

@typing.type_check_only
class GoogleCloudAiplatformV1Retrieval(typing.TypedDict, total=False):
    disableAttribution: bool
    externalApi: GoogleCloudAiplatformV1ExternalApi
    vertexAiSearch: GoogleCloudAiplatformV1VertexAISearch
    vertexRagStore: GoogleCloudAiplatformV1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1RetrievalConfig(typing.TypedDict, total=False):
    languageCode: str
    latLng: GoogleTypeLatLng

@typing.type_check_only
class GoogleCloudAiplatformV1RetrievalMetadata(typing.TypedDict, total=False):
    googleSearchDynamicRetrievalScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsRequest(typing.TypedDict, total=False):
    query: GoogleCloudAiplatformV1RagQuery
    vertexRagStore: GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStore(
    typing.TypedDict, total=False
):
    ragResources: _list[
        GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStoreRagResource
    ]
    vectorDistanceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsRequestVertexRagStoreRagResource(
    typing.TypedDict, total=False
):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsResponse(typing.TypedDict, total=False):
    contexts: GoogleCloudAiplatformV1RagContexts

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveMemoriesRequest(typing.TypedDict, total=False):
    filter: str
    filterGroups: _list[GoogleCloudAiplatformV1MemoryConjunctionFilter]
    memoryTypes: _list[
        typing.Literal[
            "MEMORY_TYPE_UNSPECIFIED",
            "NATURAL_LANGUAGE_COLLECTION",
            "STRUCTURED_PROFILE",
        ]
    ]
    scope: dict[str, typing.Any]
    similaritySearchParams: (
        GoogleCloudAiplatformV1RetrieveMemoriesRequestSimilaritySearchParams
    )
    simpleRetrievalParams: (
        GoogleCloudAiplatformV1RetrieveMemoriesRequestSimpleRetrievalParams
    )

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveMemoriesRequestSimilaritySearchParams(
    typing.TypedDict, total=False
):
    searchQuery: str
    topK: int

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveMemoriesRequestSimpleRetrievalParams(
    typing.TypedDict, total=False
):
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveMemoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    retrievedMemories: _list[
        GoogleCloudAiplatformV1RetrieveMemoriesResponseRetrievedMemory
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveMemoriesResponseRetrievedMemory(
    typing.TypedDict, total=False
):
    distance: float
    memory: GoogleCloudAiplatformV1Memory

@typing.type_check_only
class GoogleCloudAiplatformV1RollbackMemoryRequest(typing.TypedDict, total=False):
    targetRevisionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1RougeInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1RougeInstance]
    metricSpec: GoogleCloudAiplatformV1RougeSpec

@typing.type_check_only
class GoogleCloudAiplatformV1RougeInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1RougeMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1RougeResults(typing.TypedDict, total=False):
    rougeMetricValues: _list[GoogleCloudAiplatformV1RougeMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1RougeSpec(typing.TypedDict, total=False):
    rougeType: str
    splitSummaries: bool
    useStemmer: bool

@typing.type_check_only
class GoogleCloudAiplatformV1Rubric(typing.TypedDict, total=False):
    content: GoogleCloudAiplatformV1RubricContent
    importance: typing.Literal["IMPORTANCE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW"]
    rubricId: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1RubricBasedInstructionFollowingInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1RubricBasedInstructionFollowingInstance
    metricSpec: GoogleCloudAiplatformV1RubricBasedInstructionFollowingSpec

@typing.type_check_only
class GoogleCloudAiplatformV1RubricBasedInstructionFollowingInstance(
    typing.TypedDict, total=False
):
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1RubricBasedInstructionFollowingResult(
    typing.TypedDict, total=False
):
    rubricCritiqueResults: _list[GoogleCloudAiplatformV1RubricCritiqueResult]
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1RubricBasedInstructionFollowingSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1RubricContent(typing.TypedDict, total=False):
    property: GoogleCloudAiplatformV1RubricContentProperty

@typing.type_check_only
class GoogleCloudAiplatformV1RubricContentProperty(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class GoogleCloudAiplatformV1RubricCritiqueResult(typing.TypedDict, total=False):
    rubric: str
    verdict: bool

@typing.type_check_only
class GoogleCloudAiplatformV1RubricGenerationSpec(typing.TypedDict, total=False):
    modelConfig: GoogleCloudAiplatformV1AutoraterConfig
    promptTemplate: str
    rubricContentType: typing.Literal[
        "RUBRIC_CONTENT_TYPE_UNSPECIFIED",
        "PROPERTY",
        "NL_QUESTION_ANSWER",
        "PYTHON_CODE_ASSERTION",
    ]
    rubricTypeOntology: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1RubricGroup(typing.TypedDict, total=False):
    displayName: str
    groupId: str
    rubrics: _list[GoogleCloudAiplatformV1Rubric]

@typing.type_check_only
class GoogleCloudAiplatformV1RubricVerdict(typing.TypedDict, total=False):
    evaluatedRubric: GoogleCloudAiplatformV1Rubric
    reasoning: str
    verdict: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1SafetyInstance
    metricSpec: GoogleCloudAiplatformV1SafetySpec

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyInstance(typing.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyRating(typing.TypedDict, total=False):
    blocked: bool
    category: typing.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
        "HARM_CATEGORY_IMAGE_HATE",
        "HARM_CATEGORY_IMAGE_DANGEROUS_CONTENT",
        "HARM_CATEGORY_IMAGE_HARASSMENT",
        "HARM_CATEGORY_IMAGE_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_JAILBREAK",
    ]
    overwrittenThreshold: typing.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]
    probability: typing.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]
    probabilityScore: float
    severity: typing.Literal[
        "HARM_SEVERITY_UNSPECIFIED",
        "HARM_SEVERITY_NEGLIGIBLE",
        "HARM_SEVERITY_LOW",
        "HARM_SEVERITY_MEDIUM",
        "HARM_SEVERITY_HIGH",
    ]
    severityScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1SafetyResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SafetySetting(typing.TypedDict, total=False):
    category: typing.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
        "HARM_CATEGORY_IMAGE_HATE",
        "HARM_CATEGORY_IMAGE_DANGEROUS_CONTENT",
        "HARM_CATEGORY_IMAGE_HARASSMENT",
        "HARM_CATEGORY_IMAGE_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_JAILBREAK",
    ]
    method: typing.Literal["HARM_BLOCK_METHOD_UNSPECIFIED", "SEVERITY", "PROBABILITY"]
    threshold: typing.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SafetySpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1SampleConfig(typing.TypedDict, total=False):
    followingBatchSamplePercentage: int
    initialBatchSamplePercentage: int
    sampleStrategy: typing.Literal["SAMPLE_STRATEGY_UNSPECIFIED", "UNCERTAINTY"]

@typing.type_check_only
class GoogleCloudAiplatformV1SampledShapleyAttribution(typing.TypedDict, total=False):
    pathCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SamplingStrategy(typing.TypedDict, total=False):
    randomSampleConfig: GoogleCloudAiplatformV1SamplingStrategyRandomSampleConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SamplingStrategyRandomSampleConfig(
    typing.TypedDict, total=False
):
    sampleRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironment(typing.TypedDict, total=False):
    connectionInfo: GoogleCloudAiplatformV1SandboxEnvironmentConnectionInfo
    createTime: str
    displayName: str
    expireTime: str
    latestSandboxEnvironmentSnapshot: str
    name: str
    owner: str
    sandboxEnvironmentSnapshot: str
    sandboxEnvironmentTemplate: str
    spec: GoogleCloudAiplatformV1SandboxEnvironmentSpec
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STATE_PROVISIONING",
        "STATE_RUNNING",
        "STATE_DEPROVISIONING",
        "STATE_TERMINATED",
        "STATE_DELETED",
    ]
    ttl: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentConnectionInfo(
    typing.TypedDict, total=False
):
    loadBalancerHostname: str
    loadBalancerIp: str
    routingToken: str
    sandboxInternalIp: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentSnapshot(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    expireTime: str
    name: str
    owner: str
    parentSnapshot: str
    postSnapshotAction: typing.Literal[
        "POST_SNAPSHOT_ACTION_UNSPECIFIED", "RUNNING", "PAUSE"
    ]
    sizeBytes: str
    sourceSandboxEnvironment: str
    ttl: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentSpec(typing.TypedDict, total=False):
    codeExecutionEnvironment: (
        GoogleCloudAiplatformV1SandboxEnvironmentSpecCodeExecutionEnvironment
    )

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentSpecCodeExecutionEnvironment(
    typing.TypedDict, total=False
):
    codeLanguage: typing.Literal[
        "LANGUAGE_UNSPECIFIED", "LANGUAGE_PYTHON", "LANGUAGE_JAVASCRIPT"
    ]
    machineConfig: typing.Literal[
        "MACHINE_CONFIG_UNSPECIFIED", "MACHINE_CONFIG_VCPU4_RAM4GIB"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplate(typing.TypedDict, total=False):
    createTime: str
    customContainerEnvironment: (
        GoogleCloudAiplatformV1SandboxEnvironmentTemplateCustomContainerEnvironment
    )
    defaultContainerEnvironment: (
        GoogleCloudAiplatformV1SandboxEnvironmentTemplateDefaultContainerEnvironment
    )
    displayName: str
    egressControlConfig: (
        GoogleCloudAiplatformV1SandboxEnvironmentTemplateEgressControlConfig
    )
    ingressControlConfig: GoogleCloudAiplatformV1PrivateServiceConnectConfig
    name: str
    state: typing.Literal[
        "UNSPECIFIED", "PROVISIONING", "ACTIVE", "DEPROVISIONING", "DELETED", "FAILED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplateCustomContainerEnvironment(
    typing.TypedDict, total=False
):
    customContainerSpec: (
        GoogleCloudAiplatformV1SandboxEnvironmentTemplateCustomContainerSpec
    )
    ports: _list[GoogleCloudAiplatformV1SandboxEnvironmentTemplateNetworkPort]
    resources: GoogleCloudAiplatformV1SandboxEnvironmentTemplateResourceRequirements

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplateCustomContainerSpec(
    typing.TypedDict, total=False
):
    imageUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplateDefaultContainerEnvironment(
    typing.TypedDict, total=False
):
    defaultContainerCategory: typing.Literal[
        "DEFAULT_CONTAINER_CATEGORY_UNSPECIFIED",
        "DEFAULT_CONTAINER_CATEGORY_COMPUTER_USE",
        "DEFAULT_CONTAINER_CATEGORY_SHELL_SANDBOX",
    ]
    resources: GoogleCloudAiplatformV1SandboxEnvironmentTemplateResourceRequirements

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplateEgressControlConfig(
    typing.TypedDict, total=False
):
    customerVpcNetwork: str
    dnsPeeringConfigs: _list[
        GoogleCloudAiplatformV1SandboxEnvironmentTemplateEgressControlConfigDnsPeeringConfig
    ]
    internetAccess: bool
    networkAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplateEgressControlConfigDnsPeeringConfig(
    typing.TypedDict, total=False
):
    domain: str
    targetNetwork: str
    targetProject: str

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplateNetworkPort(
    typing.TypedDict, total=False
):
    port: int
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "TCP", "UDP"]

@typing.type_check_only
class GoogleCloudAiplatformV1SandboxEnvironmentTemplateResourceRequirements(
    typing.TypedDict, total=False
):
    limits: dict[str, typing.Any]
    requests: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1SavedQuery(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1Scalar(typing.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1Schedule(typing.TypedDict, total=False):
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
    maxConcurrentActiveRunCount: str
    maxConcurrentRunCount: str
    maxRunCount: str
    name: str
    nextRunTime: str
    startTime: str
    startedRunCount: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "PAUSED", "COMPLETED"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1ScheduleRunResponse(typing.TypedDict, total=False):
    runResponse: str
    scheduledRunTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1Scheduling(typing.TypedDict, total=False):
    disableRetries: bool
    maxWaitDuration: str
    restartJobOnWorkerRestart: bool
    strategy: typing.Literal[
        "STRATEGY_UNSPECIFIED",
        "ON_DEMAND",
        "LOW_COST",
        "STANDARD",
        "SPOT",
        "FLEX_START",
    ]
    timeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1Schema(typing.TypedDict, total=False):
    additionalProperties: typing.Any
    anyOf: _list[GoogleCloudAiplatformV1Schema]
    default: typing.Any
    defs: dict[str, typing.Any]
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
    ref: str
    required: _list[str]
    title: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "STRING",
        "NUMBER",
        "INTEGER",
        "BOOLEAN",
        "ARRAY",
        "OBJECT",
        "NULL",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaAnnotationSpecColor(typing.TypedDict, total=False):
    color: GoogleTypeColor
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageBoundingBoxAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageClassificationAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageDataItem(typing.TypedDict, total=False):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageDatasetMetadata(typing.TypedDict, total=False):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageSegmentationAnnotation(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    annotationSpecColors: _list[GoogleCloudAiplatformV1SchemaAnnotationSpecColor]
    maskGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolygonAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaImageSegmentationAnnotationPolylineAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics(
    typing.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsClassificationEvaluationMetrics(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    annotationSpecs: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef
    ]
    rows: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef(
    typing.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetrics(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    observedQuantile: float
    quantile: float
    scaledPinballLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsGeneralTextGenerationEvaluationMetrics(
    typing.TypedDict, total=False
):
    bleu: float
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageObjectDetectionEvaluationMetrics(
    typing.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageSegmentationEvaluationMetrics(
    typing.TypedDict, total=False
):
    confidenceMetricsEntries: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix
    diceScoreCoefficient: float
    iouScore: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsPairwiseTextGenerationEvaluationMetrics(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    exactMatch: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsRegressionEvaluationMetrics(
    typing.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsSummarizationEvaluationMetrics(
    typing.TypedDict, total=False
):
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextExtractionEvaluationMetrics(
    typing.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: GoogleCloudAiplatformV1SchemaModelevaluationMetricsConfusionMatrix

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsTextSentimentEvaluationMetrics(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    boundingBoxIou: float
    confidenceThreshold: float
    mismatchRate: float
    trackingPrecision: float
    trackingRecall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetrics(
    typing.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics
    ]
    meanAveragePrecision: float
    precisionWindowLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionRecognitionMetrics(
    typing.TypedDict, total=False
):
    evaluatedActionCount: int
    videoActionMetrics: _list[
        GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoActionMetrics
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaModelevaluationMetricsVideoObjectTrackingMetrics(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceImageObjectDetectionPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceImageSegmentationPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceTextClassificationPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceTextExtractionPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    key: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceTextSentimentPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceVideoActionRecognitionPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceVideoClassificationPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictInstanceVideoObjectTrackingPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfig(
    typing.TypedDict, total=False
):
    disableAttribution: bool
    sources: _list[GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfigSourceEntry]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfigSourceEntry(
    typing.TypedDict, total=False
):
    enterpriseDatastore: str
    inlineContext: str
    type: typing.Literal[
        "UNSPECIFIED", "WEB", "ENTERPRISE", "VERTEX_AI_SEARCH", "INLINE"
    ]
    vertexAiSearchDatastore: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsImageClassificationPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsImageObjectDetectionPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsImageSegmentationPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsVideoActionRecognitionPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsVideoClassificationPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    oneSecIntervalClassification: bool
    segmentClassification: bool
    shotClassification: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictParamsVideoObjectTrackingPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    minBoundingBoxSize: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionClassificationPredictionResult(
    typing.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionImageObjectDetectionPredictionResult(
    typing.TypedDict, total=False
):
    bboxes: _list[_list[typing.Any]]
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionImageSegmentationPredictionResult(
    typing.TypedDict, total=False
):
    categoryMask: str
    confidenceMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTabularClassificationPredictionResult(
    typing.TypedDict, total=False
):
    classes: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTabularRegressionPredictionResult(
    typing.TypedDict, total=False
):
    lowerBound: float
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    upperBound: float
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTextExtractionPredictionResult(
    typing.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]
    textSegmentEndOffsets: _list[str]
    textSegmentStartOffsets: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTextSentimentPredictionResult(
    typing.TypedDict, total=False
):
    sentiment: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTftFeatureImportance(
    typing.TypedDict, total=False
):
    attributeColumns: _list[str]
    attributeWeights: _list[float]
    contextColumns: _list[str]
    contextWeights: _list[float]
    horizonColumns: _list[str]
    horizonWeights: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionTimeSeriesForecastingPredictionResult(
    typing.TypedDict, total=False
):
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    tftFeatureImportance: (
        GoogleCloudAiplatformV1SchemaPredictPredictionTftFeatureImportance
    )
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionVideoActionRecognitionPredictionResult(
    typing.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionVideoClassificationPredictionResult(
    typing.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictPredictionVideoObjectTrackingPredictionResult(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    timeOffset: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictionResult(typing.TypedDict, total=False):
    error: GoogleCloudAiplatformV1SchemaPredictionResultError
    instance: dict[str, typing.Any]
    key: str
    prediction: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPredictionResultError(typing.TypedDict, total=False):
    message: str
    status: typing.Literal[
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
class GoogleCloudAiplatformV1SchemaPromptApiSchema(typing.TypedDict, total=False):
    apiSchemaVersion: str
    executions: _list[GoogleCloudAiplatformV1SchemaPromptInstancePromptExecution]
    multimodalPrompt: GoogleCloudAiplatformV1SchemaPromptSpecMultimodalPrompt
    structuredPrompt: GoogleCloudAiplatformV1SchemaPromptSpecStructuredPrompt
    translationPrompt: GoogleCloudAiplatformV1SchemaPromptSpecTranslationPrompt

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptInstancePromptExecution(
    typing.TypedDict, total=False
):
    arguments: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptInstanceVariableValue(
    typing.TypedDict, total=False
):
    partList: GoogleCloudAiplatformV1SchemaPromptSpecPartList

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecAppBuilderData(
    typing.TypedDict, total=False
):
    codeRepositoryState: str
    framework: typing.Literal["FRAMEWORK_UNSPECIFIED", "REACT", "ANGULAR"]
    linkedResources: _list[
        GoogleCloudAiplatformV1SchemaPromptSpecAppBuilderDataLinkedResource
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecAppBuilderDataLinkedResource(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecInteractionData(
    typing.TypedDict, total=False
):
    interactionIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecMultimodalPrompt(
    typing.TypedDict, total=False
):
    promptMessage: GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecPartList(typing.TypedDict, total=False):
    parts: _list[GoogleCloudAiplatformV1Part]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    sourceSentence: str
    targetSentence: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecReferenceSentencePairList(
    typing.TypedDict, total=False
):
    referenceSentencePairs: _list[
        GoogleCloudAiplatformV1SchemaPromptSpecReferenceSentencePair
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecStructuredPrompt(
    typing.TypedDict, total=False
):
    appBuilderData: GoogleCloudAiplatformV1SchemaPromptSpecAppBuilderData
    context: GoogleCloudAiplatformV1Content
    examples: _list[GoogleCloudAiplatformV1SchemaPromptSpecPartList]
    infillPrefix: str
    infillSuffix: str
    inputPrefixes: _list[str]
    interactionData: GoogleCloudAiplatformV1SchemaPromptSpecInteractionData
    outputPrefixes: _list[str]
    predictionInputs: _list[GoogleCloudAiplatformV1SchemaPromptSpecPartList]
    promptMessage: GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationExample(
    typing.TypedDict, total=False
):
    referenceSentencePairLists: _list[
        GoogleCloudAiplatformV1SchemaPromptSpecReferenceSentencePairList
    ]
    referenceSentencesFileInputs: _list[
        GoogleCloudAiplatformV1SchemaPromptSpecTranslationSentenceFileInput
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationFileInputSource(
    typing.TypedDict, total=False
):
    content: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationGcsInputSource(
    typing.TypedDict, total=False
):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationOption(
    typing.TypedDict, total=False
):
    numberOfShots: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationPrompt(
    typing.TypedDict, total=False
):
    example: GoogleCloudAiplatformV1SchemaPromptSpecTranslationExample
    option: GoogleCloudAiplatformV1SchemaPromptSpecTranslationOption
    promptMessage: GoogleCloudAiplatformV1SchemaPromptSpecPromptMessage
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaPromptSpecTranslationSentenceFileInput(
    typing.TypedDict, total=False
):
    fileInputSource: GoogleCloudAiplatformV1SchemaPromptSpecTranslationFileInputSource
    gcsInputSource: GoogleCloudAiplatformV1SchemaPromptSpecTranslationGcsInputSource

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadata(typing.TypedDict, total=False):
    inputConfig: GoogleCloudAiplatformV1SchemaTablesDatasetMetadataInputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadataBigQuerySource(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadataGcsSource(
    typing.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTablesDatasetMetadataInputConfig(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1SchemaTablesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1SchemaTablesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextClassificationAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextDataItem(typing.TypedDict, total=False):
    gcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextDatasetMetadata(typing.TypedDict, total=False):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextExtractionAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    textSegment: GoogleCloudAiplatformV1SchemaTextSegment

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextPromptDatasetMetadata(
    typing.TypedDict, total=False
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
class GoogleCloudAiplatformV1SchemaTextSegment(typing.TypedDict, total=False):
    content: str
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextSentimentAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    sentiment: int
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTextSentimentSavedQueryMetadata(
    typing.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSegment(typing.TypedDict, total=False):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadata(
    typing.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataInputConfig
    timeColumn: str
    timeSeriesIdentifierColumn: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataBigQuerySource(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataGcsSource(
    typing.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataInputConfig(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1SchemaTimeSeriesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecasting(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputs
    metadata: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputs(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation(
    typing.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlForecastingMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassification(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs(
    typing.TypedDict, total=False
):
    baseModelId: str
    budgetMilliNodeHours: str
    disableEarlyStopping: bool
    modelType: typing.Literal[
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
    typing.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetection(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs(
    typing.TypedDict, total=False
):
    budgetMilliNodeHours: str
    disableEarlyStopping: bool
    modelType: typing.Literal[
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
    typing.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentation(
    typing.TypedDict, total=False
):
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs
    )
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs(
    typing.TypedDict, total=False
):
    baseModelId: str
    budgetMilliNodeHours: str
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD_HIGH_ACCURACY_1",
        "CLOUD_LOW_ACCURACY_1",
        "MOBILE_TF_LOW_LATENCY_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata(
    typing.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTables(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputs(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTablesMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextClassification(
    typing.TypedDict, total=False
):
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs
    )

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs(
    typing.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextExtraction(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextSentiment(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs(
    typing.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoActionRecognition(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs(
    typing.TypedDict, total=False
):
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
        "MOBILE_CORAL_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoClassification(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs(
    typing.TypedDict, total=False
):
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoObjectTracking(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs(
    typing.TypedDict, total=False
):
    modelType: typing.Literal[
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
    typing.TypedDict, total=False
):
    checkpointName: str
    datasetConfig: dict[str, typing.Any]
    studySpec: GoogleCloudAiplatformV1StudySpec
    trainerConfig: dict[str, typing.Any]
    trainerType: typing.Literal[
        "TRAINER_TYPE_UNSPECIFIED", "AUTOML_TRAINER", "MODEL_GARDEN_TRAINER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionCustomJobMetadata(
    typing.TypedDict, total=False
):
    backingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionCustomTask(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1CustomJobSpec
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionCustomJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig(
    typing.TypedDict, total=False
):
    destinationBigqueryUri: str
    overrideExistingTable: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHierarchyConfig(
    typing.TypedDict, total=False
):
    groupColumns: _list[str]
    groupTemporalTotalWeight: float
    groupTotalWeight: float
    temporalTotalWeight: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata(
    typing.TypedDict, total=False
):
    backingHyperparameterTuningJob: str
    bestTrialBackingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec(
    typing.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxTrialCount: int
    parallelTrialCount: int
    studySpec: GoogleCloudAiplatformV1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningTask(
    typing.TypedDict, total=False
):
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec
    )
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecasting(
    typing.TypedDict, total=False
):
    inputs: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs
    )
    metadata: (
        GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation(
    typing.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecasting(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputs
    metadata: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputs(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformation(
    typing.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionTftForecastingMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaTrainingjobDefinitionWindowConfig(
    typing.TypedDict, total=False
):
    column: str
    maxCount: str
    strideLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVertex(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoActionRecognitionAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoClassificationAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoDataItem(typing.TypedDict, total=False):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoDatasetMetadata(typing.TypedDict, total=False):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVideoObjectTrackingAnnotation(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SchemaVisualInspectionMaskSavedQueryMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchDataItemsResponse(typing.TypedDict, total=False):
    dataItemViews: _list[GoogleCloudAiplatformV1DataItemView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchEntryPoint(typing.TypedDict, total=False):
    renderedContent: str
    sdkBlob: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchFeaturesResponse(typing.TypedDict, total=False):
    features: _list[GoogleCloudAiplatformV1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchMigratableResourcesRequest(
    typing.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchMigratableResourcesResponse(
    typing.TypedDict, total=False
):
    migratableResources: _list[GoogleCloudAiplatformV1MigratableResource]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    topFeatureCount: int
    type: typing.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse(
    typing.TypedDict, total=False
):
    monitoringStats: _list[GoogleCloudAiplatformV1ModelMonitoringStatsAnomalies]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1SearchNearestEntitiesRequest(
    typing.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1NearestNeighborQuery
    returnFullEntity: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SearchNearestEntitiesResponse(
    typing.TypedDict, total=False
):
    nearestNeighbors: GoogleCloudAiplatformV1NearestNeighbors

@typing.type_check_only
class GoogleCloudAiplatformV1SecretEnvVar(typing.TypedDict, total=False):
    name: str
    secretRef: GoogleCloudAiplatformV1SecretRef

@typing.type_check_only
class GoogleCloudAiplatformV1SecretRef(typing.TypedDict, total=False):
    secret: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1Segment(typing.TypedDict, total=False):
    endIndex: int
    partIndex: int
    startIndex: int
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1SemanticGovernancePolicy(typing.TypedDict, total=False):
    agent: str
    agentIdentity: str
    createTime: str
    description: str
    displayName: str
    etag: str
    mcpTools: _list[GoogleCloudAiplatformV1SemanticGovernancePolicyMcpTool]
    name: str
    naturalLanguageConstraint: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1SemanticGovernancePolicyEngine(
    typing.TypedDict, total=False
):
    createTime: str
    gatewayConfigs: dict[str, typing.Any]
    ipAddress: str
    name: str
    pscForwardingRule: str
    pscServiceAttachment: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "ACTIVE",
        "DEPROVISIONING",
        "INACTIVE",
        "FAILED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1SemanticGovernancePolicyMcpTool(
    typing.TypedDict, total=False
):
    mcpServer: str
    tools: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ServiceAccountSpec(typing.TypedDict, total=False):
    enableCustomServiceAccount: bool
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1Session(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    sessionState: dict[str, typing.Any]
    ttl: str
    updateTime: str
    userId: str

@typing.type_check_only
class GoogleCloudAiplatformV1SessionEvent(typing.TypedDict, total=False):
    actions: GoogleCloudAiplatformV1EventActions
    author: str
    content: GoogleCloudAiplatformV1Content
    errorCode: str
    errorMessage: str
    eventMetadata: GoogleCloudAiplatformV1EventMetadata
    invocationId: str
    name: str
    rawEvent: dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class GoogleCloudAiplatformV1SharePointSources(typing.TypedDict, total=False):
    sharePointSources: _list[GoogleCloudAiplatformV1SharePointSourcesSharePointSource]

@typing.type_check_only
class GoogleCloudAiplatformV1SharePointSourcesSharePointSource(
    typing.TypedDict, total=False
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
class GoogleCloudAiplatformV1ShieldedVmConfig(typing.TypedDict, total=False):
    enableSecureBoot: bool

@typing.type_check_only
class GoogleCloudAiplatformV1SlackSource(typing.TypedDict, total=False):
    channels: _list[GoogleCloudAiplatformV1SlackSourceSlackChannels]

@typing.type_check_only
class GoogleCloudAiplatformV1SlackSourceSlackChannels(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1ApiAuthApiKeyConfig
    channels: _list[GoogleCloudAiplatformV1SlackSourceSlackChannelsSlackChannel]

@typing.type_check_only
class GoogleCloudAiplatformV1SlackSourceSlackChannelsSlackChannel(
    typing.TypedDict, total=False
):
    channelId: str
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1SmoothGradConfig(typing.TypedDict, total=False):
    featureNoiseSigma: GoogleCloudAiplatformV1FeatureNoiseSigma
    noiseSigma: float
    noisySampleCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SpeakerVoiceConfig(typing.TypedDict, total=False):
    speaker: str
    voiceConfig: GoogleCloudAiplatformV1VoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1SpecialistPool(typing.TypedDict, total=False):
    displayName: str
    name: str
    pendingDataLabelingJobs: _list[str]
    specialistManagerEmails: _list[str]
    specialistManagersCount: int
    specialistWorkerEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1SpeculativeDecodingSpec(typing.TypedDict, total=False):
    draftModelSpeculation: (
        GoogleCloudAiplatformV1SpeculativeDecodingSpecDraftModelSpeculation
    )
    ngramSpeculation: GoogleCloudAiplatformV1SpeculativeDecodingSpecNgramSpeculation
    speculativeTokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SpeculativeDecodingSpecDraftModelSpeculation(
    typing.TypedDict, total=False
):
    draftModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1SpeculativeDecodingSpecNgramSpeculation(
    typing.TypedDict, total=False
):
    ngramSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1SpeechConfig(typing.TypedDict, total=False):
    languageCode: str
    multiSpeakerVoiceConfig: GoogleCloudAiplatformV1MultiSpeakerVoiceConfig
    voiceConfig: GoogleCloudAiplatformV1VoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1StartNotebookRuntimeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1StartNotebookRuntimeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1StopNotebookRuntimeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1StopTrialRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1StratifiedSplit(typing.TypedDict, total=False):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1StreamQueryReasoningEngineRequest(
    typing.TypedDict, total=False
):
    classMethod: str
    input: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1StreamRawPredictRequest(typing.TypedDict, total=False):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingPredictRequest(typing.TypedDict, total=False):
    inputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingPredictResponse(typing.TypedDict, total=False):
    outputs: _list[GoogleCloudAiplatformV1Tensor]
    parameters: GoogleCloudAiplatformV1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest(
    typing.TypedDict, total=False
):
    entityIds: _list[str]
    featureSelector: GoogleCloudAiplatformV1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1StringArray(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StructFieldValue(typing.TypedDict, total=False):
    name: str
    value: GoogleCloudAiplatformV1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1StructValue(typing.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1StructFieldValue]

@typing.type_check_only
class GoogleCloudAiplatformV1Study(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    inactiveReason: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"]
    studySpec: GoogleCloudAiplatformV1StudySpec

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpec(typing.TypedDict, total=False):
    algorithm: typing.Literal["ALGORITHM_UNSPECIFIED", "GRID_SEARCH", "RANDOM_SEARCH"]
    convexAutomatedStoppingSpec: (
        GoogleCloudAiplatformV1StudySpecConvexAutomatedStoppingSpec
    )
    decayCurveStoppingSpec: (
        GoogleCloudAiplatformV1StudySpecDecayCurveAutomatedStoppingSpec
    )
    measurementSelectionType: typing.Literal[
        "MEASUREMENT_SELECTION_TYPE_UNSPECIFIED", "LAST_MEASUREMENT", "BEST_MEASUREMENT"
    ]
    medianAutomatedStoppingSpec: (
        GoogleCloudAiplatformV1StudySpecMedianAutomatedStoppingSpec
    )
    metrics: _list[GoogleCloudAiplatformV1StudySpecMetricSpec]
    observationNoise: typing.Literal["OBSERVATION_NOISE_UNSPECIFIED", "LOW", "HIGH"]
    parameters: _list[GoogleCloudAiplatformV1StudySpecParameterSpec]
    studyStoppingConfig: GoogleCloudAiplatformV1StudySpecStudyStoppingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecConvexAutomatedStoppingSpec(
    typing.TypedDict, total=False
):
    learningRateParameterName: str
    maxStepCount: str
    minMeasurementCount: str
    minStepCount: str
    updateAllStoppedTrials: bool
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecDecayCurveAutomatedStoppingSpec(
    typing.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecMedianAutomatedStoppingSpec(
    typing.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecMetricSpec(typing.TypedDict, total=False):
    goal: typing.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str
    safetyConfig: GoogleCloudAiplatformV1StudySpecMetricSpecSafetyMetricConfig

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecMetricSpecSafetyMetricConfig(
    typing.TypedDict, total=False
):
    desiredMinSafeTrialsFraction: float
    safetyThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpec(typing.TypedDict, total=False):
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
    scaleType: typing.Literal[
        "SCALE_TYPE_UNSPECIFIED",
        "UNIT_LINEAR_SCALE",
        "UNIT_LOG_SCALE",
        "UNIT_REVERSE_LOG_SCALE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecCategoricalValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpec(
    typing.TypedDict, total=False
):
    parameterSpec: GoogleCloudAiplatformV1StudySpecParameterSpec
    parentCategoricalValues: GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition
    parentDiscreteValues: GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition
    parentIntValues: GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecIntValueCondition

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition(
    typing.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecConditionalParameterSpecIntValueCondition(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecDiscreteValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: float
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecDoubleValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: float
    maxValue: float
    minValue: float

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecParameterSpecIntegerValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: str
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1StudySpecStudyStoppingConfig(
    typing.TypedDict, total=False
):
    maxDurationNoProgress: str
    maxNumTrials: int
    maxNumTrialsNoProgress: int
    maximumRuntimeConstraint: GoogleCloudAiplatformV1StudyTimeConstraint
    minNumTrials: int
    minimumRuntimeConstraint: GoogleCloudAiplatformV1StudyTimeConstraint
    shouldStopAsap: bool

@typing.type_check_only
class GoogleCloudAiplatformV1StudyTimeConstraint(typing.TypedDict, total=False):
    endTime: str
    maxDuration: str

@typing.type_check_only
class GoogleCloudAiplatformV1SuggestTrialsMetadata(typing.TypedDict, total=False):
    clientId: str
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SuggestTrialsRequest(typing.TypedDict, total=False):
    clientId: str
    contexts: _list[GoogleCloudAiplatformV1TrialContext]
    suggestionCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1SuggestTrialsResponse(typing.TypedDict, total=False):
    endTime: str
    startTime: str
    studyState: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"]
    trials: _list[GoogleCloudAiplatformV1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationHelpfulnessInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1SummarizationHelpfulnessInstance
    metricSpec: GoogleCloudAiplatformV1SummarizationHelpfulnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationHelpfulnessInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationHelpfulnessResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationHelpfulnessSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualityInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1SummarizationQualityInstance
    metricSpec: GoogleCloudAiplatformV1SummarizationQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualityInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualityResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationQualitySpec(typing.TypedDict, total=False):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbosityInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1SummarizationVerbosityInstance
    metricSpec: GoogleCloudAiplatformV1SummarizationVerbositySpec

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbosityInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbosityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1SummarizationVerbositySpec(typing.TypedDict, total=False):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1SummaryMetrics(typing.TypedDict, total=False):
    failedItems: int
    metrics: dict[str, typing.Any]
    totalItems: int

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedHyperParameters(typing.TypedDict, total=False):
    adapterSize: typing.Literal[
        "ADAPTER_SIZE_UNSPECIFIED",
        "ADAPTER_SIZE_ONE",
        "ADAPTER_SIZE_TWO",
        "ADAPTER_SIZE_FOUR",
        "ADAPTER_SIZE_EIGHT",
        "ADAPTER_SIZE_SIXTEEN",
        "ADAPTER_SIZE_THIRTY_TWO",
    ]
    epochCount: str
    learningRateMultiplier: float

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedTuningDataStats(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    count: float
    left: float
    right: float

@typing.type_check_only
class GoogleCloudAiplatformV1SupervisedTuningSpec(typing.TypedDict, total=False):
    evaluationConfig: GoogleCloudAiplatformV1EvaluationConfig
    exportLastCheckpointOnly: bool
    hyperParameters: GoogleCloudAiplatformV1SupervisedHyperParameters
    trainingDatasetUri: str
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1SuspendOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1SuspendOnlineEvaluatorRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SyncFeatureViewRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SyncFeatureViewResponse(typing.TypedDict, total=False):
    featureViewSync: str

@typing.type_check_only
class GoogleCloudAiplatformV1SyntheticExample(typing.TypedDict, total=False):
    fields: _list[GoogleCloudAiplatformV1SyntheticField]

@typing.type_check_only
class GoogleCloudAiplatformV1SyntheticField(typing.TypedDict, total=False):
    content: GoogleCloudAiplatformV1Content
    fieldName: str

@typing.type_check_only
class GoogleCloudAiplatformV1TFRecordDestination(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1TaskDescriptionStrategy(typing.TypedDict, total=False):
    taskDescription: str

@typing.type_check_only
class GoogleCloudAiplatformV1Tensor(typing.TypedDict, total=False):
    boolVal: _list[bool]
    bytesVal: _list[str]
    doubleVal: _list[float]
    dtype: typing.Literal[
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
class GoogleCloudAiplatformV1Tensorboard(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1TensorboardBlob(typing.TypedDict, total=False):
    data: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardBlobSequence(typing.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardExperiment(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    source: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardRun(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTensor(typing.TypedDict, total=False):
    value: str
    versionNumber: int

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTimeSeries(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    metadata: GoogleCloudAiplatformV1TensorboardTimeSeriesMetadata
    name: str
    pluginData: str
    pluginName: str
    updateTime: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTimeSeriesMetadata(
    typing.TypedDict, total=False
):
    maxBlobSequenceLength: str
    maxStep: str
    maxWallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1TextResponseFormat(typing.TypedDict, total=False):
    mimeType: typing.Literal["MIME_TYPE_UNSPECIFIED", "APPLICATION_JSON", "TEXT_PLAIN"]
    schema: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1ThresholdConfig(typing.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1TimeSeriesData(typing.TypedDict, total=False):
    tensorboardTimeSeriesId: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]
    values: _list[GoogleCloudAiplatformV1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1TimeSeriesDataPoint(typing.TypedDict, total=False):
    blobs: GoogleCloudAiplatformV1TensorboardBlobSequence
    scalar: GoogleCloudAiplatformV1Scalar
    step: str
    tensor: GoogleCloudAiplatformV1TensorboardTensor
    wallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1TimestampSplit(typing.TypedDict, total=False):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1TokensInfo(typing.TypedDict, total=False):
    role: str
    tokenIds: _list[str]
    tokens: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1Tool(typing.TypedDict, total=False):
    codeExecution: GoogleCloudAiplatformV1ToolCodeExecution
    computerUse: GoogleCloudAiplatformV1ToolComputerUse
    enterpriseWebSearch: GoogleCloudAiplatformV1EnterpriseWebSearch
    exaAiSearch: GoogleCloudAiplatformV1ToolExaAiSearch
    functionDeclarations: _list[GoogleCloudAiplatformV1FunctionDeclaration]
    googleMaps: GoogleCloudAiplatformV1GoogleMaps
    googleSearch: GoogleCloudAiplatformV1ToolGoogleSearch
    googleSearchRetrieval: GoogleCloudAiplatformV1GoogleSearchRetrieval
    parallelAiSearch: GoogleCloudAiplatformV1ToolParallelAiSearch
    retrieval: GoogleCloudAiplatformV1Retrieval
    urlContext: GoogleCloudAiplatformV1UrlContext

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCall(typing.TypedDict, total=False):
    toolInput: str
    toolName: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1ToolCallValidInstance]
    metricSpec: GoogleCloudAiplatformV1ToolCallValidSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidResults(typing.TypedDict, total=False):
    toolCallValidMetricValues: _list[GoogleCloudAiplatformV1ToolCallValidMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCallValidSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolCodeExecution(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolComputerUse(typing.TypedDict, total=False):
    enablePromptInjectionDetection: bool
    environment: typing.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_BROWSER",
        "ENVIRONMENT_MOBILE",
        "ENVIRONMENT_DESKTOP",
    ]
    excludedPredefinedFunctions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolConfig(typing.TypedDict, total=False):
    functionCallingConfig: GoogleCloudAiplatformV1FunctionCallingConfig
    retrievalConfig: GoogleCloudAiplatformV1RetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1ToolExaAiSearch(typing.TypedDict, total=False):
    apiKey: str
    customConfigs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolGoogleSearch(typing.TypedDict, total=False):
    blockingConfidence: typing.Literal[
        "PHISH_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_HIGH_AND_ABOVE",
        "BLOCK_HIGHER_AND_ABOVE",
        "BLOCK_VERY_HIGH_AND_ABOVE",
        "BLOCK_ONLY_EXTREMELY_HIGH",
    ]
    excludeDomains: _list[str]
    searchTypes: GoogleCloudAiplatformV1ToolGoogleSearchSearchTypes

@typing.type_check_only
class GoogleCloudAiplatformV1ToolGoogleSearchImageSearch(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolGoogleSearchSearchTypes(typing.TypedDict, total=False):
    imageSearch: GoogleCloudAiplatformV1ToolGoogleSearchImageSearch
    webSearch: GoogleCloudAiplatformV1ToolGoogleSearchWebSearch

@typing.type_check_only
class GoogleCloudAiplatformV1ToolGoogleSearchWebSearch(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1ToolNameMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ToolNameMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchResults(typing.TypedDict, total=False):
    toolNameMatchMetricValues: _list[GoogleCloudAiplatformV1ToolNameMatchMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolNameMatchSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParallelAiSearch(typing.TypedDict, total=False):
    apiKey: str
    customConfigs: dict[str, typing.Any]
    enableDataRetention: bool
    enableZeroDataRetention: bool

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1ToolParameterKVMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ToolParameterKVMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchInstance(
    typing.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchResults(typing.TypedDict, total=False):
    toolParameterKvMatchMetricValues: _list[
        GoogleCloudAiplatformV1ToolParameterKVMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKVMatchSpec(typing.TypedDict, total=False):
    useStrictStringMatch: bool

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1ToolParameterKeyMatchInstance]
    metricSpec: GoogleCloudAiplatformV1ToolParameterKeyMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchInstance(
    typing.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchResults(
    typing.TypedDict, total=False
):
    toolParameterKeyMatchMetricValues: _list[
        GoogleCloudAiplatformV1ToolParameterKeyMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1ToolParameterKeyMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrainingConfig(typing.TypedDict, total=False):
    timeoutTrainingMilliHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1TrainingPipeline(typing.TypedDict, total=False):
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
    state: typing.Literal[
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
class GoogleCloudAiplatformV1Trajectory(typing.TypedDict, total=False):
    toolCalls: _list[GoogleCloudAiplatformV1ToolCall]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectoryAnyOrderMatchInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryAnyOrderMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchResults(
    typing.TypedDict, total=False
):
    trajectoryAnyOrderMatchMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryAnyOrderMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryAnyOrderMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1TrajectoryExactMatchInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryExactMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchResults(typing.TypedDict, total=False):
    trajectoryExactMatchMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryExactMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryExactMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1TrajectoryInOrderMatchInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryInOrderMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchResults(
    typing.TypedDict, total=False
):
    trajectoryInOrderMatchMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryInOrderMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryInOrderMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1TrajectoryPrecisionInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryPrecisionSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionInstance(typing.TypedDict, total=False):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionResults(typing.TypedDict, total=False):
    trajectoryPrecisionMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryPrecisionMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryPrecisionSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1TrajectoryRecallInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectoryRecallSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallInstance(typing.TypedDict, total=False):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallResults(typing.TypedDict, total=False):
    trajectoryRecallMetricValues: _list[
        GoogleCloudAiplatformV1TrajectoryRecallMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectoryRecallSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1TrajectorySingleToolUseInstance]
    metricSpec: GoogleCloudAiplatformV1TrajectorySingleToolUseSpec

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseResults(
    typing.TypedDict, total=False
):
    trajectorySingleToolUseMetricValues: _list[
        GoogleCloudAiplatformV1TrajectorySingleToolUseMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1TrajectorySingleToolUseSpec(typing.TypedDict, total=False):
    toolName: str

@typing.type_check_only
class GoogleCloudAiplatformV1Transcription(typing.TypedDict, total=False):
    finished: bool
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1Trial(typing.TypedDict, total=False):
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
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "REQUESTED",
        "ACTIVE",
        "STOPPING",
        "SUCCEEDED",
        "INFEASIBLE",
    ]
    webAccessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1TrialContext(typing.TypedDict, total=False):
    description: str
    parameters: _list[GoogleCloudAiplatformV1TrialParameter]

@typing.type_check_only
class GoogleCloudAiplatformV1TrialParameter(typing.TypedDict, total=False):
    parameterId: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1TunedModel(typing.TypedDict, total=False):
    checkpoints: _list[GoogleCloudAiplatformV1TunedModelCheckpoint]
    endpoint: str
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1TunedModelCheckpoint(typing.TypedDict, total=False):
    checkpointId: str
    endpoint: str
    epoch: str
    step: str

@typing.type_check_only
class GoogleCloudAiplatformV1TunedModelRef(typing.TypedDict, total=False):
    pipelineJob: str
    tunedModel: str
    tuningJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1TuningDataStats(typing.TypedDict, total=False):
    preferenceOptimizationDataStats: (
        GoogleCloudAiplatformV1PreferenceOptimizationDataStats
    )
    supervisedTuningDataStats: GoogleCloudAiplatformV1SupervisedTuningDataStats

@typing.type_check_only
class GoogleCloudAiplatformV1TuningJob(typing.TypedDict, total=False):
    baseModel: str
    createTime: str
    description: str
    encryptionSpec: GoogleCloudAiplatformV1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    evaluateDatasetRuns: _list[GoogleCloudAiplatformV1EvaluateDatasetRun]
    experiment: str
    labels: dict[str, typing.Any]
    name: str
    preTunedModel: GoogleCloudAiplatformV1PreTunedModel
    preferenceOptimizationSpec: GoogleCloudAiplatformV1PreferenceOptimizationSpec
    serviceAccount: str
    startTime: str
    state: typing.Literal[
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
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployIndexRequest(typing.TypedDict, total=False):
    deployedIndexId: str

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployIndexResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployModelRequest(typing.TypedDict, total=False):
    deployedModelId: str
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1UndeployModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UnmanagedContainerModel(typing.TypedDict, total=False):
    artifactUri: str
    containerSpec: GoogleCloudAiplatformV1ModelContainerSpec
    predictSchemata: GoogleCloudAiplatformV1PredictSchemata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateDeploymentResourcePoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateEndpointLongRunningRequest(
    typing.TypedDict, total=False
):
    endpoint: GoogleCloudAiplatformV1Endpoint

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateExplanationDatasetOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateExplanationDatasetRequest(
    typing.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1Examples

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateExplanationDatasetResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureGroupOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureOnlineStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeatureViewOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateFeaturestoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateIndexOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: (
        GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateModelDeploymentMonitoringJobOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpdatePersistentResourceOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateSpecialistPoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    specialistPool: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpdateTensorboardOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UpgradeNotebookRuntimeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpgradeNotebookRuntimeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UploadModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1UploadModelRequest(typing.TypedDict, total=False):
    model: GoogleCloudAiplatformV1Model
    modelId: str
    parentModel: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1UploadModelResponse(typing.TypedDict, total=False):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1UploadRagFileConfig(typing.TypedDict, total=False):
    ragFileTransformationConfig: GoogleCloudAiplatformV1RagFileTransformationConfig

@typing.type_check_only
class GoogleCloudAiplatformV1UploadRagFileRequest(typing.TypedDict, total=False):
    ragFile: GoogleCloudAiplatformV1RagFile
    uploadRagFileConfig: GoogleCloudAiplatformV1UploadRagFileConfig

@typing.type_check_only
class GoogleCloudAiplatformV1UploadRagFileResponse(typing.TypedDict, total=False):
    error: GoogleRpcStatus
    ragFile: GoogleCloudAiplatformV1RagFile

@typing.type_check_only
class GoogleCloudAiplatformV1UpsertDatapointsRequest(typing.TypedDict, total=False):
    datapoints: _list[GoogleCloudAiplatformV1IndexDatapoint]
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1UpsertDatapointsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UrlContext(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1UrlContextMetadata(typing.TypedDict, total=False):
    urlMetadata: _list[GoogleCloudAiplatformV1UrlMetadata]

@typing.type_check_only
class GoogleCloudAiplatformV1UrlMetadata(typing.TypedDict, total=False):
    retrievedUrl: str
    urlRetrievalStatus: typing.Literal[
        "URL_RETRIEVAL_STATUS_UNSPECIFIED",
        "URL_RETRIEVAL_STATUS_SUCCESS",
        "URL_RETRIEVAL_STATUS_ERROR",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1UsageMetadata(typing.TypedDict, total=False):
    cacheTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    cachedContentTokenCount: int
    candidatesTokenCount: int
    candidatesTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    promptTokenCount: int
    promptTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    thoughtsTokenCount: int
    toolUsePromptTokenCount: int
    toolUsePromptTokensDetails: _list[GoogleCloudAiplatformV1ModalityTokenCount]
    totalTokenCount: int
    trafficType: typing.Literal[
        "TRAFFIC_TYPE_UNSPECIFIED",
        "ON_DEMAND",
        "ON_DEMAND_PRIORITY",
        "ON_DEMAND_FLEX",
        "ON_DEMAND_OFFPEAK",
        "PROVISIONED_THROUGHPUT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1UserActionReference(typing.TypedDict, total=False):
    dataLabelingJob: str
    method: str
    operation: str

@typing.type_check_only
class GoogleCloudAiplatformV1UserScenario(typing.TypedDict, total=False):
    conversationPlan: str
    startingPrompt: str
    testCaseTitle: str

@typing.type_check_only
class GoogleCloudAiplatformV1UserScenarioGenerationConfig(
    typing.TypedDict, total=False
):
    environmentData: str
    modelName: str
    simulationInstruction: str
    userScenarioCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1Value(typing.TypedDict, total=False):
    doubleValue: float
    intValue: str
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1VertexAISearch(typing.TypedDict, total=False):
    dataStoreSpecs: _list[GoogleCloudAiplatformV1VertexAISearchDataStoreSpec]
    datastore: str
    engine: str
    filter: str
    maxResults: int

@typing.type_check_only
class GoogleCloudAiplatformV1VertexAISearchDataStoreSpec(typing.TypedDict, total=False):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudAiplatformV1VertexAiSearchConfig(typing.TypedDict, total=False):
    servingConfig: str

@typing.type_check_only
class GoogleCloudAiplatformV1VertexMultimodalDatasetDestination(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1BigQueryDestination
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1VertexMultimodalDatasetSource(
    typing.TypedDict, total=False
):
    datasetName: str

@typing.type_check_only
class GoogleCloudAiplatformV1VertexRagStore(typing.TypedDict, total=False):
    ragResources: _list[GoogleCloudAiplatformV1VertexRagStoreRagResource]
    ragRetrievalConfig: GoogleCloudAiplatformV1RagRetrievalConfig
    similarityTopK: int
    vectorDistanceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1VertexRagStoreRagResource(typing.TypedDict, total=False):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1VideoMetadata(typing.TypedDict, total=False):
    endOffset: str
    fps: float
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1VideoResponseFormat(typing.TypedDict, total=False):
    aspectRatio: typing.Literal[
        "ASPECT_RATIO_UNSPECIFIED",
        "ASPECT_RATIO_SIXTEEN_BY_NINE",
        "ASPECT_RATIO_NINE_BY_SIXTEEN",
    ]
    delivery: typing.Literal["DELIVERY_UNSPECIFIED", "INLINE", "URI"]
    duration: str
    gcsUri: str
    resolution: str

@typing.type_check_only
class GoogleCloudAiplatformV1VoiceConfig(typing.TypedDict, total=False):
    prebuiltVoiceConfig: GoogleCloudAiplatformV1PrebuiltVoiceConfig
    replicatedVoiceConfig: GoogleCloudAiplatformV1ReplicatedVoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1WorkerPoolSpec(typing.TypedDict, total=False):
    containerSpec: GoogleCloudAiplatformV1ContainerSpec
    diskSpec: GoogleCloudAiplatformV1DiskSpec
    lustreMounts: _list[GoogleCloudAiplatformV1LustreMount]
    machineSpec: GoogleCloudAiplatformV1MachineSpec
    nfsMounts: _list[GoogleCloudAiplatformV1NfsMount]
    pythonPackageSpec: GoogleCloudAiplatformV1PythonPackageSpec
    replicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesPayload(typing.TypedDict, total=False):
    entityId: str
    featureValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesRequest(typing.TypedDict, total=False):
    payloads: _list[GoogleCloudAiplatformV1WriteFeatureValuesPayload]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest(
    typing.TypedDict, total=False
):
    writeRunDataRequests: _list[GoogleCloudAiplatformV1WriteTensorboardRunDataRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardExperimentDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardRunDataRequest(
    typing.TypedDict, total=False
):
    tensorboardRun: str
    timeSeriesData: _list[GoogleCloudAiplatformV1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardRunDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1XraiAttribution(typing.TypedDict, total=False):
    blurBaselineConfig: GoogleCloudAiplatformV1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1SmoothGradConfig
    stepCount: int

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
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

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
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleTypeInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleTypeLatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
