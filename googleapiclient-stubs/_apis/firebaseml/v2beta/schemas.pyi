import typing

_list = list

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ApiAuth(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudAiplatformV1beta1ApiAuthApiKeyConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ApiAuthApiKeyConfig(typing.TypedDict, total=False):
    apiKeySecretVersion: str
    apiKeyString: str

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
class GoogleCloudAiplatformV1beta1Blob(typing.TypedDict, total=False):
    data: str
    displayName: str
    mimeType: str

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
class GoogleCloudAiplatformV1beta1Citation(typing.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: Date
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CitationMetadata(typing.TypedDict, total=False):
    citations: _list[GoogleCloudAiplatformV1beta1Citation]

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
class GoogleCloudAiplatformV1beta1Content(typing.TypedDict, total=False):
    parts: _list[GoogleCloudAiplatformV1beta1Part]
    role: str

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
class GoogleCloudAiplatformV1beta1DynamicRetrievalConfig(typing.TypedDict, total=False):
    dynamicThreshold: float
    mode: typing.Literal["MODE_UNSPECIFIED", "MODE_DYNAMIC"]

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
class GoogleCloudAiplatformV1beta1ExecutableCode(typing.TypedDict, total=False):
    code: str
    id: str
    language: typing.Literal["LANGUAGE_UNSPECIFIED", "PYTHON"]

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
class GoogleCloudAiplatformV1beta1FileData(typing.TypedDict, total=False):
    displayName: str
    fileUri: str
    mimeType: str

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
class GoogleCloudAiplatformV1beta1ModalityTokenCount(typing.TypedDict, total=False):
    modality: typing.Literal[
        "MODALITY_UNSPECIFIED", "TEXT", "IMAGE", "VIDEO", "AUDIO", "DOCUMENT"
    ]
    tokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelArmorConfig(typing.TypedDict, total=False):
    promptTemplateName: str
    responseTemplateName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MultiSpeakerVoiceConfig(
    typing.TypedDict, total=False
):
    speakerVoiceConfigs: _list[GoogleCloudAiplatformV1beta1SpeakerVoiceConfig]

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
class GoogleCloudAiplatformV1beta1PrebuiltVoiceConfig(typing.TypedDict, total=False):
    voiceName: str

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
class GoogleCloudAiplatformV1beta1ReplicatedVoiceConfig(typing.TypedDict, total=False):
    mimeType: str
    voiceSampleAudio: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResponseFormat(typing.TypedDict, total=False):
    audio: GoogleCloudAiplatformV1beta1AudioResponseFormat
    image: GoogleCloudAiplatformV1beta1ImageResponseFormat
    text: GoogleCloudAiplatformV1beta1TextResponseFormat
    video: GoogleCloudAiplatformV1beta1VideoResponseFormat

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Retrieval(typing.TypedDict, total=False):
    disableAttribution: bool
    externalApi: GoogleCloudAiplatformV1beta1ExternalApi
    vertexAiSearch: GoogleCloudAiplatformV1beta1VertexAISearch
    vertexRagStore: GoogleCloudAiplatformV1beta1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrievalConfig(typing.TypedDict, total=False):
    languageCode: str
    latLng: LatLng

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrievalMetadata(typing.TypedDict, total=False):
    googleSearchDynamicRetrievalScore: float

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
class GoogleCloudAiplatformV1beta1SearchEntryPoint(typing.TypedDict, total=False):
    renderedContent: str
    sdkBlob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Segment(typing.TypedDict, total=False):
    endIndex: int
    partIndex: int
    startIndex: int
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeakerVoiceConfig(typing.TypedDict, total=False):
    speaker: str
    voiceConfig: GoogleCloudAiplatformV1beta1VoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeechConfig(typing.TypedDict, total=False):
    languageCode: str
    multiSpeakerVoiceConfig: GoogleCloudAiplatformV1beta1MultiSpeakerVoiceConfig
    voiceConfig: GoogleCloudAiplatformV1beta1VoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TextResponseFormat(typing.TypedDict, total=False):
    mimeType: typing.Literal["MIME_TYPE_UNSPECIFIED", "APPLICATION_JSON", "TEXT_PLAIN"]
    schema: typing.Any

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
class GoogleCloudAiplatformV1beta1ToolParallelAiSearch(typing.TypedDict, total=False):
    apiKey: str
    customConfigs: dict[str, typing.Any]
    enableDataRetention: bool
    enableZeroDataRetention: bool

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
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ModelOperationMetadata(typing.TypedDict, total=False):
    basicOperationStatus: typing.Literal[
        "BASIC_OPERATION_STATUS_UNSPECIFIED",
        "BASIC_OPERATION_STATUS_UPLOADING",
        "BASIC_OPERATION_STATUS_VERIFYING",
    ]
    name: str
