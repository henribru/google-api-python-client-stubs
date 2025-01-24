import typing

import typing_extensions

_list = list

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Blob(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Candidate(typing_extensions.TypedDict, total=False):
    avgLogprobs: float
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
        "BLOCKLIST",
        "PROHIBITED_CONTENT",
        "SPII",
        "MALFORMED_FUNCTION_CALL",
    ]
    groundingMetadata: GoogleCloudAiplatformV1beta1GroundingMetadata
    index: int
    logprobsResult: GoogleCloudAiplatformV1beta1LogprobsResult
    safetyRatings: _list[GoogleCloudAiplatformV1beta1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Citation(typing_extensions.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: Date
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CitationMetadata(
    typing_extensions.TypedDict, total=False
):
    citations: _list[GoogleCloudAiplatformV1beta1Citation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CodeExecutionResult(
    typing_extensions.TypedDict, total=False
):
    outcome: typing_extensions.Literal[
        "OUTCOME_UNSPECIFIED",
        "OUTCOME_OK",
        "OUTCOME_FAILED",
        "OUTCOME_DEADLINE_EXCEEDED",
    ]
    output: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Content(typing_extensions.TypedDict, total=False):
    parts: _list[GoogleCloudAiplatformV1beta1Part]
    role: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    instances: _list[typing.Any]
    model: str
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensResponse(
    typing_extensions.TypedDict, total=False
):
    totalBillableCharacters: int
    totalTokens: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DynamicRetrievalConfig(
    typing_extensions.TypedDict, total=False
):
    dynamicThreshold: float
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "MODE_DYNAMIC"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecutableCode(
    typing_extensions.TypedDict, total=False
):
    code: str
    language: typing_extensions.Literal["LANGUAGE_UNSPECIFIED", "PYTHON"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FileData(typing_extensions.TypedDict, total=False):
    fileUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionCall(
    typing_extensions.TypedDict, total=False
):
    args: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionCallingConfig(
    typing_extensions.TypedDict, total=False
):
    allowedFunctionNames: _list[str]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "ANY", "NONE"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionDeclaration(
    typing_extensions.TypedDict, total=False
):
    description: str
    name: str
    parameters: GoogleCloudAiplatformV1beta1Schema
    response: GoogleCloudAiplatformV1beta1Schema

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FunctionResponse(
    typing_extensions.TypedDict, total=False
):
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentRequest(
    typing_extensions.TypedDict, total=False
):
    cachedContent: str
    contents: _list[GoogleCloudAiplatformV1beta1Content]
    generationConfig: GoogleCloudAiplatformV1beta1GenerationConfig
    labels: dict[str, typing.Any]
    safetySettings: _list[GoogleCloudAiplatformV1beta1SafetySetting]
    systemInstruction: GoogleCloudAiplatformV1beta1Content
    toolConfig: GoogleCloudAiplatformV1beta1ToolConfig
    tools: _list[GoogleCloudAiplatformV1beta1Tool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponse(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1beta1Candidate]
    modelVersion: str
    promptFeedback: GoogleCloudAiplatformV1beta1GenerateContentResponsePromptFeedback
    usageMetadata: GoogleCloudAiplatformV1beta1GenerateContentResponseUsageMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponsePromptFeedback(
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
    safetyRatings: _list[GoogleCloudAiplatformV1beta1SafetyRating]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponseUsageMetadata(
    typing_extensions.TypedDict, total=False
):
    cachedContentTokenCount: int
    candidatesTokenCount: int
    promptTokenCount: int
    totalTokenCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfig(
    typing_extensions.TypedDict, total=False
):
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
    responseSchema: GoogleCloudAiplatformV1beta1Schema
    routingConfig: GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfig
    seed: int
    speechConfig: GoogleCloudAiplatformV1beta1SpeechConfig
    stopSequences: _list[str]
    temperature: float
    topK: float
    topP: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfig(
    typing_extensions.TypedDict, total=False
):
    autoMode: GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigAutoRoutingMode
    manualMode: (
        GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigManualRoutingMode
    )

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigAutoRoutingMode(
    typing_extensions.TypedDict, total=False
):
    modelRoutingPreference: typing_extensions.Literal[
        "UNKNOWN", "PRIORITIZE_QUALITY", "BALANCED", "PRIORITIZE_COST"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerationConfigRoutingConfigManualRoutingMode(
    typing_extensions.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GoogleSearchRetrieval(
    typing_extensions.TypedDict, total=False
):
    dynamicRetrievalConfig: GoogleCloudAiplatformV1beta1DynamicRetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunk(
    typing_extensions.TypedDict, total=False
):
    retrievedContext: GoogleCloudAiplatformV1beta1GroundingChunkRetrievedContext
    web: GoogleCloudAiplatformV1beta1GroundingChunkWeb

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkRetrievedContext(
    typing_extensions.TypedDict, total=False
):
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingChunkWeb(
    typing_extensions.TypedDict, total=False
):
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingMetadata(
    typing_extensions.TypedDict, total=False
):
    groundingChunks: _list[GoogleCloudAiplatformV1beta1GroundingChunk]
    groundingSupports: _list[GoogleCloudAiplatformV1beta1GroundingSupport]
    retrievalMetadata: GoogleCloudAiplatformV1beta1RetrievalMetadata
    retrievalQueries: _list[str]
    searchEntryPoint: GoogleCloudAiplatformV1beta1SearchEntryPoint
    webSearchQueries: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GroundingSupport(
    typing_extensions.TypedDict, total=False
):
    confidenceScores: _list[float]
    groundingChunkIndices: _list[int]
    segment: GoogleCloudAiplatformV1beta1Segment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LogprobsResult(
    typing_extensions.TypedDict, total=False
):
    chosenCandidates: _list[GoogleCloudAiplatformV1beta1LogprobsResultCandidate]
    topCandidates: _list[GoogleCloudAiplatformV1beta1LogprobsResultTopCandidates]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LogprobsResultCandidate(
    typing_extensions.TypedDict, total=False
):
    logProbability: float
    token: str
    tokenId: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LogprobsResultTopCandidates(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudAiplatformV1beta1LogprobsResultCandidate]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Part(typing_extensions.TypedDict, total=False):
    codeExecutionResult: GoogleCloudAiplatformV1beta1CodeExecutionResult
    executableCode: GoogleCloudAiplatformV1beta1ExecutableCode
    fileData: GoogleCloudAiplatformV1beta1FileData
    functionCall: GoogleCloudAiplatformV1beta1FunctionCall
    functionResponse: GoogleCloudAiplatformV1beta1FunctionResponse
    inlineData: GoogleCloudAiplatformV1beta1Blob
    text: str
    thought: bool
    videoMetadata: GoogleCloudAiplatformV1beta1VideoMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrebuiltVoiceConfig(
    typing_extensions.TypedDict, total=False
):
    voiceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfig(
    typing_extensions.TypedDict, total=False
):
    filter: GoogleCloudAiplatformV1beta1RagRetrievalConfigFilter
    hybridSearch: GoogleCloudAiplatformV1beta1RagRetrievalConfigHybridSearch
    ranking: GoogleCloudAiplatformV1beta1RagRetrievalConfigRanking
    topK: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigFilter(
    typing_extensions.TypedDict, total=False
):
    metadataFilter: str
    vectorDistanceThreshold: float
    vectorSimilarityThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigHybridSearch(
    typing_extensions.TypedDict, total=False
):
    alpha: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigRanking(
    typing_extensions.TypedDict, total=False
):
    llmRanker: GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingLlmRanker
    rankService: GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingRankService

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingLlmRanker(
    typing_extensions.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagRetrievalConfigRankingRankService(
    typing_extensions.TypedDict, total=False
):
    modelName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Retrieval(typing_extensions.TypedDict, total=False):
    disableAttribution: bool
    vertexAiSearch: GoogleCloudAiplatformV1beta1VertexAISearch
    vertexRagStore: GoogleCloudAiplatformV1beta1VertexRagStore

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrievalConfig(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    latLng: LatLng

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrievalMetadata(
    typing_extensions.TypedDict, total=False
):
    googleSearchDynamicRetrievalScore: float

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
class GoogleCloudAiplatformV1beta1SafetySetting(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudAiplatformV1beta1Schema(typing_extensions.TypedDict, total=False):
    anyOf: _list[GoogleCloudAiplatformV1beta1Schema]
    default: typing.Any
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
    required: _list[str]
    title: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STRING", "NUMBER", "INTEGER", "BOOLEAN", "ARRAY", "OBJECT"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchEntryPoint(
    typing_extensions.TypedDict, total=False
):
    renderedContent: str
    sdkBlob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Segment(typing_extensions.TypedDict, total=False):
    endIndex: int
    partIndex: int
    startIndex: int
    text: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpeechConfig(
    typing_extensions.TypedDict, total=False
):
    voiceConfig: GoogleCloudAiplatformV1beta1VoiceConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tool(typing_extensions.TypedDict, total=False):
    codeExecution: GoogleCloudAiplatformV1beta1ToolCodeExecution
    functionDeclarations: _list[GoogleCloudAiplatformV1beta1FunctionDeclaration]
    googleSearch: GoogleCloudAiplatformV1beta1ToolGoogleSearch
    googleSearchRetrieval: GoogleCloudAiplatformV1beta1GoogleSearchRetrieval
    retrieval: GoogleCloudAiplatformV1beta1Retrieval

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolCodeExecution(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolConfig(typing_extensions.TypedDict, total=False):
    functionCallingConfig: GoogleCloudAiplatformV1beta1FunctionCallingConfig
    retrievalConfig: GoogleCloudAiplatformV1beta1RetrievalConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ToolGoogleSearch(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexAISearch(
    typing_extensions.TypedDict, total=False
):
    datastore: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexRagStore(
    typing_extensions.TypedDict, total=False
):
    ragCorpora: _list[str]
    ragResources: _list[GoogleCloudAiplatformV1beta1VertexRagStoreRagResource]
    ragRetrievalConfig: GoogleCloudAiplatformV1beta1RagRetrievalConfig
    similarityTopK: int
    vectorDistanceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VertexRagStoreRagResource(
    typing_extensions.TypedDict, total=False
):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VideoMetadata(
    typing_extensions.TypedDict, total=False
):
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1VoiceConfig(typing_extensions.TypedDict, total=False):
    prebuiltVoiceConfig: GoogleCloudAiplatformV1beta1PrebuiltVoiceConfig

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ModelOperationMetadata(typing_extensions.TypedDict, total=False):
    basicOperationStatus: typing_extensions.Literal[
        "BASIC_OPERATION_STATUS_UNSPECIFIED",
        "BASIC_OPERATION_STATUS_UPLOADING",
        "BASIC_OPERATION_STATUS_VERIFYING",
    ]
    name: str
