import typing

import typing_extensions

_list = list

@typing.type_check_only
class Blob(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class Candidate(typing_extensions.TypedDict, total=False):
    citationMetadata: CitationMetadata
    content: Content
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
    ]
    groundingMetadata: GroundingMetadata
    index: int
    safetyRatings: _list[SafetyRating]

@typing.type_check_only
class Citation(typing_extensions.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: Date
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class CitationMetadata(typing_extensions.TypedDict, total=False):
    citations: _list[Citation]

@typing.type_check_only
class Content(typing_extensions.TypedDict, total=False):
    parts: _list[Part]
    role: str

@typing.type_check_only
class CountTokensRequest(typing_extensions.TypedDict, total=False):
    contents: _list[Content]
    instances: _list[typing.Any]
    model: str

@typing.type_check_only
class CountTokensResponse(typing_extensions.TypedDict, total=False):
    totalBillableCharacters: int
    totalTokens: int

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class FileData(typing_extensions.TypedDict, total=False):
    fileUri: str
    mimeType: str

@typing.type_check_only
class FunctionCall(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    name: str

@typing.type_check_only
class FunctionCallingConfig(typing_extensions.TypedDict, total=False):
    allowedFunctionNames: _list[str]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "ANY", "NONE"]

@typing.type_check_only
class FunctionDeclaration(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    parameters: Schema
    response: Schema

@typing.type_check_only
class FunctionResponse(typing_extensions.TypedDict, total=False):
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GenerateContentRequest(typing_extensions.TypedDict, total=False):
    contents: _list[Content]
    generationConfig: GenerationConfig
    safetySettings: _list[SafetySetting]
    systemInstruction: Content
    toolConfig: ToolConfig
    tools: _list[Tool]

@typing.type_check_only
class GenerateContentResponse(typing_extensions.TypedDict, total=False):
    candidates: _list[Candidate]
    promptFeedback: PromptFeedback
    usageMetadata: UsageMetadata

@typing.type_check_only
class GenerationConfig(typing_extensions.TypedDict, total=False):
    candidateCount: int
    frequencyPenalty: float
    maxOutputTokens: int
    presencePenalty: float
    responseMimeType: str
    stopSequences: _list[str]
    temperature: float
    topK: float
    topP: float

@typing.type_check_only
class GoogleSearchRetrieval(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GroundingMetadata(typing_extensions.TypedDict, total=False):
    retrievalQueries: _list[str]
    searchEntryPoint: SearchEntryPoint
    webSearchQueries: _list[str]

@typing.type_check_only
class ModelOperationMetadata(typing_extensions.TypedDict, total=False):
    basicOperationStatus: typing_extensions.Literal[
        "BASIC_OPERATION_STATUS_UNSPECIFIED",
        "BASIC_OPERATION_STATUS_UPLOADING",
        "BASIC_OPERATION_STATUS_VERIFYING",
    ]
    name: str

@typing.type_check_only
class Part(typing_extensions.TypedDict, total=False):
    fileData: FileData
    functionCall: FunctionCall
    functionResponse: FunctionResponse
    inlineData: Blob
    text: str
    videoMetadata: VideoMetadata

@typing.type_check_only
class PromptFeedback(typing_extensions.TypedDict, total=False):
    blockReason: typing_extensions.Literal[
        "BLOCKED_REASON_UNSPECIFIED",
        "SAFETY",
        "OTHER",
        "BLOCKLIST",
        "PROHIBITED_CONTENT",
    ]
    blockReasonMessage: str
    safetyRatings: _list[SafetyRating]

@typing.type_check_only
class RagResource(typing_extensions.TypedDict, total=False):
    ragCorpus: str
    ragFileIds: _list[str]

@typing.type_check_only
class Retrieval(typing_extensions.TypedDict, total=False):
    disableAttribution: bool
    vertexAiSearch: VertexAISearch
    vertexRagStore: VertexRagStore

@typing.type_check_only
class SafetyRating(typing_extensions.TypedDict, total=False):
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
class SafetySetting(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
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
    ]

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    default: typing.Any
    description: str
    enum: _list[str]
    example: typing.Any
    format: str
    items: Schema
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
    required: _list[str]
    title: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STRING", "NUMBER", "INTEGER", "BOOLEAN", "ARRAY", "OBJECT"
    ]

@typing.type_check_only
class SearchEntryPoint(typing_extensions.TypedDict, total=False):
    renderedContent: str
    sdkBlob: str

@typing.type_check_only
class Tool(typing_extensions.TypedDict, total=False):
    functionDeclarations: _list[FunctionDeclaration]
    googleSearchRetrieval: GoogleSearchRetrieval
    retrieval: Retrieval

@typing.type_check_only
class ToolConfig(typing_extensions.TypedDict, total=False):
    functionCallingConfig: FunctionCallingConfig

@typing.type_check_only
class UsageMetadata(typing_extensions.TypedDict, total=False):
    candidatesTokenCount: int
    promptTokenCount: int
    totalTokenCount: int

@typing.type_check_only
class VertexAISearch(typing_extensions.TypedDict, total=False):
    datastore: str

@typing.type_check_only
class VertexRagStore(typing_extensions.TypedDict, total=False):
    ragCorpora: _list[str]
    ragResources: _list[RagResource]
    similarityTopK: int
    vectorDistanceThreshold: float

@typing.type_check_only
class VideoMetadata(typing_extensions.TypedDict, total=False):
    endOffset: str
    startOffset: str
