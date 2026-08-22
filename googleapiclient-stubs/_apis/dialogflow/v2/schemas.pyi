import typing

_list = list

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettings(typing.TypedDict, total=False):
    audioExportGcsDestination: GoogleCloudDialogflowCxV3GcsDestination
    dtmfSettings: GoogleCloudDialogflowCxV3AdvancedSettingsDtmfSettings
    loggingSettings: GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettings
    speechSettings: GoogleCloudDialogflowCxV3AdvancedSettingsSpeechSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettingsDtmfSettings(
    typing.TypedDict, total=False
):
    enabled: bool
    endpointingTimeoutDuration: str
    finishDigit: str
    interdigitTimeoutDuration: str
    maxDigits: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettings(
    typing.TypedDict, total=False
):
    enableConsentBasedRedaction: bool
    enableInteractionLogging: bool
    enableStackdriverLogging: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettingsSpeechSettings(
    typing.TypedDict, total=False
):
    endpointerSensitivity: int
    models: dict[str, typing.Any]
    noSpeechTimeout: str
    useTimeoutBasedEndpointing: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3AudioInput(typing.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowCxV3InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3BargeInConfig(typing.TypedDict, total=False):
    noBargeInDuration: str
    totalDuration: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesMetadata(typing.TypedDict, total=False):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesResponse(typing.TypedDict, total=False):
    results: _list[GoogleCloudDialogflowCxV3TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ContinuousTestResult(typing.TypedDict, total=False):
    name: str
    result: typing.Literal["AGGREGATED_TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    runTime: str
    testCaseResults: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationSignals(typing.TypedDict, total=False):
    turnSignals: GoogleCloudDialogflowCxV3TurnSignals

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationTurn(typing.TypedDict, total=False):
    userInput: GoogleCloudDialogflowCxV3ConversationTurnUserInput
    virtualAgentOutput: GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutput

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationTurnUserInput(typing.TypedDict, total=False):
    enableSentimentAnalysis: bool
    injectedParameters: dict[str, typing.Any]
    input: GoogleCloudDialogflowCxV3QueryInput
    isWebhookEnabled: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutput(
    typing.TypedDict, total=False
):
    currentPage: GoogleCloudDialogflowCxV3Page
    diagnosticInfo: dict[str, typing.Any]
    differences: _list[GoogleCloudDialogflowCxV3TestRunDifference]
    sessionParameters: dict[str, typing.Any]
    status: GoogleRpcStatus
    textResponses: _list[GoogleCloudDialogflowCxV3ResponseMessageText]
    triggeredIntent: GoogleCloudDialogflowCxV3Intent

@typing.type_check_only
class GoogleCloudDialogflowCxV3CreateVersionOperationMetadata(
    typing.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnection(typing.TypedDict, total=False):
    dataStore: str
    dataStoreType: typing.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED", "PUBLIC_WEB", "UNSTRUCTURED", "STRUCTURED"
    ]
    documentProcessingMode: typing.Literal[
        "DOCUMENT_PROCESSING_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowMetadata(typing.TypedDict, total=False):
    testErrors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowResponse(typing.TypedDict, total=False):
    deployment: str
    environment: GoogleCloudDialogflowCxV3Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3DtmfInput(typing.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Environment(typing.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    testCasesConfig: GoogleCloudDialogflowCxV3EnvironmentTestCasesConfig
    updateTime: str
    versionConfigs: _list[GoogleCloudDialogflowCxV3EnvironmentVersionConfig]
    webhookConfig: GoogleCloudDialogflowCxV3EnvironmentWebhookConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3EnvironmentTestCasesConfig(
    typing.TypedDict, total=False
):
    enableContinuousRun: bool
    enablePredeploymentRun: bool
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3EnvironmentVersionConfig(typing.TypedDict, total=False):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3EnvironmentWebhookConfig(typing.TypedDict, total=False):
    webhookOverrides: _list[GoogleCloudDialogflowCxV3Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3EventHandler(typing.TypedDict, total=False):
    event: str
    name: str
    targetFlow: str
    targetPage: str
    targetPlaybook: str
    triggerFulfillment: GoogleCloudDialogflowCxV3Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3EventInput(typing.TypedDict, total=False):
    event: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportAgentResponse(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str
    commitSha: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportEntityTypesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportEntityTypesResponse(typing.TypedDict, total=False):
    entityTypesContent: GoogleCloudDialogflowCxV3InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportFlowResponse(typing.TypedDict, total=False):
    flowContent: str
    flowUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportIntentsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportIntentsResponse(typing.TypedDict, total=False):
    intentsContent: GoogleCloudDialogflowCxV3InlineDestination
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesResponse(typing.TypedDict, total=False):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Form(typing.TypedDict, total=False):
    parameters: _list[GoogleCloudDialogflowCxV3FormParameter]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FormParameter(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    defaultValue: typing.Any
    displayName: str
    entityType: str
    fillBehavior: GoogleCloudDialogflowCxV3FormParameterFillBehavior
    isList: bool
    redact: bool
    required: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3FormParameterFillBehavior(typing.TypedDict, total=False):
    initialPromptFulfillment: GoogleCloudDialogflowCxV3Fulfillment
    repromptEventHandlers: _list[GoogleCloudDialogflowCxV3EventHandler]

@typing.type_check_only
class GoogleCloudDialogflowCxV3Fulfillment(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    codeBlockFunction: str
    conditionalCases: _list[GoogleCloudDialogflowCxV3FulfillmentConditionalCases]
    enableGenerativeFallback: bool
    generators: _list[GoogleCloudDialogflowCxV3FulfillmentGeneratorSettings]
    messages: _list[GoogleCloudDialogflowCxV3ResponseMessage]
    returnPartialResponses: bool
    setParameterActions: _list[GoogleCloudDialogflowCxV3FulfillmentSetParameterAction]
    tag: str
    webhook: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentConditionalCases(
    typing.TypedDict, total=False
):
    cases: _list[GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCase(
    typing.TypedDict, total=False
):
    caseContent: _list[
        GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContent
    ]
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContent(
    typing.TypedDict, total=False
):
    additionalCases: GoogleCloudDialogflowCxV3FulfillmentConditionalCases
    message: GoogleCloudDialogflowCxV3ResponseMessage

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentGeneratorSettings(
    typing.TypedDict, total=False
):
    generator: str
    inputParameters: dict[str, typing.Any]
    outputParameter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentSetParameterAction(
    typing.TypedDict, total=False
):
    parameter: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3GcsDestination(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesResponse(typing.TypedDict, total=False):
    conflictingResources: (
        GoogleCloudDialogflowCxV3ImportEntityTypesResponseConflictingResources
    )
    entityTypes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesResponseConflictingResources(
    typing.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    entityTypeDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportFlowResponse(typing.TypedDict, total=False):
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsResponse(typing.TypedDict, total=False):
    conflictingResources: (
        GoogleCloudDialogflowCxV3ImportIntentsResponseConflictingResources
    )
    intents: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsResponseConflictingResources(
    typing.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    intentDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportTestCasesMetadata(typing.TypedDict, total=False):
    errors: _list[GoogleCloudDialogflowCxV3TestCaseError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportTestCasesResponse(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3InlineDestination(typing.TypedDict, total=False):
    content: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3InputAudioConfig(typing.TypedDict, total=False):
    audioEncoding: typing.Literal[
        "AUDIO_ENCODING_UNSPECIFIED",
        "AUDIO_ENCODING_LINEAR_16",
        "AUDIO_ENCODING_FLAC",
        "AUDIO_ENCODING_MULAW",
        "AUDIO_ENCODING_AMR",
        "AUDIO_ENCODING_AMR_WB",
        "AUDIO_ENCODING_OGG_OPUS",
        "AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE",
        "AUDIO_ENCODING_ALAW",
    ]
    bargeInConfig: GoogleCloudDialogflowCxV3BargeInConfig
    enableWordInfo: bool
    model: str
    modelVariant: typing.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]
    optOutConformerModelMigration: bool
    phraseHints: _list[str]
    sampleRateHertz: int
    singleUtterance: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3Intent(typing.TypedDict, total=False):
    description: str
    displayName: str
    dtmfPattern: str
    isFallback: bool
    labels: dict[str, typing.Any]
    name: str
    parameters: _list[GoogleCloudDialogflowCxV3IntentParameter]
    priority: int
    trainingPhrases: _list[GoogleCloudDialogflowCxV3IntentTrainingPhrase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentInput(typing.TypedDict, total=False):
    intent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentParameter(typing.TypedDict, total=False):
    entityType: str
    id: str
    isList: bool
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentTrainingPhrase(typing.TypedDict, total=False):
    id: str
    parts: _list[GoogleCloudDialogflowCxV3IntentTrainingPhrasePart]
    repeatCount: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentTrainingPhrasePart(typing.TypedDict, total=False):
    parameterId: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3KnowledgeConnectorSettings(
    typing.TypedDict, total=False
):
    dataStoreConnections: _list[GoogleCloudDialogflowCxV3DataStoreConnection]
    enabled: bool
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3LanguageInfo(typing.TypedDict, total=False):
    confidenceScore: float
    inputLanguageCode: str
    resolvedLanguageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Page(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    description: str
    displayName: str
    entryFulfillment: GoogleCloudDialogflowCxV3Fulfillment
    eventHandlers: _list[GoogleCloudDialogflowCxV3EventHandler]
    form: GoogleCloudDialogflowCxV3Form
    knowledgeConnectorSettings: GoogleCloudDialogflowCxV3KnowledgeConnectorSettings
    name: str
    transitionRouteGroups: _list[str]
    transitionRoutes: _list[GoogleCloudDialogflowCxV3TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3PageInfo(typing.TypedDict, total=False):
    currentPage: str
    displayName: str
    formInfo: GoogleCloudDialogflowCxV3PageInfoFormInfo

@typing.type_check_only
class GoogleCloudDialogflowCxV3PageInfoFormInfo(typing.TypedDict, total=False):
    parameterInfo: _list[GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfo]

@typing.type_check_only
class GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfo(
    typing.TypedDict, total=False
):
    displayName: str
    justCollected: bool
    required: bool
    state: typing.Literal["PARAMETER_STATE_UNSPECIFIED", "EMPTY", "INVALID", "FILLED"]
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3QueryInput(typing.TypedDict, total=False):
    audio: GoogleCloudDialogflowCxV3AudioInput
    dtmf: GoogleCloudDialogflowCxV3DtmfInput
    event: GoogleCloudDialogflowCxV3EventInput
    intent: GoogleCloudDialogflowCxV3IntentInput
    languageCode: str
    text: GoogleCloudDialogflowCxV3TextInput
    toolCallResult: GoogleCloudDialogflowCxV3ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessage(typing.TypedDict, total=False):
    channel: str
    conversationSuccess: GoogleCloudDialogflowCxV3ResponseMessageConversationSuccess
    endInteraction: GoogleCloudDialogflowCxV3ResponseMessageEndInteraction
    knowledgeInfoCard: GoogleCloudDialogflowCxV3ResponseMessageKnowledgeInfoCard
    liveAgentHandoff: GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoff
    mixedAudio: GoogleCloudDialogflowCxV3ResponseMessageMixedAudio
    outputAudioText: GoogleCloudDialogflowCxV3ResponseMessageOutputAudioText
    payload: dict[str, typing.Any]
    playAudio: GoogleCloudDialogflowCxV3ResponseMessagePlayAudio
    responseType: typing.Literal[
        "RESPONSE_TYPE_UNSPECIFIED",
        "ENTRY_PROMPT",
        "PARAMETER_PROMPT",
        "HANDLER_PROMPT",
    ]
    telephonyTransferCall: GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCall
    text: GoogleCloudDialogflowCxV3ResponseMessageText
    toolCall: GoogleCloudDialogflowCxV3ToolCall

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageConversationSuccess(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageEndInteraction(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageKnowledgeInfoCard(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoff(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageMixedAudio(typing.TypedDict, total=False):
    segments: _list[GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegment]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegment(
    typing.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audio: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageOutputAudioText(
    typing.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    ssml: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessagePlayAudio(typing.TypedDict, total=False):
    allowPlaybackInterruption: bool
    audioUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCall(
    typing.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageText(typing.TypedDict, total=False):
    allowPlaybackInterruption: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestMetadata(typing.TypedDict, total=False):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestResponse(typing.TypedDict, total=False):
    continuousTestResult: GoogleCloudDialogflowCxV3ContinuousTestResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseResponse(typing.TypedDict, total=False):
    result: GoogleCloudDialogflowCxV3TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3SessionInfo(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCase(typing.TypedDict, total=False):
    creationTime: str
    displayName: str
    lastTestResult: GoogleCloudDialogflowCxV3TestCaseResult
    name: str
    notes: str
    tags: _list[str]
    testCaseConversationTurns: _list[GoogleCloudDialogflowCxV3ConversationTurn]
    testConfig: GoogleCloudDialogflowCxV3TestConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCaseError(typing.TypedDict, total=False):
    status: GoogleRpcStatus
    testCase: GoogleCloudDialogflowCxV3TestCase

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCaseResult(typing.TypedDict, total=False):
    conversationTurns: _list[GoogleCloudDialogflowCxV3ConversationTurn]
    environment: str
    name: str
    testResult: typing.Literal["TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestConfig(typing.TypedDict, total=False):
    flow: str
    page: str
    trackingParameters: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestError(typing.TypedDict, total=False):
    status: GoogleRpcStatus
    testCase: str
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestRunDifference(typing.TypedDict, total=False):
    description: str
    type: typing.Literal[
        "DIFF_TYPE_UNSPECIFIED", "INTENT", "PAGE", "PARAMETERS", "UTTERANCE", "FLOW"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TextInput(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolCall(typing.TypedDict, total=False):
    action: str
    inputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolCallResult(typing.TypedDict, total=False):
    action: str
    error: GoogleCloudDialogflowCxV3ToolCallResultError
    outputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolCallResultError(typing.TypedDict, total=False):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRoute(typing.TypedDict, total=False):
    condition: str
    description: str
    intent: str
    name: str
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3TurnSignals(typing.TypedDict, total=False):
    agentEscalated: bool
    dtmfUsed: bool
    failureReasons: _list[
        typing.Literal["FAILURE_REASON_UNSPECIFIED", "FAILED_INTENT", "FAILED_WEBHOOK"]
    ]
    noMatch: bool
    noUserInput: bool
    reachedEndPage: bool
    sentimentMagnitude: float
    sentimentScore: float
    userEscalated: bool
    webhookStatuses: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3Webhook(typing.TypedDict, total=False):
    disabled: bool
    displayName: str
    genericWebService: GoogleCloudDialogflowCxV3WebhookGenericWebService
    name: str
    serviceDirectory: GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfig
    timeout: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookGenericWebService(typing.TypedDict, total=False):
    allowedCaCerts: _list[str]
    httpMethod: typing.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "POST",
        "GET",
        "HEAD",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS",
    ]
    oauthConfig: GoogleCloudDialogflowCxV3WebhookGenericWebServiceOAuthConfig
    parameterMapping: dict[str, typing.Any]
    password: str
    requestBody: str
    requestHeaders: dict[str, typing.Any]
    secretVersionForUsernamePassword: str
    secretVersionsForRequestHeaders: dict[str, typing.Any]
    serviceAccountAuthConfig: (
        GoogleCloudDialogflowCxV3WebhookGenericWebServiceServiceAccountAuthConfig
    )
    serviceAgentAuth: typing.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "NONE", "ID_TOKEN", "ACCESS_TOKEN"
    ]
    uri: str
    username: str
    webhookType: typing.Literal["WEBHOOK_TYPE_UNSPECIFIED", "STANDARD", "FLEXIBLE"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookGenericWebServiceOAuthConfig(
    typing.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    scopes: _list[str]
    secretVersionForClientSecret: str
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookGenericWebServiceSecretVersionHeaderValue(
    typing.TypedDict, total=False
):
    secretVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookGenericWebServiceServiceAccountAuthConfig(
    typing.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequest(typing.TypedDict, total=False):
    detectIntentResponseId: str
    dtmfDigits: str
    fulfillmentInfo: GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfo
    intentInfo: GoogleCloudDialogflowCxV3WebhookRequestIntentInfo
    languageCode: str
    languageInfo: GoogleCloudDialogflowCxV3LanguageInfo
    messages: _list[GoogleCloudDialogflowCxV3ResponseMessage]
    pageInfo: GoogleCloudDialogflowCxV3PageInfo
    payload: dict[str, typing.Any]
    sentimentAnalysisResult: (
        GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResult
    )
    sessionInfo: GoogleCloudDialogflowCxV3SessionInfo
    text: str
    transcript: str
    triggerEvent: str
    triggerIntent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequestFulfillmentInfo(
    typing.TypedDict, total=False
):
    tag: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequestIntentInfo(typing.TypedDict, total=False):
    confidence: float
    displayName: str
    lastMatchedIntent: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValue(
    typing.TypedDict, total=False
):
    originalValue: str
    resolvedValue: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResult(
    typing.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookResponse(typing.TypedDict, total=False):
    fulfillmentResponse: GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponse
    pageInfo: GoogleCloudDialogflowCxV3PageInfo
    payload: dict[str, typing.Any]
    sessionInfo: GoogleCloudDialogflowCxV3SessionInfo
    targetFlow: str
    targetPage: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponse(
    typing.TypedDict, total=False
):
    mergeBehavior: typing.Literal["MERGE_BEHAVIOR_UNSPECIFIED", "APPEND", "REPLACE"]
    messages: _list[GoogleCloudDialogflowCxV3ResponseMessage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfig(
    typing.TypedDict, total=False
):
    genericWebService: GoogleCloudDialogflowCxV3WebhookGenericWebService
    service: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettings(typing.TypedDict, total=False):
    audioExportGcsDestination: GoogleCloudDialogflowCxV3beta1GcsDestination
    dtmfSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsDtmfSettings
    loggingSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsLoggingSettings
    speechSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsSpeechSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettingsDtmfSettings(
    typing.TypedDict, total=False
):
    enabled: bool
    endpointingTimeoutDuration: str
    finishDigit: str
    interdigitTimeoutDuration: str
    maxDigits: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettingsLoggingSettings(
    typing.TypedDict, total=False
):
    enableConsentBasedRedaction: bool
    enableInteractionLogging: bool
    enableStackdriverLogging: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettingsSpeechSettings(
    typing.TypedDict, total=False
):
    endpointerSensitivity: int
    models: dict[str, typing.Any]
    noSpeechTimeout: str
    useTimeoutBasedEndpointing: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AudioInput(typing.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowCxV3beta1InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BargeInConfig(typing.TypedDict, total=False):
    noBargeInDuration: str
    totalDuration: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadata(
    typing.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleCloudDialogflowCxV3beta1TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ContinuousTestResult(typing.TypedDict, total=False):
    name: str
    result: typing.Literal["AGGREGATED_TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    runTime: str
    testCaseResults: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationSignals(typing.TypedDict, total=False):
    turnSignals: GoogleCloudDialogflowCxV3beta1TurnSignals

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationTurn(typing.TypedDict, total=False):
    userInput: GoogleCloudDialogflowCxV3beta1ConversationTurnUserInput
    virtualAgentOutput: GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutput

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationTurnUserInput(
    typing.TypedDict, total=False
):
    enableSentimentAnalysis: bool
    injectedParameters: dict[str, typing.Any]
    input: GoogleCloudDialogflowCxV3beta1QueryInput
    isWebhookEnabled: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutput(
    typing.TypedDict, total=False
):
    currentPage: GoogleCloudDialogflowCxV3beta1Page
    diagnosticInfo: dict[str, typing.Any]
    differences: _list[GoogleCloudDialogflowCxV3beta1TestRunDifference]
    sessionParameters: dict[str, typing.Any]
    status: GoogleRpcStatus
    textResponses: _list[GoogleCloudDialogflowCxV3beta1ResponseMessageText]
    triggeredIntent: GoogleCloudDialogflowCxV3beta1Intent

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadata(
    typing.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnection(typing.TypedDict, total=False):
    dataStore: str
    dataStoreType: typing.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED", "PUBLIC_WEB", "UNSTRUCTURED", "STRUCTURED"
    ]
    documentProcessingMode: typing.Literal[
        "DOCUMENT_PROCESSING_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowMetadata(typing.TypedDict, total=False):
    testErrors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowResponse(typing.TypedDict, total=False):
    deployment: str
    environment: GoogleCloudDialogflowCxV3beta1Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DtmfInput(typing.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Environment(typing.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    testCasesConfig: GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfig
    updateTime: str
    versionConfigs: _list[GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfig]
    webhookConfig: GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfig(
    typing.TypedDict, total=False
):
    enableContinuousRun: bool
    enablePredeploymentRun: bool
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfig(
    typing.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfig(
    typing.TypedDict, total=False
):
    webhookOverrides: _list[GoogleCloudDialogflowCxV3beta1Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EventHandler(typing.TypedDict, total=False):
    event: str
    name: str
    targetFlow: str
    targetPage: str
    targetPlaybook: str
    triggerFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EventInput(typing.TypedDict, total=False):
    event: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportAgentResponse(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str
    commitSha: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesResponse(
    typing.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportFlowResponse(typing.TypedDict, total=False):
    flowContent: str
    flowUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsResponse(
    typing.TypedDict, total=False
):
    intentsContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesResponse(
    typing.TypedDict, total=False
):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Form(typing.TypedDict, total=False):
    parameters: _list[GoogleCloudDialogflowCxV3beta1FormParameter]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FormParameter(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    defaultValue: typing.Any
    displayName: str
    entityType: str
    fillBehavior: GoogleCloudDialogflowCxV3beta1FormParameterFillBehavior
    isList: bool
    redact: bool
    required: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FormParameterFillBehavior(
    typing.TypedDict, total=False
):
    initialPromptFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment
    repromptEventHandlers: _list[GoogleCloudDialogflowCxV3beta1EventHandler]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Fulfillment(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    codeBlockFunction: str
    conditionalCases: _list[GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCases]
    enableGenerativeFallback: bool
    generators: _list[GoogleCloudDialogflowCxV3beta1FulfillmentGeneratorSettings]
    messages: _list[GoogleCloudDialogflowCxV3beta1ResponseMessage]
    returnPartialResponses: bool
    setParameterActions: _list[
        GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterAction
    ]
    tag: str
    webhook: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCases(
    typing.TypedDict, total=False
):
    cases: _list[GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCase(
    typing.TypedDict, total=False
):
    caseContent: _list[
        GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContent
    ]
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContent(
    typing.TypedDict, total=False
):
    additionalCases: GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCases
    message: GoogleCloudDialogflowCxV3beta1ResponseMessage

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentGeneratorSettings(
    typing.TypedDict, total=False
):
    generator: str
    inputParameters: dict[str, typing.Any]
    outputParameter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterAction(
    typing.TypedDict, total=False
):
    parameter: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GcsDestination(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesResponse(
    typing.TypedDict, total=False
):
    conflictingResources: (
        GoogleCloudDialogflowCxV3beta1ImportEntityTypesResponseConflictingResources
    )
    entityTypes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesResponseConflictingResources(
    typing.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    entityTypeDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportFlowResponse(typing.TypedDict, total=False):
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsResponse(
    typing.TypedDict, total=False
):
    conflictingResources: (
        GoogleCloudDialogflowCxV3beta1ImportIntentsResponseConflictingResources
    )
    intents: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsResponseConflictingResources(
    typing.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    intentDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadata(
    typing.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestCaseError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesResponse(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InlineDestination(typing.TypedDict, total=False):
    content: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InputAudioConfig(typing.TypedDict, total=False):
    audioEncoding: typing.Literal[
        "AUDIO_ENCODING_UNSPECIFIED",
        "AUDIO_ENCODING_LINEAR_16",
        "AUDIO_ENCODING_FLAC",
        "AUDIO_ENCODING_MULAW",
        "AUDIO_ENCODING_AMR",
        "AUDIO_ENCODING_AMR_WB",
        "AUDIO_ENCODING_OGG_OPUS",
        "AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE",
        "AUDIO_ENCODING_ALAW",
    ]
    bargeInConfig: GoogleCloudDialogflowCxV3beta1BargeInConfig
    enableWordInfo: bool
    model: str
    modelVariant: typing.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]
    optOutConformerModelMigration: bool
    phraseHints: _list[str]
    sampleRateHertz: int
    singleUtterance: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Intent(typing.TypedDict, total=False):
    description: str
    displayName: str
    dtmfPattern: str
    isFallback: bool
    labels: dict[str, typing.Any]
    name: str
    parameters: _list[GoogleCloudDialogflowCxV3beta1IntentParameter]
    priority: int
    trainingPhrases: _list[GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentInput(typing.TypedDict, total=False):
    intent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentParameter(typing.TypedDict, total=False):
    entityType: str
    id: str
    isList: bool
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase(typing.TypedDict, total=False):
    id: str
    parts: _list[GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePart]
    repeatCount: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePart(
    typing.TypedDict, total=False
):
    parameterId: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettings(
    typing.TypedDict, total=False
):
    dataStoreConnections: _list[GoogleCloudDialogflowCxV3beta1DataStoreConnection]
    enabled: bool
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LanguageInfo(typing.TypedDict, total=False):
    confidenceScore: float
    inputLanguageCode: str
    resolvedLanguageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Page(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    description: str
    displayName: str
    entryFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment
    eventHandlers: _list[GoogleCloudDialogflowCxV3beta1EventHandler]
    form: GoogleCloudDialogflowCxV3beta1Form
    knowledgeConnectorSettings: GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettings
    name: str
    transitionRouteGroups: _list[str]
    transitionRoutes: _list[GoogleCloudDialogflowCxV3beta1TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PageInfo(typing.TypedDict, total=False):
    currentPage: str
    displayName: str
    formInfo: GoogleCloudDialogflowCxV3beta1PageInfoFormInfo

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PageInfoFormInfo(typing.TypedDict, total=False):
    parameterInfo: _list[GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo(
    typing.TypedDict, total=False
):
    displayName: str
    justCollected: bool
    required: bool
    state: typing.Literal["PARAMETER_STATE_UNSPECIFIED", "EMPTY", "INVALID", "FILLED"]
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1QueryInput(typing.TypedDict, total=False):
    audio: GoogleCloudDialogflowCxV3beta1AudioInput
    dtmf: GoogleCloudDialogflowCxV3beta1DtmfInput
    event: GoogleCloudDialogflowCxV3beta1EventInput
    intent: GoogleCloudDialogflowCxV3beta1IntentInput
    languageCode: str
    text: GoogleCloudDialogflowCxV3beta1TextInput
    toolCallResult: GoogleCloudDialogflowCxV3beta1ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessage(typing.TypedDict, total=False):
    channel: str
    conversationSuccess: (
        GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess
    )
    endInteraction: GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction
    knowledgeInfoCard: GoogleCloudDialogflowCxV3beta1ResponseMessageKnowledgeInfoCard
    liveAgentHandoff: GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff
    mixedAudio: GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio
    outputAudioText: GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText
    payload: dict[str, typing.Any]
    playAudio: GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio
    telephonyTransferCall: (
        GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCall
    )
    text: GoogleCloudDialogflowCxV3beta1ResponseMessageText
    toolCall: GoogleCloudDialogflowCxV3beta1ToolCall

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageKnowledgeInfoCard(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio(
    typing.TypedDict, total=False
):
    segments: _list[GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment(
    typing.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audio: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText(
    typing.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    ssml: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio(
    typing.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audioUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCall(
    typing.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageText(typing.TypedDict, total=False):
    allowPlaybackInterruption: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadata(
    typing.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestResponse(
    typing.TypedDict, total=False
):
    continuousTestResult: GoogleCloudDialogflowCxV3beta1ContinuousTestResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunTestCaseMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunTestCaseResponse(typing.TypedDict, total=False):
    result: GoogleCloudDialogflowCxV3beta1TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionInfo(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCase(typing.TypedDict, total=False):
    creationTime: str
    displayName: str
    lastTestResult: GoogleCloudDialogflowCxV3beta1TestCaseResult
    name: str
    notes: str
    tags: _list[str]
    testCaseConversationTurns: _list[GoogleCloudDialogflowCxV3beta1ConversationTurn]
    testConfig: GoogleCloudDialogflowCxV3beta1TestConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCaseError(typing.TypedDict, total=False):
    status: GoogleRpcStatus
    testCase: GoogleCloudDialogflowCxV3beta1TestCase

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCaseResult(typing.TypedDict, total=False):
    conversationTurns: _list[GoogleCloudDialogflowCxV3beta1ConversationTurn]
    environment: str
    name: str
    testResult: typing.Literal["TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestConfig(typing.TypedDict, total=False):
    flow: str
    page: str
    trackingParameters: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestError(typing.TypedDict, total=False):
    status: GoogleRpcStatus
    testCase: str
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestRunDifference(typing.TypedDict, total=False):
    description: str
    type: typing.Literal[
        "DIFF_TYPE_UNSPECIFIED", "INTENT", "PAGE", "PARAMETERS", "UTTERANCE", "FLOW"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TextInput(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolCall(typing.TypedDict, total=False):
    action: str
    inputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolCallResult(typing.TypedDict, total=False):
    action: str
    error: GoogleCloudDialogflowCxV3beta1ToolCallResultError
    outputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolCallResultError(typing.TypedDict, total=False):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRoute(typing.TypedDict, total=False):
    condition: str
    description: str
    intent: str
    name: str
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TurnSignals(typing.TypedDict, total=False):
    agentEscalated: bool
    dtmfUsed: bool
    failureReasons: _list[
        typing.Literal["FAILURE_REASON_UNSPECIFIED", "FAILED_INTENT", "FAILED_WEBHOOK"]
    ]
    noMatch: bool
    noUserInput: bool
    reachedEndPage: bool
    sentimentMagnitude: float
    sentimentScore: float
    userEscalated: bool
    webhookStatuses: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Webhook(typing.TypedDict, total=False):
    disabled: bool
    displayName: str
    genericWebService: GoogleCloudDialogflowCxV3beta1WebhookGenericWebService
    name: str
    serviceDirectory: GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfig
    timeout: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookGenericWebService(
    typing.TypedDict, total=False
):
    allowedCaCerts: _list[str]
    httpMethod: typing.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "POST",
        "GET",
        "HEAD",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS",
    ]
    oauthConfig: GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOAuthConfig
    parameterMapping: dict[str, typing.Any]
    password: str
    requestBody: str
    requestHeaders: dict[str, typing.Any]
    secretVersionForUsernamePassword: str
    secretVersionsForRequestHeaders: dict[str, typing.Any]
    serviceAccountAuthConfig: (
        GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceServiceAccountAuthConfig
    )
    serviceAgentAuth: typing.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "NONE", "ID_TOKEN", "ACCESS_TOKEN"
    ]
    uri: str
    username: str
    webhookType: typing.Literal["WEBHOOK_TYPE_UNSPECIFIED", "STANDARD", "FLEXIBLE"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOAuthConfig(
    typing.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    scopes: _list[str]
    secretVersionForClientSecret: str
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceSecretVersionHeaderValue(
    typing.TypedDict, total=False
):
    secretVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceServiceAccountAuthConfig(
    typing.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequest(typing.TypedDict, total=False):
    detectIntentResponseId: str
    dtmfDigits: str
    fulfillmentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo
    intentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo
    languageCode: str
    languageInfo: GoogleCloudDialogflowCxV3beta1LanguageInfo
    messages: _list[GoogleCloudDialogflowCxV3beta1ResponseMessage]
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo
    payload: dict[str, typing.Any]
    sentimentAnalysisResult: (
        GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResult
    )
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    text: str
    transcript: str
    triggerEvent: str
    triggerIntent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo(
    typing.TypedDict, total=False
):
    tag: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo(
    typing.TypedDict, total=False
):
    confidence: float
    displayName: str
    lastMatchedIntent: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValue(
    typing.TypedDict, total=False
):
    originalValue: str
    resolvedValue: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResult(
    typing.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookResponse(typing.TypedDict, total=False):
    fulfillmentResponse: (
        GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse
    )
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo
    payload: dict[str, typing.Any]
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    targetFlow: str
    targetPage: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse(
    typing.TypedDict, total=False
):
    mergeBehavior: typing.Literal["MERGE_BEHAVIOR_UNSPECIFIED", "APPEND", "REPLACE"]
    messages: _list[GoogleCloudDialogflowCxV3beta1ResponseMessage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfig(
    typing.TypedDict, total=False
):
    genericWebService: GoogleCloudDialogflowCxV3beta1WebhookGenericWebService
    service: str

@typing.type_check_only
class GoogleCloudDialogflowV2Agent(typing.TypedDict, total=False):
    apiVersion: typing.Literal[
        "API_VERSION_UNSPECIFIED",
        "API_VERSION_V1",
        "API_VERSION_V2",
        "API_VERSION_V2_BETA_1",
    ]
    avatarUri: str
    classificationThreshold: float
    defaultLanguageCode: str
    description: str
    displayName: str
    enableLogging: bool
    matchMode: typing.Literal[
        "MATCH_MODE_UNSPECIFIED", "MATCH_MODE_HYBRID", "MATCH_MODE_ML_ONLY"
    ]
    parent: str
    supportedLanguageCodes: _list[str]
    tier: typing.Literal[
        "TIER_UNSPECIFIED", "TIER_STANDARD", "TIER_ENTERPRISE", "TIER_ENTERPRISE_PLUS"
    ]
    timeZone: str

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantFeedback(typing.TypedDict, total=False):
    answerRelevance: typing.Literal[
        "ANSWER_RELEVANCE_UNSPECIFIED", "IRRELEVANT", "RELEVANT"
    ]
    documentCorrectness: typing.Literal[
        "DOCUMENT_CORRECTNESS_UNSPECIFIED", "INCORRECT", "CORRECT"
    ]
    documentEfficiency: typing.Literal[
        "DOCUMENT_EFFICIENCY_UNSPECIFIED", "INEFFICIENT", "EFFICIENT"
    ]
    knowledgeAssistFeedback: (
        GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeAssistFeedback
    )
    knowledgeSearchFeedback: (
        GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback
    )
    summarizationFeedback: (
        GoogleCloudDialogflowV2AgentAssistantFeedbackSummarizationFeedback
    )

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeAssistFeedback(
    typing.TypedDict, total=False
):
    answerCopied: bool
    clickedUris: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback(
    typing.TypedDict, total=False
):
    answerCopied: bool
    clickedUris: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantFeedbackSummarizationFeedback(
    typing.TypedDict, total=False
):
    startTime: str
    submitTime: str
    summaryText: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantRecord(typing.TypedDict, total=False):
    articleSuggestionAnswer: GoogleCloudDialogflowV2ArticleAnswer
    dialogflowAssistAnswer: GoogleCloudDialogflowV2DialogflowAssistAnswer
    faqAnswer: GoogleCloudDialogflowV2FaqAnswer
    generatorSuggestion: GoogleCloudDialogflowV2GeneratorSuggestion

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingContext(typing.TypedDict, total=False):
    instructions: _list[GoogleCloudDialogflowV2AgentCoachingInstruction]
    outputLanguageCode: str
    overarchingGuidance: str
    version: str

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingInstruction(typing.TypedDict, total=False):
    agentAction: str
    condition: str
    displayDetails: str
    displayName: str
    duplicateCheckResult: (
        GoogleCloudDialogflowV2AgentCoachingInstructionDuplicateCheckResult
    )
    systemAction: str
    triggeringEvent: typing.Literal[
        "TRIGGER_EVENT_UNSPECIFIED",
        "END_OF_UTTERANCE",
        "MANUAL_CALL",
        "CUSTOMER_MESSAGE",
        "AGENT_MESSAGE",
        "TOOL_CALL_COMPLETION",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingInstructionDuplicateCheckResult(
    typing.TypedDict, total=False
):
    duplicateSuggestions: _list[
        GoogleCloudDialogflowV2AgentCoachingInstructionDuplicateCheckResultDuplicateSuggestion
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingInstructionDuplicateCheckResultDuplicateSuggestion(
    typing.TypedDict, total=False
):
    answerRecord: str
    similarityScore: float
    suggestionIndex: int

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingSuggestion(typing.TypedDict, total=False):
    agentActionSuggestions: _list[
        GoogleCloudDialogflowV2AgentCoachingSuggestionAgentActionSuggestion
    ]
    applicableInstructions: _list[GoogleCloudDialogflowV2AgentCoachingInstruction]
    sampleResponses: _list[GoogleCloudDialogflowV2AgentCoachingSuggestionSampleResponse]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingSuggestionAgentActionSuggestion(
    typing.TypedDict, total=False
):
    agentAction: str
    duplicateCheckResult: (
        GoogleCloudDialogflowV2AgentCoachingSuggestionDuplicateCheckResult
    )
    sources: GoogleCloudDialogflowV2AgentCoachingSuggestionSources

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingSuggestionDuplicateCheckResult(
    typing.TypedDict, total=False
):
    duplicateSuggestions: _list[
        GoogleCloudDialogflowV2AgentCoachingSuggestionDuplicateCheckResultDuplicateSuggestion
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingSuggestionDuplicateCheckResultDuplicateSuggestion(
    typing.TypedDict, total=False
):
    answerRecord: str
    similarityScore: float
    sources: GoogleCloudDialogflowV2AgentCoachingSuggestionSources
    suggestionIndex: int

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingSuggestionSampleResponse(
    typing.TypedDict, total=False
):
    duplicateCheckResult: (
        GoogleCloudDialogflowV2AgentCoachingSuggestionDuplicateCheckResult
    )
    responseText: str
    sources: GoogleCloudDialogflowV2AgentCoachingSuggestionSources

@typing.type_check_only
class GoogleCloudDialogflowV2AgentCoachingSuggestionSources(
    typing.TypedDict, total=False
):
    instructionIndexes: _list[int]

@typing.type_check_only
class GoogleCloudDialogflowV2AnalyzeContentRequest(typing.TypedDict, total=False):
    assistQueryParams: GoogleCloudDialogflowV2AssistQueryParameters
    audioInput: GoogleCloudDialogflowV2AudioInput
    cxParameters: dict[str, typing.Any]
    eventInput: GoogleCloudDialogflowV2EventInput
    queryParams: GoogleCloudDialogflowV2QueryParameters
    replyAudioConfig: GoogleCloudDialogflowV2OutputAudioConfig
    requestId: str
    suggestionInput: GoogleCloudDialogflowV2SuggestionInput
    textInput: GoogleCloudDialogflowV2TextInput

@typing.type_check_only
class GoogleCloudDialogflowV2AnalyzeContentResponse(typing.TypedDict, total=False):
    automatedAgentReply: GoogleCloudDialogflowV2AutomatedAgentReply
    dtmfParameters: GoogleCloudDialogflowV2DtmfParameters
    endUserSuggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]
    humanAgentSuggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]
    message: GoogleCloudDialogflowV2Message
    replyAudio: GoogleCloudDialogflowV2OutputAudio
    replyText: str

@typing.type_check_only
class GoogleCloudDialogflowV2AnnotatedMessagePart(typing.TypedDict, total=False):
    entityType: str
    formattedValue: typing.Any
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2AnswerFeedback(typing.TypedDict, total=False):
    agentAssistantDetailFeedback: GoogleCloudDialogflowV2AgentAssistantFeedback
    clickTime: str
    clicked: bool
    correctnessLevel: typing.Literal[
        "CORRECTNESS_LEVEL_UNSPECIFIED",
        "NOT_CORRECT",
        "PARTIALLY_CORRECT",
        "FULLY_CORRECT",
    ]
    displayTime: str
    displayed: bool

@typing.type_check_only
class GoogleCloudDialogflowV2AnswerRecord(typing.TypedDict, total=False):
    agentAssistantRecord: GoogleCloudDialogflowV2AgentAssistantRecord
    answerFeedback: GoogleCloudDialogflowV2AnswerFeedback
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2ArticleAnswer(typing.TypedDict, total=False):
    answerRecord: str
    confidence: float
    metadata: dict[str, typing.Any]
    snippets: _list[str]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ArticleSuggestionModelMetadata(
    typing.TypedDict, total=False
):
    trainingModelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "SMART_REPLY_DUAL_ENCODER_MODEL",
        "SMART_REPLY_BERT_MODEL",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2AssistQueryParameters(typing.TypedDict, total=False):
    documentsMetadataFilters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2AudioInput(typing.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowV2InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowV2AutomatedAgentConfig(typing.TypedDict, total=False):
    agent: str
    sessionTtl: str

@typing.type_check_only
class GoogleCloudDialogflowV2AutomatedAgentReply(typing.TypedDict, total=False):
    allowCancellation: bool
    automatedAgentReplyType: typing.Literal[
        "AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED", "PARTIAL", "FINAL"
    ]
    cxCurrentPage: str
    detectIntentResponse: GoogleCloudDialogflowV2DetectIntentResponse

@typing.type_check_only
class GoogleCloudDialogflowV2BatchCreateEntitiesRequest(typing.TypedDict, total=False):
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchDeleteEntitiesRequest(typing.TypedDict, total=False):
    entityValues: _list[str]
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchDeleteEntityTypesRequest(
    typing.TypedDict, total=False
):
    entityTypeNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2BatchDeleteIntentsRequest(typing.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowV2Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateEntitiesRequest(typing.TypedDict, total=False):
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    languageCode: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest(
    typing.TypedDict, total=False
):
    entityTypeBatchInline: GoogleCloudDialogflowV2EntityTypeBatch
    entityTypeBatchUri: str
    languageCode: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateEntityTypesResponse(
    typing.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateIntentsRequest(typing.TypedDict, total=False):
    intentBatchInline: GoogleCloudDialogflowV2IntentBatch
    intentBatchUri: str
    intentView: typing.Literal["INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"]
    languageCode: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateIntentsResponse(typing.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowV2Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2CesAppSpec(typing.TypedDict, total=False):
    cesApp: str
    confirmationRequirement: typing.Literal[
        "CONFIRMATION_REQUIREMENT_UNSPECIFIED", "REQUIRED", "NOT_REQUIRED"
    ]
    proactiveEnabled: bool
    reactiveEnabled: bool

@typing.type_check_only
class GoogleCloudDialogflowV2CesToolSpec(typing.TypedDict, total=False):
    cesTool: str
    confirmationRequirement: typing.Literal[
        "CONFIRMATION_REQUIREMENT_UNSPECIFIED", "REQUIRED", "NOT_REQUIRED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadata(
    typing.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ARTICLE_SUGGESTION",
        "FAQ",
        "SMART_REPLY",
        "CONVERSATION_SUMMARIZATION",
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ClearSuggestionFeatureConfigRequest(
    typing.TypedDict, total=False
):
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ARTICLE_SUGGESTION",
        "FAQ",
        "SMART_REPLY",
        "CONVERSATION_SUMMARIZATION",
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2CompleteConversationRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2Connection(typing.TypedDict, total=False):
    connectionId: str
    errorDetails: GoogleCloudDialogflowV2ConnectionErrorDetails
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CONNECTED",
        "DISCONNECTED",
        "AUTHENTICATION_FAILED",
        "KEEPALIVE",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConnectionErrorDetails(typing.TypedDict, total=False):
    certificateState: typing.Literal[
        "CERTIFICATE_STATE_UNSPECIFIED",
        "CERTIFICATE_VALID",
        "CERTIFICATE_INVALID",
        "CERTIFICATE_EXPIRED",
        "CERTIFICATE_HOSTNAME_NOT_FOUND",
        "CERTIFICATE_UNAUTHENTICATED",
        "CERTIFICATE_TRUST_STORE_NOT_FOUND",
        "CERTIFICATE_HOSTNAME_INVALID_FORMAT",
        "CERTIFICATE_QUOTA_EXCEEDED",
    ]
    errorMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2Context(typing.TypedDict, total=False):
    lifespanCount: int
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2Conversation(typing.TypedDict, total=False):
    conversationProfile: str
    conversationStage: typing.Literal[
        "CONVERSATION_STAGE_UNSPECIFIED", "VIRTUAL_AGENT_STAGE", "HUMAN_ASSIST_STAGE"
    ]
    endTime: str
    ingestedContextReferences: dict[str, typing.Any]
    initialConversationProfile: GoogleCloudDialogflowV2ConversationProfile
    initialGeneratorContexts: dict[str, typing.Any]
    lifecycleState: typing.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETED"
    ]
    name: str
    phoneNumber: GoogleCloudDialogflowV2ConversationPhoneNumber
    startTime: str
    telephonyConnectionInfo: GoogleCloudDialogflowV2ConversationTelephonyConnectionInfo

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationContext(typing.TypedDict, total=False):
    messageEntries: _list[GoogleCloudDialogflowV2MessageEntry]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationContextReference(
    typing.TypedDict, total=False
):
    contextContents: _list[
        GoogleCloudDialogflowV2ConversationContextReferenceContextContent
    ]
    createTime: str
    languageCode: str
    updateMode: typing.Literal["UPDATE_MODE_UNSPECIFIED", "APPEND", "OVERWRITE"]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationContextReferenceContextContent(
    typing.TypedDict, total=False
):
    answerRecord: str
    content: str
    contentFormat: typing.Literal["CONTENT_FORMAT_UNSPECIFIED", "JSON", "PLAIN_TEXT"]
    ingestionTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationDataset(typing.TypedDict, total=False):
    conversationCount: str
    conversationInfo: GoogleCloudDialogflowV2ConversationInfo
    createTime: str
    description: str
    displayName: str
    inputConfig: GoogleCloudDialogflowV2InputConfig
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationEvent(typing.TypedDict, total=False):
    conversation: str
    errorStatus: GoogleRpcStatus
    newMessagePayload: GoogleCloudDialogflowV2Message
    newRecognitionResultPayload: GoogleCloudDialogflowV2StreamingRecognitionResult
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "CONVERSATION_STARTED",
        "CONVERSATION_FINISHED",
        "HUMAN_INTERVENTION_NEEDED",
        "NEW_MESSAGE",
        "NEW_RECOGNITION_RESULT",
        "UNRECOVERABLE_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationGeneratorContext(
    typing.TypedDict, total=False
):
    generatorType: typing.Literal[
        "GENERATOR_TYPE_UNSPECIFIED",
        "FREE_FORM",
        "AGENT_COACHING",
        "SUMMARIZATION",
        "TRANSLATION",
        "AGENT_FEEDBACK",
        "CUSTOMER_MESSAGE_GENERATION",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationInfo(typing.TypedDict, total=False):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationModel(typing.TypedDict, total=False):
    articleSuggestionModelMetadata: (
        GoogleCloudDialogflowV2ArticleSuggestionModelMetadata
    )
    createTime: str
    datasets: _list[GoogleCloudDialogflowV2InputDataset]
    displayName: str
    languageCode: str
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    smartReplyModelMetadata: GoogleCloudDialogflowV2SmartReplyModelMetadata
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UNDEPLOYED",
        "DEPLOYING",
        "DEPLOYED",
        "UNDEPLOYING",
        "DELETING",
        "FAILED",
        "PENDING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationModelEvaluation(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    evaluationConfig: GoogleCloudDialogflowV2EvaluationConfig
    name: str
    rawHumanEvalTemplateCsv: str
    smartReplyMetrics: GoogleCloudDialogflowV2SmartReplyMetrics

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationPhoneNumber(typing.TypedDict, total=False):
    countryCode: int
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationProfile(typing.TypedDict, total=False):
    automatedAgentConfig: GoogleCloudDialogflowV2AutomatedAgentConfig
    createTime: str
    displayName: str
    humanAgentAssistantConfig: GoogleCloudDialogflowV2HumanAgentAssistantConfig
    humanAgentHandoffConfig: GoogleCloudDialogflowV2HumanAgentHandoffConfig
    languageCode: str
    loggingConfig: GoogleCloudDialogflowV2LoggingConfig
    name: str
    newMessageEventNotificationConfig: GoogleCloudDialogflowV2NotificationConfig
    newRecognitionResultNotificationConfig: GoogleCloudDialogflowV2NotificationConfig
    notificationConfig: GoogleCloudDialogflowV2NotificationConfig
    securitySettings: str
    sipConfig: GoogleCloudDialogflowV2SipConfig
    sttConfig: GoogleCloudDialogflowV2SpeechToTextConfig
    timeZone: str
    ttsConfig: GoogleCloudDialogflowV2SynthesizeSpeechConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationTelephonyConnectionInfo(
    typing.TypedDict, total=False
):
    dialedNumber: str
    extraMimeContents: _list[
        GoogleCloudDialogflowV2ConversationTelephonyConnectionInfoMimeContent
    ]
    sdp: str
    sipHeaders: _list[
        GoogleCloudDialogflowV2ConversationTelephonyConnectionInfoSipHeader
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationTelephonyConnectionInfoMimeContent(
    typing.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationTelephonyConnectionInfoSipHeader(
    typing.TypedDict, total=False
):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadata(
    typing.TypedDict, total=False
):
    conversationDataset: str

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadata(
    typing.TypedDict, total=False
):
    conversationModel: str
    conversationModelEvaluation: str
    createTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "RUNNING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationModelEvaluationRequest(
    typing.TypedDict, total=False
):
    conversationModelEvaluation: GoogleCloudDialogflowV2ConversationModelEvaluation

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationModelOperationMetadata(
    typing.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "CANCELLING",
        "TRAINING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2CustomPronunciationParams(typing.TypedDict, total=False):
    phoneticEncoding: typing.Literal[
        "PHONETIC_ENCODING_UNSPECIFIED",
        "PHONETIC_ENCODING_IPA",
        "PHONETIC_ENCODING_X_SAMPA",
    ]
    phrase: str
    pronunciation: str

@typing.type_check_only
class GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2DeleteConversationModelOperationMetadata(
    typing.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2DeployConversationModelOperationMetadata(
    typing.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2DeployConversationModelRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2DetectIntentRequest(typing.TypedDict, total=False):
    inputAudio: str
    outputAudioConfig: GoogleCloudDialogflowV2OutputAudioConfig
    outputAudioConfigMask: str
    queryInput: GoogleCloudDialogflowV2QueryInput
    queryParams: GoogleCloudDialogflowV2QueryParameters

@typing.type_check_only
class GoogleCloudDialogflowV2DetectIntentResponse(typing.TypedDict, total=False):
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowV2OutputAudioConfig
    queryResult: GoogleCloudDialogflowV2QueryResult
    responseId: str
    webhookStatus: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDialogflowV2DialogflowAssistAnswer(typing.TypedDict, total=False):
    answerRecord: str
    intentSuggestion: GoogleCloudDialogflowV2IntentSuggestion
    queryResult: GoogleCloudDialogflowV2QueryResult

@typing.type_check_only
class GoogleCloudDialogflowV2Document(typing.TypedDict, total=False):
    contentUri: str
    displayName: str
    enableAutoReload: bool
    knowledgeTypes: _list[
        typing.Literal[
            "KNOWLEDGE_TYPE_UNSPECIFIED",
            "FAQ",
            "EXTRACTIVE_QA",
            "ARTICLE_SUGGESTION",
            "AGENT_FACING_SMART_REPLY",
        ]
    ]
    latestReloadStatus: GoogleCloudDialogflowV2DocumentReloadStatus
    metadata: dict[str, typing.Any]
    mimeType: str
    name: str
    rawContent: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "RELOADING", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2DocumentReloadStatus(typing.TypedDict, total=False):
    status: GoogleRpcStatus
    time: str

@typing.type_check_only
class GoogleCloudDialogflowV2DtmfParameters(typing.TypedDict, total=False):
    acceptsDtmfInput: bool

@typing.type_check_only
class GoogleCloudDialogflowV2EncryptionSpec(typing.TypedDict, total=False):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2EntityType(typing.TypedDict, total=False):
    autoExpansionMode: typing.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    kind: typing.Literal["KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2EntityTypeBatch(typing.TypedDict, total=False):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2EntityTypeEntity(typing.TypedDict, total=False):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2Environment(typing.TypedDict, total=False):
    agentVersion: str
    description: str
    fulfillment: GoogleCloudDialogflowV2Fulfillment
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "STOPPED", "LOADING", "RUNNING"]
    textToSpeechSettings: GoogleCloudDialogflowV2TextToSpeechSettings
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2EnvironmentHistory(typing.TypedDict, total=False):
    entries: _list[GoogleCloudDialogflowV2EnvironmentHistoryEntry]
    nextPageToken: str
    parent: str

@typing.type_check_only
class GoogleCloudDialogflowV2EnvironmentHistoryEntry(typing.TypedDict, total=False):
    agentVersion: str
    createTime: str
    description: str

@typing.type_check_only
class GoogleCloudDialogflowV2EvaluationConfig(typing.TypedDict, total=False):
    datasets: _list[GoogleCloudDialogflowV2InputDataset]
    smartComposeConfig: GoogleCloudDialogflowV2EvaluationConfigSmartComposeConfig
    smartReplyConfig: GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfig

@typing.type_check_only
class GoogleCloudDialogflowV2EvaluationConfigSmartComposeConfig(
    typing.TypedDict, total=False
):
    allowlistDocument: str
    maxResultCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfig(
    typing.TypedDict, total=False
):
    allowlistDocument: str
    maxResultCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2EvaluationStatus(typing.TypedDict, total=False):
    done: bool
    pipelineStatus: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDialogflowV2EventInput(typing.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2ExportAgentRequest(typing.TypedDict, total=False):
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ExportAgentResponse(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ExportDocumentRequest(typing.TypedDict, total=False):
    exportFullContent: bool
    gcsDestination: GoogleCloudDialogflowV2GcsDestination
    smartMessagingPartialUpdate: bool

@typing.type_check_only
class GoogleCloudDialogflowV2ExportOperationMetadata(typing.TypedDict, total=False):
    exportedGcsDestination: GoogleCloudDialogflowV2GcsDestination

@typing.type_check_only
class GoogleCloudDialogflowV2FaqAnswer(typing.TypedDict, total=False):
    answer: str
    answerRecord: str
    confidence: float
    metadata: dict[str, typing.Any]
    question: str
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2FewShotExample(typing.TypedDict, total=False):
    conversationContext: GoogleCloudDialogflowV2ConversationContext
    extraInfo: dict[str, typing.Any]
    output: GoogleCloudDialogflowV2GeneratorSuggestion
    summarizationSectionList: GoogleCloudDialogflowV2SummarizationSectionList

@typing.type_check_only
class GoogleCloudDialogflowV2FreeFormContext(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2FreeFormSuggestion(typing.TypedDict, total=False):
    response: str

@typing.type_check_only
class GoogleCloudDialogflowV2Fulfillment(typing.TypedDict, total=False):
    displayName: str
    enabled: bool
    features: _list[GoogleCloudDialogflowV2FulfillmentFeature]
    genericWebService: GoogleCloudDialogflowV2FulfillmentGenericWebService
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2FulfillmentFeature(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "SMALLTALK"]

@typing.type_check_only
class GoogleCloudDialogflowV2FulfillmentGenericWebService(
    typing.TypedDict, total=False
):
    isCloudFunction: bool
    password: str
    requestHeaders: dict[str, typing.Any]
    uri: str
    username: str

@typing.type_check_only
class GoogleCloudDialogflowV2GcsDestination(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2GcsSources(typing.TypedDict, total=False):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSuggestionRequest(
    typing.TypedDict, total=False
):
    contextReferences: dict[str, typing.Any]
    conversationContext: GoogleCloudDialogflowV2ConversationContext
    generator: GoogleCloudDialogflowV2Generator
    generatorName: str
    securitySettings: str
    triggerEvents: _list[
        typing.Literal[
            "TRIGGER_EVENT_UNSPECIFIED",
            "END_OF_UTTERANCE",
            "MANUAL_CALL",
            "CUSTOMER_MESSAGE",
            "AGENT_MESSAGE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSuggestionResponse(
    typing.TypedDict, total=False
):
    generatorSuggestion: GoogleCloudDialogflowV2GeneratorSuggestion

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryRequest(
    typing.TypedDict, total=False
):
    conversationProfile: GoogleCloudDialogflowV2ConversationProfile
    latestMessage: str
    maxContextSize: int
    statelessConversation: (
        GoogleCloudDialogflowV2GenerateStatelessSummaryRequestMinimalConversation
    )

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryRequestMinimalConversation(
    typing.TypedDict, total=False
):
    messages: _list[GoogleCloudDialogflowV2Message]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryResponse(
    typing.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    summary: GoogleCloudDialogflowV2GenerateStatelessSummaryResponseSummary

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryResponseSummary(
    typing.TypedDict, total=False
):
    baselineModelVersion: str
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateSuggestionsRequest(typing.TypedDict, total=False):
    latestMessage: str
    triggerEvents: _list[
        typing.Literal[
            "TRIGGER_EVENT_UNSPECIFIED",
            "END_OF_UTTERANCE",
            "MANUAL_CALL",
            "CUSTOMER_MESSAGE",
            "AGENT_MESSAGE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateSuggestionsResponse(typing.TypedDict, total=False):
    generatorSuggestionAnswers: _list[
        GoogleCloudDialogflowV2GenerateSuggestionsResponseGeneratorSuggestionAnswer
    ]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateSuggestionsResponseGeneratorSuggestionAnswer(
    typing.TypedDict, total=False
):
    answerRecord: str
    generatorSuggestion: GoogleCloudDialogflowV2GeneratorSuggestion
    sourceGenerator: str

@typing.type_check_only
class GoogleCloudDialogflowV2Generator(typing.TypedDict, total=False):
    agentCoachingContext: GoogleCloudDialogflowV2AgentCoachingContext
    cesAppSpecs: _list[GoogleCloudDialogflowV2CesAppSpec]
    cesToolSpecs: _list[GoogleCloudDialogflowV2CesToolSpec]
    createTime: str
    description: str
    freeFormContext: GoogleCloudDialogflowV2FreeFormContext
    inferenceParameter: GoogleCloudDialogflowV2InferenceParameter
    name: str
    publishedModel: str
    suggestionDedupingConfig: GoogleCloudDialogflowV2SuggestionDedupingConfig
    summarizationContext: GoogleCloudDialogflowV2SummarizationContext
    tools: _list[str]
    toolsetTools: _list[GoogleCloudDialogflowV2ToolsetTool]
    triggerEvent: typing.Literal[
        "TRIGGER_EVENT_UNSPECIFIED",
        "END_OF_UTTERANCE",
        "MANUAL_CALL",
        "CUSTOMER_MESSAGE",
        "AGENT_MESSAGE",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorEvaluation(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    displayName: str
    evaluationStatus: GoogleCloudDialogflowV2EvaluationStatus
    generatorEvaluationConfig: GoogleCloudDialogflowV2GeneratorEvaluationConfig
    initialGenerator: GoogleCloudDialogflowV2Generator
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    summarizationMetrics: GoogleCloudDialogflowV2SummarizationEvaluationMetrics

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorEvaluationConfig(typing.TypedDict, total=False):
    inputDataConfig: GoogleCloudDialogflowV2GeneratorEvaluationConfigInputDataConfig
    outputGcsBucketPath: str
    summarizationConfig: (
        GoogleCloudDialogflowV2GeneratorEvaluationConfigSummarizationConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorEvaluationConfigAgentAssistInputDataConfig(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorEvaluationConfigDatasetInputDataConfig(
    typing.TypedDict, total=False
):
    dataset: str

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorEvaluationConfigInputDataConfig(
    typing.TypedDict, total=False
):
    agentAssistInputDataConfig: (
        GoogleCloudDialogflowV2GeneratorEvaluationConfigAgentAssistInputDataConfig
    )
    datasetInputDataConfig: (
        GoogleCloudDialogflowV2GeneratorEvaluationConfigDatasetInputDataConfig
    )
    endTime: str
    inputDataSourceType: typing.Literal[
        "INPUT_DATA_SOURCE_TYPE_UNSPECIFIED",
        "AGENT_ASSIST_CONVERSATIONS",
        "INSIGHTS_CONVERSATIONS",
    ]
    isSummaryGenerationAllowed: bool
    sampleSize: int
    startTime: str
    summaryGenerationOption: typing.Literal[
        "SUMMARY_GENERATION_OPTION_UNSPECIFIED",
        "ALWAYS_GENERATE",
        "GENERATE_IF_MISSING",
        "DO_NOT_GENERATE",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorEvaluationConfigSummarizationConfig(
    typing.TypedDict, total=False
):
    accuracyEvaluationVersion: str
    completenessEvaluationVersion: str
    enableAccuracyEvaluation: bool
    enableCompletenessEvaluation: bool
    evaluatorVersion: str

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorSuggestion(typing.TypedDict, total=False):
    agentCoachingSuggestion: GoogleCloudDialogflowV2AgentCoachingSuggestion
    freeFormSuggestion: GoogleCloudDialogflowV2FreeFormSuggestion
    summarySuggestion: GoogleCloudDialogflowV2SummarySuggestion
    toolCallInfo: _list[GoogleCloudDialogflowV2GeneratorSuggestionToolCallInfo]

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorSuggestionToolCallInfo(
    typing.TypedDict, total=False
):
    toolCall: GoogleCloudDialogflowV2ToolCall
    toolCallResult: GoogleCloudDialogflowV2ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfig(typing.TypedDict, total=False):
    endUserSuggestionConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionConfig
    )
    humanAgentSuggestionConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionConfig
    )
    messageAnalysisConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigMessageAnalysisConfig
    )
    notificationConfig: GoogleCloudDialogflowV2NotificationConfig

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfig(
    typing.TypedDict, total=False
):
    baselineModelVersion: str
    model: str

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfig(
    typing.TypedDict, total=False
):
    recentSentencesCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigMessageAnalysisConfig(
    typing.TypedDict, total=False
):
    enableEntityExtraction: bool
    enableSentimentAnalysis: bool
    enableSentimentAnalysisV3: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionConfig(
    typing.TypedDict, total=False
):
    disableHighLatencyFeaturesSyncDelivery: bool
    enableAsyncToolCall: bool
    featureConfigs: _list[
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig
    ]
    generators: _list[str]
    groupSuggestionResponses: bool
    skipEmptyEventBasedSuggestion: bool
    useUnredactedConversationData: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig(
    typing.TypedDict, total=False
):
    conversationModelConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfig
    )
    conversationProcessConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfig
    )
    disableAgentQueryLogging: bool
    disableQuerySearchContext: bool
    enableConversationAugmentedQuery: bool
    enableEventBasedSuggestion: bool
    enableQuerySuggestionOnly: bool
    enableQuerySuggestionWhenNoAnswer: bool
    enableResponseDebugInfo: bool
    queryConfig: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfig
    raiSettings: GoogleCloudDialogflowV2RaiSettings
    suggestionFeature: GoogleCloudDialogflowV2SuggestionFeature
    suggestionTriggerEvent: typing.Literal[
        "TRIGGER_EVENT_UNSPECIFIED",
        "END_OF_UTTERANCE",
        "MANUAL_CALL",
        "CUSTOMER_MESSAGE",
        "AGENT_MESSAGE",
    ]
    suggestionTriggerSettings: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionTriggerSettings
    )

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfig(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    contextFilterSettings: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigContextFilterSettings
    contextSize: int
    dialogflowQuerySource: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySource
    documentQuerySource: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDocumentQuerySource
    knowledgeBaseQuerySource: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigKnowledgeBaseQuerySource
    maxResults: int
    sections: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigSections
    )

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigContextFilterSettings(
    typing.TypedDict, total=False
):
    dropHandoffMessages: bool
    dropIvrMessages: bool
    dropVirtualAgentMessages: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySource(
    typing.TypedDict, total=False
):
    agent: str
    humanAgentSideConfig: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySourceHumanAgentSideConfig

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySourceHumanAgentSideConfig(
    typing.TypedDict, total=False
):
    agent: str

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDocumentQuerySource(
    typing.TypedDict, total=False
):
    documents: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigKnowledgeBaseQuerySource(
    typing.TypedDict, total=False
):
    knowledgeBases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigSections(
    typing.TypedDict, total=False
):
    sectionTypes: _list[
        typing.Literal[
            "SECTION_TYPE_UNSPECIFIED",
            "SITUATION",
            "ACTION",
            "RESOLUTION",
            "REASON_FOR_CANCELLATION",
            "CUSTOMER_SATISFACTION",
            "ENTITIES",
        ]
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionTriggerSettings(
    typing.TypedDict, total=False
):
    noSmalltalk: bool
    onlyEndUser: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantEvent(typing.TypedDict, total=False):
    conversation: str
    participant: str
    suggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentHandoffConfig(typing.TypedDict, total=False):
    livePersonConfig: GoogleCloudDialogflowV2HumanAgentHandoffConfigLivePersonConfig
    salesforceLiveAgentConfig: (
        GoogleCloudDialogflowV2HumanAgentHandoffConfigSalesforceLiveAgentConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentHandoffConfigLivePersonConfig(
    typing.TypedDict, total=False
):
    accountNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentHandoffConfigSalesforceLiveAgentConfig(
    typing.TypedDict, total=False
):
    buttonId: str
    deploymentId: str
    endpointDomain: str
    organizationId: str

@typing.type_check_only
class GoogleCloudDialogflowV2ImportAgentRequest(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ImportConversationDataOperationMetadata(
    typing.TypedDict, total=False
):
    conversationDataset: str
    createTime: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowV2ImportConversationDataOperationResponse(
    typing.TypedDict, total=False
):
    conversationDataset: str
    importCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2ImportConversationDataRequest(
    typing.TypedDict, total=False
):
    inputConfig: GoogleCloudDialogflowV2InputConfig

@typing.type_check_only
class GoogleCloudDialogflowV2ImportDocumentTemplate(typing.TypedDict, total=False):
    knowledgeTypes: _list[
        typing.Literal[
            "KNOWLEDGE_TYPE_UNSPECIFIED",
            "FAQ",
            "EXTRACTIVE_QA",
            "ARTICLE_SUGGESTION",
            "AGENT_FACING_SMART_REPLY",
        ]
    ]
    metadata: dict[str, typing.Any]
    mimeType: str

@typing.type_check_only
class GoogleCloudDialogflowV2ImportDocumentsRequest(typing.TypedDict, total=False):
    documentTemplate: GoogleCloudDialogflowV2ImportDocumentTemplate
    gcsSource: GoogleCloudDialogflowV2GcsSources
    importGcsCustomMetadata: bool

@typing.type_check_only
class GoogleCloudDialogflowV2ImportDocumentsResponse(typing.TypedDict, total=False):
    warnings: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowV2InferenceParameter(typing.TypedDict, total=False):
    maxOutputTokens: int
    temperature: float
    topK: int
    topP: float

@typing.type_check_only
class GoogleCloudDialogflowV2IngestContextReferencesRequest(
    typing.TypedDict, total=False
):
    contextReferences: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2IngestContextReferencesResponse(
    typing.TypedDict, total=False
):
    ingestedContextReferences: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2IngestedContextReferenceDebugInfo(
    typing.TypedDict, total=False
):
    contextReferenceRetrieved: bool
    ingestedParametersDebugInfo: _list[
        GoogleCloudDialogflowV2IngestedContextReferenceDebugInfoIngestedParameterDebugInfo
    ]
    projectNotAllowlisted: bool

@typing.type_check_only
class GoogleCloudDialogflowV2IngestedContextReferenceDebugInfoIngestedParameterDebugInfo(
    typing.TypedDict, total=False
):
    ingestionStatus: typing.Literal[
        "INGESTION_STATUS_UNSPECIFIED",
        "INGESTION_STATUS_SUCCEEDED",
        "INGESTION_STATUS_CONTEXT_NOT_AVAILABLE",
        "INGESTION_STATUS_PARSE_FAILED",
        "INGESTION_STATUS_INVALID_ENTRY",
        "INGESTION_STATUS_INVALID_FORMAT",
        "INGESTION_STATUS_LANGUAGE_MISMATCH",
    ]
    parameter: str

@typing.type_check_only
class GoogleCloudDialogflowV2InitializeEncryptionSpecMetadata(
    typing.TypedDict, total=False
):
    request: GoogleCloudDialogflowV2InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudDialogflowV2InitializeEncryptionSpecRequest(
    typing.TypedDict, total=False
):
    encryptionSpec: GoogleCloudDialogflowV2EncryptionSpec

@typing.type_check_only
class GoogleCloudDialogflowV2InputAudioConfig(typing.TypedDict, total=False):
    audioEncoding: typing.Literal[
        "AUDIO_ENCODING_UNSPECIFIED",
        "AUDIO_ENCODING_LINEAR_16",
        "AUDIO_ENCODING_FLAC",
        "AUDIO_ENCODING_MULAW",
        "AUDIO_ENCODING_AMR",
        "AUDIO_ENCODING_AMR_WB",
        "AUDIO_ENCODING_OGG_OPUS",
        "AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE",
        "AUDIO_ENCODING_ALAW",
    ]
    disableNoSpeechRecognizedEvent: bool
    enableAutomaticPunctuation: bool
    enableVoiceActivityEvents: bool
    enableWordInfo: bool
    languageCode: str
    model: str
    modelVariant: typing.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]
    optOutConformerModelMigration: bool
    phraseHints: _list[str]
    phraseSets: _list[str]
    sampleRateHertz: int
    singleUtterance: bool
    speechContexts: _list[GoogleCloudDialogflowV2SpeechContext]

@typing.type_check_only
class GoogleCloudDialogflowV2InputConfig(typing.TypedDict, total=False):
    gcsSource: GoogleCloudDialogflowV2GcsSources

@typing.type_check_only
class GoogleCloudDialogflowV2InputDataset(typing.TypedDict, total=False):
    dataset: str

@typing.type_check_only
class GoogleCloudDialogflowV2Intent(typing.TypedDict, total=False):
    action: str
    defaultResponsePlatforms: _list[
        typing.Literal[
            "PLATFORM_UNSPECIFIED",
            "FACEBOOK",
            "SLACK",
            "TELEGRAM",
            "KIK",
            "SKYPE",
            "LINE",
            "VIBER",
            "ACTIONS_ON_GOOGLE",
            "GOOGLE_HANGOUTS",
        ]
    ]
    displayName: str
    endInteraction: bool
    events: _list[str]
    followupIntentInfo: _list[GoogleCloudDialogflowV2IntentFollowupIntentInfo]
    inputContextNames: _list[str]
    isFallback: bool
    liveAgentHandoff: bool
    messages: _list[GoogleCloudDialogflowV2IntentMessage]
    mlDisabled: bool
    name: str
    outputContexts: _list[GoogleCloudDialogflowV2Context]
    parameters: _list[GoogleCloudDialogflowV2IntentParameter]
    parentFollowupIntentName: str
    priority: int
    resetContexts: bool
    rootFollowupIntentName: str
    trainingPhrases: _list[GoogleCloudDialogflowV2IntentTrainingPhrase]
    webhookState: typing.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentBatch(typing.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowV2Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentFollowupIntentInfo(typing.TypedDict, total=False):
    followupIntentName: str
    parentFollowupIntentName: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessage(typing.TypedDict, total=False):
    basicCard: GoogleCloudDialogflowV2IntentMessageBasicCard
    browseCarouselCard: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard
    card: GoogleCloudDialogflowV2IntentMessageCard
    carouselSelect: GoogleCloudDialogflowV2IntentMessageCarouselSelect
    image: GoogleCloudDialogflowV2IntentMessageImage
    linkOutSuggestion: GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion
    listSelect: GoogleCloudDialogflowV2IntentMessageListSelect
    mediaContent: GoogleCloudDialogflowV2IntentMessageMediaContent
    payload: dict[str, typing.Any]
    platform: typing.Literal[
        "PLATFORM_UNSPECIFIED",
        "FACEBOOK",
        "SLACK",
        "TELEGRAM",
        "KIK",
        "SKYPE",
        "LINE",
        "VIBER",
        "ACTIONS_ON_GOOGLE",
        "GOOGLE_HANGOUTS",
    ]
    quickReplies: GoogleCloudDialogflowV2IntentMessageQuickReplies
    simpleResponses: GoogleCloudDialogflowV2IntentMessageSimpleResponses
    suggestions: GoogleCloudDialogflowV2IntentMessageSuggestions
    tableCard: GoogleCloudDialogflowV2IntentMessageTableCard
    text: GoogleCloudDialogflowV2IntentMessageText

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBasicCard(typing.TypedDict, total=False):
    buttons: _list[GoogleCloudDialogflowV2IntentMessageBasicCardButton]
    formattedText: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBasicCardButton(
    typing.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard(
    typing.TypedDict, total=False
):
    imageDisplayOptions: typing.Literal[
        "IMAGE_DISPLAY_OPTIONS_UNSPECIFIED",
        "GRAY",
        "WHITE",
        "CROPPED",
        "BLURRED_BACKGROUND",
    ]
    items: _list[
        GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItem
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing.TypedDict, total=False
):
    description: str
    footer: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    openUriAction: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing.TypedDict, total=False
):
    url: str
    urlTypeHint: typing.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCard(typing.TypedDict, total=False):
    buttons: _list[GoogleCloudDialogflowV2IntentMessageCardButton]
    imageUri: str
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCardButton(typing.TypedDict, total=False):
    postback: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCarouselSelect(typing.TypedDict, total=False):
    items: _list[GoogleCloudDialogflowV2IntentMessageCarouselSelectItem]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCarouselSelectItem(
    typing.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageColumnProperties(
    typing.TypedDict, total=False
):
    header: str
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageImage(typing.TypedDict, total=False):
    accessibilityText: str
    imageUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion(
    typing.TypedDict, total=False
):
    destinationName: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageListSelect(typing.TypedDict, total=False):
    items: _list[GoogleCloudDialogflowV2IntentMessageListSelectItem]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageListSelectItem(typing.TypedDict, total=False):
    description: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageMediaContent(typing.TypedDict, total=False):
    mediaObjects: _list[
        GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject
    ]
    mediaType: typing.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject(
    typing.TypedDict, total=False
):
    contentUrl: str
    description: str
    icon: GoogleCloudDialogflowV2IntentMessageImage
    largeImage: GoogleCloudDialogflowV2IntentMessageImage
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageQuickReplies(typing.TypedDict, total=False):
    quickReplies: _list[str]
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSelectItemInfo(typing.TypedDict, total=False):
    key: str
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSimpleResponse(typing.TypedDict, total=False):
    displayText: str
    ssml: str
    textToSpeech: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSimpleResponses(
    typing.TypedDict, total=False
):
    simpleResponses: _list[GoogleCloudDialogflowV2IntentMessageSimpleResponse]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSuggestion(typing.TypedDict, total=False):
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSuggestions(typing.TypedDict, total=False):
    suggestions: _list[GoogleCloudDialogflowV2IntentMessageSuggestion]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageTableCard(typing.TypedDict, total=False):
    buttons: _list[GoogleCloudDialogflowV2IntentMessageBasicCardButton]
    columnProperties: _list[GoogleCloudDialogflowV2IntentMessageColumnProperties]
    image: GoogleCloudDialogflowV2IntentMessageImage
    rows: _list[GoogleCloudDialogflowV2IntentMessageTableCardRow]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageTableCardCell(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageTableCardRow(typing.TypedDict, total=False):
    cells: _list[GoogleCloudDialogflowV2IntentMessageTableCardCell]
    dividerAfter: bool

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageText(typing.TypedDict, total=False):
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentParameter(typing.TypedDict, total=False):
    defaultValue: str
    displayName: str
    entityTypeDisplayName: str
    isList: bool
    mandatory: bool
    name: str
    prompts: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentSuggestion(typing.TypedDict, total=False):
    description: str
    displayName: str
    intentV2: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentTrainingPhrase(typing.TypedDict, total=False):
    name: str
    parts: _list[GoogleCloudDialogflowV2IntentTrainingPhrasePart]
    timesAddedCount: int
    type: typing.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentTrainingPhrasePart(typing.TypedDict, total=False):
    alias: str
    entityType: str
    text: str
    userDefined: bool

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswer(typing.TypedDict, total=False):
    answerRecord: str
    knowledgeAssistDebugInfo: GoogleCloudDialogflowV2KnowledgeAssistDebugInfo
    suggestedQuery: GoogleCloudDialogflowV2KnowledgeAssistAnswerSuggestedQuery
    suggestedQueryAnswer: GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswer

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerAdditionalSuggestedQueryResult(
    typing.TypedDict, total=False
):
    answerRecord: str
    suggestedQuery: GoogleCloudDialogflowV2KnowledgeAssistAnswerSuggestedQuery

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswer(
    typing.TypedDict, total=False
):
    answerText: str
    eventSource: GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerEventSource
    faqSource: GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerFaqSource
    generativeSource: (
        GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )
    playbookSource: (
        GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerEventSource(
    typing.TypedDict, total=False
):
    event: str
    snippets: (
        GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerFaqSource(
    typing.TypedDict, total=False
):
    question: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource(
    typing.TypedDict, total=False
):
    snippets: _list[
        GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerSuggestedQuery(
    typing.TypedDict, total=False
):
    queryText: str
    searchContexts: _list[
        GoogleCloudDialogflowV2KnowledgeAssistAnswerSuggestedQuerySearchContext
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerSuggestedQuerySearchContext(
    typing.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistDebugInfo(typing.TypedDict, total=False):
    cesDebugInfo: dict[str, typing.Any]
    datastoreResponseReason: typing.Literal[
        "DATASTORE_RESPONSE_REASON_UNSPECIFIED",
        "NONE",
        "SEARCH_OUT_OF_QUOTA",
        "SEARCH_EMPTY_RESULTS",
        "ANSWER_GENERATION_GEN_AI_DISABLED",
        "ANSWER_GENERATION_OUT_OF_QUOTA",
        "ANSWER_GENERATION_ERROR",
        "ANSWER_GENERATION_NOT_ENOUGH_INFO",
        "ANSWER_GENERATION_RAI_FAILED",
        "ANSWER_GENERATION_NOT_GROUNDED",
    ]
    ingestedContextReferenceDebugInfo: (
        GoogleCloudDialogflowV2IngestedContextReferenceDebugInfo
    )
    knowledgeAssistBehavior: (
        GoogleCloudDialogflowV2KnowledgeAssistDebugInfoKnowledgeAssistBehavior
    )
    queryCategorizationFailureReason: typing.Literal[
        "QUERY_CATEGORIZATION_FAILURE_REASON_UNSPECIFIED",
        "QUERY_CATEGORIZATION_INVALID_CONFIG",
        "QUERY_CATEGORIZATION_RESULT_NOT_FOUND",
        "QUERY_CATEGORIZATION_FAILED",
    ]
    queryGenerationDebugInfo: (
        GoogleCloudDialogflowV2KnowledgeAssistDebugInfoQueryGenerationDebugInfo
    )
    queryGenerationFailureReason: typing.Literal[
        "QUERY_GENERATION_FAILURE_REASON_UNSPECIFIED",
        "QUERY_GENERATION_OUT_OF_QUOTA",
        "QUERY_GENERATION_FAILED",
        "QUERY_GENERATION_NO_QUERY_GENERATED",
        "QUERY_GENERATION_RAI_FAILED",
        "NOT_IN_ALLOWLIST",
        "QUERY_GENERATION_QUERY_REDACTED",
        "QUERY_GENERATION_LLM_RESPONSE_PARSE_FAILED",
        "QUERY_GENERATION_EMPTY_CONVERSATION",
        "QUERY_GENERATION_EMPTY_LAST_MESSAGE",
        "QUERY_GENERATION_TRIGGERING_EVENT_CONDITION_NOT_MET",
    ]
    serviceLatency: GoogleCloudDialogflowV2ServiceLatency

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistDebugInfoKnowledgeAssistBehavior(
    typing.TypedDict, total=False
):
    answerGenerationRewriterOn: bool
    appendedSearchContextCount: int
    conversationTranscriptHasMixedLanguages: bool
    disableSyncDelivery: bool
    endUserMetadataIncluded: bool
    invalidItemsQuerySuggestionSkipped: bool
    multipleQueriesGenerated: bool
    previousQueriesIncluded: bool
    primaryQueryRedactedAndReplaced: bool
    queryContainedSearchContext: bool
    queryGenerationAgentLanguageMismatch: bool
    queryGenerationEndUserLanguageMismatch: bool
    returnQueryOnly: bool
    thirdPartyConnectorAllowed: bool
    useCustomSafetyFilterLevel: bool
    usePubsubDelivery: bool
    useTranslatedMessage: bool

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistDebugInfoQueryGenerationDebugInfo(
    typing.TypedDict, total=False
):
    candidatesTokenCount: int
    promptTokenCount: int
    similarityToLastQuery: float
    similarityToLastQueryThreshold: float
    thinkingBudgetTokens: int
    thinkingLevel: str
    totalTokenCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeBase(typing.TypedDict, total=False):
    displayName: str
    languageCode: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeOperationMetadata(typing.TypedDict, total=False):
    doneTime: str
    exportOperationMetadata: GoogleCloudDialogflowV2ExportOperationMetadata
    knowledgeBase: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

@typing.type_check_only
class GoogleCloudDialogflowV2ListAnswerRecordsResponse(typing.TypedDict, total=False):
    answerRecords: _list[GoogleCloudDialogflowV2AnswerRecord]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListContextsResponse(typing.TypedDict, total=False):
    contexts: _list[GoogleCloudDialogflowV2Context]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationDatasetsResponse(
    typing.TypedDict, total=False
):
    conversationDatasets: _list[GoogleCloudDialogflowV2ConversationDataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationModelEvaluationsResponse(
    typing.TypedDict, total=False
):
    conversationModelEvaluations: _list[
        GoogleCloudDialogflowV2ConversationModelEvaluation
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationModelsResponse(
    typing.TypedDict, total=False
):
    conversationModels: _list[GoogleCloudDialogflowV2ConversationModel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationProfilesResponse(
    typing.TypedDict, total=False
):
    conversationProfiles: _list[GoogleCloudDialogflowV2ConversationProfile]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationsResponse(typing.TypedDict, total=False):
    conversations: _list[GoogleCloudDialogflowV2Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListDocumentsResponse(typing.TypedDict, total=False):
    documents: _list[GoogleCloudDialogflowV2Document]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListEntityTypesResponse(typing.TypedDict, total=False):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListEnvironmentsResponse(typing.TypedDict, total=False):
    environments: _list[GoogleCloudDialogflowV2Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListGeneratorEvaluationsResponse(
    typing.TypedDict, total=False
):
    generatorEvaluations: _list[GoogleCloudDialogflowV2GeneratorEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListGeneratorsResponse(typing.TypedDict, total=False):
    generators: _list[GoogleCloudDialogflowV2Generator]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListIntentsResponse(typing.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowV2Intent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListKnowledgeBasesResponse(typing.TypedDict, total=False):
    knowledgeBases: _list[GoogleCloudDialogflowV2KnowledgeBase]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListMessagesResponse(typing.TypedDict, total=False):
    messages: _list[GoogleCloudDialogflowV2Message]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListParticipantsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    participants: _list[GoogleCloudDialogflowV2Participant]

@typing.type_check_only
class GoogleCloudDialogflowV2ListSessionEntityTypesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: _list[GoogleCloudDialogflowV2SessionEntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2ListSipTrunksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sipTrunks: _list[GoogleCloudDialogflowV2SipTrunk]

@typing.type_check_only
class GoogleCloudDialogflowV2ListToolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tools: _list[GoogleCloudDialogflowV2Tool]

@typing.type_check_only
class GoogleCloudDialogflowV2ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[GoogleCloudDialogflowV2Version]

@typing.type_check_only
class GoogleCloudDialogflowV2LoggingConfig(typing.TypedDict, total=False):
    enableStackdriverLogging: bool

@typing.type_check_only
class GoogleCloudDialogflowV2Message(typing.TypedDict, total=False):
    content: str
    createTime: str
    languageCode: str
    messageAnnotation: GoogleCloudDialogflowV2MessageAnnotation
    name: str
    participant: str
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    sendTime: str
    sentimentAnalysis: GoogleCloudDialogflowV2SentimentAnalysisResult

@typing.type_check_only
class GoogleCloudDialogflowV2MessageAnnotation(typing.TypedDict, total=False):
    containEntities: bool
    parts: _list[GoogleCloudDialogflowV2AnnotatedMessagePart]

@typing.type_check_only
class GoogleCloudDialogflowV2MessageEntry(typing.TypedDict, total=False):
    createTime: str
    languageCode: str
    role: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2NotificationConfig(typing.TypedDict, total=False):
    messageFormat: typing.Literal["MESSAGE_FORMAT_UNSPECIFIED", "PROTO", "JSON"]
    topic: str

@typing.type_check_only
class GoogleCloudDialogflowV2OriginalDetectIntentRequest(typing.TypedDict, total=False):
    payload: dict[str, typing.Any]
    source: str
    version: str

@typing.type_check_only
class GoogleCloudDialogflowV2OutputAudio(typing.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowV2OutputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowV2OutputAudioConfig(typing.TypedDict, total=False):
    audioEncoding: typing.Literal[
        "OUTPUT_AUDIO_ENCODING_UNSPECIFIED",
        "OUTPUT_AUDIO_ENCODING_LINEAR_16",
        "OUTPUT_AUDIO_ENCODING_MP3",
        "OUTPUT_AUDIO_ENCODING_MP3_64_KBPS",
        "OUTPUT_AUDIO_ENCODING_OGG_OPUS",
        "OUTPUT_AUDIO_ENCODING_MULAW",
        "OUTPUT_AUDIO_ENCODING_ALAW",
    ]
    sampleRateHertz: int
    synthesizeSpeechConfig: GoogleCloudDialogflowV2SynthesizeSpeechConfig

@typing.type_check_only
class GoogleCloudDialogflowV2Participant(typing.TypedDict, total=False):
    agentDesktopSource: typing.Literal[
        "AGENT_DESKTOP_SOURCE_UNSPECIFIED",
        "LIVE_PERSON",
        "GENESYS_CLOUD",
        "TWILIO",
        "SALESFORCE",
        "OTHER",
    ]
    documentsMetadataFilters: dict[str, typing.Any]
    name: str
    obfuscatedExternalUserId: str
    role: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    sipRecordingMediaLabel: str

@typing.type_check_only
class GoogleCloudDialogflowV2ProbeDetails(typing.TypedDict, total=False):
    initTime: str
    optionsLatency: str
    probeStatus: typing.Literal[
        "PROBE_STATUS_UNSPECIFIED", "PROBE_STATUS_SUCCESS", "PROBE_STATUS_FAILED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2QueryInput(typing.TypedDict, total=False):
    audioConfig: GoogleCloudDialogflowV2InputAudioConfig
    event: GoogleCloudDialogflowV2EventInput
    text: GoogleCloudDialogflowV2TextInput

@typing.type_check_only
class GoogleCloudDialogflowV2QueryParameters(typing.TypedDict, total=False):
    contexts: _list[GoogleCloudDialogflowV2Context]
    geoLocation: GoogleTypeLatLng
    payload: dict[str, typing.Any]
    platform: str
    resetContexts: bool
    sentimentAnalysisRequestConfig: (
        GoogleCloudDialogflowV2SentimentAnalysisRequestConfig
    )
    sessionEntityTypes: _list[GoogleCloudDialogflowV2SessionEntityType]
    timeZone: str
    webhookHeaders: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2QueryResult(typing.TypedDict, total=False):
    action: str
    allRequiredParamsPresent: bool
    cancelsSlotFilling: bool
    diagnosticInfo: dict[str, typing.Any]
    fulfillmentMessages: _list[GoogleCloudDialogflowV2IntentMessage]
    fulfillmentText: str
    intent: GoogleCloudDialogflowV2Intent
    intentDetectionConfidence: float
    languageCode: str
    outputContexts: _list[GoogleCloudDialogflowV2Context]
    parameters: dict[str, typing.Any]
    queryText: str
    sentimentAnalysisResult: GoogleCloudDialogflowV2SentimentAnalysisResult
    speechRecognitionConfidence: float
    webhookPayload: dict[str, typing.Any]
    webhookSource: str

@typing.type_check_only
class GoogleCloudDialogflowV2RaiSettings(typing.TypedDict, total=False):
    raiCategoryConfigs: _list[GoogleCloudDialogflowV2RaiSettingsRaiCategoryConfig]

@typing.type_check_only
class GoogleCloudDialogflowV2RaiSettingsRaiCategoryConfig(
    typing.TypedDict, total=False
):
    category: typing.Literal[
        "RAI_CATEGORY_UNSPECIFIED",
        "DANGEROUS_CONTENT",
        "SEXUALLY_EXPLICIT",
        "HARASSMENT",
        "HATE_SPEECH",
    ]
    sensitivityLevel: typing.Literal[
        "SENSITIVITY_LEVEL_UNSPECIFIED",
        "BLOCK_MOST",
        "BLOCK_SOME",
        "BLOCK_FEW",
        "BLOCK_NONE",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ReloadDocumentRequest(typing.TypedDict, total=False):
    contentUri: str
    importGcsCustomMetadata: bool
    smartMessagingPartialUpdate: bool

@typing.type_check_only
class GoogleCloudDialogflowV2RestoreAgentRequest(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchAgentsResponse(typing.TypedDict, total=False):
    agents: _list[GoogleCloudDialogflowV2Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeAnswer(typing.TypedDict, total=False):
    answer: str
    answerRecord: str
    answerSources: _list[GoogleCloudDialogflowV2SearchKnowledgeAnswerAnswerSource]
    answerType: typing.Literal[
        "ANSWER_TYPE_UNSPECIFIED", "FAQ", "GENERATIVE", "INTENT", "PLAYBOOK", "EVENT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeAnswerAnswerSource(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]
    snippet: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeDebugInfo(typing.TypedDict, total=False):
    cesDebugInfo: dict[str, typing.Any]
    datastoreResponseReason: typing.Literal[
        "DATASTORE_RESPONSE_REASON_UNSPECIFIED",
        "NONE",
        "SEARCH_OUT_OF_QUOTA",
        "SEARCH_EMPTY_RESULTS",
        "ANSWER_GENERATION_GEN_AI_DISABLED",
        "ANSWER_GENERATION_OUT_OF_QUOTA",
        "ANSWER_GENERATION_ERROR",
        "ANSWER_GENERATION_NOT_ENOUGH_INFO",
        "ANSWER_GENERATION_RAI_FAILED",
        "ANSWER_GENERATION_NOT_GROUNDED",
    ]
    ingestedContextReferenceDebugInfo: (
        GoogleCloudDialogflowV2IngestedContextReferenceDebugInfo
    )
    searchKnowledgeBehavior: (
        GoogleCloudDialogflowV2SearchKnowledgeDebugInfoSearchKnowledgeBehavior
    )
    serviceLatency: GoogleCloudDialogflowV2ServiceLatency

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeDebugInfoSearchKnowledgeBehavior(
    typing.TypedDict, total=False
):
    answerGenerationRewriterOn: bool
    endUserMetadataIncluded: bool
    thirdPartyConnectorAllowed: bool

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequest(typing.TypedDict, total=False):
    conversation: str
    conversationProfile: str
    endUserMetadata: dict[str, typing.Any]
    exactSearch: bool
    latestMessage: str
    parent: str
    query: GoogleCloudDialogflowV2TextInput
    querySource: typing.Literal[
        "QUERY_SOURCE_UNSPECIFIED", "AGENT_QUERY", "SUGGESTED_QUERY"
    ]
    searchConfig: GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfig
    sessionId: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfig(
    typing.TypedDict, total=False
):
    boostSpecs: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecs
    ]
    filterSpecs: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigFilterSpecs
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecs(
    typing.TypedDict, total=False
):
    dataStores: _list[str]
    spec: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpec(
    typing.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigFilterSpecs(
    typing.TypedDict, total=False
):
    dataStores: _list[str]
    filter: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeResponse(typing.TypedDict, total=False):
    answers: _list[GoogleCloudDialogflowV2SearchKnowledgeAnswer]
    rewrittenQuery: str
    searchKnowledgeDebugInfo: GoogleCloudDialogflowV2SearchKnowledgeDebugInfo

@typing.type_check_only
class GoogleCloudDialogflowV2Sentiment(typing.TypedDict, total=False):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowV2SentimentAnalysisRequestConfig(
    typing.TypedDict, total=False
):
    analyzeQueryTextSentiment: bool

@typing.type_check_only
class GoogleCloudDialogflowV2SentimentAnalysisResult(typing.TypedDict, total=False):
    queryTextSentiment: GoogleCloudDialogflowV2Sentiment

@typing.type_check_only
class GoogleCloudDialogflowV2ServiceLatency(typing.TypedDict, total=False):
    internalServiceLatencies: _list[
        GoogleCloudDialogflowV2ServiceLatencyInternalServiceLatency
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ServiceLatencyInternalServiceLatency(
    typing.TypedDict, total=False
):
    completeTime: str
    latencyMs: float
    startTime: str
    step: str

@typing.type_check_only
class GoogleCloudDialogflowV2SessionEntityType(typing.TypedDict, total=False):
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    entityOverrideMode: typing.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadata(
    typing.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ARTICLE_SUGGESTION",
        "FAQ",
        "SMART_REPLY",
        "CONVERSATION_SUMMARIZATION",
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SetSuggestionFeatureConfigRequest(
    typing.TypedDict, total=False
):
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowV2SipConfig(typing.TypedDict, total=False):
    allowVirtualAgentInteraction: bool
    copyInboundCallLegHeaders: _list[str]
    createConversationOnTheFly: bool
    ignoreReinviteMediaDirection: bool
    inactiveStart: bool
    keepConversationRunning: bool
    maxAudioRecordingDuration: str

@typing.type_check_only
class GoogleCloudDialogflowV2SipHostname(typing.TypedDict, total=False):
    connectionState: typing.Literal[
        "CONNECTION_STATE_UNSPECIFIED",
        "CONNECTED",
        "DISCONNECTED",
        "AUTHENTICATION_FAILED",
        "KEEPALIVE",
    ]
    enabledSipPing: bool
    errorDetails: GoogleCloudDialogflowV2SipHostnameHostnameErrorDetails
    peerHostname: str
    peerSocketAddress: str
    pingInterval: str
    probeDetails: GoogleCloudDialogflowV2ProbeDetails

@typing.type_check_only
class GoogleCloudDialogflowV2SipHostnameHostnameErrorDetails(
    typing.TypedDict, total=False
):
    certificateState: typing.Literal[
        "HOSTNAME_CERTIFICATE_STATE_UNSPECIFIED",
        "VALID",
        "INVALID",
        "EXPIRED",
        "HOSTNAME_NOT_FOUND",
        "UNAUTHENTICATED",
        "TRUST_STORE_NOT_FOUND",
        "HOSTNAME_INVALID_FORMAT",
        "QUOTA_EXCEEDED",
    ]
    errorMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SipTrunk(typing.TypedDict, total=False):
    connections: _list[GoogleCloudDialogflowV2Connection]
    displayName: str
    expectedHostname: _list[str]
    googleRootCertFile: typing.Literal["CERT_FILE_UNSPECIFIED", "EXTERNAL_PRIVATE_CA"]
    name: str
    peerHostnames: _list[GoogleCloudDialogflowV2SipHostname]

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyAnswer(typing.TypedDict, total=False):
    answerRecord: str
    confidence: float
    reply: str

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyMetrics(typing.TypedDict, total=False):
    allowlistCoverage: float
    conversationCount: str
    topNMetrics: _list[GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics]

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics(
    typing.TypedDict, total=False
):
    n: int
    recall: float

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyModelMetadata(typing.TypedDict, total=False):
    trainingModelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "SMART_REPLY_DUAL_ENCODER_MODEL",
        "SMART_REPLY_BERT_MODEL",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SpeechContext(typing.TypedDict, total=False):
    boost: float
    phrases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2SpeechToTextConfig(typing.TypedDict, total=False):
    audioEncoding: typing.Literal[
        "AUDIO_ENCODING_UNSPECIFIED",
        "AUDIO_ENCODING_LINEAR_16",
        "AUDIO_ENCODING_FLAC",
        "AUDIO_ENCODING_MULAW",
        "AUDIO_ENCODING_AMR",
        "AUDIO_ENCODING_AMR_WB",
        "AUDIO_ENCODING_OGG_OPUS",
        "AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE",
        "AUDIO_ENCODING_ALAW",
    ]
    enableWordInfo: bool
    languageCode: str
    model: str
    phraseSets: _list[str]
    sampleRateHertz: int
    speechModelVariant: typing.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]
    useTimeoutBasedEndpointing: bool

@typing.type_check_only
class GoogleCloudDialogflowV2SpeechWordInfo(typing.TypedDict, total=False):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudDialogflowV2StreamingRecognitionResult(typing.TypedDict, total=False):
    confidence: float
    isFinal: bool
    languageCode: str
    messageType: typing.Literal[
        "MESSAGE_TYPE_UNSPECIFIED",
        "TRANSCRIPT",
        "DTMF_DIGITS",
        "END_OF_SINGLE_UTTERANCE",
        "PARTIAL_DTMF_DIGITS",
        "SPEECH_ACTIVITY_BEGIN",
        "SPEECH_ACTIVITY_END",
    ]
    speechEndOffset: str
    speechWordInfo: _list[GoogleCloudDialogflowV2SpeechWordInfo]
    transcript: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestArticlesRequest(typing.TypedDict, total=False):
    assistQueryParams: GoogleCloudDialogflowV2AssistQueryParameters
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestArticlesResponse(typing.TypedDict, total=False):
    articleAnswers: _list[GoogleCloudDialogflowV2ArticleAnswer]
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestConversationSummaryRequest(
    typing.TypedDict, total=False
):
    assistQueryParams: GoogleCloudDialogflowV2AssistQueryParameters
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestConversationSummaryResponse(
    typing.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    summary: GoogleCloudDialogflowV2SuggestConversationSummaryResponseSummary

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestConversationSummaryResponseSummary(
    typing.TypedDict, total=False
):
    answerRecord: str
    baselineModelVersion: str
    sortedTextSections: _list[
        GoogleCloudDialogflowV2SuggestConversationSummaryResponseSummarySummarySection
    ]
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestConversationSummaryResponseSummarySummarySection(
    typing.TypedDict, total=False
):
    section: str
    summary: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestFaqAnswersRequest(typing.TypedDict, total=False):
    assistQueryParams: GoogleCloudDialogflowV2AssistQueryParameters
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestFaqAnswersResponse(typing.TypedDict, total=False):
    contextSize: int
    faqAnswers: _list[GoogleCloudDialogflowV2FaqAnswer]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestKnowledgeAssistRequest(
    typing.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    previousSuggestedQuery: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestKnowledgeAssistResponse(
    typing.TypedDict, total=False
):
    additionalSuggestedQueryResults: _list[
        GoogleCloudDialogflowV2KnowledgeAssistAnswerAdditionalSuggestedQueryResult
    ]
    contextSize: int
    knowledgeAssistAnswer: GoogleCloudDialogflowV2KnowledgeAssistAnswer
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestSmartRepliesRequest(typing.TypedDict, total=False):
    contextSize: int
    currentTextInput: GoogleCloudDialogflowV2TextInput
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestSmartRepliesResponse(typing.TypedDict, total=False):
    contextSize: int
    latestMessage: str
    smartReplyAnswers: _list[GoogleCloudDialogflowV2SmartReplyAnswer]

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionDedupingConfig(typing.TypedDict, total=False):
    enableDeduping: bool
    similarityThreshold: float

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionFeature(typing.TypedDict, total=False):
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ARTICLE_SUGGESTION",
        "FAQ",
        "SMART_REPLY",
        "CONVERSATION_SUMMARIZATION",
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionInput(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "CANCEL", "REVISE", "CONFIRM"]
    answerRecord: str
    parameters: dict[str, typing.Any]
    sendTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionResult(typing.TypedDict, total=False):
    error: GoogleRpcStatus
    generateSuggestionsResponse: GoogleCloudDialogflowV2GenerateSuggestionsResponse
    suggestArticlesResponse: GoogleCloudDialogflowV2SuggestArticlesResponse
    suggestFaqAnswersResponse: GoogleCloudDialogflowV2SuggestFaqAnswersResponse
    suggestKnowledgeAssistResponse: (
        GoogleCloudDialogflowV2SuggestKnowledgeAssistResponse
    )
    suggestSmartRepliesResponse: GoogleCloudDialogflowV2SuggestSmartRepliesResponse

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationContext(typing.TypedDict, total=False):
    fewShotExamples: _list[GoogleCloudDialogflowV2FewShotExample]
    outputLanguageCode: str
    summarizationSections: _list[GoogleCloudDialogflowV2SummarizationSection]
    version: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetrics(
    typing.TypedDict, total=False
):
    conversationDetails: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsConversationDetail
    ]
    overallMetrics: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsOverallScoresByMetric
    ]
    overallSectionTokens: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsSectionToken
    ]
    summarizationEvaluationMergedResultsUri: str
    summarizationEvaluationResults: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsSummarizationEvaluationResult
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsAccuracyDecomposition(
    typing.TypedDict, total=False
):
    accuracyReasoning: str
    isAccurate: bool
    point: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsAdherenceDecomposition(
    typing.TypedDict, total=False
):
    adherenceReasoning: str
    isAdherent: bool
    point: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsAdherenceRubric(
    typing.TypedDict, total=False
):
    isAddressed: bool
    question: str
    reasoning: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsCompletenessRubric(
    typing.TypedDict, total=False
):
    isAddressed: bool
    question: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsConversationDetail(
    typing.TypedDict, total=False
):
    messageEntries: _list[GoogleCloudDialogflowV2MessageEntry]
    metricDetails: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsConversationDetailMetricDetail
    ]
    sectionTokens: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsSectionToken
    ]
    summarySections: _list[GoogleCloudDialogflowV2SummarySuggestionSummarySection]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsConversationDetailMetricDetail(
    typing.TypedDict, total=False
):
    metric: str
    score: float
    sectionDetails: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsConversationDetailMetricDetailSectionDetail
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsConversationDetailMetricDetailSectionDetail(
    typing.TypedDict, total=False
):
    evaluationResults: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsEvaluationResult
    ]
    score: float
    section: str
    sectionSummary: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsDecomposition(
    typing.TypedDict, total=False
):
    accuracyDecomposition: (
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsAccuracyDecomposition
    )
    adherenceDecomposition: (
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsAdherenceDecomposition
    )

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsEvaluationResult(
    typing.TypedDict, total=False
):
    accuracyDecomposition: (
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsAccuracyDecomposition
    )
    adherenceRubric: (
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsAdherenceRubric
    )
    completenessRubric: (
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsCompletenessRubric
    )

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsOverallScoresByMetric(
    typing.TypedDict, total=False
):
    metric: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsSectionToken(
    typing.TypedDict, total=False
):
    section: str
    tokenCount: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationEvaluationMetricsSummarizationEvaluationResult(
    typing.TypedDict, total=False
):
    decompositions: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsDecomposition
    ]
    evaluationResults: _list[
        GoogleCloudDialogflowV2SummarizationEvaluationMetricsEvaluationResult
    ]
    metric: str
    score: float
    section: str
    sectionSummary: str
    sessionId: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationSection(typing.TypedDict, total=False):
    definition: str
    key: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "SITUATION",
        "ACTION",
        "RESOLUTION",
        "REASON_FOR_CANCELLATION",
        "CUSTOMER_SATISFACTION",
        "ENTITIES",
        "CUSTOMER_DEFINED",
        "SITUATION_CONCISE",
        "ACTION_CONCISE",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationSectionList(typing.TypedDict, total=False):
    summarizationSections: _list[GoogleCloudDialogflowV2SummarizationSection]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarySuggestion(typing.TypedDict, total=False):
    summarySections: _list[GoogleCloudDialogflowV2SummarySuggestionSummarySection]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarySuggestionSummarySection(
    typing.TypedDict, total=False
):
    section: str
    summary: str

@typing.type_check_only
class GoogleCloudDialogflowV2SynthesizeSpeechConfig(typing.TypedDict, total=False):
    effectsProfileId: _list[str]
    pitch: float
    pronunciations: _list[GoogleCloudDialogflowV2CustomPronunciationParams]
    speakingRate: float
    voice: GoogleCloudDialogflowV2VoiceSelectionParams
    volumeGainDb: float

@typing.type_check_only
class GoogleCloudDialogflowV2TextInput(typing.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2TextToSpeechSettings(typing.TypedDict, total=False):
    enableTextToSpeech: bool
    outputAudioEncoding: typing.Literal[
        "OUTPUT_AUDIO_ENCODING_UNSPECIFIED",
        "OUTPUT_AUDIO_ENCODING_LINEAR_16",
        "OUTPUT_AUDIO_ENCODING_MP3",
        "OUTPUT_AUDIO_ENCODING_MP3_64_KBPS",
        "OUTPUT_AUDIO_ENCODING_OGG_OPUS",
        "OUTPUT_AUDIO_ENCODING_MULAW",
        "OUTPUT_AUDIO_ENCODING_ALAW",
    ]
    sampleRateHertz: int
    synthesizeSpeechConfigs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2Tool(typing.TypedDict, total=False):
    actionConfirmationRequirement: dict[str, typing.Any]
    connectorSpec: GoogleCloudDialogflowV2ToolConnectorTool
    createTime: str
    description: str
    displayName: str
    extensionSpec: GoogleCloudDialogflowV2ToolExtensionTool
    functionSpec: GoogleCloudDialogflowV2ToolFunctionTool
    name: str
    openApiSpec: GoogleCloudDialogflowV2ToolOpenApiTool
    satisfiesPzi: bool
    satisfiesPzs: bool
    toolKey: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolAuthentication(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudDialogflowV2ToolAuthenticationApiKeyConfig
    bearerTokenConfig: GoogleCloudDialogflowV2ToolAuthenticationBearerTokenConfig
    oauthConfig: GoogleCloudDialogflowV2ToolAuthenticationOAuthConfig
    serviceAgentAuthConfig: (
        GoogleCloudDialogflowV2ToolAuthenticationServiceAgentAuthConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowV2ToolAuthenticationApiKeyConfig(
    typing.TypedDict, total=False
):
    apiKey: str
    keyName: str
    requestLocation: typing.Literal[
        "REQUEST_LOCATION_UNSPECIFIED", "HEADER", "QUERY_STRING"
    ]
    secretVersionForApiKey: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolAuthenticationBearerTokenConfig(
    typing.TypedDict, total=False
):
    secretVersionForToken: str
    token: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolAuthenticationOAuthConfig(
    typing.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    oauthGrantType: typing.Literal["OAUTH_GRANT_TYPE_UNSPECIFIED", "CLIENT_CREDENTIAL"]
    scopes: _list[str]
    secretVersionForClientSecret: str
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolAuthenticationServiceAgentAuthConfig(
    typing.TypedDict, total=False
):
    serviceAgentAuth: typing.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "ID_TOKEN", "ACCESS_TOKEN"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ToolCall(typing.TypedDict, total=False):
    action: str
    answerRecord: str
    cesApp: str
    cesTool: str
    cesToolset: str
    createTime: str
    inputParameters: dict[str, typing.Any]
    state: typing.Literal["STATE_UNSPECIFIED", "TRIGGERED", "NEEDS_CONFIRMATION"]
    tool: str
    toolDisplayDetails: str
    toolDisplayName: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolCallResult(typing.TypedDict, total=False):
    action: str
    answerRecord: str
    cesApp: str
    cesTool: str
    cesToolset: str
    content: str
    createTime: str
    error: GoogleCloudDialogflowV2ToolCallResultError
    rawContent: str
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolCallResultError(typing.TypedDict, total=False):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolConnectorTool(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDialogflowV2ToolConnectorToolAction]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolConnectorToolAction(typing.TypedDict, total=False):
    connectionActionId: str
    entityOperation: GoogleCloudDialogflowV2ToolConnectorToolActionEntityOperation
    inputFields: _list[str]
    outputFields: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2ToolConnectorToolActionEntityOperation(
    typing.TypedDict, total=False
):
    entityId: str
    operation: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ToolExtensionTool(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolFunctionTool(typing.TypedDict, total=False):
    inputSchema: dict[str, typing.Any]
    methodType: typing.Literal[
        "METHOD_TYPE_UNSPECIFIED", "GET", "POST", "PUT", "DELETE", "PATCH"
    ]
    outputSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2ToolOpenApiTool(typing.TypedDict, total=False):
    authentication: GoogleCloudDialogflowV2ToolAuthentication
    serviceDirectoryConfig: GoogleCloudDialogflowV2ToolServiceDirectoryConfig
    textSchema: str
    tlsConfig: GoogleCloudDialogflowV2ToolTLSConfig

@typing.type_check_only
class GoogleCloudDialogflowV2ToolServiceDirectoryConfig(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolTLSConfig(typing.TypedDict, total=False):
    caCerts: _list[GoogleCloudDialogflowV2ToolTLSConfigCACert]

@typing.type_check_only
class GoogleCloudDialogflowV2ToolTLSConfigCACert(typing.TypedDict, total=False):
    cert: str
    displayName: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolsetTool(typing.TypedDict, total=False):
    confirmationRequirement: typing.Literal[
        "CONFIRMATION_REQUIREMENT_UNSPECIFIED", "REQUIRED", "NOT_REQUIRED"
    ]
    operationId: str
    toolset: str

@typing.type_check_only
class GoogleCloudDialogflowV2TrainAgentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowV2UndeployConversationModelOperationMetadata(
    typing.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2UndeployConversationModelRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2ValidationError(typing.TypedDict, total=False):
    entries: _list[str]
    errorMessage: str
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "CRITICAL"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ValidationResult(typing.TypedDict, total=False):
    validationErrors: _list[GoogleCloudDialogflowV2ValidationError]

@typing.type_check_only
class GoogleCloudDialogflowV2Version(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    status: typing.Literal[
        "VERSION_STATUS_UNSPECIFIED", "IN_PROGRESS", "READY", "FAILED"
    ]
    versionNumber: int

@typing.type_check_only
class GoogleCloudDialogflowV2VoiceSelectionParams(typing.TypedDict, total=False):
    name: str
    ssmlGender: typing.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED",
        "SSML_VOICE_GENDER_MALE",
        "SSML_VOICE_GENDER_FEMALE",
        "SSML_VOICE_GENDER_NEUTRAL",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2WebhookRequest(typing.TypedDict, total=False):
    originalDetectIntentRequest: GoogleCloudDialogflowV2OriginalDetectIntentRequest
    queryResult: GoogleCloudDialogflowV2QueryResult
    responseId: str
    session: str

@typing.type_check_only
class GoogleCloudDialogflowV2WebhookResponse(typing.TypedDict, total=False):
    followupEventInput: GoogleCloudDialogflowV2EventInput
    fulfillmentMessages: _list[GoogleCloudDialogflowV2IntentMessage]
    fulfillmentText: str
    outputContexts: _list[GoogleCloudDialogflowV2Context]
    payload: dict[str, typing.Any]
    sessionEntityTypes: _list[GoogleCloudDialogflowV2SessionEntityType]
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingInstruction(
    typing.TypedDict, total=False
):
    agentAction: str
    condition: str
    displayDetails: str
    displayName: str
    duplicateCheckResult: (
        GoogleCloudDialogflowV2beta1AgentCoachingInstructionDuplicateCheckResult
    )
    systemAction: str
    triggeringEvent: typing.Literal[
        "TRIGGER_EVENT_UNSPECIFIED",
        "END_OF_UTTERANCE",
        "MANUAL_CALL",
        "CUSTOMER_MESSAGE",
        "AGENT_MESSAGE",
        "TOOL_CALL_COMPLETION",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingInstructionDuplicateCheckResult(
    typing.TypedDict, total=False
):
    duplicateSuggestions: _list[
        GoogleCloudDialogflowV2beta1AgentCoachingInstructionDuplicateCheckResultDuplicateSuggestion
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingInstructionDuplicateCheckResultDuplicateSuggestion(
    typing.TypedDict, total=False
):
    answerRecord: str
    similarityScore: float
    suggestionIndex: int

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingSuggestion(
    typing.TypedDict, total=False
):
    agentActionSuggestions: _list[
        GoogleCloudDialogflowV2beta1AgentCoachingSuggestionAgentActionSuggestion
    ]
    applicableInstructions: _list[GoogleCloudDialogflowV2beta1AgentCoachingInstruction]
    sampleResponses: _list[
        GoogleCloudDialogflowV2beta1AgentCoachingSuggestionSampleResponse
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingSuggestionAgentActionSuggestion(
    typing.TypedDict, total=False
):
    agentAction: str
    duplicateCheckResult: (
        GoogleCloudDialogflowV2beta1AgentCoachingSuggestionDuplicateCheckResult
    )
    sources: GoogleCloudDialogflowV2beta1AgentCoachingSuggestionSources

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingSuggestionDuplicateCheckResult(
    typing.TypedDict, total=False
):
    duplicateSuggestions: _list[
        GoogleCloudDialogflowV2beta1AgentCoachingSuggestionDuplicateCheckResultDuplicateSuggestion
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingSuggestionDuplicateCheckResultDuplicateSuggestion(
    typing.TypedDict, total=False
):
    answerRecord: str
    similarityScore: float
    sources: GoogleCloudDialogflowV2beta1AgentCoachingSuggestionSources
    suggestionIndex: int

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingSuggestionSampleResponse(
    typing.TypedDict, total=False
):
    duplicateCheckResult: (
        GoogleCloudDialogflowV2beta1AgentCoachingSuggestionDuplicateCheckResult
    )
    responseText: str
    sources: GoogleCloudDialogflowV2beta1AgentCoachingSuggestionSources

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AgentCoachingSuggestionSources(
    typing.TypedDict, total=False
):
    instructionIndexes: _list[int]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AnnotatedMessagePart(typing.TypedDict, total=False):
    entityType: str
    formattedValue: typing.Any
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ArticleAnswer(typing.TypedDict, total=False):
    answerRecord: str
    metadata: dict[str, typing.Any]
    snippets: _list[str]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponse(
    typing.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowV2beta1EntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponse(
    typing.TypedDict, total=False
):
    intents: _list[GoogleCloudDialogflowV2beta1Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadata(
    typing.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ARTICLE_SUGGESTION",
        "FAQ",
        "SMART_REPLY",
        "DIALOGFLOW_ASSIST",
        "CONVERSATION_SUMMARIZATION",
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1Context(typing.TypedDict, total=False):
    lifespanCount: int
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ConversationEvent(typing.TypedDict, total=False):
    conversation: str
    errorStatus: GoogleRpcStatus
    newMessagePayload: GoogleCloudDialogflowV2beta1Message
    newRecognitionResultPayload: GoogleCloudDialogflowV2beta1StreamingRecognitionResult
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "CONVERSATION_STARTED",
        "CONVERSATION_FINISHED",
        "HUMAN_INTERVENTION_NEEDED",
        "NEW_MESSAGE",
        "NEW_RECOGNITION_RESULT",
        "UNRECOVERABLE_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1DialogflowAssistAnswer(typing.TypedDict, total=False):
    answerRecord: str
    intentSuggestion: GoogleCloudDialogflowV2beta1IntentSuggestion
    queryResult: GoogleCloudDialogflowV2beta1QueryResult

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EncryptionSpec(typing.TypedDict, total=False):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EntityType(typing.TypedDict, total=False):
    autoExpansionMode: typing.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    kind: typing.Literal["KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EntityTypeEntity(typing.TypedDict, total=False):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EventInput(typing.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ExportAgentResponse(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ExportOperationMetadata(
    typing.TypedDict, total=False
):
    exportedGcsDestination: GoogleCloudDialogflowV2beta1GcsDestination

@typing.type_check_only
class GoogleCloudDialogflowV2beta1FaqAnswer(typing.TypedDict, total=False):
    answer: str
    answerRecord: str
    confidence: float
    metadata: dict[str, typing.Any]
    question: str
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1FreeFormSuggestion(typing.TypedDict, total=False):
    response: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GcsDestination(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GenerateSuggestionsResponse(
    typing.TypedDict, total=False
):
    generatorSuggestionAnswers: _list[
        GoogleCloudDialogflowV2beta1GenerateSuggestionsResponseGeneratorSuggestionAnswer
    ]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GenerateSuggestionsResponseGeneratorSuggestionAnswer(
    typing.TypedDict, total=False
):
    answerRecord: str
    generatorSuggestion: GoogleCloudDialogflowV2beta1GeneratorSuggestion
    sourceGenerator: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GeneratorSuggestion(typing.TypedDict, total=False):
    agentCoachingSuggestion: GoogleCloudDialogflowV2beta1AgentCoachingSuggestion
    freeFormSuggestion: GoogleCloudDialogflowV2beta1FreeFormSuggestion
    summarySuggestion: GoogleCloudDialogflowV2beta1SummarySuggestion
    toolCallInfo: _list[GoogleCloudDialogflowV2beta1GeneratorSuggestionToolCallInfo]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GeneratorSuggestionToolCallInfo(
    typing.TypedDict, total=False
):
    toolCall: GoogleCloudDialogflowV2beta1ToolCall
    toolCallResult: GoogleCloudDialogflowV2beta1ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowV2beta1HumanAgentAssistantEvent(
    typing.TypedDict, total=False
):
    conversation: str
    participant: str
    suggestionResults: _list[GoogleCloudDialogflowV2beta1SuggestionResult]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ImportDocumentsResponse(
    typing.TypedDict, total=False
):
    warnings: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IngestedContextReferenceDebugInfo(
    typing.TypedDict, total=False
):
    contextReferenceRetrieved: bool
    ingestedParametersDebugInfo: _list[
        GoogleCloudDialogflowV2beta1IngestedContextReferenceDebugInfoIngestedParameterDebugInfo
    ]
    projectNotAllowlisted: bool

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IngestedContextReferenceDebugInfoIngestedParameterDebugInfo(
    typing.TypedDict, total=False
):
    ingestionStatus: typing.Literal[
        "INGESTION_STATUS_UNSPECIFIED",
        "INGESTION_STATUS_SUCCEEDED",
        "INGESTION_STATUS_CONTEXT_NOT_AVAILABLE",
        "INGESTION_STATUS_PARSE_FAILED",
        "INGESTION_STATUS_INVALID_ENTRY",
        "INGESTION_STATUS_INVALID_FORMAT",
        "INGESTION_STATUS_LANGUAGE_MISMATCH",
    ]
    parameter: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1InitializeEncryptionSpecMetadata(
    typing.TypedDict, total=False
):
    request: GoogleCloudDialogflowV2beta1InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudDialogflowV2beta1InitializeEncryptionSpecRequest(
    typing.TypedDict, total=False
):
    encryptionSpec: GoogleCloudDialogflowV2beta1EncryptionSpec

@typing.type_check_only
class GoogleCloudDialogflowV2beta1Intent(typing.TypedDict, total=False):
    action: str
    defaultResponsePlatforms: _list[
        typing.Literal[
            "PLATFORM_UNSPECIFIED",
            "FACEBOOK",
            "SLACK",
            "TELEGRAM",
            "KIK",
            "SKYPE",
            "LINE",
            "VIBER",
            "ACTIONS_ON_GOOGLE",
            "TELEPHONY",
            "GOOGLE_HANGOUTS",
        ]
    ]
    displayName: str
    endInteraction: bool
    events: _list[str]
    followupIntentInfo: _list[GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo]
    inputContextNames: _list[str]
    isFallback: bool
    liveAgentHandoff: bool
    messages: _list[GoogleCloudDialogflowV2beta1IntentMessage]
    mlDisabled: bool
    mlEnabled: bool
    name: str
    outputContexts: _list[GoogleCloudDialogflowV2beta1Context]
    parameters: _list[GoogleCloudDialogflowV2beta1IntentParameter]
    parentFollowupIntentName: str
    priority: int
    resetContexts: bool
    rootFollowupIntentName: str
    trainingPhrases: _list[GoogleCloudDialogflowV2beta1IntentTrainingPhrase]
    webhookState: typing.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo(
    typing.TypedDict, total=False
):
    followupIntentName: str
    parentFollowupIntentName: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessage(typing.TypedDict, total=False):
    basicCard: GoogleCloudDialogflowV2beta1IntentMessageBasicCard
    browseCarouselCard: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard
    card: GoogleCloudDialogflowV2beta1IntentMessageCard
    carouselSelect: GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    linkOutSuggestion: GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion
    listSelect: GoogleCloudDialogflowV2beta1IntentMessageListSelect
    mediaContent: GoogleCloudDialogflowV2beta1IntentMessageMediaContent
    payload: dict[str, typing.Any]
    platform: typing.Literal[
        "PLATFORM_UNSPECIFIED",
        "FACEBOOK",
        "SLACK",
        "TELEGRAM",
        "KIK",
        "SKYPE",
        "LINE",
        "VIBER",
        "ACTIONS_ON_GOOGLE",
        "TELEPHONY",
        "GOOGLE_HANGOUTS",
    ]
    quickReplies: GoogleCloudDialogflowV2beta1IntentMessageQuickReplies
    rbmCarouselRichCard: GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard
    rbmStandaloneRichCard: GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard
    rbmText: GoogleCloudDialogflowV2beta1IntentMessageRbmText
    simpleResponses: GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses
    suggestions: GoogleCloudDialogflowV2beta1IntentMessageSuggestions
    tableCard: GoogleCloudDialogflowV2beta1IntentMessageTableCard
    telephonyPlayAudio: GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio
    telephonySynthesizeSpeech: (
        GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech
    )
    telephonyTransferCall: (
        GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall
    )
    text: GoogleCloudDialogflowV2beta1IntentMessageText

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBasicCard(typing.TypedDict, total=False):
    buttons: _list[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    formattedText: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton(
    typing.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard(
    typing.TypedDict, total=False
):
    imageDisplayOptions: typing.Literal[
        "IMAGE_DISPLAY_OPTIONS_UNSPECIFIED",
        "GRAY",
        "WHITE",
        "CROPPED",
        "BLURRED_BACKGROUND",
    ]
    items: _list[
        GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing.TypedDict, total=False
):
    description: str
    footer: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing.TypedDict, total=False
):
    url: str
    urlTypeHint: typing.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCard(typing.TypedDict, total=False):
    buttons: _list[GoogleCloudDialogflowV2beta1IntentMessageCardButton]
    imageUri: str
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCardButton(
    typing.TypedDict, total=False
):
    postback: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect(
    typing.TypedDict, total=False
):
    items: _list[GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem(
    typing.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageColumnProperties(
    typing.TypedDict, total=False
):
    header: str
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageImage(typing.TypedDict, total=False):
    accessibilityText: str
    imageUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion(
    typing.TypedDict, total=False
):
    destinationName: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageListSelect(
    typing.TypedDict, total=False
):
    items: _list[GoogleCloudDialogflowV2beta1IntentMessageListSelectItem]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageListSelectItem(
    typing.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageMediaContent(
    typing.TypedDict, total=False
):
    mediaObjects: _list[
        GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject
    ]
    mediaType: typing.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject(
    typing.TypedDict, total=False
):
    contentUrl: str
    description: str
    icon: GoogleCloudDialogflowV2beta1IntentMessageImage
    largeImage: GoogleCloudDialogflowV2beta1IntentMessageImage
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageQuickReplies(
    typing.TypedDict, total=False
):
    quickReplies: _list[str]
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent(
    typing.TypedDict, total=False
):
    description: str
    media: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia
    suggestions: _list[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia(
    typing.TypedDict, total=False
):
    fileUri: str
    height: typing.Literal["HEIGHT_UNSPECIFIED", "SHORT", "MEDIUM", "TALL"]
    thumbnailUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard(
    typing.TypedDict, total=False
):
    cardContents: _list[GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent]
    cardWidth: typing.Literal["CARD_WIDTH_UNSPECIFIED", "SMALL", "MEDIUM"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard(
    typing.TypedDict, total=False
):
    cardContent: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent
    cardOrientation: typing.Literal[
        "CARD_ORIENTATION_UNSPECIFIED", "HORIZONTAL", "VERTICAL"
    ]
    thumbnailImageAlignment: typing.Literal[
        "THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction(
    typing.TypedDict, total=False
):
    dial: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial
    openUrl: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri
    postbackData: str
    shareLocation: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial(
    typing.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply(
    typing.TypedDict, total=False
):
    postbackData: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion(
    typing.TypedDict, total=False
):
    action: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction
    reply: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmText(typing.TypedDict, total=False):
    rbmSuggestion: _list[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo(
    typing.TypedDict, total=False
):
    key: str
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse(
    typing.TypedDict, total=False
):
    displayText: str
    ssml: str
    textToSpeech: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses(
    typing.TypedDict, total=False
):
    simpleResponses: _list[GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSuggestion(
    typing.TypedDict, total=False
):
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSuggestions(
    typing.TypedDict, total=False
):
    suggestions: _list[GoogleCloudDialogflowV2beta1IntentMessageSuggestion]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTableCard(typing.TypedDict, total=False):
    buttons: _list[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    columnProperties: _list[GoogleCloudDialogflowV2beta1IntentMessageColumnProperties]
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    rows: _list[GoogleCloudDialogflowV2beta1IntentMessageTableCardRow]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTableCardCell(
    typing.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTableCardRow(
    typing.TypedDict, total=False
):
    cells: _list[GoogleCloudDialogflowV2beta1IntentMessageTableCardCell]
    dividerAfter: bool

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio(
    typing.TypedDict, total=False
):
    audioUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech(
    typing.TypedDict, total=False
):
    ssml: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall(
    typing.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageText(typing.TypedDict, total=False):
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentParameter(typing.TypedDict, total=False):
    defaultValue: str
    displayName: str
    entityTypeDisplayName: str
    isList: bool
    mandatory: bool
    name: str
    prompts: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentSuggestion(typing.TypedDict, total=False):
    description: str
    displayName: str
    intentV2: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentTrainingPhrase(typing.TypedDict, total=False):
    name: str
    parts: _list[GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart]
    timesAddedCount: int
    type: typing.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart(
    typing.TypedDict, total=False
):
    alias: str
    entityType: str
    text: str
    userDefined: bool

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAnswers(typing.TypedDict, total=False):
    answers: _list[GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer(typing.TypedDict, total=False):
    answer: str
    faqQuestion: str
    matchConfidence: float
    matchConfidenceLevel: typing.Literal[
        "MATCH_CONFIDENCE_LEVEL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswer(typing.TypedDict, total=False):
    answerRecord: str
    knowledgeAssistDebugInfo: GoogleCloudDialogflowV2beta1KnowledgeAssistDebugInfo
    suggestedQuery: GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerSuggestedQuery
    suggestedQueryAnswer: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswer
    )

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerAdditionalSuggestedQueryResult(
    typing.TypedDict, total=False
):
    answerRecord: str
    suggestedQuery: GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerSuggestedQuery

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswer(
    typing.TypedDict, total=False
):
    answerText: str
    eventSource: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerEventSource
    )
    faqSource: GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerFaqSource
    generativeSource: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )
    playbookSource: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerEventSource(
    typing.TypedDict, total=False
):
    event: str
    snippets: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerFaqSource(
    typing.TypedDict, total=False
):
    question: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource(
    typing.TypedDict, total=False
):
    snippets: _list[
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerSuggestedQuery(
    typing.TypedDict, total=False
):
    queryText: str
    searchContexts: _list[
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerSuggestedQuerySearchContext
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerSuggestedQuerySearchContext(
    typing.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistDebugInfo(
    typing.TypedDict, total=False
):
    cesDebugInfo: dict[str, typing.Any]
    datastoreResponseReason: typing.Literal[
        "DATASTORE_RESPONSE_REASON_UNSPECIFIED",
        "NONE",
        "SEARCH_OUT_OF_QUOTA",
        "SEARCH_EMPTY_RESULTS",
        "ANSWER_GENERATION_GEN_AI_DISABLED",
        "ANSWER_GENERATION_OUT_OF_QUOTA",
        "ANSWER_GENERATION_ERROR",
        "ANSWER_GENERATION_NOT_ENOUGH_INFO",
        "ANSWER_GENERATION_RAI_FAILED",
        "ANSWER_GENERATION_NOT_GROUNDED",
    ]
    ingestedContextReferenceDebugInfo: (
        GoogleCloudDialogflowV2beta1IngestedContextReferenceDebugInfo
    )
    knowledgeAssistBehavior: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistDebugInfoKnowledgeAssistBehavior
    )
    queryCategorizationFailureReason: typing.Literal[
        "QUERY_CATEGORIZATION_FAILURE_REASON_UNSPECIFIED",
        "QUERY_CATEGORIZATION_INVALID_CONFIG",
        "QUERY_CATEGORIZATION_RESULT_NOT_FOUND",
        "QUERY_CATEGORIZATION_FAILED",
    ]
    queryGenerationDebugInfo: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistDebugInfoQueryGenerationDebugInfo
    )
    queryGenerationFailureReason: typing.Literal[
        "QUERY_GENERATION_FAILURE_REASON_UNSPECIFIED",
        "QUERY_GENERATION_OUT_OF_QUOTA",
        "QUERY_GENERATION_FAILED",
        "QUERY_GENERATION_NO_QUERY_GENERATED",
        "QUERY_GENERATION_RAI_FAILED",
        "NOT_IN_ALLOWLIST",
        "QUERY_GENERATION_QUERY_REDACTED",
        "QUERY_GENERATION_LLM_RESPONSE_PARSE_FAILED",
        "QUERY_GENERATION_EMPTY_CONVERSATION",
        "QUERY_GENERATION_EMPTY_LAST_MESSAGE",
        "QUERY_GENERATION_TRIGGERING_EVENT_CONDITION_NOT_MET",
    ]
    serviceLatency: GoogleCloudDialogflowV2beta1ServiceLatency

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistDebugInfoKnowledgeAssistBehavior(
    typing.TypedDict, total=False
):
    answerGenerationRewriterOn: bool
    appendedSearchContextCount: int
    conversationTranscriptHasMixedLanguages: bool
    disableSyncDelivery: bool
    endUserMetadataIncluded: bool
    invalidItemsQuerySuggestionSkipped: bool
    multipleQueriesGenerated: bool
    previousQueriesIncluded: bool
    primaryQueryRedactedAndReplaced: bool
    queryContainedSearchContext: bool
    queryGenerationAgentLanguageMismatch: bool
    queryGenerationEndUserLanguageMismatch: bool
    returnQueryOnly: bool
    thirdPartyConnectorAllowed: bool
    useCustomSafetyFilterLevel: bool
    usePubsubDelivery: bool
    useTranslatedMessage: bool

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistDebugInfoQueryGenerationDebugInfo(
    typing.TypedDict, total=False
):
    candidatesTokenCount: int
    promptTokenCount: int
    similarityToLastQuery: float
    similarityToLastQueryThreshold: float
    thinkingBudgetTokens: int
    thinkingLevel: str
    totalTokenCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeOperationMetadata(
    typing.TypedDict, total=False
):
    doneTime: str
    exportOperationMetadata: GoogleCloudDialogflowV2beta1ExportOperationMetadata
    knowledgeBase: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1Message(typing.TypedDict, total=False):
    content: str
    createTime: str
    languageCode: str
    messageAnnotation: GoogleCloudDialogflowV2beta1MessageAnnotation
    name: str
    participant: str
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    responseMessages: _list[GoogleCloudDialogflowV2beta1ResponseMessage]
    sendTime: str
    sentimentAnalysis: GoogleCloudDialogflowV2beta1SentimentAnalysisResult

@typing.type_check_only
class GoogleCloudDialogflowV2beta1MessageAnnotation(typing.TypedDict, total=False):
    containEntities: bool
    parts: _list[GoogleCloudDialogflowV2beta1AnnotatedMessagePart]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest(
    typing.TypedDict, total=False
):
    payload: dict[str, typing.Any]
    source: str
    version: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1QueryResult(typing.TypedDict, total=False):
    action: str
    allRequiredParamsPresent: bool
    cancelsSlotFilling: bool
    diagnosticInfo: dict[str, typing.Any]
    fulfillmentMessages: _list[GoogleCloudDialogflowV2beta1IntentMessage]
    fulfillmentText: str
    intent: GoogleCloudDialogflowV2beta1Intent
    intentDetectionConfidence: float
    knowledgeAnswers: GoogleCloudDialogflowV2beta1KnowledgeAnswers
    languageCode: str
    outputContexts: _list[GoogleCloudDialogflowV2beta1Context]
    parameters: dict[str, typing.Any]
    queryText: str
    sentimentAnalysisResult: GoogleCloudDialogflowV2beta1SentimentAnalysisResult
    speechRecognitionConfidence: float
    webhookPayload: dict[str, typing.Any]
    webhookSource: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessage(typing.TypedDict, total=False):
    endInteraction: GoogleCloudDialogflowV2beta1ResponseMessageEndInteraction
    liveAgentHandoff: GoogleCloudDialogflowV2beta1ResponseMessageLiveAgentHandoff
    mixedAudio: GoogleCloudDialogflowV2beta1ResponseMessageMixedAudio
    payload: dict[str, typing.Any]
    telephonyTransferCall: (
        GoogleCloudDialogflowV2beta1ResponseMessageTelephonyTransferCall
    )
    text: GoogleCloudDialogflowV2beta1ResponseMessageText

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageEndInteraction(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageLiveAgentHandoff(
    typing.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageMixedAudio(
    typing.TypedDict, total=False
):
    segments: _list[GoogleCloudDialogflowV2beta1ResponseMessageMixedAudioSegment]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageMixedAudioSegment(
    typing.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audio: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageTelephonyTransferCall(
    typing.TypedDict, total=False
):
    phoneNumber: str
    sipUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageText(typing.TypedDict, total=False):
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1Sentiment(typing.TypedDict, total=False):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SentimentAnalysisResult(
    typing.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2beta1Sentiment

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ServiceLatency(typing.TypedDict, total=False):
    internalServiceLatencies: _list[
        GoogleCloudDialogflowV2beta1ServiceLatencyInternalServiceLatency
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ServiceLatencyInternalServiceLatency(
    typing.TypedDict, total=False
):
    completeTime: str
    latencyMs: float
    startTime: str
    step: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SessionEntityType(typing.TypedDict, total=False):
    entities: _list[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    entityOverrideMode: typing.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadata(
    typing.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ARTICLE_SUGGESTION",
        "FAQ",
        "SMART_REPLY",
        "DIALOGFLOW_ASSIST",
        "CONVERSATION_SUMMARIZATION",
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SmartReplyAnswer(typing.TypedDict, total=False):
    answerRecord: str
    confidence: float
    reply: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SpeechWordInfo(typing.TypedDict, total=False):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1StreamingRecognitionResult(
    typing.TypedDict, total=False
):
    confidence: float
    dtmfDigits: GoogleCloudDialogflowV2beta1TelephonyDtmfEvents
    isFinal: bool
    languageCode: str
    messageType: typing.Literal[
        "MESSAGE_TYPE_UNSPECIFIED",
        "TRANSCRIPT",
        "END_OF_SINGLE_UTTERANCE",
        "DTMF_DIGITS",
        "PARTIAL_DTMF_DIGITS",
        "SPEECH_ACTIVITY_BEGIN",
        "SPEECH_ACTIVITY_END",
    ]
    speechEndOffset: str
    speechWordInfo: _list[GoogleCloudDialogflowV2beta1SpeechWordInfo]
    stability: float
    transcript: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestArticlesResponse(
    typing.TypedDict, total=False
):
    articleAnswers: _list[GoogleCloudDialogflowV2beta1ArticleAnswer]
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponse(
    typing.TypedDict, total=False
):
    contextSize: int
    dialogflowAssistAnswers: _list[GoogleCloudDialogflowV2beta1DialogflowAssistAnswer]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponse(
    typing.TypedDict, total=False
):
    contextSize: int
    faqAnswers: _list[GoogleCloudDialogflowV2beta1FaqAnswer]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestKnowledgeAssistResponse(
    typing.TypedDict, total=False
):
    additionalSuggestedQueryResults: _list[
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerAdditionalSuggestedQueryResult
    ]
    contextSize: int
    knowledgeAssistAnswer: GoogleCloudDialogflowV2beta1KnowledgeAssistAnswer
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponse(
    typing.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    smartReplyAnswers: _list[GoogleCloudDialogflowV2beta1SmartReplyAnswer]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestionResult(typing.TypedDict, total=False):
    error: GoogleRpcStatus
    generateSuggestionsResponse: GoogleCloudDialogflowV2beta1GenerateSuggestionsResponse
    suggestArticlesResponse: GoogleCloudDialogflowV2beta1SuggestArticlesResponse
    suggestDialogflowAssistsResponse: (
        GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponse
    )
    suggestEntityExtractionResponse: (
        GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponse
    )
    suggestFaqAnswersResponse: GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponse
    suggestKnowledgeAssistResponse: (
        GoogleCloudDialogflowV2beta1SuggestKnowledgeAssistResponse
    )
    suggestSmartRepliesResponse: GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponse

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SummarySuggestion(typing.TypedDict, total=False):
    summarySections: _list[GoogleCloudDialogflowV2beta1SummarySuggestionSummarySection]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SummarySuggestionSummarySection(
    typing.TypedDict, total=False
):
    section: str
    summary: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1TelephonyDtmfEvents(typing.TypedDict, total=False):
    dtmfEvents: _list[
        typing.Literal[
            "TELEPHONY_DTMF_UNSPECIFIED",
            "DTMF_ONE",
            "DTMF_TWO",
            "DTMF_THREE",
            "DTMF_FOUR",
            "DTMF_FIVE",
            "DTMF_SIX",
            "DTMF_SEVEN",
            "DTMF_EIGHT",
            "DTMF_NINE",
            "DTMF_ZERO",
            "DTMF_A",
            "DTMF_B",
            "DTMF_C",
            "DTMF_D",
            "DTMF_STAR",
            "DTMF_POUND",
        ]
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ToolCall(typing.TypedDict, total=False):
    action: str
    answerRecord: str
    cesApp: str
    cesTool: str
    cesToolset: str
    createTime: str
    inputParameters: dict[str, typing.Any]
    state: typing.Literal["STATE_UNSPECIFIED", "TRIGGERED", "NEEDS_CONFIRMATION"]
    tool: str
    toolDisplayDetails: str
    toolDisplayName: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ToolCallResult(typing.TypedDict, total=False):
    action: str
    answerRecord: str
    cesApp: str
    cesTool: str
    cesToolset: str
    content: str
    createTime: str
    error: GoogleCloudDialogflowV2beta1ToolCallResultError
    rawContent: str
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ToolCallResultError(typing.TypedDict, total=False):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1WebhookRequest(typing.TypedDict, total=False):
    alternativeQueryResults: _list[GoogleCloudDialogflowV2beta1QueryResult]
    originalDetectIntentRequest: GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest
    queryResult: GoogleCloudDialogflowV2beta1QueryResult
    responseId: str
    session: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1WebhookResponse(typing.TypedDict, total=False):
    endInteraction: bool
    followupEventInput: GoogleCloudDialogflowV2beta1EventInput
    fulfillmentMessages: _list[GoogleCloudDialogflowV2beta1IntentMessage]
    fulfillmentText: str
    liveAgentHandoff: bool
    outputContexts: _list[GoogleCloudDialogflowV2beta1Context]
    payload: dict[str, typing.Any]
    sessionEntityTypes: _list[GoogleCloudDialogflowV2beta1SessionEntityType]
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV3alpha1ConversationSignals(typing.TypedDict, total=False):
    turnSignals: GoogleCloudDialogflowV3alpha1TurnSignals

@typing.type_check_only
class GoogleCloudDialogflowV3alpha1TurnSignals(typing.TypedDict, total=False):
    agentEscalated: bool
    dtmfUsed: bool
    failureReasons: _list[
        typing.Literal["FAILURE_REASON_UNSPECIFIED", "FAILED_INTENT", "FAILED_WEBHOOK"]
    ]
    noMatch: bool
    noUserInput: bool
    reachedEndPage: bool
    sentimentMagnitude: float
    sentimentScore: float
    triggeredAbandonmentEvent: bool
    userEscalated: bool
    webhookStatuses: _list[str]

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
class GoogleTypeLatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float
