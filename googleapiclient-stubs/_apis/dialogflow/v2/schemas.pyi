import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettings(
    typing_extensions.TypedDict, total=False
):
    audioExportGcsDestination: GoogleCloudDialogflowCxV3GcsDestination
    dtmfSettings: GoogleCloudDialogflowCxV3AdvancedSettingsDtmfSettings
    loggingSettings: GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettings
    speechSettings: GoogleCloudDialogflowCxV3AdvancedSettingsSpeechSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettingsDtmfSettings(
    typing_extensions.TypedDict, total=False
):
    enabled: bool
    endpointingTimeoutDuration: str
    finishDigit: str
    interdigitTimeoutDuration: str
    maxDigits: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettingsLoggingSettings(
    typing_extensions.TypedDict, total=False
):
    enableConsentBasedRedaction: bool
    enableInteractionLogging: bool
    enableStackdriverLogging: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3AdvancedSettingsSpeechSettings(
    typing_extensions.TypedDict, total=False
):
    endpointerSensitivity: int
    models: dict[str, typing.Any]
    noSpeechTimeout: str
    useTimeoutBasedEndpointing: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3AudioInput(typing_extensions.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowCxV3InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3BargeInConfig(typing_extensions.TypedDict, total=False):
    noBargeInDuration: str
    totalDuration: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    results: _list[GoogleCloudDialogflowCxV3TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ContinuousTestResult(
    typing_extensions.TypedDict, total=False
):
    name: str
    result: typing_extensions.Literal[
        "AGGREGATED_TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"
    ]
    runTime: str
    testCaseResults: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationSignals(
    typing_extensions.TypedDict, total=False
):
    turnSignals: GoogleCloudDialogflowCxV3TurnSignals

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationTurn(
    typing_extensions.TypedDict, total=False
):
    userInput: GoogleCloudDialogflowCxV3ConversationTurnUserInput
    virtualAgentOutput: GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutput

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationTurnUserInput(
    typing_extensions.TypedDict, total=False
):
    enableSentimentAnalysis: bool
    injectedParameters: dict[str, typing.Any]
    input: GoogleCloudDialogflowCxV3QueryInput
    isWebhookEnabled: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutput(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnection(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    dataStoreType: typing_extensions.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED", "PUBLIC_WEB", "UNSTRUCTURED", "STRUCTURED"
    ]
    documentProcessingMode: typing_extensions.Literal[
        "DOCUMENT_PROCESSING_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowMetadata(
    typing_extensions.TypedDict, total=False
):
    testErrors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowResponse(
    typing_extensions.TypedDict, total=False
):
    deployment: str
    environment: GoogleCloudDialogflowCxV3Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3DtmfInput(typing_extensions.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Environment(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    testCasesConfig: GoogleCloudDialogflowCxV3EnvironmentTestCasesConfig
    updateTime: str
    versionConfigs: _list[GoogleCloudDialogflowCxV3EnvironmentVersionConfig]
    webhookConfig: GoogleCloudDialogflowCxV3EnvironmentWebhookConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3EnvironmentTestCasesConfig(
    typing_extensions.TypedDict, total=False
):
    enableContinuousRun: bool
    enablePredeploymentRun: bool
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3EnvironmentVersionConfig(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3EnvironmentWebhookConfig(
    typing_extensions.TypedDict, total=False
):
    webhookOverrides: _list[GoogleCloudDialogflowCxV3Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3EventHandler(typing_extensions.TypedDict, total=False):
    event: str
    name: str
    targetFlow: str
    targetPage: str
    targetPlaybook: str
    triggerFulfillment: GoogleCloudDialogflowCxV3Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3EventInput(typing_extensions.TypedDict, total=False):
    event: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str
    commitSha: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportEntityTypesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportFlowResponse(
    typing_extensions.TypedDict, total=False
):
    flowContent: str
    flowUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportIntentsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intentsContent: GoogleCloudDialogflowCxV3InlineDestination
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Form(typing_extensions.TypedDict, total=False):
    parameters: _list[GoogleCloudDialogflowCxV3FormParameter]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FormParameter(typing_extensions.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    defaultValue: typing.Any
    displayName: str
    entityType: str
    fillBehavior: GoogleCloudDialogflowCxV3FormParameterFillBehavior
    isList: bool
    redact: bool
    required: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3FormParameterFillBehavior(
    typing_extensions.TypedDict, total=False
):
    initialPromptFulfillment: GoogleCloudDialogflowCxV3Fulfillment
    repromptEventHandlers: _list[GoogleCloudDialogflowCxV3EventHandler]

@typing.type_check_only
class GoogleCloudDialogflowCxV3Fulfillment(typing_extensions.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
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
    typing_extensions.TypedDict, total=False
):
    cases: _list[GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCase(
    typing_extensions.TypedDict, total=False
):
    caseContent: _list[
        GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContent
    ]
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContent(
    typing_extensions.TypedDict, total=False
):
    additionalCases: GoogleCloudDialogflowCxV3FulfillmentConditionalCases
    message: GoogleCloudDialogflowCxV3ResponseMessage

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentGeneratorSettings(
    typing_extensions.TypedDict, total=False
):
    generator: str
    inputParameters: dict[str, typing.Any]
    outputParameter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillmentSetParameterAction(
    typing_extensions.TypedDict, total=False
):
    parameter: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    conflictingResources: (
        GoogleCloudDialogflowCxV3ImportEntityTypesResponseConflictingResources
    )
    entityTypes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesResponseConflictingResources(
    typing_extensions.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    entityTypeDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportFlowResponse(
    typing_extensions.TypedDict, total=False
):
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    conflictingResources: (
        GoogleCloudDialogflowCxV3ImportIntentsResponseConflictingResources
    )
    intents: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsResponseConflictingResources(
    typing_extensions.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    intentDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3TestCaseError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3InlineDestination(
    typing_extensions.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3InputAudioConfig(
    typing_extensions.TypedDict, total=False
):
    audioEncoding: typing_extensions.Literal[
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
    modelVariant: typing_extensions.Literal[
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
class GoogleCloudDialogflowCxV3Intent(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    isFallback: bool
    labels: dict[str, typing.Any]
    name: str
    parameters: _list[GoogleCloudDialogflowCxV3IntentParameter]
    priority: int
    trainingPhrases: _list[GoogleCloudDialogflowCxV3IntentTrainingPhrase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentInput(typing_extensions.TypedDict, total=False):
    intent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentParameter(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    id: str
    isList: bool
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    id: str
    parts: _list[GoogleCloudDialogflowCxV3IntentTrainingPhrasePart]
    repeatCount: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    parameterId: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3KnowledgeConnectorSettings(
    typing_extensions.TypedDict, total=False
):
    dataStoreConnections: _list[GoogleCloudDialogflowCxV3DataStoreConnection]
    enabled: bool
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3LanguageInfo(typing_extensions.TypedDict, total=False):
    confidenceScore: float
    inputLanguageCode: str
    resolvedLanguageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Page(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3PageInfo(typing_extensions.TypedDict, total=False):
    currentPage: str
    displayName: str
    formInfo: GoogleCloudDialogflowCxV3PageInfoFormInfo

@typing.type_check_only
class GoogleCloudDialogflowCxV3PageInfoFormInfo(
    typing_extensions.TypedDict, total=False
):
    parameterInfo: _list[GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfo]

@typing.type_check_only
class GoogleCloudDialogflowCxV3PageInfoFormInfoParameterInfo(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    justCollected: bool
    required: bool
    state: typing_extensions.Literal[
        "PARAMETER_STATE_UNSPECIFIED", "EMPTY", "INVALID", "FILLED"
    ]
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3QueryInput(typing_extensions.TypedDict, total=False):
    audio: GoogleCloudDialogflowCxV3AudioInput
    dtmf: GoogleCloudDialogflowCxV3DtmfInput
    event: GoogleCloudDialogflowCxV3EventInput
    intent: GoogleCloudDialogflowCxV3IntentInput
    languageCode: str
    text: GoogleCloudDialogflowCxV3TextInput
    toolCallResult: GoogleCloudDialogflowCxV3ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessage(
    typing_extensions.TypedDict, total=False
):
    channel: str
    conversationSuccess: GoogleCloudDialogflowCxV3ResponseMessageConversationSuccess
    endInteraction: GoogleCloudDialogflowCxV3ResponseMessageEndInteraction
    knowledgeInfoCard: GoogleCloudDialogflowCxV3ResponseMessageKnowledgeInfoCard
    liveAgentHandoff: GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoff
    mixedAudio: GoogleCloudDialogflowCxV3ResponseMessageMixedAudio
    outputAudioText: GoogleCloudDialogflowCxV3ResponseMessageOutputAudioText
    payload: dict[str, typing.Any]
    playAudio: GoogleCloudDialogflowCxV3ResponseMessagePlayAudio
    responseType: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageEndInteraction(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageKnowledgeInfoCard(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoff(
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageMixedAudio(
    typing_extensions.TypedDict, total=False
):
    segments: _list[GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegment]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageMixedAudioSegment(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audio: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageOutputAudioText(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    ssml: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessagePlayAudio(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audioUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageTelephonyTransferCall(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResponseMessageText(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestResponse(
    typing_extensions.TypedDict, total=False
):
    continuousTestResult: GoogleCloudDialogflowCxV3ContinuousTestResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseResponse(
    typing_extensions.TypedDict, total=False
):
    result: GoogleCloudDialogflowCxV3TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3SessionInfo(typing_extensions.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCase(typing_extensions.TypedDict, total=False):
    creationTime: str
    displayName: str
    lastTestResult: GoogleCloudDialogflowCxV3TestCaseResult
    name: str
    notes: str
    tags: _list[str]
    testCaseConversationTurns: _list[GoogleCloudDialogflowCxV3ConversationTurn]
    testConfig: GoogleCloudDialogflowCxV3TestConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCaseError(typing_extensions.TypedDict, total=False):
    status: GoogleRpcStatus
    testCase: GoogleCloudDialogflowCxV3TestCase

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCaseResult(typing_extensions.TypedDict, total=False):
    conversationTurns: _list[GoogleCloudDialogflowCxV3ConversationTurn]
    environment: str
    name: str
    testResult: typing_extensions.Literal["TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestConfig(typing_extensions.TypedDict, total=False):
    flow: str
    page: str
    trackingParameters: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestError(typing_extensions.TypedDict, total=False):
    status: GoogleRpcStatus
    testCase: str
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestRunDifference(
    typing_extensions.TypedDict, total=False
):
    description: str
    type: typing_extensions.Literal[
        "DIFF_TYPE_UNSPECIFIED", "INTENT", "PAGE", "PARAMETERS", "UTTERANCE", "FLOW"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TextInput(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolCall(typing_extensions.TypedDict, total=False):
    action: str
    inputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolCallResult(typing_extensions.TypedDict, total=False):
    action: str
    error: GoogleCloudDialogflowCxV3ToolCallResultError
    outputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolCallResultError(
    typing_extensions.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRoute(
    typing_extensions.TypedDict, total=False
):
    condition: str
    description: str
    intent: str
    name: str
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3TurnSignals(typing_extensions.TypedDict, total=False):
    agentEscalated: bool
    dtmfUsed: bool
    failureReasons: _list[
        typing_extensions.Literal[
            "FAILURE_REASON_UNSPECIFIED", "FAILED_INTENT", "FAILED_WEBHOOK"
        ]
    ]
    noMatch: bool
    noUserInput: bool
    reachedEndPage: bool
    sentimentMagnitude: float
    sentimentScore: float
    userEscalated: bool
    webhookStatuses: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3Webhook(typing_extensions.TypedDict, total=False):
    disabled: bool
    displayName: str
    genericWebService: GoogleCloudDialogflowCxV3WebhookGenericWebService
    name: str
    serviceDirectory: GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfig
    timeout: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookGenericWebService(
    typing_extensions.TypedDict, total=False
):
    allowedCaCerts: _list[str]
    httpMethod: typing_extensions.Literal[
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
    serviceAgentAuth: typing_extensions.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "NONE", "ID_TOKEN", "ACCESS_TOKEN"
    ]
    uri: str
    username: str
    webhookType: typing_extensions.Literal[
        "WEBHOOK_TYPE_UNSPECIFIED", "STANDARD", "FLEXIBLE"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookGenericWebServiceOAuthConfig(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    scopes: _list[str]
    secretVersionForClientSecret: str
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookGenericWebServiceSecretVersionHeaderValue(
    typing_extensions.TypedDict, total=False
):
    secretVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequest(typing_extensions.TypedDict, total=False):
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
    typing_extensions.TypedDict, total=False
):
    tag: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequestIntentInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    lastMatchedIntent: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequestIntentInfoIntentParameterValue(
    typing_extensions.TypedDict, total=False
):
    originalValue: str
    resolvedValue: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookRequestSentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookResponse(
    typing_extensions.TypedDict, total=False
):
    fulfillmentResponse: GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponse
    pageInfo: GoogleCloudDialogflowCxV3PageInfo
    payload: dict[str, typing.Any]
    sessionInfo: GoogleCloudDialogflowCxV3SessionInfo
    targetFlow: str
    targetPage: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponse(
    typing_extensions.TypedDict, total=False
):
    mergeBehavior: typing_extensions.Literal[
        "MERGE_BEHAVIOR_UNSPECIFIED", "APPEND", "REPLACE"
    ]
    messages: _list[GoogleCloudDialogflowCxV3ResponseMessage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookServiceDirectoryConfig(
    typing_extensions.TypedDict, total=False
):
    genericWebService: GoogleCloudDialogflowCxV3WebhookGenericWebService
    service: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettings(
    typing_extensions.TypedDict, total=False
):
    audioExportGcsDestination: GoogleCloudDialogflowCxV3beta1GcsDestination
    dtmfSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsDtmfSettings
    loggingSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsLoggingSettings
    speechSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsSpeechSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettingsDtmfSettings(
    typing_extensions.TypedDict, total=False
):
    enabled: bool
    endpointingTimeoutDuration: str
    finishDigit: str
    interdigitTimeoutDuration: str
    maxDigits: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettingsLoggingSettings(
    typing_extensions.TypedDict, total=False
):
    enableConsentBasedRedaction: bool
    enableInteractionLogging: bool
    enableStackdriverLogging: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AdvancedSettingsSpeechSettings(
    typing_extensions.TypedDict, total=False
):
    endpointerSensitivity: int
    models: dict[str, typing.Any]
    noSpeechTimeout: str
    useTimeoutBasedEndpointing: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AudioInput(
    typing_extensions.TypedDict, total=False
):
    audio: str
    config: GoogleCloudDialogflowCxV3beta1InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BargeInConfig(
    typing_extensions.TypedDict, total=False
):
    noBargeInDuration: str
    totalDuration: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    results: _list[GoogleCloudDialogflowCxV3beta1TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ContinuousTestResult(
    typing_extensions.TypedDict, total=False
):
    name: str
    result: typing_extensions.Literal[
        "AGGREGATED_TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"
    ]
    runTime: str
    testCaseResults: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationSignals(
    typing_extensions.TypedDict, total=False
):
    turnSignals: GoogleCloudDialogflowCxV3beta1TurnSignals

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationTurn(
    typing_extensions.TypedDict, total=False
):
    userInput: GoogleCloudDialogflowCxV3beta1ConversationTurnUserInput
    virtualAgentOutput: GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutput

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationTurnUserInput(
    typing_extensions.TypedDict, total=False
):
    enableSentimentAnalysis: bool
    injectedParameters: dict[str, typing.Any]
    input: GoogleCloudDialogflowCxV3beta1QueryInput
    isWebhookEnabled: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutput(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnection(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    dataStoreType: typing_extensions.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED", "PUBLIC_WEB", "UNSTRUCTURED", "STRUCTURED"
    ]
    documentProcessingMode: typing_extensions.Literal[
        "DOCUMENT_PROCESSING_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowMetadata(
    typing_extensions.TypedDict, total=False
):
    testErrors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowResponse(
    typing_extensions.TypedDict, total=False
):
    deployment: str
    environment: GoogleCloudDialogflowCxV3beta1Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DtmfInput(typing_extensions.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Environment(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    name: str
    testCasesConfig: GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfig
    updateTime: str
    versionConfigs: _list[GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfig]
    webhookConfig: GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentTestCasesConfig(
    typing_extensions.TypedDict, total=False
):
    enableContinuousRun: bool
    enablePredeploymentRun: bool
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfig(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentWebhookConfig(
    typing_extensions.TypedDict, total=False
):
    webhookOverrides: _list[GoogleCloudDialogflowCxV3beta1Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EventHandler(
    typing_extensions.TypedDict, total=False
):
    event: str
    name: str
    targetFlow: str
    targetPage: str
    targetPlaybook: str
    triggerFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EventInput(
    typing_extensions.TypedDict, total=False
):
    event: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str
    commitSha: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportFlowResponse(
    typing_extensions.TypedDict, total=False
):
    flowContent: str
    flowUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intentsContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Form(typing_extensions.TypedDict, total=False):
    parameters: _list[GoogleCloudDialogflowCxV3beta1FormParameter]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FormParameter(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    initialPromptFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment
    repromptEventHandlers: _list[GoogleCloudDialogflowCxV3beta1EventHandler]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Fulfillment(
    typing_extensions.TypedDict, total=False
):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
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
    typing_extensions.TypedDict, total=False
):
    cases: _list[GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCase(
    typing_extensions.TypedDict, total=False
):
    caseContent: _list[
        GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContent
    ]
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContent(
    typing_extensions.TypedDict, total=False
):
    additionalCases: GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCases
    message: GoogleCloudDialogflowCxV3beta1ResponseMessage

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentGeneratorSettings(
    typing_extensions.TypedDict, total=False
):
    generator: str
    inputParameters: dict[str, typing.Any]
    outputParameter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterAction(
    typing_extensions.TypedDict, total=False
):
    parameter: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    conflictingResources: (
        GoogleCloudDialogflowCxV3beta1ImportEntityTypesResponseConflictingResources
    )
    entityTypes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesResponseConflictingResources(
    typing_extensions.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    entityTypeDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportFlowResponse(
    typing_extensions.TypedDict, total=False
):
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    conflictingResources: (
        GoogleCloudDialogflowCxV3beta1ImportIntentsResponseConflictingResources
    )
    intents: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportIntentsResponseConflictingResources(
    typing_extensions.TypedDict, total=False
):
    entityDisplayNames: _list[str]
    intentDisplayNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestCaseError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InlineDestination(
    typing_extensions.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InputAudioConfig(
    typing_extensions.TypedDict, total=False
):
    audioEncoding: typing_extensions.Literal[
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
    modelVariant: typing_extensions.Literal[
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
class GoogleCloudDialogflowCxV3beta1Intent(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    isFallback: bool
    labels: dict[str, typing.Any]
    name: str
    parameters: _list[GoogleCloudDialogflowCxV3beta1IntentParameter]
    priority: int
    trainingPhrases: _list[GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentInput(
    typing_extensions.TypedDict, total=False
):
    intent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentParameter(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    id: str
    isList: bool
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    id: str
    parts: _list[GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePart]
    repeatCount: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    parameterId: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettings(
    typing_extensions.TypedDict, total=False
):
    dataStoreConnections: _list[GoogleCloudDialogflowCxV3beta1DataStoreConnection]
    enabled: bool
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LanguageInfo(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    inputLanguageCode: str
    resolvedLanguageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Page(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3beta1PageInfo(typing_extensions.TypedDict, total=False):
    currentPage: str
    displayName: str
    formInfo: GoogleCloudDialogflowCxV3beta1PageInfoFormInfo

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PageInfoFormInfo(
    typing_extensions.TypedDict, total=False
):
    parameterInfo: _list[GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    justCollected: bool
    required: bool
    state: typing_extensions.Literal[
        "PARAMETER_STATE_UNSPECIFIED", "EMPTY", "INVALID", "FILLED"
    ]
    value: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1QueryInput(
    typing_extensions.TypedDict, total=False
):
    audio: GoogleCloudDialogflowCxV3beta1AudioInput
    dtmf: GoogleCloudDialogflowCxV3beta1DtmfInput
    event: GoogleCloudDialogflowCxV3beta1EventInput
    intent: GoogleCloudDialogflowCxV3beta1IntentInput
    languageCode: str
    text: GoogleCloudDialogflowCxV3beta1TextInput
    toolCallResult: GoogleCloudDialogflowCxV3beta1ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessage(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageKnowledgeInfoCard(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff(
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio(
    typing_extensions.TypedDict, total=False
):
    segments: _list[GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audio: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    ssml: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audioUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageTelephonyTransferCall(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ResponseMessageText(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestResponse(
    typing_extensions.TypedDict, total=False
):
    continuousTestResult: GoogleCloudDialogflowCxV3beta1ContinuousTestResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunTestCaseMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunTestCaseResponse(
    typing_extensions.TypedDict, total=False
):
    result: GoogleCloudDialogflowCxV3beta1TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionInfo(
    typing_extensions.TypedDict, total=False
):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCase(typing_extensions.TypedDict, total=False):
    creationTime: str
    displayName: str
    lastTestResult: GoogleCloudDialogflowCxV3beta1TestCaseResult
    name: str
    notes: str
    tags: _list[str]
    testCaseConversationTurns: _list[GoogleCloudDialogflowCxV3beta1ConversationTurn]
    testConfig: GoogleCloudDialogflowCxV3beta1TestConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCaseError(
    typing_extensions.TypedDict, total=False
):
    status: GoogleRpcStatus
    testCase: GoogleCloudDialogflowCxV3beta1TestCase

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCaseResult(
    typing_extensions.TypedDict, total=False
):
    conversationTurns: _list[GoogleCloudDialogflowCxV3beta1ConversationTurn]
    environment: str
    name: str
    testResult: typing_extensions.Literal["TEST_RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestConfig(
    typing_extensions.TypedDict, total=False
):
    flow: str
    page: str
    trackingParameters: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestError(typing_extensions.TypedDict, total=False):
    status: GoogleRpcStatus
    testCase: str
    testTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestRunDifference(
    typing_extensions.TypedDict, total=False
):
    description: str
    type: typing_extensions.Literal[
        "DIFF_TYPE_UNSPECIFIED", "INTENT", "PAGE", "PARAMETERS", "UTTERANCE", "FLOW"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TextInput(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolCall(typing_extensions.TypedDict, total=False):
    action: str
    inputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolCallResult(
    typing_extensions.TypedDict, total=False
):
    action: str
    error: GoogleCloudDialogflowCxV3beta1ToolCallResultError
    outputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolCallResultError(
    typing_extensions.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRoute(
    typing_extensions.TypedDict, total=False
):
    condition: str
    description: str
    intent: str
    name: str
    targetFlow: str
    targetPage: str
    triggerFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TurnSignals(
    typing_extensions.TypedDict, total=False
):
    agentEscalated: bool
    dtmfUsed: bool
    failureReasons: _list[
        typing_extensions.Literal[
            "FAILURE_REASON_UNSPECIFIED", "FAILED_INTENT", "FAILED_WEBHOOK"
        ]
    ]
    noMatch: bool
    noUserInput: bool
    reachedEndPage: bool
    sentimentMagnitude: float
    sentimentScore: float
    userEscalated: bool
    webhookStatuses: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Webhook(typing_extensions.TypedDict, total=False):
    disabled: bool
    displayName: str
    genericWebService: GoogleCloudDialogflowCxV3beta1WebhookGenericWebService
    name: str
    serviceDirectory: GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfig
    timeout: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookGenericWebService(
    typing_extensions.TypedDict, total=False
):
    allowedCaCerts: _list[str]
    httpMethod: typing_extensions.Literal[
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
    serviceAgentAuth: typing_extensions.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "NONE", "ID_TOKEN", "ACCESS_TOKEN"
    ]
    uri: str
    username: str
    webhookType: typing_extensions.Literal[
        "WEBHOOK_TYPE_UNSPECIFIED", "STANDARD", "FLEXIBLE"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceOAuthConfig(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    scopes: _list[str]
    secretVersionForClientSecret: str
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookGenericWebServiceSecretVersionHeaderValue(
    typing_extensions.TypedDict, total=False
):
    secretVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    tag: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    lastMatchedIntent: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValue(
    typing_extensions.TypedDict, total=False
):
    originalValue: str
    resolvedValue: typing.Any

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookRequestSentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    mergeBehavior: typing_extensions.Literal[
        "MERGE_BEHAVIOR_UNSPECIFIED", "APPEND", "REPLACE"
    ]
    messages: _list[GoogleCloudDialogflowCxV3beta1ResponseMessage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfig(
    typing_extensions.TypedDict, total=False
):
    genericWebService: GoogleCloudDialogflowCxV3beta1WebhookGenericWebService
    service: str

@typing.type_check_only
class GoogleCloudDialogflowV2Agent(typing_extensions.TypedDict, total=False):
    apiVersion: typing_extensions.Literal[
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
    matchMode: typing_extensions.Literal[
        "MATCH_MODE_UNSPECIFIED", "MATCH_MODE_HYBRID", "MATCH_MODE_ML_ONLY"
    ]
    parent: str
    supportedLanguageCodes: _list[str]
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED", "TIER_STANDARD", "TIER_ENTERPRISE", "TIER_ENTERPRISE_PLUS"
    ]
    timeZone: str

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantFeedback(
    typing_extensions.TypedDict, total=False
):
    answerRelevance: typing_extensions.Literal[
        "ANSWER_RELEVANCE_UNSPECIFIED", "IRRELEVANT", "RELEVANT"
    ]
    documentCorrectness: typing_extensions.Literal[
        "DOCUMENT_CORRECTNESS_UNSPECIFIED", "INCORRECT", "CORRECT"
    ]
    documentEfficiency: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    answerCopied: bool
    clickedUris: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantFeedbackKnowledgeSearchFeedback(
    typing_extensions.TypedDict, total=False
):
    answerCopied: bool
    clickedUris: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantFeedbackSummarizationFeedback(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    submitTime: str
    summaryText: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2AgentAssistantRecord(
    typing_extensions.TypedDict, total=False
):
    articleSuggestionAnswer: GoogleCloudDialogflowV2ArticleAnswer
    dialogflowAssistAnswer: GoogleCloudDialogflowV2DialogflowAssistAnswer
    faqAnswer: GoogleCloudDialogflowV2FaqAnswer

@typing.type_check_only
class GoogleCloudDialogflowV2AnalyzeContentRequest(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudDialogflowV2AnalyzeContentResponse(
    typing_extensions.TypedDict, total=False
):
    automatedAgentReply: GoogleCloudDialogflowV2AutomatedAgentReply
    dtmfParameters: GoogleCloudDialogflowV2DtmfParameters
    endUserSuggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]
    humanAgentSuggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]
    message: GoogleCloudDialogflowV2Message
    replyAudio: GoogleCloudDialogflowV2OutputAudio
    replyText: str

@typing.type_check_only
class GoogleCloudDialogflowV2AnnotatedMessagePart(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    formattedValue: typing.Any
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2AnswerFeedback(typing_extensions.TypedDict, total=False):
    agentAssistantDetailFeedback: GoogleCloudDialogflowV2AgentAssistantFeedback
    clickTime: str
    clicked: bool
    correctnessLevel: typing_extensions.Literal[
        "CORRECTNESS_LEVEL_UNSPECIFIED",
        "NOT_CORRECT",
        "PARTIALLY_CORRECT",
        "FULLY_CORRECT",
    ]
    displayTime: str
    displayed: bool

@typing.type_check_only
class GoogleCloudDialogflowV2AnswerRecord(typing_extensions.TypedDict, total=False):
    agentAssistantRecord: GoogleCloudDialogflowV2AgentAssistantRecord
    answerFeedback: GoogleCloudDialogflowV2AnswerFeedback
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2ArticleAnswer(typing_extensions.TypedDict, total=False):
    answerRecord: str
    confidence: float
    metadata: dict[str, typing.Any]
    snippets: _list[str]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ArticleSuggestionModelMetadata(
    typing_extensions.TypedDict, total=False
):
    trainingModelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "SMART_REPLY_DUAL_ENCODER_MODEL",
        "SMART_REPLY_BERT_MODEL",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2AssistQueryParameters(
    typing_extensions.TypedDict, total=False
):
    documentsMetadataFilters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2AudioInput(typing_extensions.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowV2InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowV2AutomatedAgentConfig(
    typing_extensions.TypedDict, total=False
):
    agent: str
    sessionTtl: str

@typing.type_check_only
class GoogleCloudDialogflowV2AutomatedAgentReply(
    typing_extensions.TypedDict, total=False
):
    allowCancellation: bool
    automatedAgentReplyType: typing_extensions.Literal[
        "AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED", "PARTIAL", "FINAL"
    ]
    cxCurrentPage: str
    detectIntentResponse: GoogleCloudDialogflowV2DetectIntentResponse

@typing.type_check_only
class GoogleCloudDialogflowV2BatchCreateEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchDeleteEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entityValues: _list[str]
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchDeleteEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    entityTypeNames: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2BatchDeleteIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    intents: _list[GoogleCloudDialogflowV2Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    languageCode: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    entityTypeBatchInline: GoogleCloudDialogflowV2EntityTypeBatch
    entityTypeBatchUri: str
    languageCode: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    intentBatchInline: GoogleCloudDialogflowV2IntentBatch
    intentBatchUri: str
    intentView: typing_extensions.Literal["INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"]
    languageCode: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowV2BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: _list[GoogleCloudDialogflowV2Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2ClearSuggestionFeatureConfigOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2Context(typing_extensions.TypedDict, total=False):
    lifespanCount: int
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2Conversation(typing_extensions.TypedDict, total=False):
    conversationProfile: str
    conversationStage: typing_extensions.Literal[
        "CONVERSATION_STAGE_UNSPECIFIED", "VIRTUAL_AGENT_STAGE", "HUMAN_ASSIST_STAGE"
    ]
    endTime: str
    ingestedContextReferences: dict[str, typing.Any]
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETED"
    ]
    name: str
    phoneNumber: GoogleCloudDialogflowV2ConversationPhoneNumber
    startTime: str
    telephonyConnectionInfo: GoogleCloudDialogflowV2ConversationTelephonyConnectionInfo

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationContext(
    typing_extensions.TypedDict, total=False
):
    messageEntries: _list[GoogleCloudDialogflowV2MessageEntry]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationContextReference(
    typing_extensions.TypedDict, total=False
):
    contextContents: _list[
        GoogleCloudDialogflowV2ConversationContextReferenceContextContent
    ]
    createTime: str
    languageCode: str
    updateMode: typing_extensions.Literal[
        "UPDATE_MODE_UNSPECIFIED", "APPEND", "OVERWRITE"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationContextReferenceContextContent(
    typing_extensions.TypedDict, total=False
):
    content: str
    contentFormat: typing_extensions.Literal[
        "CONTENT_FORMAT_UNSPECIFIED", "JSON", "PLAIN_TEXT"
    ]
    ingestionTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationDataset(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudDialogflowV2ConversationEvent(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    errorStatus: GoogleRpcStatus
    newMessagePayload: GoogleCloudDialogflowV2Message
    newRecognitionResultPayload: GoogleCloudDialogflowV2StreamingRecognitionResult
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CONVERSATION_STARTED",
        "CONVERSATION_FINISHED",
        "HUMAN_INTERVENTION_NEEDED",
        "NEW_MESSAGE",
        "NEW_RECOGNITION_RESULT",
        "UNRECOVERABLE_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationInfo(typing_extensions.TypedDict, total=False):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationModel(
    typing_extensions.TypedDict, total=False
):
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
    state: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2ConversationModelEvaluation(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    evaluationConfig: GoogleCloudDialogflowV2EvaluationConfig
    name: str
    rawHumanEvalTemplateCsv: str
    smartReplyMetrics: GoogleCloudDialogflowV2SmartReplyMetrics

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationPhoneNumber(
    typing_extensions.TypedDict, total=False
):
    countryCode: int
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationProfile(
    typing_extensions.TypedDict, total=False
):
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
    sttConfig: GoogleCloudDialogflowV2SpeechToTextConfig
    timeZone: str
    ttsConfig: GoogleCloudDialogflowV2SynthesizeSpeechConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationTelephonyConnectionInfo(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationTelephonyConnectionInfoSipHeader(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationDataset: str

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    conversationModelEvaluation: str
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "RUNNING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationModelEvaluationRequest(
    typing_extensions.TypedDict, total=False
):
    conversationModelEvaluation: GoogleCloudDialogflowV2ConversationModelEvaluation

@typing.type_check_only
class GoogleCloudDialogflowV2CreateConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "CANCELLING",
        "TRAINING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2CustomPronunciationParams(
    typing_extensions.TypedDict, total=False
):
    phoneticEncoding: typing_extensions.Literal[
        "PHONETIC_ENCODING_UNSPECIFIED",
        "PHONETIC_ENCODING_IPA",
        "PHONETIC_ENCODING_X_SAMPA",
    ]
    phrase: str
    pronunciation: str

@typing.type_check_only
class GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2DeleteConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2DeployConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2DeployConversationModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2DetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    inputAudio: str
    outputAudioConfig: GoogleCloudDialogflowV2OutputAudioConfig
    outputAudioConfigMask: str
    queryInput: GoogleCloudDialogflowV2QueryInput
    queryParams: GoogleCloudDialogflowV2QueryParameters

@typing.type_check_only
class GoogleCloudDialogflowV2DetectIntentResponse(
    typing_extensions.TypedDict, total=False
):
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowV2OutputAudioConfig
    queryResult: GoogleCloudDialogflowV2QueryResult
    responseId: str
    webhookStatus: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDialogflowV2DialogflowAssistAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    intentSuggestion: GoogleCloudDialogflowV2IntentSuggestion
    queryResult: GoogleCloudDialogflowV2QueryResult

@typing.type_check_only
class GoogleCloudDialogflowV2Document(typing_extensions.TypedDict, total=False):
    contentUri: str
    displayName: str
    enableAutoReload: bool
    knowledgeTypes: _list[
        typing_extensions.Literal[
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "RELOADING", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2DocumentReloadStatus(
    typing_extensions.TypedDict, total=False
):
    status: GoogleRpcStatus
    time: str

@typing.type_check_only
class GoogleCloudDialogflowV2DtmfParameters(typing_extensions.TypedDict, total=False):
    acceptsDtmfInput: bool

@typing.type_check_only
class GoogleCloudDialogflowV2EncryptionSpec(typing_extensions.TypedDict, total=False):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2EntityType(typing_extensions.TypedDict, total=False):
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2EntityTypeBatch(typing_extensions.TypedDict, total=False):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2EntityTypeEntity(typing_extensions.TypedDict, total=False):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2Environment(typing_extensions.TypedDict, total=False):
    agentVersion: str
    description: str
    fulfillment: GoogleCloudDialogflowV2Fulfillment
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STOPPED", "LOADING", "RUNNING"
    ]
    textToSpeechSettings: GoogleCloudDialogflowV2TextToSpeechSettings
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2EnvironmentHistory(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleCloudDialogflowV2EnvironmentHistoryEntry]
    nextPageToken: str
    parent: str

@typing.type_check_only
class GoogleCloudDialogflowV2EnvironmentHistoryEntry(
    typing_extensions.TypedDict, total=False
):
    agentVersion: str
    createTime: str
    description: str

@typing.type_check_only
class GoogleCloudDialogflowV2EvaluationConfig(typing_extensions.TypedDict, total=False):
    datasets: _list[GoogleCloudDialogflowV2InputDataset]
    smartComposeConfig: GoogleCloudDialogflowV2EvaluationConfigSmartComposeConfig
    smartReplyConfig: GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfig

@typing.type_check_only
class GoogleCloudDialogflowV2EvaluationConfigSmartComposeConfig(
    typing_extensions.TypedDict, total=False
):
    allowlistDocument: str
    maxResultCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfig(
    typing_extensions.TypedDict, total=False
):
    allowlistDocument: str
    maxResultCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2EventInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2ExportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ExportDocumentRequest(
    typing_extensions.TypedDict, total=False
):
    exportFullContent: bool
    gcsDestination: GoogleCloudDialogflowV2GcsDestination
    smartMessagingPartialUpdate: bool

@typing.type_check_only
class GoogleCloudDialogflowV2ExportOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    exportedGcsDestination: GoogleCloudDialogflowV2GcsDestination

@typing.type_check_only
class GoogleCloudDialogflowV2FaqAnswer(typing_extensions.TypedDict, total=False):
    answer: str
    answerRecord: str
    confidence: float
    metadata: dict[str, typing.Any]
    question: str
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2FewShotExample(typing_extensions.TypedDict, total=False):
    conversationContext: GoogleCloudDialogflowV2ConversationContext
    extraInfo: dict[str, typing.Any]
    output: GoogleCloudDialogflowV2GeneratorSuggestion
    summarizationSectionList: GoogleCloudDialogflowV2SummarizationSectionList

@typing.type_check_only
class GoogleCloudDialogflowV2FreeFormContext(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2FreeFormSuggestion(
    typing_extensions.TypedDict, total=False
):
    response: str

@typing.type_check_only
class GoogleCloudDialogflowV2Fulfillment(typing_extensions.TypedDict, total=False):
    displayName: str
    enabled: bool
    features: _list[GoogleCloudDialogflowV2FulfillmentFeature]
    genericWebService: GoogleCloudDialogflowV2FulfillmentGenericWebService
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2FulfillmentFeature(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SMALLTALK"]

@typing.type_check_only
class GoogleCloudDialogflowV2FulfillmentGenericWebService(
    typing_extensions.TypedDict, total=False
):
    isCloudFunction: bool
    password: str
    requestHeaders: dict[str, typing.Any]
    uri: str
    username: str

@typing.type_check_only
class GoogleCloudDialogflowV2GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2GcsSources(typing_extensions.TypedDict, total=False):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSuggestionRequest(
    typing_extensions.TypedDict, total=False
):
    contextReferences: dict[str, typing.Any]
    conversationContext: GoogleCloudDialogflowV2ConversationContext
    generator: GoogleCloudDialogflowV2Generator
    generatorName: str
    securitySettings: str
    triggerEvents: _list[
        typing_extensions.Literal[
            "TRIGGER_EVENT_UNSPECIFIED",
            "END_OF_UTTERANCE",
            "MANUAL_CALL",
            "CUSTOMER_MESSAGE",
            "AGENT_MESSAGE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSuggestionResponse(
    typing_extensions.TypedDict, total=False
):
    generatorSuggestion: GoogleCloudDialogflowV2GeneratorSuggestion

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryRequest(
    typing_extensions.TypedDict, total=False
):
    conversationProfile: GoogleCloudDialogflowV2ConversationProfile
    latestMessage: str
    maxContextSize: int
    statelessConversation: (
        GoogleCloudDialogflowV2GenerateStatelessSummaryRequestMinimalConversation
    )

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryRequestMinimalConversation(
    typing_extensions.TypedDict, total=False
):
    messages: _list[GoogleCloudDialogflowV2Message]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    summary: GoogleCloudDialogflowV2GenerateStatelessSummaryResponseSummary

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateStatelessSummaryResponseSummary(
    typing_extensions.TypedDict, total=False
):
    baselineModelVersion: str
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateSuggestionsRequest(
    typing_extensions.TypedDict, total=False
):
    latestMessage: str
    triggerEvents: _list[
        typing_extensions.Literal[
            "TRIGGER_EVENT_UNSPECIFIED",
            "END_OF_UTTERANCE",
            "MANUAL_CALL",
            "CUSTOMER_MESSAGE",
            "AGENT_MESSAGE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    generatorSuggestionAnswers: _list[
        GoogleCloudDialogflowV2GenerateSuggestionsResponseGeneratorSuggestionAnswer
    ]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2GenerateSuggestionsResponseGeneratorSuggestionAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    generatorSuggestion: GoogleCloudDialogflowV2GeneratorSuggestion
    sourceGenerator: str

@typing.type_check_only
class GoogleCloudDialogflowV2Generator(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    freeFormContext: GoogleCloudDialogflowV2FreeFormContext
    inferenceParameter: GoogleCloudDialogflowV2InferenceParameter
    name: str
    publishedModel: str
    summarizationContext: GoogleCloudDialogflowV2SummarizationContext
    tools: _list[str]
    triggerEvent: typing_extensions.Literal[
        "TRIGGER_EVENT_UNSPECIFIED",
        "END_OF_UTTERANCE",
        "MANUAL_CALL",
        "CUSTOMER_MESSAGE",
        "AGENT_MESSAGE",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorSuggestion(
    typing_extensions.TypedDict, total=False
):
    freeFormSuggestion: GoogleCloudDialogflowV2FreeFormSuggestion
    summarySuggestion: GoogleCloudDialogflowV2SummarySuggestion
    toolCallInfo: _list[GoogleCloudDialogflowV2GeneratorSuggestionToolCallInfo]

@typing.type_check_only
class GoogleCloudDialogflowV2GeneratorSuggestionToolCallInfo(
    typing_extensions.TypedDict, total=False
):
    toolCall: GoogleCloudDialogflowV2ToolCall
    toolCallResult: GoogleCloudDialogflowV2ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfig(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    baselineModelVersion: str
    model: str

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfig(
    typing_extensions.TypedDict, total=False
):
    recentSentencesCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigMessageAnalysisConfig(
    typing_extensions.TypedDict, total=False
):
    enableEntityExtraction: bool
    enableSentimentAnalysis: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionConfig(
    typing_extensions.TypedDict, total=False
):
    disableHighLatencyFeaturesSyncDelivery: bool
    featureConfigs: _list[
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig
    ]
    generators: _list[str]
    groupSuggestionResponses: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig(
    typing_extensions.TypedDict, total=False
):
    conversationModelConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfig
    )
    conversationProcessConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfig
    )
    disableAgentQueryLogging: bool
    enableConversationAugmentedQuery: bool
    enableEventBasedSuggestion: bool
    enableQuerySuggestionOnly: bool
    enableQuerySuggestionWhenNoAnswer: bool
    queryConfig: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfig
    suggestionFeature: GoogleCloudDialogflowV2SuggestionFeature
    suggestionTriggerSettings: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionTriggerSettings
    )

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfig(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    dropHandoffMessages: bool
    dropIvrMessages: bool
    dropVirtualAgentMessages: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySource(
    typing_extensions.TypedDict, total=False
):
    agent: str
    humanAgentSideConfig: GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySourceHumanAgentSideConfig

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySourceHumanAgentSideConfig(
    typing_extensions.TypedDict, total=False
):
    agent: str

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigDocumentQuerySource(
    typing_extensions.TypedDict, total=False
):
    documents: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigKnowledgeBaseQuerySource(
    typing_extensions.TypedDict, total=False
):
    knowledgeBases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfigSections(
    typing_extensions.TypedDict, total=False
):
    sectionTypes: _list[
        typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    noSmalltalk: bool
    onlyEndUser: bool

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantEvent(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    participant: str
    suggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentHandoffConfig(
    typing_extensions.TypedDict, total=False
):
    livePersonConfig: GoogleCloudDialogflowV2HumanAgentHandoffConfigLivePersonConfig
    salesforceLiveAgentConfig: (
        GoogleCloudDialogflowV2HumanAgentHandoffConfigSalesforceLiveAgentConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentHandoffConfigLivePersonConfig(
    typing_extensions.TypedDict, total=False
):
    accountNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentHandoffConfigSalesforceLiveAgentConfig(
    typing_extensions.TypedDict, total=False
):
    buttonId: str
    deploymentId: str
    endpointDomain: str
    organizationId: str

@typing.type_check_only
class GoogleCloudDialogflowV2ImportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2ImportConversationDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationDataset: str
    createTime: str
    partialFailures: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowV2ImportConversationDataOperationResponse(
    typing_extensions.TypedDict, total=False
):
    conversationDataset: str
    importCount: int

@typing.type_check_only
class GoogleCloudDialogflowV2ImportConversationDataRequest(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudDialogflowV2InputConfig

@typing.type_check_only
class GoogleCloudDialogflowV2ImportDocumentTemplate(
    typing_extensions.TypedDict, total=False
):
    knowledgeTypes: _list[
        typing_extensions.Literal[
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
class GoogleCloudDialogflowV2ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    documentTemplate: GoogleCloudDialogflowV2ImportDocumentTemplate
    gcsSource: GoogleCloudDialogflowV2GcsSources
    importGcsCustomMetadata: bool

@typing.type_check_only
class GoogleCloudDialogflowV2ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    warnings: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowV2InferenceParameter(
    typing_extensions.TypedDict, total=False
):
    maxOutputTokens: int
    temperature: float
    topK: int
    topP: float

@typing.type_check_only
class GoogleCloudDialogflowV2IngestContextReferencesRequest(
    typing_extensions.TypedDict, total=False
):
    contextReferences: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2IngestContextReferencesResponse(
    typing_extensions.TypedDict, total=False
):
    ingestedContextReferences: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2InitializeEncryptionSpecMetadata(
    typing_extensions.TypedDict, total=False
):
    request: GoogleCloudDialogflowV2InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudDialogflowV2InitializeEncryptionSpecRequest(
    typing_extensions.TypedDict, total=False
):
    encryptionSpec: GoogleCloudDialogflowV2EncryptionSpec

@typing.type_check_only
class GoogleCloudDialogflowV2InputAudioConfig(typing_extensions.TypedDict, total=False):
    audioEncoding: typing_extensions.Literal[
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
    enableWordInfo: bool
    languageCode: str
    model: str
    modelVariant: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudDialogflowV2GcsSources

@typing.type_check_only
class GoogleCloudDialogflowV2InputDataset(typing_extensions.TypedDict, total=False):
    dataset: str

@typing.type_check_only
class GoogleCloudDialogflowV2Intent(typing_extensions.TypedDict, total=False):
    action: str
    defaultResponsePlatforms: _list[
        typing_extensions.Literal[
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
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentBatch(typing_extensions.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowV2Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    followupIntentName: str
    parentFollowupIntentName: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessage(typing_extensions.TypedDict, total=False):
    basicCard: GoogleCloudDialogflowV2IntentMessageBasicCard
    browseCarouselCard: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard
    card: GoogleCloudDialogflowV2IntentMessageCard
    carouselSelect: GoogleCloudDialogflowV2IntentMessageCarouselSelect
    image: GoogleCloudDialogflowV2IntentMessageImage
    linkOutSuggestion: GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion
    listSelect: GoogleCloudDialogflowV2IntentMessageListSelect
    mediaContent: GoogleCloudDialogflowV2IntentMessageMediaContent
    payload: dict[str, typing.Any]
    platform: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    buttons: _list[GoogleCloudDialogflowV2IntentMessageBasicCardButton]
    formattedText: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard(
    typing_extensions.TypedDict, total=False
):
    imageDisplayOptions: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    description: str
    footer: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    openUriAction: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    url: str
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    buttons: _list[GoogleCloudDialogflowV2IntentMessageCardButton]
    imageUri: str
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    postback: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: _list[GoogleCloudDialogflowV2IntentMessageCarouselSelectItem]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    header: str
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    accessibilityText: str
    imageUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    destinationName: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    items: _list[GoogleCloudDialogflowV2IntentMessageListSelectItem]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaObjects: _list[
        GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject
    ]
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    contentUrl: str
    description: str
    icon: GoogleCloudDialogflowV2IntentMessageImage
    largeImage: GoogleCloudDialogflowV2IntentMessageImage
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    quickReplies: _list[str]
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    key: str
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    displayText: str
    ssml: str
    textToSpeech: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: _list[GoogleCloudDialogflowV2IntentMessageSimpleResponse]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: _list[GoogleCloudDialogflowV2IntentMessageSuggestion]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    buttons: _list[GoogleCloudDialogflowV2IntentMessageBasicCardButton]
    columnProperties: _list[GoogleCloudDialogflowV2IntentMessageColumnProperties]
    image: GoogleCloudDialogflowV2IntentMessageImage
    rows: _list[GoogleCloudDialogflowV2IntentMessageTableCardRow]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    cells: _list[GoogleCloudDialogflowV2IntentMessageTableCardCell]
    dividerAfter: bool

@typing.type_check_only
class GoogleCloudDialogflowV2IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentParameter(typing_extensions.TypedDict, total=False):
    defaultValue: str
    displayName: str
    entityTypeDisplayName: str
    isList: bool
    mandatory: bool
    name: str
    prompts: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentSuggestion(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    intentV2: str

@typing.type_check_only
class GoogleCloudDialogflowV2IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    name: str
    parts: _list[GoogleCloudDialogflowV2IntentTrainingPhrasePart]
    timesAddedCount: int
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]

@typing.type_check_only
class GoogleCloudDialogflowV2IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    alias: str
    entityType: str
    text: str
    userDefined: bool

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    suggestedQuery: GoogleCloudDialogflowV2KnowledgeAssistAnswerSuggestedQuery
    suggestedQueryAnswer: GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswer

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswer(
    typing_extensions.TypedDict, total=False
):
    answerText: str
    faqSource: GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerFaqSource
    generativeSource: (
        GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerFaqSource(
    typing_extensions.TypedDict, total=False
):
    question: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource(
    typing_extensions.TypedDict, total=False
):
    snippets: _list[
        GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet(
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeAssistAnswerSuggestedQuery(
    typing_extensions.TypedDict, total=False
):
    queryText: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeBase(typing_extensions.TypedDict, total=False):
    displayName: str
    languageCode: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    doneTime: str
    exportOperationMetadata: GoogleCloudDialogflowV2ExportOperationMetadata
    knowledgeBase: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

@typing.type_check_only
class GoogleCloudDialogflowV2ListAnswerRecordsResponse(
    typing_extensions.TypedDict, total=False
):
    answerRecords: _list[GoogleCloudDialogflowV2AnswerRecord]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListContextsResponse(
    typing_extensions.TypedDict, total=False
):
    contexts: _list[GoogleCloudDialogflowV2Context]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationDatasetsResponse(
    typing_extensions.TypedDict, total=False
):
    conversationDatasets: _list[GoogleCloudDialogflowV2ConversationDataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationModelEvaluationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversationModelEvaluations: _list[
        GoogleCloudDialogflowV2ConversationModelEvaluation
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationModelsResponse(
    typing_extensions.TypedDict, total=False
):
    conversationModels: _list[GoogleCloudDialogflowV2ConversationModel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationProfilesResponse(
    typing_extensions.TypedDict, total=False
):
    conversationProfiles: _list[GoogleCloudDialogflowV2ConversationProfile]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversations: _list[GoogleCloudDialogflowV2Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDialogflowV2Document]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListEnvironmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowV2Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListGeneratorsResponse(
    typing_extensions.TypedDict, total=False
):
    generators: _list[GoogleCloudDialogflowV2Generator]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: _list[GoogleCloudDialogflowV2Intent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListKnowledgeBasesResponse(
    typing_extensions.TypedDict, total=False
):
    knowledgeBases: _list[GoogleCloudDialogflowV2KnowledgeBase]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListMessagesResponse(
    typing_extensions.TypedDict, total=False
):
    messages: _list[GoogleCloudDialogflowV2Message]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2ListParticipantsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    participants: _list[GoogleCloudDialogflowV2Participant]

@typing.type_check_only
class GoogleCloudDialogflowV2ListSessionEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: _list[GoogleCloudDialogflowV2SessionEntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2ListVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    versions: _list[GoogleCloudDialogflowV2Version]

@typing.type_check_only
class GoogleCloudDialogflowV2LoggingConfig(typing_extensions.TypedDict, total=False):
    enableStackdriverLogging: bool

@typing.type_check_only
class GoogleCloudDialogflowV2Message(typing_extensions.TypedDict, total=False):
    content: str
    createTime: str
    languageCode: str
    messageAnnotation: GoogleCloudDialogflowV2MessageAnnotation
    name: str
    participant: str
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    sendTime: str
    sentimentAnalysis: GoogleCloudDialogflowV2SentimentAnalysisResult

@typing.type_check_only
class GoogleCloudDialogflowV2MessageAnnotation(
    typing_extensions.TypedDict, total=False
):
    containEntities: bool
    parts: _list[GoogleCloudDialogflowV2AnnotatedMessagePart]

@typing.type_check_only
class GoogleCloudDialogflowV2MessageEntry(typing_extensions.TypedDict, total=False):
    createTime: str
    languageCode: str
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2NotificationConfig(
    typing_extensions.TypedDict, total=False
):
    messageFormat: typing_extensions.Literal[
        "MESSAGE_FORMAT_UNSPECIFIED", "PROTO", "JSON"
    ]
    topic: str

@typing.type_check_only
class GoogleCloudDialogflowV2OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    payload: dict[str, typing.Any]
    source: str
    version: str

@typing.type_check_only
class GoogleCloudDialogflowV2OutputAudio(typing_extensions.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowV2OutputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowV2OutputAudioConfig(
    typing_extensions.TypedDict, total=False
):
    audioEncoding: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2Participant(typing_extensions.TypedDict, total=False):
    documentsMetadataFilters: dict[str, typing.Any]
    name: str
    obfuscatedExternalUserId: str
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    sipRecordingMediaLabel: str

@typing.type_check_only
class GoogleCloudDialogflowV2QueryInput(typing_extensions.TypedDict, total=False):
    audioConfig: GoogleCloudDialogflowV2InputAudioConfig
    event: GoogleCloudDialogflowV2EventInput
    text: GoogleCloudDialogflowV2TextInput

@typing.type_check_only
class GoogleCloudDialogflowV2QueryParameters(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDialogflowV2QueryResult(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDialogflowV2ReloadDocumentRequest(
    typing_extensions.TypedDict, total=False
):
    contentUri: str
    importGcsCustomMetadata: bool
    smartMessagingPartialUpdate: bool

@typing.type_check_only
class GoogleCloudDialogflowV2RestoreAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchAgentsResponse(
    typing_extensions.TypedDict, total=False
):
    agents: _list[GoogleCloudDialogflowV2Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeAnswer(
    typing_extensions.TypedDict, total=False
):
    answer: str
    answerRecord: str
    answerSources: _list[GoogleCloudDialogflowV2SearchKnowledgeAnswerAnswerSource]
    answerType: typing_extensions.Literal[
        "ANSWER_TYPE_UNSPECIFIED", "FAQ", "GENERATIVE", "INTENT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeAnswerAnswerSource(
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]
    snippet: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequest(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    conversationProfile: str
    endUserMetadata: dict[str, typing.Any]
    exactSearch: bool
    latestMessage: str
    parent: str
    query: GoogleCloudDialogflowV2TextInput
    querySource: typing_extensions.Literal[
        "QUERY_SOURCE_UNSPECIFIED", "AGENT_QUERY", "SUGGESTED_QUERY"
    ]
    searchConfig: GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfig
    sessionId: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfig(
    typing_extensions.TypedDict, total=False
):
    boostSpecs: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecs
    ]
    filterSpecs: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigFilterSpecs
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecs(
    typing_extensions.TypedDict, total=False
):
    dataStores: _list[str]
    spec: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigBoostSpecsBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeRequestSearchConfigFilterSpecs(
    typing_extensions.TypedDict, total=False
):
    dataStores: _list[str]
    filter: str

@typing.type_check_only
class GoogleCloudDialogflowV2SearchKnowledgeResponse(
    typing_extensions.TypedDict, total=False
):
    answers: _list[GoogleCloudDialogflowV2SearchKnowledgeAnswer]
    rewrittenQuery: str

@typing.type_check_only
class GoogleCloudDialogflowV2Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowV2SentimentAnalysisRequestConfig(
    typing_extensions.TypedDict, total=False
):
    analyzeQueryTextSentiment: bool

@typing.type_check_only
class GoogleCloudDialogflowV2SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2Sentiment

@typing.type_check_only
class GoogleCloudDialogflowV2SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDialogflowV2EntityTypeEntity]
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2SetSuggestionFeatureConfigOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureConfig: (
        GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyAnswer(typing_extensions.TypedDict, total=False):
    answerRecord: str
    confidence: float
    reply: str

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyMetrics(
    typing_extensions.TypedDict, total=False
):
    allowlistCoverage: float
    conversationCount: str
    topNMetrics: _list[GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics]

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics(
    typing_extensions.TypedDict, total=False
):
    n: int
    recall: float

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyModelMetadata(
    typing_extensions.TypedDict, total=False
):
    trainingModelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "SMART_REPLY_DUAL_ENCODER_MODEL",
        "SMART_REPLY_BERT_MODEL",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SpeechContext(typing_extensions.TypedDict, total=False):
    boost: float
    phrases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2SpeechToTextConfig(
    typing_extensions.TypedDict, total=False
):
    audioEncoding: typing_extensions.Literal[
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
    speechModelVariant: typing_extensions.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]
    useTimeoutBasedEndpointing: bool

@typing.type_check_only
class GoogleCloudDialogflowV2SpeechWordInfo(typing_extensions.TypedDict, total=False):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudDialogflowV2StreamingRecognitionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    isFinal: bool
    languageCode: str
    messageType: typing_extensions.Literal[
        "MESSAGE_TYPE_UNSPECIFIED", "TRANSCRIPT", "END_OF_SINGLE_UTTERANCE"
    ]
    speechEndOffset: str
    speechWordInfo: _list[GoogleCloudDialogflowV2SpeechWordInfo]
    transcript: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestArticlesRequest(
    typing_extensions.TypedDict, total=False
):
    assistQueryParams: GoogleCloudDialogflowV2AssistQueryParameters
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestArticlesResponse(
    typing_extensions.TypedDict, total=False
):
    articleAnswers: _list[GoogleCloudDialogflowV2ArticleAnswer]
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestConversationSummaryRequest(
    typing_extensions.TypedDict, total=False
):
    assistQueryParams: GoogleCloudDialogflowV2AssistQueryParameters
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestConversationSummaryResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    summary: GoogleCloudDialogflowV2SuggestConversationSummaryResponseSummary

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestConversationSummaryResponseSummary(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    baselineModelVersion: str
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestFaqAnswersRequest(
    typing_extensions.TypedDict, total=False
):
    assistQueryParams: GoogleCloudDialogflowV2AssistQueryParameters
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestFaqAnswersResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    faqAnswers: _list[GoogleCloudDialogflowV2FaqAnswer]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestKnowledgeAssistRequest(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    previousSuggestedQuery: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestKnowledgeAssistResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    knowledgeAssistAnswer: GoogleCloudDialogflowV2KnowledgeAssistAnswer
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestSmartRepliesRequest(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    currentTextInput: GoogleCloudDialogflowV2TextInput
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestSmartRepliesResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    smartReplyAnswers: _list[GoogleCloudDialogflowV2SmartReplyAnswer]

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionFeature(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "ARTICLE_SUGGESTION",
        "FAQ",
        "SMART_REPLY",
        "CONVERSATION_SUMMARIZATION",
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionInput(typing_extensions.TypedDict, total=False):
    answerRecord: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionResult(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    generateSuggestionsResponse: GoogleCloudDialogflowV2GenerateSuggestionsResponse
    suggestArticlesResponse: GoogleCloudDialogflowV2SuggestArticlesResponse
    suggestFaqAnswersResponse: GoogleCloudDialogflowV2SuggestFaqAnswersResponse
    suggestKnowledgeAssistResponse: (
        GoogleCloudDialogflowV2SuggestKnowledgeAssistResponse
    )
    suggestSmartRepliesResponse: GoogleCloudDialogflowV2SuggestSmartRepliesResponse

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationContext(
    typing_extensions.TypedDict, total=False
):
    fewShotExamples: _list[GoogleCloudDialogflowV2FewShotExample]
    outputLanguageCode: str
    summarizationSections: _list[GoogleCloudDialogflowV2SummarizationSection]
    version: str

@typing.type_check_only
class GoogleCloudDialogflowV2SummarizationSection(
    typing_extensions.TypedDict, total=False
):
    definition: str
    key: str
    type: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2SummarizationSectionList(
    typing_extensions.TypedDict, total=False
):
    summarizationSections: _list[GoogleCloudDialogflowV2SummarizationSection]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarySuggestion(
    typing_extensions.TypedDict, total=False
):
    summarySections: _list[GoogleCloudDialogflowV2SummarySuggestionSummarySection]

@typing.type_check_only
class GoogleCloudDialogflowV2SummarySuggestionSummarySection(
    typing_extensions.TypedDict, total=False
):
    section: str
    summary: str

@typing.type_check_only
class GoogleCloudDialogflowV2SynthesizeSpeechConfig(
    typing_extensions.TypedDict, total=False
):
    effectsProfileId: _list[str]
    pitch: float
    pronunciations: _list[GoogleCloudDialogflowV2CustomPronunciationParams]
    speakingRate: float
    voice: GoogleCloudDialogflowV2VoiceSelectionParams
    volumeGainDb: float

@typing.type_check_only
class GoogleCloudDialogflowV2TextInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2TextToSpeechSettings(
    typing_extensions.TypedDict, total=False
):
    enableTextToSpeech: bool
    outputAudioEncoding: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2ToolCall(typing_extensions.TypedDict, total=False):
    action: str
    createTime: str
    inputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolCallResult(typing_extensions.TypedDict, total=False):
    action: str
    content: str
    createTime: str
    error: GoogleCloudDialogflowV2ToolCallResultError
    rawContent: str
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowV2ToolCallResultError(
    typing_extensions.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowV2TrainAgentRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2UndeployConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str
    doneTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2UndeployConversationModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2ValidationError(typing_extensions.TypedDict, total=False):
    entries: _list[str]
    errorMessage: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "CRITICAL"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2ValidationResult(typing_extensions.TypedDict, total=False):
    validationErrors: _list[GoogleCloudDialogflowV2ValidationError]

@typing.type_check_only
class GoogleCloudDialogflowV2Version(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    status: typing_extensions.Literal[
        "VERSION_STATUS_UNSPECIFIED", "IN_PROGRESS", "READY", "FAILED"
    ]
    versionNumber: int

@typing.type_check_only
class GoogleCloudDialogflowV2VoiceSelectionParams(
    typing_extensions.TypedDict, total=False
):
    name: str
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED",
        "SSML_VOICE_GENDER_MALE",
        "SSML_VOICE_GENDER_FEMALE",
        "SSML_VOICE_GENDER_NEUTRAL",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2WebhookRequest(typing_extensions.TypedDict, total=False):
    originalDetectIntentRequest: GoogleCloudDialogflowV2OriginalDetectIntentRequest
    queryResult: GoogleCloudDialogflowV2QueryResult
    responseId: str
    session: str

@typing.type_check_only
class GoogleCloudDialogflowV2WebhookResponse(typing_extensions.TypedDict, total=False):
    followupEventInput: GoogleCloudDialogflowV2EventInput
    fulfillmentMessages: _list[GoogleCloudDialogflowV2IntentMessage]
    fulfillmentText: str
    outputContexts: _list[GoogleCloudDialogflowV2Context]
    payload: dict[str, typing.Any]
    sessionEntityTypes: _list[GoogleCloudDialogflowV2SessionEntityType]
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AnnotatedMessagePart(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    formattedValue: typing.Any
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ArticleAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    metadata: dict[str, typing.Any]
    snippets: _list[str]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowV2beta1EntityType]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: _list[GoogleCloudDialogflowV2beta1Intent]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2beta1Context(typing_extensions.TypedDict, total=False):
    lifespanCount: int
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ConversationEvent(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    errorStatus: GoogleRpcStatus
    newMessagePayload: GoogleCloudDialogflowV2beta1Message
    newRecognitionResultPayload: GoogleCloudDialogflowV2beta1StreamingRecognitionResult
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CONVERSATION_STARTED",
        "CONVERSATION_FINISHED",
        "HUMAN_INTERVENTION_NEEDED",
        "NEW_MESSAGE",
        "NEW_RECOGNITION_RESULT",
        "UNRECOVERABLE_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1DialogflowAssistAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    intentSuggestion: GoogleCloudDialogflowV2beta1IntentSuggestion
    queryResult: GoogleCloudDialogflowV2beta1QueryResult

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EncryptionSpec(
    typing_extensions.TypedDict, total=False
):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EntityType(typing_extensions.TypedDict, total=False):
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EntityTypeEntity(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EventInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ExportOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    exportedGcsDestination: GoogleCloudDialogflowV2beta1GcsDestination

@typing.type_check_only
class GoogleCloudDialogflowV2beta1FaqAnswer(typing_extensions.TypedDict, total=False):
    answer: str
    answerRecord: str
    confidence: float
    metadata: dict[str, typing.Any]
    question: str
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1FreeFormSuggestion(
    typing_extensions.TypedDict, total=False
):
    response: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GenerateSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    generatorSuggestionAnswers: _list[
        GoogleCloudDialogflowV2beta1GenerateSuggestionsResponseGeneratorSuggestionAnswer
    ]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GenerateSuggestionsResponseGeneratorSuggestionAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    generatorSuggestion: GoogleCloudDialogflowV2beta1GeneratorSuggestion
    sourceGenerator: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GeneratorSuggestion(
    typing_extensions.TypedDict, total=False
):
    freeFormSuggestion: GoogleCloudDialogflowV2beta1FreeFormSuggestion
    summarySuggestion: GoogleCloudDialogflowV2beta1SummarySuggestion
    toolCallInfo: _list[GoogleCloudDialogflowV2beta1GeneratorSuggestionToolCallInfo]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1GeneratorSuggestionToolCallInfo(
    typing_extensions.TypedDict, total=False
):
    toolCall: GoogleCloudDialogflowV2beta1ToolCall
    toolCallResult: GoogleCloudDialogflowV2beta1ToolCallResult

@typing.type_check_only
class GoogleCloudDialogflowV2beta1HumanAgentAssistantEvent(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    participant: str
    suggestionResults: _list[GoogleCloudDialogflowV2beta1SuggestionResult]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    warnings: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1InitializeEncryptionSpecMetadata(
    typing_extensions.TypedDict, total=False
):
    request: GoogleCloudDialogflowV2beta1InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudDialogflowV2beta1InitializeEncryptionSpecRequest(
    typing_extensions.TypedDict, total=False
):
    encryptionSpec: GoogleCloudDialogflowV2beta1EncryptionSpec

@typing.type_check_only
class GoogleCloudDialogflowV2beta1Intent(typing_extensions.TypedDict, total=False):
    action: str
    defaultResponsePlatforms: _list[
        typing_extensions.Literal[
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
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    followupIntentName: str
    parentFollowupIntentName: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessage(
    typing_extensions.TypedDict, total=False
):
    basicCard: GoogleCloudDialogflowV2beta1IntentMessageBasicCard
    browseCarouselCard: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard
    card: GoogleCloudDialogflowV2beta1IntentMessageCard
    carouselSelect: GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    linkOutSuggestion: GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion
    listSelect: GoogleCloudDialogflowV2beta1IntentMessageListSelect
    mediaContent: GoogleCloudDialogflowV2beta1IntentMessageMediaContent
    payload: dict[str, typing.Any]
    platform: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2beta1IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    buttons: _list[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    formattedText: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard(
    typing_extensions.TypedDict, total=False
):
    imageDisplayOptions: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    description: str
    footer: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    url: str
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    buttons: _list[GoogleCloudDialogflowV2beta1IntentMessageCardButton]
    imageUri: str
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    postback: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: _list[GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    header: str
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    accessibilityText: str
    imageUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    destinationName: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    items: _list[GoogleCloudDialogflowV2beta1IntentMessageListSelectItem]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaObjects: _list[
        GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject
    ]
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    contentUrl: str
    description: str
    icon: GoogleCloudDialogflowV2beta1IntentMessageImage
    largeImage: GoogleCloudDialogflowV2beta1IntentMessageImage
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    quickReplies: _list[str]
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent(
    typing_extensions.TypedDict, total=False
):
    description: str
    media: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia
    suggestions: _list[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia(
    typing_extensions.TypedDict, total=False
):
    fileUri: str
    height: typing_extensions.Literal["HEIGHT_UNSPECIFIED", "SHORT", "MEDIUM", "TALL"]
    thumbnailUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard(
    typing_extensions.TypedDict, total=False
):
    cardContents: _list[GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent]
    cardWidth: typing_extensions.Literal["CARD_WIDTH_UNSPECIFIED", "SMALL", "MEDIUM"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard(
    typing_extensions.TypedDict, total=False
):
    cardContent: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent
    cardOrientation: typing_extensions.Literal[
        "CARD_ORIENTATION_UNSPECIFIED", "HORIZONTAL", "VERTICAL"
    ]
    thumbnailImageAlignment: typing_extensions.Literal[
        "THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT"
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction(
    typing_extensions.TypedDict, total=False
):
    dial: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial
    openUrl: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri
    postbackData: str
    shareLocation: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply(
    typing_extensions.TypedDict, total=False
):
    postbackData: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion(
    typing_extensions.TypedDict, total=False
):
    action: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction
    reply: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageRbmText(
    typing_extensions.TypedDict, total=False
):
    rbmSuggestion: _list[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    key: str
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    displayText: str
    ssml: str
    textToSpeech: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: _list[GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: _list[GoogleCloudDialogflowV2beta1IntentMessageSuggestion]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    buttons: _list[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    columnProperties: _list[GoogleCloudDialogflowV2beta1IntentMessageColumnProperties]
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    rows: _list[GoogleCloudDialogflowV2beta1IntentMessageTableCardRow]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    cells: _list[GoogleCloudDialogflowV2beta1IntentMessageTableCardCell]
    dividerAfter: bool

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio(
    typing_extensions.TypedDict, total=False
):
    audioUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech(
    typing_extensions.TypedDict, total=False
):
    ssml: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentParameter(
    typing_extensions.TypedDict, total=False
):
    defaultValue: str
    displayName: str
    entityTypeDisplayName: str
    isList: bool
    mandatory: bool
    name: str
    prompts: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentSuggestion(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    intentV2: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    name: str
    parts: _list[GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart]
    timesAddedCount: int
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    alias: str
    entityType: str
    text: str
    userDefined: bool

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAnswers(
    typing_extensions.TypedDict, total=False
):
    answers: _list[GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer(
    typing_extensions.TypedDict, total=False
):
    answer: str
    faqQuestion: str
    matchConfidence: float
    matchConfidenceLevel: typing_extensions.Literal[
        "MATCH_CONFIDENCE_LEVEL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    source: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    suggestedQuery: GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerSuggestedQuery
    suggestedQueryAnswer: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswer
    )

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswer(
    typing_extensions.TypedDict, total=False
):
    answerText: str
    faqSource: GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerFaqSource
    generativeSource: (
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource
    )

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerFaqSource(
    typing_extensions.TypedDict, total=False
):
    question: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSource(
    typing_extensions.TypedDict, total=False
):
    snippets: _list[
        GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerKnowledgeAnswerGenerativeSourceSnippet(
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]
    text: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeAssistAnswerSuggestedQuery(
    typing_extensions.TypedDict, total=False
):
    queryText: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    doneTime: str
    exportOperationMetadata: GoogleCloudDialogflowV2beta1ExportOperationMetadata
    knowledgeBase: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1Message(typing_extensions.TypedDict, total=False):
    content: str
    createTime: str
    languageCode: str
    messageAnnotation: GoogleCloudDialogflowV2beta1MessageAnnotation
    name: str
    participant: str
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    responseMessages: _list[GoogleCloudDialogflowV2beta1ResponseMessage]
    sendTime: str
    sentimentAnalysis: GoogleCloudDialogflowV2beta1SentimentAnalysisResult

@typing.type_check_only
class GoogleCloudDialogflowV2beta1MessageAnnotation(
    typing_extensions.TypedDict, total=False
):
    containEntities: bool
    parts: _list[GoogleCloudDialogflowV2beta1AnnotatedMessagePart]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    payload: dict[str, typing.Any]
    source: str
    version: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1QueryResult(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDialogflowV2beta1ResponseMessage(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageLiveAgentHandoff(
    typing_extensions.TypedDict, total=False
):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageMixedAudio(
    typing_extensions.TypedDict, total=False
):
    segments: _list[GoogleCloudDialogflowV2beta1ResponseMessageMixedAudioSegment]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageMixedAudioSegment(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audio: str
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageTelephonyTransferCall(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str
    sipUri: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ResponseMessageText(
    typing_extensions.TypedDict, total=False
):
    text: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2beta1Sentiment

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationProfile: str
    createTime: str
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    suggestionFeatureType: typing_extensions.Literal[
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
class GoogleCloudDialogflowV2beta1SmartReplyAnswer(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    confidence: float
    reply: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SpeechWordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1StreamingRecognitionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    dtmfDigits: GoogleCloudDialogflowV2beta1TelephonyDtmfEvents
    isFinal: bool
    languageCode: str
    messageType: typing_extensions.Literal[
        "MESSAGE_TYPE_UNSPECIFIED",
        "TRANSCRIPT",
        "END_OF_SINGLE_UTTERANCE",
        "DTMF_DIGITS",
        "PARTIAL_DTMF_DIGITS",
    ]
    speechEndOffset: str
    speechWordInfo: _list[GoogleCloudDialogflowV2beta1SpeechWordInfo]
    stability: float
    transcript: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestArticlesResponse(
    typing_extensions.TypedDict, total=False
):
    articleAnswers: _list[GoogleCloudDialogflowV2beta1ArticleAnswer]
    contextSize: int
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestDialogflowAssistsResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    dialogflowAssistAnswers: _list[GoogleCloudDialogflowV2beta1DialogflowAssistAnswer]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    faqAnswers: _list[GoogleCloudDialogflowV2beta1FaqAnswer]
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestKnowledgeAssistResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    knowledgeAssistAnswer: GoogleCloudDialogflowV2beta1KnowledgeAssistAnswer
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    smartReplyAnswers: _list[GoogleCloudDialogflowV2beta1SmartReplyAnswer]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestionResult(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudDialogflowV2beta1SummarySuggestion(
    typing_extensions.TypedDict, total=False
):
    summarySections: _list[GoogleCloudDialogflowV2beta1SummarySuggestionSummarySection]

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SummarySuggestionSummarySection(
    typing_extensions.TypedDict, total=False
):
    section: str
    summary: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1TelephonyDtmfEvents(
    typing_extensions.TypedDict, total=False
):
    dtmfEvents: _list[
        typing_extensions.Literal[
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
class GoogleCloudDialogflowV2beta1ToolCall(typing_extensions.TypedDict, total=False):
    action: str
    createTime: str
    inputParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ToolCallResult(
    typing_extensions.TypedDict, total=False
):
    action: str
    content: str
    createTime: str
    error: GoogleCloudDialogflowV2beta1ToolCallResultError
    rawContent: str
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ToolCallResultError(
    typing_extensions.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
    alternativeQueryResults: _list[GoogleCloudDialogflowV2beta1QueryResult]
    originalDetectIntentRequest: GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest
    queryResult: GoogleCloudDialogflowV2beta1QueryResult
    responseId: str
    session: str

@typing.type_check_only
class GoogleCloudDialogflowV2beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudDialogflowV3alpha1ConversationSignals(
    typing_extensions.TypedDict, total=False
):
    turnSignals: GoogleCloudDialogflowV3alpha1TurnSignals

@typing.type_check_only
class GoogleCloudDialogflowV3alpha1TurnSignals(
    typing_extensions.TypedDict, total=False
):
    agentEscalated: bool
    dtmfUsed: bool
    failureReasons: _list[
        typing_extensions.Literal[
            "FAILURE_REASON_UNSPECIFIED", "FAILED_INTENT", "FAILED_WEBHOOK"
        ]
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
class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float
