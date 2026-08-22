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
class GoogleCloudDialogflowCxV3beta1Action(typing.TypedDict, total=False):
    agentUtterance: GoogleCloudDialogflowCxV3beta1AgentUtterance
    completeTime: str
    displayName: str
    event: GoogleCloudDialogflowCxV3beta1Event
    flowInvocation: GoogleCloudDialogflowCxV3beta1FlowInvocation
    flowStateUpdate: GoogleCloudDialogflowCxV3beta1ActionFlowStateUpdate
    flowTransition: GoogleCloudDialogflowCxV3beta1FlowTransition
    intentMatch: GoogleCloudDialogflowCxV3beta1ActionIntentMatch
    llmCall: GoogleCloudDialogflowCxV3beta1LlmCall
    playbookInvocation: GoogleCloudDialogflowCxV3beta1PlaybookInvocation
    playbookTransition: GoogleCloudDialogflowCxV3beta1PlaybookTransition
    startTime: str
    status: GoogleCloudDialogflowCxV3beta1Status
    stt: GoogleCloudDialogflowCxV3beta1ActionSTT
    subExecutionSteps: _list[GoogleCloudDialogflowCxV3beta1Span]
    toolUse: GoogleCloudDialogflowCxV3beta1ToolUse
    tts: GoogleCloudDialogflowCxV3beta1ActionTTS
    userUtterance: GoogleCloudDialogflowCxV3beta1UserUtterance

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ActionFlowStateUpdate(
    typing.TypedDict, total=False
):
    destination: str
    eventType: str
    functionCall: GoogleCloudDialogflowCxV3beta1ActionFlowStateUpdateFunctionCall
    pageState: GoogleCloudDialogflowCxV3beta1ActionFlowStateUpdatePageState
    updatedParameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ActionFlowStateUpdateFunctionCall(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ActionFlowStateUpdatePageState(
    typing.TypedDict, total=False
):
    displayName: str
    page: str
    status: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ActionIntentMatch(typing.TypedDict, total=False):
    matchedIntents: _list[GoogleCloudDialogflowCxV3beta1ActionIntentMatchMatchedIntent]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ActionIntentMatchMatchedIntent(
    typing.TypedDict, total=False
):
    displayName: str
    generativeFallback: dict[str, typing.Any]
    intentId: str
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ActionSTT(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ActionTTS(typing.TypedDict, total=False): ...

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
class GoogleCloudDialogflowCxV3beta1Agent(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    answerFeedbackSettings: GoogleCloudDialogflowCxV3beta1AgentAnswerFeedbackSettings
    avatarUri: str
    bigqueryExportSettings: GoogleCloudDialogflowCxV3beta1BigQueryExportSettings
    clientCertificateSettings: (
        GoogleCloudDialogflowCxV3beta1AgentClientCertificateSettings
    )
    defaultLanguageCode: str
    description: str
    displayName: str
    enableMultiLanguageTraining: bool
    enableSpellCorrection: bool
    enableStackdriverLogging: bool
    genAppBuilderSettings: GoogleCloudDialogflowCxV3beta1AgentGenAppBuilderSettings
    gitIntegrationSettings: GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettings
    locked: bool
    name: str
    personalizationSettings: GoogleCloudDialogflowCxV3beta1AgentPersonalizationSettings
    satisfiesPzi: bool
    satisfiesPzs: bool
    securitySettings: str
    speechToTextSettings: GoogleCloudDialogflowCxV3beta1SpeechToTextSettings
    startFlow: str
    startPlaybook: str
    supportedLanguageCodes: _list[str]
    textToSpeechSettings: GoogleCloudDialogflowCxV3beta1TextToSpeechSettings
    timeZone: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentAnswerFeedbackSettings(
    typing.TypedDict, total=False
):
    enableAnswerFeedback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentClientCertificateSettings(
    typing.TypedDict, total=False
):
    passphrase: str
    privateKey: str
    sslCertificate: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentGenAppBuilderSettings(
    typing.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettings(
    typing.TypedDict, total=False
):
    gitConnectionSettings: (
        GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGitConnectionSettings
    )
    githubSettings: (
        GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGithubSettings
    )

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGitConnectionSettings(
    typing.TypedDict, total=False
):
    accessTokenSecret: str
    branches: _list[str]
    displayName: str
    repositoryUri: str
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGithubSettings(
    typing.TypedDict, total=False
):
    accessToken: str
    branches: _list[str]
    displayName: str
    repositoryUri: str
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentPersonalizationSettings(
    typing.TypedDict, total=False
):
    defaultEndUserMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentUtterance(typing.TypedDict, total=False):
    requireGeneration: bool
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentValidationResult(
    typing.TypedDict, total=False
):
    flowValidationResults: _list[GoogleCloudDialogflowCxV3beta1FlowValidationResult]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AnswerFeedback(typing.TypedDict, total=False):
    customRating: str
    rating: typing.Literal["RATING_UNSPECIFIED", "THUMBS_UP", "THUMBS_DOWN"]
    ratingReason: GoogleCloudDialogflowCxV3beta1AnswerFeedbackRatingReason

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AnswerFeedbackRatingReason(
    typing.TypedDict, total=False
):
    feedback: str
    reasonLabels: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AudioInput(typing.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowCxV3beta1InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BargeInConfig(typing.TypedDict, total=False):
    noBargeInDuration: str
    totalDuration: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchDeleteTestCasesRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadata(
    typing.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesRequest(
    typing.TypedDict, total=False
):
    environment: str
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleCloudDialogflowCxV3beta1TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BigQueryExportSettings(
    typing.TypedDict, total=False
):
    bigqueryTable: str
    enabled: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpec(typing.TypedDict, total=False):
    conditionBoostSpecs: _list[
        GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    boostControlSpec: (
        GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpec
    )
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecs(typing.TypedDict, total=False):
    dataStores: _list[str]
    spec: _list[GoogleCloudDialogflowCxV3beta1BoostSpec]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CalculateCoverageResponse(
    typing.TypedDict, total=False
):
    agent: str
    intentCoverage: GoogleCloudDialogflowCxV3beta1IntentCoverage
    routeGroupCoverage: GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverage
    transitionCoverage: GoogleCloudDialogflowCxV3beta1TransitionCoverage

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Changelog(typing.TypedDict, total=False):
    action: str
    createTime: str
    displayName: str
    languageCode: str
    name: str
    resource: str
    type: str
    userEmail: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CodeBlock(typing.TypedDict, total=False):
    code: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CompareVersionsRequest(
    typing.TypedDict, total=False
):
    languageCode: str
    targetVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CompareVersionsResponse(
    typing.TypedDict, total=False
):
    baseVersionContentJson: str
    compareTime: str
    targetVersionContentJson: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ContinuousTestResult(typing.TypedDict, total=False):
    name: str
    result: typing.Literal["AGGREGATED_TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    runTime: str
    testCaseResults: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Conversation(typing.TypedDict, total=False):
    duration: str
    environment: GoogleCloudDialogflowCxV3beta1Environment
    flowVersions: dict[str, typing.Any]
    flows: _list[GoogleCloudDialogflowCxV3beta1Flow]
    intents: _list[GoogleCloudDialogflowCxV3beta1Intent]
    interactions: _list[GoogleCloudDialogflowCxV3beta1ConversationInteraction]
    languageCode: str
    metrics: GoogleCloudDialogflowCxV3beta1ConversationMetrics
    name: str
    pages: _list[GoogleCloudDialogflowCxV3beta1Page]
    startTime: str
    type: typing.Literal["TYPE_UNSPECIFIED", "AUDIO", "TEXT", "UNDETERMINED"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationInteraction(
    typing.TypedDict, total=False
):
    answerFeedback: GoogleCloudDialogflowCxV3beta1AnswerFeedback
    createTime: str
    missingTransition: (
        GoogleCloudDialogflowCxV3beta1ConversationInteractionMissingTransition
    )
    partialResponses: _list[GoogleCloudDialogflowCxV3beta1DetectIntentResponse]
    request: GoogleCloudDialogflowCxV3beta1DetectIntentRequest
    requestUtterances: str
    response: GoogleCloudDialogflowCxV3beta1DetectIntentResponse
    responseUtterances: str
    stepMetrics: _list[GoogleCloudDialogflowCxV3beta1ConversationInteractionStepMetrics]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationInteractionMissingTransition(
    typing.TypedDict, total=False
):
    intentDisplayName: str
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationInteractionStepMetrics(
    typing.TypedDict, total=False
):
    latency: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationMetrics(typing.TypedDict, total=False):
    averageMatchConfidence: float
    hasEndInteraction: bool
    hasLiveAgentHandoff: bool
    inputAudioDuration: str
    interactionCount: int
    matchTypeCount: GoogleCloudDialogflowCxV3beta1ConversationMetricsMatchTypeCount
    maxWebhookLatency: str
    outputAudioDuration: str
    queryInputCount: GoogleCloudDialogflowCxV3beta1ConversationMetricsQueryInputCount

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationMetricsMatchTypeCount(
    typing.TypedDict, total=False
):
    directIntentCount: int
    eventCount: int
    intentCount: int
    noInputCount: int
    noMatchCount: int
    parameterFillingCount: int
    unspecifiedCount: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationMetricsQueryInputCount(
    typing.TypedDict, total=False
):
    audioCount: int
    dtmfCount: int
    eventCount: int
    intentCount: int
    textCount: int

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
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignals(
    typing.TypedDict, total=False
):
    answer: str
    answerGenerationModelCallSignals: GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsAnswerGenerationModelCallSignals
    answerParts: _list[
        GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsAnswerPart
    ]
    citedSnippets: _list[
        GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsCitedSnippet
    ]
    groundingSignals: (
        GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsGroundingSignals
    )
    rewriterModelCallSignals: (
        GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsRewriterModelCallSignals
    )
    rewrittenQuery: str
    safetySignals: GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSafetySignals
    searchSnippets: _list[
        GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSearchSnippet
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsAnswerGenerationModelCallSignals(
    typing.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsAnswerPart(
    typing.TypedDict, total=False
):
    supportingIndices: _list[int]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsCitedSnippet(
    typing.TypedDict, total=False
):
    searchSnippet: GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSearchSnippet
    snippetIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsGroundingSignals(
    typing.TypedDict, total=False
):
    decision: typing.Literal[
        "GROUNDING_DECISION_UNSPECIFIED",
        "ACCEPTED_BY_GROUNDING",
        "REJECTED_BY_GROUNDING",
    ]
    score: typing.Literal[
        "GROUNDING_SCORE_BUCKET_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsRewriterModelCallSignals(
    typing.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSafetySignals(
    typing.TypedDict, total=False
):
    bannedPhraseMatch: typing.Literal[
        "BANNED_PHRASE_MATCH_UNSPECIFIED",
        "BANNED_PHRASE_MATCH_NONE",
        "BANNED_PHRASE_MATCH_QUERY",
        "BANNED_PHRASE_MATCH_RESPONSE",
    ]
    decision: typing.Literal[
        "SAFETY_DECISION_UNSPECIFIED",
        "ACCEPTED_BY_SAFETY_CHECK",
        "REJECTED_BY_SAFETY_CHECK",
    ]
    matchedBannedPhrase: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSearchSnippet(
    typing.TypedDict, total=False
):
    documentTitle: str
    documentUri: str
    metadata: dict[str, typing.Any]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowMetadata(typing.TypedDict, total=False):
    testErrors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowRequest(typing.TypedDict, total=False):
    flowVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowResponse(typing.TypedDict, total=False):
    deployment: str
    environment: GoogleCloudDialogflowCxV3beta1Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Deployment(typing.TypedDict, total=False):
    endTime: str
    flowVersion: str
    name: str
    result: GoogleCloudDialogflowCxV3beta1DeploymentResult
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeploymentResult(typing.TypedDict, total=False):
    deploymentTestResults: _list[str]
    experiment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DetectIntentRequest(typing.TypedDict, total=False):
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    queryInput: GoogleCloudDialogflowCxV3beta1QueryInput
    queryParams: GoogleCloudDialogflowCxV3beta1QueryParameters
    responseView: typing.Literal[
        "DETECT_INTENT_RESPONSE_VIEW_UNSPECIFIED",
        "DETECT_INTENT_RESPONSE_VIEW_FULL",
        "DETECT_INTENT_RESPONSE_VIEW_BASIC",
        "DETECT_INTENT_RESPONSE_VIEW_DEFAULT",
    ]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DetectIntentResponse(typing.TypedDict, total=False):
    allowCancellation: bool
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3beta1QueryResult
    responseId: str
    responseType: typing.Literal["RESPONSE_TYPE_UNSPECIFIED", "PARTIAL", "FINAL"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DtmfInput(typing.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityType(typing.TypedDict, total=False):
    autoExpansionMode: typing.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowCxV3beta1EntityTypeEntity]
    excludedPhrases: _list[GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase]
    kind: typing.Literal["KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"]
    name: str
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityTypeEntity(typing.TypedDict, total=False):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase(
    typing.TypedDict, total=False
):
    value: str

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
class GoogleCloudDialogflowCxV3beta1Event(typing.TypedDict, total=False):
    event: str
    text: str

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
class GoogleCloudDialogflowCxV3beta1Example(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDialogflowCxV3beta1Action]
    conversationState: typing.Literal[
        "OUTPUT_STATE_UNSPECIFIED",
        "OUTPUT_STATE_OK",
        "OUTPUT_STATE_CANCELLED",
        "OUTPUT_STATE_FAILED",
        "OUTPUT_STATE_ESCALATED",
        "OUTPUT_STATE_PENDING",
    ]
    createTime: str
    description: str
    displayName: str
    languageCode: str
    name: str
    playbookInput: GoogleCloudDialogflowCxV3beta1PlaybookInput
    playbookOutput: GoogleCloudDialogflowCxV3beta1PlaybookOutput
    tokenCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExceptionDetail(typing.TypedDict, total=False):
    errorMessage: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Experiment(typing.TypedDict, total=False):
    createTime: str
    definition: GoogleCloudDialogflowCxV3beta1ExperimentDefinition
    description: str
    displayName: str
    endTime: str
    experimentLength: str
    lastUpdateTime: str
    name: str
    result: GoogleCloudDialogflowCxV3beta1ExperimentResult
    rolloutConfig: GoogleCloudDialogflowCxV3beta1RolloutConfig
    rolloutFailureReason: str
    rolloutState: GoogleCloudDialogflowCxV3beta1RolloutState
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DRAFT", "RUNNING", "DONE", "ROLLOUT_FAILED"
    ]
    variantsHistory: _list[GoogleCloudDialogflowCxV3beta1VariantsHistory]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentDefinition(typing.TypedDict, total=False):
    condition: str
    versionVariants: GoogleCloudDialogflowCxV3beta1VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResult(typing.TypedDict, total=False):
    lastUpdateTime: str
    versionMetrics: _list[GoogleCloudDialogflowCxV3beta1ExperimentResultVersionMetrics]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval(
    typing.TypedDict, total=False
):
    confidenceLevel: float
    lowerBound: float
    ratio: float
    upperBound: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResultMetric(
    typing.TypedDict, total=False
):
    confidenceInterval: GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval
    count: float
    countType: typing.Literal[
        "COUNT_TYPE_UNSPECIFIED",
        "TOTAL_NO_MATCH_COUNT",
        "TOTAL_TURN_COUNT",
        "AVERAGE_TURN_COUNT",
    ]
    ratio: float
    type: typing.Literal[
        "METRIC_UNSPECIFIED",
        "CONTAINED_SESSION_NO_CALLBACK_RATE",
        "LIVE_AGENT_HANDOFF_RATE",
        "CALLBACK_SESSION_RATE",
        "ABANDONED_SESSION_RATE",
        "SESSION_END_RATE",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResultVersionMetrics(
    typing.TypedDict, total=False
):
    metrics: _list[GoogleCloudDialogflowCxV3beta1ExperimentResultMetric]
    sessionCount: int
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportAgentRequest(typing.TypedDict, total=False):
    agentUri: str
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON_PACKAGE"]
    environment: str
    gitDestination: GoogleCloudDialogflowCxV3beta1ExportAgentRequestGitDestination
    includeBigqueryExportSettings: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportAgentRequestGitDestination(
    typing.TypedDict, total=False
):
    commitMessage: str
    trackingBranch: str

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
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesRequest(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON_PACKAGE"]
    entityTypes: _list[str]
    entityTypesContentInline: bool
    entityTypesUri: str
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesResponse(
    typing.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportFlowRequest(typing.TypedDict, total=False):
    flowUri: str
    includeReferencedFlows: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportFlowResponse(typing.TypedDict, total=False):
    flowContent: str
    flowUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsRequest(typing.TypedDict, total=False):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON", "CSV"]
    intents: _list[str]
    intentsContentInline: bool
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsResponse(
    typing.TypedDict, total=False
):
    intentsContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportPlaybookRequest(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    playbookUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesRequest(
    typing.TypedDict, total=False
):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    filter: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesResponse(
    typing.TypedDict, total=False
):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportToolsRequest(typing.TypedDict, total=False):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB"]
    tools: _list[str]
    toolsContentInline: bool
    toolsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FilterSpecs(typing.TypedDict, total=False):
    dataStores: _list[str]
    filter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Flow(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    description: str
    displayName: str
    eventHandlers: _list[GoogleCloudDialogflowCxV3beta1EventHandler]
    inputParameterDefinitions: _list[GoogleCloudDialogflowCxV3beta1ParameterDefinition]
    knowledgeConnectorSettings: GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettings
    locked: bool
    multiLanguageSettings: GoogleCloudDialogflowCxV3beta1FlowMultiLanguageSettings
    name: str
    nluSettings: GoogleCloudDialogflowCxV3beta1NluSettings
    outputParameterDefinitions: _list[GoogleCloudDialogflowCxV3beta1ParameterDefinition]
    transitionRouteGroups: _list[str]
    transitionRoutes: _list[GoogleCloudDialogflowCxV3beta1TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowImportStrategy(typing.TypedDict, total=False):
    globalImportStrategy: typing.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowInvocation(typing.TypedDict, total=False):
    displayName: str
    flow: str
    flowState: typing.Literal[
        "OUTPUT_STATE_UNSPECIFIED",
        "OUTPUT_STATE_OK",
        "OUTPUT_STATE_CANCELLED",
        "OUTPUT_STATE_FAILED",
        "OUTPUT_STATE_ESCALATED",
        "OUTPUT_STATE_PENDING",
    ]
    inputActionParameters: dict[str, typing.Any]
    outputActionParameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowMultiLanguageSettings(
    typing.TypedDict, total=False
):
    enableMultiLanguageDetection: bool
    supportedResponseLanguageCodes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowTraceMetadata(typing.TypedDict, total=False):
    displayName: str
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowTransition(typing.TypedDict, total=False):
    displayName: str
    flow: str
    inputActionParameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowValidationResult(typing.TypedDict, total=False):
    name: str
    updateTime: str
    validationMessages: _list[GoogleCloudDialogflowCxV3beta1ValidationMessage]

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
class GoogleCloudDialogflowCxV3beta1FulfillIntentRequest(typing.TypedDict, total=False):
    match: GoogleCloudDialogflowCxV3beta1Match
    matchIntentRequest: GoogleCloudDialogflowCxV3beta1MatchIntentRequest
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillIntentResponse(
    typing.TypedDict, total=False
):
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3beta1QueryResult
    responseId: str

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
class GoogleCloudDialogflowCxV3beta1GenerativeInfo(typing.TypedDict, total=False):
    actionTracingInfo: GoogleCloudDialogflowCxV3beta1Example
    currentPlaybooks: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettings(typing.TypedDict, total=False):
    fallbackSettings: GoogleCloudDialogflowCxV3beta1GenerativeSettingsFallbackSettings
    generativeSafetySettings: GoogleCloudDialogflowCxV3beta1SafetySettings
    knowledgeConnectorSettings: (
        GoogleCloudDialogflowCxV3beta1GenerativeSettingsKnowledgeConnectorSettings
    )
    languageCode: str
    llmModelSettings: GoogleCloudDialogflowCxV3beta1LlmModelSettings
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettingsFallbackSettings(
    typing.TypedDict, total=False
):
    promptTemplates: _list[
        GoogleCloudDialogflowCxV3beta1GenerativeSettingsFallbackSettingsPromptTemplate
    ]
    selectedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettingsFallbackSettingsPromptTemplate(
    typing.TypedDict, total=False
):
    displayName: str
    frozen: bool
    promptText: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettingsKnowledgeConnectorSettings(
    typing.TypedDict, total=False
):
    agent: str
    agentIdentity: str
    agentScope: str
    business: str
    businessDescription: str
    disableDataStoreFallback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Generator(typing.TypedDict, total=False):
    displayName: str
    llmModelSettings: GoogleCloudDialogflowCxV3beta1LlmModelSettings
    modelParameter: GoogleCloudDialogflowCxV3beta1GeneratorModelParameter
    name: str
    placeholders: _list[GoogleCloudDialogflowCxV3beta1GeneratorPlaceholder]
    promptText: GoogleCloudDialogflowCxV3beta1Phrase

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GeneratorModelParameter(
    typing.TypedDict, total=False
):
    maxDecodeSteps: int
    temperature: float
    topK: int
    topP: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GeneratorPlaceholder(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Handler(typing.TypedDict, total=False):
    eventHandler: GoogleCloudDialogflowCxV3beta1HandlerEventHandler
    lifecycleHandler: GoogleCloudDialogflowCxV3beta1HandlerLifecycleHandler

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1HandlerEventHandler(typing.TypedDict, total=False):
    condition: str
    event: str
    fulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1HandlerLifecycleHandler(
    typing.TypedDict, total=False
):
    condition: str
    fulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment
    lifecycleStage: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesRequest(
    typing.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3beta1InlineSource
    entityTypesUri: str
    mergeOption: typing.Literal[
        "MERGE_OPTION_UNSPECIFIED",
        "REPLACE",
        "MERGE",
        "RENAME",
        "REPORT_CONFLICT",
        "KEEP",
    ]
    targetEntityType: str

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
class GoogleCloudDialogflowCxV3beta1ImportFlowRequest(typing.TypedDict, total=False):
    flowContent: str
    flowImportStrategy: GoogleCloudDialogflowCxV3beta1FlowImportStrategy
    flowUri: str
    importOption: typing.Literal["IMPORT_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportFlowResponse(typing.TypedDict, total=False):
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsRequest(typing.TypedDict, total=False):
    intentsContent: GoogleCloudDialogflowCxV3beta1InlineSource
    intentsUri: str
    mergeOption: typing.Literal[
        "MERGE_OPTION_UNSPECIFIED",
        "REJECT",
        "REPLACE",
        "MERGE",
        "RENAME",
        "REPORT_CONFLICT",
        "KEEP",
    ]

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
class GoogleCloudDialogflowCxV3beta1ImportPlaybookRequest(
    typing.TypedDict, total=False
):
    importStrategy: GoogleCloudDialogflowCxV3beta1PlaybookImportStrategy
    playbookContent: str
    playbookUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadata(
    typing.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestCaseError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesRequest(
    typing.TypedDict, total=False
):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesResponse(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InlineDestination(typing.TypedDict, total=False):
    content: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InlineSchema(typing.TypedDict, total=False):
    items: GoogleCloudDialogflowCxV3beta1TypeSchema
    type: typing.Literal[
        "DATA_TYPE_UNSPECIFIED", "STRING", "NUMBER", "BOOLEAN", "ARRAY"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InlineSource(typing.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3beta1IntentCoverage(typing.TypedDict, total=False):
    coverageScore: float
    intents: _list[GoogleCloudDialogflowCxV3beta1IntentCoverageIntent]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentCoverageIntent(typing.TypedDict, total=False):
    covered: bool
    intent: str

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
class GoogleCloudDialogflowCxV3beta1ListAgentsResponse(typing.TypedDict, total=False):
    agents: _list[GoogleCloudDialogflowCxV3beta1Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListChangelogsResponse(
    typing.TypedDict, total=False
):
    changelogs: _list[GoogleCloudDialogflowCxV3beta1Changelog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponse(
    typing.TypedDict, total=False
):
    continuousTestResults: _list[GoogleCloudDialogflowCxV3beta1ContinuousTestResult]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListConversationsResponse(
    typing.TypedDict, total=False
):
    conversations: _list[GoogleCloudDialogflowCxV3beta1Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListDeploymentsResponse(
    typing.TypedDict, total=False
):
    deployments: _list[GoogleCloudDialogflowCxV3beta1Deployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEntityTypesResponse(
    typing.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowCxV3beta1EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponse(
    typing.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowCxV3beta1Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListExamplesResponse(typing.TypedDict, total=False):
    examples: _list[GoogleCloudDialogflowCxV3beta1Example]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListExperimentsResponse(
    typing.TypedDict, total=False
):
    experiments: _list[GoogleCloudDialogflowCxV3beta1Experiment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListFlowsResponse(typing.TypedDict, total=False):
    flows: _list[GoogleCloudDialogflowCxV3beta1Flow]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListGeneratorsResponse(
    typing.TypedDict, total=False
):
    generators: _list[GoogleCloudDialogflowCxV3beta1Generator]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListIntentsResponse(typing.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowCxV3beta1Intent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pages: _list[GoogleCloudDialogflowCxV3beta1Page]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    playbookVersions: _list[GoogleCloudDialogflowCxV3beta1PlaybookVersion]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPlaybooksResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    playbooks: _list[GoogleCloudDialogflowCxV3beta1Playbook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    securitySettings: _list[GoogleCloudDialogflowCxV3beta1SecuritySettings]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3beta1SessionEntityType]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    testCaseResults: _list[GoogleCloudDialogflowCxV3beta1TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTestCasesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    testCases: _list[GoogleCloudDialogflowCxV3beta1TestCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListToolVersionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    toolVersions: _list[GoogleCloudDialogflowCxV3beta1ToolVersion]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListToolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tools: _list[GoogleCloudDialogflowCxV3beta1Tool]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    transitionRouteGroups: _list[GoogleCloudDialogflowCxV3beta1TransitionRouteGroup]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[GoogleCloudDialogflowCxV3beta1Version]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListWebhooksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    webhooks: _list[GoogleCloudDialogflowCxV3beta1Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LlmCall(typing.TypedDict, total=False):
    model: str
    retrievedExamples: _list[GoogleCloudDialogflowCxV3beta1LlmCallRetrievedExample]
    temperature: float
    tokenCount: GoogleCloudDialogflowCxV3beta1LlmCallTokenCount

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LlmCallRetrievedExample(
    typing.TypedDict, total=False
):
    exampleDisplayName: str
    exampleId: str
    matchedRetrievalLabel: str
    retrievalStrategy: typing.Literal[
        "RETRIEVAL_STRATEGY_UNSPECIFIED", "DEFAULT", "STATIC", "NEVER"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LlmCallTokenCount(typing.TypedDict, total=False):
    conversationContextTokenCount: str
    exampleTokenCount: str
    totalInputTokenCount: str
    totalOutputTokenCount: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LlmModelSettings(typing.TypedDict, total=False):
    model: str
    parameters: GoogleCloudDialogflowCxV3beta1LlmModelSettingsParameters
    promptText: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LlmModelSettingsParameters(
    typing.TypedDict, total=False
):
    inputTokenLimit: typing.Literal[
        "INPUT_TOKEN_LIMIT_UNSPECIFIED",
        "INPUT_TOKEN_LIMIT_SHORT",
        "INPUT_TOKEN_LIMIT_MEDIUM",
        "INPUT_TOKEN_LIMIT_LONG",
    ]
    outputTokenLimit: typing.Literal[
        "OUTPUT_TOKEN_LIMIT_UNSPECIFIED",
        "OUTPUT_TOKEN_LIMIT_SHORT",
        "OUTPUT_TOKEN_LIMIT_MEDIUM",
        "OUTPUT_TOKEN_LIMIT_LONG",
    ]
    temperature: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LoadVersionRequest(typing.TypedDict, total=False):
    allowOverrideAgentResources: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponse(
    typing.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowCxV3beta1Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Match(typing.TypedDict, total=False):
    confidence: float
    event: str
    intent: GoogleCloudDialogflowCxV3beta1Intent
    matchType: typing.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "INTENT",
        "DIRECT_INTENT",
        "PARAMETER_FILLING",
        "NO_MATCH",
        "NO_INPUT",
        "EVENT",
        "KNOWLEDGE_CONNECTOR",
        "PLAYBOOK",
    ]
    parameters: dict[str, typing.Any]
    resolvedInput: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1MatchIntentRequest(typing.TypedDict, total=False):
    persistParameterChanges: bool
    queryInput: GoogleCloudDialogflowCxV3beta1QueryInput
    queryParams: GoogleCloudDialogflowCxV3beta1QueryParameters

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1MatchIntentResponse(typing.TypedDict, total=False):
    currentPage: GoogleCloudDialogflowCxV3beta1Page
    matches: _list[GoogleCloudDialogflowCxV3beta1Match]
    text: str
    transcript: str
    triggerEvent: str
    triggerIntent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1NamedMetric(typing.TypedDict, total=False):
    name: str
    unit: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1NluSettings(typing.TypedDict, total=False):
    classificationThreshold: float
    modelTrainingMode: typing.Literal[
        "MODEL_TRAINING_MODE_UNSPECIFIED",
        "MODEL_TRAINING_MODE_AUTOMATIC",
        "MODEL_TRAINING_MODE_MANUAL",
    ]
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED", "MODEL_TYPE_STANDARD", "MODEL_TYPE_ADVANCED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1OutputAudioConfig(typing.TypedDict, total=False):
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
    synthesizeSpeechConfig: GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig

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
class GoogleCloudDialogflowCxV3beta1ParameterDefinition(typing.TypedDict, total=False):
    description: str
    name: str
    type: typing.Literal[
        "PARAMETER_TYPE_UNSPECIFIED",
        "STRING",
        "NUMBER",
        "BOOLEAN",
        "NULL",
        "OBJECT",
        "LIST",
    ]
    typeSchema: GoogleCloudDialogflowCxV3beta1TypeSchema

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Phrase(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Playbook(typing.TypedDict, total=False):
    codeBlock: GoogleCloudDialogflowCxV3beta1CodeBlock
    createTime: str
    displayName: str
    goal: str
    handlers: _list[GoogleCloudDialogflowCxV3beta1Handler]
    inlineActions: _list[str]
    inputParameterDefinitions: _list[GoogleCloudDialogflowCxV3beta1ParameterDefinition]
    instruction: GoogleCloudDialogflowCxV3beta1PlaybookInstruction
    llmModelSettings: GoogleCloudDialogflowCxV3beta1LlmModelSettings
    name: str
    outputParameterDefinitions: _list[GoogleCloudDialogflowCxV3beta1ParameterDefinition]
    playbookType: typing.Literal["PLAYBOOK_TYPE_UNSPECIFIED", "TASK", "ROUTINE"]
    referencedFlows: _list[str]
    referencedPlaybooks: _list[str]
    referencedTools: _list[str]
    speechSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsSpeechSettings
    tokenCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookImportStrategy(
    typing.TypedDict, total=False
):
    mainPlaybookImportStrategy: typing.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]
    nestedResourceImportStrategy: typing.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]
    toolImportStrategy: typing.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookInput(typing.TypedDict, total=False):
    actionParameters: dict[str, typing.Any]
    precedingConversationSummary: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookInstruction(typing.TypedDict, total=False):
    guidelines: str
    steps: _list[GoogleCloudDialogflowCxV3beta1PlaybookStep]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookInvocation(typing.TypedDict, total=False):
    displayName: str
    playbook: str
    playbookInput: GoogleCloudDialogflowCxV3beta1PlaybookInput
    playbookOutput: GoogleCloudDialogflowCxV3beta1PlaybookOutput
    playbookState: typing.Literal[
        "OUTPUT_STATE_UNSPECIFIED",
        "OUTPUT_STATE_OK",
        "OUTPUT_STATE_CANCELLED",
        "OUTPUT_STATE_FAILED",
        "OUTPUT_STATE_ESCALATED",
        "OUTPUT_STATE_PENDING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookOutput(typing.TypedDict, total=False):
    actionParameters: dict[str, typing.Any]
    executionSummary: str
    state: typing.Literal["STATE_UNSPECIFIED", "OK", "CANCELLED", "FAILED", "ESCALATED"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookStep(typing.TypedDict, total=False):
    steps: _list[GoogleCloudDialogflowCxV3beta1PlaybookStep]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookTraceMetadata(
    typing.TypedDict, total=False
):
    displayName: str
    playbook: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookTransition(typing.TypedDict, total=False):
    displayName: str
    inputActionParameters: dict[str, typing.Any]
    playbook: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookVersion(typing.TypedDict, total=False):
    description: str
    examples: _list[GoogleCloudDialogflowCxV3beta1Example]
    name: str
    playbook: GoogleCloudDialogflowCxV3beta1Playbook
    updateTime: str

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
class GoogleCloudDialogflowCxV3beta1QueryParameters(typing.TypedDict, total=False):
    analyzeQueryTextSentiment: bool
    channel: str
    currentPage: str
    currentPlaybook: str
    disableWebhook: bool
    endUserMetadata: dict[str, typing.Any]
    flowVersions: _list[str]
    geoLocation: GoogleTypeLatLng
    llmModelSettings: GoogleCloudDialogflowCxV3beta1LlmModelSettings
    parameterScope: str
    parameters: dict[str, typing.Any]
    payload: dict[str, typing.Any]
    populateDataStoreConnectionSignals: bool
    searchConfig: GoogleCloudDialogflowCxV3beta1SearchConfig
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3beta1SessionEntityType]
    sessionTtl: str
    timeZone: str
    webhookHeaders: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1QueryResult(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    allowAnswerFeedback: bool
    currentFlow: GoogleCloudDialogflowCxV3beta1Flow
    currentPage: GoogleCloudDialogflowCxV3beta1Page
    dataStoreConnectionSignals: GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignals
    diagnosticInfo: dict[str, typing.Any]
    dtmf: GoogleCloudDialogflowCxV3beta1DtmfInput
    generativeInfo: GoogleCloudDialogflowCxV3beta1GenerativeInfo
    intent: GoogleCloudDialogflowCxV3beta1Intent
    intentDetectionConfidence: float
    languageCode: str
    match: GoogleCloudDialogflowCxV3beta1Match
    parameters: dict[str, typing.Any]
    responseMessages: _list[GoogleCloudDialogflowCxV3beta1ResponseMessage]
    sentimentAnalysisResult: GoogleCloudDialogflowCxV3beta1SentimentAnalysisResult
    text: str
    traceBlocks: _list[GoogleCloudDialogflowCxV3beta1TraceBlock]
    transcript: str
    triggerEvent: str
    triggerIntent: str
    webhookDisplayNames: _list[str]
    webhookIds: _list[str]
    webhookLatencies: _list[str]
    webhookPayloads: _list[dict[str, typing.Any]]
    webhookStatuses: _list[GoogleRpcStatus]
    webhookTags: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResourceName(typing.TypedDict, total=False):
    displayName: str
    name: str

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
class GoogleCloudDialogflowCxV3beta1RestoreAgentRequest(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str
    gitSource: GoogleCloudDialogflowCxV3beta1RestoreAgentRequestGitSource
    restoreOption: typing.Literal["RESTORE_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestoreAgentRequestGitSource(
    typing.TypedDict, total=False
):
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionResponse(
    typing.TypedDict, total=False
):
    playbook: GoogleCloudDialogflowCxV3beta1Playbook

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestoreToolVersionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestoreToolVersionResponse(
    typing.TypedDict, total=False
):
    tool: GoogleCloudDialogflowCxV3beta1Tool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RolloutConfig(typing.TypedDict, total=False):
    failureCondition: str
    rolloutCondition: str
    rolloutSteps: _list[GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStep]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStep(
    typing.TypedDict, total=False
):
    displayName: str
    minDuration: str
    trafficPercent: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RolloutState(typing.TypedDict, total=False):
    startTime: str
    step: str
    stepIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadata(
    typing.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestRequest(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDialogflowCxV3beta1RunTestCaseRequest(typing.TypedDict, total=False):
    environment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunTestCaseResponse(typing.TypedDict, total=False):
    result: GoogleCloudDialogflowCxV3beta1TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SafetySettings(typing.TypedDict, total=False):
    bannedPhrases: _list[GoogleCloudDialogflowCxV3beta1SafetySettingsPhrase]
    defaultBannedPhraseMatchStrategy: typing.Literal[
        "PHRASE_MATCH_STRATEGY_UNSPECIFIED", "PARTIAL_MATCH", "WORD_MATCH"
    ]
    defaultRaiSettings: GoogleCloudDialogflowCxV3beta1SafetySettingsRaiSettings
    promptSecuritySettings: (
        GoogleCloudDialogflowCxV3beta1SafetySettingsPromptSecuritySettings
    )
    raiSettings: GoogleCloudDialogflowCxV3beta1SafetySettingsRaiSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SafetySettingsPhrase(typing.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SafetySettingsPromptSecuritySettings(
    typing.TypedDict, total=False
):
    enablePromptSecurity: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SafetySettingsRaiSettings(
    typing.TypedDict, total=False
):
    categoryFilters: _list[
        GoogleCloudDialogflowCxV3beta1SafetySettingsRaiSettingsCategoryFilter
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SafetySettingsRaiSettingsCategoryFilter(
    typing.TypedDict, total=False
):
    category: typing.Literal[
        "SAFETY_CATEGORY_UNSPECIFIED",
        "DANGEROUS_CONTENT",
        "HATE_SPEECH",
        "HARASSMENT",
        "SEXUALLY_EXPLICIT_CONTENT",
    ]
    filterLevel: typing.Literal[
        "SAFETY_FILTER_LEVEL_UNSPECIFIED",
        "BLOCK_NONE",
        "BLOCK_FEW",
        "BLOCK_SOME",
        "BLOCK_MOST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SearchConfig(typing.TypedDict, total=False):
    boostSpecs: _list[GoogleCloudDialogflowCxV3beta1BoostSpecs]
    filterSpecs: _list[GoogleCloudDialogflowCxV3beta1FilterSpecs]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SecuritySettings(typing.TypedDict, total=False):
    audioExportSettings: (
        GoogleCloudDialogflowCxV3beta1SecuritySettingsAudioExportSettings
    )
    deidentifyTemplate: str
    displayName: str
    insightsExportSettings: (
        GoogleCloudDialogflowCxV3beta1SecuritySettingsInsightsExportSettings
    )
    inspectTemplate: str
    name: str
    purgeDataTypes: _list[
        typing.Literal["PURGE_DATA_TYPE_UNSPECIFIED", "DIALOGFLOW_HISTORY"]
    ]
    redactionScope: typing.Literal["REDACTION_SCOPE_UNSPECIFIED", "REDACT_DISK_STORAGE"]
    redactionStrategy: typing.Literal[
        "REDACTION_STRATEGY_UNSPECIFIED", "REDACT_WITH_SERVICE"
    ]
    retentionStrategy: typing.Literal[
        "RETENTION_STRATEGY_UNSPECIFIED", "REMOVE_AFTER_CONVERSATION"
    ]
    retentionWindowDays: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SecuritySettingsAudioExportSettings(
    typing.TypedDict, total=False
):
    audioExportPattern: str
    audioFormat: typing.Literal["AUDIO_FORMAT_UNSPECIFIED", "MULAW", "MP3", "OGG"]
    enableAudioRedaction: bool
    gcsBucket: str
    storeTtsAudio: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SecuritySettingsInsightsExportSettings(
    typing.TypedDict, total=False
):
    enableInsightsExport: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SentimentAnalysisResult(
    typing.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionEntityType(typing.TypedDict, total=False):
    entities: _list[GoogleCloudDialogflowCxV3beta1EntityTypeEntity]
    entityOverrideMode: typing.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionInfo(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Span(typing.TypedDict, total=False):
    completeTime: str
    metrics: _list[GoogleCloudDialogflowCxV3beta1NamedMetric]
    name: str
    startTime: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SpeechProcessingMetadata(
    typing.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SpeechToTextSettings(typing.TypedDict, total=False):
    enableSpeechAdaptation: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1StartExperimentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Status(typing.TypedDict, total=False):
    exception: GoogleCloudDialogflowCxV3beta1ExceptionDetail

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1StopExperimentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SubmitAnswerFeedbackRequest(
    typing.TypedDict, total=False
):
    answerFeedback: GoogleCloudDialogflowCxV3beta1AnswerFeedback
    responseId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig(
    typing.TypedDict, total=False
):
    effectsProfileId: _list[str]
    pitch: float
    speakingRate: float
    voice: GoogleCloudDialogflowCxV3beta1VoiceSelectionParams
    volumeGainDb: float

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
class GoogleCloudDialogflowCxV3beta1TextToSpeechSettings(typing.TypedDict, total=False):
    synthesizeSpeechConfigs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Tool(typing.TypedDict, total=False):
    connectorSpec: GoogleCloudDialogflowCxV3beta1ToolConnectorTool
    dataStoreSpec: GoogleCloudDialogflowCxV3beta1ToolDataStoreTool
    description: str
    displayName: str
    extensionSpec: GoogleCloudDialogflowCxV3beta1ToolExtensionTool
    functionSpec: GoogleCloudDialogflowCxV3beta1ToolFunctionTool
    name: str
    openApiSpec: GoogleCloudDialogflowCxV3beta1ToolOpenApiTool
    toolType: typing.Literal["TOOL_TYPE_UNSPECIFIED", "CUSTOMIZED_TOOL", "BUILTIN_TOOL"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthentication(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudDialogflowCxV3beta1ToolAuthenticationApiKeyConfig
    bearerTokenConfig: GoogleCloudDialogflowCxV3beta1ToolAuthenticationBearerTokenConfig
    oauthConfig: GoogleCloudDialogflowCxV3beta1ToolAuthenticationOAuthConfig
    serviceAccountAuthConfig: (
        GoogleCloudDialogflowCxV3beta1ToolAuthenticationServiceAccountAuthConfig
    )
    serviceAgentAuthConfig: (
        GoogleCloudDialogflowCxV3beta1ToolAuthenticationServiceAgentAuthConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationApiKeyConfig(
    typing.TypedDict, total=False
):
    apiKey: str
    keyName: str
    requestLocation: typing.Literal[
        "REQUEST_LOCATION_UNSPECIFIED", "HEADER", "QUERY_STRING"
    ]
    secretVersionForApiKey: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationBearerTokenConfig(
    typing.TypedDict, total=False
):
    secretVersionForToken: str
    token: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationOAuthConfig(
    typing.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    oauthGrantType: typing.Literal["OAUTH_GRANT_TYPE_UNSPECIFIED", "CLIENT_CREDENTIAL"]
    scopes: _list[str]
    secretVersionForClientSecret: str
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationServiceAccountAuthConfig(
    typing.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationServiceAgentAuthConfig(
    typing.TypedDict, total=False
):
    serviceAgentAuth: typing.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "ID_TOKEN", "ACCESS_TOKEN"
    ]

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
class GoogleCloudDialogflowCxV3beta1ToolConnectorTool(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDialogflowCxV3beta1ToolConnectorToolAction]
    endUserAuthConfig: GoogleCloudDialogflowCxV3beta1ToolEndUserAuthConfig
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolConnectorToolAction(
    typing.TypedDict, total=False
):
    connectionActionId: str
    entityOperation: (
        GoogleCloudDialogflowCxV3beta1ToolConnectorToolActionEntityOperation
    )
    inputFields: _list[str]
    outputFields: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolConnectorToolActionEntityOperation(
    typing.TypedDict, total=False
):
    entityId: str
    operation: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolDataStoreTool(typing.TypedDict, total=False):
    dataStoreConnections: _list[GoogleCloudDialogflowCxV3beta1DataStoreConnection]
    fallbackPrompt: GoogleCloudDialogflowCxV3beta1ToolDataStoreToolFallbackPrompt

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolDataStoreToolFallbackPrompt(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolEndUserAuthConfig(
    typing.TypedDict, total=False
):
    oauth2AuthCodeConfig: (
        GoogleCloudDialogflowCxV3beta1ToolEndUserAuthConfigOauth2AuthCodeConfig
    )
    oauth2JwtBearerConfig: (
        GoogleCloudDialogflowCxV3beta1ToolEndUserAuthConfigOauth2JwtBearerConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolEndUserAuthConfigOauth2AuthCodeConfig(
    typing.TypedDict, total=False
):
    oauthToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolEndUserAuthConfigOauth2JwtBearerConfig(
    typing.TypedDict, total=False
):
    clientKey: str
    issuer: str
    subject: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolExtensionTool(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolFunctionTool(typing.TypedDict, total=False):
    inputSchema: dict[str, typing.Any]
    outputSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolOpenApiTool(typing.TypedDict, total=False):
    authentication: GoogleCloudDialogflowCxV3beta1ToolAuthentication
    serviceDirectoryConfig: GoogleCloudDialogflowCxV3beta1ToolServiceDirectoryConfig
    textSchema: str
    tlsConfig: GoogleCloudDialogflowCxV3beta1ToolTLSConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolServiceDirectoryConfig(
    typing.TypedDict, total=False
):
    service: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolTLSConfig(typing.TypedDict, total=False):
    caCerts: _list[GoogleCloudDialogflowCxV3beta1ToolTLSConfigCACert]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolTLSConfigCACert(typing.TypedDict, total=False):
    cert: str
    displayName: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolUse(typing.TypedDict, total=False):
    action: str
    dataStoreToolTrace: GoogleCloudDialogflowCxV3beta1ToolUseDataStoreToolTrace
    displayName: str
    inputActionParameters: dict[str, typing.Any]
    outputActionParameters: dict[str, typing.Any]
    tool: str
    webhookToolTrace: GoogleCloudDialogflowCxV3beta1ToolUseWebhookToolTrace

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolUseDataStoreToolTrace(
    typing.TypedDict, total=False
):
    dataStoreConnectionSignals: GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignals

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolUseWebhookToolTrace(
    typing.TypedDict, total=False
):
    webhookTag: str
    webhookUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolVersion(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    tool: GoogleCloudDialogflowCxV3beta1Tool
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TraceBlock(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDialogflowCxV3beta1Action]
    completeTime: str
    endState: typing.Literal[
        "OUTPUT_STATE_UNSPECIFIED",
        "OUTPUT_STATE_OK",
        "OUTPUT_STATE_CANCELLED",
        "OUTPUT_STATE_FAILED",
        "OUTPUT_STATE_ESCALATED",
        "OUTPUT_STATE_PENDING",
    ]
    flowTraceMetadata: GoogleCloudDialogflowCxV3beta1FlowTraceMetadata
    inputParameters: dict[str, typing.Any]
    outputParameters: dict[str, typing.Any]
    playbookTraceMetadata: GoogleCloudDialogflowCxV3beta1PlaybookTraceMetadata
    speechProcessingMetadata: GoogleCloudDialogflowCxV3beta1SpeechProcessingMetadata
    startTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TrainFlowRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionCoverage(typing.TypedDict, total=False):
    coverageScore: float
    transitions: _list[GoogleCloudDialogflowCxV3beta1TransitionCoverageTransition]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionCoverageTransition(
    typing.TypedDict, total=False
):
    covered: bool
    eventHandler: GoogleCloudDialogflowCxV3beta1EventHandler
    index: int
    source: GoogleCloudDialogflowCxV3beta1TransitionCoverageTransitionNode
    target: GoogleCloudDialogflowCxV3beta1TransitionCoverageTransitionNode
    transitionRoute: GoogleCloudDialogflowCxV3beta1TransitionRoute

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionCoverageTransitionNode(
    typing.TypedDict, total=False
):
    flow: GoogleCloudDialogflowCxV3beta1Flow
    page: GoogleCloudDialogflowCxV3beta1Page

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
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroup(typing.TypedDict, total=False):
    displayName: str
    name: str
    transitionRoutes: _list[GoogleCloudDialogflowCxV3beta1TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverage(
    typing.TypedDict, total=False
):
    coverageScore: float
    coverages: _list[GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverage(
    typing.TypedDict, total=False
):
    coverageScore: float
    routeGroup: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup
    transitions: _list[
        GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverageTransition
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverageTransition(
    typing.TypedDict, total=False
):
    covered: bool
    transitionRoute: GoogleCloudDialogflowCxV3beta1TransitionRoute

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
class GoogleCloudDialogflowCxV3beta1TypeSchema(typing.TypedDict, total=False):
    inlineSchema: GoogleCloudDialogflowCxV3beta1InlineSchema
    schemaReference: GoogleCloudDialogflowCxV3beta1TypeSchemaSchemaReference

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TypeSchemaSchemaReference(
    typing.TypedDict, total=False
):
    schema: str
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1UserUtterance(typing.TypedDict, total=False):
    audio: str
    audioTokens: _list[int]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ValidateAgentRequest(typing.TypedDict, total=False):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ValidateFlowRequest(typing.TypedDict, total=False):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ValidationMessage(typing.TypedDict, total=False):
    detail: str
    resourceNames: _list[GoogleCloudDialogflowCxV3beta1ResourceName]
    resourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "AGENT",
        "INTENT",
        "INTENT_TRAINING_PHRASE",
        "INTENT_PARAMETER",
        "INTENTS",
        "INTENT_TRAINING_PHRASES",
        "ENTITY_TYPE",
        "ENTITY_TYPES",
        "WEBHOOK",
        "FLOW",
        "PAGE",
        "PAGES",
        "TRANSITION_ROUTE_GROUP",
        "AGENT_TRANSITION_ROUTE_GROUP",
    ]
    resources: _list[str]
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VariantsHistory(typing.TypedDict, total=False):
    updateTime: str
    versionVariants: GoogleCloudDialogflowCxV3beta1VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Version(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    nluSettings: GoogleCloudDialogflowCxV3beta1NluSettings
    state: typing.Literal["STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VersionVariants(typing.TypedDict, total=False):
    variants: _list[GoogleCloudDialogflowCxV3beta1VersionVariantsVariant]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VersionVariantsVariant(
    typing.TypedDict, total=False
):
    isControlGroup: bool
    trafficAllocation: float
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VoiceSelectionParams(typing.TypedDict, total=False):
    name: str
    ssmlGender: typing.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED",
        "SSML_VOICE_GENDER_MALE",
        "SSML_VOICE_GENDER_FEMALE",
        "SSML_VOICE_GENDER_NEUTRAL",
    ]

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
class GoogleCloudDialogflowV2AnnotatedMessagePart(typing.TypedDict, total=False):
    entityType: str
    formattedValue: typing.Any
    text: str

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
class GoogleCloudDialogflowV2BatchUpdateEntityTypesResponse(
    typing.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateIntentsResponse(typing.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowV2Intent]

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
class GoogleCloudDialogflowV2Context(typing.TypedDict, total=False):
    lifespanCount: int
    name: str
    parameters: dict[str, typing.Any]

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
class GoogleCloudDialogflowV2EntityTypeEntity(typing.TypedDict, total=False):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2EventInput(typing.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2ExportAgentResponse(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str

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
class GoogleCloudDialogflowV2FreeFormSuggestion(typing.TypedDict, total=False):
    response: str

@typing.type_check_only
class GoogleCloudDialogflowV2GcsDestination(typing.TypedDict, total=False):
    uri: str

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
class GoogleCloudDialogflowV2HumanAgentAssistantEvent(typing.TypedDict, total=False):
    conversation: str
    participant: str
    suggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]

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
class GoogleCloudDialogflowV2ImportDocumentsResponse(typing.TypedDict, total=False):
    warnings: _list[GoogleRpcStatus]

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
class GoogleCloudDialogflowV2KnowledgeOperationMetadata(typing.TypedDict, total=False):
    doneTime: str
    exportOperationMetadata: GoogleCloudDialogflowV2ExportOperationMetadata
    knowledgeBase: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

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
class GoogleCloudDialogflowV2OriginalDetectIntentRequest(typing.TypedDict, total=False):
    payload: dict[str, typing.Any]
    source: str
    version: str

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
class GoogleCloudDialogflowV2Sentiment(typing.TypedDict, total=False):
    magnitude: float
    score: float

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
class GoogleCloudDialogflowV2SmartReplyAnswer(typing.TypedDict, total=False):
    answerRecord: str
    confidence: float
    reply: str

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyModelMetadata(typing.TypedDict, total=False):
    trainingModelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "SMART_REPLY_DUAL_ENCODER_MODEL",
        "SMART_REPLY_BERT_MODEL",
    ]

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
class GoogleCloudDialogflowV2SuggestArticlesResponse(typing.TypedDict, total=False):
    articleAnswers: _list[GoogleCloudDialogflowV2ArticleAnswer]
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestFaqAnswersResponse(typing.TypedDict, total=False):
    contextSize: int
    faqAnswers: _list[GoogleCloudDialogflowV2FaqAnswer]
    latestMessage: str

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
class GoogleCloudDialogflowV2SuggestSmartRepliesResponse(typing.TypedDict, total=False):
    contextSize: int
    latestMessage: str
    smartReplyAnswers: _list[GoogleCloudDialogflowV2SmartReplyAnswer]

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
class GoogleCloudDialogflowV2SummarySuggestion(typing.TypedDict, total=False):
    summarySections: _list[GoogleCloudDialogflowV2SummarySuggestionSummarySection]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarySuggestionSummarySection(
    typing.TypedDict, total=False
):
    section: str
    summary: str

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
class GoogleCloudDialogflowV2UndeployConversationModelOperationMetadata(
    typing.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str

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
