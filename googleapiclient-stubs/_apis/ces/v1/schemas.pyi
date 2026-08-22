import typing

_list = list

@typing.type_check_only
class Action(typing.TypedDict, total=False):
    connectionActionId: str
    entityOperation: ActionEntityOperation
    inputFields: _list[str]
    outputFields: _list[str]

@typing.type_check_only
class ActionEntityOperation(typing.TypedDict, total=False):
    entityId: str
    operation: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
    ]

@typing.type_check_only
class Agent(typing.TypedDict, total=False):
    afterAgentCallbacks: _list[Callback]
    afterModelCallbacks: _list[Callback]
    afterToolCallbacks: _list[Callback]
    beforeAgentCallbacks: _list[Callback]
    beforeModelCallbacks: _list[Callback]
    beforeToolCallbacks: _list[Callback]
    childAgents: _list[str]
    createTime: str
    description: str
    displayName: str
    etag: str
    generatedSummary: str
    guardrails: _list[str]
    instruction: str
    llmAgent: AgentLlmAgent
    modelSettings: ModelSettings
    name: str
    remoteDialogflowAgent: AgentRemoteDialogflowAgent
    tools: _list[str]
    toolsets: _list[AgentAgentToolset]
    transferRules: _list[TransferRule]
    updateTime: str
    validationErrors: _list[str]

@typing.type_check_only
class AgentAgentToolset(typing.TypedDict, total=False):
    toolIds: _list[str]
    toolset: str

@typing.type_check_only
class AgentCard(typing.TypedDict, total=False):
    description: str
    name: str
    skills: _list[AgentSkill]
    supportedInterfaces: _list[AgentInterface]
    version: str

@typing.type_check_only
class AgentInterface(typing.TypedDict, total=False):
    protocolBinding: str
    protocolVersion: str
    tenant: str
    url: str

@typing.type_check_only
class AgentLlmAgent(typing.TypedDict, total=False): ...

@typing.type_check_only
class AgentRemoteDialogflowAgent(typing.TypedDict, total=False):
    agent: str
    environmentId: str
    flowId: str
    inputVariableMapping: dict[str, typing.Any]
    languageCodeVariable: str
    outputVariableMapping: dict[str, typing.Any]
    respectResponseInterruptionSettings: bool

@typing.type_check_only
class AgentSkill(typing.TypedDict, total=False):
    description: str
    examples: _list[str]
    id: str
    inputModes: _list[str]
    name: str
    outputModes: _list[str]
    tags: _list[str]

@typing.type_check_only
class AgentTool(typing.TypedDict, total=False):
    agent: str
    description: str
    name: str

@typing.type_check_only
class AgentTransfer(typing.TypedDict, total=False):
    displayName: str
    targetAgent: str

@typing.type_check_only
class AmbientSoundConfig(typing.TypedDict, total=False):
    gcsUri: str
    prebuiltAmbientNoise: typing.Literal[
        "PREBUILT_AMBIENT_NOISE_UNSPECIFIED",
        "RETAIL_STORE",
        "CONVENTION_HALL",
        "OUTDOOR",
    ]
    prebuiltAmbientSound: str
    volumeGainDb: float

@typing.type_check_only
class ApiAuthentication(typing.TypedDict, total=False):
    apiKeyConfig: ApiKeyConfig
    bearerTokenConfig: BearerTokenConfig
    oauthConfig: OAuthConfig
    serviceAccountAuthConfig: ServiceAccountAuthConfig
    serviceAgentIdTokenAuthConfig: ServiceAgentIdTokenAuthConfig

@typing.type_check_only
class ApiKeyConfig(typing.TypedDict, total=False):
    apiKeySecretVersion: str
    keyName: str
    requestLocation: typing.Literal[
        "REQUEST_LOCATION_UNSPECIFIED", "HEADER", "QUERY_STRING"
    ]

@typing.type_check_only
class App(typing.TypedDict, total=False):
    audioProcessingConfig: AudioProcessingConfig
    clientCertificateSettings: ClientCertificateSettings
    createTime: str
    dataStoreSettings: DataStoreSettings
    defaultChannelProfile: ChannelProfile
    deploymentCount: int
    description: str
    displayName: str
    errorHandlingSettings: ErrorHandlingSettings
    etag: str
    evaluationMetricsThresholds: EvaluationMetricsThresholds
    globalInstruction: str
    guardrails: _list[str]
    languageSettings: LanguageSettings
    locked: bool
    loggingSettings: LoggingSettings
    metadata: dict[str, typing.Any]
    modelSettings: ModelSettings
    name: str
    pinned: bool
    predefinedVariableDeclarations: _list[AppVariableDeclaration]
    rootAgent: str
    timeZoneSettings: TimeZoneSettings
    toolExecutionMode: typing.Literal[
        "TOOL_EXECUTION_MODE_UNSPECIFIED", "PARALLEL", "SEQUENTIAL"
    ]
    updateTime: str
    validationErrors: _list[str]
    variableDeclarations: _list[AppVariableDeclaration]
    vpcScSettings: VpcScSettings

@typing.type_check_only
class AppSnapshot(typing.TypedDict, total=False):
    agents: _list[Agent]
    app: App
    examples: _list[Example]
    guardrails: _list[Guardrail]
    tools: _list[Tool]
    toolsets: _list[Toolset]

@typing.type_check_only
class AppVariableDeclaration(typing.TypedDict, total=False):
    description: str
    name: str
    schema: Schema

@typing.type_check_only
class AppVersion(typing.TypedDict, total=False):
    createTime: str
    creator: str
    description: str
    displayName: str
    etag: str
    name: str
    snapshot: AppSnapshot

@typing.type_check_only
class AudioProcessingConfig(typing.TypedDict, total=False):
    ambientSoundConfig: AmbientSoundConfig
    bargeInConfig: BargeInConfig
    inactivityTimeout: str
    synthesizeSpeechConfigs: dict[str, typing.Any]

@typing.type_check_only
class AudioRecordingConfig(typing.TypedDict, total=False):
    gcsBucket: str
    gcsPathPrefix: str

@typing.type_check_only
class BargeInConfig(typing.TypedDict, total=False):
    bargeInAwareness: bool
    disableBargeIn: bool

@typing.type_check_only
class BatchDeleteConversationsRequest(typing.TypedDict, total=False):
    conversations: _list[str]

@typing.type_check_only
class BearerTokenConfig(typing.TypedDict, total=False):
    token: str

@typing.type_check_only
class BigQueryExportSettings(typing.TypedDict, total=False):
    dataset: str
    enabled: bool
    project: str

@typing.type_check_only
class Blob(typing.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class Callback(typing.TypedDict, total=False):
    description: str
    disabled: bool
    proactiveExecutionEnabled: bool
    pythonCode: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Changelog(typing.TypedDict, total=False):
    action: str
    author: str
    createTime: str
    dependentResources: _list[dict[str, typing.Any]]
    description: str
    displayName: str
    name: str
    newResource: dict[str, typing.Any]
    originalResource: dict[str, typing.Any]
    resource: str
    resourceType: str
    sequenceNumber: str

@typing.type_check_only
class ChannelProfile(typing.TypedDict, total=False):
    channelType: typing.Literal[
        "UNKNOWN",
        "WEB_UI",
        "API",
        "TWILIO",
        "GOOGLE_TELEPHONY_PLATFORM",
        "CONTACT_CENTER_AS_A_SERVICE",
        "CONTACT_CENTER_AS_A_SERVICE_CHAT",
        "FIVE9",
        "CONTACT_CENTER_INTEGRATION",
        "WHATSAPP",
        "INSTAGRAM",
    ]
    disableBargeInControl: bool
    disableDtmf: bool
    instagramConfig: ChannelProfileInstagramConfig
    noiseSuppressionLevel: str
    personaProperty: ChannelProfilePersonaProperty
    profileId: str
    webWidgetConfig: ChannelProfileWebWidgetConfig
    whatsappConfig: ChannelProfileWhatsAppConfig

@typing.type_check_only
class ChannelProfileInstagramConfig(typing.TypedDict, total=False):
    description: str
    displayName: str
    instagramAccountId: str
    thumbnailUrl: str

@typing.type_check_only
class ChannelProfilePersonaProperty(typing.TypedDict, total=False):
    persona: typing.Literal["UNKNOWN", "CONCISE", "CHATTY"]

@typing.type_check_only
class ChannelProfileWebWidgetConfig(typing.TypedDict, total=False):
    modality: typing.Literal[
        "MODALITY_UNSPECIFIED",
        "CHAT_AND_VOICE",
        "VOICE_ONLY",
        "CHAT_ONLY",
        "CHAT_VOICE_AND_VIDEO",
    ]
    securitySettings: ChannelProfileWebWidgetConfigSecuritySettings
    theme: typing.Literal["THEME_UNSPECIFIED", "LIGHT", "DARK"]
    webWidgetTitle: str

@typing.type_check_only
class ChannelProfileWebWidgetConfigSecuritySettings(typing.TypedDict, total=False):
    allowedOrigins: _list[str]
    enableOriginCheck: bool
    enablePublicAccess: bool
    enableRecaptcha: bool

@typing.type_check_only
class ChannelProfileWhatsAppConfig(typing.TypedDict, total=False):
    description: str
    displayName: str
    phoneNumber: str
    phoneNumberId: str
    thumbnailUrl: str
    wabaId: str

@typing.type_check_only
class Chunk(typing.TypedDict, total=False):
    agentTransfer: AgentTransfer
    blob: Blob
    defaultVariables: dict[str, typing.Any]
    image: Image
    payload: dict[str, typing.Any]
    text: str
    toolCall: ToolCall
    toolResponse: ToolResponse
    transcript: str
    updatedVariables: dict[str, typing.Any]

@typing.type_check_only
class Citations(typing.TypedDict, total=False):
    citedChunks: _list[CitationsCitedChunk]

@typing.type_check_only
class CitationsCitedChunk(typing.TypedDict, total=False):
    requiresAttribution: bool
    text: str
    title: str
    uri: str

@typing.type_check_only
class ClientCertificateSettings(typing.TypedDict, total=False):
    passphrase: str
    privateKey: str
    tlsCertificate: str

@typing.type_check_only
class ClientFunction(typing.TypedDict, total=False):
    description: str
    name: str
    parameters: Schema
    response: Schema

@typing.type_check_only
class CloudLoggingSettings(typing.TypedDict, total=False):
    enableCloudLogging: bool

@typing.type_check_only
class CodeBlock(typing.TypedDict, total=False):
    pythonCode: str

@typing.type_check_only
class ConnectorTool(typing.TypedDict, total=False):
    action: Action
    authConfig: EndUserAuthConfig
    connection: str
    description: str
    name: str

@typing.type_check_only
class ConnectorToolset(typing.TypedDict, total=False):
    authConfig: EndUserAuthConfig
    connection: str
    connectorActions: _list[Action]

@typing.type_check_only
class Conversation(typing.TypedDict, total=False):
    appVersion: str
    channelType: typing.Literal[
        "CHANNEL_TYPE_UNSPECIFIED", "TEXT", "AUDIO", "MULTIMODAL"
    ]
    deployment: str
    endTime: str
    entryAgent: str
    inputTypes: _list[
        typing.Literal[
            "INPUT_TYPE_UNSPECIFIED",
            "INPUT_TYPE_TEXT",
            "INPUT_TYPE_EVENT",
            "INPUT_TYPE_AUDIO",
            "INPUT_TYPE_IMAGE",
            "INPUT_TYPE_BLOB",
            "INPUT_TYPE_TOOL_RESPONSE",
            "INPUT_TYPE_VARIABLES",
        ]
    ]
    languageCode: str
    messages: _list[Message]
    name: str
    source: typing.Literal[
        "SOURCE_UNSPECIFIED", "LIVE", "SIMULATOR", "EVAL", "AGENT_TOOL"
    ]
    startTime: str
    turnCount: int
    turns: _list[ConversationTurn]

@typing.type_check_only
class ConversationLoggingSettings(typing.TypedDict, total=False):
    disableConversationLogging: bool
    retentionWindow: str

@typing.type_check_only
class ConversationTurn(typing.TypedDict, total=False):
    messages: _list[Message]
    resolvedDeveloperInstruction: str
    rootSpan: Span
    templateAttributes: dict[str, typing.Any]
    userIntendedText: str

@typing.type_check_only
class DataStore(typing.TypedDict, total=False):
    connectorConfig: DataStoreConnectorConfig
    createTime: str
    displayName: str
    documentProcessingMode: typing.Literal[
        "DOCUMENT_PROCESSING_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    name: str
    type: typing.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED", "PUBLIC_WEB", "UNSTRUCTURED", "FAQ", "CONNECTOR"
    ]

@typing.type_check_only
class DataStoreConnectorConfig(typing.TypedDict, total=False):
    collection: str
    collectionDisplayName: str
    dataSource: str

@typing.type_check_only
class DataStoreSettings(typing.TypedDict, total=False):
    engines: _list[DataStoreSettingsEngine]

@typing.type_check_only
class DataStoreSettingsEngine(typing.TypedDict, total=False):
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "ENGINE_TYPE_SEARCH", "ENGINE_TYPE_CHAT"]

@typing.type_check_only
class DataStoreTool(typing.TypedDict, total=False):
    boostSpecs: _list[DataStoreToolBoostSpecs]
    dataStoreSource: DataStoreToolDataStoreSource
    description: str
    engineSource: DataStoreToolEngineSource
    filterParameterBehavior: typing.Literal[
        "FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED", "ALWAYS_INCLUDE", "NEVER_INCLUDE"
    ]
    modalityConfigs: _list[DataStoreToolModalityConfig]
    name: str

@typing.type_check_only
class DataStoreToolBoostSpec(typing.TypedDict, total=False):
    conditionBoostSpecs: _list[DataStoreToolBoostSpecConditionBoostSpec]

@typing.type_check_only
class DataStoreToolBoostSpecConditionBoostSpec(typing.TypedDict, total=False):
    boost: float
    boostControlSpec: DataStoreToolBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class DataStoreToolBoostSpecConditionBoostSpecBoostControlSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        DataStoreToolBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class DataStoreToolBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class DataStoreToolBoostSpecs(typing.TypedDict, total=False):
    dataStores: _list[str]
    spec: _list[DataStoreToolBoostSpec]

@typing.type_check_only
class DataStoreToolDataStoreSource(typing.TypedDict, total=False):
    dataStore: DataStore
    filter: str

@typing.type_check_only
class DataStoreToolEngineSource(typing.TypedDict, total=False):
    dataStoreSources: _list[DataStoreToolDataStoreSource]
    engine: str
    filter: str

@typing.type_check_only
class DataStoreToolGroundingConfig(typing.TypedDict, total=False):
    disabled: bool
    groundingLevel: float

@typing.type_check_only
class DataStoreToolModalityConfig(typing.TypedDict, total=False):
    groundingConfig: DataStoreToolGroundingConfig
    modalityType: typing.Literal["MODALITY_TYPE_UNSPECIFIED", "TEXT", "AUDIO"]
    rewriterConfig: DataStoreToolRewriterConfig
    snippetsConfig: DataStoreToolSnippetsConfig
    summarizationConfig: DataStoreToolSummarizationConfig

@typing.type_check_only
class DataStoreToolRewriterConfig(typing.TypedDict, total=False):
    disabled: bool
    modelSettings: ModelSettings
    prompt: str

@typing.type_check_only
class DataStoreToolSnippetsConfig(typing.TypedDict, total=False):
    enableSnippets: bool

@typing.type_check_only
class DataStoreToolSummarizationConfig(typing.TypedDict, total=False):
    disabled: bool
    modelSettings: ModelSettings
    prompt: str

@typing.type_check_only
class Deployment(typing.TypedDict, total=False):
    appVersion: str
    channelProfile: ChannelProfile
    createTime: str
    displayName: str
    etag: str
    experimentConfig: ExperimentConfig
    instagramCredentials: InstagramCredentials
    modality: typing.Literal[
        "MODALITY_UNSPECIFIED", "MODALITY_TEXT", "MODALITY_VOICE", "MODALITY_VIDEO"
    ]
    modelSettings: ModelSettings
    name: str
    updateTime: str
    whatsappCredentials: WhatsAppCredentials

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EndSession(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class EndUserAuthConfig(typing.TypedDict, total=False):
    oauth2AuthCodeConfig: EndUserAuthConfigOauth2AuthCodeConfig
    oauth2JwtBearerConfig: EndUserAuthConfigOauth2JwtBearerConfig

@typing.type_check_only
class EndUserAuthConfigOauth2AuthCodeConfig(typing.TypedDict, total=False):
    oauthToken: str

@typing.type_check_only
class EndUserAuthConfigOauth2JwtBearerConfig(typing.TypedDict, total=False):
    clientKey: str
    issuer: str
    subject: str

@typing.type_check_only
class EndpointControlPolicy(typing.TypedDict, total=False):
    allowedOrigins: _list[str]
    enforcementScope: typing.Literal[
        "ENFORCEMENT_SCOPE_UNSPECIFIED", "VPCSC_ONLY", "ALWAYS"
    ]

@typing.type_check_only
class ErrorHandlingSettings(typing.TypedDict, total=False):
    endSessionConfig: ErrorHandlingSettingsEndSessionConfig
    errorHandlingStrategy: typing.Literal[
        "ERROR_HANDLING_STRATEGY_UNSPECIFIED",
        "NONE",
        "FALLBACK_RESPONSE",
        "END_SESSION",
    ]
    fallbackResponseConfig: ErrorHandlingSettingsFallbackResponseConfig

@typing.type_check_only
class ErrorHandlingSettingsEndSessionConfig(typing.TypedDict, total=False):
    escalateSession: bool

@typing.type_check_only
class ErrorHandlingSettingsFallbackResponseConfig(typing.TypedDict, total=False):
    customFallbackMessages: dict[str, typing.Any]
    maxFallbackAttempts: int

@typing.type_check_only
class EvaluationMetricsThresholds(typing.TypedDict, total=False):
    goldenEvaluationMetricsThresholds: (
        EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholds
    )
    goldenHallucinationMetricBehavior: typing.Literal[
        "HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    hallucinationMetricBehavior: typing.Literal[
        "HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    scenarioHallucinationMetricBehavior: typing.Literal[
        "HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED", "DISABLED", "ENABLED"
    ]

@typing.type_check_only
class EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholds(
    typing.TypedDict, total=False
):
    expectationLevelMetricsThresholds: EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholds
    toolMatchingSettings: EvaluationMetricsThresholdsToolMatchingSettings
    turnLevelMetricsThresholds: EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholds

@typing.type_check_only
class EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholds(
    typing.TypedDict, total=False
):
    toolInvocationParameterCorrectnessThreshold: float

@typing.type_check_only
class EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholds(
    typing.TypedDict, total=False
):
    overallToolInvocationCorrectnessThreshold: float
    semanticSimilarityChannel: typing.Literal[
        "SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED", "TEXT", "AUDIO"
    ]
    semanticSimilaritySuccessThreshold: int

@typing.type_check_only
class EvaluationMetricsThresholdsToolMatchingSettings(typing.TypedDict, total=False):
    extraToolCallBehavior: typing.Literal[
        "EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED", "FAIL", "ALLOW"
    ]

@typing.type_check_only
class Event(typing.TypedDict, total=False):
    event: str

@typing.type_check_only
class Example(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    entryAgent: str
    etag: str
    invalid: bool
    messages: _list[Message]
    name: str
    updateTime: str

@typing.type_check_only
class ExecuteToolRequest(typing.TypedDict, total=False):
    args: dict[str, typing.Any]
    context: dict[str, typing.Any]
    mockConfig: MockConfig
    tool: str
    toolsetTool: ToolsetTool
    variables: dict[str, typing.Any]

@typing.type_check_only
class ExecuteToolResponse(typing.TypedDict, total=False):
    citations: Citations
    googleSearchSuggestions: GoogleSearchSuggestions
    response: dict[str, typing.Any]
    tool: str
    toolsetTool: ToolsetTool
    variables: dict[str, typing.Any]

@typing.type_check_only
class ExperimentConfig(typing.TypedDict, total=False):
    versionRelease: ExperimentConfigVersionRelease

@typing.type_check_only
class ExperimentConfigVersionRelease(typing.TypedDict, total=False):
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE", "EXPIRED"]
    trafficAllocations: _list[ExperimentConfigVersionReleaseTrafficAllocation]

@typing.type_check_only
class ExperimentConfigVersionReleaseTrafficAllocation(typing.TypedDict, total=False):
    appVersion: str
    id: str
    trafficPercentage: int

@typing.type_check_only
class ExportAppRequest(typing.TypedDict, total=False):
    appVersion: str
    exportFormat: typing.Literal["EXPORT_FORMAT_UNSPECIFIED", "JSON", "YAML"]
    gcsUri: str

@typing.type_check_only
class ExportAppResponse(typing.TypedDict, total=False):
    appContent: str
    appUri: str

@typing.type_check_only
class ExpressionCondition(typing.TypedDict, total=False):
    expression: str

@typing.type_check_only
class FileSearchTool(typing.TypedDict, total=False):
    corpusType: typing.Literal["CORPUS_TYPE_UNSPECIFIED", "USER_OWNED", "FULLY_MANAGED"]
    description: str
    fileCorpus: str
    name: str

@typing.type_check_only
class GenerateChatTokenRequest(typing.TypedDict, total=False):
    deployment: str
    liveHandoffEnabled: bool
    recaptchaToken: str

@typing.type_check_only
class GenerateChatTokenResponse(typing.TypedDict, total=False):
    chatToken: str
    expireTime: str

@typing.type_check_only
class GoogleSearchSuggestions(typing.TypedDict, total=False):
    htmls: _list[str]
    webSearchQueries: _list[WebSearchQuery]

@typing.type_check_only
class GoogleSearchTool(typing.TypedDict, total=False):
    contextUrls: _list[str]
    description: str
    excludeDomains: _list[str]
    name: str
    preferredDomains: _list[str]
    promptConfig: GoogleSearchToolPromptConfig

@typing.type_check_only
class GoogleSearchToolPromptConfig(typing.TypedDict, total=False):
    textPrompt: str
    voicePrompt: str

@typing.type_check_only
class Guardrail(typing.TypedDict, total=False):
    action: TriggerAction
    codeCallback: GuardrailCodeCallback
    contentFilter: GuardrailContentFilter
    createTime: str
    description: str
    displayName: str
    enabled: bool
    etag: str
    llmPolicy: GuardrailLlmPolicy
    llmPromptSecurity: GuardrailLlmPromptSecurity
    modelSafety: GuardrailModelSafety
    name: str
    updateTime: str

@typing.type_check_only
class GuardrailCodeCallback(typing.TypedDict, total=False):
    afterAgentCallback: Callback
    afterModelCallback: Callback
    beforeAgentCallback: Callback
    beforeModelCallback: Callback

@typing.type_check_only
class GuardrailContentFilter(typing.TypedDict, total=False):
    bannedContents: _list[str]
    bannedContentsInAgentResponse: _list[str]
    bannedContentsInUserInput: _list[str]
    disregardDiacritics: bool
    matchType: typing.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "SIMPLE_STRING_MATCH",
        "WORD_BOUNDARY_STRING_MATCH",
        "REGEXP_MATCH",
    ]

@typing.type_check_only
class GuardrailLlmPolicy(typing.TypedDict, total=False):
    allowShortUtterance: bool
    failOpen: bool
    maxConversationMessages: int
    modelSettings: ModelSettings
    policyScope: typing.Literal[
        "POLICY_SCOPE_UNSPECIFIED",
        "USER_QUERY",
        "AGENT_RESPONSE",
        "USER_QUERY_AND_AGENT_RESPONSE",
    ]
    prompt: str

@typing.type_check_only
class GuardrailLlmPromptSecurity(typing.TypedDict, total=False):
    customPolicy: GuardrailLlmPolicy
    defaultSettings: GuardrailLlmPromptSecurityDefaultSecuritySettings
    failOpen: bool

@typing.type_check_only
class GuardrailLlmPromptSecurityDefaultSecuritySettings(typing.TypedDict, total=False):
    defaultPromptTemplate: str

@typing.type_check_only
class GuardrailModelSafety(typing.TypedDict, total=False):
    safetySettings: _list[GuardrailModelSafetySafetySetting]

@typing.type_check_only
class GuardrailModelSafetySafetySetting(typing.TypedDict, total=False):
    category: typing.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    ]
    threshold: typing.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class ImportAppRequest(typing.TypedDict, total=False):
    appContent: str
    appId: str
    displayName: str
    gcsUri: str
    ignoreAppLock: bool
    importOptions: ImportAppRequestImportOptions

@typing.type_check_only
class ImportAppRequestImportOptions(typing.TypedDict, total=False):
    conflictResolutionStrategy: typing.Literal[
        "CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED", "REPLACE", "OVERWRITE"
    ]
    validateOnly: bool

@typing.type_check_only
class ImportAppResponse(typing.TypedDict, total=False):
    name: str
    warnings: _list[str]

@typing.type_check_only
class InputAudioConfig(typing.TypedDict, total=False):
    audioEncoding: typing.Literal[
        "AUDIO_ENCODING_UNSPECIFIED", "LINEAR16", "MULAW", "ALAW"
    ]
    noiseSuppressionLevel: str
    sampleRateHertz: int

@typing.type_check_only
class InstagramCredentials(typing.TypedDict, total=False):
    authCode: str
    conversationProfileId: str

@typing.type_check_only
class LanguageSettings(typing.TypedDict, total=False):
    defaultLanguageCode: str
    enableMultilingualSupport: bool
    fallbackAction: str
    supportedLanguageCodes: _list[str]

@typing.type_check_only
class LfA2aV1APIKeySecurityScheme(typing.TypedDict, total=False):
    description: str
    location: str
    name: str

@typing.type_check_only
class LfA2aV1AgentCapabilities(typing.TypedDict, total=False):
    extendedAgentCard: bool
    extensions: _list[LfA2aV1AgentExtension]
    pushNotifications: bool
    streaming: bool

@typing.type_check_only
class LfA2aV1AgentCard(typing.TypedDict, total=False):
    capabilities: LfA2aV1AgentCapabilities
    defaultInputModes: _list[str]
    defaultOutputModes: _list[str]
    description: str
    documentationUrl: str
    iconUrl: str
    name: str
    provider: LfA2aV1AgentProvider
    securityRequirements: _list[LfA2aV1SecurityRequirement]
    securitySchemes: dict[str, typing.Any]
    signatures: _list[LfA2aV1AgentCardSignature]
    skills: _list[LfA2aV1AgentSkill]
    supportedInterfaces: _list[LfA2aV1AgentInterface]
    version: str

@typing.type_check_only
class LfA2aV1AgentCardSignature(typing.TypedDict, total=False):
    header: dict[str, typing.Any]
    protected: str
    signature: str

@typing.type_check_only
class LfA2aV1AgentExtension(typing.TypedDict, total=False):
    description: str
    params: dict[str, typing.Any]
    required: bool
    uri: str

@typing.type_check_only
class LfA2aV1AgentInterface(typing.TypedDict, total=False):
    protocolBinding: str
    protocolVersion: str
    tenant: str
    url: str

@typing.type_check_only
class LfA2aV1AgentProvider(typing.TypedDict, total=False):
    organization: str
    url: str

@typing.type_check_only
class LfA2aV1AgentSkill(typing.TypedDict, total=False):
    description: str
    examples: _list[str]
    id: str
    inputModes: _list[str]
    name: str
    outputModes: _list[str]
    securityRequirements: _list[LfA2aV1SecurityRequirement]
    tags: _list[str]

@typing.type_check_only
class LfA2aV1Artifact(typing.TypedDict, total=False):
    artifactId: str
    description: str
    extensions: _list[str]
    metadata: dict[str, typing.Any]
    name: str
    parts: _list[LfA2aV1Part]

@typing.type_check_only
class LfA2aV1AuthenticationInfo(typing.TypedDict, total=False):
    credentials: str
    scheme: str

@typing.type_check_only
class LfA2aV1AuthorizationCodeOAuthFlow(typing.TypedDict, total=False):
    authorizationUrl: str
    pkceRequired: bool
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class LfA2aV1ClientCredentialsOAuthFlow(typing.TypedDict, total=False):
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class LfA2aV1DeviceCodeOAuthFlow(typing.TypedDict, total=False):
    deviceAuthorizationUrl: str
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class LfA2aV1HTTPAuthSecurityScheme(typing.TypedDict, total=False):
    bearerFormat: str
    description: str
    scheme: str

@typing.type_check_only
class LfA2aV1ImplicitOAuthFlow(typing.TypedDict, total=False):
    authorizationUrl: str
    refreshUrl: str
    scopes: dict[str, typing.Any]

@typing.type_check_only
class LfA2aV1Message(typing.TypedDict, total=False):
    contextId: str
    extensions: _list[str]
    messageId: str
    metadata: dict[str, typing.Any]
    parts: _list[LfA2aV1Part]
    referenceTaskIds: _list[str]
    role: typing.Literal["ROLE_UNSPECIFIED", "ROLE_USER", "ROLE_AGENT"]
    taskId: str

@typing.type_check_only
class LfA2aV1MutualTlsSecurityScheme(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class LfA2aV1OAuth2SecurityScheme(typing.TypedDict, total=False):
    description: str
    flows: LfA2aV1OAuthFlows
    oauth2MetadataUrl: str

@typing.type_check_only
class LfA2aV1OAuthFlows(typing.TypedDict, total=False):
    authorizationCode: LfA2aV1AuthorizationCodeOAuthFlow
    clientCredentials: LfA2aV1ClientCredentialsOAuthFlow
    deviceCode: LfA2aV1DeviceCodeOAuthFlow
    implicit: LfA2aV1ImplicitOAuthFlow
    password: LfA2aV1PasswordOAuthFlow

@typing.type_check_only
class LfA2aV1OpenIdConnectSecurityScheme(typing.TypedDict, total=False):
    description: str
    openIdConnectUrl: str

@typing.type_check_only
class LfA2aV1Part(typing.TypedDict, total=False):
    data: typing.Any
    filename: str
    mediaType: str
    metadata: dict[str, typing.Any]
    raw: str
    text: str
    url: str

@typing.type_check_only
class LfA2aV1PasswordOAuthFlow(typing.TypedDict, total=False):
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class LfA2aV1SecurityRequirement(typing.TypedDict, total=False):
    schemes: dict[str, typing.Any]

@typing.type_check_only
class LfA2aV1SecurityScheme(typing.TypedDict, total=False):
    apiKeySecurityScheme: LfA2aV1APIKeySecurityScheme
    httpAuthSecurityScheme: LfA2aV1HTTPAuthSecurityScheme
    mtlsSecurityScheme: LfA2aV1MutualTlsSecurityScheme
    oauth2SecurityScheme: LfA2aV1OAuth2SecurityScheme
    openIdConnectSecurityScheme: LfA2aV1OpenIdConnectSecurityScheme

@typing.type_check_only
class LfA2aV1SendMessageConfiguration(typing.TypedDict, total=False):
    acceptedOutputModes: _list[str]
    historyLength: int
    returnImmediately: bool
    taskPushNotificationConfig: LfA2aV1TaskPushNotificationConfig

@typing.type_check_only
class LfA2aV1SendMessageRequest(typing.TypedDict, total=False):
    configuration: LfA2aV1SendMessageConfiguration
    message: LfA2aV1Message
    metadata: dict[str, typing.Any]

@typing.type_check_only
class LfA2aV1SendMessageResponse(typing.TypedDict, total=False):
    message: LfA2aV1Message
    task: LfA2aV1Task

@typing.type_check_only
class LfA2aV1StringList(typing.TypedDict, total=False):
    list: _list[str]

@typing.type_check_only
class LfA2aV1Task(typing.TypedDict, total=False):
    artifacts: _list[LfA2aV1Artifact]
    contextId: str
    history: _list[LfA2aV1Message]
    id: str
    metadata: dict[str, typing.Any]
    status: LfA2aV1TaskStatus

@typing.type_check_only
class LfA2aV1TaskPushNotificationConfig(typing.TypedDict, total=False):
    authentication: LfA2aV1AuthenticationInfo
    id: str
    taskId: str
    tenant: str
    token: str
    url: str

@typing.type_check_only
class LfA2aV1TaskStatus(typing.TypedDict, total=False):
    message: LfA2aV1Message
    state: typing.Literal[
        "TASK_STATE_UNSPECIFIED",
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
class ListAgentsResponse(typing.TypedDict, total=False):
    agents: _list[Agent]
    nextPageToken: str

@typing.type_check_only
class ListAppVersionsResponse(typing.TypedDict, total=False):
    appVersions: _list[AppVersion]
    nextPageToken: str

@typing.type_check_only
class ListAppsResponse(typing.TypedDict, total=False):
    apps: _list[App]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListChangelogsResponse(typing.TypedDict, total=False):
    changelogs: _list[Changelog]
    nextPageToken: str

@typing.type_check_only
class ListConversationsResponse(typing.TypedDict, total=False):
    conversations: _list[Conversation]
    nextPageToken: str

@typing.type_check_only
class ListDeploymentsResponse(typing.TypedDict, total=False):
    deployments: _list[Deployment]
    nextPageToken: str

@typing.type_check_only
class ListExamplesResponse(typing.TypedDict, total=False):
    examples: _list[Example]
    nextPageToken: str

@typing.type_check_only
class ListGuardrailsResponse(typing.TypedDict, total=False):
    guardrails: _list[Guardrail]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListToolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tools: _list[Tool]

@typing.type_check_only
class ListToolsetsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    toolsets: _list[Toolset]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LoggingSettings(typing.TypedDict, total=False):
    audioRecordingConfig: AudioRecordingConfig
    bigqueryExportSettings: BigQueryExportSettings
    cloudLoggingSettings: CloudLoggingSettings
    conversationLoggingSettings: ConversationLoggingSettings
    evaluationAudioRecordingConfig: AudioRecordingConfig
    metricAnalysisSettings: MetricAnalysisSettings
    redactionConfig: RedactionConfig
    unredactedAudioRecordingConfig: AudioRecordingConfig
    unredactedBigqueryExportSettings: BigQueryExportSettings

@typing.type_check_only
class McpTool(typing.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    customHeaders: dict[str, typing.Any]
    description: str
    inputSchema: Schema
    name: str
    nameOverride: str
    outputSchema: Schema
    serverAddress: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "STALE"]
    tlsConfig: TlsConfig

@typing.type_check_only
class McpToolDefinition(typing.TypedDict, total=False):
    description: str
    inputSchema: Schema
    outputSchema: Schema

@typing.type_check_only
class McpToolOverride(typing.TypedDict, total=False):
    descriptionOverride: str
    nameOverride: str
    snapshot: McpToolDefinition
    tool: str

@typing.type_check_only
class McpToolset(typing.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    customHeaders: dict[str, typing.Any]
    serverAddress: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    tlsConfig: TlsConfig
    toolOverrides: _list[McpToolOverride]

@typing.type_check_only
class Message(typing.TypedDict, total=False):
    chunks: _list[Chunk]
    eventTime: str
    role: str

@typing.type_check_only
class MetricAnalysisSettings(typing.TypedDict, total=False):
    llmMetricsOptedOut: bool

@typing.type_check_only
class MockConfig(typing.TypedDict, total=False):
    mockedToolCalls: _list[MockedToolCall]
    unmatchedToolCallBehavior: typing.Literal[
        "UNMATCHED_TOOL_CALL_BEHAVIOR_UNSPECIFIED", "FAIL", "PASS_THROUGH"
    ]

@typing.type_check_only
class MockedToolCall(typing.TypedDict, total=False):
    expectedArgsPattern: dict[str, typing.Any]
    mockResponse: dict[str, typing.Any]
    tool: str
    toolId: str
    toolset: ToolsetTool

@typing.type_check_only
class ModelSettings(typing.TypedDict, total=False):
    model: str
    temperature: float

@typing.type_check_only
class OAuthConfig(typing.TypedDict, total=False):
    clientId: str
    clientSecretVersion: str
    oauthGrantType: typing.Literal["OAUTH_GRANT_TYPE_UNSPECIFIED", "CLIENT_CREDENTIAL"]
    scopes: _list[str]
    tokenEndpoint: str

@typing.type_check_only
class OpenApiTool(typing.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    description: str
    ignoreUnknownFields: bool
    name: str
    openApiSchema: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    tlsConfig: TlsConfig
    url: str

@typing.type_check_only
class OpenApiToolset(typing.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    ignoreUnknownFields: bool
    openApiSchema: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    tlsConfig: TlsConfig
    url: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str

@typing.type_check_only
class OutputAudioConfig(typing.TypedDict, total=False):
    audioEncoding: typing.Literal[
        "AUDIO_ENCODING_UNSPECIFIED", "LINEAR16", "MULAW", "ALAW"
    ]
    sampleRateHertz: int

@typing.type_check_only
class PythonCodeCondition(typing.TypedDict, total=False):
    pythonCode: str

@typing.type_check_only
class PythonFunction(typing.TypedDict, total=False):
    description: str
    name: str
    pythonCode: str
    serviceDirectoryConfig: ServiceDirectoryConfig

@typing.type_check_only
class RedactionConfig(typing.TypedDict, total=False):
    deidentifyTemplate: str
    enableRedaction: bool
    inspectTemplate: str

@typing.type_check_only
class RemoteAgentTool(typing.TypedDict, total=False):
    agentCard: AgentCard
    description: str
    name: str

@typing.type_check_only
class RestoreAppVersionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RetrieveToolSchemaRequest(typing.TypedDict, total=False):
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class RetrieveToolSchemaResponse(typing.TypedDict, total=False):
    inputSchema: Schema
    outputSchema: Schema
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class RetrieveToolsRequest(typing.TypedDict, total=False):
    bypassPersistenceConfig: bool
    toolIds: _list[str]

@typing.type_check_only
class RetrieveToolsResponse(typing.TypedDict, total=False):
    tools: _list[Tool]

@typing.type_check_only
class RunSessionRequest(typing.TypedDict, total=False):
    config: SessionConfig
    inputs: _list[SessionInput]

@typing.type_check_only
class RunSessionResponse(typing.TypedDict, total=False):
    outputs: _list[SessionOutput]

@typing.type_check_only
class Schema(typing.TypedDict, total=False):
    additionalProperties: Schema
    anyOf: _list[Schema]
    default: typing.Any
    defs: dict[str, typing.Any]
    description: str
    enum: _list[str]
    items: Schema
    maxItems: str
    maximum: float
    minItems: str
    minimum: float
    nullable: bool
    prefixItems: _list[Schema]
    properties: dict[str, typing.Any]
    ref: str
    required: _list[str]
    title: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "STRING", "INTEGER", "NUMBER", "BOOLEAN", "OBJECT", "ARRAY"
    ]
    uniqueItems: bool

@typing.type_check_only
class SecuritySettings(typing.TypedDict, total=False):
    createTime: str
    endpointControlPolicy: EndpointControlPolicy
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class ServiceAccountAuthConfig(typing.TypedDict, total=False):
    scopes: _list[str]
    serviceAccount: str

@typing.type_check_only
class ServiceAgentIdTokenAuthConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class ServiceDirectoryConfig(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class SessionConfig(typing.TypedDict, total=False):
    deployment: str
    enableTextStreaming: bool
    entryAgent: str
    excludeDiagnosticInfo: bool
    historicalContexts: _list[Message]
    inputAudioConfig: InputAudioConfig
    outputAudioConfig: OutputAudioConfig
    remoteDialogflowQueryParameters: SessionConfigRemoteDialogflowQueryParameters
    timeZone: str
    useToolFakes: bool

@typing.type_check_only
class SessionConfigRemoteDialogflowQueryParameters(typing.TypedDict, total=False):
    endUserMetadata: dict[str, typing.Any]
    payload: dict[str, typing.Any]
    webhookHeaders: dict[str, typing.Any]

@typing.type_check_only
class SessionInput(typing.TypedDict, total=False):
    audio: str
    blob: Blob
    dtmf: str
    event: Event
    image: Image
    text: str
    toolResponses: ToolResponses
    variables: dict[str, typing.Any]
    willContinue: bool

@typing.type_check_only
class SessionOutput(typing.TypedDict, total=False):
    audio: str
    citations: Citations
    context: _list[dict[str, typing.Any]]
    diagnosticInfo: SessionOutputDiagnosticInfo
    endSession: EndSession
    googleSearchSuggestions: GoogleSearchSuggestions
    payload: dict[str, typing.Any]
    text: str
    toolCalls: ToolCalls
    turnCompleted: bool
    turnIndex: int

@typing.type_check_only
class SessionOutputDiagnosticInfo(typing.TypedDict, total=False):
    messages: _list[Message]
    rootSpan: Span

@typing.type_check_only
class Span(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    childSpans: _list[Span]
    duration: str
    endTime: str
    name: str
    startTime: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SynthesizeSpeechConfig(typing.TypedDict, total=False):
    consentAudioGcsUri: str
    instruction: str
    model: str
    speakingRate: float
    voice: str
    voiceSampleGcsUri: str

@typing.type_check_only
class SystemTool(typing.TypedDict, total=False):
    description: str
    name: str

@typing.type_check_only
class TimeZoneSettings(typing.TypedDict, total=False):
    timeZone: str

@typing.type_check_only
class TlsConfig(typing.TypedDict, total=False):
    caCerts: _list[TlsConfigCaCert]

@typing.type_check_only
class TlsConfigCaCert(typing.TypedDict, total=False):
    cert: str
    displayName: str

@typing.type_check_only
class Tool(typing.TypedDict, total=False):
    agentTool: AgentTool
    clientFunction: ClientFunction
    connectorTool: ConnectorTool
    createTime: str
    dataStoreTool: DataStoreTool
    displayName: str
    etag: str
    executionType: typing.Literal[
        "EXECUTION_TYPE_UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
    ]
    fileSearchTool: FileSearchTool
    generatedSummary: str
    googleSearchTool: GoogleSearchTool
    mcpTool: McpTool
    name: str
    openApiTool: OpenApiTool
    pythonFunction: PythonFunction
    remoteAgentTool: RemoteAgentTool
    systemTool: SystemTool
    timeout: str
    toolFakeConfig: ToolFakeConfig
    updateTime: str
    widgetTool: WidgetTool

@typing.type_check_only
class ToolCall(typing.TypedDict, total=False):
    args: dict[str, typing.Any]
    displayName: str
    id: str
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class ToolCalls(typing.TypedDict, total=False):
    toolCalls: _list[ToolCall]

@typing.type_check_only
class ToolFakeConfig(typing.TypedDict, total=False):
    codeBlock: CodeBlock
    enableFakeMode: bool

@typing.type_check_only
class ToolResponse(typing.TypedDict, total=False):
    displayName: str
    id: str
    response: dict[str, typing.Any]
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class ToolResponses(typing.TypedDict, total=False):
    toolResponses: _list[ToolResponse]

@typing.type_check_only
class Toolset(typing.TypedDict, total=False):
    connectorToolset: ConnectorToolset
    createTime: str
    description: str
    displayName: str
    etag: str
    executionType: typing.Literal[
        "EXECUTION_TYPE_UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
    ]
    mcpToolset: McpToolset
    name: str
    openApiToolset: OpenApiToolset
    timeout: str
    toolFakeConfig: ToolFakeConfig
    updateTime: str

@typing.type_check_only
class ToolsetTool(typing.TypedDict, total=False):
    toolId: str
    toolset: str

@typing.type_check_only
class TransferRule(typing.TypedDict, total=False):
    childAgent: str
    deterministicTransfer: TransferRuleDeterministicTransfer
    direction: typing.Literal[
        "DIRECTION_UNSPECIFIED", "PARENT_TO_CHILD", "CHILD_TO_PARENT"
    ]
    disablePlannerTransfer: TransferRuleDisablePlannerTransfer

@typing.type_check_only
class TransferRuleDeterministicTransfer(typing.TypedDict, total=False):
    expressionCondition: ExpressionCondition
    pythonCodeCondition: PythonCodeCondition

@typing.type_check_only
class TransferRuleDisablePlannerTransfer(typing.TypedDict, total=False):
    expressionCondition: ExpressionCondition

@typing.type_check_only
class TriggerAction(typing.TypedDict, total=False):
    generativeAnswer: TriggerActionGenerativeAnswer
    respondImmediately: TriggerActionRespondImmediately
    transferAgent: TriggerActionTransferAgent

@typing.type_check_only
class TriggerActionGenerativeAnswer(typing.TypedDict, total=False):
    prompt: str

@typing.type_check_only
class TriggerActionRespondImmediately(typing.TypedDict, total=False):
    responses: _list[TriggerActionResponse]

@typing.type_check_only
class TriggerActionResponse(typing.TypedDict, total=False):
    disabled: bool
    text: str

@typing.type_check_only
class TriggerActionTransferAgent(typing.TypedDict, total=False):
    agent: str

@typing.type_check_only
class VpcScSettings(typing.TypedDict, total=False):
    allowedOrigins: _list[str]

@typing.type_check_only
class WebSearchQuery(typing.TypedDict, total=False):
    query: str
    uri: str

@typing.type_check_only
class WhatsAppCredentials(typing.TypedDict, total=False):
    authCode: str
    businessAccountId: str
    conversationProfileId: str
    phoneNumber: str
    pin: str
    wabaId: str

@typing.type_check_only
class WidgetTool(typing.TypedDict, total=False):
    dataMapping: WidgetToolDataMapping
    description: str
    name: str
    parameters: Schema
    textResponseConfig: WidgetToolTextResponseConfig
    uiConfig: dict[str, typing.Any]
    widgetType: typing.Literal[
        "WIDGET_TYPE_UNSPECIFIED",
        "CUSTOM",
        "PRODUCT_CAROUSEL",
        "PRODUCT_DETAILS",
        "QUICK_ACTIONS",
        "PRODUCT_COMPARISON",
        "ADVANCED_PRODUCT_DETAILS",
        "SHORT_FORM",
        "OVERALL_SATISFACTION",
        "ORDER_SUMMARY",
        "APPOINTMENT_DETAILS",
        "APPOINTMENT_SCHEDULER",
        "CONTACT_FORM",
    ]

@typing.type_check_only
class WidgetToolDataMapping(typing.TypedDict, total=False):
    fieldMappings: dict[str, typing.Any]
    mode: typing.Literal["MODE_UNSPECIFIED", "FIELD_MAPPING", "PYTHON_SCRIPT"]
    pythonFunction: PythonFunction
    pythonScript: str
    sourceToolName: str

@typing.type_check_only
class WidgetToolTextResponseConfig(typing.TypedDict, total=False):
    staticText: str
    textResponseInstruction: str
    type: typing.Literal["TYPE_UNSPECIFIED", "NONE", "LLM_GENERATED", "STATIC"]
