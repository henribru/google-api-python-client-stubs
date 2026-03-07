import typing

import typing_extensions

_list = list

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    connectionActionId: str
    entityOperation: ActionEntityOperation
    inputFields: _list[str]
    outputFields: _list[str]

@typing.type_check_only
class ActionEntityOperation(typing_extensions.TypedDict, total=False):
    entityId: str
    operation: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
    ]

@typing.type_check_only
class Agent(typing_extensions.TypedDict, total=False):
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

@typing.type_check_only
class AgentAgentToolset(typing_extensions.TypedDict, total=False):
    toolIds: _list[str]
    toolset: str

@typing.type_check_only
class AgentLlmAgent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AgentRemoteDialogflowAgent(typing_extensions.TypedDict, total=False):
    agent: str
    environmentId: str
    flowId: str
    inputVariableMapping: dict[str, typing.Any]
    outputVariableMapping: dict[str, typing.Any]
    respectResponseInterruptionSettings: bool

@typing.type_check_only
class AgentTransfer(typing_extensions.TypedDict, total=False):
    displayName: str
    targetAgent: str

@typing.type_check_only
class AmbientSoundConfig(typing_extensions.TypedDict, total=False):
    gcsUri: str
    prebuiltAmbientNoise: typing_extensions.Literal[
        "PREBUILT_AMBIENT_NOISE_UNSPECIFIED",
        "RETAIL_STORE",
        "CONVENTION_HALL",
        "OUTDOOR",
    ]
    prebuiltAmbientSound: str
    volumeGainDb: float

@typing.type_check_only
class ApiAuthentication(typing_extensions.TypedDict, total=False):
    apiKeyConfig: ApiKeyConfig
    bearerTokenConfig: BearerTokenConfig
    oauthConfig: OAuthConfig
    serviceAccountAuthConfig: ServiceAccountAuthConfig
    serviceAgentIdTokenAuthConfig: ServiceAgentIdTokenAuthConfig

@typing.type_check_only
class ApiKeyConfig(typing_extensions.TypedDict, total=False):
    apiKeySecretVersion: str
    keyName: str
    requestLocation: typing_extensions.Literal[
        "REQUEST_LOCATION_UNSPECIFIED", "HEADER", "QUERY_STRING"
    ]

@typing.type_check_only
class App(typing_extensions.TypedDict, total=False):
    audioProcessingConfig: AudioProcessingConfig
    clientCertificateSettings: ClientCertificateSettings
    createTime: str
    dataStoreSettings: DataStoreSettings
    defaultChannelProfile: ChannelProfile
    deploymentCount: int
    description: str
    displayName: str
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
    toolExecutionMode: typing_extensions.Literal[
        "TOOL_EXECUTION_MODE_UNSPECIFIED", "PARALLEL", "SEQUENTIAL"
    ]
    updateTime: str
    variableDeclarations: _list[AppVariableDeclaration]

@typing.type_check_only
class AppSnapshot(typing_extensions.TypedDict, total=False):
    agents: _list[Agent]
    app: App
    examples: _list[Example]
    guardrails: _list[Guardrail]
    tools: _list[Tool]
    toolsets: _list[Toolset]

@typing.type_check_only
class AppVariableDeclaration(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    schema: Schema

@typing.type_check_only
class AppVersion(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    description: str
    displayName: str
    etag: str
    name: str
    snapshot: AppSnapshot

@typing.type_check_only
class AudioProcessingConfig(typing_extensions.TypedDict, total=False):
    ambientSoundConfig: AmbientSoundConfig
    bargeInConfig: BargeInConfig
    inactivityTimeout: str
    synthesizeSpeechConfigs: dict[str, typing.Any]

@typing.type_check_only
class AudioRecordingConfig(typing_extensions.TypedDict, total=False):
    gcsBucket: str
    gcsPathPrefix: str

@typing.type_check_only
class BargeInConfig(typing_extensions.TypedDict, total=False):
    bargeInAwareness: bool
    disableBargeIn: bool

@typing.type_check_only
class BatchDeleteConversationsRequest(typing_extensions.TypedDict, total=False):
    conversations: _list[str]

@typing.type_check_only
class BearerTokenConfig(typing_extensions.TypedDict, total=False):
    token: str

@typing.type_check_only
class BigQueryExportSettings(typing_extensions.TypedDict, total=False):
    dataset: str
    enabled: bool
    project: str

@typing.type_check_only
class Blob(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class Callback(typing_extensions.TypedDict, total=False):
    description: str
    disabled: bool
    proactiveExecutionEnabled: bool
    pythonCode: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Changelog(typing_extensions.TypedDict, total=False):
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
class ChannelProfile(typing_extensions.TypedDict, total=False):
    channelType: typing_extensions.Literal[
        "UNKNOWN",
        "WEB_UI",
        "API",
        "TWILIO",
        "GOOGLE_TELEPHONY_PLATFORM",
        "CONTACT_CENTER_AS_A_SERVICE",
        "FIVE9",
    ]
    disableBargeInControl: bool
    disableDtmf: bool
    noiseSuppressionLevel: str
    personaProperty: ChannelProfilePersonaProperty
    profileId: str
    webWidgetConfig: ChannelProfileWebWidgetConfig

@typing.type_check_only
class ChannelProfilePersonaProperty(typing_extensions.TypedDict, total=False):
    persona: typing_extensions.Literal["UNKNOWN", "CONCISE", "CHATTY"]

@typing.type_check_only
class ChannelProfileWebWidgetConfig(typing_extensions.TypedDict, total=False):
    modality: typing_extensions.Literal[
        "MODALITY_UNSPECIFIED", "CHAT_AND_VOICE", "VOICE_ONLY", "CHAT_ONLY"
    ]
    securitySettings: ChannelProfileWebWidgetConfigSecuritySettings
    theme: typing_extensions.Literal["THEME_UNSPECIFIED", "LIGHT", "DARK"]
    webWidgetTitle: str

@typing.type_check_only
class ChannelProfileWebWidgetConfigSecuritySettings(
    typing_extensions.TypedDict, total=False
):
    allowedOrigins: _list[str]
    enableOriginCheck: bool
    enablePublicAccess: bool
    enableRecaptcha: bool

@typing.type_check_only
class Chunk(typing_extensions.TypedDict, total=False):
    agentTransfer: AgentTransfer
    defaultVariables: dict[str, typing.Any]
    image: Image
    payload: dict[str, typing.Any]
    text: str
    toolCall: ToolCall
    toolResponse: ToolResponse
    transcript: str
    updatedVariables: dict[str, typing.Any]

@typing.type_check_only
class Citations(typing_extensions.TypedDict, total=False):
    citedChunks: _list[CitationsCitedChunk]

@typing.type_check_only
class CitationsCitedChunk(typing_extensions.TypedDict, total=False):
    text: str
    title: str
    uri: str

@typing.type_check_only
class ClientCertificateSettings(typing_extensions.TypedDict, total=False):
    passphrase: str
    privateKey: str
    tlsCertificate: str

@typing.type_check_only
class ClientFunction(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    parameters: Schema
    response: Schema

@typing.type_check_only
class CloudLoggingSettings(typing_extensions.TypedDict, total=False):
    enableCloudLogging: bool

@typing.type_check_only
class CodeBlock(typing_extensions.TypedDict, total=False):
    pythonCode: str

@typing.type_check_only
class ConnectorTool(typing_extensions.TypedDict, total=False):
    action: Action
    authConfig: EndUserAuthConfig
    connection: str
    description: str
    name: str

@typing.type_check_only
class ConnectorToolset(typing_extensions.TypedDict, total=False):
    authConfig: EndUserAuthConfig
    connection: str
    connectorActions: _list[Action]

@typing.type_check_only
class Conversation(typing_extensions.TypedDict, total=False):
    appVersion: str
    channelType: typing_extensions.Literal[
        "CHANNEL_TYPE_UNSPECIFIED", "TEXT", "AUDIO", "MULTIMODAL"
    ]
    deployment: str
    endTime: str
    entryAgent: str
    inputTypes: _list[
        typing_extensions.Literal[
            "INPUT_TYPE_UNSPECIFIED",
            "INPUT_TYPE_TEXT",
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
    source: typing_extensions.Literal["SOURCE_UNSPECIFIED", "LIVE", "SIMULATOR", "EVAL"]
    startTime: str
    turnCount: int
    turns: _list[ConversationTurn]

@typing.type_check_only
class ConversationLoggingSettings(typing_extensions.TypedDict, total=False):
    disableConversationLogging: bool

@typing.type_check_only
class ConversationTurn(typing_extensions.TypedDict, total=False):
    messages: _list[Message]
    rootSpan: Span

@typing.type_check_only
class DataStore(typing_extensions.TypedDict, total=False):
    connectorConfig: DataStoreConnectorConfig
    createTime: str
    displayName: str
    documentProcessingMode: typing_extensions.Literal[
        "DOCUMENT_PROCESSING_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    name: str
    type: typing_extensions.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED", "PUBLIC_WEB", "UNSTRUCTURED", "FAQ", "CONNECTOR"
    ]

@typing.type_check_only
class DataStoreConnectorConfig(typing_extensions.TypedDict, total=False):
    collection: str
    collectionDisplayName: str
    dataSource: str

@typing.type_check_only
class DataStoreSettings(typing_extensions.TypedDict, total=False):
    engines: _list[DataStoreSettingsEngine]

@typing.type_check_only
class DataStoreSettingsEngine(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "ENGINE_TYPE_SEARCH", "ENGINE_TYPE_CHAT"
    ]

@typing.type_check_only
class DataStoreTool(typing_extensions.TypedDict, total=False):
    boostSpecs: _list[DataStoreToolBoostSpecs]
    dataStoreSource: DataStoreToolDataStoreSource
    description: str
    engineSource: DataStoreToolEngineSource
    filterParameterBehavior: typing_extensions.Literal[
        "FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED", "ALWAYS_INCLUDE", "NEVER_INCLUDE"
    ]
    modalityConfigs: _list[DataStoreToolModalityConfig]
    name: str

@typing.type_check_only
class DataStoreToolBoostSpec(typing_extensions.TypedDict, total=False):
    conditionBoostSpecs: _list[DataStoreToolBoostSpecConditionBoostSpec]

@typing.type_check_only
class DataStoreToolBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: DataStoreToolBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class DataStoreToolBoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        DataStoreToolBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class DataStoreToolBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class DataStoreToolBoostSpecs(typing_extensions.TypedDict, total=False):
    dataStores: _list[str]
    spec: _list[DataStoreToolBoostSpec]

@typing.type_check_only
class DataStoreToolDataStoreSource(typing_extensions.TypedDict, total=False):
    dataStore: DataStore
    filter: str

@typing.type_check_only
class DataStoreToolEngineSource(typing_extensions.TypedDict, total=False):
    dataStoreSources: _list[DataStoreToolDataStoreSource]
    engine: str
    filter: str

@typing.type_check_only
class DataStoreToolGroundingConfig(typing_extensions.TypedDict, total=False):
    disabled: bool
    groundingLevel: float

@typing.type_check_only
class DataStoreToolModalityConfig(typing_extensions.TypedDict, total=False):
    groundingConfig: DataStoreToolGroundingConfig
    modalityType: typing_extensions.Literal[
        "MODALITY_TYPE_UNSPECIFIED", "TEXT", "AUDIO"
    ]
    rewriterConfig: DataStoreToolRewriterConfig
    summarizationConfig: DataStoreToolSummarizationConfig

@typing.type_check_only
class DataStoreToolRewriterConfig(typing_extensions.TypedDict, total=False):
    disabled: bool
    modelSettings: ModelSettings
    prompt: str

@typing.type_check_only
class DataStoreToolSummarizationConfig(typing_extensions.TypedDict, total=False):
    disabled: bool
    modelSettings: ModelSettings
    prompt: str

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    appVersion: str
    channelProfile: ChannelProfile
    createTime: str
    displayName: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EndSession(typing_extensions.TypedDict, total=False):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class EndUserAuthConfig(typing_extensions.TypedDict, total=False):
    oauth2AuthCodeConfig: EndUserAuthConfigOauth2AuthCodeConfig
    oauth2JwtBearerConfig: EndUserAuthConfigOauth2JwtBearerConfig

@typing.type_check_only
class EndUserAuthConfigOauth2AuthCodeConfig(typing_extensions.TypedDict, total=False):
    oauthToken: str

@typing.type_check_only
class EndUserAuthConfigOauth2JwtBearerConfig(typing_extensions.TypedDict, total=False):
    clientKey: str
    issuer: str
    subject: str

@typing.type_check_only
class EvaluationMetricsThresholds(typing_extensions.TypedDict, total=False):
    goldenEvaluationMetricsThresholds: (
        EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholds
    )
    goldenHallucinationMetricBehavior: typing_extensions.Literal[
        "HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    hallucinationMetricBehavior: typing_extensions.Literal[
        "HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    scenarioHallucinationMetricBehavior: typing_extensions.Literal[
        "HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED", "DISABLED", "ENABLED"
    ]

@typing.type_check_only
class EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholds(
    typing_extensions.TypedDict, total=False
):
    expectationLevelMetricsThresholds: EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholds
    turnLevelMetricsThresholds: EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholds

@typing.type_check_only
class EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholds(
    typing_extensions.TypedDict, total=False
):
    toolInvocationParameterCorrectnessThreshold: float

@typing.type_check_only
class EvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholds(
    typing_extensions.TypedDict, total=False
):
    overallToolInvocationCorrectnessThreshold: float
    semanticSimilarityChannel: typing_extensions.Literal[
        "SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED", "TEXT", "AUDIO"
    ]
    semanticSimilaritySuccessThreshold: int

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    event: str

@typing.type_check_only
class Example(typing_extensions.TypedDict, total=False):
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
class ExecuteToolRequest(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class ExecuteToolResponse(typing_extensions.TypedDict, total=False):
    response: dict[str, typing.Any]
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class ExportAppRequest(typing_extensions.TypedDict, total=False):
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "JSON", "YAML"]
    gcsUri: str

@typing.type_check_only
class ExportAppResponse(typing_extensions.TypedDict, total=False):
    appContent: str
    appUri: str

@typing.type_check_only
class ExpressionCondition(typing_extensions.TypedDict, total=False):
    expression: str

@typing.type_check_only
class FileSearchTool(typing_extensions.TypedDict, total=False):
    corpusType: typing_extensions.Literal[
        "CORPUS_TYPE_UNSPECIFIED", "USER_OWNED", "FULLY_MANAGED"
    ]
    description: str
    fileCorpus: str
    name: str

@typing.type_check_only
class GenerateChatTokenRequest(typing_extensions.TypedDict, total=False):
    deployment: str
    recaptchaToken: str

@typing.type_check_only
class GenerateChatTokenResponse(typing_extensions.TypedDict, total=False):
    chatToken: str
    expireTime: str

@typing.type_check_only
class GoogleSearchSuggestions(typing_extensions.TypedDict, total=False):
    htmls: _list[str]
    webSearchQueries: _list[WebSearchQuery]

@typing.type_check_only
class GoogleSearchTool(typing_extensions.TypedDict, total=False):
    contextUrls: _list[str]
    description: str
    excludeDomains: _list[str]
    name: str
    preferredDomains: _list[str]
    promptConfig: GoogleSearchToolPromptConfig

@typing.type_check_only
class GoogleSearchToolPromptConfig(typing_extensions.TypedDict, total=False):
    textPrompt: str
    voicePrompt: str

@typing.type_check_only
class Guardrail(typing_extensions.TypedDict, total=False):
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
class GuardrailCodeCallback(typing_extensions.TypedDict, total=False):
    afterAgentCallback: Callback
    afterModelCallback: Callback
    beforeAgentCallback: Callback
    beforeModelCallback: Callback

@typing.type_check_only
class GuardrailContentFilter(typing_extensions.TypedDict, total=False):
    bannedContents: _list[str]
    bannedContentsInAgentResponse: _list[str]
    bannedContentsInUserInput: _list[str]
    disregardDiacritics: bool
    matchType: typing_extensions.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "SIMPLE_STRING_MATCH",
        "WORD_BOUNDARY_STRING_MATCH",
        "REGEXP_MATCH",
    ]

@typing.type_check_only
class GuardrailLlmPolicy(typing_extensions.TypedDict, total=False):
    allowShortUtterance: bool
    failOpen: bool
    maxConversationMessages: int
    modelSettings: ModelSettings
    policyScope: typing_extensions.Literal[
        "POLICY_SCOPE_UNSPECIFIED",
        "USER_QUERY",
        "AGENT_RESPONSE",
        "USER_QUERY_AND_AGENT_RESPONSE",
    ]
    prompt: str

@typing.type_check_only
class GuardrailLlmPromptSecurity(typing_extensions.TypedDict, total=False):
    customPolicy: GuardrailLlmPolicy
    defaultSettings: GuardrailLlmPromptSecurityDefaultSecuritySettings
    failOpen: bool

@typing.type_check_only
class GuardrailLlmPromptSecurityDefaultSecuritySettings(
    typing_extensions.TypedDict, total=False
):
    defaultPromptTemplate: str

@typing.type_check_only
class GuardrailModelSafety(typing_extensions.TypedDict, total=False):
    safetySettings: _list[GuardrailModelSafetySafetySetting]

@typing.type_check_only
class GuardrailModelSafetySafetySetting(typing_extensions.TypedDict, total=False):
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
        "OFF",
    ]

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class ImportAppRequest(typing_extensions.TypedDict, total=False):
    appContent: str
    appId: str
    displayName: str
    gcsUri: str
    ignoreAppLock: bool
    importOptions: ImportAppRequestImportOptions

@typing.type_check_only
class ImportAppRequestImportOptions(typing_extensions.TypedDict, total=False):
    conflictResolutionStrategy: typing_extensions.Literal[
        "CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED", "REPLACE", "OVERWRITE"
    ]

@typing.type_check_only
class ImportAppResponse(typing_extensions.TypedDict, total=False):
    name: str
    warnings: _list[str]

@typing.type_check_only
class InputAudioConfig(typing_extensions.TypedDict, total=False):
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED", "LINEAR16", "MULAW", "ALAW"
    ]
    noiseSuppressionLevel: str
    sampleRateHertz: int

@typing.type_check_only
class LanguageSettings(typing_extensions.TypedDict, total=False):
    defaultLanguageCode: str
    enableMultilingualSupport: bool
    fallbackAction: str
    supportedLanguageCodes: _list[str]

@typing.type_check_only
class ListAgentsResponse(typing_extensions.TypedDict, total=False):
    agents: _list[Agent]
    nextPageToken: str

@typing.type_check_only
class ListAppVersionsResponse(typing_extensions.TypedDict, total=False):
    appVersions: _list[AppVersion]
    nextPageToken: str

@typing.type_check_only
class ListAppsResponse(typing_extensions.TypedDict, total=False):
    apps: _list[App]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListChangelogsResponse(typing_extensions.TypedDict, total=False):
    changelogs: _list[Changelog]
    nextPageToken: str

@typing.type_check_only
class ListConversationsResponse(typing_extensions.TypedDict, total=False):
    conversations: _list[Conversation]
    nextPageToken: str

@typing.type_check_only
class ListDeploymentsResponse(typing_extensions.TypedDict, total=False):
    deployments: _list[Deployment]
    nextPageToken: str

@typing.type_check_only
class ListExamplesResponse(typing_extensions.TypedDict, total=False):
    examples: _list[Example]
    nextPageToken: str

@typing.type_check_only
class ListGuardrailsResponse(typing_extensions.TypedDict, total=False):
    guardrails: _list[Guardrail]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListToolsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tools: _list[Tool]

@typing.type_check_only
class ListToolsetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    toolsets: _list[Toolset]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LoggingSettings(typing_extensions.TypedDict, total=False):
    audioRecordingConfig: AudioRecordingConfig
    bigqueryExportSettings: BigQueryExportSettings
    cloudLoggingSettings: CloudLoggingSettings
    conversationLoggingSettings: ConversationLoggingSettings
    evaluationAudioRecordingConfig: AudioRecordingConfig
    metricAnalysisSettings: MetricAnalysisSettings
    redactionConfig: RedactionConfig

@typing.type_check_only
class McpTool(typing_extensions.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    description: str
    inputSchema: Schema
    name: str
    outputSchema: Schema
    serverAddress: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    tlsConfig: TlsConfig

@typing.type_check_only
class McpToolset(typing_extensions.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    serverAddress: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    tlsConfig: TlsConfig

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    chunks: _list[Chunk]
    eventTime: str
    role: str

@typing.type_check_only
class MetricAnalysisSettings(typing_extensions.TypedDict, total=False):
    llmMetricsOptedOut: bool

@typing.type_check_only
class ModelSettings(typing_extensions.TypedDict, total=False):
    model: str
    temperature: float

@typing.type_check_only
class OAuthConfig(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecretVersion: str
    oauthGrantType: typing_extensions.Literal[
        "OAUTH_GRANT_TYPE_UNSPECIFIED", "CLIENT_CREDENTIAL"
    ]
    scopes: _list[str]
    tokenEndpoint: str

@typing.type_check_only
class Omnichannel(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    integrationConfig: OmnichannelIntegrationConfig
    name: str
    updateTime: str

@typing.type_check_only
class OmnichannelIntegrationConfig(typing_extensions.TypedDict, total=False):
    channelConfigs: dict[str, typing.Any]
    routingConfigs: dict[str, typing.Any]
    subscriberConfigs: dict[str, typing.Any]

@typing.type_check_only
class OmnichannelIntegrationConfigCesAppConfig(
    typing_extensions.TypedDict, total=False
):
    app: str

@typing.type_check_only
class OmnichannelIntegrationConfigChannelConfig(
    typing_extensions.TypedDict, total=False
):
    whatsappConfig: OmnichannelIntegrationConfigWhatsappConfig

@typing.type_check_only
class OmnichannelIntegrationConfigRoutingConfig(
    typing_extensions.TypedDict, total=False
):
    subscriberKey: str

@typing.type_check_only
class OmnichannelIntegrationConfigSubscriberConfig(
    typing_extensions.TypedDict, total=False
):
    cesAppConfig: OmnichannelIntegrationConfigCesAppConfig

@typing.type_check_only
class OmnichannelIntegrationConfigWhatsappConfig(
    typing_extensions.TypedDict, total=False
):
    metaBusinessPortfolioId: str
    phoneNumber: str
    phoneNumberId: str
    webhookVerifyToken: str
    whatsappBusinessAccountId: str
    whatsappBusinessToken: str

@typing.type_check_only
class OmnichannelOperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str

@typing.type_check_only
class OpenApiTool(typing_extensions.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    description: str
    ignoreUnknownFields: bool
    name: str
    openApiSchema: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    tlsConfig: TlsConfig
    url: str

@typing.type_check_only
class OpenApiToolset(typing_extensions.TypedDict, total=False):
    apiAuthentication: ApiAuthentication
    ignoreUnknownFields: bool
    openApiSchema: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    tlsConfig: TlsConfig
    url: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str

@typing.type_check_only
class OutputAudioConfig(typing_extensions.TypedDict, total=False):
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED", "LINEAR16", "MULAW", "ALAW"
    ]
    sampleRateHertz: int

@typing.type_check_only
class PythonCodeCondition(typing_extensions.TypedDict, total=False):
    pythonCode: str

@typing.type_check_only
class PythonFunction(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    pythonCode: str

@typing.type_check_only
class RedactionConfig(typing_extensions.TypedDict, total=False):
    deidentifyTemplate: str
    enableRedaction: bool
    inspectTemplate: str

@typing.type_check_only
class RestoreAppVersionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetrieveToolSchemaRequest(typing_extensions.TypedDict, total=False):
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class RetrieveToolSchemaResponse(typing_extensions.TypedDict, total=False):
    inputSchema: Schema
    outputSchema: Schema
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class RetrieveToolsRequest(typing_extensions.TypedDict, total=False):
    toolIds: _list[str]

@typing.type_check_only
class RetrieveToolsResponse(typing_extensions.TypedDict, total=False):
    tools: _list[Tool]

@typing.type_check_only
class RunSessionRequest(typing_extensions.TypedDict, total=False):
    config: SessionConfig
    inputs: _list[SessionInput]

@typing.type_check_only
class RunSessionResponse(typing_extensions.TypedDict, total=False):
    outputs: _list[SessionOutput]

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
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
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STRING", "INTEGER", "NUMBER", "BOOLEAN", "OBJECT", "ARRAY"
    ]
    uniqueItems: bool

@typing.type_check_only
class ServiceAccountAuthConfig(typing_extensions.TypedDict, total=False):
    scopes: _list[str]
    serviceAccount: str

@typing.type_check_only
class ServiceAgentIdTokenAuthConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ServiceDirectoryConfig(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class SessionConfig(typing_extensions.TypedDict, total=False):
    deployment: str
    entryAgent: str
    historicalContexts: _list[Message]
    inputAudioConfig: InputAudioConfig
    outputAudioConfig: OutputAudioConfig
    remoteDialogflowQueryParameters: SessionConfigRemoteDialogflowQueryParameters
    timeZone: str

@typing.type_check_only
class SessionConfigRemoteDialogflowQueryParameters(
    typing_extensions.TypedDict, total=False
):
    endUserMetadata: dict[str, typing.Any]
    payload: dict[str, typing.Any]
    webhookHeaders: dict[str, typing.Any]

@typing.type_check_only
class SessionInput(typing_extensions.TypedDict, total=False):
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
class SessionOutput(typing_extensions.TypedDict, total=False):
    audio: str
    citations: Citations
    diagnosticInfo: SessionOutputDiagnosticInfo
    endSession: EndSession
    googleSearchSuggestions: GoogleSearchSuggestions
    payload: dict[str, typing.Any]
    text: str
    toolCalls: ToolCalls
    turnCompleted: bool
    turnIndex: int

@typing.type_check_only
class SessionOutputDiagnosticInfo(typing_extensions.TypedDict, total=False):
    messages: _list[Message]
    rootSpan: Span

@typing.type_check_only
class Span(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    childSpans: _list[Span]
    duration: str
    endTime: str
    name: str
    startTime: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SynthesizeSpeechConfig(typing_extensions.TypedDict, total=False):
    speakingRate: float
    voice: str

@typing.type_check_only
class SystemTool(typing_extensions.TypedDict, total=False):
    description: str
    name: str

@typing.type_check_only
class TimeZoneSettings(typing_extensions.TypedDict, total=False):
    timeZone: str

@typing.type_check_only
class TlsConfig(typing_extensions.TypedDict, total=False):
    caCerts: _list[TlsConfigCaCert]

@typing.type_check_only
class TlsConfigCaCert(typing_extensions.TypedDict, total=False):
    cert: str
    displayName: str

@typing.type_check_only
class Tool(typing_extensions.TypedDict, total=False):
    clientFunction: ClientFunction
    connectorTool: ConnectorTool
    createTime: str
    dataStoreTool: DataStoreTool
    displayName: str
    etag: str
    executionType: typing_extensions.Literal[
        "EXECUTION_TYPE_UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
    ]
    fileSearchTool: FileSearchTool
    generatedSummary: str
    googleSearchTool: GoogleSearchTool
    mcpTool: McpTool
    name: str
    openApiTool: OpenApiTool
    pythonFunction: PythonFunction
    systemTool: SystemTool
    toolFakeConfig: ToolFakeConfig
    updateTime: str
    widgetTool: WidgetTool

@typing.type_check_only
class ToolCall(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    displayName: str
    id: str
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class ToolCalls(typing_extensions.TypedDict, total=False):
    toolCalls: _list[ToolCall]

@typing.type_check_only
class ToolFakeConfig(typing_extensions.TypedDict, total=False):
    codeBlock: CodeBlock
    enableFakeMode: bool

@typing.type_check_only
class ToolResponse(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str
    response: dict[str, typing.Any]
    tool: str
    toolsetTool: ToolsetTool

@typing.type_check_only
class ToolResponses(typing_extensions.TypedDict, total=False):
    toolResponses: _list[ToolResponse]

@typing.type_check_only
class Toolset(typing_extensions.TypedDict, total=False):
    connectorToolset: ConnectorToolset
    createTime: str
    description: str
    displayName: str
    etag: str
    executionType: typing_extensions.Literal[
        "EXECUTION_TYPE_UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
    ]
    mcpToolset: McpToolset
    name: str
    openApiToolset: OpenApiToolset
    toolFakeConfig: ToolFakeConfig
    updateTime: str

@typing.type_check_only
class ToolsetTool(typing_extensions.TypedDict, total=False):
    toolId: str
    toolset: str

@typing.type_check_only
class TransferRule(typing_extensions.TypedDict, total=False):
    childAgent: str
    deterministicTransfer: TransferRuleDeterministicTransfer
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "PARENT_TO_CHILD", "CHILD_TO_PARENT"
    ]
    disablePlannerTransfer: TransferRuleDisablePlannerTransfer

@typing.type_check_only
class TransferRuleDeterministicTransfer(typing_extensions.TypedDict, total=False):
    expressionCondition: ExpressionCondition
    pythonCodeCondition: PythonCodeCondition

@typing.type_check_only
class TransferRuleDisablePlannerTransfer(typing_extensions.TypedDict, total=False):
    expressionCondition: ExpressionCondition

@typing.type_check_only
class TriggerAction(typing_extensions.TypedDict, total=False):
    generativeAnswer: TriggerActionGenerativeAnswer
    respondImmediately: TriggerActionRespondImmediately
    transferAgent: TriggerActionTransferAgent

@typing.type_check_only
class TriggerActionGenerativeAnswer(typing_extensions.TypedDict, total=False):
    prompt: str

@typing.type_check_only
class TriggerActionRespondImmediately(typing_extensions.TypedDict, total=False):
    responses: _list[TriggerActionResponse]

@typing.type_check_only
class TriggerActionResponse(typing_extensions.TypedDict, total=False):
    disabled: bool
    text: str

@typing.type_check_only
class TriggerActionTransferAgent(typing_extensions.TypedDict, total=False):
    agent: str

@typing.type_check_only
class WebSearchQuery(typing_extensions.TypedDict, total=False):
    query: str
    uri: str

@typing.type_check_only
class WidgetTool(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    parameters: Schema
    widgetType: typing_extensions.Literal[
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
    ]
