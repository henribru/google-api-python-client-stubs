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
class GenaiVertexV1beta1AgentInteraction(typing.TypedDict, total=False):
    agent: str
    antigravityConfig: GenaiVertexV1beta1AntigravityAgentConfig
    codeMenderConfig: GenaiVertexV1beta1CodeMenderAgentConfig
    deepResearchConfig: GenaiVertexV1beta1DeepResearchAgentConfig
    dynamicConfig: GenaiVertexV1beta1DynamicAgentConfig

@typing.type_check_only
class GenaiVertexV1beta1AllowedTools(typing.TypedDict, total=False):
    mode: typing.Literal[
        "TOOL_CHOICE_TYPE_UNSPECIFIED", "AUTO", "ANY", "NONE", "VALIDATED"
    ]
    tools: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1AntigravityAgentConfig(typing.TypedDict, total=False):
    maxTotalTokens: str
    model: str

@typing.type_check_only
class GenaiVertexV1beta1ArgumentsDelta(typing.TypedDict, total=False):
    arguments: str

@typing.type_check_only
class GenaiVertexV1beta1AudioContent(typing.TypedDict, total=False):
    channels: int
    data: str
    mimeTypeString: str
    sampleRate: int
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1AudioDelta(typing.TypedDict, total=False):
    channels: int
    data: str
    mimeType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_WAV",
        "TYPE_MP3",
        "TYPE_AIFF",
        "TYPE_AAC",
        "TYPE_OGG",
        "TYPE_FLAC",
        "TYPE_MPEG",
        "TYPE_M4A",
        "TYPE_L16",
        "TYPE_OPUS",
        "TYPE_ALAW",
        "TYPE_MULAW",
    ]
    rate: int
    sampleRate: int
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1AudioResponseFormat(typing.TypedDict, total=False):
    bitRate: int
    delivery: typing.Literal["DELIVERY_UNSPECIFIED", "INLINE", "URI"]
    mimeType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_MP3",
        "TYPE_OGG_OPUS",
        "TYPE_L16",
        "TYPE_WAV",
        "TYPE_ALAW",
        "TYPE_MULAW",
    ]
    sampleRate: int

@typing.type_check_only
class GenaiVertexV1beta1CodeExecution(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionCallContent(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1CodeExecutionCallContentCodeExecutionCallArguments

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionCallContentCodeExecutionCallArguments(
    typing.TypedDict, total=False
):
    code: str
    language: typing.Literal["LANGUAGE_UNSPECIFIED", "PYTHON"]

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionCallDelta(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1CodeExecutionCallContentCodeExecutionCallArguments

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionCallStep(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1CodeExecutionCallStepCodeExecutionCallStepArguments

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionCallStepCodeExecutionCallStepArguments(
    typing.TypedDict, total=False
):
    code: str
    language: typing.Literal["LANGUAGE_UNSPECIFIED", "PYTHON"]

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionResultContent(typing.TypedDict, total=False):
    isError: bool
    result: str

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionResultDelta(typing.TypedDict, total=False):
    isError: bool
    result: str

@typing.type_check_only
class GenaiVertexV1beta1CodeExecutionResultStep(typing.TypedDict, total=False):
    isError: bool
    result: str

@typing.type_check_only
class GenaiVertexV1beta1CodeMenderAgentConfig(typing.TypedDict, total=False):
    findRequest: GenaiVertexV1beta1CodeMenderAgentConfigFindRequest
    fixRequest: GenaiVertexV1beta1CodeMenderAgentConfigFixRequest
    model: str
    sessionConfig: GenaiVertexV1beta1CodeMenderAgentConfigSessionConfig
    sessionId: str

@typing.type_check_only
class GenaiVertexV1beta1CodeMenderAgentConfigFileContent(typing.TypedDict, total=False):
    content: str
    path: str

@typing.type_check_only
class GenaiVertexV1beta1CodeMenderAgentConfigFindRequest(typing.TypedDict, total=False):
    description: str
    findingId: str
    mode: typing.Literal["MODE_UNSPECIFIED", "MODE_SCAN", "MODE_VERIFY"]
    sourceFiles: _list[GenaiVertexV1beta1CodeMenderAgentConfigFileContent]

@typing.type_check_only
class GenaiVertexV1beta1CodeMenderAgentConfigFixRequest(typing.TypedDict, total=False):
    description: str
    findingId: str
    sourceFiles: _list[GenaiVertexV1beta1CodeMenderAgentConfigFileContent]

@typing.type_check_only
class GenaiVertexV1beta1CodeMenderAgentConfigSessionConfig(
    typing.TypedDict, total=False
):
    maxRounds: int

@typing.type_check_only
class GenaiVertexV1beta1ComputerUse(typing.TypedDict, total=False):
    disabledSafetyPolicies: _list[
        typing.Literal[
            "SAFETY_POLICY_UNSPECIFIED",
            "FINANCIAL_TRANSACTIONS",
            "SENSITIVE_DATA_MODIFICATION",
            "COMMUNICATION_TOOL",
            "ACCOUNT_CREATION",
            "DATA_MODIFICATION",
            "USER_CONSENT_MANAGEMENT",
            "LEGAL_TERMS_AND_AGREEMENTS",
        ]
    ]
    enablePromptInjectionDetection: bool
    environment: typing.Literal[
        "ENVIRONMENT_UNSPECIFIED", "BROWSER", "MOBILE", "DESKTOP"
    ]
    excludedPredefinedFunctions: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1Content(typing.TypedDict, total=False):
    audio: GenaiVertexV1beta1AudioContent
    document: GenaiVertexV1beta1DocumentContent
    image: GenaiVertexV1beta1ImageContent
    text: GenaiVertexV1beta1TextContent
    thought: GenaiVertexV1beta1ThoughtContent
    toolCall: GenaiVertexV1beta1ToolCallContent
    toolResult: GenaiVertexV1beta1ToolResultContent
    video: GenaiVertexV1beta1VideoContent

@typing.type_check_only
class GenaiVertexV1beta1ContentDelta(typing.TypedDict, total=False):
    delta: GenaiVertexV1beta1ContentDeltaData
    index: int

@typing.type_check_only
class GenaiVertexV1beta1ContentDeltaData(typing.TypedDict, total=False):
    audio: GenaiVertexV1beta1AudioDelta
    document: GenaiVertexV1beta1DocumentDelta
    image: GenaiVertexV1beta1ImageDelta
    text: GenaiVertexV1beta1TextDelta
    textAnnotation: GenaiVertexV1beta1TextAnnotationDelta
    thoughtSignature: GenaiVertexV1beta1ThoughtSignatureDelta
    thoughtSummary: GenaiVertexV1beta1ThoughtSummaryDelta
    toolCall: GenaiVertexV1beta1ToolCallDelta
    toolResult: GenaiVertexV1beta1ToolResultDelta
    video: GenaiVertexV1beta1VideoDelta

@typing.type_check_only
class GenaiVertexV1beta1ContentList(typing.TypedDict, total=False):
    contents: _list[GenaiVertexV1beta1Content]

@typing.type_check_only
class GenaiVertexV1beta1ContentStart(typing.TypedDict, total=False):
    content: GenaiVertexV1beta1Content
    index: int

@typing.type_check_only
class GenaiVertexV1beta1ContentStop(typing.TypedDict, total=False):
    index: int

@typing.type_check_only
class GenaiVertexV1beta1CreateInteractionRequest(typing.TypedDict, total=False):
    background: bool
    interaction: GenaiVertexV1beta1Interaction
    store: bool
    stream: bool

@typing.type_check_only
class GenaiVertexV1beta1DeepResearchAgentConfig(typing.TypedDict, total=False):
    collaborativePlanning: bool
    enableBigqueryTool: bool
    thinkingSummaries: typing.Literal[
        "THINKING_SUMMARIES_UNSPECIFIED",
        "THINKING_SUMMARIES_AUTO",
        "THINKING_SUMMARIES_NONE",
    ]
    visualization: typing.Literal["UNSPECIFIED", "OFF", "AUTO"]

@typing.type_check_only
class GenaiVertexV1beta1DeleteInteractionResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1DocumentContent(typing.TypedDict, total=False):
    data: str
    mimeTypeString: str
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1DocumentDelta(typing.TypedDict, total=False):
    data: str
    mimeType: typing.Literal["TYPE_UNSPECIFIED", "TYPE_PDF", "TYPE_CSV"]
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1DynamicAgentConfig(typing.TypedDict, total=False):
    config: GenaiVertexV1beta1Struct

@typing.type_check_only
class GenaiVertexV1beta1EnvironmentConfig(typing.TypedDict, total=False):
    environmentId: str
    networkAllowlist: (
        GenaiVertexV1beta1EnvironmentConfigEnvironmentNetworkEgressAllowlist
    )
    networkMode: typing.Literal["NETWORK_MODE_UNSPECIFIED", "DISABLED"]
    sources: _list[GenaiVertexV1beta1EnvironmentConfigSource]

@typing.type_check_only
class GenaiVertexV1beta1EnvironmentConfigEgressRule(typing.TypedDict, total=False):
    domain: str
    transform: dict[str, typing.Any]

@typing.type_check_only
class GenaiVertexV1beta1EnvironmentConfigEnvironmentNetworkEgressAllowlist(
    typing.TypedDict, total=False
):
    allowlist: _list[GenaiVertexV1beta1EnvironmentConfigEgressRule]

@typing.type_check_only
class GenaiVertexV1beta1EnvironmentConfigSource(typing.TypedDict, total=False):
    content: str
    encoding: str
    source: str
    target: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "GCS", "INLINE", "REPOSITORY", "SKILL_REGISTRY"
    ]

@typing.type_check_only
class GenaiVertexV1beta1Error(typing.TypedDict, total=False):
    code: str
    message: str

@typing.type_check_only
class GenaiVertexV1beta1ErrorEvent(typing.TypedDict, total=False):
    error: GenaiVertexV1beta1Error

@typing.type_check_only
class GenaiVertexV1beta1ExaAISearchConfig(typing.TypedDict, total=False):
    apiKey: str
    customConfig: dict[str, typing.Any]

@typing.type_check_only
class GenaiVertexV1beta1Field(typing.TypedDict, total=False):
    name: str
    value: GenaiVertexV1beta1Value

@typing.type_check_only
class GenaiVertexV1beta1FileCitation(typing.TypedDict, total=False):
    customMetadata: GenaiVertexV1beta1Struct
    documentUri: str
    fileName: str
    mediaId: str
    pageNumber: int
    source: str

@typing.type_check_only
class GenaiVertexV1beta1FileSearch(typing.TypedDict, total=False):
    fileSearchStoreNames: _list[str]
    metadataFilter: str
    topK: int

@typing.type_check_only
class GenaiVertexV1beta1FileSearchCallContent(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1FileSearchCallDelta(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1FileSearchCallStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1FileSearchResultContent(typing.TypedDict, total=False):
    result: _list[GenaiVertexV1beta1FileSearchResultContentFileSearchResult]

@typing.type_check_only
class GenaiVertexV1beta1FileSearchResultContentFileSearchResult(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GenaiVertexV1beta1FileSearchResultDelta(typing.TypedDict, total=False):
    result: _list[GenaiVertexV1beta1FileSearchResultContentFileSearchResult]

@typing.type_check_only
class GenaiVertexV1beta1FileSearchResultStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1Function(typing.TypedDict, total=False):
    description: str
    name: str
    parameters: GenaiVertexV1beta1Value

@typing.type_check_only
class GenaiVertexV1beta1FunctionCallContent(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1Struct
    name: str

@typing.type_check_only
class GenaiVertexV1beta1FunctionCallDelta(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1Struct
    name: str

@typing.type_check_only
class GenaiVertexV1beta1FunctionCallStep(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1Struct
    name: str

@typing.type_check_only
class GenaiVertexV1beta1FunctionResultContent(typing.TypedDict, total=False):
    contentList: GenaiVertexV1beta1FunctionResultSubcontentList
    isError: bool
    name: str
    stringResult: str
    structResult: GenaiVertexV1beta1Struct

@typing.type_check_only
class GenaiVertexV1beta1FunctionResultDelta(typing.TypedDict, total=False):
    isError: bool
    name: str
    result: GenaiVertexV1beta1Value

@typing.type_check_only
class GenaiVertexV1beta1FunctionResultStep(typing.TypedDict, total=False):
    isError: bool
    name: str
    result: GenaiVertexV1beta1Value

@typing.type_check_only
class GenaiVertexV1beta1FunctionResultSubcontent(typing.TypedDict, total=False):
    image: GenaiVertexV1beta1ImageContent
    text: GenaiVertexV1beta1TextContent

@typing.type_check_only
class GenaiVertexV1beta1FunctionResultSubcontentList(typing.TypedDict, total=False):
    contents: _list[GenaiVertexV1beta1FunctionResultSubcontent]

@typing.type_check_only
class GenaiVertexV1beta1GenerationConfig(typing.TypedDict, total=False):
    imageConfig: GenaiVertexV1beta1ImageConfig
    maxOutputTokens: int
    seed: int
    speechConfig: _list[GenaiVertexV1beta1SpeechConfig]
    stopSequences: _list[str]
    temperature: float
    thinkingLevel: typing.Literal[
        "THINKING_LEVEL_UNSPECIFIED",
        "THINKING_LEVEL_MINIMAL",
        "THINKING_LEVEL_LOW",
        "THINKING_LEVEL_MEDIUM",
        "THINKING_LEVEL_HIGH",
    ]
    thinkingSummaries: typing.Literal[
        "THINKING_SUMMARIES_UNSPECIFIED",
        "THINKING_SUMMARIES_AUTO",
        "THINKING_SUMMARIES_NONE",
    ]
    toolChoiceConfig: GenaiVertexV1beta1ToolChoiceConfig
    toolChoiceMode: typing.Literal[
        "TOOL_CHOICE_TYPE_UNSPECIFIED", "AUTO", "ANY", "NONE", "VALIDATED"
    ]
    topP: float
    transcriptionConfig: GenaiVertexV1beta1TranscriptionConfig
    videoConfig: GenaiVertexV1beta1VideoConfig

@typing.type_check_only
class GenaiVertexV1beta1GoogleMaps(typing.TypedDict, total=False):
    enableWidget: bool
    latitude: float
    longitude: float

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsCallContent(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1GoogleMapsCallContentGoogleMapsCallArguments

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsCallContentGoogleMapsCallArguments(
    typing.TypedDict, total=False
):
    queries: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsCallDelta(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1GoogleMapsCallContentGoogleMapsCallArguments

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsCallStep(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1GoogleMapsCallStepGoogleMapsCallStepArguments

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsCallStepGoogleMapsCallStepArguments(
    typing.TypedDict, total=False
):
    queries: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsResultContent(typing.TypedDict, total=False):
    result: _list[GenaiVertexV1beta1GoogleMapsResultContentGoogleMapsResult]

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsResultContentGoogleMapsResult(
    typing.TypedDict, total=False
):
    places: _list[GenaiVertexV1beta1GoogleMapsResultContentGoogleMapsResultPlaces]
    widgetContextToken: str

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsResultContentGoogleMapsResultPlaces(
    typing.TypedDict, total=False
):
    name: str
    placeId: str
    reviewSnippets: _list[GenaiVertexV1beta1ReviewSnippet]
    url: str

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsResultDelta(typing.TypedDict, total=False):
    result: _list[GenaiVertexV1beta1GoogleMapsResultContentGoogleMapsResult]

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsResultStep(typing.TypedDict, total=False):
    result: _list[GenaiVertexV1beta1GoogleMapsResultStepGoogleMapsResultItem]

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsResultStepGoogleMapsResultItem(
    typing.TypedDict, total=False
):
    places: _list[
        GenaiVertexV1beta1GoogleMapsResultStepGoogleMapsResultItemGoogleMapsResultPlaces
    ]
    widgetContextToken: str

@typing.type_check_only
class GenaiVertexV1beta1GoogleMapsResultStepGoogleMapsResultItemGoogleMapsResultPlaces(
    typing.TypedDict, total=False
):
    name: str
    placeId: str
    reviewSnippets: _list[GenaiVertexV1beta1ReviewSnippet]
    url: str

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearch(typing.TypedDict, total=False):
    searchTypes: _list[
        typing.Literal[
            "SEARCH_TYPE_UNSPECIFIED",
            "SEARCH_TYPE_WEB_SEARCH",
            "SEARCH_TYPE_IMAGE_SEARCH",
            "SEARCH_TYPE_ENTERPRISE_WEB_SEARCH",
        ]
    ]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchCallContent(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1GoogleSearchCallContentGoogleSearchCallArguments
    searchType: typing.Literal[
        "SEARCH_TYPE_UNSPECIFIED",
        "SEARCH_TYPE_WEB_SEARCH",
        "SEARCH_TYPE_IMAGE_SEARCH",
        "SEARCH_TYPE_ENTERPRISE_WEB_SEARCH",
    ]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchCallContentGoogleSearchCallArguments(
    typing.TypedDict, total=False
):
    queries: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchCallDelta(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1GoogleSearchCallContentGoogleSearchCallArguments

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchCallStep(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1GoogleSearchCallStepGoogleSearchCallStepArguments
    searchType: typing.Literal[
        "SEARCH_TYPE_UNSPECIFIED",
        "SEARCH_TYPE_WEB_SEARCH",
        "SEARCH_TYPE_IMAGE_SEARCH",
        "SEARCH_TYPE_ENTERPRISE_WEB_SEARCH",
    ]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchCallStepGoogleSearchCallStepArguments(
    typing.TypedDict, total=False
):
    queries: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchResultContent(typing.TypedDict, total=False):
    isError: bool
    result: _list[GenaiVertexV1beta1GoogleSearchResultContentGoogleSearchResult]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchResultContentGoogleSearchResult(
    typing.TypedDict, total=False
):
    searchSuggestions: str

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchResultDelta(typing.TypedDict, total=False):
    isError: bool
    result: _list[GenaiVertexV1beta1GoogleSearchResultContentGoogleSearchResult]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchResultStep(typing.TypedDict, total=False):
    isError: bool
    result: _list[GenaiVertexV1beta1GoogleSearchResultStepGoogleSearchResultItem]

@typing.type_check_only
class GenaiVertexV1beta1GoogleSearchResultStepGoogleSearchResultItem(
    typing.TypedDict, total=False
):
    searchSuggestions: str

@typing.type_check_only
class GenaiVertexV1beta1ImageConfig(typing.TypedDict, total=False):
    aspectRatio: str
    imageSize: str

@typing.type_check_only
class GenaiVertexV1beta1ImageContent(typing.TypedDict, total=False):
    data: str
    mimeTypeString: str
    resolution: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "ULTRA_HIGH"
    ]
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1ImageDelta(typing.TypedDict, total=False):
    data: str
    mimeType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PNG",
        "TYPE_JPEG",
        "TYPE_WEBP",
        "TYPE_HEIC",
        "TYPE_HEIF",
        "TYPE_GIF",
        "TYPE_BMP",
        "TYPE_TIFF",
    ]
    resolution: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "ULTRA_HIGH"
    ]
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1ImageResponseFormat(typing.TypedDict, total=False):
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
    mimeType: typing.Literal["TYPE_UNSPECIFIED", "TYPE_JPEG"]

@typing.type_check_only
class GenaiVertexV1beta1Interaction(typing.TypedDict, total=False):
    agentInteraction: GenaiVertexV1beta1AgentInteraction
    content: GenaiVertexV1beta1Content
    contentList: GenaiVertexV1beta1ContentList
    created: str
    envId: str
    environmentId: str
    errors: _list[GenaiVertexV1beta1Error]
    id: str
    labels: dict[str, typing.Any]
    localEnvironment: GenaiVertexV1beta1LocalEnvironmentConfig
    modelInteraction: GenaiVertexV1beta1ModelInteraction
    outputs: _list[GenaiVertexV1beta1Content]
    previousInteractionId: str
    remoteEnvironment: GenaiVertexV1beta1EnvironmentConfig
    responseFormat: GenaiVertexV1beta1Value
    responseFormatList: GenaiVertexV1beta1ResponseFormatList
    responseFormatSingleton: GenaiVertexV1beta1ResponseFormat
    responseMimeType: str
    responseModalities: _list[
        typing.Literal[
            "RESPONSE_MODALITY_UNSPECIFIED",
            "TEXT",
            "IMAGE",
            "AUDIO",
            "VIDEO",
            "DOCUMENT",
        ]
    ]
    role: str
    safetySettings: _list[GenaiVertexV1beta1SafetySetting]
    serviceTier: typing.Literal[
        "SERVICE_TIER_UNSPECIFIED",
        "SERVICE_TIER_FLEX",
        "SERVICE_TIER_STANDARD",
        "SERVICE_TIER_PRIORITY",
        "SERVICE_TIER_DEFERRED",
    ]
    status: typing.Literal[
        "UNSPECIFIED",
        "IN_PROGRESS",
        "REQUIRES_ACTION",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
        "INCOMPLETE",
        "BUDGET_EXCEEDED",
        "QUEUED",
    ]
    stepList: GenaiVertexV1beta1StepList
    steps: _list[GenaiVertexV1beta1Step]
    stringContent: str
    systemInstruction: str
    tools: _list[GenaiVertexV1beta1Tool]
    turnList: GenaiVertexV1beta1TurnList
    updated: str
    usage: GenaiVertexV1beta1InteractionUsage

@typing.type_check_only
class GenaiVertexV1beta1InteractionCompleteEvent(typing.TypedDict, total=False):
    interaction: GenaiVertexV1beta1Interaction

@typing.type_check_only
class GenaiVertexV1beta1InteractionCompletedSseEvent(typing.TypedDict, total=False):
    interaction: GenaiVertexV1beta1Interaction

@typing.type_check_only
class GenaiVertexV1beta1InteractionCreatedSseEvent(typing.TypedDict, total=False):
    interaction: GenaiVertexV1beta1Interaction

@typing.type_check_only
class GenaiVertexV1beta1InteractionStartEvent(typing.TypedDict, total=False):
    interaction: GenaiVertexV1beta1Interaction

@typing.type_check_only
class GenaiVertexV1beta1InteractionStatusUpdate(typing.TypedDict, total=False):
    interactionId: str
    status: typing.Literal[
        "UNSPECIFIED",
        "IN_PROGRESS",
        "REQUIRES_ACTION",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
        "INCOMPLETE",
        "BUDGET_EXCEEDED",
        "QUEUED",
    ]

@typing.type_check_only
class GenaiVertexV1beta1InteractionStreamingEvent(typing.TypedDict, total=False):
    contentDelta: GenaiVertexV1beta1ContentDelta
    contentStart: GenaiVertexV1beta1ContentStart
    contentStop: GenaiVertexV1beta1ContentStop
    errorEvent: GenaiVertexV1beta1ErrorEvent
    eventId: str
    interactionCompleteEvent: GenaiVertexV1beta1InteractionCompleteEvent
    interactionCompletedEvent: GenaiVertexV1beta1InteractionCompletedSseEvent
    interactionCreatedEvent: GenaiVertexV1beta1InteractionCreatedSseEvent
    interactionStartEvent: GenaiVertexV1beta1InteractionStartEvent
    interactionStatusUpdate: GenaiVertexV1beta1InteractionStatusUpdate
    stepDelta: GenaiVertexV1beta1StepDelta
    stepStart: GenaiVertexV1beta1StepStart
    stepStop: GenaiVertexV1beta1StepStop

@typing.type_check_only
class GenaiVertexV1beta1InteractionUsage(typing.TypedDict, total=False):
    cachedTokensByModality: _list[GenaiVertexV1beta1InteractionUsageModalityTokens]
    groundingToolCount: _list[GenaiVertexV1beta1InteractionUsageGroundingToolCount]
    inputTokensByModality: _list[GenaiVertexV1beta1InteractionUsageModalityTokens]
    outputTokensByModality: _list[GenaiVertexV1beta1InteractionUsageModalityTokens]
    toolUseTokensByModality: _list[GenaiVertexV1beta1InteractionUsageModalityTokens]
    totalCachedTokens: int
    totalInputTokens: int
    totalOutputTokens: int
    totalThoughtTokens: int
    totalTokens: int
    totalToolUseTokens: int

@typing.type_check_only
class GenaiVertexV1beta1InteractionUsageGroundingToolCount(
    typing.TypedDict, total=False
):
    count: int
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "GOOGLE_SEARCH", "GOOGLE_MAPS", "RETRIEVAL"
    ]

@typing.type_check_only
class GenaiVertexV1beta1InteractionUsageModalityTokens(typing.TypedDict, total=False):
    modality: typing.Literal[
        "RESPONSE_MODALITY_UNSPECIFIED", "TEXT", "IMAGE", "AUDIO", "VIDEO", "DOCUMENT"
    ]
    tokens: int

@typing.type_check_only
class GenaiVertexV1beta1ListValue(typing.TypedDict, total=False):
    values: _list[GenaiVertexV1beta1Value]

@typing.type_check_only
class GenaiVertexV1beta1LocalEnvironmentConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1McpServer(typing.TypedDict, total=False):
    allowedTools: _list[GenaiVertexV1beta1AllowedTools]
    headers: dict[str, typing.Any]
    name: str
    url: str

@typing.type_check_only
class GenaiVertexV1beta1McpServerToolCallContent(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1Struct
    name: str
    serverName: str

@typing.type_check_only
class GenaiVertexV1beta1McpServerToolCallDelta(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1Struct
    name: str
    serverName: str

@typing.type_check_only
class GenaiVertexV1beta1McpServerToolCallStep(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1Struct
    name: str
    serverName: str

@typing.type_check_only
class GenaiVertexV1beta1McpServerToolResultContent(typing.TypedDict, total=False):
    contentList: GenaiVertexV1beta1FunctionResultSubcontentList
    name: str
    serverName: str
    stringResult: str
    structResult: GenaiVertexV1beta1Struct

@typing.type_check_only
class GenaiVertexV1beta1McpServerToolResultDelta(typing.TypedDict, total=False):
    name: str
    result: GenaiVertexV1beta1Value
    serverName: str

@typing.type_check_only
class GenaiVertexV1beta1McpServerToolResultStep(typing.TypedDict, total=False):
    name: str
    result: GenaiVertexV1beta1Value
    serverName: str

@typing.type_check_only
class GenaiVertexV1beta1ModelInteraction(typing.TypedDict, total=False):
    generationConfig: GenaiVertexV1beta1GenerationConfig
    model: str

@typing.type_check_only
class GenaiVertexV1beta1ModelOutputStep(typing.TypedDict, total=False):
    content: _list[GenaiVertexV1beta1Content]
    error: GoogleRpcStatus

@typing.type_check_only
class GenaiVertexV1beta1ParallelAISearchConfig(typing.TypedDict, total=False):
    apiKey: str
    customConfig: dict[str, typing.Any]

@typing.type_check_only
class GenaiVertexV1beta1PlaceCitation(typing.TypedDict, total=False):
    name: str
    placeId: str
    reviewSnippets: _list[GenaiVertexV1beta1ReviewSnippet]
    url: str

@typing.type_check_only
class GenaiVertexV1beta1RagStoreConfig(typing.TypedDict, total=False):
    ragResources: _list[GenaiVertexV1beta1RagStoreConfigRagResource]
    ragRetrievalConfig: GenaiVertexV1beta1RagStoreConfigRagRetrievalConfig
    similarityTopK: int
    vectorDistanceThreshold: float

@typing.type_check_only
class GenaiVertexV1beta1RagStoreConfigRagResource(typing.TypedDict, total=False):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1RagStoreConfigRagRetrievalConfig(typing.TypedDict, total=False):
    filter: GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigFilter
    hybridSearch: GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigHybridSearch
    ranking: GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigRanking
    topK: int

@typing.type_check_only
class GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigFilter(
    typing.TypedDict, total=False
):
    metadataFilter: str
    vectorDistanceThreshold: float
    vectorSimilarityThreshold: float

@typing.type_check_only
class GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigHybridSearch(
    typing.TypedDict, total=False
):
    alpha: float

@typing.type_check_only
class GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigRanking(
    typing.TypedDict, total=False
):
    rankService: GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigRankingRankService

@typing.type_check_only
class GenaiVertexV1beta1RagStoreConfigRagRetrievalConfigRankingRankService(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GenaiVertexV1beta1ResponseFormat(typing.TypedDict, total=False):
    audio: GenaiVertexV1beta1AudioResponseFormat
    image: GenaiVertexV1beta1ImageResponseFormat
    structValue: GenaiVertexV1beta1Struct
    text: GenaiVertexV1beta1TextResponseFormat
    video: GenaiVertexV1beta1VideoResponseFormat

@typing.type_check_only
class GenaiVertexV1beta1ResponseFormatList(typing.TypedDict, total=False):
    responseFormats: _list[GenaiVertexV1beta1ResponseFormat]

@typing.type_check_only
class GenaiVertexV1beta1Retrieval(typing.TypedDict, total=False):
    exaAiSearchConfig: GenaiVertexV1beta1ExaAISearchConfig
    parallelAiSearchConfig: GenaiVertexV1beta1ParallelAISearchConfig
    ragStoreConfig: GenaiVertexV1beta1RagStoreConfig
    retrievalTypes: _list[
        typing.Literal[
            "RETRIEVAL_TYPE_UNSPECIFIED",
            "RETRIEVAL_TYPE_VERTEX_AI_SEARCH",
            "RETRIEVAL_TYPE_RAG_STORE",
            "RETRIEVAL_TYPE_EXA_AI_SEARCH",
            "RETRIEVAL_TYPE_PARALLEL_AI_SEARCH",
        ]
    ]
    vertexAiSearchConfig: GenaiVertexV1beta1VertexAISearchConfig

@typing.type_check_only
class GenaiVertexV1beta1RetrievalCallDelta(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1RetrievalCallStepRetrievalStepArguments
    retrievalType: typing.Literal[
        "RETRIEVAL_TYPE_UNSPECIFIED",
        "RETRIEVAL_TYPE_VERTEX_AI_SEARCH",
        "RETRIEVAL_TYPE_RAG_STORE",
        "RETRIEVAL_TYPE_EXA_AI_SEARCH",
        "RETRIEVAL_TYPE_PARALLEL_AI_SEARCH",
    ]

@typing.type_check_only
class GenaiVertexV1beta1RetrievalCallStep(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1RetrievalCallStepRetrievalStepArguments
    retrievalType: typing.Literal[
        "RETRIEVAL_TYPE_UNSPECIFIED",
        "RETRIEVAL_TYPE_VERTEX_AI_SEARCH",
        "RETRIEVAL_TYPE_RAG_STORE",
        "RETRIEVAL_TYPE_EXA_AI_SEARCH",
        "RETRIEVAL_TYPE_PARALLEL_AI_SEARCH",
    ]

@typing.type_check_only
class GenaiVertexV1beta1RetrievalCallStepRetrievalStepArguments(
    typing.TypedDict, total=False
):
    queries: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1RetrievalResultDelta(typing.TypedDict, total=False):
    isError: bool

@typing.type_check_only
class GenaiVertexV1beta1RetrievalResultStep(typing.TypedDict, total=False):
    isError: bool

@typing.type_check_only
class GenaiVertexV1beta1ReviewSnippet(typing.TypedDict, total=False):
    reviewId: str
    title: str
    url: str

@typing.type_check_only
class GenaiVertexV1beta1SafetySetting(typing.TypedDict, total=False):
    method: typing.Literal["HARM_BLOCK_METHOD_UNSPECIFIED", "SEVERITY", "PROBABILITY"]
    threshold: typing.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]
    type: typing.Literal[
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

@typing.type_check_only
class GenaiVertexV1beta1ServerToolCallDelta(typing.TypedDict, total=False):
    codeExecutionCall: GenaiVertexV1beta1CodeExecutionCallDelta
    fileSearchCall: GenaiVertexV1beta1FileSearchCallDelta
    googleMapsCall: GenaiVertexV1beta1GoogleMapsCallDelta
    googleSearchCall: GenaiVertexV1beta1GoogleSearchCallDelta
    mcpServerToolCall: GenaiVertexV1beta1McpServerToolCallDelta
    retrievalCall: GenaiVertexV1beta1RetrievalCallDelta
    signature: str
    urlContextCall: GenaiVertexV1beta1UrlContextCallDelta

@typing.type_check_only
class GenaiVertexV1beta1ServerToolResultDelta(typing.TypedDict, total=False):
    codeExecutionResult: GenaiVertexV1beta1CodeExecutionResultDelta
    fileSearchResult: GenaiVertexV1beta1FileSearchResultDelta
    googleMapsResult: GenaiVertexV1beta1GoogleMapsResultDelta
    googleSearchResult: GenaiVertexV1beta1GoogleSearchResultDelta
    mcpServerToolResult: GenaiVertexV1beta1McpServerToolResultDelta
    retrievalResult: GenaiVertexV1beta1RetrievalResultDelta
    signature: str
    urlContextResult: GenaiVertexV1beta1UrlContextResultDelta

@typing.type_check_only
class GenaiVertexV1beta1SpeechConfig(typing.TypedDict, total=False):
    language: str
    speaker: str
    voice: str

@typing.type_check_only
class GenaiVertexV1beta1Step(typing.TypedDict, total=False):
    modelOutput: GenaiVertexV1beta1ModelOutputStep
    thought: GenaiVertexV1beta1ThoughtStep
    toolCall: GenaiVertexV1beta1ToolCallStep
    toolResult: GenaiVertexV1beta1ToolResultStep
    userInput: GenaiVertexV1beta1UserInputStep

@typing.type_check_only
class GenaiVertexV1beta1StepDelta(typing.TypedDict, total=False):
    delta: GenaiVertexV1beta1StepDeltaData
    index: int

@typing.type_check_only
class GenaiVertexV1beta1StepDeltaData(typing.TypedDict, total=False):
    argumentsDelta: GenaiVertexV1beta1ArgumentsDelta
    audio: GenaiVertexV1beta1AudioDelta
    document: GenaiVertexV1beta1DocumentDelta
    functionResult: GenaiVertexV1beta1FunctionResultDelta
    image: GenaiVertexV1beta1ImageDelta
    serverToolCall: GenaiVertexV1beta1ServerToolCallDelta
    serverToolResult: GenaiVertexV1beta1ServerToolResultDelta
    text: GenaiVertexV1beta1TextDelta
    textAnnotationDelta: GenaiVertexV1beta1TextAnnotationDelta
    thoughtSignature: GenaiVertexV1beta1ThoughtSignatureDelta
    thoughtSummary: GenaiVertexV1beta1ThoughtSummaryDelta
    video: GenaiVertexV1beta1VideoDelta

@typing.type_check_only
class GenaiVertexV1beta1StepList(typing.TypedDict, total=False):
    steps: _list[GenaiVertexV1beta1Step]

@typing.type_check_only
class GenaiVertexV1beta1StepStart(typing.TypedDict, total=False):
    index: int
    step: GenaiVertexV1beta1Step

@typing.type_check_only
class GenaiVertexV1beta1StepStop(typing.TypedDict, total=False):
    index: int
    stepUsage: GenaiVertexV1beta1InteractionUsage
    usage: GenaiVertexV1beta1InteractionUsage

@typing.type_check_only
class GenaiVertexV1beta1Struct(typing.TypedDict, total=False):
    fields: _list[GenaiVertexV1beta1Field]

@typing.type_check_only
class GenaiVertexV1beta1TextAnnotationDelta(typing.TypedDict, total=False):
    annotations: _list[GenaiVertexV1beta1TextContentAnnotation]

@typing.type_check_only
class GenaiVertexV1beta1TextContent(typing.TypedDict, total=False):
    annotations: _list[GenaiVertexV1beta1TextContentAnnotation]
    text: str

@typing.type_check_only
class GenaiVertexV1beta1TextContentAnnotation(typing.TypedDict, total=False):
    endIndex: int
    fileCitation: GenaiVertexV1beta1FileCitation
    placeCitation: GenaiVertexV1beta1PlaceCitation
    startIndex: int
    urlCitation: GenaiVertexV1beta1UrlCitation
    wordInfo: GenaiVertexV1beta1WordInfo

@typing.type_check_only
class GenaiVertexV1beta1TextDelta(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GenaiVertexV1beta1TextResponseFormat(typing.TypedDict, total=False):
    mimeType: typing.Literal[
        "TYPE_UNSPECIFIED", "TYPE_APPLICATION_JSON", "TYPE_TEXT_PLAIN"
    ]
    schema: GenaiVertexV1beta1Struct

@typing.type_check_only
class GenaiVertexV1beta1ThoughtContent(typing.TypedDict, total=False):
    signature: str
    summary: _list[GenaiVertexV1beta1ThoughtSummaryContent]

@typing.type_check_only
class GenaiVertexV1beta1ThoughtSignatureDelta(typing.TypedDict, total=False):
    signature: str

@typing.type_check_only
class GenaiVertexV1beta1ThoughtStep(typing.TypedDict, total=False):
    signature: str
    summary: _list[GenaiVertexV1beta1Content]

@typing.type_check_only
class GenaiVertexV1beta1ThoughtSummaryContent(typing.TypedDict, total=False):
    image: GenaiVertexV1beta1ImageContent
    text: GenaiVertexV1beta1TextContent

@typing.type_check_only
class GenaiVertexV1beta1ThoughtSummaryDelta(typing.TypedDict, total=False):
    content: GenaiVertexV1beta1Content

@typing.type_check_only
class GenaiVertexV1beta1Tool(typing.TypedDict, total=False):
    codeExecution: GenaiVertexV1beta1CodeExecution
    computerUse: GenaiVertexV1beta1ComputerUse
    fileSearch: GenaiVertexV1beta1FileSearch
    function: GenaiVertexV1beta1Function
    googleMaps: GenaiVertexV1beta1GoogleMaps
    googleSearch: GenaiVertexV1beta1GoogleSearch
    mcpServer: GenaiVertexV1beta1McpServer
    retrieval: GenaiVertexV1beta1Retrieval
    urlContext: GenaiVertexV1beta1UrlContext

@typing.type_check_only
class GenaiVertexV1beta1ToolCallContent(typing.TypedDict, total=False):
    codeExecutionCall: GenaiVertexV1beta1CodeExecutionCallContent
    fileSearchCall: GenaiVertexV1beta1FileSearchCallContent
    functionCall: GenaiVertexV1beta1FunctionCallContent
    googleMapsCall: GenaiVertexV1beta1GoogleMapsCallContent
    googleSearchCall: GenaiVertexV1beta1GoogleSearchCallContent
    id: str
    mcpServerToolCall: GenaiVertexV1beta1McpServerToolCallContent
    signature: str
    urlContextCall: GenaiVertexV1beta1UrlContextCallContent

@typing.type_check_only
class GenaiVertexV1beta1ToolCallDelta(typing.TypedDict, total=False):
    codeExecutionCall: GenaiVertexV1beta1CodeExecutionCallDelta
    fileSearchCall: GenaiVertexV1beta1FileSearchCallDelta
    functionCall: GenaiVertexV1beta1FunctionCallDelta
    googleMapsCall: GenaiVertexV1beta1GoogleMapsCallDelta
    googleSearchCall: GenaiVertexV1beta1GoogleSearchCallDelta
    id: str
    mcpServerToolCall: GenaiVertexV1beta1McpServerToolCallDelta
    signature: str
    urlContextCall: GenaiVertexV1beta1UrlContextCallDelta

@typing.type_check_only
class GenaiVertexV1beta1ToolCallStep(typing.TypedDict, total=False):
    codeExecutionCall: GenaiVertexV1beta1CodeExecutionCallStep
    fileSearchCall: GenaiVertexV1beta1FileSearchCallStep
    functionCall: GenaiVertexV1beta1FunctionCallStep
    googleMapsCall: GenaiVertexV1beta1GoogleMapsCallStep
    googleSearchCall: GenaiVertexV1beta1GoogleSearchCallStep
    id: str
    mcpServerToolCall: GenaiVertexV1beta1McpServerToolCallStep
    retrievalCall: GenaiVertexV1beta1RetrievalCallStep
    signature: str
    urlContextCall: GenaiVertexV1beta1UrlContextCallStep

@typing.type_check_only
class GenaiVertexV1beta1ToolChoiceConfig(typing.TypedDict, total=False):
    allowedTools: GenaiVertexV1beta1AllowedTools

@typing.type_check_only
class GenaiVertexV1beta1ToolResultContent(typing.TypedDict, total=False):
    callId: str
    codeExecutionResult: GenaiVertexV1beta1CodeExecutionResultContent
    fileSearchResult: GenaiVertexV1beta1FileSearchResultContent
    functionResult: GenaiVertexV1beta1FunctionResultContent
    googleMapsResult: GenaiVertexV1beta1GoogleMapsResultContent
    googleSearchResult: GenaiVertexV1beta1GoogleSearchResultContent
    mcpServerToolResult: GenaiVertexV1beta1McpServerToolResultContent
    signature: str
    urlContextResult: GenaiVertexV1beta1UrlContextResultContent

@typing.type_check_only
class GenaiVertexV1beta1ToolResultDelta(typing.TypedDict, total=False):
    callId: str
    codeExecutionResult: GenaiVertexV1beta1CodeExecutionResultDelta
    fileSearchResult: GenaiVertexV1beta1FileSearchResultDelta
    functionResult: GenaiVertexV1beta1FunctionResultDelta
    googleMapsResult: GenaiVertexV1beta1GoogleMapsResultDelta
    googleSearchResult: GenaiVertexV1beta1GoogleSearchResultDelta
    mcpServerToolResult: GenaiVertexV1beta1McpServerToolResultDelta
    signature: str
    urlContextResult: GenaiVertexV1beta1UrlContextResultDelta

@typing.type_check_only
class GenaiVertexV1beta1ToolResultStep(typing.TypedDict, total=False):
    callId: str
    codeExecutionResult: GenaiVertexV1beta1CodeExecutionResultStep
    fileSearchResult: GenaiVertexV1beta1FileSearchResultStep
    functionResult: GenaiVertexV1beta1FunctionResultStep
    googleMapsResult: GenaiVertexV1beta1GoogleMapsResultStep
    googleSearchResult: GenaiVertexV1beta1GoogleSearchResultStep
    mcpServerToolResult: GenaiVertexV1beta1McpServerToolResultStep
    retrievalResult: GenaiVertexV1beta1RetrievalResultStep
    signature: str
    urlContextResult: GenaiVertexV1beta1UrlContextResultStep

@typing.type_check_only
class GenaiVertexV1beta1TranscriptionConfig(typing.TypedDict, total=False):
    adaptationPhrases: _list[str]
    customVocabulary: _list[str]
    diarizationMode: str
    languageCodes: _list[str]
    timestampGranularities: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1Turn(typing.TypedDict, total=False):
    contentList: GenaiVertexV1beta1ContentList
    contentString: str
    role: str

@typing.type_check_only
class GenaiVertexV1beta1TurnList(typing.TypedDict, total=False):
    turns: _list[GenaiVertexV1beta1Turn]

@typing.type_check_only
class GenaiVertexV1beta1UrlCitation(typing.TypedDict, total=False):
    title: str
    url: str

@typing.type_check_only
class GenaiVertexV1beta1UrlContext(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenaiVertexV1beta1UrlContextCallContent(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1UrlContextCallContentUrlContextCallArguments

@typing.type_check_only
class GenaiVertexV1beta1UrlContextCallContentUrlContextCallArguments(
    typing.TypedDict, total=False
):
    urls: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1UrlContextCallDelta(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1UrlContextCallContentUrlContextCallArguments

@typing.type_check_only
class GenaiVertexV1beta1UrlContextCallStep(typing.TypedDict, total=False):
    arguments: GenaiVertexV1beta1UrlContextCallStepUrlContextCallStepArguments

@typing.type_check_only
class GenaiVertexV1beta1UrlContextCallStepUrlContextCallStepArguments(
    typing.TypedDict, total=False
):
    urls: _list[str]

@typing.type_check_only
class GenaiVertexV1beta1UrlContextResultContent(typing.TypedDict, total=False):
    isError: bool
    result: _list[GenaiVertexV1beta1UrlContextResultContentUrlContextResult]

@typing.type_check_only
class GenaiVertexV1beta1UrlContextResultContentUrlContextResult(
    typing.TypedDict, total=False
):
    status: typing.Literal[
        "STATUS_UNSPECIFIED", "SUCCESS", "ERROR", "PAYWALL", "UNSAFE"
    ]
    url: str

@typing.type_check_only
class GenaiVertexV1beta1UrlContextResultDelta(typing.TypedDict, total=False):
    isError: bool
    result: _list[GenaiVertexV1beta1UrlContextResultContentUrlContextResult]

@typing.type_check_only
class GenaiVertexV1beta1UrlContextResultStep(typing.TypedDict, total=False):
    isError: bool
    result: _list[GenaiVertexV1beta1UrlContextResultStepUrlContextResultItem]

@typing.type_check_only
class GenaiVertexV1beta1UrlContextResultStepUrlContextResultItem(
    typing.TypedDict, total=False
):
    status: typing.Literal[
        "STATUS_UNSPECIFIED", "SUCCESS", "ERROR", "PAYWALL", "UNSAFE"
    ]
    url: str

@typing.type_check_only
class GenaiVertexV1beta1UserInputStep(typing.TypedDict, total=False):
    contentList: GenaiVertexV1beta1ContentList
    contentString: str

@typing.type_check_only
class GenaiVertexV1beta1Value(typing.TypedDict, total=False):
    boolValue: bool
    contentValue: GenaiVertexV1beta1Content
    listValue: GenaiVertexV1beta1ListValue
    nullValue: typing.Literal["NULL_VALUE"]
    numberValue: float
    stringValue: str
    structValue: GenaiVertexV1beta1Struct

@typing.type_check_only
class GenaiVertexV1beta1VertexAISearchConfig(typing.TypedDict, total=False):
    datastores: _list[str]
    engine: str

@typing.type_check_only
class GenaiVertexV1beta1VideoConfig(typing.TypedDict, total=False):
    task: typing.Literal[
        "TASK_UNSPECIFIED",
        "TEXT_TO_VIDEO",
        "IMAGE_TO_VIDEO",
        "REFERENCE_TO_VIDEO",
        "EDIT",
    ]

@typing.type_check_only
class GenaiVertexV1beta1VideoContent(typing.TypedDict, total=False):
    data: str
    mimeTypeString: str
    resolution: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "ULTRA_HIGH"
    ]
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1VideoDelta(typing.TypedDict, total=False):
    data: str
    mimeType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_MP4",
        "TYPE_MPEG",
        "TYPE_MPG",
        "TYPE_MOV",
        "TYPE_AVI",
        "TYPE_X_FLV",
        "TYPE_WEBM",
        "TYPE_WMV",
        "TYPE_3GPP",
    ]
    resolution: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "ULTRA_HIGH"
    ]
    uri: str

@typing.type_check_only
class GenaiVertexV1beta1VideoResponseFormat(typing.TypedDict, total=False):
    aspectRatio: typing.Literal[
        "ASPECT_RATIO_UNSPECIFIED",
        "ASPECT_RATIO_SIXTEEN_BY_NINE",
        "ASPECT_RATIO_NINE_BY_SIXTEEN",
    ]
    delivery: typing.Literal["DELIVERY_UNSPECIFIED", "INLINE", "URI"]
    duration: str
    gcsUri: str

@typing.type_check_only
class GenaiVertexV1beta1WordInfo(typing.TypedDict, total=False):
    endOffset: str
    speaker: str
    startOffset: str
    text: str

@typing.type_check_only
class GoogleApiHttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aPart(typing.TypedDict, total=False):
    data: dict[str, typing.Any]
    filename: str
    mediaType: str
    metadata: dict[str, typing.Any]
    raw: str
    text: str
    url: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTask(typing.TypedDict, total=False):
    appId: str
    artifacts: _list[GoogleCloudAiplatformV1beta1A2aTaskArtifact]
    contextId: str
    createTime: str
    expireTime: str
    generation: str
    history: _list[GoogleCloudAiplatformV1beta1A2aTaskMessage]
    metadata: dict[str, typing.Any]
    name: str
    nextEventSequenceNumber: str
    output: GoogleCloudAiplatformV1beta1TaskOutput
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "SUBMITTED",
        "WORKING",
        "COMPLETED",
        "CANCELLED",
        "FAILED",
        "REJECTED",
        "INPUT_REQUIRED",
        "AUTH_REQUIRED",
        "PAUSED",
    ]
    status: GoogleCloudAiplatformV1beta1A2aTaskStatus
    statusDetails: GoogleCloudAiplatformV1beta1TaskStatusDetails
    ttl: str
    updateTime: str
    userId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskArtifact(typing.TypedDict, total=False):
    artifactId: str
    description: str
    displayName: str
    extensions: _list[str]
    metadata: dict[str, typing.Any]
    parts: _list[GoogleCloudAiplatformV1beta1A2aPart]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskArtifactChange(typing.TypedDict, total=False):
    append: bool
    artifact: GoogleCloudAiplatformV1beta1A2aTaskArtifact
    lastChunk: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskEvent(typing.TypedDict, total=False):
    createTime: str
    eventData: GoogleCloudAiplatformV1beta1A2aTaskEventData
    generation: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskEventData(typing.TypedDict, total=False):
    artifactChange: GoogleCloudAiplatformV1beta1A2aTaskArtifactChange
    historyAppend: GoogleCloudAiplatformV1beta1A2aTaskHistoryAppend
    metadataChange: GoogleCloudAiplatformV1beta1A2aTaskMetadataChange
    statusUpdate: GoogleCloudAiplatformV1beta1A2aTaskStatusUpdate

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskHistoryAppend(typing.TypedDict, total=False):
    message: GoogleCloudAiplatformV1beta1A2aTaskMessage

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskMessage(typing.TypedDict, total=False):
    extensions: _list[str]
    messageId: str
    metadata: dict[str, typing.Any]
    parts: _list[GoogleCloudAiplatformV1beta1A2aPart]
    referenceTaskIds: _list[str]
    role: typing.Literal["ROLE_UNSPECIFIED", "ROLE_USER", "ROLE_AGENT"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskMetadataChange(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskStatus(typing.TypedDict, total=False):
    message: GoogleCloudAiplatformV1beta1A2aTaskMessage
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "TASK_STATE_SUBMITTED",
        "TASK_STATE_WORKING",
        "TASK_STATE_COMPLETED",
        "TASK_STATE_FAILED",
        "TASK_STATE_CANCELED",
        "TASK_STATE_INPUT_REQUIRED",
        "TASK_STATE_REJECTED",
        "TASK_STATE_AUTH_REQUIRED",
    ]
    timestamp: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1A2aTaskStatusUpdate(typing.TypedDict, total=False):
    message: GoogleCloudAiplatformV1beta1A2aTaskMessage
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "TASK_STATE_SUBMITTED",
        "TASK_STATE_WORKING",
        "TASK_STATE_COMPLETED",
        "TASK_STATE_FAILED",
        "TASK_STATE_CANCELED",
        "TASK_STATE_INPUT_REQUIRED",
        "TASK_STATE_REJECTED",
        "TASK_STATE_AUTH_REQUIRED",
    ]
    timestamp: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AcceptPublisherModelEulaRequest(
    typing.TypedDict, total=False
):
    publisherModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ActivateOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ActivateOnlineEvaluatorRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ActiveLearningConfig(typing.TypedDict, total=False):
    maxDataItemCount: str
    maxDataItemPercentage: int
    sampleConfig: GoogleCloudAiplatformV1beta1SampleConfig
    trainingConfig: GoogleCloudAiplatformV1beta1TrainingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsRequest(
    typing.TypedDict, total=False
):
    artifacts: _list[str]
    executions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextChildrenRequest(
    typing.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextChildrenResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddExecutionEventsRequest(
    typing.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1beta1Event]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddExecutionEventsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddTrialMeasurementRequest(
    typing.TypedDict, total=False
):
    measurement: GoogleCloudAiplatformV1beta1Measurement

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Agent(typing.TypedDict, total=False):
    base_agent: str
    base_environment: typing.Any
    created: str
    description: str
    id: str
    metadata: dict[str, typing.Any]
    name: str
    object: str
    system_instruction: str
    tools: _list[GoogleCloudAiplatformV1beta1AgentTool]
    updated: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AgentAnomalyDetectionScope(
    typing.TypedDict, total=False
):
    displayName: str
    logBuckets: _list[str]
    name: str
    observabilityBuckets: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AgentConfig(typing.TypedDict, total=False):
    agentId: str
    agentType: str
    description: str
    instruction: str
    subAgents: _list[str]
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AgentData(typing.TypedDict, total=False):
    agents: dict[str, typing.Any]
    turns: _list[GoogleCloudAiplatformV1beta1ConversationTurn]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AgentEvent(typing.TypedDict, total=False):
    activeTools: _list[GoogleCloudAiplatformV1beta1Tool]
    author: str
    content: GoogleCloudAiplatformV1beta1Content
    eventTime: str
    stateDelta: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AgentResource(typing.TypedDict, total=False):
    agent: str
    agentFramework: typing.Literal["AGENT_FRAMEWORK_UNSPECIFIED", "ADK"]
    agentType: typing.Literal[
        "AGENT_TYPE_UNSPECIFIED",
        "REASONING_ENGINE",
        "CLOUD_RUN_SERVICE",
        "GKE_WORKLOAD",
        "GCE_INSTANCE",
        "AGENT_TYPE_OTHER",
    ]
    location: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AgentTool(typing.TypedDict, total=False):
    headers: dict[str, typing.Any]
    name: str
    type: str
    url: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AggregateAnalyzedSessionsResponse(
    typing.TypedDict, total=False
):
    agentAggregates: _list[
        GoogleCloudAiplatformV1beta1AggregateAnalyzedSessionsResponseAgentAggregate
    ]
    nextPageToken: str
    summary: GoogleCloudAiplatformV1beta1ListAnalyzedSessionsResponseViewSummary

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AggregateAnalyzedSessionsResponseAgentAggregate(
    typing.TypedDict, total=False
):
    agentDisplayName: str
    agentResourceName: str
    agentStatus: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ACTIVE", "ENABLING", "DISABLED"
    ]
    agentType: typing.Literal[
        "AGENT_TYPE_UNSPECIFIED",
        "REASONING_ENGINE",
        "CLOUD_RUN_SERVICE",
        "GKE_WORKLOAD",
        "GCE_INSTANCE",
        "AGENT_TYPE_OTHER",
    ]
    anomalousSessionsCount: int
    latestSessionTime: str
    location: str
    monitoredAgent: str
    severities: dict[str, typing.Any]
    totalSessionsCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AggregationOutput(typing.TypedDict, total=False):
    aggregationResults: _list[GoogleCloudAiplatformV1beta1AggregationResult]
    dataset: GoogleCloudAiplatformV1beta1EvaluationDataset

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AggregationResult(typing.TypedDict, total=False):
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
    bleuMetricValue: GoogleCloudAiplatformV1beta1BleuMetricValue
    customCodeExecutionResult: GoogleCloudAiplatformV1beta1CustomCodeExecutionResult
    exactMatchMetricValue: GoogleCloudAiplatformV1beta1ExactMatchMetricValue
    pairwiseMetricResult: GoogleCloudAiplatformV1beta1PairwiseMetricResult
    pointwiseMetricResult: GoogleCloudAiplatformV1beta1PointwiseMetricResult
    rougeMetricValue: GoogleCloudAiplatformV1beta1RougeMetricValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AnalyzedInvocation(typing.TypedDict, total=False):
    assessment: GoogleCloudAiplatformV1beta1Assessment
    invocationId: str
    invocationState: typing.Literal[
        "INVOCATION_STATE_UNSPECIFIED",
        "INVOCATION_STATE_ANOMALOUS",
        "INVOCATION_STATE_NOT_ANOMALOUS",
    ]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AnalyzedSession(typing.TypedDict, total=False):
    agentDisplayName: str
    agentResourceName: str
    agentState: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ACTIVE", "ENABLING", "DISABLED"
    ]
    agentType: typing.Literal[
        "AGENT_TYPE_UNSPECIFIED",
        "REASONING_ENGINE",
        "CLOUD_RUN_SERVICE",
        "GKE_WORKLOAD",
        "GCE_INSTANCE",
        "AGENT_TYPE_OTHER",
    ]
    assessment: GoogleCloudAiplatformV1beta1Assessment
    createTime: str
    latestAnalyzedTime: str
    location: str
    name: str
    sessionId: str
    sessionState: typing.Literal[
        "SESSION_STATE_UNSPECIFIED",
        "SESSION_STATE_UNANALYZED",
        "SESSION_STATE_NOT_FLAGGED",
        "SESSION_STATE_FLAGGED",
        "SESSION_STATE_LLM_UNFLAGGED",
    ]
    severities: dict[str, typing.Any]
    userId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AnalyzedSessionSeveritySummary(
    typing.TypedDict, total=False
):
    detectorIds: _list[str]
    sessionsCount: int
    severityLevel: typing.Literal[
        "SEVERITY_UNSPECIFIED",
        "SEVERITY_LOW",
        "SEVERITY_MEDIUM",
        "SEVERITY_HIGH",
        "SEVERITY_CRITICAL",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Annotation(typing.TypedDict, total=False):
    annotationSource: GoogleCloudAiplatformV1beta1UserActionReference
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    payloadSchemaUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AnnotationSpec(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ApiAuth(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1beta1ApiAuthApiKeyConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ApiAuthApiKeyConfig(typing.TypedDict, total=False):
    apiKeySecretVersion: str
    apiKeyString: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AppendA2aTaskEventsRequest(
    typing.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1beta1A2aTaskEvent]
    generation: str
    taskEvents: _list[GoogleCloudAiplatformV1beta1TaskEvent]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AppendA2aTaskEventsResponse(
    typing.TypedDict, total=False
):
    generation: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AppendEventResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Artifact(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1ArtifactTypeSchema(typing.TypedDict, total=False):
    instanceSchema: str
    schemaTitle: str
    schemaUri: str
    schemaVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AskContextsRequest(typing.TypedDict, total=False):
    query: GoogleCloudAiplatformV1beta1RagQuery
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AskContextsResponse(typing.TypedDict, total=False):
    contexts: GoogleCloudAiplatformV1beta1RagContexts
    response: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssembleDataRequest(typing.TypedDict, total=False):
    geminiRequestReadConfig: GoogleCloudAiplatformV1beta1GeminiRequestReadConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssessDataRequest(typing.TypedDict, total=False):
    batchPredictionResourceUsageAssessmentConfig: GoogleCloudAiplatformV1beta1AssessDataRequestBatchPredictionResourceUsageAssessmentConfig
    batchPredictionValidationAssessmentConfig: GoogleCloudAiplatformV1beta1AssessDataRequestBatchPredictionValidationAssessmentConfig
    geminiRequestReadConfig: GoogleCloudAiplatformV1beta1GeminiRequestReadConfig
    tuningResourceUsageAssessmentConfig: (
        GoogleCloudAiplatformV1beta1AssessDataRequestTuningResourceUsageAssessmentConfig
    )
    tuningValidationAssessmentConfig: (
        GoogleCloudAiplatformV1beta1AssessDataRequestTuningValidationAssessmentConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssessDataRequestBatchPredictionResourceUsageAssessmentConfig(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssessDataRequestBatchPredictionValidationAssessmentConfig(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssessDataRequestTuningResourceUsageAssessmentConfig(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssessDataRequestTuningValidationAssessmentConfig(
    typing.TypedDict, total=False
):
    datasetUsage: typing.Literal[
        "DATASET_USAGE_UNSPECIFIED", "SFT_TRAINING", "SFT_VALIDATION"
    ]
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Assessment(typing.TypedDict, total=False):
    detectorFindings: _list[GoogleCloudAiplatformV1beta1AssessmentDetectorFinding]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssessmentDetectorFinding(
    typing.TypedDict, total=False
):
    detectorId: str
    displayName: str
    explanation: str
    probability: float
    recommendations: _list[str]
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED",
        "SEVERITY_LOW",
        "SEVERITY_MEDIUM",
        "SEVERITY_HIGH",
        "SEVERITY_CRITICAL",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssignNotebookRuntimeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssignNotebookRuntimeRequest(
    typing.TypedDict, total=False
):
    notebookRuntime: GoogleCloudAiplatformV1beta1NotebookRuntime
    notebookRuntimeId: str
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AsyncQueryReasoningEngineRequest(
    typing.TypedDict, total=False
):
    inputGcsUri: str
    outputGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AsyncRetrieveContextsRequest(
    typing.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1beta1RagQuery
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Attribution(typing.TypedDict, total=False):
    approximationError: float
    baselineOutputValue: float
    featureAttributions: typing.Any
    instanceOutputValue: float
    outputDisplayName: str
    outputIndex: _list[int]
    outputName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AudioResponseFormat(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1AudioTranscription(typing.TypedDict, total=False):
    speakerLabel: str
    text: str
    words: _list[GoogleCloudAiplatformV1beta1AudioTranscriptionWordInfo]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AudioTranscriptionConfig(
    typing.TypedDict, total=False
):
    adaptationPhrases: _list[str]
    customVocabulary: _list[str]
    diarization: bool
    languageAuto: GoogleCloudAiplatformV1beta1AudioTranscriptionConfigLanguageAuto
    languageCodes: _list[str]
    languageHints: GoogleCloudAiplatformV1beta1AudioTranscriptionConfigLanguageHints
    wordTimestamp: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AudioTranscriptionConfigLanguageAuto(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AudioTranscriptionConfigLanguageHints(
    typing.TypedDict, total=False
):
    languageCodes: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AudioTranscriptionWordInfo(
    typing.TypedDict, total=False
):
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AugmentPromptRequest(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    model: GoogleCloudAiplatformV1beta1AugmentPromptRequestModel
    vertexRagStore: GoogleCloudAiplatformV1beta1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AugmentPromptRequestModel(
    typing.TypedDict, total=False
):
    model: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AugmentPromptResponse(typing.TypedDict, total=False):
    augmentedPrompt: _list[GoogleCloudAiplatformV1beta1Content]
    facts: _list[GoogleCloudAiplatformV1beta1Fact]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AuthConfig(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1beta1AuthConfigApiKeyConfig
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
        GoogleCloudAiplatformV1beta1AuthConfigGoogleServiceAccountConfig
    )
    httpBasicAuthConfig: GoogleCloudAiplatformV1beta1AuthConfigHttpBasicAuthConfig
    oauthConfig: GoogleCloudAiplatformV1beta1AuthConfigOauthConfig
    oidcConfig: GoogleCloudAiplatformV1beta1AuthConfigOidcConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AuthConfigApiKeyConfig(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1AuthConfigGoogleServiceAccountConfig(
    typing.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AuthConfigHttpBasicAuthConfig(
    typing.TypedDict, total=False
):
    credentialSecret: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AuthConfigOauthConfig(typing.TypedDict, total=False):
    accessToken: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AuthConfigOidcConfig(typing.TypedDict, total=False):
    idToken: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AutomaticResources(typing.TypedDict, total=False):
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AutoraterConfig(typing.TypedDict, total=False):
    autoraterModel: str
    flipEnabled: bool
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    samplingCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AutoscalingMetricSpec(typing.TypedDict, total=False):
    metricName: str
    monitoredResourceLabels: dict[str, typing.Any]
    target: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AvroSource(typing.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCancelPipelineJobsRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCancelPipelineJobsResponse(
    typing.TypedDict, total=False
):
    pipelineJobs: _list[GoogleCloudAiplatformV1beta1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateFeatureRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesResponse(
    typing.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1beta1Feature]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateRagDataSchemasRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateRagDataSchemaRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateRagMetadataRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateRagMetadataRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateTensorboardRunRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsResponse(
    typing.TypedDict, total=False
):
    tensorboardRuns: _list[GoogleCloudAiplatformV1beta1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateTensorboardTimeSeriesRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesResponse(
    typing.TypedDict, total=False
):
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1beta1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDedicatedResources(
    typing.TypedDict, total=False
):
    flexStart: GoogleCloudAiplatformV1beta1FlexStart
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    maxReplicaCount: int
    spot: bool
    startingReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDeletePipelineJobsRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDeletePipelineJobsResponse(
    typing.TypedDict, total=False
):
    pipelineJobs: _list[GoogleCloudAiplatformV1beta1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDeleteRagDataSchemasRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDeleteRagMetadataRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsRequest(
    typing.TypedDict, total=False
):
    evaluatedAnnotations: _list[GoogleCloudAiplatformV1beta1EvaluatedAnnotation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsResponse(
    typing.TypedDict, total=False
):
    importedEvaluatedAnnotationsCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportModelEvaluationSlicesRequest(
    typing.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1beta1ModelEvaluationSlice]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportModelEvaluationSlicesResponse(
    typing.TypedDict, total=False
):
    importedModelEvaluationSlices: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    partialResults: _list[
        GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadataPartialResult
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadataPartialResult(
    typing.TypedDict, total=False
):
    dataset: str
    error: GoogleRpcStatus
    model: str
    request: GoogleCloudAiplatformV1beta1MigrateResourceRequest

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesRequest(
    typing.TypedDict, total=False
):
    migrateResourceRequests: _list[GoogleCloudAiplatformV1beta1MigrateResourceRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesResponse(
    typing.TypedDict, total=False
):
    migrateResourceResponses: _list[GoogleCloudAiplatformV1beta1MigrateResourceResponse]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJob(typing.TypedDict, total=False):
    completionStats: GoogleCloudAiplatformV1beta1CompletionStats
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1BatchDedicatedResources
    disableContainerLogging: bool
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    endpoint: str
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
    unmanagedContainerModel: GoogleCloudAiplatformV1beta1UnmanagedContainerModel
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    instancesFormat: str
    vertexMultimodalDatasetSource: (
        GoogleCloudAiplatformV1beta1VertexMultimodalDatasetSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobInstanceConfig(
    typing.TypedDict, total=False
):
    excludedFields: _list[str]
    includedFields: _list[str]
    instanceType: str
    keyField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobOutputConfig(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination
    predictionsFormat: str
    vertexMultimodalDatasetDestination: (
        GoogleCloudAiplatformV1beta1VertexMultimodalDatasetDestination
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobOutputInfo(
    typing.TypedDict, total=False
):
    bigqueryOutputDataset: str
    bigqueryOutputTable: str
    gcsOutputDirectory: str
    vertexMultimodalDatasetName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequest(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    entityTypeId: str
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    settings: _list[GoogleCloudAiplatformV1beta1DestinationFeatureSetting]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestPassThroughField(
    typing.TypedDict, total=False
):
    fieldName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadTensorboardTimeSeriesDataResponse(
    typing.TypedDict, total=False
):
    timeSeriesData: _list[GoogleCloudAiplatformV1beta1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQueryDestination(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQueryRequestSet(typing.TypedDict, total=False):
    candidateResponseColumns: dict[str, typing.Any]
    promptColumn: str
    rubricsColumn: str
    samplingConfig: GoogleCloudAiplatformV1beta1BigQueryRequestSetSamplingConfig
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQueryRequestSetSamplingConfig(
    typing.TypedDict, total=False
):
    samplingCount: int
    samplingDuration: str
    samplingMethod: typing.Literal["SAMPLING_METHOD_UNSPECIFIED", "RANDOM"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQuerySource(typing.TypedDict, total=False):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BleuInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1beta1BleuInstance]
    metricSpec: GoogleCloudAiplatformV1beta1BleuSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BleuInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BleuMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BleuResults(typing.TypedDict, total=False):
    bleuMetricValues: _list[GoogleCloudAiplatformV1beta1BleuMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BleuSpec(typing.TypedDict, total=False):
    useEffectiveOrder: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Blob(typing.TypedDict, total=False):
    data: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BlurBaselineConfig(typing.TypedDict, total=False):
    maxBlurSigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BoolArray(typing.TypedDict, total=False):
    values: _list[bool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CacheConfig(typing.TypedDict, total=False):
    disableCache: bool
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CachedContent(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    expireTime: str
    model: str
    name: str
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    toolConfig: GoogleCloudAiplatformV1beta1ToolConfig
    tools: _list[GoogleCloudAiplatformV1beta1Tool]
    ttl: str
    updateTime: str
    usageMetadata: GoogleCloudAiplatformV1beta1CachedContentUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CachedContentUsageMetadata(
    typing.TypedDict, total=False
):
    audioDurationSeconds: int
    imageCount: int
    textCount: int
    totalTokenCount: int
    videoDurationSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelAsyncQueryReasoningEngineRequest(
    typing.TypedDict, total=False
):
    operationName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelAsyncQueryReasoningEngineResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelBatchPredictionJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelCustomJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelDataLabelingJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelEvaluationRunRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelHyperparameterTuningJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelNasJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelPipelineJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelTrainingPipelineRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelTuningJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Candidate(typing.TypedDict, total=False):
    avgLogprobs: float
    citationMetadata: GoogleCloudAiplatformV1beta1CitationMetadata
    content: GoogleCloudAiplatformV1beta1Content
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
    groundingMetadata: GoogleCloudAiplatformV1beta1GroundingMetadata
    index: int
    logprobsResult: GoogleCloudAiplatformV1beta1LogprobsResult
    safetyRatings: _list[GoogleCloudAiplatformV1beta1SafetyRating]
    urlContextMetadata: GoogleCloudAiplatformV1beta1UrlContextMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CandidateResponse(typing.TypedDict, total=False):
    agentData: GoogleCloudAiplatformV1beta1AgentData
    candidate: str
    error: GoogleRpcStatus
    events: _list[GoogleCloudAiplatformV1beta1Content]
    text: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CandidateResult(typing.TypedDict, total=False):
    additionalResults: typing.Any
    candidate: str
    error: GoogleRpcStatus
    explanation: str
    metric: str
    rubricVerdicts: _list[GoogleCloudAiplatformV1beta1RubricVerdict]
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckPublisherModelEulaAcceptanceRequest(
    typing.TypedDict, total=False
):
    publisherModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckSignUpEligibilityResponse(
    typing.TypedDict, total=False
):
    eligibility: typing.Literal[
        "ELIGIBILITY_STATUS_UNSPECIFIED", "ELIGIBLE", "IN_SCOPE", "INELIGIBLE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateMetatdata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    study: str
    trial: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateResponse(
    typing.TypedDict, total=False
):
    shouldStop: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Checkpoint(typing.TypedDict, total=False):
    checkpointId: str
    epoch: str
    step: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Chunk(typing.TypedDict, total=False):
    data: str
    metadata: GoogleCloudAiplatformV1beta1Metadata
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Citation(typing.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: GoogleTypeDate
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CitationMetadata(typing.TypedDict, total=False):
    citations: _list[GoogleCloudAiplatformV1beta1Citation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Claim(typing.TypedDict, total=False):
    endIndex: int
    factIndexes: _list[int]
    score: float
    startIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ClientConnectionConfig(typing.TypedDict, total=False):
    inferenceTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CloudLoggingConfig(typing.TypedDict, total=False):
    project: str
    resourceLabels: dict[str, typing.Any]
    resourceType: str
    tracingContext: GoogleCloudAiplatformV1beta1CloudLoggingConfigTracingContext

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CloudLoggingConfigTracingContext(
    typing.TypedDict, total=False
):
    conversationId: str
    spanId: str
    traceId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CodeExecutionResult(typing.TypedDict, total=False):
    id: str
    outcome: typing.Literal[
        "OUTCOME_UNSPECIFIED",
        "OUTCOME_OK",
        "OUTCOME_FAILED",
        "OUTCOME_DEADLINE_EXCEEDED",
    ]
    output: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CoherenceInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1CoherenceInstance
    metricSpec: GoogleCloudAiplatformV1beta1CoherenceSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CoherenceInstance(typing.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CoherenceResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CoherenceSpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ColabImage(typing.TypedDict, total=False):
    description: str
    releaseName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CometInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1CometInstance
    metricSpec: GoogleCloudAiplatformV1beta1CometSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CometInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str
    source: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CometResult(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CometSpec(typing.TypedDict, total=False):
    sourceLanguage: str
    targetLanguage: str
    version: typing.Literal["COMET_VERSION_UNSPECIFIED", "COMET_22_SRC_REF"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompactSessionRequest(typing.TypedDict, total=False):
    compaction: GoogleCloudAiplatformV1beta1CompactionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompactionConfig(typing.TypedDict, total=False):
    eventEditing: GoogleCloudAiplatformV1beta1CompactionConfigEventEditingConfig
    summarization: GoogleCloudAiplatformV1beta1CompactionConfigLlmSummarizationConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompactionConfigEventEditingConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompactionConfigLlmSummarizationConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompleteTrialRequest(typing.TypedDict, total=False):
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
    infeasibleReason: str
    trialInfeasible: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompletionStats(typing.TypedDict, total=False):
    failedCount: str
    incompleteCount: str
    successfulCount: str
    successfulForecastPointCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompositeReinforcementTuningRewardConfig(
    typing.TypedDict, total=False
):
    weightedRewardConfigs: _list[
        GoogleCloudAiplatformV1beta1CompositeReinforcementTuningRewardConfigWeightedRewardConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompositeReinforcementTuningRewardConfigWeightedRewardConfig(
    typing.TypedDict, total=False
):
    rewardConfig: GoogleCloudAiplatformV1beta1SingleReinforcementTuningRewardConfig
    weight: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ComputationBasedMetricSpec(
    typing.TypedDict, total=False
):
    parameters: dict[str, typing.Any]
    type: typing.Literal[
        "COMPUTATION_BASED_METRIC_TYPE_UNSPECIFIED", "EXACT_MATCH", "BLEU", "ROUGE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ComputeTokensRequest(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    instances: _list[typing.Any]
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ComputeTokensResponse(typing.TypedDict, total=False):
    tokensInfo: _list[GoogleCloudAiplatformV1beta1TokensInfo]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContainerRegistryDestination(
    typing.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContainerSpec(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    imageUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Content(typing.TypedDict, total=False):
    parts: _list[GoogleCloudAiplatformV1beta1Part]
    role: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContentMap(typing.TypedDict, total=False):
    values: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContentMapContents(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1beta1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContentsExample(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    expectedContents: _list[GoogleCloudAiplatformV1beta1ContentsExampleExpectedContent]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContentsExampleExpectedContent(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1beta1Content

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Context(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1ConversationTurn(typing.TypedDict, total=False):
    events: _list[GoogleCloudAiplatformV1beta1AgentEvent]
    turnId: str
    turnIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelRequest(typing.TypedDict, total=False):
    customServiceAccount: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    modelId: str
    parentModel: str
    sourceModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelResponse(typing.TypedDict, total=False):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CorpusStatus(typing.TypedDict, total=False):
    errorStatus: str
    state: typing.Literal["UNKNOWN", "INITIALIZED", "ACTIVE", "ERROR"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CorroborateContentRequest(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1beta1Content
    facts: _list[GoogleCloudAiplatformV1beta1Fact]
    parameters: GoogleCloudAiplatformV1beta1CorroborateContentRequestParameters

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CorroborateContentRequestParameters(
    typing.TypedDict, total=False
):
    citationThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CorroborateContentResponse(
    typing.TypedDict, total=False
):
    claims: _list[GoogleCloudAiplatformV1beta1Claim]
    corroborationScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensRequest(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    instances: _list[typing.Any]
    model: str
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensResponse(typing.TypedDict, total=False):
    promptTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
    totalBillableCharacters: int
    totalTokens: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDatasetOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDatasetVersionOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolRequest(
    typing.TypedDict, total=False
):
    deploymentResourcePool: GoogleCloudAiplatformV1beta1DeploymentResourcePool
    deploymentResourcePoolId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateEndpointOperationMetadata(
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
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateEntityTypeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateExtensionControllerOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureGroupOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureOnlineStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureRequest(typing.TypedDict, total=False):
    feature: GoogleCloudAiplatformV1beta1Feature
    featureId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureViewOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeaturestoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateIndexEndpointOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateIndexOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: (
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateMetadataStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateModelMonitorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateModelMonitoringJobRequest(
    typing.TypedDict, total=False
):
    modelMonitoringJob: GoogleCloudAiplatformV1beta1ModelMonitoringJob
    modelMonitoringJobId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateNotebookExecutionJobOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateNotebookExecutionJobRequest(
    typing.TypedDict, total=False
):
    notebookExecutionJob: GoogleCloudAiplatformV1beta1NotebookExecutionJob
    notebookExecutionJobId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateNotebookRuntimeTemplateOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreatePersistentResourceOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreatePipelineJobRequest(
    typing.TypedDict, total=False
):
    parent: str
    pipelineJob: GoogleCloudAiplatformV1beta1PipelineJob
    pipelineJobId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateRagDataSchemaRequest(
    typing.TypedDict, total=False
):
    parent: str
    ragDataSchema: GoogleCloudAiplatformV1beta1RagDataSchema
    ragDataSchemaId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateRagMetadataRequest(
    typing.TypedDict, total=False
):
    parent: str
    ragMetadata: GoogleCloudAiplatformV1beta1RagMetadata
    ragMetadataId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateRegistryFeatureOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateServingProfileOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateSolverOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateSpecialistPoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardRunRequest(
    typing.TypedDict, total=False
):
    parent: str
    tensorboardRun: GoogleCloudAiplatformV1beta1TensorboardRun
    tensorboardRunId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardTimeSeriesRequest(
    typing.TypedDict, total=False
):
    parent: str
    tensorboardTimeSeries: GoogleCloudAiplatformV1beta1TensorboardTimeSeries
    tensorboardTimeSeriesId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CsvDestination(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CsvSource(typing.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomCodeExecutionResult(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomCodeExecutionSpec(
    typing.TypedDict, total=False
):
    codeExecutionRegion: str
    evaluationFunction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomJob(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec
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
class GoogleCloudAiplatformV1beta1CustomJobSpec(typing.TypedDict, total=False):
    baseOutputDirectory: GoogleCloudAiplatformV1beta1GcsDestination
    enableDashboardAccess: bool
    enableWebAccess: bool
    experiment: str
    experimentRun: str
    models: _list[str]
    network: str
    persistentResourceId: str
    protectedArtifactLocationId: str
    pscInterfaceConfig: GoogleCloudAiplatformV1beta1PscInterfaceConfig
    reservedIpRanges: _list[str]
    scheduling: GoogleCloudAiplatformV1beta1Scheduling
    serviceAccount: str
    tensorboard: str
    workerPoolSpecs: _list[GoogleCloudAiplatformV1beta1WorkerPoolSpec]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomOutput(typing.TypedDict, total=False):
    rawOutputs: GoogleCloudAiplatformV1beta1RawOutput

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomOutputFormatConfig(
    typing.TypedDict, total=False
):
    returnRawOutput: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataItem(typing.TypedDict, total=False):
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataItemView(typing.TypedDict, total=False):
    annotations: _list[GoogleCloudAiplatformV1beta1Annotation]
    dataItem: GoogleCloudAiplatformV1beta1DataItem
    hasTruncatedAnnotations: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataLabelingJob(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1Dataset(typing.TypedDict, total=False):
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
    modelReference: str
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    savedQueries: _list[GoogleCloudAiplatformV1beta1SavedQuery]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetCustomMetric(typing.TypedDict, total=False):
    aggregationFunction: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetDistribution(typing.TypedDict, total=False):
    buckets: _list[GoogleCloudAiplatformV1beta1DatasetDistributionDistributionBucket]
    max: float
    mean: float
    median: float
    min: float
    p5: float
    p95: float
    sum: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetDistributionDistributionBucket(
    typing.TypedDict, total=False
):
    count: str
    left: float
    right: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetStats(typing.TypedDict, total=False):
    contentsPerExampleDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution
    droppedExampleIndices: _list[str]
    droppedExampleReasons: _list[str]
    reinforcementTuningUserDatasetExamples: (
        GoogleCloudAiplatformV1beta1ReinforcementTuningUserDatasetExamples
    )
    totalBillableCharacterCount: str
    totalBillableTokenCount: str
    totalTuningCharacterCount: str
    tuningDatasetExampleCount: str
    tuningStepCount: str
    userDatasetExamples: _list[GoogleCloudAiplatformV1beta1Content]
    userInputTokenDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution
    userMessagePerExampleDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution
    userOutputTokenDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetVersion(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1DedicatedResources(typing.TypedDict, total=False):
    autoscalingMetricSpecs: _list[GoogleCloudAiplatformV1beta1AutoscalingMetricSpec]
    flexStart: GoogleCloudAiplatformV1beta1FlexStart
    initialReplicaCount: int
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    maxReplicaCount: int
    minReplicaCount: int
    requiredReplicaCount: int
    scaleToZeroSpec: GoogleCloudAiplatformV1beta1DedicatedResourcesScaleToZeroSpec
    spot: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DedicatedResourcesScaleToZeroSpec(
    typing.TypedDict, total=False
):
    idleScaledownPeriod: str
    minScaleupPeriod: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequest(
    typing.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectEntity
    selectTimeRangeAndFeature: (
        GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectEntity(
    typing.TypedDict, total=False
):
    entityIdSelector: GoogleCloudAiplatformV1beta1EntityIdSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature(
    typing.TypedDict, total=False
):
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    skipOnlineStorageDelete: bool
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponse(
    typing.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectEntity
    selectTimeRangeAndFeature: (
        GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectTimeRangeAndFeature
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectEntity(
    typing.TypedDict, total=False
):
    offlineStorageDeletedEntityRowCount: str
    onlineStorageDeletedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectTimeRangeAndFeature(
    typing.TypedDict, total=False
):
    impactedFeatureCount: str
    offlineStorageModifiedEntityRowCount: str
    onlineStorageModifiedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteMetadataStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteReasoningEngineRuntimeRevisionOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexOperationMetadata(
    typing.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexRequest(typing.TypedDict, total=False):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexResponse(typing.TypedDict, total=False):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelOperationMetadata(
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
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelRequest(typing.TypedDict, total=False):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelResponse(typing.TypedDict, total=False):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployPublisherModelRequest(
    typing.TypedDict, total=False
):
    acceptEula: bool
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    endpointDisplayName: str
    huggingFaceAccessToken: str
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployRequest(typing.TypedDict, total=False):
    customModel: GoogleCloudAiplatformV1beta1DeployRequestCustomModel
    deployConfig: GoogleCloudAiplatformV1beta1DeployRequestDeployConfig
    endpointConfig: GoogleCloudAiplatformV1beta1DeployRequestEndpointConfig
    huggingFaceModelId: str
    modelConfig: GoogleCloudAiplatformV1beta1DeployRequestModelConfig
    publisherModelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployRequestCustomModel(
    typing.TypedDict, total=False
):
    gcsUri: str
    modelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployRequestDeployConfig(
    typing.TypedDict, total=False
):
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    fastTryoutEnabled: bool
    systemLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployRequestEndpointConfig(
    typing.TypedDict, total=False
):
    dedicatedEndpointDisabled: bool
    dedicatedEndpointEnabled: bool
    endpointDisplayName: str
    endpointUserId: str
    labels: dict[str, typing.Any]
    privateServiceConnectConfig: GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployRequestModelConfig(
    typing.TypedDict, total=False
):
    acceptEula: bool
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    huggingFaceAccessToken: str
    huggingFaceCacheEnabled: bool
    modelDisplayName: str
    modelUserId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeploySolverOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndex(typing.TypedDict, total=False):
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    deployedIndexAuthConfig: GoogleCloudAiplatformV1beta1DeployedIndexAuthConfig
    deploymentGroup: str
    deploymentTier: typing.Literal["DEPLOYMENT_TIER_UNSPECIFIED", "STORAGE"]
    displayName: str
    enableAccessLogging: bool
    enableDatapointUpsertLogging: bool
    id: str
    index: str
    indexSyncTime: str
    privateEndpoints: GoogleCloudAiplatformV1beta1IndexPrivateEndpoints
    pscAutomationConfigs: _list[GoogleCloudAiplatformV1beta1PSCAutomationConfig]
    reservedIpRanges: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexAuthConfig(
    typing.TypedDict, total=False
):
    authProvider: GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProvider

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProvider(
    typing.TypedDict, total=False
):
    allowedIssuers: _list[str]
    audiences: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexRef(typing.TypedDict, total=False):
    deployedIndexId: str
    displayName: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedModel(typing.TypedDict, total=False):
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    checkpointId: str
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    disableContainerLogging: bool
    disableExplanations: bool
    displayName: str
    enableAccessLogging: bool
    enableContainerLogging: bool
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    fasterDeploymentConfig: GoogleCloudAiplatformV1beta1FasterDeploymentConfig
    fullFineTunedResources: GoogleCloudAiplatformV1beta1FullFineTunedResources
    gdcConnectedModel: str
    id: str
    model: str
    modelVersionId: str
    privateEndpoints: GoogleCloudAiplatformV1beta1PrivateEndpoints
    rolloutOptions: GoogleCloudAiplatformV1beta1RolloutOptions
    serviceAccount: str
    sharedResources: str
    speculativeDecodingSpec: GoogleCloudAiplatformV1beta1SpeculativeDecodingSpec
    status: GoogleCloudAiplatformV1beta1DeployedModelStatus
    systemLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedModelRef(typing.TypedDict, total=False):
    checkpointId: str
    deployedModelId: str
    endpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedModelStatus(typing.TypedDict, total=False):
    availableReplicaCount: int
    lastUpdateTime: str
    message: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeploymentResourcePool(typing.TypedDict, total=False):
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    disableContainerLogging: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeprovisionSemanticGovernancePolicyEngineRequest(
    typing.TypedDict, total=False
):
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DestinationFeatureSetting(
    typing.TypedDict, total=False
):
    destinationField: str
    featureId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectPredictRequest(typing.TypedDict, total=False):
    inputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectPredictResponse(typing.TypedDict, total=False):
    outputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectRawPredictRequest(
    typing.TypedDict, total=False
):
    input: str
    methodName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectRawPredictResponse(
    typing.TypedDict, total=False
):
    output: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectUploadSource(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DisableMonitoredAgentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DisableXmanagerOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progress: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DiskSpec(typing.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DistillationDataStats(typing.TypedDict, total=False):
    trainingDatasetStats: GoogleCloudAiplatformV1beta1DatasetStats

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DistillationHyperParameters(
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
    batchSize: str
    epochCount: str
    learningRate: float
    learningRateMultiplier: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DistillationSpec(typing.TypedDict, total=False):
    baseTeacherModel: str
    hyperParameters: GoogleCloudAiplatformV1beta1DistillationHyperParameters
    pipelineRootDirectory: str
    promptDatasetUri: str
    studentModel: str
    trainingDatasetUri: str
    tunedTeacherModelSource: str
    tuningMode: typing.Literal[
        "TUNING_MODE_UNSPECIFIED", "TUNING_MODE_FULL", "TUNING_MODE_PEFT_ADAPTER"
    ]
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DnsPeeringConfig(typing.TypedDict, total=False):
    domain: str
    targetNetwork: str
    targetProject: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DoubleArray(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DynamicRetrievalConfig(typing.TypedDict, total=False):
    dynamicThreshold: float
    mode: typing.Literal["MODE_UNSPECIFIED", "MODE_DYNAMIC"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EmbedContentRequest(typing.TypedDict, total=False):
    autoTruncate: bool
    content: GoogleCloudAiplatformV1beta1Content
    embedContentConfig: (
        GoogleCloudAiplatformV1beta1EmbedContentRequestEmbedContentConfig
    )
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
class GoogleCloudAiplatformV1beta1EmbedContentRequestEmbedContentConfig(
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
class GoogleCloudAiplatformV1beta1EmbedContentResponse(typing.TypedDict, total=False):
    embedding: GoogleCloudAiplatformV1beta1EmbedContentResponseEmbedding
    truncated: bool
    usageMetadata: GoogleCloudAiplatformV1beta1UsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EmbedContentResponseEmbedding(
    typing.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnableModelRequest(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnableModelResponse(typing.TypedDict, total=False):
    enablementState: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED",
        "ENABLEMENT_STATE_SUCCEEDED",
        "ENABLEMENT_STATE_FAILED",
    ]
    publisherEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnableMonitoredAgentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnableXmanagerOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progress: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EncryptionSpec(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Endpoint(typing.TypedDict, total=False):
    clientConnectionConfig: GoogleCloudAiplatformV1beta1ClientConnectionConfig
    createTime: str
    dedicatedEndpointDns: str
    dedicatedEndpointEnabled: bool
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModel]
    description: str
    displayName: str
    enablePrivateServiceConnect: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    gdcConfig: GoogleCloudAiplatformV1beta1GdcConfig
    genAiAdvancedFeaturesConfig: GoogleCloudAiplatformV1beta1GenAiAdvancedFeaturesConfig
    labels: dict[str, typing.Any]
    modelDeploymentMonitoringJob: str
    name: str
    network: str
    predictRequestResponseLoggingConfig: (
        GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfig
    )
    privateServiceConnectConfig: GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig
    publisherModelConfig: GoogleCloudAiplatformV1beta1PublisherModelConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    trafficSplit: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnterpriseWebSearch(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1EntityIdSelector(typing.TypedDict, total=False):
    csvSource: GoogleCloudAiplatformV1beta1CsvSource
    entityIdField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EntityType(typing.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    monitoringConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig
    name: str
    offlineStorageTtlDays: int
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnvVar(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotation(
    typing.TypedDict, total=False
):
    attributedItems: _list[
        GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem
    ]
    outlierScore: float
    outlierThreshold: float
    queryType: typing.Literal[
        "QUERY_TYPE_UNSPECIFIED",
        "ALL_SIMILAR",
        "SAME_CLASS_SIMILAR",
        "SAME_CLASS_DISSIMILAR",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem(
    typing.TypedDict, total=False
):
    annotationResourceName: str
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluateDatasetRequest(typing.TypedDict, total=False):
    autoraterConfig: GoogleCloudAiplatformV1beta1AutoraterConfig
    dataset: GoogleCloudAiplatformV1beta1EvaluationDataset
    location: str
    metrics: _list[GoogleCloudAiplatformV1beta1Metric]
    outputConfig: GoogleCloudAiplatformV1beta1OutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluateDatasetResponse(
    typing.TypedDict, total=False
):
    aggregationOutput: GoogleCloudAiplatformV1beta1AggregationOutput
    outputInfo: GoogleCloudAiplatformV1beta1OutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluateDatasetRun(typing.TypedDict, total=False):
    checkpointId: str
    error: GoogleRpcStatus
    evaluateDatasetResponse: GoogleCloudAiplatformV1beta1EvaluateDatasetResponse
    evaluationRun: str
    operationName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluateInstancesRequest(
    typing.TypedDict, total=False
):
    autoraterConfig: GoogleCloudAiplatformV1beta1AutoraterConfig
    bleuInput: GoogleCloudAiplatformV1beta1BleuInput
    coherenceInput: GoogleCloudAiplatformV1beta1CoherenceInput
    cometInput: GoogleCloudAiplatformV1beta1CometInput
    exactMatchInput: GoogleCloudAiplatformV1beta1ExactMatchInput
    fluencyInput: GoogleCloudAiplatformV1beta1FluencyInput
    fulfillmentInput: GoogleCloudAiplatformV1beta1FulfillmentInput
    groundednessInput: GoogleCloudAiplatformV1beta1GroundednessInput
    instance: GoogleCloudAiplatformV1beta1EvaluationInstance
    location: str
    metricSources: _list[GoogleCloudAiplatformV1beta1MetricSource]
    metrics: _list[GoogleCloudAiplatformV1beta1Metric]
    metricxInput: GoogleCloudAiplatformV1beta1MetricxInput
    pairwiseMetricInput: GoogleCloudAiplatformV1beta1PairwiseMetricInput
    pairwiseQuestionAnsweringQualityInput: (
        GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualityInput
    )
    pairwiseSummarizationQualityInput: (
        GoogleCloudAiplatformV1beta1PairwiseSummarizationQualityInput
    )
    pointwiseMetricInput: GoogleCloudAiplatformV1beta1PointwiseMetricInput
    questionAnsweringCorrectnessInput: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessInput
    )
    questionAnsweringHelpfulnessInput: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessInput
    )
    questionAnsweringQualityInput: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringQualityInput
    )
    questionAnsweringRelevanceInput: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceInput
    )
    rougeInput: GoogleCloudAiplatformV1beta1RougeInput
    rubricBasedInstructionFollowingInput: (
        GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingInput
    )
    safetyInput: GoogleCloudAiplatformV1beta1SafetyInput
    summarizationHelpfulnessInput: (
        GoogleCloudAiplatformV1beta1SummarizationHelpfulnessInput
    )
    summarizationQualityInput: GoogleCloudAiplatformV1beta1SummarizationQualityInput
    summarizationVerbosityInput: GoogleCloudAiplatformV1beta1SummarizationVerbosityInput
    toolCallValidInput: GoogleCloudAiplatformV1beta1ToolCallValidInput
    toolNameMatchInput: GoogleCloudAiplatformV1beta1ToolNameMatchInput
    toolParameterKeyMatchInput: GoogleCloudAiplatformV1beta1ToolParameterKeyMatchInput
    toolParameterKvMatchInput: GoogleCloudAiplatformV1beta1ToolParameterKVMatchInput
    trajectoryAnyOrderMatchInput: (
        GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchInput
    )
    trajectoryExactMatchInput: GoogleCloudAiplatformV1beta1TrajectoryExactMatchInput
    trajectoryInOrderMatchInput: GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchInput
    trajectoryPrecisionInput: GoogleCloudAiplatformV1beta1TrajectoryPrecisionInput
    trajectoryRecallInput: GoogleCloudAiplatformV1beta1TrajectoryRecallInput
    trajectorySingleToolUseInput: (
        GoogleCloudAiplatformV1beta1TrajectorySingleToolUseInput
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluateInstancesResponse(
    typing.TypedDict, total=False
):
    bleuResults: GoogleCloudAiplatformV1beta1BleuResults
    coherenceResult: GoogleCloudAiplatformV1beta1CoherenceResult
    cometResult: GoogleCloudAiplatformV1beta1CometResult
    exactMatchResults: GoogleCloudAiplatformV1beta1ExactMatchResults
    fluencyResult: GoogleCloudAiplatformV1beta1FluencyResult
    fulfillmentResult: GoogleCloudAiplatformV1beta1FulfillmentResult
    groundednessResult: GoogleCloudAiplatformV1beta1GroundednessResult
    metricResults: _list[GoogleCloudAiplatformV1beta1MetricResult]
    metricxResult: GoogleCloudAiplatformV1beta1MetricxResult
    pairwiseMetricResult: GoogleCloudAiplatformV1beta1PairwiseMetricResult
    pairwiseQuestionAnsweringQualityResult: (
        GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualityResult
    )
    pairwiseSummarizationQualityResult: (
        GoogleCloudAiplatformV1beta1PairwiseSummarizationQualityResult
    )
    pointwiseMetricResult: GoogleCloudAiplatformV1beta1PointwiseMetricResult
    questionAnsweringCorrectnessResult: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessResult
    )
    questionAnsweringHelpfulnessResult: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessResult
    )
    questionAnsweringQualityResult: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringQualityResult
    )
    questionAnsweringRelevanceResult: (
        GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceResult
    )
    rougeResults: GoogleCloudAiplatformV1beta1RougeResults
    rubricBasedInstructionFollowingResult: (
        GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingResult
    )
    safetyResult: GoogleCloudAiplatformV1beta1SafetyResult
    summarizationHelpfulnessResult: (
        GoogleCloudAiplatformV1beta1SummarizationHelpfulnessResult
    )
    summarizationQualityResult: GoogleCloudAiplatformV1beta1SummarizationQualityResult
    summarizationVerbosityResult: (
        GoogleCloudAiplatformV1beta1SummarizationVerbosityResult
    )
    toolCallValidResults: GoogleCloudAiplatformV1beta1ToolCallValidResults
    toolNameMatchResults: GoogleCloudAiplatformV1beta1ToolNameMatchResults
    toolParameterKeyMatchResults: (
        GoogleCloudAiplatformV1beta1ToolParameterKeyMatchResults
    )
    toolParameterKvMatchResults: GoogleCloudAiplatformV1beta1ToolParameterKVMatchResults
    trajectoryAnyOrderMatchResults: (
        GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchResults
    )
    trajectoryExactMatchResults: GoogleCloudAiplatformV1beta1TrajectoryExactMatchResults
    trajectoryInOrderMatchResults: (
        GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchResults
    )
    trajectoryPrecisionResults: GoogleCloudAiplatformV1beta1TrajectoryPrecisionResults
    trajectoryRecallResults: GoogleCloudAiplatformV1beta1TrajectoryRecallResults
    trajectorySingleToolUseResults: (
        GoogleCloudAiplatformV1beta1TrajectorySingleToolUseResults
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluatedAnnotation(typing.TypedDict, total=False):
    dataItemPayload: typing.Any
    errorAnalysisAnnotations: _list[GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotation]
    evaluatedDataItemViewId: str
    explanations: _list[GoogleCloudAiplatformV1beta1EvaluatedAnnotationExplanation]
    groundTruths: _list[typing.Any]
    predictions: _list[typing.Any]
    type: typing.Literal[
        "EVALUATED_ANNOTATION_TYPE_UNSPECIFIED",
        "TRUE_POSITIVE",
        "FALSE_POSITIVE",
        "FALSE_NEGATIVE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluatedAnnotationExplanation(
    typing.TypedDict, total=False
):
    explanation: GoogleCloudAiplatformV1beta1Explanation
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationConfig(typing.TypedDict, total=False):
    autoraterConfig: GoogleCloudAiplatformV1beta1AutoraterConfig
    datasetCustomMetrics: _list[GoogleCloudAiplatformV1beta1DatasetCustomMetric]
    inferenceGenerationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    metrics: _list[GoogleCloudAiplatformV1beta1Metric]
    outputConfig: GoogleCloudAiplatformV1beta1OutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationDataset(typing.TypedDict, total=False):
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstance(typing.TypedDict, total=False):
    agentData: GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentData
    agentEvalData: GoogleCloudAiplatformV1beta1AgentData
    interactionsDataSource: (
        GoogleCloudAiplatformV1beta1EvaluationInstanceInteractionsDataSource
    )
    otherData: GoogleCloudAiplatformV1beta1EvaluationInstanceMapInstance
    prompt: GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceData
    reference: GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceData
    response: GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceData
    rubricGroups: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentConfig(
    typing.TypedDict, total=False
):
    agentId: str
    agentType: str
    description: str
    developerInstruction: GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceData
    subAgents: _list[str]
    tools: GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentConfigTools
    toolsText: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentConfigTools(
    typing.TypedDict, total=False
):
    tool: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentData(
    typing.TypedDict, total=False
):
    agentConfig: GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentConfig
    agents: dict[str, typing.Any]
    developerInstruction: GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceData
    events: GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataEvents
    tools: GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataTools
    toolsText: str
    turns: _list[
        GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataConversationTurn
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataAgentEvent(
    typing.TypedDict, total=False
):
    activeTools: _list[GoogleCloudAiplatformV1beta1Tool]
    author: str
    content: GoogleCloudAiplatformV1beta1Content
    eventTime: str
    stateDelta: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataConversationTurn(
    typing.TypedDict, total=False
):
    events: _list[
        GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataAgentEvent
    ]
    turnId: str
    turnIndex: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataEvents(
    typing.TypedDict, total=False
):
    event: _list[GoogleCloudAiplatformV1beta1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentDataTools(
    typing.TypedDict, total=False
):
    tool: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceData(
    typing.TypedDict, total=False
):
    contents: GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceDataContents
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceInstanceDataContents(
    typing.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1beta1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceInteractionsDataSource(
    typing.TypedDict, total=False
):
    geminiAgentConfig: GoogleCloudAiplatformV1beta1GeminiAgentConfig
    interaction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationInstanceMapInstance(
    typing.TypedDict, total=False
):
    mapInstance: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationItem(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    error: GoogleRpcStatus
    evaluationItemType: typing.Literal[
        "EVALUATION_ITEM_TYPE_UNSPECIFIED", "REQUEST", "RESULT"
    ]
    evaluationRequest: GoogleCloudAiplatformV1beta1EvaluationRequest
    evaluationResponse: GoogleCloudAiplatformV1beta1EvaluationResult
    gcsUri: str
    labels: dict[str, typing.Any]
    metadata: typing.Any
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationMetric(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    gcsUri: str
    labels: dict[str, typing.Any]
    metric: GoogleCloudAiplatformV1beta1Metric
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationParserConfig(typing.TypedDict, total=False):
    customCodeParserConfig: (
        GoogleCloudAiplatformV1beta1EvaluationParserConfigCustomCodeParserConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationParserConfigCustomCodeParserConfig(
    typing.TypedDict, total=False
):
    codeExecutionRegion: str
    parsingFunction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationPrompt(typing.TypedDict, total=False):
    agentData: GoogleCloudAiplatformV1beta1AgentData
    promptTemplateData: GoogleCloudAiplatformV1beta1EvaluationPromptPromptTemplateData
    text: str
    userScenario: GoogleCloudAiplatformV1beta1EvaluationPromptUserScenario
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationPromptPromptTemplateData(
    typing.TypedDict, total=False
):
    values: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationPromptUserScenario(
    typing.TypedDict, total=False
):
    conversationPlan: str
    startingPrompt: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRequest(typing.TypedDict, total=False):
    candidateResponses: _list[GoogleCloudAiplatformV1beta1CandidateResponse]
    goldenResponse: GoogleCloudAiplatformV1beta1CandidateResponse
    prompt: GoogleCloudAiplatformV1beta1EvaluationPrompt
    rubrics: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationResult(typing.TypedDict, total=False):
    candidateResults: _list[GoogleCloudAiplatformV1beta1CandidateResult]
    evaluationRequest: str
    evaluationRun: str
    metadata: typing.Any
    metric: str
    request: GoogleCloudAiplatformV1beta1EvaluationRequest

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationResults(typing.TypedDict, total=False):
    evaluationSet: str
    lossAnalysisResults: _list[GoogleCloudAiplatformV1beta1LossAnalysisResult]
    summaryMetrics: GoogleCloudAiplatformV1beta1SummaryMetrics

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRubricConfig(typing.TypedDict, total=False):
    predefinedRubricGenerationSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricPredefinedMetricSpec
    )
    rubricGenerationSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricGenerationSpec
    )
    rubricGroupKey: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRun(typing.TypedDict, total=False):
    completionTime: str
    createTime: str
    dataSource: GoogleCloudAiplatformV1beta1EvaluationRunDataSource
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    error: GoogleRpcStatus
    evaluationConfig: GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfig
    evaluationResults: GoogleCloudAiplatformV1beta1EvaluationResults
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
class GoogleCloudAiplatformV1beta1EvaluationRunDataSource(
    typing.TypedDict, total=False
):
    bigqueryRequestSet: GoogleCloudAiplatformV1beta1BigQueryRequestSet
    evaluationSet: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfig(
    typing.TypedDict, total=False
):
    autoraterConfig: (
        GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigAutoraterConfig
    )
    cloudLoggingConfig: GoogleCloudAiplatformV1beta1CloudLoggingConfig
    datasetCustomMetrics: _list[GoogleCloudAiplatformV1beta1DatasetCustomMetric]
    lossAnalysisConfig: _list[GoogleCloudAiplatformV1beta1LossAnalysisConfig]
    metrics: _list[GoogleCloudAiplatformV1beta1EvaluationRunMetric]
    outputConfig: GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigOutputConfig
    promptTemplate: (
        GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigPromptTemplate
    )
    rubricConfigs: _list[GoogleCloudAiplatformV1beta1EvaluationRubricConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigAutoraterConfig(
    typing.TypedDict, total=False
):
    autoraterModel: str
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    sampleCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigOutputConfig(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigPromptTemplate(
    typing.TypedDict, total=False
):
    gcsUri: str
    promptTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfig(
    typing.TypedDict, total=False
):
    agentConfig: (
        GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigInferenceAgentConfig
    )
    agentRunConfig: (
        GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigAgentRunConfig
    )
    agents: dict[str, typing.Any]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    model: str
    parallelism: int
    promptTemplate: (
        GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigPromptTemplate
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigAgentRunConfig(
    typing.TypedDict, total=False
):
    agentEngine: str
    geminiAgentConfig: GoogleCloudAiplatformV1beta1GeminiAgentConfig
    sessionInput: GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigSessionInput
    userSimulatorConfig: GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigAgentRunConfigUserSimulatorConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigAgentRunConfigUserSimulatorConfig(
    typing.TypedDict, total=False
):
    maxTurn: int
    modelConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigInferenceAgentConfig(
    typing.TypedDict, total=False
):
    developerInstruction: GoogleCloudAiplatformV1beta1Content
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunInferenceConfigSessionInput(
    typing.TypedDict, total=False
):
    parameters: dict[str, typing.Any]
    sessionState: dict[str, typing.Any]
    userId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunMetric(typing.TypedDict, total=False):
    computationBasedMetricSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricComputationBasedMetricSpec
    )
    llmBasedMetricSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricLLMBasedMetricSpec
    )
    metric: str
    metricConfig: GoogleCloudAiplatformV1beta1Metric
    metricResourceName: str
    predefinedMetricSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricPredefinedMetricSpec
    )
    rubricBasedMetricSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricBasedMetricSpec
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunMetricComputationBasedMetricSpec(
    typing.TypedDict, total=False
):
    parameters: dict[str, typing.Any]
    type: typing.Literal[
        "COMPUTATION_BASED_METRIC_TYPE_UNSPECIFIED", "EXACT_MATCH", "BLEU", "ROUGE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunMetricLLMBasedMetricSpec(
    typing.TypedDict, total=False
):
    additionalConfig: dict[str, typing.Any]
    judgeAutoraterConfig: (
        GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigAutoraterConfig
    )
    metricPromptTemplate: str
    predefinedRubricGenerationSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricPredefinedMetricSpec
    )
    rubricGenerationSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricGenerationSpec
    )
    rubricGroupKey: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunMetricPredefinedMetricSpec(
    typing.TypedDict, total=False
):
    metricSpecName: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricBasedMetricSpec(
    typing.TypedDict, total=False
):
    inlineRubrics: GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricBasedMetricSpecRepeatedRubrics
    judgeAutoraterConfig: (
        GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigAutoraterConfig
    )
    metricPromptTemplate: str
    rubricGenerationSpec: (
        GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricGenerationSpec
    )
    rubricGroupKey: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricBasedMetricSpecRepeatedRubrics(
    typing.TypedDict, total=False
):
    rubrics: _list[GoogleCloudAiplatformV1beta1Rubric]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationRunMetricRubricGenerationSpec(
    typing.TypedDict, total=False
):
    metricResourceName: str
    modelConfig: (
        GoogleCloudAiplatformV1beta1EvaluationRunEvaluationConfigAutoraterConfig
    )
    promptTemplate: str
    rubricContentType: typing.Literal[
        "RUBRIC_CONTENT_TYPE_UNSPECIFIED",
        "PROPERTY",
        "NL_QUESTION_ANSWER",
        "PYTHON_CODE_ASSERTION",
    ]
    rubricTypeOntology: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluationSet(typing.TypedDict, total=False):
    agentConfigs: dict[str, typing.Any]
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    evaluationItems: _list[str]
    metadata: typing.Any
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Event(typing.TypedDict, total=False):
    artifact: str
    eventTime: str
    execution: str
    labels: dict[str, typing.Any]
    type: typing.Literal["TYPE_UNSPECIFIED", "INPUT", "OUTPUT"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EventActions(typing.TypedDict, total=False):
    artifactDelta: dict[str, typing.Any]
    escalate: bool
    requestedAuthConfigs: dict[str, typing.Any]
    skipSummarization: bool
    stateDelta: dict[str, typing.Any]
    transferAgent: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EventMetadata(typing.TypedDict, total=False):
    branch: str
    customMetadata: dict[str, typing.Any]
    groundingMetadata: GoogleCloudAiplatformV1beta1GroundingMetadata
    inputTranscription: GoogleCloudAiplatformV1beta1Transcription
    interrupted: bool
    longRunningToolIds: _list[str]
    outputTranscription: GoogleCloudAiplatformV1beta1Transcription
    partial: bool
    turnComplete: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExactMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1beta1ExactMatchInstance]
    metricSpec: GoogleCloudAiplatformV1beta1ExactMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExactMatchInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExactMatchMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExactMatchResults(typing.TypedDict, total=False):
    exactMatchMetricValues: _list[GoogleCloudAiplatformV1beta1ExactMatchMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExactMatchSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Example(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    exampleId: str
    storedContentsExample: GoogleCloudAiplatformV1beta1StoredContentsExample

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExampleStore(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    exampleStoreConfig: GoogleCloudAiplatformV1beta1ExampleStoreConfig
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExampleStoreConfig(typing.TypedDict, total=False):
    vertexEmbeddingModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Examples(typing.TypedDict, total=False):
    exampleGcsSource: GoogleCloudAiplatformV1beta1ExamplesExampleGcsSource
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    nearestNeighborSearchConfig: typing.Any
    neighborCount: int
    presets: GoogleCloudAiplatformV1beta1Presets

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesArrayFilter(typing.TypedDict, total=False):
    arrayOperator: typing.Literal[
        "ARRAY_OPERATOR_UNSPECIFIED", "CONTAINS_ANY", "CONTAINS_ALL"
    ]
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesExampleGcsSource(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "JSONL"]
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesOverride(typing.TypedDict, total=False):
    crowdingCount: int
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "INSTANCES", "EMBEDDINGS"]
    neighborCount: int
    restrictions: _list[GoogleCloudAiplatformV1beta1ExamplesRestrictionsNamespace]
    returnEmbeddings: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesRestrictionsNamespace(
    typing.TypedDict, total=False
):
    allow: _list[str]
    deny: _list[str]
    namespaceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecutableCode(typing.TypedDict, total=False):
    code: str
    id: str
    language: typing.Literal["LANGUAGE_UNSPECIFIED", "PYTHON"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecuteCodeRequest(typing.TypedDict, total=False):
    inputs: _list[GoogleCloudAiplatformV1beta1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecuteCodeResponse(typing.TypedDict, total=False):
    outputs: _list[GoogleCloudAiplatformV1beta1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecuteExtensionRequest(
    typing.TypedDict, total=False
):
    operationId: str
    operationParams: dict[str, typing.Any]
    runtimeAuthConfig: GoogleCloudAiplatformV1beta1AuthConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecuteExtensionResponse(
    typing.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecuteSandboxEnvironmentRequest(
    typing.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1beta1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecuteSandboxEnvironmentResponse(
    typing.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1beta1Chunk]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Execution(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1ExplainRequest(typing.TypedDict, total=False):
    concurrentExplanationSpecOverride: dict[str, typing.Any]
    deployedModelId: str
    explanationSpecOverride: GoogleCloudAiplatformV1beta1ExplanationSpecOverride
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainResponse(typing.TypedDict, total=False):
    concurrentExplanations: dict[str, typing.Any]
    deployedModelId: str
    explanations: _list[GoogleCloudAiplatformV1beta1Explanation]
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainResponseConcurrentExplanation(
    typing.TypedDict, total=False
):
    explanations: _list[GoogleCloudAiplatformV1beta1Explanation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Explanation(typing.TypedDict, total=False):
    attributions: _list[GoogleCloudAiplatformV1beta1Attribution]
    neighbors: _list[GoogleCloudAiplatformV1beta1Neighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadata(typing.TypedDict, total=False):
    featureAttributionsSchemaUri: str
    inputs: dict[str, typing.Any]
    latentSpaceSource: str
    outputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadata(
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
        GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomain
    )
    groupName: str
    indexFeatureMapping: _list[str]
    indicesTensorName: str
    inputBaselines: _list[typing.Any]
    inputTensorName: str
    modality: str
    visualization: (
        GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataVisualization
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomain(
    typing.TypedDict, total=False
):
    maxValue: float
    minValue: float
    originalMean: float
    originalStddev: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataVisualization(
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
class GoogleCloudAiplatformV1beta1ExplanationMetadataOutputMetadata(
    typing.TypedDict, total=False
):
    displayNameMappingKey: str
    indexDisplayNameMapping: typing.Any
    outputTensorName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOverride(
    typing.TypedDict, total=False
):
    inputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOverrideInputMetadataOverride(
    typing.TypedDict, total=False
):
    inputBaselines: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationParameters(typing.TypedDict, total=False):
    examples: GoogleCloudAiplatformV1beta1Examples
    integratedGradientsAttribution: (
        GoogleCloudAiplatformV1beta1IntegratedGradientsAttribution
    )
    outputIndices: _list[typing.Any]
    sampledShapleyAttribution: GoogleCloudAiplatformV1beta1SampledShapleyAttribution
    topK: int
    xraiAttribution: GoogleCloudAiplatformV1beta1XraiAttribution

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationSpec(typing.TypedDict, total=False):
    metadata: GoogleCloudAiplatformV1beta1ExplanationMetadata
    parameters: GoogleCloudAiplatformV1beta1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationSpecOverride(
    typing.TypedDict, total=False
):
    examplesOverride: GoogleCloudAiplatformV1beta1ExamplesOverride
    metadata: GoogleCloudAiplatformV1beta1ExplanationMetadataOverride
    parameters: GoogleCloudAiplatformV1beta1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataConfig(typing.TypedDict, total=False):
    annotationsFilter: str
    fractionSplit: GoogleCloudAiplatformV1beta1ExportFractionSplit
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataOperationMetadata(
    typing.TypedDict, total=False
):
    gcsOutputDirectory: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataRequest(typing.TypedDict, total=False):
    exportConfig: GoogleCloudAiplatformV1beta1ExportDataConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataResponse(typing.TypedDict, total=False):
    exportedFiles: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequest(
    typing.TypedDict, total=False
):
    destination: GoogleCloudAiplatformV1beta1FeatureValueDestination
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    fullExport: GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestFullExport
    settings: _list[GoogleCloudAiplatformV1beta1DestinationFeatureSetting]
    snapshotExport: GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestSnapshotExport

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestFullExport(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestSnapshotExport(
    typing.TypedDict, total=False
):
    snapshotTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFractionSplit(typing.TypedDict, total=False):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    outputInfo: GoogleCloudAiplatformV1beta1ExportModelOperationMetadataOutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelOperationMetadataOutputInfo(
    typing.TypedDict, total=False
):
    artifactOutputUri: str
    imageOutputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelRequest(typing.TypedDict, total=False):
    outputConfig: GoogleCloudAiplatformV1beta1ExportModelRequestOutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelRequestOutputConfig(
    typing.TypedDict, total=False
):
    artifactDestination: GoogleCloudAiplatformV1beta1GcsDestination
    exportFormatId: str
    imageDestination: GoogleCloudAiplatformV1beta1ContainerRegistryDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportPublisherModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportPublisherModelRequest(
    typing.TypedDict, total=False
):
    destination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportPublisherModelResponse(
    typing.TypedDict, total=False
):
    destinationUri: str
    publisherModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataRequest(
    typing.TypedDict, total=False
):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    timeSeriesDataPoints: _list[GoogleCloudAiplatformV1beta1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExpressProject(typing.TypedDict, total=False):
    createTime: str
    defaultApiKey: str
    projectId: str
    projectNumber: str
    region: str
    tier: typing.Literal["TIER_UNSPECIFIED", "TIER_FREE", "TIER_PAID"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Extension(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    extensionOperations: _list[GoogleCloudAiplatformV1beta1ExtensionOperation]
    manifest: GoogleCloudAiplatformV1beta1ExtensionManifest
    name: str
    privateServiceConnectConfig: (
        GoogleCloudAiplatformV1beta1ExtensionPrivateServiceConnectConfig
    )
    runtimeConfig: GoogleCloudAiplatformV1beta1RuntimeConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    toolUseExamples: _list[GoogleCloudAiplatformV1beta1ToolUseExample]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExtensionManifest(typing.TypedDict, total=False):
    apiSpec: GoogleCloudAiplatformV1beta1ExtensionManifestApiSpec
    authConfig: GoogleCloudAiplatformV1beta1AuthConfig
    description: str
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExtensionManifestApiSpec(
    typing.TypedDict, total=False
):
    openApiGcsUri: str
    openApiYaml: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExtensionOperation(typing.TypedDict, total=False):
    functionDeclaration: GoogleCloudAiplatformV1beta1FunctionDeclaration
    operationId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExtensionPrivateServiceConnectConfig(
    typing.TypedDict, total=False
):
    serviceDirectory: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExternalApi(typing.TypedDict, total=False):
    apiAuth: GoogleCloudAiplatformV1beta1ApiAuth
    apiSpec: typing.Literal["API_SPEC_UNSPECIFIED", "SIMPLE_SEARCH", "ELASTIC_SEARCH"]
    authConfig: GoogleCloudAiplatformV1beta1AuthConfig
    elasticSearchParams: GoogleCloudAiplatformV1beta1ExternalApiElasticSearchParams
    endpoint: str
    simpleSearchParams: GoogleCloudAiplatformV1beta1ExternalApiSimpleSearchParams

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExternalApiElasticSearchParams(
    typing.TypedDict, total=False
):
    index: str
    numHits: int
    searchTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExternalApiSimpleSearchParams(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Fact(typing.TypedDict, total=False):
    chunk: GoogleCloudAiplatformV1beta1RagChunk
    query: str
    score: float
    summary: str
    title: str
    uri: str
    vectorDistance: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FailedRubric(typing.TypedDict, total=False):
    classificationRationale: str
    rubricId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FasterDeploymentConfig(typing.TypedDict, total=False):
    fastTryoutEnabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Feature(typing.TypedDict, total=False):
    createTime: str
    description: str
    disableMonitoring: bool
    etag: str
    featureStatsAndAnomaly: _list[GoogleCloudAiplatformV1beta1FeatureStatsAndAnomaly]
    labels: dict[str, typing.Any]
    monitoringConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig
    monitoringStats: _list[GoogleCloudAiplatformV1beta1FeatureStatsAnomaly]
    monitoringStatsAnomalies: _list[
        GoogleCloudAiplatformV1beta1FeatureMonitoringStatsAnomaly
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
class GoogleCloudAiplatformV1beta1FeatureGroup(typing.TypedDict, total=False):
    bigQuery: GoogleCloudAiplatformV1beta1FeatureGroupBigQuery
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
class GoogleCloudAiplatformV1beta1FeatureGroupBigQuery(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    dense: bool
    entityIdColumns: _list[str]
    staticDataSource: bool
    timeSeries: GoogleCloudAiplatformV1beta1FeatureGroupBigQueryTimeSeries

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureGroupBigQueryTimeSeries(
    typing.TypedDict, total=False
):
    timestampColumn: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitor(typing.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    featureSelectionConfig: GoogleCloudAiplatformV1beta1FeatureSelectionConfig
    labels: dict[str, typing.Any]
    name: str
    scheduleConfig: GoogleCloudAiplatformV1beta1ScheduleConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitorJob(typing.TypedDict, total=False):
    createTime: str
    description: str
    driftBaseFeatureMonitorJobId: str
    driftBaseSnapshotTime: str
    featureSelectionConfig: GoogleCloudAiplatformV1beta1FeatureSelectionConfig
    finalStatus: GoogleRpcStatus
    jobSummary: GoogleCloudAiplatformV1beta1FeatureMonitorJobJobSummary
    labels: dict[str, typing.Any]
    name: str
    triggerType: typing.Literal[
        "FEATURE_MONITOR_JOB_TRIGGER_UNSPECIFIED",
        "FEATURE_MONITOR_JOB_TRIGGER_PERIODIC",
        "FEATURE_MONITOR_JOB_TRIGGER_ON_DEMAND",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitorJobJobSummary(
    typing.TypedDict, total=False
):
    featureStatsAndAnomalies: _list[GoogleCloudAiplatformV1beta1FeatureStatsAndAnomaly]
    totalSlotMs: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitoringStatsAnomaly(
    typing.TypedDict, total=False
):
    featureStatsAnomaly: GoogleCloudAiplatformV1beta1FeatureStatsAnomaly
    objective: typing.Literal[
        "OBJECTIVE_UNSPECIFIED", "IMPORT_FEATURE_ANALYSIS", "SNAPSHOT_ANALYSIS"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureNoiseSigma(typing.TypedDict, total=False):
    noiseSigma: _list[GoogleCloudAiplatformV1beta1FeatureNoiseSigmaNoiseSigmaForFeature]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureNoiseSigmaNoiseSigmaForFeature(
    typing.TypedDict, total=False
):
    name: str
    sigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStore(typing.TypedDict, total=False):
    bigtable: GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtable
    createTime: str
    dedicatedServingEndpoint: (
        GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpoint
    )
    embeddingManagement: (
        GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagement
    )
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    optimized: GoogleCloudAiplatformV1beta1FeatureOnlineStoreOptimized
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtable(
    typing.TypedDict, total=False
):
    autoScaling: GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableAutoScaling
    bigtableMetadata: (
        GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableBigtableMetadata
    )
    enableDirectBigtableAccess: bool
    zone: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableAutoScaling(
    typing.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableBigtableMetadata(
    typing.TypedDict, total=False
):
    instanceId: str
    tableId: str
    tenantProjectId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpoint(
    typing.TypedDict, total=False
):
    privateServiceConnectConfig: GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig
    publicEndpointDomainName: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagement(
    typing.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreOptimized(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureSelectionConfig(typing.TypedDict, total=False):
    featureConfigs: _list[
        GoogleCloudAiplatformV1beta1FeatureSelectionConfigFeatureConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureSelectionConfigFeatureConfig(
    typing.TypedDict, total=False
):
    driftThreshold: float
    featureId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureSelector(typing.TypedDict, total=False):
    idMatcher: GoogleCloudAiplatformV1beta1IdMatcher

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureStatsAndAnomaly(typing.TypedDict, total=False):
    distributionDeviation: float
    driftDetected: bool
    driftDetectionThreshold: float
    featureId: str
    featureMonitorId: str
    featureMonitorJobId: str
    featureStats: typing.Any
    statsTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureStatsAnomaly(typing.TypedDict, total=False):
    anomalyDetectionThreshold: float
    anomalyUri: str
    distributionDeviation: float
    endTime: str
    score: float
    startTime: str
    statsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValue(typing.TypedDict, total=False):
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
    structValue: GoogleCloudAiplatformV1beta1StructValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueDestination(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    csvDestination: GoogleCloudAiplatformV1beta1CsvDestination
    tfrecordDestination: GoogleCloudAiplatformV1beta1TFRecordDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueList(typing.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1beta1FeatureValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueMetadata(typing.TypedDict, total=False):
    generateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureView(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudAiplatformV1beta1FeatureViewBigQuerySource
    bigtableMetadata: GoogleCloudAiplatformV1beta1FeatureViewBigtableMetadata
    createTime: str
    etag: str
    featureRegistrySource: GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySource
    indexConfig: GoogleCloudAiplatformV1beta1FeatureViewIndexConfig
    labels: dict[str, typing.Any]
    name: str
    optimizedConfig: GoogleCloudAiplatformV1beta1FeatureViewOptimizedConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceAccountEmail: str
    serviceAgentType: typing.Literal[
        "SERVICE_AGENT_TYPE_UNSPECIFIED",
        "SERVICE_AGENT_TYPE_PROJECT",
        "SERVICE_AGENT_TYPE_FEATURE_VIEW",
    ]
    syncConfig: GoogleCloudAiplatformV1beta1FeatureViewSyncConfig
    updateTime: str
    vectorSearchConfig: GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig
    vertexRagSource: GoogleCloudAiplatformV1beta1FeatureViewVertexRagSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewBigQuerySource(
    typing.TypedDict, total=False
):
    entityIdColumns: _list[str]
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewBigtableMetadata(
    typing.TypedDict, total=False
):
    readAppProfile: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDataKey(typing.TypedDict, total=False):
    compositeKey: GoogleCloudAiplatformV1beta1FeatureViewDataKeyCompositeKey
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDataKeyCompositeKey(
    typing.TypedDict, total=False
):
    parts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDirectWriteRequest(
    typing.TypedDict, total=False
):
    dataKeyAndFeatureValues: _list[
        GoogleCloudAiplatformV1beta1FeatureViewDirectWriteRequestDataKeyAndFeatureValues
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDirectWriteRequestDataKeyAndFeatureValues(
    typing.TypedDict, total=False
):
    dataKey: GoogleCloudAiplatformV1beta1FeatureViewDataKey
    features: _list[
        GoogleCloudAiplatformV1beta1FeatureViewDirectWriteRequestDataKeyAndFeatureValuesFeature
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDirectWriteRequestDataKeyAndFeatureValuesFeature(
    typing.TypedDict, total=False
):
    name: str
    value: GoogleCloudAiplatformV1beta1FeatureValue
    valueAndTimestamp: GoogleCloudAiplatformV1beta1FeatureViewDirectWriteRequestDataKeyAndFeatureValuesFeatureFeatureValueAndTimestamp

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDirectWriteRequestDataKeyAndFeatureValuesFeatureFeatureValueAndTimestamp(
    typing.TypedDict, total=False
):
    timestamp: str
    value: GoogleCloudAiplatformV1beta1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDirectWriteResponse(
    typing.TypedDict, total=False
):
    status: GoogleRpcStatus
    writeResponses: _list[
        GoogleCloudAiplatformV1beta1FeatureViewDirectWriteResponseWriteResponse
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewDirectWriteResponseWriteResponse(
    typing.TypedDict, total=False
):
    dataKey: GoogleCloudAiplatformV1beta1FeatureViewDataKey
    onlineStoreWriteTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySource(
    typing.TypedDict, total=False
):
    featureGroups: _list[
        GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySourceFeatureGroup
    ]
    projectNumber: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySourceFeatureGroup(
    typing.TypedDict, total=False
):
    featureGroupId: str
    featureIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewIndexConfig(typing.TypedDict, total=False):
    bruteForceConfig: GoogleCloudAiplatformV1beta1FeatureViewIndexConfigBruteForceConfig
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
    treeAhConfig: GoogleCloudAiplatformV1beta1FeatureViewIndexConfigTreeAHConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewIndexConfigBruteForceConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewIndexConfigTreeAHConfig(
    typing.TypedDict, total=False
):
    leafNodeEmbeddingCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewOptimizedConfig(
    typing.TypedDict, total=False
):
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewSync(typing.TypedDict, total=False):
    createTime: str
    finalStatus: GoogleRpcStatus
    name: str
    runTime: GoogleTypeInterval
    satisfiesPzi: bool
    satisfiesPzs: bool
    syncSummary: GoogleCloudAiplatformV1beta1FeatureViewSyncSyncSummary

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewSyncConfig(typing.TypedDict, total=False):
    continuous: bool
    cron: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewSyncSyncSummary(
    typing.TypedDict, total=False
):
    rowSynced: str
    systemWatermarkTime: str
    totalSlot: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig(
    typing.TypedDict, total=False
):
    bruteForceConfig: (
        GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigBruteForceConfig
    )
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
    treeAhConfig: GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigBruteForceConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfigTreeAHConfig(
    typing.TypedDict, total=False
):
    leafNodeEmbeddingCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewVertexRagSource(
    typing.TypedDict, total=False
):
    ragCorpusId: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Featurestore(typing.TypedDict, total=False):
    createTime: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    onlineServingConfig: GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfig
    onlineStorageTtlDays: int
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig(
    typing.TypedDict, total=False
):
    categoricalThresholdConfig: (
        GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig
    )
    importFeaturesAnalysis: (
        GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigImportFeaturesAnalysis
    )
    numericalThresholdConfig: (
        GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig
    )
    snapshotAnalysis: (
        GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigSnapshotAnalysis
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigImportFeaturesAnalysis(
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
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigSnapshotAnalysis(
    typing.TypedDict, total=False
):
    disabled: bool
    monitoringInterval: str
    monitoringIntervalDays: int
    stalenessDays: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig(
    typing.TypedDict, total=False
):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfig(
    typing.TypedDict, total=False
):
    fixedNodeCount: int
    scaling: GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling(
    typing.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeedbackContext(typing.TypedDict, total=False):
    contextEvents: _list[GoogleCloudAiplatformV1beta1SessionEvent]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeedbackEntry(typing.TypedDict, total=False):
    createTime: str
    customMetadata: dict[str, typing.Any]
    eventId: str
    feedbackLabels: _list[str]
    feedbackText: str
    feedbackType: typing.Literal[
        "FEEDBACK_TYPE_UNSPECIFIED", "THUMBS_UP", "THUMBS_DOWN"
    ]
    name: str
    sessionId: str
    source: str
    updateTime: str
    userId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchExamplesRequest(typing.TypedDict, total=False):
    exampleIds: _list[str]
    pageSize: int
    pageToken: str
    storedContentsExampleFilter: GoogleCloudAiplatformV1beta1StoredContentsExampleFilter

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchExamplesResponse(typing.TypedDict, total=False):
    examples: _list[GoogleCloudAiplatformV1beta1Example]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesRequest(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal[
        "FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED", "KEY_VALUE", "PROTO_STRUCT"
    ]
    dataKey: GoogleCloudAiplatformV1beta1FeatureViewDataKey
    format: typing.Literal["FORMAT_UNSPECIFIED", "KEY_VALUE", "PROTO_STRUCT"]
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesResponse(
    typing.TypedDict, total=False
):
    dataKey: GoogleCloudAiplatformV1beta1FeatureViewDataKey
    keyValues: (
        GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairList
    )
    protoStruct: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairList(
    typing.TypedDict, total=False
):
    features: _list[
        GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseFeatureNameValuePairListFeatureNameValuePair(
    typing.TypedDict, total=False
):
    name: str
    value: GoogleCloudAiplatformV1beta1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchPredictOperationRequest(
    typing.TypedDict, total=False
):
    operationName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FileData(typing.TypedDict, total=False):
    displayName: str
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FileStatus(typing.TypedDict, total=False):
    errorStatus: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ERROR"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FilterSplit(typing.TypedDict, total=False):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsRequest(typing.TypedDict, total=False):
    deployedIndexId: str
    queries: _list[GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery]
    returnFullDatapoint: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery(
    typing.TypedDict, total=False
):
    approximateNeighborCount: int
    datapoint: GoogleCloudAiplatformV1beta1IndexDatapoint
    fractionLeafNodesToSearchOverride: float
    neighborCount: int
    perCrowdingAttributeNeighborCount: int
    rrf: GoogleCloudAiplatformV1beta1FindNeighborsRequestQueryRRF

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsRequestQueryRRF(
    typing.TypedDict, total=False
):
    alpha: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponse(typing.TypedDict, total=False):
    nearestNeighbors: _list[
        GoogleCloudAiplatformV1beta1FindNeighborsResponseNearestNeighbors
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponseNearestNeighbors(
    typing.TypedDict, total=False
):
    id: str
    neighbors: _list[GoogleCloudAiplatformV1beta1FindNeighborsResponseNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponseNeighbor(
    typing.TypedDict, total=False
):
    datapoint: GoogleCloudAiplatformV1beta1IndexDatapoint
    distance: float
    sparseDistance: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FlexStart(typing.TypedDict, total=False):
    maxRuntimeDuration: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FluencyInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1FluencyInstance
    metricSpec: GoogleCloudAiplatformV1beta1FluencySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FluencyInstance(typing.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FluencyResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FluencySpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FractionSplit(typing.TypedDict, total=False):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FulfillmentInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1FulfillmentInstance
    metricSpec: GoogleCloudAiplatformV1beta1FulfillmentSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FulfillmentInstance(typing.TypedDict, total=False):
    instruction: str
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FulfillmentResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FulfillmentSpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FullFineTunedResources(typing.TypedDict, total=False):
    deploymentType: typing.Literal[
        "DEPLOYMENT_TYPE_UNSPECIFIED", "DEPLOYMENT_TYPE_EVAL", "DEPLOYMENT_TYPE_PROD"
    ]
    modelInferenceUnitCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FullFineTuningSpec(typing.TypedDict, total=False):
    hyperParameters: GoogleCloudAiplatformV1beta1SupervisedHyperParameters
    trainingDatasetUri: str
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionCall(typing.TypedDict, total=False):
    args: dict[str, typing.Any]
    id: str
    name: str
    partialArgs: _list[GoogleCloudAiplatformV1beta1PartialArg]
    willContinue: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionCallingConfig(typing.TypedDict, total=False):
    allowedFunctionNames: _list[str]
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO", "ANY", "NONE", "VALIDATED"]
    streamFunctionCallArguments: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionDeclaration(typing.TypedDict, total=False):
    behavior: typing.Literal["UNSPECIFIED", "BLOCKING", "NON_BLOCKING"]
    description: str
    name: str
    parameters: GoogleCloudAiplatformV1beta1Schema
    parametersJsonSchema: typing.Any
    response: GoogleCloudAiplatformV1beta1Schema
    responseJsonSchema: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionResponse(typing.TypedDict, total=False):
    id: str
    name: str
    parts: _list[GoogleCloudAiplatformV1beta1FunctionResponsePart]
    response: dict[str, typing.Any]
    scheduling: typing.Literal[
        "SCHEDULING_UNSPECIFIED", "SILENT", "WHEN_IDLE", "INTERRUPT"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionResponseBlob(typing.TypedDict, total=False):
    data: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionResponseFileData(
    typing.TypedDict, total=False
):
    displayName: str
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionResponsePart(typing.TypedDict, total=False):
    fileData: GoogleCloudAiplatformV1beta1FunctionResponseFileData
    inlineData: GoogleCloudAiplatformV1beta1FunctionResponseBlob

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GatewayConfig(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1GcsDestination(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GcsSource(typing.TypedDict, total=False):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GdcConfig(typing.TypedDict, total=False):
    zone: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GeminiAgentConfig(typing.TypedDict, total=False):
    geminiAgent: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GeminiExample(typing.TypedDict, total=False):
    cachedContent: str
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    labels: dict[str, typing.Any]
    model: str
    modelArmorConfig: GoogleCloudAiplatformV1beta1ModelArmorConfig
    safetySettings: _list[GoogleCloudAiplatformV1beta1SafetySetting]
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    toolConfig: GoogleCloudAiplatformV1beta1ToolConfig
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GeminiPreferenceExample(
    typing.TypedDict, total=False
):
    completions: _list[GoogleCloudAiplatformV1beta1GeminiPreferenceExampleCompletion]
    contents: _list[GoogleCloudAiplatformV1beta1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GeminiPreferenceExampleCompletion(
    typing.TypedDict, total=False
):
    completion: GoogleCloudAiplatformV1beta1Content
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GeminiRequestReadConfig(
    typing.TypedDict, total=False
):
    assembledRequestColumnName: str
    templateConfig: GoogleCloudAiplatformV1beta1GeminiTemplateConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GeminiTemplateConfig(typing.TypedDict, total=False):
    fieldMapping: dict[str, typing.Any]
    geminiExample: GoogleCloudAiplatformV1beta1GeminiExample

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenAiAdvancedFeaturesConfig(
    typing.TypedDict, total=False
):
    ragConfig: GoogleCloudAiplatformV1beta1GenAiAdvancedFeaturesConfigRagConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenAiAdvancedFeaturesConfigRagConfig(
    typing.TypedDict, total=False
):
    enableRag: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateAccessTokenRequest(
    typing.TypedDict, total=False
):
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateAccessTokenResponse(
    typing.TypedDict, total=False
):
    accessToken: str
    expiresIn: int
    scope: str
    tokenType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentRequest(typing.TypedDict, total=False):
    cachedContent: str
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    labels: dict[str, typing.Any]
    modelArmorConfig: GoogleCloudAiplatformV1beta1ModelArmorConfig
    safetySettings: _list[GoogleCloudAiplatformV1beta1SafetySetting]
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    toolConfig: GoogleCloudAiplatformV1beta1ToolConfig
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponse(
    typing.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1beta1Candidate]
    createTime: str
    modelVersion: str
    promptFeedback: GoogleCloudAiplatformV1beta1GenerateContentResponsePromptFeedback
    responseId: str
    usageMetadata: GoogleCloudAiplatformV1beta1GenerateContentResponseUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponsePromptFeedback(
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
    safetyRatings: _list[GoogleCloudAiplatformV1beta1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponseUsageMetadata(
    typing.TypedDict, total=False
):
    cacheTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
    cachedContentTokenCount: int
    candidatesTokenCount: int
    candidatesTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
    promptTokenCount: int
    promptTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
    thoughtsTokenCount: int
    toolUsePromptTokenCount: int
    toolUsePromptTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
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
class GoogleCloudAiplatformV1beta1GenerateFetchAccessTokenRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateFetchAccessTokenResponse(
    typing.TypedDict, total=False
):
    accessToken: str
    expireTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateInstanceRubricsRequest(
    typing.TypedDict, total=False
):
    agentConfig: GoogleCloudAiplatformV1beta1EvaluationInstanceDeprecatedAgentConfig
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    location: str
    metricResourceName: str
    predefinedRubricGenerationSpec: GoogleCloudAiplatformV1beta1PredefinedMetricSpec
    rubricGenerationSpec: GoogleCloudAiplatformV1beta1RubricGenerationSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateInstanceRubricsResponse(
    typing.TypedDict, total=False
):
    generatedRubrics: _list[GoogleCloudAiplatformV1beta1Rubric]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateLossClustersOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateLossClustersRequest(
    typing.TypedDict, total=False
):
    configs: _list[GoogleCloudAiplatformV1beta1LossAnalysisConfig]
    evaluationSet: str
    inlineResults: (
        GoogleCloudAiplatformV1beta1GenerateLossClustersRequestEvaluationResultList
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateLossClustersRequestEvaluationResultList(
    typing.TypedDict, total=False
):
    evaluationResults: _list[GoogleCloudAiplatformV1beta1EvaluationResult]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateLossClustersResponse(
    typing.TypedDict, total=False
):
    analysisTime: str
    results: _list[GoogleCloudAiplatformV1beta1LossAnalysisResult]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateMemoriesRequest(
    typing.TypedDict, total=False
):
    allowedTopics: _list[GoogleCloudAiplatformV1beta1MemoryTopicId]
    directContentsSource: (
        GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectContentsSource
    )
    directMemoriesSource: (
        GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectMemoriesSource
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
        GoogleCloudAiplatformV1beta1GenerateMemoriesRequestVertexSessionSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectContentsSource(
    typing.TypedDict, total=False
):
    events: _list[
        GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectContentsSourceEvent
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectContentsSourceEvent(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1beta1Content

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectMemoriesSource(
    typing.TypedDict, total=False
):
    directMemories: _list[
        GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectMemoriesSourceDirectMemory
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateMemoriesRequestDirectMemoriesSourceDirectMemory(
    typing.TypedDict, total=False
):
    fact: str
    topics: _list[GoogleCloudAiplatformV1beta1MemoryTopicId]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateMemoriesRequestVertexSessionSource(
    typing.TypedDict, total=False
):
    endTime: str
    session: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateSyntheticDataRequest(
    typing.TypedDict, total=False
):
    count: int
    examples: _list[GoogleCloudAiplatformV1beta1SyntheticExample]
    outputFieldSpecs: _list[GoogleCloudAiplatformV1beta1OutputFieldSpec]
    taskDescription: GoogleCloudAiplatformV1beta1TaskDescriptionStrategy

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateSyntheticDataResponse(
    typing.TypedDict, total=False
):
    syntheticExamples: _list[GoogleCloudAiplatformV1beta1SyntheticExample]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateUserScenariosRequest(
    typing.TypedDict, total=False
):
    agents: dict[str, typing.Any]
    allowCrossRegionModel: bool
    geminiAgentConfig: GoogleCloudAiplatformV1beta1GeminiAgentConfig
    rootAgentId: str
    userScenarioGenerationConfig: (
        GoogleCloudAiplatformV1beta1UserScenarioGenerationConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateUserScenariosResponse(
    typing.TypedDict, total=False
):
    userScenarios: _list[GoogleCloudAiplatformV1beta1UserScenario]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateVideoResponse(typing.TypedDict, total=False):
    generatedSamples: _list[str]
    raiMediaFilteredCount: int
    raiMediaFilteredReasons: _list[str]
    videos: _list[GoogleCloudAiplatformV1beta1GenerateVideoResponseVideo]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateVideoResponseVideo(
    typing.TypedDict, total=False
):
    bytesBase64Encoded: str
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfig(typing.TypedDict, total=False):
    audioTimestamp: bool
    audioTranscriptionConfig: GoogleCloudAiplatformV1beta1AudioTranscriptionConfig
    candidateCount: int
    enableAffectiveDialog: bool
    frequencyPenalty: float
    imageConfig: GoogleCloudAiplatformV1beta1ImageConfig
    logprobs: int
    maxOutputTokens: int
    mediaResolution: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED",
        "MEDIA_RESOLUTION_LOW",
        "MEDIA_RESOLUTION_MEDIUM",
        "MEDIA_RESOLUTION_HIGH",
    ]
    modelConfig: GoogleCloudAiplatformV1beta1GenerationConfigModelConfig
    presencePenalty: float
    responseFormat: _list[GoogleCloudAiplatformV1beta1ResponseFormat]
    responseJsonSchema: typing.Any
    responseLogprobs: bool
    responseMimeType: str
    responseModalities: _list[
        typing.Literal["MODALITY_UNSPECIFIED", "TEXT", "IMAGE", "AUDIO", "VIDEO"]
    ]
    responseSchema: GoogleCloudAiplatformV1beta1Schema
    routingConfig: GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfig
    seed: int
    speechConfig: GoogleCloudAiplatformV1beta1SpeechConfig
    stopSequences: _list[str]
    temperature: float
    thinkingConfig: GoogleCloudAiplatformV1beta1GenerationConfigThinkingConfig
    topK: float
    topP: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigModelConfig(
    typing.TypedDict, total=False
):
    featureSelectionPreference: typing.Literal[
        "FEATURE_SELECTION_PREFERENCE_UNSPECIFIED",
        "PRIORITIZE_QUALITY",
        "BALANCED",
        "PRIORITIZE_COST",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfig(
    typing.TypedDict, total=False
):
    autoMode: GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigAutoRoutingMode
    manualMode: (
        GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigManualRoutingMode
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigAutoRoutingMode(
    typing.TypedDict, total=False
):
    modelRoutingPreference: typing.Literal[
        "UNKNOWN", "PRIORITIZE_QUALITY", "BALANCED", "PRIORITIZE_COST"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigManualRoutingMode(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigThinkingConfig(
    typing.TypedDict, total=False
):
    includeThoughts: bool
    thinkingBudget: int
    thinkingLevel: typing.Literal[
        "THINKING_LEVEL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "MINIMAL"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenericOperationMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    partialFailures: _list[GoogleRpcStatus]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenieSource(typing.TypedDict, total=False):
    baseModelUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleDriveSource(typing.TypedDict, total=False):
    resourceIds: _list[GoogleCloudAiplatformV1beta1GoogleDriveSourceResourceId]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleDriveSourceResourceId(
    typing.TypedDict, total=False
):
    resourceId: str
    resourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "RESOURCE_TYPE_FILE", "RESOURCE_TYPE_FOLDER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleMaps(typing.TypedDict, total=False):
    enableWidget: bool
    groundingTypes: GoogleCloudAiplatformV1beta1GoogleMapsGroundingTypes

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleMapsGroundingTypes(
    typing.TypedDict, total=False
):
    places: GoogleCloudAiplatformV1beta1GoogleMapsPlaces
    routing: GoogleCloudAiplatformV1beta1GoogleMapsRouting

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleMapsPlaces(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleMapsRouting(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleSearchRetrieval(typing.TypedDict, total=False):
    dynamicRetrievalConfig: GoogleCloudAiplatformV1beta1DynamicRetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundednessInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1GroundednessInstance
    metricSpec: GoogleCloudAiplatformV1beta1GroundednessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundednessInstance(typing.TypedDict, total=False):
    context: str
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundednessResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundednessSpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunk(typing.TypedDict, total=False):
    image: GoogleCloudAiplatformV1beta1GroundingChunkImage
    maps: GoogleCloudAiplatformV1beta1GroundingChunkMaps
    retrievedContext: GoogleCloudAiplatformV1beta1GroundingChunkRetrievedContext
    web: GoogleCloudAiplatformV1beta1GroundingChunkWeb

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkImage(typing.TypedDict, total=False):
    domain: str
    imageUri: str
    sourceUri: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkMaps(typing.TypedDict, total=False):
    placeAnswerSources: GoogleCloudAiplatformV1beta1GroundingChunkMapsPlaceAnswerSources
    placeId: str
    route: GoogleCloudAiplatformV1beta1GroundingChunkMapsRoute
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkMapsPlaceAnswerSources(
    typing.TypedDict, total=False
):
    reviewSnippets: _list[
        GoogleCloudAiplatformV1beta1GroundingChunkMapsPlaceAnswerSourcesReviewSnippet
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkMapsPlaceAnswerSourcesReviewSnippet(
    typing.TypedDict, total=False
):
    googleMapsUri: str
    reviewId: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkMapsRoute(
    typing.TypedDict, total=False
):
    distanceMeters: int
    duration: str
    encodedPolyline: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkRetrievedContext(
    typing.TypedDict, total=False
):
    documentName: str
    ragChunk: GoogleCloudAiplatformV1beta1RagChunk
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkWeb(typing.TypedDict, total=False):
    domain: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingMetadata(typing.TypedDict, total=False):
    googleMapsWidgetContextToken: str
    groundingChunks: _list[GoogleCloudAiplatformV1beta1GroundingChunk]
    groundingSupports: _list[GoogleCloudAiplatformV1beta1GroundingSupport]
    imageSearchQueries: _list[str]
    retrievalMetadata: GoogleCloudAiplatformV1beta1RetrievalMetadata
    retrievalQueries: _list[str]
    searchEntryPoint: GoogleCloudAiplatformV1beta1SearchEntryPoint
    sourceFlaggingUris: _list[
        GoogleCloudAiplatformV1beta1GroundingMetadataSourceFlaggingUri
    ]
    webSearchQueries: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingMetadataSourceFlaggingUri(
    typing.TypedDict, total=False
):
    flagContentUri: str
    sourceId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingSupport(typing.TypedDict, total=False):
    confidenceScores: _list[float]
    groundingChunkIndices: _list[int]
    renderedParts: _list[int]
    segment: GoogleCloudAiplatformV1beta1Segment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1HyperparameterTuningJob(
    typing.TypedDict, total=False
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
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec
    trials: _list[GoogleCloudAiplatformV1beta1Trial]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IdMatcher(typing.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImageConfig(typing.TypedDict, total=False):
    aspectRatio: str
    imageOutputOptions: GoogleCloudAiplatformV1beta1ImageConfigImageOutputOptions
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
class GoogleCloudAiplatformV1beta1ImageConfigImageOutputOptions(
    typing.TypedDict, total=False
):
    compressionQuality: int
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImageResponseFormat(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1ImportDataConfig(typing.TypedDict, total=False):
    annotationLabels: dict[str, typing.Any]
    dataItemLabels: dict[str, typing.Any]
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    importSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataRequest(typing.TypedDict, total=False):
    importConfigs: _list[GoogleCloudAiplatformV1beta1ImportDataConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportEvaluationSetRequest(
    typing.TypedDict, total=False
):
    agentEngineSource: (
        GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestAgentEngineSource
    )
    bigquerySource: GoogleCloudAiplatformV1beta1BigQueryRequestSet
    cloudTraceSource: (
        GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestCloudTraceSource
    )
    evaluationSet: GoogleCloudAiplatformV1beta1EvaluationSet
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination
    gcsSource: GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestGcsSource
    inlineSource: GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestInlineSource
    interactionsSource: (
        GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestInteractionsSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestAgentEngineSource(
    typing.TypedDict, total=False
):
    location: str
    projectId: str
    reasoningEngineId: str
    sessionIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestCloudTraceSource(
    typing.TypedDict, total=False
):
    projectId: str
    sessionIds: _list[str]
    traceIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestGcsSource(
    typing.TypedDict, total=False
):
    gcsUri: str
    importSchemaConfig: (
        GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestImportSchemaConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestImportSchemaConfig(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal[
        "DATA_FORMAT_UNSPECIFIED", "OTEL_PROTO", "OTEL_JSON", "JSONL"
    ]
    dataFormatVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestInlineSource(
    typing.TypedDict, total=False
):
    content: str
    importSchemaConfig: (
        GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestImportSchemaConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportEvaluationSetRequestInteractionsSource(
    typing.TypedDict, total=False
):
    geminiAgentConfig: GoogleCloudAiplatformV1beta1GeminiAgentConfig
    interactions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportExtensionOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesOperationMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    id: str
    sourceField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesResponse(
    typing.TypedDict, total=False
):
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportIndexRequest(typing.TypedDict, total=False):
    config: GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfig
    isCompleteOverwrite: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfig(
    typing.TypedDict, total=False
):
    bigQuerySourceConfig: GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigBigQuerySourceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigBigQuerySourceConfig(
    typing.TypedDict, total=False
):
    datapointFieldMapping: GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigDatapointFieldMapping
    tablePath: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigDatapointFieldMapping(
    typing.TypedDict, total=False
):
    embeddingColumn: str
    idColumn: str
    metadataColumns: _list[str]
    numericRestricts: _list[
        GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigDatapointFieldMappingNumericRestrict
    ]
    restricts: _list[
        GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigDatapointFieldMappingRestrict
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigDatapointFieldMappingNumericRestrict(
    typing.TypedDict, total=False
):
    namespace: str
    valueColumn: str
    valueType: typing.Literal["VALUE_TYPE_UNSPECIFIED", "INT", "FLOAT", "DOUBLE"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportIndexRequestConnectorConfigDatapointFieldMappingRestrict(
    typing.TypedDict, total=False
):
    allowColumn: _list[str]
    denyColumn: _list[str]
    namespace: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportModelEvaluationRequest(
    typing.TypedDict, total=False
):
    modelEvaluation: GoogleCloudAiplatformV1beta1ModelEvaluation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportRagFilesConfig(typing.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    globalMaxEmbeddingRequestsPerMin: int
    googleDriveSource: GoogleCloudAiplatformV1beta1GoogleDriveSource
    importResultBigquerySink: GoogleCloudAiplatformV1beta1BigQueryDestination
    importResultGcsSink: GoogleCloudAiplatformV1beta1GcsDestination
    jiraSource: GoogleCloudAiplatformV1beta1JiraSource
    maxEmbeddingRequestsPerMin: int
    partialFailureBigquerySink: GoogleCloudAiplatformV1beta1BigQueryDestination
    partialFailureGcsSink: GoogleCloudAiplatformV1beta1GcsDestination
    ragFileChunkingConfig: GoogleCloudAiplatformV1beta1RagFileChunkingConfig
    ragFileMetadataConfig: GoogleCloudAiplatformV1beta1RagFileMetadataConfig
    ragFileParsingConfig: GoogleCloudAiplatformV1beta1RagFileParsingConfig
    ragFileTransformationConfig: GoogleCloudAiplatformV1beta1RagFileTransformationConfig
    rebuildAnnIndex: bool
    sharePointSources: GoogleCloudAiplatformV1beta1SharePointSources
    slackSource: GoogleCloudAiplatformV1beta1SlackSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportRagFilesRequest(typing.TypedDict, total=False):
    importRagFilesConfig: GoogleCloudAiplatformV1beta1ImportRagFilesConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Index(typing.TypedDict, total=False):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1beta1DeployedIndexRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    indexStats: GoogleCloudAiplatformV1beta1IndexStats
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
class GoogleCloudAiplatformV1beta1IndexDatapoint(typing.TypedDict, total=False):
    crowdingTag: GoogleCloudAiplatformV1beta1IndexDatapointCrowdingTag
    datapointId: str
    embeddingMetadata: dict[str, typing.Any]
    featureVector: _list[float]
    numericRestricts: _list[
        GoogleCloudAiplatformV1beta1IndexDatapointNumericRestriction
    ]
    restricts: _list[GoogleCloudAiplatformV1beta1IndexDatapointRestriction]
    sparseEmbedding: GoogleCloudAiplatformV1beta1IndexDatapointSparseEmbedding

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointCrowdingTag(
    typing.TypedDict, total=False
):
    crowdingAttribute: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointNumericRestriction(
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
class GoogleCloudAiplatformV1beta1IndexDatapointRestriction(
    typing.TypedDict, total=False
):
    allowList: _list[str]
    denyList: _list[str]
    namespace: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointSparseEmbedding(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexEndpoint(typing.TypedDict, total=False):
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
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexPrivateEndpoints(typing.TypedDict, total=False):
    matchGrpcAddress: str
    pscAutomatedEndpoints: _list[GoogleCloudAiplatformV1beta1PscAutomatedEndpoints]
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexStats(typing.TypedDict, total=False):
    shardsCount: int
    sparseVectorsCount: str
    vectorsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1InferenceEventLoggingConfig(
    typing.TypedDict, total=False
):
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IngestEventsRequest(typing.TypedDict, total=False):
    directContentsSource: GoogleCloudAiplatformV1beta1IngestionDirectContentsSource
    disableMemoryRevisions: bool
    forceFlush: bool
    generationTriggerConfig: GoogleCloudAiplatformV1beta1MemoryGenerationTriggerConfig
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
class GoogleCloudAiplatformV1beta1IngestionDirectContentsSource(
    typing.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1beta1IngestionDirectContentsSourceEvent]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IngestionDirectContentsSourceEvent(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1beta1Content
    eventId: str
    eventTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1InputDataConfig(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1Int64Array(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IntegratedGradientsAttribution(
    typing.TypedDict, total=False
):
    blurBaselineConfig: GoogleCloudAiplatformV1beta1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1beta1SmoothGradConfig
    stepCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IntermediateExtractedMemory(
    typing.TypedDict, total=False
):
    context: str
    fact: str
    structuredData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance(
    typing.TypedDict, total=False
):
    serviceName: typing.Literal[
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
        "GCR_DNS_STATE",
        "GUEST_ATTRIBUTE_STATE",
    ]
    serviceState: typing.Literal["UNKNOWN", "HEALTHY", "UNHEALTHY"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1InvokeRequest(typing.TypedDict, total=False):
    deployedModelId: str
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1beta1JiraSource(typing.TypedDict, total=False):
    jiraQueries: _list[GoogleCloudAiplatformV1beta1JiraSourceJiraQueries]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1JiraSourceJiraQueries(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1beta1ApiAuthApiKeyConfig
    customQueries: _list[str]
    email: str
    projects: _list[str]
    serverUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1KeepAliveProbe(typing.TypedDict, total=False):
    httpGet: GoogleCloudAiplatformV1beta1KeepAliveProbeHttpGet
    maxSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1KeepAliveProbeHttpGet(typing.TypedDict, total=False):
    path: str
    port: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LLMBasedMetricSpec(typing.TypedDict, total=False):
    additionalConfig: dict[str, typing.Any]
    judgeAutoraterConfig: GoogleCloudAiplatformV1beta1AutoraterConfig
    metricPromptTemplate: str
    predefinedRubricGenerationSpec: GoogleCloudAiplatformV1beta1PredefinedMetricSpec
    resultParserConfig: GoogleCloudAiplatformV1beta1EvaluationParserConfig
    rubricGenerationSpec: GoogleCloudAiplatformV1beta1RubricGenerationSpec
    rubricGroupKey: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LargeModelReference(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LineageSubgraph(typing.TypedDict, total=False):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]
    events: _list[GoogleCloudAiplatformV1beta1Event]
    executions: _list[GoogleCloudAiplatformV1beta1Execution]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListA2aTaskEventsResponse(
    typing.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1beta1A2aTaskEvent]
    nextPageToken: str
    taskEvents: _list[GoogleCloudAiplatformV1beta1TaskEvent]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListA2aTasksResponse(typing.TypedDict, total=False):
    a2aTasks: _list[GoogleCloudAiplatformV1beta1A2aTask]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAgentAnomalyDetectionScopesResponse(
    typing.TypedDict, total=False
):
    agentAnomalyDetectionScopes: _list[
        GoogleCloudAiplatformV1beta1AgentAnomalyDetectionScope
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAgentsResponse(typing.TypedDict, total=False):
    agents: _list[GoogleCloudAiplatformV1beta1Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAnalyzedInvocationsResponse(
    typing.TypedDict, total=False
):
    analyzedInvocations: _list[GoogleCloudAiplatformV1beta1AnalyzedInvocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAnalyzedSessionsResponse(
    typing.TypedDict, total=False
):
    analyzedSessions: _list[GoogleCloudAiplatformV1beta1AnalyzedSession]
    nextPageToken: str
    summary: GoogleCloudAiplatformV1beta1ListAnalyzedSessionsResponseViewSummary

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAnalyzedSessionsResponseViewSummary(
    typing.TypedDict, total=False
):
    anomalousAgentsCount: int
    anomalousSessionsCount: int
    llmScannedSessionsCount: int
    severities: dict[str, typing.Any]
    totalSessionsCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAnnotationsResponse(
    typing.TypedDict, total=False
):
    annotations: _list[GoogleCloudAiplatformV1beta1Annotation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListArtifactsResponse(typing.TypedDict, total=False):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponse(
    typing.TypedDict, total=False
):
    batchPredictionJobs: _list[GoogleCloudAiplatformV1beta1BatchPredictionJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListCachedContentsResponse(
    typing.TypedDict, total=False
):
    cachedContents: _list[GoogleCloudAiplatformV1beta1CachedContent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListContextsResponse(typing.TypedDict, total=False):
    contexts: _list[GoogleCloudAiplatformV1beta1Context]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListCustomJobsResponse(typing.TypedDict, total=False):
    customJobs: _list[GoogleCloudAiplatformV1beta1CustomJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataItemsResponse(typing.TypedDict, total=False):
    dataItems: _list[GoogleCloudAiplatformV1beta1DataItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponse(
    typing.TypedDict, total=False
):
    dataLabelingJobs: _list[GoogleCloudAiplatformV1beta1DataLabelingJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetVersionsResponse(
    typing.TypedDict, total=False
):
    datasetVersions: _list[GoogleCloudAiplatformV1beta1DatasetVersion]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetsResponse(typing.TypedDict, total=False):
    datasets: _list[GoogleCloudAiplatformV1beta1Dataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponse(
    typing.TypedDict, total=False
):
    deploymentResourcePools: _list[GoogleCloudAiplatformV1beta1DeploymentResourcePool]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEndpointsResponse(typing.TypedDict, total=False):
    endpoints: _list[GoogleCloudAiplatformV1beta1Endpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEntityTypesResponse(
    typing.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudAiplatformV1beta1EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEvaluationItemsResponse(
    typing.TypedDict, total=False
):
    evaluationItems: _list[GoogleCloudAiplatformV1beta1EvaluationItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEvaluationMetricsResponse(
    typing.TypedDict, total=False
):
    evaluationMetrics: _list[GoogleCloudAiplatformV1beta1EvaluationMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEvaluationRunsResponse(
    typing.TypedDict, total=False
):
    evaluationRuns: _list[GoogleCloudAiplatformV1beta1EvaluationRun]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEvaluationSetsResponse(
    typing.TypedDict, total=False
):
    evaluationSets: _list[GoogleCloudAiplatformV1beta1EvaluationSet]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEventsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessionEvents: _list[GoogleCloudAiplatformV1beta1SessionEvent]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListExampleStoresResponse(
    typing.TypedDict, total=False
):
    exampleStores: _list[GoogleCloudAiplatformV1beta1ExampleStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListExecutionsResponse(typing.TypedDict, total=False):
    executions: _list[GoogleCloudAiplatformV1beta1Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListExtensionsResponse(typing.TypedDict, total=False):
    extensions: _list[GoogleCloudAiplatformV1beta1Extension]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureGroupsResponse(
    typing.TypedDict, total=False
):
    featureGroups: _list[GoogleCloudAiplatformV1beta1FeatureGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureMonitorJobsResponse(
    typing.TypedDict, total=False
):
    featureMonitorJobs: _list[GoogleCloudAiplatformV1beta1FeatureMonitorJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureMonitorsResponse(
    typing.TypedDict, total=False
):
    featureMonitors: _list[GoogleCloudAiplatformV1beta1FeatureMonitor]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponse(
    typing.TypedDict, total=False
):
    featureOnlineStores: _list[GoogleCloudAiplatformV1beta1FeatureOnlineStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponse(
    typing.TypedDict, total=False
):
    featureViewSyncs: _list[GoogleCloudAiplatformV1beta1FeatureViewSync]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureViewsResponse(
    typing.TypedDict, total=False
):
    featureViews: _list[GoogleCloudAiplatformV1beta1FeatureView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturesResponse(typing.TypedDict, total=False):
    features: _list[GoogleCloudAiplatformV1beta1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturestoresResponse(
    typing.TypedDict, total=False
):
    featurestores: _list[GoogleCloudAiplatformV1beta1Featurestore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeedbackEntriesResponse(
    typing.TypedDict, total=False
):
    feedbackEntries: _list[GoogleCloudAiplatformV1beta1FeedbackEntry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponse(
    typing.TypedDict, total=False
):
    hyperparameterTuningJobs: _list[GoogleCloudAiplatformV1beta1HyperparameterTuningJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexEndpointsResponse(
    typing.TypedDict, total=False
):
    indexEndpoints: _list[GoogleCloudAiplatformV1beta1IndexEndpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexesResponse(typing.TypedDict, total=False):
    indexes: _list[GoogleCloudAiplatformV1beta1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMemoriesResponse(typing.TypedDict, total=False):
    memories: _list[GoogleCloudAiplatformV1beta1Memory]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMemoryRevisionsResponse(
    typing.TypedDict, total=False
):
    memoryRevisions: _list[GoogleCloudAiplatformV1beta1MemoryRevision]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataSchemasResponse(
    typing.TypedDict, total=False
):
    metadataSchemas: _list[GoogleCloudAiplatformV1beta1MetadataSchema]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataStoresResponse(
    typing.TypedDict, total=False
):
    metadataStores: _list[GoogleCloudAiplatformV1beta1MetadataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponse(
    typing.TypedDict, total=False
):
    modelDeploymentMonitoringJobs: _list[
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponse(
    typing.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1beta1ModelEvaluationSlice]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationsResponse(
    typing.TypedDict, total=False
):
    modelEvaluations: _list[GoogleCloudAiplatformV1beta1ModelEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelMonitoringJobsResponse(
    typing.TypedDict, total=False
):
    modelMonitoringJobs: _list[GoogleCloudAiplatformV1beta1ModelMonitoringJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelMonitorsResponse(
    typing.TypedDict, total=False
):
    modelMonitors: _list[GoogleCloudAiplatformV1beta1ModelMonitor]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelVersionCheckpointsResponse(
    typing.TypedDict, total=False
):
    checkpoints: _list[GoogleCloudAiplatformV1beta1ModelVersionCheckpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelVersionsResponse(
    typing.TypedDict, total=False
):
    models: _list[GoogleCloudAiplatformV1beta1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelsResponse(typing.TypedDict, total=False):
    models: _list[GoogleCloudAiplatformV1beta1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMonitoredAgentsResponse(
    typing.TypedDict, total=False
):
    monitoredAgents: _list[GoogleCloudAiplatformV1beta1MonitoredAgent]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasJobsResponse(typing.TypedDict, total=False):
    nasJobs: _list[GoogleCloudAiplatformV1beta1NasJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponse(
    typing.TypedDict, total=False
):
    nasTrialDetails: _list[GoogleCloudAiplatformV1beta1NasTrialDetail]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookExecutionJobsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notebookExecutionJobs: _list[GoogleCloudAiplatformV1beta1NotebookExecutionJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimeTemplates: _list[GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimes: _list[GoogleCloudAiplatformV1beta1NotebookRuntime]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOnlineEvaluatorsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    onlineEvaluators: _list[GoogleCloudAiplatformV1beta1OnlineEvaluator]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOptimalTrialsRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOptimalTrialsResponse(
    typing.TypedDict, total=False
):
    optimalTrials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPersistentResourcesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    persistentResources: _list[GoogleCloudAiplatformV1beta1PersistentResource]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPipelineJobsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    pipelineJobs: _list[GoogleCloudAiplatformV1beta1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPublisherModelsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    publisherModels: _list[GoogleCloudAiplatformV1beta1PublisherModel]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListRagCorporaResponse(typing.TypedDict, total=False):
    nextPageToken: str
    ragCorpora: _list[GoogleCloudAiplatformV1beta1RagCorpus]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListRagDataSchemasResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    ragDataSchemas: _list[GoogleCloudAiplatformV1beta1RagDataSchema]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListRagFilesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    ragFiles: _list[GoogleCloudAiplatformV1beta1RagFile]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListRagMetadataResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    ragMetadata: _list[GoogleCloudAiplatformV1beta1RagMetadata]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListReasoningEngineRuntimeRevisionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    reasoningEngineRuntimeRevisions: _list[
        GoogleCloudAiplatformV1beta1ReasoningEngineRuntimeRevision
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListReasoningEnginesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    reasoningEngines: _list[GoogleCloudAiplatformV1beta1ReasoningEngine]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSandboxEnvironmentSnapshotsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sandboxEnvironmentSnapshots: _list[
        GoogleCloudAiplatformV1beta1SandboxEnvironmentSnapshot
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSandboxEnvironmentTemplatesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sandboxEnvironmentTemplates: _list[
        GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplate
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSandboxEnvironmentsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sandboxEnvironments: _list[GoogleCloudAiplatformV1beta1SandboxEnvironment]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSavedQueriesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    savedQueries: _list[GoogleCloudAiplatformV1beta1SavedQuery]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSchedulesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schedules: _list[GoogleCloudAiplatformV1beta1Schedule]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSemanticGovernancePoliciesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    semanticGovernancePolicies: _list[
        GoogleCloudAiplatformV1beta1SemanticGovernancePolicy
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListServingProfilesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    servingProfiles: _list[GoogleCloudAiplatformV1beta1ServingProfile]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[GoogleCloudAiplatformV1beta1Session]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSkillRevisionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    skillRevisions: _list[GoogleCloudAiplatformV1beta1SkillRevision]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSkillsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    skills: _list[GoogleCloudAiplatformV1beta1Skill]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    specialistPools: _list[GoogleCloudAiplatformV1beta1SpecialistPool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListStudiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    studies: _list[GoogleCloudAiplatformV1beta1Study]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    tensorboardExperiments: _list[GoogleCloudAiplatformV1beta1TensorboardExperiment]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardRunsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    tensorboardRuns: _list[GoogleCloudAiplatformV1beta1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1beta1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    tensorboards: _list[GoogleCloudAiplatformV1beta1Tensorboard]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    trainingPipelines: _list[GoogleCloudAiplatformV1beta1TrainingPipeline]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrialsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    trials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTuningJobsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tuningJobs: _list[GoogleCloudAiplatformV1beta1TuningJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LogprobsResult(typing.TypedDict, total=False):
    chosenCandidates: _list[GoogleCloudAiplatformV1beta1LogprobsResultCandidate]
    topCandidates: _list[GoogleCloudAiplatformV1beta1LogprobsResultTopCandidates]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LogprobsResultCandidate(
    typing.TypedDict, total=False
):
    logProbability: float
    token: str
    tokenId: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LogprobsResultTopCandidates(
    typing.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1beta1LogprobsResultCandidate]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LookupStudyRequest(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LossAnalysisConfig(typing.TypedDict, total=False):
    candidate: str
    metric: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LossAnalysisResult(typing.TypedDict, total=False):
    analysisTime: str
    clusters: _list[GoogleCloudAiplatformV1beta1LossCluster]
    config: GoogleCloudAiplatformV1beta1LossAnalysisConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LossCluster(typing.TypedDict, total=False):
    clusterId: str
    examples: _list[GoogleCloudAiplatformV1beta1LossExample]
    itemCount: int
    taxonomyEntry: GoogleCloudAiplatformV1beta1LossTaxonomyEntry

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LossExample(typing.TypedDict, total=False):
    evaluationItem: str
    evaluationResult: GoogleCloudAiplatformV1beta1EvaluationResult
    failedRubrics: _list[GoogleCloudAiplatformV1beta1FailedRubric]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LossTaxonomyEntry(typing.TypedDict, total=False):
    description: str
    l1Category: str
    l2Category: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LustreMount(typing.TypedDict, total=False):
    filesystem: str
    instanceIp: str
    mountPoint: str
    volumeHandle: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MachineSpec(typing.TypedDict, total=False):
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
    minGpuDriverVersion: str
    multihostGpuNodeCount: int
    reservationAffinity: GoogleCloudAiplatformV1beta1ReservationAffinity
    tpuTopology: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ManualBatchTuningParameters(
    typing.TypedDict, total=False
):
    batchSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Measurement(typing.TypedDict, total=False):
    elapsedDuration: str
    metrics: _list[GoogleCloudAiplatformV1beta1MeasurementMetric]
    stepCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MeasurementMetric(typing.TypedDict, total=False):
    metricId: str
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Memory(typing.TypedDict, total=False):
    createTime: str
    description: str
    disableMemoryRevisions: bool
    displayName: str
    expireTime: str
    fact: str
    memoryType: typing.Literal[
        "MEMORY_TYPE_UNSPECIFIED", "NATURAL_LANGUAGE_COLLECTION", "STRUCTURED_PROFILE"
    ]
    metadata: dict[str, typing.Any]
    name: str
    revisionExpireTime: str
    revisionLabels: dict[str, typing.Any]
    revisionTtl: str
    scope: dict[str, typing.Any]
    structuredContent: GoogleCloudAiplatformV1beta1MemoryStructuredContent
    topics: _list[GoogleCloudAiplatformV1beta1MemoryTopicId]
    ttl: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfig(
    typing.TypedDict, total=False
):
    consolidationConfig: (
        GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigConsolidationConfig
    )
    disableNaturalLanguageMemories: bool
    enableThirdPersonMemories: bool
    generateMemoriesExamples: _list[
        GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExample
    ]
    memoryTopics: _list[
        GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigMemoryTopic
    ]
    scopeKeys: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigConsolidationConfig(
    typing.TypedDict, total=False
):
    revisionsPerCandidateCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExample(
    typing.TypedDict, total=False
):
    conversationSource: GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource
    generatedMemories: _list[
        GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource(
    typing.TypedDict, total=False
):
    events: _list[
        GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent(
    typing.TypedDict, total=False
):
    content: GoogleCloudAiplatformV1beta1Content

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory(
    typing.TypedDict, total=False
):
    fact: str
    topics: _list[GoogleCloudAiplatformV1beta1MemoryTopicId]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigMemoryTopic(
    typing.TypedDict, total=False
):
    customMemoryTopic: GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic
    managedMemoryTopic: GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic(
    typing.TypedDict, total=False
):
    description: str
    label: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic(
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
class GoogleCloudAiplatformV1beta1MemoryConjunctionFilter(
    typing.TypedDict, total=False
):
    filters: _list[GoogleCloudAiplatformV1beta1MemoryFilter]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryFilter(typing.TypedDict, total=False):
    key: str
    negate: bool
    op: typing.Literal["OPERATOR_UNSPECIFIED", "EQUAL", "GREATER_THAN", "LESS_THAN"]
    value: GoogleCloudAiplatformV1beta1MemoryMetadataValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryGenerationTriggerConfig(
    typing.TypedDict, total=False
):
    generationRule: (
        GoogleCloudAiplatformV1beta1MemoryGenerationTriggerConfigGenerationTriggerRule
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryGenerationTriggerConfigGenerationTriggerRule(
    typing.TypedDict, total=False
):
    eventCount: int
    fixedInterval: str
    idleDuration: str
    overlapEventCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryMetadataValue(typing.TypedDict, total=False):
    boolValue: bool
    doubleValue: float
    stringValue: str
    timestampValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryProfile(typing.TypedDict, total=False):
    profile: dict[str, typing.Any]
    schemaId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryRevision(typing.TypedDict, total=False):
    createTime: str
    expireTime: str
    extractedMemories: _list[GoogleCloudAiplatformV1beta1IntermediateExtractedMemory]
    fact: str
    labels: dict[str, typing.Any]
    name: str
    structuredData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryStructuredContent(
    typing.TypedDict, total=False
):
    data: dict[str, typing.Any]
    schemaId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MemoryTopicId(typing.TypedDict, total=False):
    customMemoryTopicLabel: str
    managedMemoryTopic: typing.Literal[
        "MANAGED_TOPIC_ENUM_UNSPECIFIED",
        "USER_PERSONAL_INFO",
        "USER_PREFERENCES",
        "KEY_CONVERSATION_DETAILS",
        "EXPLICIT_INSTRUCTIONS",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MergeVersionAliasesRequest(
    typing.TypedDict, total=False
):
    versionAliases: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Metadata(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataList(typing.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1beta1MetadataValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataSchema(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1MetadataStore(typing.TypedDict, total=False):
    createTime: str
    dataplexConfig: GoogleCloudAiplatformV1beta1MetadataStoreDataplexConfig
    description: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    name: str
    state: GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreState
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataStoreDataplexConfig(
    typing.TypedDict, total=False
):
    enabledPipelinesLineage: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreState(
    typing.TypedDict, total=False
):
    diskUtilizationBytes: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataValue(typing.TypedDict, total=False):
    boolValue: bool
    datetimeValue: str
    floatValue: float
    intValue: str
    listValue: GoogleCloudAiplatformV1beta1MetadataList
    strValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Metric(typing.TypedDict, total=False):
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
    bleuSpec: GoogleCloudAiplatformV1beta1BleuSpec
    computationBasedMetricSpec: GoogleCloudAiplatformV1beta1ComputationBasedMetricSpec
    customCodeExecutionSpec: GoogleCloudAiplatformV1beta1CustomCodeExecutionSpec
    exactMatchSpec: GoogleCloudAiplatformV1beta1ExactMatchSpec
    llmBasedMetricSpec: GoogleCloudAiplatformV1beta1LLMBasedMetricSpec
    metadata: GoogleCloudAiplatformV1beta1MetricMetadata
    pairwiseMetricSpec: GoogleCloudAiplatformV1beta1PairwiseMetricSpec
    pointwiseMetricSpec: GoogleCloudAiplatformV1beta1PointwiseMetricSpec
    predefinedMetricSpec: GoogleCloudAiplatformV1beta1PredefinedMetricSpec
    rougeSpec: GoogleCloudAiplatformV1beta1RougeSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricMetadata(typing.TypedDict, total=False):
    otherMetadata: dict[str, typing.Any]
    scoreRange: GoogleCloudAiplatformV1beta1MetricMetadataScoreRange
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricMetadataScoreRange(
    typing.TypedDict, total=False
):
    description: str
    max: float
    min: float
    step: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricResult(typing.TypedDict, total=False):
    error: GoogleRpcStatus
    explanation: str
    rubricVerdicts: _list[GoogleCloudAiplatformV1beta1RubricVerdict]
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricSource(typing.TypedDict, total=False):
    metric: GoogleCloudAiplatformV1beta1Metric
    metricResourceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricxInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1MetricxInstance
    metricSpec: GoogleCloudAiplatformV1beta1MetricxSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricxInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str
    source: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricxResult(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetricxSpec(typing.TypedDict, total=False):
    sourceLanguage: str
    targetLanguage: str
    version: typing.Literal[
        "METRICX_VERSION_UNSPECIFIED",
        "METRICX_24_REF",
        "METRICX_24_SRC",
        "METRICX_24_SRC_REF",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResource(typing.TypedDict, total=False):
    automlDataset: GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset
    automlModel: GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel
    dataLabelingDataset: (
        GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset
    )
    lastMigrateTime: str
    lastUpdateTime: str
    mlEngineModelVersion: (
        GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset(
    typing.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel(
    typing.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset(
    typing.TypedDict, total=False
):
    dataLabelingAnnotatedDatasets: _list[
        GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset
    ]
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset(
    typing.TypedDict, total=False
):
    annotatedDataset: str
    annotatedDatasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion(
    typing.TypedDict, total=False
):
    endpoint: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequest(typing.TypedDict, total=False):
    migrateAutomlDatasetConfig: (
        GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlDatasetConfig
    )
    migrateAutomlModelConfig: (
        GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlModelConfig
    )
    migrateDataLabelingDatasetConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfig
    migrateMlEngineModelVersionConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateMlEngineModelVersionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlDatasetConfig(
    typing.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlModelConfig(
    typing.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfig(
    typing.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str
    migrateDataLabelingAnnotatedDatasetConfigs: _list[
        GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig(
    typing.TypedDict, total=False
):
    annotatedDataset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateMlEngineModelVersionConfig(
    typing.TypedDict, total=False
):
    endpoint: str
    modelDisplayName: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceResponse(
    typing.TypedDict, total=False
):
    dataset: str
    migratableResource: GoogleCloudAiplatformV1beta1MigratableResource
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModalityTokenCount(typing.TypedDict, total=False):
    modality: typing.Literal[
        "MODALITY_UNSPECIFIED", "TEXT", "IMAGE", "VIDEO", "AUDIO", "DOCUMENT"
    ]
    tokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Model(typing.TypedDict, total=False):
    artifactUri: str
    baseModelSource: GoogleCloudAiplatformV1beta1ModelBaseModelSource
    checkpoints: _list[GoogleCloudAiplatformV1beta1Checkpoint]
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    createTime: str
    defaultCheckpointId: str
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
class GoogleCloudAiplatformV1beta1ModelArmorConfig(typing.TypedDict, total=False):
    promptTemplateName: str
    responseTemplateName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelBaseModelSource(typing.TypedDict, total=False):
    genieSource: GoogleCloudAiplatformV1beta1GenieSource
    modelGardenSource: GoogleCloudAiplatformV1beta1ModelGardenSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelContainerSpec(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    deploymentTimeout: str
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    grpcPorts: _list[GoogleCloudAiplatformV1beta1Port]
    healthProbe: GoogleCloudAiplatformV1beta1Probe
    healthRoute: str
    imageUri: str
    invokeRoutePrefix: str
    livenessProbe: GoogleCloudAiplatformV1beta1Probe
    ports: _list[GoogleCloudAiplatformV1beta1Port]
    predictRoute: str
    sharedMemorySizeMb: str
    startupProbe: GoogleCloudAiplatformV1beta1Probe

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable(
    typing.TypedDict, total=False
):
    bigqueryTablePath: str
    logSource: typing.Literal["LOG_SOURCE_UNSPECIFIED", "TRAINING", "SERVING"]
    logType: typing.Literal["LOG_TYPE_UNSPECIFIED", "PREDICT", "EXPLAIN"]
    requestResponseLoggingSchemaVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob(
    typing.TypedDict, total=False
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
    modelDeploymentMonitoringScheduleConfig: (
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig
    )
    modelMonitoringAlertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig
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
    statsAnomaliesBaseDirectory: GoogleCloudAiplatformV1beta1GcsDestination
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata(
    typing.TypedDict, total=False
):
    runTime: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfig(
    typing.TypedDict, total=False
):
    deployedModelId: str
    objectiveConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig(
    typing.TypedDict, total=False
):
    monitorInterval: str
    monitorWindow: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluation(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    biasSlices: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec
    labels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationModelEvaluationExplanationSpec(
    typing.TypedDict, total=False
):
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSlice(typing.TypedDict, total=False):
    createTime: str
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1beta1ModelExplanation
    name: str
    slice: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice(
    typing.TypedDict, total=False
):
    dimension: str
    sliceSpec: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec(
    typing.TypedDict, total=False
):
    configs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange(
    typing.TypedDict, total=False
):
    high: float
    low: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecSliceConfig(
    typing.TypedDict, total=False
):
    allValues: bool
    range: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange
    value: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue(
    typing.TypedDict, total=False
):
    floatValue: float
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelExplanation(typing.TypedDict, total=False):
    meanAttributions: _list[GoogleCloudAiplatformV1beta1Attribution]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelExportFormat(typing.TypedDict, total=False):
    exportableContents: _list[
        typing.Literal["EXPORTABLE_CONTENT_UNSPECIFIED", "ARTIFACT", "IMAGE"]
    ]
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelGardenSource(typing.TypedDict, total=False):
    publicModelName: str
    skipHfModelCache: bool
    versionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitor(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    modelMonitoringSchema: GoogleCloudAiplatformV1beta1ModelMonitoringSchema
    modelMonitoringTarget: GoogleCloudAiplatformV1beta1ModelMonitorModelMonitoringTarget
    name: str
    notificationSpec: GoogleCloudAiplatformV1beta1ModelMonitoringNotificationSpec
    outputSpec: GoogleCloudAiplatformV1beta1ModelMonitoringOutputSpec
    satisfiesPzi: bool
    satisfiesPzs: bool
    tabularObjective: (
        GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecTabularObjective
    )
    trainingDataset: GoogleCloudAiplatformV1beta1ModelMonitoringInput
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitorModelMonitoringTarget(
    typing.TypedDict, total=False
):
    vertexModel: (
        GoogleCloudAiplatformV1beta1ModelMonitorModelMonitoringTargetVertexModelSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitorModelMonitoringTargetVertexModelSource(
    typing.TypedDict, total=False
):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlert(typing.TypedDict, total=False):
    alertTime: str
    anomaly: GoogleCloudAiplatformV1beta1ModelMonitoringAnomaly
    objectiveType: str
    statsName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlertCondition(
    typing.TypedDict, total=False
):
    threshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig(
    typing.TypedDict, total=False
):
    emailAlertConfig: (
        GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig
    )
    enableLogging: bool
    notificationChannels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig(
    typing.TypedDict, total=False
):
    userEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAnomaly(typing.TypedDict, total=False):
    algorithm: str
    modelMonitoringJob: str
    tabularAnomaly: GoogleCloudAiplatformV1beta1ModelMonitoringAnomalyTabularAnomaly

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAnomalyTabularAnomaly(
    typing.TypedDict, total=False
):
    anomaly: typing.Any
    anomalyUri: str
    condition: GoogleCloudAiplatformV1beta1ModelMonitoringAlertCondition
    summary: str
    triggerTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringConfig(typing.TypedDict, total=False):
    alertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig
    analysisInstanceSchemaUri: str
    objectiveConfigs: _list[GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig]
    statsAnomaliesBaseDirectory: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringInput(typing.TypedDict, total=False):
    batchPredictionOutput: (
        GoogleCloudAiplatformV1beta1ModelMonitoringInputBatchPredictionOutput
    )
    columnizedDataset: (
        GoogleCloudAiplatformV1beta1ModelMonitoringInputModelMonitoringDataset
    )
    timeInterval: GoogleTypeInterval
    timeOffset: GoogleCloudAiplatformV1beta1ModelMonitoringInputTimeOffset
    vertexEndpointLogs: (
        GoogleCloudAiplatformV1beta1ModelMonitoringInputVertexEndpointLogs
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringInputBatchPredictionOutput(
    typing.TypedDict, total=False
):
    batchPredictionJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringInputModelMonitoringDataset(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1ModelMonitoringInputModelMonitoringDatasetModelMonitoringBigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1ModelMonitoringInputModelMonitoringDatasetModelMonitoringGcsSource
    timestampField: str
    vertexDataset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringInputModelMonitoringDatasetModelMonitoringBigQuerySource(
    typing.TypedDict, total=False
):
    query: str
    tableUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringInputModelMonitoringDatasetModelMonitoringGcsSource(
    typing.TypedDict, total=False
):
    format: typing.Literal["DATA_FORMAT_UNSPECIFIED", "CSV", "TF_RECORD", "JSONL"]
    gcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringInputTimeOffset(
    typing.TypedDict, total=False
):
    offset: str
    window: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringInputVertexEndpointLogs(
    typing.TypedDict, total=False
):
    endpoints: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringJob(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    jobExecutionDetail: GoogleCloudAiplatformV1beta1ModelMonitoringJobExecutionDetail
    modelMonitoringSpec: GoogleCloudAiplatformV1beta1ModelMonitoringSpec
    name: str
    schedule: str
    scheduleTime: str
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
class GoogleCloudAiplatformV1beta1ModelMonitoringJobExecutionDetail(
    typing.TypedDict, total=False
):
    baselineDatasets: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringJobExecutionDetailProcessedDataset
    ]
    error: GoogleRpcStatus
    objectiveStatus: dict[str, typing.Any]
    targetDatasets: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringJobExecutionDetailProcessedDataset
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringJobExecutionDetailProcessedDataset(
    typing.TypedDict, total=False
):
    location: str
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringNotificationSpec(
    typing.TypedDict, total=False
):
    emailConfig: GoogleCloudAiplatformV1beta1ModelMonitoringNotificationSpecEmailConfig
    enableCloudLogging: bool
    notificationChannelConfigs: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringNotificationSpecNotificationChannelConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringNotificationSpecEmailConfig(
    typing.TypedDict, total=False
):
    userEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringNotificationSpecNotificationChannelConfig(
    typing.TypedDict, total=False
):
    notificationChannel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig(
    typing.TypedDict, total=False
):
    explanationConfig: (
        GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfig
    )
    predictionDriftDetectionConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig
    trainingDataset: (
        GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDataset
    )
    trainingPredictionSkewDetectionConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfig(
    typing.TypedDict, total=False
):
    enableFeatureAttributes: bool
    explanationBaseline: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline(
    typing.TypedDict, total=False
):
    bigquery: GoogleCloudAiplatformV1beta1BigQueryDestination
    gcs: GoogleCloudAiplatformV1beta1GcsDestination
    predictionFormat: typing.Literal[
        "PREDICTION_FORMAT_UNSPECIFIED", "JSONL", "BIGQUERY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig(
    typing.TypedDict, total=False
):
    attributionScoreDriftThresholds: dict[str, typing.Any]
    defaultDriftThreshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    driftThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDataset(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    dataFormat: str
    dataset: str
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    loggingSamplingStrategy: GoogleCloudAiplatformV1beta1SamplingStrategy
    targetField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig(
    typing.TypedDict, total=False
):
    attributionScoreSkewThresholds: dict[str, typing.Any]
    defaultSkewThreshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    skewThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpec(
    typing.TypedDict, total=False
):
    baselineDataset: GoogleCloudAiplatformV1beta1ModelMonitoringInput
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    tabularObjective: (
        GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecTabularObjective
    )
    targetDataset: GoogleCloudAiplatformV1beta1ModelMonitoringInput

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecDataDriftSpec(
    typing.TypedDict, total=False
):
    categoricalMetricType: str
    defaultCategoricalAlertCondition: (
        GoogleCloudAiplatformV1beta1ModelMonitoringAlertCondition
    )
    defaultNumericAlertCondition: (
        GoogleCloudAiplatformV1beta1ModelMonitoringAlertCondition
    )
    featureAlertConditions: dict[str, typing.Any]
    features: _list[str]
    numericMetricType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecFeatureAttributionSpec(
    typing.TypedDict, total=False
):
    batchExplanationDedicatedResources: (
        GoogleCloudAiplatformV1beta1BatchDedicatedResources
    )
    defaultAlertCondition: GoogleCloudAiplatformV1beta1ModelMonitoringAlertCondition
    featureAlertConditions: dict[str, typing.Any]
    features: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecTabularObjective(
    typing.TypedDict, total=False
):
    featureAttributionSpec: (
        GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecFeatureAttributionSpec
    )
    featureDriftSpec: (
        GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecDataDriftSpec
    )
    predictionOutputDriftSpec: (
        GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpecDataDriftSpec
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringOutputSpec(
    typing.TypedDict, total=False
):
    gcsBaseDirectory: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringSchema(typing.TypedDict, total=False):
    featureFields: _list[GoogleCloudAiplatformV1beta1ModelMonitoringSchemaFieldSchema]
    groundTruthFields: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringSchemaFieldSchema
    ]
    predictionFields: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringSchemaFieldSchema
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringSchemaFieldSchema(
    typing.TypedDict, total=False
):
    dataType: str
    name: str
    repeated: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringSpec(typing.TypedDict, total=False):
    notificationSpec: GoogleCloudAiplatformV1beta1ModelMonitoringNotificationSpec
    objectiveSpec: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveSpec
    outputSpec: GoogleCloudAiplatformV1beta1ModelMonitoringOutputSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStats(typing.TypedDict, total=False):
    tabularStats: GoogleCloudAiplatformV1beta1ModelMonitoringTabularStats

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies(
    typing.TypedDict, total=False
):
    anomalyCount: int
    deployedModelId: str
    featureStats: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies
    ]
    objective: typing.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies(
    typing.TypedDict, total=False
):
    featureDisplayName: str
    predictionStats: _list[GoogleCloudAiplatformV1beta1FeatureStatsAnomaly]
    threshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    trainingStats: GoogleCloudAiplatformV1beta1FeatureStatsAnomaly

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsDataPoint(
    typing.TypedDict, total=False
):
    algorithm: str
    baselineStats: GoogleCloudAiplatformV1beta1ModelMonitoringStatsDataPointTypedValue
    createTime: str
    currentStats: GoogleCloudAiplatformV1beta1ModelMonitoringStatsDataPointTypedValue
    hasAnomaly: bool
    modelMonitoringJob: str
    schedule: str
    thresholdValue: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsDataPointTypedValue(
    typing.TypedDict, total=False
):
    distributionValue: GoogleCloudAiplatformV1beta1ModelMonitoringStatsDataPointTypedValueDistributionDataValue
    doubleValue: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsDataPointTypedValueDistributionDataValue(
    typing.TypedDict, total=False
):
    distribution: typing.Any
    distributionDeviation: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringTabularStats(
    typing.TypedDict, total=False
):
    dataPoints: _list[GoogleCloudAiplatformV1beta1ModelMonitoringStatsDataPoint]
    objectiveType: str
    statsName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelOriginalModelInfo(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelSourceInfo(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1ModelVersionCheckpoint(typing.TypedDict, total=False):
    checkpointId: str
    epoch: str
    step: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MonitoredAgent(typing.TypedDict, total=False):
    agentResource: GoogleCloudAiplatformV1beta1AgentResource
    createTime: str
    displayName: str
    name: str
    state: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ACTIVE", "ENABLING", "DISABLED"
    ]
    statusMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MultiSpeakerVoiceConfig(
    typing.TypedDict, total=False
):
    speakerVoiceConfigs: _list[GoogleCloudAiplatformV1beta1SpeakerVoiceConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedIndexOperationMetadata(
    typing.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedIndexResponse(
    typing.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelRequest(
    typing.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelResponse(
    typing.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJob(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1NasJobOutput(typing.TypedDict, total=False):
    multiTrialJobOutput: GoogleCloudAiplatformV1beta1NasJobOutputMultiTrialJobOutput

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobOutputMultiTrialJobOutput(
    typing.TypedDict, total=False
):
    searchTrials: _list[GoogleCloudAiplatformV1beta1NasTrial]
    trainTrials: _list[GoogleCloudAiplatformV1beta1NasTrial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpec(typing.TypedDict, total=False):
    multiTrialAlgorithmSpec: (
        GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec
    )
    resumeNasJobId: str
    searchSpaceSpec: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec(
    typing.TypedDict, total=False
):
    metric: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec
    multiTrialAlgorithm: typing.Literal[
        "MULTI_TRIAL_ALGORITHM_UNSPECIFIED", "REINFORCEMENT_LEARNING", "GRID_SEARCH"
    ]
    searchTrialSpec: (
        GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec
    )
    trainTrialSpec: (
        GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec(
    typing.TypedDict, total=False
):
    goal: typing.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec(
    typing.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxParallelTrialCount: int
    maxTrialCount: int
    searchTrialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec(
    typing.TypedDict, total=False
):
    frequency: int
    maxParallelTrialCount: int
    trainTrialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasTrial(typing.TypedDict, total=False):
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
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
class GoogleCloudAiplatformV1beta1NasTrialDetail(typing.TypedDict, total=False):
    name: str
    parameters: str
    searchTrial: GoogleCloudAiplatformV1beta1NasTrial
    trainTrial: GoogleCloudAiplatformV1beta1NasTrial

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQuery(typing.TypedDict, total=False):
    embedding: GoogleCloudAiplatformV1beta1NearestNeighborQueryEmbedding
    entityId: str
    neighborCount: int
    numericFilters: _list[GoogleCloudAiplatformV1beta1NearestNeighborQueryNumericFilter]
    parameters: GoogleCloudAiplatformV1beta1NearestNeighborQueryParameters
    perCrowdingAttributeNeighborCount: int
    stringFilters: _list[GoogleCloudAiplatformV1beta1NearestNeighborQueryStringFilter]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQueryEmbedding(
    typing.TypedDict, total=False
):
    value: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQueryNumericFilter(
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
class GoogleCloudAiplatformV1beta1NearestNeighborQueryParameters(
    typing.TypedDict, total=False
):
    approximateNeighborCandidates: int
    leafNodesSearchFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborQueryStringFilter(
    typing.TypedDict, total=False
):
    allowTokens: _list[str]
    denyTokens: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata(
    typing.TypedDict, total=False
):
    contentValidationStats: _list[
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataContentValidationStats
    ]
    dataBytesCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataContentValidationStats(
    typing.TypedDict, total=False
):
    invalidRecordCount: str
    invalidSparseRecordCount: str
    partialErrors: _list[
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataRecordError
    ]
    sourceGcsUri: str
    validRecordCount: str
    validSparseRecordCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataRecordError(
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
class GoogleCloudAiplatformV1beta1NearestNeighbors(typing.TypedDict, total=False):
    neighbors: _list[GoogleCloudAiplatformV1beta1NearestNeighborsNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborsNeighbor(
    typing.TypedDict, total=False
):
    distance: float
    entityId: str
    entityKeyValues: GoogleCloudAiplatformV1beta1FetchFeatureValuesResponse

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Neighbor(typing.TypedDict, total=False):
    neighborDistance: float
    neighborId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NetworkSpec(typing.TypedDict, total=False):
    enableInternetAccess: bool
    network: str
    subnetwork: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NfsMount(typing.TypedDict, total=False):
    mountPoint: str
    path: str
    server: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookEucConfig(typing.TypedDict, total=False):
    bypassActasCheck: bool
    eucDisabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJob(typing.TypedDict, total=False):
    createTime: str
    customEnvironmentSpec: (
        GoogleCloudAiplatformV1beta1NotebookExecutionJobCustomEnvironmentSpec
    )
    dataformRepositorySource: (
        GoogleCloudAiplatformV1beta1NotebookExecutionJobDataformRepositorySource
    )
    directNotebookSource: (
        GoogleCloudAiplatformV1beta1NotebookExecutionJobDirectNotebookSource
    )
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    executionTimeout: str
    executionUser: str
    gcsNotebookSource: GoogleCloudAiplatformV1beta1NotebookExecutionJobGcsNotebookSource
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
    workbenchRuntime: GoogleCloudAiplatformV1beta1NotebookExecutionJobWorkbenchRuntime

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobCustomEnvironmentSpec(
    typing.TypedDict, total=False
):
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    networkSpec: GoogleCloudAiplatformV1beta1NetworkSpec
    persistentDiskSpec: GoogleCloudAiplatformV1beta1PersistentDiskSpec
    shieldedInstanceConfig: GoogleCloudAiplatformV1beta1NotebookExecutionJobCustomEnvironmentSpecShieldedInstanceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobCustomEnvironmentSpecShieldedInstanceConfig(
    typing.TypedDict, total=False
):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobDataformRepositorySource(
    typing.TypedDict, total=False
):
    commitSha: str
    dataformRepositoryResourceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobDirectNotebookSource(
    typing.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobGcsNotebookSource(
    typing.TypedDict, total=False
):
    generation: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobWorkbenchRuntime(
    typing.TypedDict, total=False
):
    customContainerImage: (
        GoogleCloudAiplatformV1beta1NotebookExecutionJobWorkbenchRuntimeContainerImage
    )
    vmImage: GoogleCloudAiplatformV1beta1NotebookExecutionJobWorkbenchRuntimeVmImage

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobWorkbenchRuntimeContainerImage(
    typing.TypedDict, total=False
):
    repository: str
    tag: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobWorkbenchRuntimeVmImage(
    typing.TypedDict, total=False
):
    family: str
    name: str
    project: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig(
    typing.TypedDict, total=False
):
    idleShutdownDisabled: bool
    idleTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookReservationAffinity(
    typing.TypedDict, total=False
):
    consumeReservationType: typing.Literal[
        "RESERVATION_AFFINITY_TYPE_UNSPECIFIED",
        "RESERVATION_NONE",
        "RESERVATION_ANY",
        "RESERVATION_SPECIFIC",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntime(typing.TypedDict, total=False):
    createTime: str
    dataPersistentDiskSpec: GoogleCloudAiplatformV1beta1PersistentDiskSpec
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    eucConfig: GoogleCloudAiplatformV1beta1NotebookEucConfig
    expirationTime: str
    healthState: typing.Literal["HEALTH_STATE_UNSPECIFIED", "HEALTHY", "UNHEALTHY"]
    idleShutdownConfig: GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig
    isUpgradable: bool
    labels: dict[str, typing.Any]
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    name: str
    networkSpec: GoogleCloudAiplatformV1beta1NetworkSpec
    networkTags: _list[str]
    notebookRuntimeTemplateRef: GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateRef
    notebookRuntimeType: typing.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    proxyUri: str
    reservationAffinity: GoogleCloudAiplatformV1beta1NotebookReservationAffinity
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
    shieldedVmConfig: GoogleCloudAiplatformV1beta1ShieldedVmConfig
    softwareConfig: GoogleCloudAiplatformV1beta1NotebookSoftwareConfig
    updateTime: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate(
    typing.TypedDict, total=False
):
    createTime: str
    dataPersistentDiskSpec: GoogleCloudAiplatformV1beta1PersistentDiskSpec
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    eucConfig: GoogleCloudAiplatformV1beta1NotebookEucConfig
    idleShutdownConfig: GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig
    isDefault: bool
    labels: dict[str, typing.Any]
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    name: str
    networkSpec: GoogleCloudAiplatformV1beta1NetworkSpec
    networkTags: _list[str]
    notebookRuntimeType: typing.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    reservationAffinity: GoogleCloudAiplatformV1beta1NotebookReservationAffinity
    serviceAccount: str
    shieldedVmConfig: GoogleCloudAiplatformV1beta1ShieldedVmConfig
    softwareConfig: GoogleCloudAiplatformV1beta1NotebookSoftwareConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateRef(
    typing.TypedDict, total=False
):
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookSoftwareConfig(typing.TypedDict, total=False):
    colabImage: GoogleCloudAiplatformV1beta1ColabImage
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    postStartupScriptConfig: GoogleCloudAiplatformV1beta1PostStartupScriptConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluator(typing.TypedDict, total=False):
    agentResource: str
    cloudObservability: GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservability
    config: GoogleCloudAiplatformV1beta1OnlineEvaluatorConfig
    createTime: str
    displayName: str
    metricSources: _list[GoogleCloudAiplatformV1beta1MetricSource]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED", "FAILED", "WARNING"
    ]
    stateDetails: _list[GoogleCloudAiplatformV1beta1OnlineEvaluatorStateDetails]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservability(
    typing.TypedDict, total=False
):
    logView: str
    openTelemetry: (
        GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityOpenTelemetry
    )
    traceScope: GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityTraceScope
    traceView: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityNumericPredicate(
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
class GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityOpenTelemetry(
    typing.TypedDict, total=False
):
    semconvVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityTraceScope(
    typing.TypedDict, total=False
):
    filter: _list[
        GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityTraceScopePredicate
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityTraceScopePredicate(
    typing.TypedDict, total=False
):
    duration: (
        GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityNumericPredicate
    )
    totalTokenUsage: (
        GoogleCloudAiplatformV1beta1OnlineEvaluatorCloudObservabilityNumericPredicate
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluatorConfig(typing.TypedDict, total=False):
    maxEvaluatedSamplesPerRun: str
    randomSampling: GoogleCloudAiplatformV1beta1OnlineEvaluatorConfigRandomSampling

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluatorConfigRandomSampling(
    typing.TypedDict, total=False
):
    percentage: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OnlineEvaluatorStateDetails(
    typing.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OptimizePromptRequest(typing.TypedDict, total=False):
    content: GoogleCloudAiplatformV1beta1Content
    optimizationTarget: typing.Literal[
        "OPTIMIZATION_TARGET_UNSPECIFIED",
        "OPTIMIZATION_TARGET_GENERAL",
        "OPTIMIZATION_TARGET_GEMINI_NANO",
        "OPTIMIZATION_TARGET_FEW_SHOT_RUBRICS",
        "OPTIMIZATION_TARGET_FEW_SHOT_TARGET_RESPONSE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OptimizePromptResponse(typing.TypedDict, total=False):
    content: GoogleCloudAiplatformV1beta1Content

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OutputConfig(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OutputFieldSpec(typing.TypedDict, total=False):
    fieldName: str
    fieldType: typing.Literal[
        "FIELD_TYPE_UNSPECIFIED", "CONTENT", "TEXT", "IMAGE", "AUDIO"
    ]
    guidance: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1OutputInfo(typing.TypedDict, total=False):
    gcsOutputDirectory: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PSCAutomationConfig(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1PairwiseMetricInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1PairwiseMetricInstance
    metricSpec: GoogleCloudAiplatformV1beta1PairwiseMetricSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseMetricInstance(typing.TypedDict, total=False):
    contentMapInstance: GoogleCloudAiplatformV1beta1ContentMap
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseMetricResult(typing.TypedDict, total=False):
    customOutput: GoogleCloudAiplatformV1beta1CustomOutput
    explanation: str
    pairwiseChoice: typing.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseMetricSpec(typing.TypedDict, total=False):
    baselineResponseFieldName: str
    candidateResponseFieldName: str
    customOutputFormatConfig: GoogleCloudAiplatformV1beta1CustomOutputFormatConfig
    metricPromptTemplate: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualityInstance
    metricSpec: GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualityInstance(
    typing.TypedDict, total=False
):
    baselinePrediction: str
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    pairwiseChoice: typing.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseQuestionAnsweringQualitySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseSummarizationQualityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1PairwiseSummarizationQualityInstance
    metricSpec: GoogleCloudAiplatformV1beta1PairwiseSummarizationQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseSummarizationQualityInstance(
    typing.TypedDict, total=False
):
    baselinePrediction: str
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseSummarizationQualityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    pairwiseChoice: typing.Literal[
        "PAIRWISE_CHOICE_UNSPECIFIED", "BASELINE", "CANDIDATE", "TIE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PairwiseSummarizationQualitySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Part(typing.TypedDict, total=False):
    audioTranscription: GoogleCloudAiplatformV1beta1AudioTranscription
    codeExecutionResult: GoogleCloudAiplatformV1beta1CodeExecutionResult
    executableCode: GoogleCloudAiplatformV1beta1ExecutableCode
    fileData: GoogleCloudAiplatformV1beta1FileData
    functionCall: GoogleCloudAiplatformV1beta1FunctionCall
    functionResponse: GoogleCloudAiplatformV1beta1FunctionResponse
    inlineData: GoogleCloudAiplatformV1beta1Blob
    mediaResolution: GoogleCloudAiplatformV1beta1PartMediaResolution
    text: str
    thought: bool
    thoughtSignature: str
    videoMetadata: GoogleCloudAiplatformV1beta1VideoMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PartMediaResolution(typing.TypedDict, total=False):
    level: typing.Literal[
        "MEDIA_RESOLUTION_UNSPECIFIED",
        "MEDIA_RESOLUTION_LOW",
        "MEDIA_RESOLUTION_MEDIUM",
        "MEDIA_RESOLUTION_HIGH",
        "MEDIA_RESOLUTION_ULTRA_HIGH",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PartialArg(typing.TypedDict, total=False):
    boolValue: bool
    jsonPath: str
    nullValue: typing.Literal["NULL_VALUE"]
    numberValue: float
    stringValue: str
    willContinue: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PartnerModelTuningSpec(typing.TypedDict, total=False):
    hyperParameters: dict[str, typing.Any]
    trainingDatasetUri: str
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PauseModelDeploymentMonitoringJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PauseSandboxEnvironmentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PauseScheduleRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PersistentDiskSpec(typing.TypedDict, total=False):
    diskSizeGb: str
    diskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PersistentResource(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    network: str
    pscInterfaceConfig: GoogleCloudAiplatformV1beta1PscInterfaceConfig
    reservedIpRanges: _list[str]
    resourcePools: _list[GoogleCloudAiplatformV1beta1ResourcePool]
    resourceRuntime: GoogleCloudAiplatformV1beta1ResourceRuntime
    resourceRuntimeSpec: GoogleCloudAiplatformV1beta1ResourceRuntimeSpec
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
class GoogleCloudAiplatformV1beta1PipelineJob(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobDetail: GoogleCloudAiplatformV1beta1PipelineJobDetail
    labels: dict[str, typing.Any]
    name: str
    network: str
    originalPipelineJobId: str
    pipelineSpec: dict[str, typing.Any]
    pipelineTaskRerunConfigs: _list[GoogleCloudAiplatformV1beta1PipelineTaskRerunConfig]
    preflightValidations: bool
    pscInterfaceConfig: GoogleCloudAiplatformV1beta1PscInterfaceConfig
    reservedIpRanges: _list[str]
    runtimeConfig: GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    templateMetadata: GoogleCloudAiplatformV1beta1PipelineTemplateMetadata
    templateUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobDetail(typing.TypedDict, total=False):
    pipelineContext: GoogleCloudAiplatformV1beta1Context
    pipelineRunContext: GoogleCloudAiplatformV1beta1Context
    taskDetails: _list[GoogleCloudAiplatformV1beta1PipelineTaskDetail]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfig(
    typing.TypedDict, total=False
):
    defaultRuntime: GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigDefaultRuntime
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
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigDefaultRuntime(
    typing.TypedDict, total=False
):
    persistentResourceRuntimeDetail: GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigPersistentResourceRuntimeDetail

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigInputArtifact(
    typing.TypedDict, total=False
):
    artifactId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigPersistentResourceRuntimeDetail(
    typing.TypedDict, total=False
):
    persistentResourceName: str
    taskResourceUnavailableTimeoutBehavior: typing.Literal[
        "TASK_RESOURCE_UNAVAILABLE_TIMEOUT_BEHAVIOR_UNSPECIFIED",
        "FAIL",
        "FALL_BACK_TO_ON_DEMAND",
    ]
    taskResourceUnavailableWaitTimeMs: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetail(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1PipelineTaskDetailArtifactList(
    typing.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetailPipelineTaskStatus(
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
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetail(
    typing.TypedDict, total=False
):
    containerDetail: (
        GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailContainerDetail
    )
    customJobDetail: (
        GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailCustomJobDetail
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailContainerDetail(
    typing.TypedDict, total=False
):
    failedMainJobs: _list[str]
    failedPreCachingCheckJobs: _list[str]
    mainJob: str
    preCachingCheckJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailCustomJobDetail(
    typing.TypedDict, total=False
):
    failedJobs: _list[str]
    job: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskRerunConfig(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1PipelineTaskRerunConfigInputs
    skipDownstreamTasks: bool
    skipTask: bool
    taskId: str
    taskName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskRerunConfigArtifactList(
    typing.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1RuntimeArtifact]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskRerunConfigInputs(
    typing.TypedDict, total=False
):
    artifacts: dict[str, typing.Any]
    parameterValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTemplateMetadata(
    typing.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PointwiseMetricInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1PointwiseMetricInstance
    metricSpec: GoogleCloudAiplatformV1beta1PointwiseMetricSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PointwiseMetricInstance(
    typing.TypedDict, total=False
):
    contentMapInstance: GoogleCloudAiplatformV1beta1ContentMap
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PointwiseMetricResult(typing.TypedDict, total=False):
    customOutput: GoogleCloudAiplatformV1beta1CustomOutput
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PointwiseMetricSpec(typing.TypedDict, total=False):
    customOutputFormatConfig: GoogleCloudAiplatformV1beta1CustomOutputFormatConfig
    metricPromptTemplate: str
    systemInstruction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Port(typing.TypedDict, total=False):
    containerPort: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PostStartupScriptConfig(
    typing.TypedDict, total=False
):
    postStartupScript: str
    postStartupScriptBehavior: typing.Literal[
        "POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED",
        "RUN_ONCE",
        "RUN_EVERY_START",
        "DOWNLOAD_AND_RUN_EVERY_START",
    ]
    postStartupScriptUrl: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PreTunedModel(typing.TypedDict, total=False):
    baseModel: str
    checkpointId: str
    tunedModelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrebuiltVoiceConfig(typing.TypedDict, total=False):
    voiceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredefinedMetricSpec(typing.TypedDict, total=False):
    metricSpecName: str
    metricSpecParameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredefinedSplit(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictLongRunningMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictLongRunningRequest(
    typing.TypedDict, total=False
):
    instances: _list[typing.Any]
    labels: dict[str, typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictLongRunningResponse(
    typing.TypedDict, total=False
):
    generateVideoResponse: GoogleCloudAiplatformV1beta1GenerateVideoResponse

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictRequest(typing.TypedDict, total=False):
    instances: _list[typing.Any]
    labels: dict[str, typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfig(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    enableOtelLogging: bool
    enabled: bool
    errorSamplingRate: float
    requestResponseLoggingSchemaVersion: str
    samplingRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictResponse(typing.TypedDict, total=False):
    deployedModelId: str
    metadata: typing.Any
    model: str
    modelDisplayName: str
    modelVersionId: str
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictSchemata(typing.TypedDict, total=False):
    instanceSchemaUri: str
    parametersSchemaUri: str
    predictionSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PreferenceOptimizationDataStats(
    typing.TypedDict, total=False
):
    droppedExampleIndices: _list[str]
    droppedExampleReasons: _list[str]
    scoreVariancePerExampleDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution
    scoresDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution
    totalBillableTokenCount: str
    tuningDatasetExampleCount: str
    tuningStepCount: str
    userDatasetExamples: _list[GoogleCloudAiplatformV1beta1GeminiPreferenceExample]
    userInputTokenDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution
    userOutputTokenDistribution: GoogleCloudAiplatformV1beta1DatasetDistribution

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PreferenceOptimizationHyperParameters(
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
class GoogleCloudAiplatformV1beta1PreferenceOptimizationSpec(
    typing.TypedDict, total=False
):
    exportLastCheckpointOnly: bool
    hyperParameters: GoogleCloudAiplatformV1beta1PreferenceOptimizationHyperParameters
    trainingDatasetUri: str
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Presets(typing.TypedDict, total=False):
    modality: typing.Literal["MODALITY_UNSPECIFIED", "IMAGE", "TEXT", "TABULAR"]
    query: typing.Literal["PRECISE", "FAST"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrivateEndpoints(typing.TypedDict, total=False):
    explainHttpUri: str
    healthHttpUri: str
    predictHttpUri: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig(
    typing.TypedDict, total=False
):
    enablePrivateServiceConnect: bool
    enableSecurePrivateServiceConnect: bool
    projectAllowlist: _list[str]
    pscAutomationConfigs: _list[GoogleCloudAiplatformV1beta1PSCAutomationConfig]
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Probe(typing.TypedDict, total=False):
    exec: GoogleCloudAiplatformV1beta1ProbeExecAction
    failureThreshold: int
    grpc: GoogleCloudAiplatformV1beta1ProbeGrpcAction
    httpGet: GoogleCloudAiplatformV1beta1ProbeHttpGetAction
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: GoogleCloudAiplatformV1beta1ProbeTcpSocketAction
    timeoutSeconds: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProbeExecAction(typing.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProbeGrpcAction(typing.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProbeHttpGetAction(typing.TypedDict, total=False):
    host: str
    httpHeaders: _list[GoogleCloudAiplatformV1beta1ProbeHttpHeader]
    path: str
    port: int
    scheme: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProbeHttpHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProbeTcpSocketAction(typing.TypedDict, total=False):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProcessDataRequest(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    inputBucketProjectNumber: str
    outputBucketProjectNumber: str
    veoSpec: GoogleCloudAiplatformV1beta1ProcessDataRequestVeoSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ProcessDataRequestVeoSpec(
    typing.TypedDict, total=False
):
    processType: typing.Literal["VEO_V1_AND_V2_DEFAULT", "VEO_V3"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PscAutomatedEndpoints(typing.TypedDict, total=False):
    matchAddress: str
    network: str
    projectId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PscInterfaceConfig(typing.TypedDict, total=False):
    dnsPeeringConfigs: _list[GoogleCloudAiplatformV1beta1DnsPeeringConfig]
    networkAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModel(typing.TypedDict, total=False):
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
    parent: GoogleCloudAiplatformV1beta1PublisherModelParent
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata
    publisherModelTemplate: str
    supportedActions: GoogleCloudAiplatformV1beta1PublisherModelCallToAction
    versionId: str
    versionState: typing.Literal[
        "VERSION_STATE_UNSPECIFIED", "VERSION_STATE_STABLE", "VERSION_STATE_UNSTABLE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToAction(
    typing.TypedDict, total=False
):
    createApplication: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    deploy: GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy
    deployGke: GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeployGke
    multiDeployVertex: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeployVertex
    )
    openEvaluationPipeline: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    openFineTuningPipeline: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    openFineTuningPipelines: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenFineTuningPipelines
    )
    openGenerationAiStudio: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    openGenie: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    openNotebook: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    openNotebooks: GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenNotebooks
    openPromptTuningPipeline: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    requestAccess: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    )
    viewRestApi: GoogleCloudAiplatformV1beta1PublisherModelCallToActionViewRestApi

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy(
    typing.TypedDict, total=False
):
    artifactUri: str
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    deployMetadata: (
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeployDeployMetadata
    )
    deployTaskName: str
    largeModelReference: GoogleCloudAiplatformV1beta1LargeModelReference
    modelDisplayName: str
    publicArtifactUri: str
    sharedResources: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeployDeployMetadata(
    typing.TypedDict, total=False
):
    labels: dict[str, typing.Any]
    sampleRequest: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeployGke(
    typing.TypedDict, total=False
):
    gkeYamlConfigs: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeployVertex(
    typing.TypedDict, total=False
):
    multiDeployVertex: _list[
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenFineTuningPipelines(
    typing.TypedDict, total=False
):
    fineTuningPipelines: _list[
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionOpenNotebooks(
    typing.TypedDict, total=False
):
    notebooks: _list[
        GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences(
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
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionViewRestApi(
    typing.TypedDict, total=False
):
    documentations: _list[GoogleCloudAiplatformV1beta1PublisherModelDocumentation]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelConfig(typing.TypedDict, total=False):
    claudeFeatureConfig: (
        GoogleCloudAiplatformV1beta1PublisherModelConfigClaudeFeatureConfig
    )
    dataSharingEnabledProvider: typing.Literal[
        "MODEL_PROVIDER_UNSPECIFIED", "ANTHROPIC"
    ]
    inferenceEventLoggingConfig: GoogleCloudAiplatformV1beta1InferenceEventLoggingConfig
    loggingConfig: GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelConfigClaudeFeatureConfig(
    typing.TypedDict, total=False
):
    advancedAiEnabled: bool
    cyberVerificationProgramEnabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelDocumentation(
    typing.TypedDict, total=False
):
    content: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelEulaAcceptance(
    typing.TypedDict, total=False
):
    projectNumber: str
    publisherModel: str
    publisherModelEulaAcked: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelParent(typing.TypedDict, total=False):
    displayName: str
    reference: GoogleCloudAiplatformV1beta1PublisherModelResourceReference

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelResourceReference(
    typing.TypedDict, total=False
):
    description: str
    resourceName: str
    uri: str
    useCase: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsMetadata(typing.TypedDict, total=False):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsResponse(
    typing.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeMemoriesRequest(typing.TypedDict, total=False):
    filter: str
    filterGroups: _list[GoogleCloudAiplatformV1beta1MemoryConjunctionFilter]
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PythonPackageSpec(typing.TypedDict, total=False):
    args: _list[str]
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    executorImageUri: str
    packageUris: _list[str]
    pythonModule: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryDeployedModelsResponse(
    typing.TypedDict, total=False
):
    deployedModelRefs: _list[GoogleCloudAiplatformV1beta1DeployedModelRef]
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModel]
    nextPageToken: str
    totalDeployedModelCount: int
    totalEndpointCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryExtensionRequest(typing.TypedDict, total=False):
    contents: _list[GoogleCloudAiplatformV1beta1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryExtensionResponse(typing.TypedDict, total=False):
    failureMessage: str
    steps: _list[GoogleCloudAiplatformV1beta1Content]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryReasoningEngineRequest(
    typing.TypedDict, total=False
):
    classMethod: str
    input: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryReasoningEngineResponse(
    typing.TypedDict, total=False
):
    output: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessInstance
    metricSpec: GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringCorrectnessSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessInstance
    metricSpec: GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringHelpfulnessSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringQualityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1QuestionAnsweringQualityInstance
    metricSpec: GoogleCloudAiplatformV1beta1QuestionAnsweringQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringQualityInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringQualityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringQualitySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceInstance
    metricSpec: GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QuestionAnsweringRelevanceSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagChunk(typing.TypedDict, total=False):
    chunkId: str
    fileId: str
    pageSpan: GoogleCloudAiplatformV1beta1RagChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagChunkPageSpan(typing.TypedDict, total=False):
    firstPage: int
    lastPage: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagContexts(typing.TypedDict, total=False):
    contexts: _list[GoogleCloudAiplatformV1beta1RagContextsContext]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagContextsContext(typing.TypedDict, total=False):
    chunk: GoogleCloudAiplatformV1beta1RagChunk
    distance: float
    score: float
    sourceDisplayName: str
    sourceUri: str
    sparseDistance: float
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagCorpus(typing.TypedDict, total=False):
    corpusStatus: GoogleCloudAiplatformV1beta1CorpusStatus
    corpusTypeConfig: GoogleCloudAiplatformV1beta1RagCorpusCorpusTypeConfig
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    name: str
    ragEmbeddingModelConfig: GoogleCloudAiplatformV1beta1RagEmbeddingModelConfig
    ragFilesCount: int
    ragVectorDbConfig: GoogleCloudAiplatformV1beta1RagVectorDbConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str
    vectorDbConfig: GoogleCloudAiplatformV1beta1RagVectorDbConfig
    vertexAiSearchConfig: GoogleCloudAiplatformV1beta1VertexAiSearchConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagCorpusCorpusTypeConfig(
    typing.TypedDict, total=False
):
    documentCorpus: GoogleCloudAiplatformV1beta1RagCorpusCorpusTypeConfigDocumentCorpus
    memoryCorpus: GoogleCloudAiplatformV1beta1RagCorpusCorpusTypeConfigMemoryCorpus

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagCorpusCorpusTypeConfigDocumentCorpus(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagCorpusCorpusTypeConfigMemoryCorpus(
    typing.TypedDict, total=False
):
    llmParser: GoogleCloudAiplatformV1beta1RagFileParsingConfigLlmParser

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagDataSchema(typing.TypedDict, total=False):
    key: str
    name: str
    schemaDetails: GoogleCloudAiplatformV1beta1RagMetadataSchemaDetails

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagEmbeddingModelConfig(
    typing.TypedDict, total=False
):
    hybridSearchConfig: (
        GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigHybridSearchConfig
    )
    vertexPredictionEndpoint: (
        GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigVertexPredictionEndpoint
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigHybridSearchConfig(
    typing.TypedDict, total=False
):
    denseEmbeddingModelPredictionEndpoint: (
        GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigVertexPredictionEndpoint
    )
    sparseEmbeddingConfig: (
        GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigSparseEmbeddingConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigSparseEmbeddingConfig(
    typing.TypedDict, total=False
):
    bm25: GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigSparseEmbeddingConfigBm25

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigSparseEmbeddingConfigBm25(
    typing.TypedDict, total=False
):
    b: float
    k1: float
    multilingual: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagEmbeddingModelConfigVertexPredictionEndpoint(
    typing.TypedDict, total=False
):
    endpoint: str
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagEngineConfig(typing.TypedDict, total=False):
    name: str
    ragManagedDbConfig: GoogleCloudAiplatformV1beta1RagManagedDbConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFile(typing.TypedDict, total=False):
    createTime: str
    description: str
    directUploadSource: GoogleCloudAiplatformV1beta1DirectUploadSource
    displayName: str
    fileStatus: GoogleCloudAiplatformV1beta1FileStatus
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    googleDriveSource: GoogleCloudAiplatformV1beta1GoogleDriveSource
    jiraSource: GoogleCloudAiplatformV1beta1JiraSource
    name: str
    ragFileType: typing.Literal[
        "RAG_FILE_TYPE_UNSPECIFIED", "RAG_FILE_TYPE_TXT", "RAG_FILE_TYPE_PDF"
    ]
    sharePointSources: GoogleCloudAiplatformV1beta1SharePointSources
    sizeBytes: str
    slackSource: GoogleCloudAiplatformV1beta1SlackSource
    updateTime: str
    userMetadata: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileChunkingConfig(typing.TypedDict, total=False):
    chunkOverlap: int
    chunkSize: int
    fixedLengthChunking: (
        GoogleCloudAiplatformV1beta1RagFileChunkingConfigFixedLengthChunking
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileChunkingConfigFixedLengthChunking(
    typing.TypedDict, total=False
):
    chunkOverlap: int
    chunkSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileMetadataConfig(typing.TypedDict, total=False):
    gcsMetadataSchemaSource: GoogleCloudAiplatformV1beta1GcsSource
    gcsMetadataSource: GoogleCloudAiplatformV1beta1GcsSource
    googleDriveMetadataSchemaSource: GoogleCloudAiplatformV1beta1GoogleDriveSource
    googleDriveMetadataSource: GoogleCloudAiplatformV1beta1GoogleDriveSource
    inlineMetadataSchemaSource: str
    inlineMetadataSource: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileParsingConfig(typing.TypedDict, total=False):
    advancedParser: GoogleCloudAiplatformV1beta1RagFileParsingConfigAdvancedParser
    layoutParser: GoogleCloudAiplatformV1beta1RagFileParsingConfigLayoutParser
    llmParser: GoogleCloudAiplatformV1beta1RagFileParsingConfigLlmParser
    useAdvancedPdfParsing: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileParsingConfigAdvancedParser(
    typing.TypedDict, total=False
):
    useAdvancedPdfParsing: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileParsingConfigLayoutParser(
    typing.TypedDict, total=False
):
    globalMaxParsingRequestsPerMin: int
    maxParsingRequestsPerMin: int
    processorName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileParsingConfigLlmParser(
    typing.TypedDict, total=False
):
    customParsingPrompt: str
    globalMaxParsingRequestsPerMin: int
    maxParsingRequestsPerMin: int
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileTransformationConfig(
    typing.TypedDict, total=False
):
    ragFileChunkingConfig: GoogleCloudAiplatformV1beta1RagFileChunkingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagManagedDbConfig(typing.TypedDict, total=False):
    basic: GoogleCloudAiplatformV1beta1RagManagedDbConfigBasic
    enterprise: GoogleCloudAiplatformV1beta1RagManagedDbConfigEnterprise
    scaled: GoogleCloudAiplatformV1beta1RagManagedDbConfigScaled
    serverless: GoogleCloudAiplatformV1beta1RagManagedDbConfigServerless
    spanner: GoogleCloudAiplatformV1beta1RagManagedDbConfigSpanner
    unprovisioned: GoogleCloudAiplatformV1beta1RagManagedDbConfigUnprovisioned

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagManagedDbConfigBasic(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagManagedDbConfigEnterprise(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagManagedDbConfigScaled(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagManagedDbConfigServerless(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagManagedDbConfigSpanner(
    typing.TypedDict, total=False
):
    basic: GoogleCloudAiplatformV1beta1RagManagedDbConfigBasic
    scaled: GoogleCloudAiplatformV1beta1RagManagedDbConfigScaled
    unprovisioned: GoogleCloudAiplatformV1beta1RagManagedDbConfigUnprovisioned

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagManagedDbConfigUnprovisioned(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagMetadata(typing.TypedDict, total=False):
    name: str
    userSpecifiedMetadata: GoogleCloudAiplatformV1beta1UserSpecifiedMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagMetadataSchemaDetails(
    typing.TypedDict, total=False
):
    granularity: typing.Literal["GRANULARITY_UNSPECIFIED", "GRANULARITY_FILE_LEVEL"]
    listConfig: GoogleCloudAiplatformV1beta1RagMetadataSchemaDetailsListConfig
    searchStrategy: GoogleCloudAiplatformV1beta1RagMetadataSchemaDetailsSearchStrategy
    type: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INTEGER",
        "FLOAT",
        "STRING",
        "DATETIME",
        "BOOLEAN",
        "LIST",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagMetadataSchemaDetailsListConfig(
    typing.TypedDict, total=False
):
    valueSchema: GoogleCloudAiplatformV1beta1RagMetadataSchemaDetails

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagMetadataSchemaDetailsSearchStrategy(
    typing.TypedDict, total=False
):
    searchStrategyType: typing.Literal[
        "SEARCH_STRATEGY_TYPE_UNSPECIFIED", "NO_SEARCH", "EXACT_SEARCH"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagQuery(typing.TypedDict, total=False):
    ragRetrievalConfig: GoogleCloudAiplatformV1beta1RagRetrievalConfig
    ranking: GoogleCloudAiplatformV1beta1RagQueryRanking
    similarityTopK: int
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagQueryRanking(typing.TypedDict, total=False):
    alpha: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfig(typing.TypedDict, total=False):
    filter: GoogleCloudAiplatformV1beta1RagRetrievalConfigFilter
    hybridSearch: GoogleCloudAiplatformV1beta1RagRetrievalConfigHybridSearch
    ranking: GoogleCloudAiplatformV1beta1RagRetrievalConfigRanking
    topK: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigFilter(
    typing.TypedDict, total=False
):
    metadataFilter: str
    vectorDistanceThreshold: float
    vectorSimilarityThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigHybridSearch(
    typing.TypedDict, total=False
):
    alpha: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigRanking(
    typing.TypedDict, total=False
):
    llmRanker: GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingLlmRanker
    rankService: GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingRankService

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingLlmRanker(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingRankService(
    typing.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfig(typing.TypedDict, total=False):
    apiAuth: GoogleCloudAiplatformV1beta1ApiAuth
    pinecone: GoogleCloudAiplatformV1beta1RagVectorDbConfigPinecone
    ragEmbeddingModelConfig: GoogleCloudAiplatformV1beta1RagEmbeddingModelConfig
    ragManagedDb: GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedDb
    ragManagedVertexVectorSearch: (
        GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedVertexVectorSearch
    )
    vertexFeatureStore: GoogleCloudAiplatformV1beta1RagVectorDbConfigVertexFeatureStore
    vertexVectorSearch: GoogleCloudAiplatformV1beta1RagVectorDbConfigVertexVectorSearch
    weaviate: GoogleCloudAiplatformV1beta1RagVectorDbConfigWeaviate

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigPinecone(
    typing.TypedDict, total=False
):
    indexName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedDb(
    typing.TypedDict, total=False
):
    ann: GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedDbANN
    knn: GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedDbKNN

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedDbANN(
    typing.TypedDict, total=False
):
    leafCount: int
    treeDepth: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedDbKNN(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigRagManagedVertexVectorSearch(
    typing.TypedDict, total=False
):
    collectionName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigVertexFeatureStore(
    typing.TypedDict, total=False
):
    featureViewResourceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigVertexVectorSearch(
    typing.TypedDict, total=False
):
    index: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagVectorDbConfigWeaviate(
    typing.TypedDict, total=False
):
    collectionName: str
    httpEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RawOutput(typing.TypedDict, total=False):
    rawOutput: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RawPredictRequest(typing.TypedDict, total=False):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RayLogsSpec(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RayMetricSpec(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RaySpec(typing.TypedDict, total=False):
    headNodeResourcePoolId: str
    imageUri: str
    nfsMounts: _list[GoogleCloudAiplatformV1beta1NfsMount]
    rayLogsSpec: GoogleCloudAiplatformV1beta1RayLogsSpec
    rayMetricSpec: GoogleCloudAiplatformV1beta1RayMetricSpec
    resourcePoolImages: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesRequest(
    typing.TypedDict, total=False
):
    entityId: str
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponse(
    typing.TypedDict, total=False
):
    entityView: GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityView
    header: GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHeader

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityView(
    typing.TypedDict, total=False
):
    data: _list[GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData]
    entityId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData(
    typing.TypedDict, total=False
):
    value: GoogleCloudAiplatformV1beta1FeatureValue
    values: GoogleCloudAiplatformV1beta1FeatureValueList

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor(
    typing.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHeader(
    typing.TypedDict, total=False
):
    entityType: str
    featureDescriptors: _list[
        GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadIndexDatapointsRequest(
    typing.TypedDict, total=False
):
    deployedIndexId: str
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadIndexDatapointsResponse(
    typing.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1beta1IndexDatapoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardBlobDataResponse(
    typing.TypedDict, total=False
):
    blobs: _list[GoogleCloudAiplatformV1beta1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardSizeResponse(
    typing.TypedDict, total=False
):
    storageSizeByte: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardTimeSeriesDataResponse(
    typing.TypedDict, total=False
):
    timeSeriesData: GoogleCloudAiplatformV1beta1TimeSeriesData

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponse(
    typing.TypedDict, total=False
):
    monthlyUsageData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerMonthUsageData(
    typing.TypedDict, total=False
):
    userUsageData: _list[
        GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerUserUsageData
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerUserUsageData(
    typing.TypedDict, total=False
):
    username: str
    viewCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngine(typing.TypedDict, total=False):
    contextSpec: GoogleCloudAiplatformV1beta1ReasoningEngineContextSpec
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    spec: GoogleCloudAiplatformV1beta1ReasoningEngineSpec
    trafficConfig: GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineContextSpec(
    typing.TypedDict, total=False
):
    memoryBankConfig: (
        GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfig(
    typing.TypedDict, total=False
):
    customizationConfigs: _list[
        GoogleCloudAiplatformV1beta1MemoryBankCustomizationConfig
    ]
    disableMemoryRevisions: bool
    generationConfig: GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigGenerationConfig
    similaritySearchConfig: GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig
    structuredMemoryConfigs: _list[GoogleCloudAiplatformV1beta1StructuredMemoryConfig]
    ttlConfig: (
        GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigTtlConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigGenerationConfig(
    typing.TypedDict, total=False
):
    generationTriggerConfig: GoogleCloudAiplatformV1beta1MemoryGenerationTriggerConfig
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig(
    typing.TypedDict, total=False
):
    embeddingModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigTtlConfig(
    typing.TypedDict, total=False
):
    defaultTtl: str
    granularTtlConfig: GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig
    memoryRevisionDefaultTtl: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig(
    typing.TypedDict, total=False
):
    createTtl: str
    generateCreatedTtl: str
    generateUpdatedTtl: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineRuntimeRevision(
    typing.TypedDict, total=False
):
    createTime: str
    name: str
    spec: GoogleCloudAiplatformV1beta1ReasoningEngineSpec
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpec(typing.TypedDict, total=False):
    agentCard: dict[str, typing.Any]
    agentFramework: str
    buildSpec: GoogleCloudAiplatformV1beta1ReasoningEngineSpecBuildSpec
    classMethods: _list[dict[str, typing.Any]]
    containerSpec: GoogleCloudAiplatformV1beta1ReasoningEngineSpecContainerSpec
    deploymentSpec: GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpec
    effectiveIdentity: str
    identityType: typing.Literal[
        "IDENTITY_TYPE_UNSPECIFIED", "SERVICE_ACCOUNT", "AGENT_IDENTITY"
    ]
    packageSpec: GoogleCloudAiplatformV1beta1ReasoningEngineSpecPackageSpec
    serviceAccount: str
    sourceCodeSpec: GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecBuildSpec(
    typing.TypedDict, total=False
):
    serviceAccount: str
    workerPool: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecContainerSpec(
    typing.TypedDict, total=False
):
    imageUri: str
    port: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpec(
    typing.TypedDict, total=False
):
    agentGatewayConfig: (
        GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpecAgentGatewayConfig
    )
    agentServerMode: typing.Literal[
        "AGENT_SERVER_MODE_UNSPECIFIED", "STABLE", "EXPERIMENTAL"
    ]
    containerConcurrency: int
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    keepAliveProbe: GoogleCloudAiplatformV1beta1KeepAliveProbe
    maxInstances: int
    minInstances: int
    pscInterfaceConfig: GoogleCloudAiplatformV1beta1PscInterfaceConfig
    resourceLimits: dict[str, typing.Any]
    secretEnv: _list[GoogleCloudAiplatformV1beta1SecretEnvVar]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpecAgentGatewayConfig(
    typing.TypedDict, total=False
):
    agentToAnywhereConfig: GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig
    clientToAgentConfig: GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig(
    typing.TypedDict, total=False
):
    agentGateway: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig(
    typing.TypedDict, total=False
):
    agentGateway: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecPackageSpec(
    typing.TypedDict, total=False
):
    dependencyFilesGcsUri: str
    pickleObjectGcsUri: str
    pythonVersion: str
    requirementsGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpec(
    typing.TypedDict, total=False
):
    agentConfigSource: (
        GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecAgentConfigSource
    )
    developerConnectSource: GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource
    imageSpec: GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecImageSpec
    inlineSource: (
        GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecInlineSource
    )
    pythonSpec: GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecPythonSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecAgentConfigSource(
    typing.TypedDict, total=False
):
    adkConfig: GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig
    inlineSource: (
        GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecInlineSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig(
    typing.TypedDict, total=False
):
    jsonConfig: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig(
    typing.TypedDict, total=False
):
    dir: str
    gitRepositoryLink: str
    revision: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource(
    typing.TypedDict, total=False
):
    config: GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecImageSpec(
    typing.TypedDict, total=False
):
    buildArgs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecInlineSource(
    typing.TypedDict, total=False
):
    sourceArchive: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineSpecSourceCodeSpecPythonSpec(
    typing.TypedDict, total=False
):
    entrypointModule: str
    entrypointObject: str
    requirementsFile: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfig(
    typing.TypedDict, total=False
):
    trafficSplitAlwaysLatest: (
        GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest
    )
    trafficSplitManual: (
        GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfigTrafficSplitManual
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfigTrafficSplitManual(
    typing.TypedDict, total=False
):
    targets: _list[
        GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfigTrafficSplitManualTarget
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineTrafficConfigTrafficSplitManualTarget(
    typing.TypedDict, total=False
):
    percent: int
    runtimeRevisionName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RebaseTunedModelRequest(
    typing.TypedDict, total=False
):
    artifactDestination: GoogleCloudAiplatformV1beta1GcsDestination
    deployToSameEndpoint: bool
    tunedModelRef: GoogleCloudAiplatformV1beta1TunedModelRef
    tuningJob: GoogleCloudAiplatformV1beta1TuningJob

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RebootPersistentResourceOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RebootPersistentResourceRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RecommendSpecRequest(typing.TypedDict, total=False):
    checkMachineAvailability: bool
    checkUserQuota: bool
    gcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RecommendSpecResponse(typing.TypedDict, total=False):
    baseModel: str
    recommendations: _list[
        GoogleCloudAiplatformV1beta1RecommendSpecResponseRecommendation
    ]
    specs: _list[
        GoogleCloudAiplatformV1beta1RecommendSpecResponseMachineAndModelContainerSpec
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RecommendSpecResponseMachineAndModelContainerSpec(
    typing.TypedDict, total=False
):
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RecommendSpecResponseRecommendation(
    typing.TypedDict, total=False
):
    region: str
    spec: GoogleCloudAiplatformV1beta1RecommendSpecResponseMachineAndModelContainerSpec
    userQuotaState: typing.Literal[
        "QUOTA_STATE_UNSPECIFIED",
        "QUOTA_STATE_USER_HAS_QUOTA",
        "QUOTA_STATE_NO_USER_QUOTA",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningAutoraterScorer(
    typing.TypedDict, total=False
):
    autoraterConfig: GoogleCloudAiplatformV1beta1AutoraterConfig
    autoraterPrompt: str
    autoraterResponseParseConfig: (
        GoogleCloudAiplatformV1beta1ReinforcementTuningParseResponseConfig
    )
    exactMatchScorer: (
        GoogleCloudAiplatformV1beta1ReinforcementTuningAutoraterScorerExactMatchScorer
    )
    parsedResponseConversionScorer: GoogleCloudAiplatformV1beta1ReinforcementTuningAutoraterScorerParsedResponseConversionScorer

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningAutoraterScorerExactMatchScorer(
    typing.TypedDict, total=False
):
    correctAnswerReward: float
    expression: str
    wrongAnswerReward: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningAutoraterScorerParsedResponseConversionScorer(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningCloudRunRewardScorer(
    typing.TypedDict, total=False
):
    cloudRunUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningCodeExecutionRewardScorer(
    typing.TypedDict, total=False
):
    pythonCodeSnippet: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningExample(
    typing.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    references: dict[str, typing.Any]
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningHyperParameters(
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
    batchSize: int
    checkpointInterval: int
    epochCount: str
    evaluateInterval: int
    learningRateMultiplier: float
    maxOutputTokens: int
    samplesPerPrompt: int
    stepCount: str
    thinkingBudget: int
    thinkingLevel: typing.Literal[
        "REINFORCEMENT_TUNING_THINKING_LEVEL_UNSPECIFIED",
        "MINIMAL",
        "LOW",
        "MEDIUM",
        "HIGH",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningParseResponseConfig(
    typing.TypedDict, total=False
):
    parseType: typing.Literal[
        "RESPONSE_PARSE_TYPE_UNSPECIFIED", "IDENTITY", "REGEX_EXTRACT"
    ]
    regexExtractExpression: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningRewardInfo(
    typing.TypedDict, total=False
):
    errorStatus: GoogleRpcStatus
    reward: float
    userRequestedAuxInfo: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningSpec(
    typing.TypedDict, total=False
):
    compositeRewardConfig: (
        GoogleCloudAiplatformV1beta1CompositeReinforcementTuningRewardConfig
    )
    hyperParameters: GoogleCloudAiplatformV1beta1ReinforcementTuningHyperParameters
    singleRewardConfig: (
        GoogleCloudAiplatformV1beta1SingleReinforcementTuningRewardConfig
    )
    trainingDatasetUri: str
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningStringMatchRewardScorer(
    typing.TypedDict, total=False
):
    correctAnswerReward: float
    jsonMatchExpression: GoogleCloudAiplatformV1beta1ReinforcementTuningStringMatchRewardScorerJsonMatchExpression
    stringMatchExpression: GoogleCloudAiplatformV1beta1ReinforcementTuningStringMatchRewardScorerStringMatchExpression
    wrongAnswerReward: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningStringMatchRewardScorerJsonMatchExpression(
    typing.TypedDict, total=False
):
    keyName: str
    valueStringMatchExpression: GoogleCloudAiplatformV1beta1ReinforcementTuningStringMatchRewardScorerStringMatchExpression

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningStringMatchRewardScorerStringMatchExpression(
    typing.TypedDict, total=False
):
    expression: str
    matchOperation: typing.Literal[
        "MATCH_OPERATION_UNSPECIFIED", "REGEX_CONTAINS", "PARTIAL_MATCH", "EXACT_MATCH"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReinforcementTuningUserDatasetExamples(
    typing.TypedDict, total=False
):
    userDatasetExamples: _list[GoogleCloudAiplatformV1beta1ReinforcementTuningExample]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveContextChildrenRequest(
    typing.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveContextChildrenResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveDatapointsRequest(
    typing.TypedDict, total=False
):
    datapointIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveDatapointsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveExamplesRequest(typing.TypedDict, total=False):
    exampleIds: _list[str]
    storedContentsExampleFilter: GoogleCloudAiplatformV1beta1StoredContentsExampleFilter

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveExamplesResponse(typing.TypedDict, total=False):
    exampleIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReplicatedVoiceConfig(typing.TypedDict, total=False):
    mimeType: str
    voiceSampleAudio: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportExecutionEventRequest(
    typing.TypedDict, total=False
):
    eventType: typing.Literal["EVENT_TYPE_UNSPECIFIED", "ACTIVE", "DONE", "FAILED"]
    status: GoogleRpcStatus
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportExecutionEventResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportRuntimeEventRequest(
    typing.TypedDict, total=False
):
    eventDetails: dict[str, typing.Any]
    eventType: typing.Literal["EVENT_TYPE_UNSPECIFIED", "HEARTBEAT", "IDLE"]
    internalOsServiceStateInstance: _list[
        GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance
    ]
    internalOsServiceStateInstances: _list[
        GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance
    ]
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportRuntimeEventResponse(
    typing.TypedDict, total=False
):
    idleShutdownMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReservationAffinity(typing.TypedDict, total=False):
    key: str
    reservationAffinityType: typing.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcePool(typing.TypedDict, total=False):
    autoscalingSpec: GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec
    diskSpec: GoogleCloudAiplatformV1beta1DiskSpec
    id: str
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    replicaCount: str
    usedReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec(
    typing.TypedDict, total=False
):
    maxReplicaCount: str
    minReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourceRuntime(typing.TypedDict, total=False):
    accessUris: dict[str, typing.Any]
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourceRuntimeSpec(typing.TypedDict, total=False):
    raySpec: GoogleCloudAiplatformV1beta1RaySpec
    serviceAccountSpec: GoogleCloudAiplatformV1beta1ServiceAccountSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcesConsumed(typing.TypedDict, total=False):
    replicaHours: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResponseFormat(typing.TypedDict, total=False):
    audio: GoogleCloudAiplatformV1beta1AudioResponseFormat
    image: GoogleCloudAiplatformV1beta1ImageResponseFormat
    text: GoogleCloudAiplatformV1beta1TextResponseFormat
    video: GoogleCloudAiplatformV1beta1VideoResponseFormat

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RestoreDatasetVersionOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResumeModelDeploymentMonitoringJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResumeSandboxEnvironmentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResumeScheduleRequest(typing.TypedDict, total=False):
    catchUp: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Retrieval(typing.TypedDict, total=False):
    disableAttribution: bool
    externalApi: GoogleCloudAiplatformV1beta1ExternalApi
    vertexAiSearch: GoogleCloudAiplatformV1beta1VertexAISearch
    vertexRagStore: GoogleCloudAiplatformV1beta1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrievalConfig(typing.TypedDict, total=False):
    languageCode: str
    latLng: GoogleTypeLatLng

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrievalMetadata(typing.TypedDict, total=False):
    googleSearchDynamicRetrievalScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveContextsRequest(
    typing.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1beta1RagQuery
    vertexRagStore: GoogleCloudAiplatformV1beta1RetrieveContextsRequestVertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveContextsRequestVertexRagStore(
    typing.TypedDict, total=False
):
    ragCorpora: _list[str]
    ragResources: _list[
        GoogleCloudAiplatformV1beta1RetrieveContextsRequestVertexRagStoreRagResource
    ]
    vectorDistanceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveContextsRequestVertexRagStoreRagResource(
    typing.TypedDict, total=False
):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveContextsResponse(
    typing.TypedDict, total=False
):
    contexts: GoogleCloudAiplatformV1beta1RagContexts

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveExpressProjectResponse(
    typing.TypedDict, total=False
):
    expressProject: GoogleCloudAiplatformV1beta1ExpressProject

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveMemoriesRequest(
    typing.TypedDict, total=False
):
    filter: str
    filterGroups: _list[GoogleCloudAiplatformV1beta1MemoryConjunctionFilter]
    memoryTypes: _list[
        typing.Literal[
            "MEMORY_TYPE_UNSPECIFIED",
            "NATURAL_LANGUAGE_COLLECTION",
            "STRUCTURED_PROFILE",
        ]
    ]
    scope: dict[str, typing.Any]
    similaritySearchParams: (
        GoogleCloudAiplatformV1beta1RetrieveMemoriesRequestSimilaritySearchParams
    )
    simpleRetrievalParams: (
        GoogleCloudAiplatformV1beta1RetrieveMemoriesRequestSimpleRetrievalParams
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveMemoriesRequestSimilaritySearchParams(
    typing.TypedDict, total=False
):
    searchQuery: str
    topK: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveMemoriesRequestSimpleRetrievalParams(
    typing.TypedDict, total=False
):
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveMemoriesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    retrievedMemories: _list[
        GoogleCloudAiplatformV1beta1RetrieveMemoriesResponseRetrievedMemory
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveMemoriesResponseRetrievedMemory(
    typing.TypedDict, total=False
):
    distance: float
    memory: GoogleCloudAiplatformV1beta1Memory

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveProfilesRequest(
    typing.TypedDict, total=False
):
    scope: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveProfilesResponse(
    typing.TypedDict, total=False
):
    profiles: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveSkillsResponse(typing.TypedDict, total=False):
    retrievedSkills: _list[
        GoogleCloudAiplatformV1beta1RetrieveSkillsResponseRetrievedSkill
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveSkillsResponseRetrievedSkill(
    typing.TypedDict, total=False
):
    description: str
    skillName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RollbackMemoryRequest(typing.TypedDict, total=False):
    targetRevisionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RolloutOptions(typing.TypedDict, total=False):
    maxSurgePercentage: int
    maxSurgeReplicas: int
    maxUnavailablePercentage: int
    maxUnavailableReplicas: int
    previousDeployedModel: str
    revisionNumber: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RougeInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1beta1RougeInstance]
    metricSpec: GoogleCloudAiplatformV1beta1RougeSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RougeInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RougeMetricValue(typing.TypedDict, total=False):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RougeResults(typing.TypedDict, total=False):
    rougeMetricValues: _list[GoogleCloudAiplatformV1beta1RougeMetricValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RougeSpec(typing.TypedDict, total=False):
    rougeType: str
    splitSummaries: bool
    useStemmer: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Rubric(typing.TypedDict, total=False):
    content: GoogleCloudAiplatformV1beta1RubricContent
    importance: typing.Literal["IMPORTANCE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW"]
    rubricId: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingInstance
    metricSpec: GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingInstance(
    typing.TypedDict, total=False
):
    jsonInstance: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingResult(
    typing.TypedDict, total=False
):
    rubricCritiqueResults: _list[GoogleCloudAiplatformV1beta1RubricCritiqueResult]
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricBasedInstructionFollowingSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricContent(typing.TypedDict, total=False):
    property: GoogleCloudAiplatformV1beta1RubricContentProperty

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricContentProperty(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricCritiqueResult(typing.TypedDict, total=False):
    rubric: str
    verdict: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricGenerationSpec(typing.TypedDict, total=False):
    modelConfig: GoogleCloudAiplatformV1beta1AutoraterConfig
    promptTemplate: str
    rubricContentType: typing.Literal[
        "RUBRIC_CONTENT_TYPE_UNSPECIFIED",
        "PROPERTY",
        "NL_QUESTION_ANSWER",
        "PYTHON_CODE_ASSERTION",
    ]
    rubricTypeOntology: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricGroup(typing.TypedDict, total=False):
    displayName: str
    groupId: str
    rubrics: _list[GoogleCloudAiplatformV1beta1Rubric]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RubricVerdict(typing.TypedDict, total=False):
    evaluatedRubric: GoogleCloudAiplatformV1beta1Rubric
    reasoning: str
    verdict: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RuntimeArtifact(typing.TypedDict, total=False):
    customProperties: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    properties: dict[str, typing.Any]
    type: GoogleCloudAiplatformV1beta1ArtifactTypeSchema
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RuntimeConfig(typing.TypedDict, total=False):
    codeInterpreterRuntimeConfig: (
        GoogleCloudAiplatformV1beta1RuntimeConfigCodeInterpreterRuntimeConfig
    )
    defaultParams: dict[str, typing.Any]
    vertexAiSearchRuntimeConfig: (
        GoogleCloudAiplatformV1beta1RuntimeConfigVertexAISearchRuntimeConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RuntimeConfigCodeInterpreterRuntimeConfig(
    typing.TypedDict, total=False
):
    fileInputGcsBucket: str
    fileOutputGcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RuntimeConfigVertexAISearchRuntimeConfig(
    typing.TypedDict, total=False
):
    engineId: str
    servingConfigName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SafetyInput(typing.TypedDict, total=False):
    instance: GoogleCloudAiplatformV1beta1SafetyInstance
    metricSpec: GoogleCloudAiplatformV1beta1SafetySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SafetyInstance(typing.TypedDict, total=False):
    prediction: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SafetyRating(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1SafetyResult(typing.TypedDict, total=False):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SafetySetting(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1SafetySpec(typing.TypedDict, total=False):
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SampleConfig(typing.TypedDict, total=False):
    followingBatchSamplePercentage: int
    initialBatchSamplePercentage: int
    sampleStrategy: typing.Literal["SAMPLE_STRATEGY_UNSPECIFIED", "UNCERTAINTY"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SampledShapleyAttribution(
    typing.TypedDict, total=False
):
    pathCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SamplingStrategy(typing.TypedDict, total=False):
    randomSampleConfig: GoogleCloudAiplatformV1beta1SamplingStrategyRandomSampleConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SamplingStrategyRandomSampleConfig(
    typing.TypedDict, total=False
):
    sampleRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironment(typing.TypedDict, total=False):
    connectionInfo: GoogleCloudAiplatformV1beta1SandboxEnvironmentConnectionInfo
    createTime: str
    displayName: str
    expireTime: str
    latestSandboxEnvironmentSnapshot: str
    name: str
    owner: str
    sandboxEnvironmentSnapshot: str
    sandboxEnvironmentTemplate: str
    spec: GoogleCloudAiplatformV1beta1SandboxEnvironmentSpec
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
class GoogleCloudAiplatformV1beta1SandboxEnvironmentConnectionInfo(
    typing.TypedDict, total=False
):
    loadBalancerHostname: str
    loadBalancerIp: str
    routingToken: str
    sandboxInternalIp: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentSnapshot(
    typing.TypedDict, total=False
):
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
class GoogleCloudAiplatformV1beta1SandboxEnvironmentSpec(typing.TypedDict, total=False):
    codeExecutionEnvironment: (
        GoogleCloudAiplatformV1beta1SandboxEnvironmentSpecCodeExecutionEnvironment
    )
    computerUseEnvironment: (
        GoogleCloudAiplatformV1beta1SandboxEnvironmentSpecComputerUseEnvironment
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentSpecCodeExecutionEnvironment(
    typing.TypedDict, total=False
):
    codeLanguage: typing.Literal[
        "LANGUAGE_UNSPECIFIED", "LANGUAGE_PYTHON", "LANGUAGE_JAVASCRIPT"
    ]
    machineConfig: typing.Literal[
        "MACHINE_CONFIG_UNSPECIFIED", "MACHINE_CONFIG_VCPU4_RAM4GIB"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentSpecComputerUseEnvironment(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplate(
    typing.TypedDict, total=False
):
    createTime: str
    customContainerEnvironment: (
        GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateCustomContainerEnvironment
    )
    defaultContainerEnvironment: GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateDefaultContainerEnvironment
    displayName: str
    egressControlConfig: (
        GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateEgressControlConfig
    )
    ingressControlConfig: GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig
    name: str
    state: typing.Literal[
        "UNSPECIFIED", "PROVISIONING", "ACTIVE", "DEPROVISIONING", "DELETED", "FAILED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateCustomContainerEnvironment(
    typing.TypedDict, total=False
):
    customContainerSpec: (
        GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateCustomContainerSpec
    )
    ports: _list[GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateNetworkPort]
    resources: (
        GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateResourceRequirements
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateCustomContainerSpec(
    typing.TypedDict, total=False
):
    imageUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateDefaultContainerEnvironment(
    typing.TypedDict, total=False
):
    defaultContainerCategory: typing.Literal[
        "DEFAULT_CONTAINER_CATEGORY_UNSPECIFIED",
        "DEFAULT_CONTAINER_CATEGORY_COMPUTER_USE",
        "DEFAULT_CONTAINER_CATEGORY_SHELL_SANDBOX",
    ]
    resources: (
        GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateResourceRequirements
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateEgressControlConfig(
    typing.TypedDict, total=False
):
    customerVpcNetwork: str
    dnsPeeringConfigs: _list[
        GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateEgressControlConfigDnsPeeringConfig
    ]
    internetAccess: bool
    networkAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateEgressControlConfigDnsPeeringConfig(
    typing.TypedDict, total=False
):
    domain: str
    targetNetwork: str
    targetProject: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateNetworkPort(
    typing.TypedDict, total=False
):
    port: int
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "TCP", "UDP"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SandboxEnvironmentTemplateResourceRequirements(
    typing.TypedDict, total=False
):
    limits: dict[str, typing.Any]
    requests: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SavedQuery(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1Scalar(typing.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Schedule(typing.TypedDict, total=False):
    allowQueueing: bool
    catchUp: bool
    createModelMonitoringJobRequest: (
        GoogleCloudAiplatformV1beta1CreateModelMonitoringJobRequest
    )
    createNotebookExecutionJobRequest: (
        GoogleCloudAiplatformV1beta1CreateNotebookExecutionJobRequest
    )
    createPipelineJobRequest: GoogleCloudAiplatformV1beta1CreatePipelineJobRequest
    createTime: str
    cron: str
    displayName: str
    endTime: str
    lastPauseTime: str
    lastResumeTime: str
    lastScheduledRunResponse: GoogleCloudAiplatformV1beta1ScheduleRunResponse
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
class GoogleCloudAiplatformV1beta1ScheduleConfig(typing.TypedDict, total=False):
    cron: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ScheduleRunResponse(typing.TypedDict, total=False):
    runResponse: str
    scheduledRunTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Scheduling(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1Schema(typing.TypedDict, total=False):
    additionalProperties: typing.Any
    anyOf: _list[GoogleCloudAiplatformV1beta1Schema]
    default: typing.Any
    defs: dict[str, typing.Any]
    description: str
    enum: _list[str]
    example: typing.Any
    format: str
    items: GoogleCloudAiplatformV1beta1Schema
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
class GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor(
    typing.TypedDict, total=False
):
    color: GoogleTypeColor
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageBoundingBoxAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageClassificationAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageDataItem(typing.TypedDict, total=False):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageDatasetMetadata(
    typing.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotation(
    typing.TypedDict, total=False
):
    maskAnnotation: (
        GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationMaskAnnotation
    )
    polygonAnnotation: (
        GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolygonAnnotation
    )
    polylineAnnotation: (
        GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolylineAnnotation
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationMaskAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecColors: _list[GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor]
    maskGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolygonAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1beta1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolylineAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1beta1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics(
    typing.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetrics(
    typing.TypedDict, total=False
):
    auPrc: float
    auRoc: float
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: (
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    )
    logLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: (
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    )
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
    typing.TypedDict, total=False
):
    annotationSpecs: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef
    ]
    rows: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef(
    typing.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsForecastingEvaluationMetrics(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    observedQuantile: float
    quantile: float
    scaledPinballLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsGeneralTextGenerationEvaluationMetrics(
    typing.TypedDict, total=False
):
    bleu: float
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageObjectDetectionEvaluationMetrics(
    typing.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetrics(
    typing.TypedDict, total=False
):
    confidenceMetricsEntries: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: (
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    )
    diceScoreCoefficient: float
    iouScore: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsPairwiseTextGenerationEvaluationMetrics(
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
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsQuestionAnsweringEvaluationMetrics(
    typing.TypedDict, total=False
):
    exactMatch: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsRegressionEvaluationMetrics(
    typing.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsSummarizationEvaluationMetrics(
    typing.TypedDict, total=False
):
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetrics(
    typing.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: (
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextSentimentEvaluationMetrics(
    typing.TypedDict, total=False
):
    confusionMatrix: (
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    )
    f1Score: float
    linearKappa: float
    meanAbsoluteError: float
    meanSquaredError: float
    precision: float
    quadraticKappa: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    boundingBoxIou: float
    confidenceThreshold: float
    mismatchRate: float
    trackingPrecision: float
    trackingRecall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetrics(
    typing.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics
    ]
    meanAveragePrecision: float
    precisionWindowLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionRecognitionMetrics(
    typing.TypedDict, total=False
):
    evaluatedActionCount: int
    videoActionMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetrics
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoObjectTrackingMetrics(
    typing.TypedDict, total=False
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
class GoogleCloudAiplatformV1beta1SchemaMultimodalDatasetMetadata(
    typing.TypedDict, total=False
):
    geminiRequestReadConfig: GoogleCloudAiplatformV1beta1GeminiRequestReadConfig
    inputConfig: GoogleCloudAiplatformV1beta1SchemaMultimodalDatasetMetadataMultimodalDatasetInputConfig
    keyColumnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaMultimodalDatasetMetadataBigQuerySource(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaMultimodalDatasetMetadataMultimodalDatasetInputConfig(
    typing.TypedDict, total=False
):
    bigquerySource: (
        GoogleCloudAiplatformV1beta1SchemaMultimodalDatasetMetadataBigQuerySource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageClassificationPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageObjectDetectionPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageSegmentationPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextClassificationPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextExtractionPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    key: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextSentimentPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoActionRecognitionPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoClassificationPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoObjectTrackingPredictionInstance(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsGroundingConfig(
    typing.TypedDict, total=False
):
    disableAttribution: bool
    sources: _list[
        GoogleCloudAiplatformV1beta1SchemaPredictParamsGroundingConfigSourceEntry
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsGroundingConfigSourceEntry(
    typing.TypedDict, total=False
):
    enterpriseDatastore: str
    inlineContext: str
    type: typing.Literal[
        "UNSPECIFIED", "WEB", "ENTERPRISE", "VERTEX_AI_SEARCH", "INLINE"
    ]
    vertexAiSearchDatastore: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageClassificationPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageObjectDetectionPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageSegmentationPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoActionRecognitionPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoClassificationPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    oneSecIntervalClassification: bool
    segmentClassification: bool
    shotClassification: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoObjectTrackingPredictionParams(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    minBoundingBoxSize: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionClassificationPredictionResult(
    typing.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionImageObjectDetectionPredictionResult(
    typing.TypedDict, total=False
):
    bboxes: _list[_list[typing.Any]]
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionImageSegmentationPredictionResult(
    typing.TypedDict, total=False
):
    categoryMask: str
    confidenceMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTabularClassificationPredictionResult(
    typing.TypedDict, total=False
):
    classes: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTabularRegressionPredictionResult(
    typing.TypedDict, total=False
):
    lowerBound: float
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    upperBound: float
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTextExtractionPredictionResult(
    typing.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]
    textSegmentEndOffsets: _list[str]
    textSegmentStartOffsets: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTextSentimentPredictionResult(
    typing.TypedDict, total=False
):
    sentiment: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTftFeatureImportance(
    typing.TypedDict, total=False
):
    attributeColumns: _list[str]
    attributeWeights: _list[float]
    contextColumns: _list[str]
    contextWeights: _list[float]
    horizonColumns: _list[str]
    horizonWeights: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTimeSeriesForecastingPredictionResult(
    typing.TypedDict, total=False
):
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    tftFeatureImportance: (
        GoogleCloudAiplatformV1beta1SchemaPredictPredictionTftFeatureImportance
    )
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoActionRecognitionPredictionResult(
    typing.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoClassificationPredictionResult(
    typing.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResult(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    timeOffset: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictionResult(typing.TypedDict, total=False):
    error: GoogleCloudAiplatformV1beta1SchemaPredictionResultError
    instance: dict[str, typing.Any]
    key: str
    prediction: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictionResultError(
    typing.TypedDict, total=False
):
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
class GoogleCloudAiplatformV1beta1SchemaPromptApiSchema(typing.TypedDict, total=False):
    apiSchemaVersion: str
    executions: _list[GoogleCloudAiplatformV1beta1SchemaPromptInstancePromptExecution]
    multimodalPrompt: GoogleCloudAiplatformV1beta1SchemaPromptSpecMultimodalPrompt
    structuredPrompt: GoogleCloudAiplatformV1beta1SchemaPromptSpecStructuredPrompt
    translationPrompt: GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationPrompt

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptInstancePromptExecution(
    typing.TypedDict, total=False
):
    arguments: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptInstanceVariableValue(
    typing.TypedDict, total=False
):
    partList: GoogleCloudAiplatformV1beta1SchemaPromptSpecPartList

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecAppBuilderData(
    typing.TypedDict, total=False
):
    codeRepositoryState: str
    framework: typing.Literal["FRAMEWORK_UNSPECIFIED", "REACT", "ANGULAR"]
    linkedResources: _list[
        GoogleCloudAiplatformV1beta1SchemaPromptSpecAppBuilderDataLinkedResource
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecAppBuilderDataLinkedResource(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecInteractionData(
    typing.TypedDict, total=False
):
    interactionIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecMultimodalPrompt(
    typing.TypedDict, total=False
):
    promptMessage: GoogleCloudAiplatformV1beta1SchemaPromptSpecPromptMessage

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecPartList(
    typing.TypedDict, total=False
):
    parts: _list[GoogleCloudAiplatformV1beta1Part]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecPromptMessage(
    typing.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    model: str
    safetySettings: _list[GoogleCloudAiplatformV1beta1SafetySetting]
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    toolConfig: GoogleCloudAiplatformV1beta1ToolConfig
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecReferenceSentencePair(
    typing.TypedDict, total=False
):
    sourceSentence: str
    targetSentence: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecReferenceSentencePairList(
    typing.TypedDict, total=False
):
    referenceSentencePairs: _list[
        GoogleCloudAiplatformV1beta1SchemaPromptSpecReferenceSentencePair
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecStructuredPrompt(
    typing.TypedDict, total=False
):
    appBuilderData: GoogleCloudAiplatformV1beta1SchemaPromptSpecAppBuilderData
    context: GoogleCloudAiplatformV1beta1Content
    examples: _list[GoogleCloudAiplatformV1beta1SchemaPromptSpecPartList]
    infillPrefix: str
    infillSuffix: str
    inputPrefixes: _list[str]
    interactionData: GoogleCloudAiplatformV1beta1SchemaPromptSpecInteractionData
    outputPrefixes: _list[str]
    predictionInputs: _list[GoogleCloudAiplatformV1beta1SchemaPromptSpecPartList]
    promptMessage: GoogleCloudAiplatformV1beta1SchemaPromptSpecPromptMessage

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationExample(
    typing.TypedDict, total=False
):
    referenceSentencePairLists: _list[
        GoogleCloudAiplatformV1beta1SchemaPromptSpecReferenceSentencePairList
    ]
    referenceSentencesFileInputs: _list[
        GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationSentenceFileInput
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationFileInputSource(
    typing.TypedDict, total=False
):
    content: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationGcsInputSource(
    typing.TypedDict, total=False
):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationOption(
    typing.TypedDict, total=False
):
    numberOfShots: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationPrompt(
    typing.TypedDict, total=False
):
    example: GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationExample
    option: GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationOption
    promptMessage: GoogleCloudAiplatformV1beta1SchemaPromptSpecPromptMessage
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationSentenceFileInput(
    typing.TypedDict, total=False
):
    fileInputSource: (
        GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationFileInputSource
    )
    gcsInputSource: (
        GoogleCloudAiplatformV1beta1SchemaPromptSpecTranslationGcsInputSource
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadata(
    typing.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataInputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataBigQuerySource(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataGcsSource(
    typing.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataInputConfig(
    typing.TypedDict, total=False
):
    bigquerySource: (
        GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataBigQuerySource
    )
    gcsSource: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextClassificationAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextDataItem(typing.TypedDict, total=False):
    gcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextDatasetMetadata(
    typing.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextExtractionAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    textSegment: GoogleCloudAiplatformV1beta1SchemaTextSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextPromptDatasetMetadata(
    typing.TypedDict, total=False
):
    candidateCount: str
    gcsUri: str
    groundingConfig: GoogleCloudAiplatformV1beta1SchemaPredictParamsGroundingConfig
    hasPromptVariable: bool
    logprobs: bool
    maxOutputTokens: str
    note: str
    promptApiSchema: GoogleCloudAiplatformV1beta1SchemaPromptApiSchema
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
class GoogleCloudAiplatformV1beta1SchemaTextSegment(typing.TypedDict, total=False):
    content: str
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSentimentAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    sentiment: int
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSentimentSavedQueryMetadata(
    typing.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSegment(typing.TypedDict, total=False):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadata(
    typing.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataInputConfig
    timeColumn: str
    timeSeriesIdentifierColumn: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataBigQuerySource(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataGcsSource(
    typing.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataInputConfig(
    typing.TypedDict, total=False
):
    bigquerySource: (
        GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataBigQuerySource
    )
    gcsSource: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecasting(
    typing.TypedDict, total=False
):
    inputs: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputs
    )
    metadata: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputs(
    typing.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity
    enableProbabilisticInference: bool
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    )
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
    typing.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation(
    typing.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassification(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs(
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
    tunableParameter: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata(
    typing.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetection(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs(
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
    tunableParameter: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata(
    typing.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentation(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs(
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
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata(
    typing.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTables(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputs
    metadata: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputs(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassification(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs(
    typing.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtraction(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentiment(
    typing.TypedDict, total=False
):
    inputs: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs(
    typing.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognition(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs(
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
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassification(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs(
    typing.TypedDict, total=False
):
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTracking(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs(
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
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter(
    typing.TypedDict, total=False
):
    checkpointName: str
    datasetConfig: dict[str, typing.Any]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trainerConfig: dict[str, typing.Any]
    trainerType: typing.Literal[
        "TRAINER_TYPE_UNSPECIFIED", "AUTOML_TRAINER", "MODEL_GARDEN_TRAINER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomJobMetadata(
    typing.TypedDict, total=False
):
    backingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomTask(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1CustomJobSpec
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig(
    typing.TypedDict, total=False
):
    destinationBigqueryUri: str
    overrideExistingTable: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig(
    typing.TypedDict, total=False
):
    groupColumns: _list[str]
    groupTemporalTotalWeight: float
    groupTotalWeight: float
    temporalTotalWeight: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata(
    typing.TypedDict, total=False
):
    backingHyperparameterTuningJob: str
    bestTrialBackingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec(
    typing.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxTrialCount: int
    parallelTrialCount: int
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningTask(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecasting(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs(
    typing.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    )
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
    typing.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation(
    typing.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecasting(
    typing.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputs
    metadata: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputs(
    typing.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: (
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    )
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
    typing.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformation(
    typing.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation(
    typing.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation(
    typing.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingMetadata(
    typing.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig(
    typing.TypedDict, total=False
):
    column: str
    maxCount: str
    strideLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVertex(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoActionRecognitionAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1beta1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoClassificationAnnotation(
    typing.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1beta1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoDataItem(typing.TypedDict, total=False):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoDatasetMetadata(
    typing.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoObjectTrackingAnnotation(
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
class GoogleCloudAiplatformV1beta1SchemaVisualInspectionClassificationLabelSavedQueryMetadata(
    typing.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVisualInspectionMaskSavedQueryMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchDataItemsResponse(
    typing.TypedDict, total=False
):
    dataItemViews: _list[GoogleCloudAiplatformV1beta1DataItemView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchEntryPoint(typing.TypedDict, total=False):
    renderedContent: str
    sdkBlob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchExamplesRequest(typing.TypedDict, total=False):
    storedContentsExampleParameters: (
        GoogleCloudAiplatformV1beta1StoredContentsExampleParameters
    )
    topK: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchExamplesResponse(typing.TypedDict, total=False):
    results: _list[GoogleCloudAiplatformV1beta1SearchExamplesResponseSimilarExample]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchExamplesResponseSimilarExample(
    typing.TypedDict, total=False
):
    example: GoogleCloudAiplatformV1beta1Example
    similarityScore: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchFeaturesResponse(typing.TypedDict, total=False):
    features: _list[GoogleCloudAiplatformV1beta1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchMigratableResourcesRequest(
    typing.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponse(
    typing.TypedDict, total=False
):
    migratableResources: _list[GoogleCloudAiplatformV1beta1MigratableResource]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequest(
    typing.TypedDict, total=False
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
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponse(
    typing.TypedDict, total=False
):
    monitoringStats: _list[GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsRequest(
    typing.TypedDict, total=False
):
    alertTimeInterval: GoogleTypeInterval
    modelMonitoringJob: str
    objectiveType: str
    pageSize: int
    pageToken: str
    statsName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsResponse(
    typing.TypedDict, total=False
):
    modelMonitoringAlerts: _list[GoogleCloudAiplatformV1beta1ModelMonitoringAlert]
    nextPageToken: str
    totalNumberAlerts: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsFilter(
    typing.TypedDict, total=False
):
    tabularStatsFilter: (
        GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsFilterTabularStatsFilter
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsFilterTabularStatsFilter(
    typing.TypedDict, total=False
):
    algorithm: str
    modelMonitoringJob: str
    modelMonitoringSchedule: str
    objectiveType: str
    statsName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsRequest(
    typing.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    statsFilter: GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsFilter
    timeInterval: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsResponse(
    typing.TypedDict, total=False
):
    monitoringStats: _list[GoogleCloudAiplatformV1beta1ModelMonitoringStats]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchNearestEntitiesRequest(
    typing.TypedDict, total=False
):
    query: GoogleCloudAiplatformV1beta1NearestNeighborQuery
    returnFullEntity: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchNearestEntitiesResponse(
    typing.TypedDict, total=False
):
    nearestNeighbors: GoogleCloudAiplatformV1beta1NearestNeighbors

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SecretEnvVar(typing.TypedDict, total=False):
    name: str
    secretRef: GoogleCloudAiplatformV1beta1SecretRef

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SecretRef(typing.TypedDict, total=False):
    secret: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Segment(typing.TypedDict, total=False):
    endIndex: int
    partIndex: int
    startIndex: int
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SemanticGovernancePolicy(
    typing.TypedDict, total=False
):
    agent: str
    agentIdentity: str
    createTime: str
    description: str
    displayName: str
    etag: str
    mcpTools: _list[GoogleCloudAiplatformV1beta1SemanticGovernancePolicyMcpTool]
    name: str
    naturalLanguageConstraint: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SemanticGovernancePolicyEngine(
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
class GoogleCloudAiplatformV1beta1SemanticGovernancePolicyMcpTool(
    typing.TypedDict, total=False
):
    mcpServer: str
    tools: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ServiceAccountSpec(typing.TypedDict, total=False):
    enableCustomServiceAccount: bool
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ServingProfile(typing.TypedDict, total=False):
    cmekConfig: GoogleCloudAiplatformV1beta1ServingProfileCmekConfig
    createTime: str
    description: str
    displayName: str
    name: str
    scope: typing.Literal[
        "SERVING_PROFILE_SCOPE_UNSPECIFIED",
        "GEMINI_LIVE",
        "INTERACTIONS_API",
        "RESPONSE_API",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ServingProfileCmekConfig(
    typing.TypedDict, total=False
):
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Session(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1SessionEvent(typing.TypedDict, total=False):
    actions: GoogleCloudAiplatformV1beta1EventActions
    author: str
    content: GoogleCloudAiplatformV1beta1Content
    errorCode: str
    errorMessage: str
    eventMetadata: GoogleCloudAiplatformV1beta1EventMetadata
    invocationId: str
    name: str
    rawEvent: dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SetPublisherModelConfigRequest(
    typing.TypedDict, total=False
):
    publisherModelConfig: GoogleCloudAiplatformV1beta1PublisherModelConfig
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SharePointSources(typing.TypedDict, total=False):
    sharePointSources: _list[
        GoogleCloudAiplatformV1beta1SharePointSourcesSharePointSource
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SharePointSourcesSharePointSource(
    typing.TypedDict, total=False
):
    clientId: str
    clientSecret: GoogleCloudAiplatformV1beta1ApiAuthApiKeyConfig
    driveId: str
    driveName: str
    fileId: str
    sharepointFolderId: str
    sharepointFolderPath: str
    sharepointSiteName: str
    tenantId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ShieldedVmConfig(typing.TypedDict, total=False):
    enableSecureBoot: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SignUpRequest(typing.TypedDict, total=False):
    getDefaultApiKey: bool
    region: str
    tosAccepted: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SingleReinforcementTuningRewardConfig(
    typing.TypedDict, total=False
):
    autoraterScorer: GoogleCloudAiplatformV1beta1ReinforcementTuningAutoraterScorer
    cloudRunRewardScorer: (
        GoogleCloudAiplatformV1beta1ReinforcementTuningCloudRunRewardScorer
    )
    codeExecutionRewardScorer: (
        GoogleCloudAiplatformV1beta1ReinforcementTuningCodeExecutionRewardScorer
    )
    parseResponseConfig: (
        GoogleCloudAiplatformV1beta1ReinforcementTuningParseResponseConfig
    )
    rewardName: str
    stringMatchRewardScorer: (
        GoogleCloudAiplatformV1beta1ReinforcementTuningStringMatchRewardScorer
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Skill(typing.TypedDict, total=False):
    compatibility: str
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    license: str
    name: str
    sha256: str
    skillSource: typing.Literal["SKILL_SOURCE_UNSPECIFIED", "USER", "SYSTEM"]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "FAILED", "DELETING"
    ]
    updateTime: str
    zippedFilesystem: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SkillRevision(typing.TypedDict, total=False):
    createTime: str
    name: str
    skill: GoogleCloudAiplatformV1beta1Skill
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "FAILED", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SlackSource(typing.TypedDict, total=False):
    channels: _list[GoogleCloudAiplatformV1beta1SlackSourceSlackChannels]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SlackSourceSlackChannels(
    typing.TypedDict, total=False
):
    apiKeyConfig: GoogleCloudAiplatformV1beta1ApiAuthApiKeyConfig
    channels: _list[GoogleCloudAiplatformV1beta1SlackSourceSlackChannelsSlackChannel]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SlackSourceSlackChannelsSlackChannel(
    typing.TypedDict, total=False
):
    channelId: str
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SmoothGradConfig(typing.TypedDict, total=False):
    featureNoiseSigma: GoogleCloudAiplatformV1beta1FeatureNoiseSigma
    noiseSigma: float
    noisySampleCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeakerVoiceConfig(typing.TypedDict, total=False):
    speaker: str
    voiceConfig: GoogleCloudAiplatformV1beta1VoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpecialistPool(typing.TypedDict, total=False):
    displayName: str
    name: str
    pendingDataLabelingJobs: _list[str]
    specialistManagerEmails: _list[str]
    specialistManagersCount: int
    specialistWorkerEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeculativeDecodingSpec(
    typing.TypedDict, total=False
):
    draftModelSpeculation: (
        GoogleCloudAiplatformV1beta1SpeculativeDecodingSpecDraftModelSpeculation
    )
    ngramSpeculation: (
        GoogleCloudAiplatformV1beta1SpeculativeDecodingSpecNgramSpeculation
    )
    speculativeTokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeculativeDecodingSpecDraftModelSpeculation(
    typing.TypedDict, total=False
):
    draftModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeculativeDecodingSpecNgramSpeculation(
    typing.TypedDict, total=False
):
    ngramSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeechConfig(typing.TypedDict, total=False):
    languageCode: str
    multiSpeakerVoiceConfig: GoogleCloudAiplatformV1beta1MultiSpeakerVoiceConfig
    voiceConfig: GoogleCloudAiplatformV1beta1VoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StartNotebookRuntimeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StartNotebookRuntimeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StopNotebookRuntimeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StopTrialRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StoredContentsExample(typing.TypedDict, total=False):
    contentsExample: GoogleCloudAiplatformV1beta1ContentsExample
    searchKey: str
    searchKeyGenerationMethod: (
        GoogleCloudAiplatformV1beta1StoredContentsExampleSearchKeyGenerationMethod
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StoredContentsExampleFilter(
    typing.TypedDict, total=False
):
    functionNames: GoogleCloudAiplatformV1beta1ExamplesArrayFilter
    searchKeys: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StoredContentsExampleParameters(
    typing.TypedDict, total=False
):
    contentSearchKey: (
        GoogleCloudAiplatformV1beta1StoredContentsExampleParametersContentSearchKey
    )
    functionNames: GoogleCloudAiplatformV1beta1ExamplesArrayFilter
    searchKey: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StoredContentsExampleParametersContentSearchKey(
    typing.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    searchKeyGenerationMethod: (
        GoogleCloudAiplatformV1beta1StoredContentsExampleSearchKeyGenerationMethod
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StoredContentsExampleSearchKeyGenerationMethod(
    typing.TypedDict, total=False
):
    lastEntry: GoogleCloudAiplatformV1beta1StoredContentsExampleSearchKeyGenerationMethodLastEntry

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StoredContentsExampleSearchKeyGenerationMethodLastEntry(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StratifiedSplit(typing.TypedDict, total=False):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamQueryReasoningEngineRequest(
    typing.TypedDict, total=False
):
    classMethod: str
    input: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamRawPredictRequest(
    typing.TypedDict, total=False
):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingFetchFeatureValuesRequest(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal[
        "FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED", "KEY_VALUE", "PROTO_STRUCT"
    ]
    dataKeys: _list[GoogleCloudAiplatformV1beta1FeatureViewDataKey]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingFetchFeatureValuesResponse(
    typing.TypedDict, total=False
):
    data: _list[GoogleCloudAiplatformV1beta1FetchFeatureValuesResponse]
    dataKeysWithError: _list[GoogleCloudAiplatformV1beta1FeatureViewDataKey]
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingPredictRequest(
    typing.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingPredictResponse(
    typing.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingReadFeatureValuesRequest(
    typing.TypedDict, total=False
):
    entityIds: _list[str]
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StringArray(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StructFieldValue(typing.TypedDict, total=False):
    name: str
    value: GoogleCloudAiplatformV1beta1FeatureValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StructValue(typing.TypedDict, total=False):
    values: _list[GoogleCloudAiplatformV1beta1StructFieldValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StructuredMemoryConfig(typing.TypedDict, total=False):
    schemaConfigs: _list[GoogleCloudAiplatformV1beta1StructuredMemoryConfigSchemaConfig]
    scopeKeys: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StructuredMemoryConfigSchemaConfig(
    typing.TypedDict, total=False
):
    id: str
    jsonSchema: typing.Any
    memoryType: typing.Literal[
        "MEMORY_TYPE_UNSPECIFIED", "NATURAL_LANGUAGE_COLLECTION", "STRUCTURED_PROFILE"
    ]
    schema: GoogleCloudAiplatformV1beta1Schema

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Study(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    inactiveReason: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpec(typing.TypedDict, total=False):
    algorithm: typing.Literal["ALGORITHM_UNSPECIFIED", "GRID_SEARCH", "RANDOM_SEARCH"]
    convexAutomatedStoppingSpec: (
        GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec
    )
    convexStopConfig: GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig
    decayCurveStoppingSpec: (
        GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec
    )
    measurementSelectionType: typing.Literal[
        "MEASUREMENT_SELECTION_TYPE_UNSPECIFIED", "LAST_MEASUREMENT", "BEST_MEASUREMENT"
    ]
    medianAutomatedStoppingSpec: (
        GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec
    )
    metrics: _list[GoogleCloudAiplatformV1beta1StudySpecMetricSpec]
    observationNoise: typing.Literal["OBSERVATION_NOISE_UNSPECIFIED", "LOW", "HIGH"]
    parameters: _list[GoogleCloudAiplatformV1beta1StudySpecParameterSpec]
    studyStoppingConfig: GoogleCloudAiplatformV1beta1StudySpecStudyStoppingConfig
    transferLearningConfig: GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec(
    typing.TypedDict, total=False
):
    learningRateParameterName: str
    maxStepCount: str
    minMeasurementCount: str
    minStepCount: str
    updateAllStoppedTrials: bool
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig(
    typing.TypedDict, total=False
):
    autoregressiveOrder: str
    learningRateParameterName: str
    maxNumSteps: str
    minNumSteps: str
    useSeconds: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec(
    typing.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec(
    typing.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMetricSpec(typing.TypedDict, total=False):
    goal: typing.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str
    safetyConfig: GoogleCloudAiplatformV1beta1StudySpecMetricSpecSafetyMetricConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMetricSpecSafetyMetricConfig(
    typing.TypedDict, total=False
):
    desiredMinSafeTrialsFraction: float
    safetyThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpec(typing.TypedDict, total=False):
    categoricalValueSpec: (
        GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec
    )
    conditionalParameterSpecs: _list[
        GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec
    ]
    discreteValueSpec: (
        GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec
    )
    doubleValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec
    integerValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec
    parameterId: str
    scaleType: typing.Literal[
        "SCALE_TYPE_UNSPECIFIED",
        "UNIT_LINEAR_SCALE",
        "UNIT_LOG_SCALE",
        "UNIT_REVERSE_LOG_SCALE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec(
    typing.TypedDict, total=False
):
    parameterSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpec
    parentCategoricalValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition
    parentDiscreteValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition
    parentIntValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecIntValueCondition

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition(
    typing.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecIntValueCondition(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: float
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: float
    maxValue: float
    minValue: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec(
    typing.TypedDict, total=False
):
    defaultValue: str
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecStudyStoppingConfig(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    disableTransferLearning: bool
    priorStudyNames: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudyTimeConstraint(typing.TypedDict, total=False):
    endTime: str
    maxDuration: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsMetadata(typing.TypedDict, total=False):
    clientId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsRequest(typing.TypedDict, total=False):
    clientId: str
    contexts: _list[GoogleCloudAiplatformV1beta1TrialContext]
    suggestionCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsResponse(typing.TypedDict, total=False):
    endTime: str
    startTime: str
    studyState: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"]
    trials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationHelpfulnessInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1SummarizationHelpfulnessInstance
    metricSpec: GoogleCloudAiplatformV1beta1SummarizationHelpfulnessSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationHelpfulnessInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationHelpfulnessResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationHelpfulnessSpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationQualityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1SummarizationQualityInstance
    metricSpec: GoogleCloudAiplatformV1beta1SummarizationQualitySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationQualityInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationQualityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationQualitySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationVerbosityInput(
    typing.TypedDict, total=False
):
    instance: GoogleCloudAiplatformV1beta1SummarizationVerbosityInstance
    metricSpec: GoogleCloudAiplatformV1beta1SummarizationVerbositySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationVerbosityInstance(
    typing.TypedDict, total=False
):
    context: str
    instruction: str
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationVerbosityResult(
    typing.TypedDict, total=False
):
    confidence: float
    explanation: str
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummarizationVerbositySpec(
    typing.TypedDict, total=False
):
    useReference: bool
    version: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SummaryMetrics(typing.TypedDict, total=False):
    failedItems: int
    metrics: dict[str, typing.Any]
    totalItems: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SupervisedHyperParameters(
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
    batchSize: str
    epochCount: str
    learningRate: float
    learningRateMultiplier: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SupervisedTuningDataStats(
    typing.TypedDict, total=False
):
    droppedExampleReasons: _list[str]
    totalBillableCharacterCount: str
    totalBillableTokenCount: str
    totalTruncatedExampleCount: str
    totalTuningCharacterCount: str
    truncatedExampleIndices: _list[str]
    tuningDatasetExampleCount: str
    tuningStepCount: str
    userDatasetExamples: _list[GoogleCloudAiplatformV1beta1Content]
    userInputTokenDistribution: (
        GoogleCloudAiplatformV1beta1SupervisedTuningDatasetDistribution
    )
    userMessagePerExampleDistribution: (
        GoogleCloudAiplatformV1beta1SupervisedTuningDatasetDistribution
    )
    userOutputTokenDistribution: (
        GoogleCloudAiplatformV1beta1SupervisedTuningDatasetDistribution
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SupervisedTuningDatasetDistribution(
    typing.TypedDict, total=False
):
    billableSum: str
    buckets: _list[
        GoogleCloudAiplatformV1beta1SupervisedTuningDatasetDistributionDatasetBucket
    ]
    max: float
    mean: float
    median: float
    min: float
    p5: float
    p95: float
    sum: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SupervisedTuningDatasetDistributionDatasetBucket(
    typing.TypedDict, total=False
):
    count: float
    left: float
    right: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SupervisedTuningSpec(typing.TypedDict, total=False):
    evaluationConfig: GoogleCloudAiplatformV1beta1EvaluationConfig
    exportLastCheckpointOnly: bool
    hyperParameters: GoogleCloudAiplatformV1beta1SupervisedHyperParameters
    trainingDatasetUri: str
    tuningMode: typing.Literal[
        "TUNING_MODE_UNSPECIFIED", "TUNING_MODE_FULL", "TUNING_MODE_PEFT_ADAPTER"
    ]
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuspendOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuspendOnlineEvaluatorRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SyncFeatureViewRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SyncFeatureViewResponse(
    typing.TypedDict, total=False
):
    featureViewSync: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SyntheticExample(typing.TypedDict, total=False):
    fields: _list[GoogleCloudAiplatformV1beta1SyntheticField]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SyntheticField(typing.TypedDict, total=False):
    content: GoogleCloudAiplatformV1beta1Content
    fieldName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TFRecordDestination(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskArtifact(typing.TypedDict, total=False):
    artifactId: str
    description: str
    displayName: str
    metadata: dict[str, typing.Any]
    parts: _list[GoogleCloudAiplatformV1beta1Part]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskArtifactChange(typing.TypedDict, total=False):
    addedArtifacts: _list[GoogleCloudAiplatformV1beta1TaskArtifact]
    deletedArtifactIds: _list[str]
    updatedArtifacts: _list[GoogleCloudAiplatformV1beta1TaskArtifact]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskDescriptionStrategy(
    typing.TypedDict, total=False
):
    taskDescription: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskEvent(typing.TypedDict, total=False):
    createTime: str
    eventData: GoogleCloudAiplatformV1beta1TaskEventData
    eventSequenceNumber: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskEventData(typing.TypedDict, total=False):
    metadataChange: GoogleCloudAiplatformV1beta1TaskMetadataChange
    outputChange: GoogleCloudAiplatformV1beta1TaskOutputChange
    stateChange: GoogleCloudAiplatformV1beta1TaskStateChange
    statusDetailsChange: GoogleCloudAiplatformV1beta1TaskStatusDetailsChange

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskMessage(typing.TypedDict, total=False):
    messageId: str
    metadata: dict[str, typing.Any]
    parts: _list[GoogleCloudAiplatformV1beta1Part]
    role: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskMetadataChange(typing.TypedDict, total=False):
    newMetadata: dict[str, typing.Any]
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskOutput(typing.TypedDict, total=False):
    artifacts: _list[GoogleCloudAiplatformV1beta1TaskArtifact]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskOutputChange(typing.TypedDict, total=False):
    taskArtifactChange: GoogleCloudAiplatformV1beta1TaskArtifactChange

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskStateChange(typing.TypedDict, total=False):
    newState: typing.Literal[
        "STATE_UNSPECIFIED",
        "SUBMITTED",
        "WORKING",
        "COMPLETED",
        "CANCELLED",
        "FAILED",
        "REJECTED",
        "INPUT_REQUIRED",
        "AUTH_REQUIRED",
        "PAUSED",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskStatusDetails(typing.TypedDict, total=False):
    taskMessage: GoogleCloudAiplatformV1beta1TaskMessage

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TaskStatusDetailsChange(
    typing.TypedDict, total=False
):
    newTaskStatus: GoogleCloudAiplatformV1beta1TaskStatusDetails

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tensor(typing.TypedDict, total=False):
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
    listVal: _list[GoogleCloudAiplatformV1beta1Tensor]
    shape: _list[str]
    stringVal: _list[str]
    structVal: dict[str, typing.Any]
    tensorVal: str
    uint64Val: _list[str]
    uintVal: _list[int]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tensorboard(typing.TypedDict, total=False):
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
    satisfiesPzi: bool
    satisfiesPzs: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardBlob(typing.TypedDict, total=False):
    data: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardBlobSequence(
    typing.TypedDict, total=False
):
    values: _list[GoogleCloudAiplatformV1beta1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardExperiment(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    source: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardRun(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTensor(typing.TypedDict, total=False):
    value: str
    versionNumber: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTimeSeries(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    metadata: GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata
    name: str
    pluginData: str
    pluginName: str
    updateTime: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata(
    typing.TypedDict, total=False
):
    maxBlobSequenceLength: str
    maxStep: str
    maxWallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TextResponseFormat(typing.TypedDict, total=False):
    mimeType: typing.Literal["MIME_TYPE_UNSPECIFIED", "APPLICATION_JSON", "TEXT_PLAIN"]
    schema: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ThresholdConfig(typing.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimeSeriesData(typing.TypedDict, total=False):
    tensorboardTimeSeriesId: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]
    values: _list[GoogleCloudAiplatformV1beta1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimeSeriesDataPoint(typing.TypedDict, total=False):
    blobs: GoogleCloudAiplatformV1beta1TensorboardBlobSequence
    scalar: GoogleCloudAiplatformV1beta1Scalar
    step: str
    tensor: GoogleCloudAiplatformV1beta1TensorboardTensor
    wallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimestampSplit(typing.TypedDict, total=False):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TokensInfo(typing.TypedDict, total=False):
    role: str
    tokenIds: _list[str]
    tokens: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tool(typing.TypedDict, total=False):
    codeExecution: GoogleCloudAiplatformV1beta1ToolCodeExecution
    computerUse: GoogleCloudAiplatformV1beta1ToolComputerUse
    enterpriseWebSearch: GoogleCloudAiplatformV1beta1EnterpriseWebSearch
    exaAiSearch: GoogleCloudAiplatformV1beta1ToolExaAiSearch
    functionDeclarations: _list[GoogleCloudAiplatformV1beta1FunctionDeclaration]
    googleMaps: GoogleCloudAiplatformV1beta1GoogleMaps
    googleSearch: GoogleCloudAiplatformV1beta1ToolGoogleSearch
    googleSearchRetrieval: GoogleCloudAiplatformV1beta1GoogleSearchRetrieval
    parallelAiSearch: GoogleCloudAiplatformV1beta1ToolParallelAiSearch
    retrieval: GoogleCloudAiplatformV1beta1Retrieval
    urlContext: GoogleCloudAiplatformV1beta1UrlContext

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCall(typing.TypedDict, total=False):
    toolInput: str
    toolName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCallValidInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1beta1ToolCallValidInstance]
    metricSpec: GoogleCloudAiplatformV1beta1ToolCallValidSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCallValidInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCallValidMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCallValidResults(typing.TypedDict, total=False):
    toolCallValidMetricValues: _list[
        GoogleCloudAiplatformV1beta1ToolCallValidMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCallValidSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCodeExecution(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolComputerUse(typing.TypedDict, total=False):
    enablePromptInjectionDetection: bool
    environment: typing.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_BROWSER",
        "ENVIRONMENT_MOBILE",
        "ENVIRONMENT_DESKTOP",
    ]
    excludedPredefinedFunctions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolConfig(typing.TypedDict, total=False):
    functionCallingConfig: GoogleCloudAiplatformV1beta1FunctionCallingConfig
    retrievalConfig: GoogleCloudAiplatformV1beta1RetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolExaAiSearch(typing.TypedDict, total=False):
    apiKey: str
    customConfigs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolGoogleSearch(typing.TypedDict, total=False):
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
    searchTypes: GoogleCloudAiplatformV1beta1ToolGoogleSearchSearchTypes

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolGoogleSearchImageSearch(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolGoogleSearchSearchTypes(
    typing.TypedDict, total=False
):
    imageSearch: GoogleCloudAiplatformV1beta1ToolGoogleSearchImageSearch
    webSearch: GoogleCloudAiplatformV1beta1ToolGoogleSearchWebSearch

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolGoogleSearchWebSearch(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolNameMatchInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1beta1ToolNameMatchInstance]
    metricSpec: GoogleCloudAiplatformV1beta1ToolNameMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolNameMatchInstance(typing.TypedDict, total=False):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolNameMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolNameMatchResults(typing.TypedDict, total=False):
    toolNameMatchMetricValues: _list[
        GoogleCloudAiplatformV1beta1ToolNameMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolNameMatchSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParallelAiSearch(typing.TypedDict, total=False):
    apiKey: str
    customConfigs: dict[str, typing.Any]
    enableDataRetention: bool
    enableZeroDataRetention: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKVMatchInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1beta1ToolParameterKVMatchInstance]
    metricSpec: GoogleCloudAiplatformV1beta1ToolParameterKVMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKVMatchInstance(
    typing.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKVMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKVMatchResults(
    typing.TypedDict, total=False
):
    toolParameterKvMatchMetricValues: _list[
        GoogleCloudAiplatformV1beta1ToolParameterKVMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKVMatchSpec(
    typing.TypedDict, total=False
):
    useStrictStringMatch: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKeyMatchInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1beta1ToolParameterKeyMatchInstance]
    metricSpec: GoogleCloudAiplatformV1beta1ToolParameterKeyMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKeyMatchInstance(
    typing.TypedDict, total=False
):
    prediction: str
    reference: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKeyMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKeyMatchResults(
    typing.TypedDict, total=False
):
    toolParameterKeyMatchMetricValues: _list[
        GoogleCloudAiplatformV1beta1ToolParameterKeyMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolParameterKeyMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolUseExample(typing.TypedDict, total=False):
    displayName: str
    extensionOperation: GoogleCloudAiplatformV1beta1ToolUseExampleExtensionOperation
    functionName: str
    query: str
    requestParams: dict[str, typing.Any]
    responseParams: dict[str, typing.Any]
    responseSummary: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolUseExampleExtensionOperation(
    typing.TypedDict, total=False
):
    extension: str
    operationId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrainingConfig(typing.TypedDict, total=False):
    timeoutTrainingMilliHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrainingPipeline(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1Trajectory(typing.TypedDict, total=False):
    toolCalls: _list[GoogleCloudAiplatformV1beta1ToolCall]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchInstance]
    metricSpec: GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1beta1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1beta1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchResults(
    typing.TypedDict, total=False
):
    trajectoryAnyOrderMatchMetricValues: _list[
        GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryAnyOrderMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryExactMatchInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1beta1TrajectoryExactMatchInstance]
    metricSpec: GoogleCloudAiplatformV1beta1TrajectoryExactMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryExactMatchInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1beta1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1beta1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryExactMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryExactMatchResults(
    typing.TypedDict, total=False
):
    trajectoryExactMatchMetricValues: _list[
        GoogleCloudAiplatformV1beta1TrajectoryExactMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryExactMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchInstance]
    metricSpec: GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1beta1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1beta1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchResults(
    typing.TypedDict, total=False
):
    trajectoryInOrderMatchMetricValues: _list[
        GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryInOrderMatchSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryPrecisionInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1beta1TrajectoryPrecisionInstance]
    metricSpec: GoogleCloudAiplatformV1beta1TrajectoryPrecisionSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryPrecisionInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1beta1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1beta1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryPrecisionMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryPrecisionResults(
    typing.TypedDict, total=False
):
    trajectoryPrecisionMetricValues: _list[
        GoogleCloudAiplatformV1beta1TrajectoryPrecisionMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryPrecisionSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryRecallInput(typing.TypedDict, total=False):
    instances: _list[GoogleCloudAiplatformV1beta1TrajectoryRecallInstance]
    metricSpec: GoogleCloudAiplatformV1beta1TrajectoryRecallSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryRecallInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1beta1Trajectory
    referenceTrajectory: GoogleCloudAiplatformV1beta1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryRecallMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryRecallResults(
    typing.TypedDict, total=False
):
    trajectoryRecallMetricValues: _list[
        GoogleCloudAiplatformV1beta1TrajectoryRecallMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectoryRecallSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectorySingleToolUseInput(
    typing.TypedDict, total=False
):
    instances: _list[GoogleCloudAiplatformV1beta1TrajectorySingleToolUseInstance]
    metricSpec: GoogleCloudAiplatformV1beta1TrajectorySingleToolUseSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectorySingleToolUseInstance(
    typing.TypedDict, total=False
):
    predictedTrajectory: GoogleCloudAiplatformV1beta1Trajectory

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectorySingleToolUseMetricValue(
    typing.TypedDict, total=False
):
    score: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectorySingleToolUseResults(
    typing.TypedDict, total=False
):
    trajectorySingleToolUseMetricValues: _list[
        GoogleCloudAiplatformV1beta1TrajectorySingleToolUseMetricValue
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrajectorySingleToolUseSpec(
    typing.TypedDict, total=False
):
    toolName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Transcription(typing.TypedDict, total=False):
    finished: bool
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Trial(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1TrialContext(typing.TypedDict, total=False):
    description: str
    parameters: _list[GoogleCloudAiplatformV1beta1TrialParameter]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrialParameter(typing.TypedDict, total=False):
    parameterId: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TunedModel(typing.TypedDict, total=False):
    checkpoints: _list[GoogleCloudAiplatformV1beta1TunedModelCheckpoint]
    endpoint: str
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TunedModelCheckpoint(typing.TypedDict, total=False):
    checkpointId: str
    endpoint: str
    epoch: str
    step: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TunedModelRef(typing.TypedDict, total=False):
    pipelineJob: str
    tunedModel: str
    tuningJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TuningDataStats(typing.TypedDict, total=False):
    distillationDataStats: GoogleCloudAiplatformV1beta1DistillationDataStats
    preferenceOptimizationDataStats: (
        GoogleCloudAiplatformV1beta1PreferenceOptimizationDataStats
    )
    reinforcementTuningDataStats: GoogleCloudAiplatformV1beta1DatasetStats
    supervisedTuningDataStats: GoogleCloudAiplatformV1beta1SupervisedTuningDataStats

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TuningJob(typing.TypedDict, total=False):
    baseModel: str
    createTime: str
    customBaseModel: str
    description: str
    distillationSpec: GoogleCloudAiplatformV1beta1DistillationSpec
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    evaluateDatasetRuns: _list[GoogleCloudAiplatformV1beta1EvaluateDatasetRun]
    experiment: str
    fullFineTuningSpec: GoogleCloudAiplatformV1beta1FullFineTuningSpec
    labels: dict[str, typing.Any]
    name: str
    outputUri: str
    partnerModelTuningSpec: GoogleCloudAiplatformV1beta1PartnerModelTuningSpec
    pipelineJob: str
    preTunedModel: GoogleCloudAiplatformV1beta1PreTunedModel
    preferenceOptimizationSpec: GoogleCloudAiplatformV1beta1PreferenceOptimizationSpec
    reinforcementTuningSpec: GoogleCloudAiplatformV1beta1ReinforcementTuningSpec
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
    supervisedTuningSpec: GoogleCloudAiplatformV1beta1SupervisedTuningSpec
    tunedModel: GoogleCloudAiplatformV1beta1TunedModel
    tunedModelDisplayName: str
    tuningDataStats: GoogleCloudAiplatformV1beta1TuningDataStats
    tuningJobMetadata: GoogleCloudAiplatformV1beta1TuningJobMetadata
    tuningJobState: typing.Literal[
        "TUNING_JOB_STATE_UNSPECIFIED",
        "TUNING_JOB_STATE_WAITING_FOR_QUOTA",
        "TUNING_JOB_STATE_PROCESSING_DATASET",
        "TUNING_JOB_STATE_WAITING_FOR_CAPACITY",
        "TUNING_JOB_STATE_TUNING",
        "TUNING_JOB_STATE_POST_PROCESSING",
    ]
    updateTime: str
    veoLoraTuningSpec: GoogleCloudAiplatformV1beta1VeoLoraTuningSpec
    veoTuningSpec: GoogleCloudAiplatformV1beta1VeoTuningSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TuningJobMetadata(typing.TypedDict, total=False):
    completedEpochCount: str
    completedStepCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexRequest(typing.TypedDict, total=False):
    deployedIndexId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelRequest(typing.TypedDict, total=False):
    deployedModelId: str
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeploySolverOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UnmanagedContainerModel(
    typing.TypedDict, total=False
):
    artifactUri: str
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateDeploymentResourcePoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateEndpointLongRunningRequest(
    typing.TypedDict, total=False
):
    endpoint: GoogleCloudAiplatformV1beta1Endpoint

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetRequest(
    typing.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1beta1Examples

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureGroupOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureOnlineStoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeatureViewOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeaturestoreOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateIndexOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: (
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateModelDeploymentMonitoringJobOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateModelMonitorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateOnlineEvaluatorOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdatePersistentResourceOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateSpecialistPoolOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    specialistPool: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateTensorboardOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpgradeNotebookRuntimeOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpgradeNotebookRuntimeRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelOperationMetadata(
    typing.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelRequest(typing.TypedDict, total=False):
    model: GoogleCloudAiplatformV1beta1Model
    modelId: str
    parentModel: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelResponse(typing.TypedDict, total=False):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadRagFileConfig(typing.TypedDict, total=False):
    ragFileChunkingConfig: GoogleCloudAiplatformV1beta1RagFileChunkingConfig
    ragFileMetadataConfig: GoogleCloudAiplatformV1beta1RagFileMetadataConfig
    ragFileParsingConfig: GoogleCloudAiplatformV1beta1RagFileParsingConfig
    ragFileTransformationConfig: GoogleCloudAiplatformV1beta1RagFileTransformationConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadRagFileRequest(typing.TypedDict, total=False):
    ragFile: GoogleCloudAiplatformV1beta1RagFile
    uploadRagFileConfig: GoogleCloudAiplatformV1beta1UploadRagFileConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadRagFileResponse(typing.TypedDict, total=False):
    error: GoogleRpcStatus
    ragFile: GoogleCloudAiplatformV1beta1RagFile

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertDatapointsRequest(
    typing.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1beta1IndexDatapoint]
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertDatapointsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertExamplesRequest(typing.TypedDict, total=False):
    examples: _list[GoogleCloudAiplatformV1beta1Example]
    overwrite: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertExamplesResponse(typing.TypedDict, total=False):
    results: _list[GoogleCloudAiplatformV1beta1UpsertExamplesResponseUpsertResult]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertExamplesResponseUpsertResult(
    typing.TypedDict, total=False
):
    example: GoogleCloudAiplatformV1beta1Example
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UrlContext(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UrlContextMetadata(typing.TypedDict, total=False):
    urlMetadata: _list[GoogleCloudAiplatformV1beta1UrlMetadata]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UrlMetadata(typing.TypedDict, total=False):
    retrievedUrl: str
    urlRetrievalStatus: typing.Literal[
        "URL_RETRIEVAL_STATUS_UNSPECIFIED",
        "URL_RETRIEVAL_STATUS_SUCCESS",
        "URL_RETRIEVAL_STATUS_ERROR",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UsageMetadata(typing.TypedDict, total=False):
    cacheTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
    cachedContentTokenCount: int
    candidatesTokenCount: int
    candidatesTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
    promptTokenCount: int
    promptTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
    thoughtsTokenCount: int
    toolUsePromptTokenCount: int
    toolUsePromptTokensDetails: _list[GoogleCloudAiplatformV1beta1ModalityTokenCount]
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
class GoogleCloudAiplatformV1beta1UserActionReference(typing.TypedDict, total=False):
    dataLabelingJob: str
    method: str
    operation: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UserScenario(typing.TypedDict, total=False):
    conversationPlan: str
    startingPrompt: str
    testCaseTitle: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UserScenarioGenerationConfig(
    typing.TypedDict, total=False
):
    environmentData: str
    modelName: str
    simulationInstruction: str
    userScenarioCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UserSpecifiedMetadata(typing.TypedDict, total=False):
    key: str
    value: GoogleCloudAiplatformV1beta1MetadataValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ValidateReinforcementTuningRewardRequest(
    typing.TypedDict, total=False
):
    compositeRewardConfig: (
        GoogleCloudAiplatformV1beta1CompositeReinforcementTuningRewardConfig
    )
    example: GoogleCloudAiplatformV1beta1ReinforcementTuningExample
    sampleResponse: GoogleCloudAiplatformV1beta1Content
    singleRewardConfig: (
        GoogleCloudAiplatformV1beta1SingleReinforcementTuningRewardConfig
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ValidateReinforcementTuningRewardResponse(
    typing.TypedDict, total=False
):
    error: str
    errorStatus: GoogleRpcStatus
    overallReward: float
    rewardDetails: dict[str, typing.Any]
    rewardInfoDetails: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Value(typing.TypedDict, total=False):
    doubleValue: float
    intValue: str
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VeoHyperParameters(typing.TypedDict, total=False):
    adapterSize: typing.Literal[
        "ADAPTER_SIZE_UNSPECIFIED",
        "ADAPTER_SIZE_EIGHT",
        "ADAPTER_SIZE_SIXTEEN",
        "ADAPTER_SIZE_THIRTY_TWO",
    ]
    epochCount: str
    learningRateMultiplier: float
    tuningSpeed: typing.Literal["TUNING_SPEED_UNSPECIFIED", "REGULAR", "FAST"]
    tuningTask: typing.Literal[
        "TUNING_TASK_UNSPECIFIED",
        "TUNING_TASK_I2V",
        "TUNING_TASK_T2V",
        "TUNING_TASK_R2V",
    ]
    veoDataMixtureRatio: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VeoLoraTuningSpec(typing.TypedDict, total=False):
    hyperParameters: GoogleCloudAiplatformV1beta1VeoHyperParameters
    trainingDatasetUri: str
    validationDatasetUri: str
    videoOrientation: typing.Literal[
        "VIDEO_ORIENTATION_UNSPECIFIED", "LANDSCAPE", "PORTRAIT"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VeoTuningSpec(typing.TypedDict, total=False):
    hyperParameters: GoogleCloudAiplatformV1beta1VeoHyperParameters
    trainingDatasetUri: str
    validationDatasetUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexAISearch(typing.TypedDict, total=False):
    dataStoreSpecs: _list[GoogleCloudAiplatformV1beta1VertexAISearchDataStoreSpec]
    datastore: str
    engine: str
    filter: str
    maxResults: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexAISearchDataStoreSpec(
    typing.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexAiSearchConfig(typing.TypedDict, total=False):
    servingConfig: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexMultimodalDatasetDestination(
    typing.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexMultimodalDatasetSource(
    typing.TypedDict, total=False
):
    datasetName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexRagStore(typing.TypedDict, total=False):
    ragCorpora: _list[str]
    ragResources: _list[GoogleCloudAiplatformV1beta1VertexRagStoreRagResource]
    ragRetrievalConfig: GoogleCloudAiplatformV1beta1RagRetrievalConfig
    similarityTopK: int
    storeContext: bool
    vectorDistanceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexRagStoreRagResource(
    typing.TypedDict, total=False
):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VideoMetadata(typing.TypedDict, total=False):
    endOffset: str
    fps: float
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VideoResponseFormat(typing.TypedDict, total=False):
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
class GoogleCloudAiplatformV1beta1VoiceConfig(typing.TypedDict, total=False):
    prebuiltVoiceConfig: GoogleCloudAiplatformV1beta1PrebuiltVoiceConfig
    replicatedVoiceConfig: GoogleCloudAiplatformV1beta1ReplicatedVoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WorkerPoolSpec(typing.TypedDict, total=False):
    containerSpec: GoogleCloudAiplatformV1beta1ContainerSpec
    diskSpec: GoogleCloudAiplatformV1beta1DiskSpec
    lustreMounts: _list[GoogleCloudAiplatformV1beta1LustreMount]
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    nfsMounts: _list[GoogleCloudAiplatformV1beta1NfsMount]
    pythonPackageSpec: GoogleCloudAiplatformV1beta1PythonPackageSpec
    replicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesPayload(
    typing.TypedDict, total=False
):
    entityId: str
    featureValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesRequest(
    typing.TypedDict, total=False
):
    payloads: _list[GoogleCloudAiplatformV1beta1WriteFeatureValuesPayload]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataRequest(
    typing.TypedDict, total=False
):
    writeRunDataRequests: _list[
        GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest(
    typing.TypedDict, total=False
):
    tensorboardRun: str
    timeSeriesData: _list[GoogleCloudAiplatformV1beta1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardRunDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1XmanagerInstance(typing.TypedDict, total=False):
    apiEndpoint: str
    createTime: str
    name: str
    network: str
    registeredClusters: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STATE_PROVISIONING",
        "STATE_RUNNING",
        "STATE_DELETING",
        "STATE_ERROR",
    ]
    subnetwork: str
    uiEndpoint: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1XraiAttribution(typing.TypedDict, total=False):
    blurBaselineConfig: GoogleCloudAiplatformV1beta1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1beta1SmoothGradConfig
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
class GoogleIamV1GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GoogleIamV1GetPolicyOptions

@typing.type_check_only
class GoogleIamV1GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

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
