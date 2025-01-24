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
    tokenEndpoint: str

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
class GoogleCloudDialogflowCxV3beta1Action(typing_extensions.TypedDict, total=False):
    agentUtterance: GoogleCloudDialogflowCxV3beta1AgentUtterance
    flowInvocation: GoogleCloudDialogflowCxV3beta1FlowInvocation
    playbookInvocation: GoogleCloudDialogflowCxV3beta1PlaybookInvocation
    toolUse: GoogleCloudDialogflowCxV3beta1ToolUse
    userUtterance: GoogleCloudDialogflowCxV3beta1UserUtterance

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
class GoogleCloudDialogflowCxV3beta1Agent(typing_extensions.TypedDict, total=False):
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
    typing_extensions.TypedDict, total=False
):
    enableAnswerFeedback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentClientCertificateSettings(
    typing_extensions.TypedDict, total=False
):
    passphrase: str
    privateKey: str
    sslCertificate: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentGenAppBuilderSettings(
    typing_extensions.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettings(
    typing_extensions.TypedDict, total=False
):
    githubSettings: (
        GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGithubSettings
    )

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentGitIntegrationSettingsGithubSettings(
    typing_extensions.TypedDict, total=False
):
    accessToken: str
    branches: _list[str]
    displayName: str
    repositoryUri: str
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentPersonalizationSettings(
    typing_extensions.TypedDict, total=False
):
    defaultEndUserMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentUtterance(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentValidationResult(
    typing_extensions.TypedDict, total=False
):
    flowValidationResults: _list[GoogleCloudDialogflowCxV3beta1FlowValidationResult]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AnswerFeedback(
    typing_extensions.TypedDict, total=False
):
    customRating: str
    rating: typing_extensions.Literal["RATING_UNSPECIFIED", "THUMBS_UP", "THUMBS_DOWN"]
    ratingReason: GoogleCloudDialogflowCxV3beta1AnswerFeedbackRatingReason

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AnswerFeedbackRatingReason(
    typing_extensions.TypedDict, total=False
):
    feedback: str
    reasonLabels: _list[str]

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
class GoogleCloudDialogflowCxV3beta1BatchDeleteTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    environment: str
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BatchRunTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    results: _list[GoogleCloudDialogflowCxV3beta1TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BigQueryExportSettings(
    typing_extensions.TypedDict, total=False
):
    bigqueryTable: str
    enabled: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpec(typing_extensions.TypedDict, total=False):
    conditionBoostSpecs: _list[
        GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: (
        GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpec
    )
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1BoostSpecs(
    typing_extensions.TypedDict, total=False
):
    dataStores: _list[str]
    spec: _list[GoogleCloudDialogflowCxV3beta1BoostSpec]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CalculateCoverageResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str
    intentCoverage: GoogleCloudDialogflowCxV3beta1IntentCoverage
    routeGroupCoverage: GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverage
    transitionCoverage: GoogleCloudDialogflowCxV3beta1TransitionCoverage

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Changelog(typing_extensions.TypedDict, total=False):
    action: str
    createTime: str
    displayName: str
    languageCode: str
    name: str
    resource: str
    type: str
    userEmail: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CompareVersionsRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    targetVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CompareVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    baseVersionContentJson: str
    compareTime: str
    targetVersionContentJson: str

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
class GoogleCloudDialogflowCxV3beta1Conversation(
    typing_extensions.TypedDict, total=False
):
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
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "AUDIO", "TEXT", "UNDETERMINED"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationInteraction(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    intentDisplayName: str
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationInteractionStepMetrics(
    typing_extensions.TypedDict, total=False
):
    latency: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationMetrics(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    audioCount: int
    dtmfCount: int
    eventCount: int
    intentCount: int
    textCount: int

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

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignals(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsAnswerPart(
    typing_extensions.TypedDict, total=False
):
    supportingIndices: _list[int]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsCitedSnippet(
    typing_extensions.TypedDict, total=False
):
    searchSnippet: GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSearchSnippet
    snippetIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsGroundingSignals(
    typing_extensions.TypedDict, total=False
):
    decision: typing_extensions.Literal[
        "GROUNDING_DECISION_UNSPECIFIED",
        "ACCEPTED_BY_GROUNDING",
        "REJECTED_BY_GROUNDING",
    ]
    score: typing_extensions.Literal[
        "GROUNDING_SCORE_BUCKET_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsRewriterModelCallSignals(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSafetySignals(
    typing_extensions.TypedDict, total=False
):
    bannedPhraseMatch: typing_extensions.Literal[
        "BANNED_PHRASE_MATCH_UNSPECIFIED",
        "BANNED_PHRASE_MATCH_NONE",
        "BANNED_PHRASE_MATCH_QUERY",
        "BANNED_PHRASE_MATCH_RESPONSE",
    ]
    decision: typing_extensions.Literal[
        "SAFETY_DECISION_UNSPECIFIED",
        "ACCEPTED_BY_SAFETY_CHECK",
        "REJECTED_BY_SAFETY_CHECK",
    ]
    matchedBannedPhrase: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DataStoreConnectionSignalsSearchSnippet(
    typing_extensions.TypedDict, total=False
):
    documentTitle: str
    documentUri: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowMetadata(
    typing_extensions.TypedDict, total=False
):
    testErrors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowRequest(
    typing_extensions.TypedDict, total=False
):
    flowVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeployFlowResponse(
    typing_extensions.TypedDict, total=False
):
    deployment: str
    environment: GoogleCloudDialogflowCxV3beta1Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Deployment(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    flowVersion: str
    name: str
    result: GoogleCloudDialogflowCxV3beta1DeploymentResult
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeploymentResult(
    typing_extensions.TypedDict, total=False
):
    deploymentTestResults: _list[str]
    experiment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    queryInput: GoogleCloudDialogflowCxV3beta1QueryInput
    queryParams: GoogleCloudDialogflowCxV3beta1QueryParameters
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DetectIntentResponse(
    typing_extensions.TypedDict, total=False
):
    allowCancellation: bool
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3beta1QueryResult
    responseId: str
    responseType: typing_extensions.Literal[
        "RESPONSE_TYPE_UNSPECIFIED", "PARTIAL", "FINAL"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DtmfInput(typing_extensions.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityType(
    typing_extensions.TypedDict, total=False
):
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowCxV3beta1EntityTypeEntity]
    excludedPhrases: _list[GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase]
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    name: str
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityTypeEntity(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase(
    typing_extensions.TypedDict, total=False
):
    value: str

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
class GoogleCloudDialogflowCxV3beta1Example(typing_extensions.TypedDict, total=False):
    actions: _list[GoogleCloudDialogflowCxV3beta1Action]
    conversationState: typing_extensions.Literal[
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
class GoogleCloudDialogflowCxV3beta1Experiment(
    typing_extensions.TypedDict, total=False
):
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "DRAFT", "RUNNING", "DONE", "ROLLOUT_FAILED"
    ]
    variantsHistory: _list[GoogleCloudDialogflowCxV3beta1VariantsHistory]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentDefinition(
    typing_extensions.TypedDict, total=False
):
    condition: str
    versionVariants: GoogleCloudDialogflowCxV3beta1VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResult(
    typing_extensions.TypedDict, total=False
):
    lastUpdateTime: str
    versionMetrics: _list[GoogleCloudDialogflowCxV3beta1ExperimentResultVersionMetrics]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval(
    typing_extensions.TypedDict, total=False
):
    confidenceLevel: float
    lowerBound: float
    ratio: float
    upperBound: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResultMetric(
    typing_extensions.TypedDict, total=False
):
    confidenceInterval: GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval
    count: float
    countType: typing_extensions.Literal[
        "COUNT_TYPE_UNSPECIFIED",
        "TOTAL_NO_MATCH_COUNT",
        "TOTAL_TURN_COUNT",
        "AVERAGE_TURN_COUNT",
    ]
    ratio: float
    type: typing_extensions.Literal[
        "METRIC_UNSPECIFIED",
        "CONTAINED_SESSION_NO_CALLBACK_RATE",
        "LIVE_AGENT_HANDOFF_RATE",
        "CALLBACK_SESSION_RATE",
        "ABANDONED_SESSION_RATE",
        "SESSION_END_RATE",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentResultVersionMetrics(
    typing_extensions.TypedDict, total=False
):
    metrics: _list[GoogleCloudDialogflowCxV3beta1ExperimentResultMetric]
    sessionCount: int
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON_PACKAGE"
    ]
    environment: str
    gitDestination: GoogleCloudDialogflowCxV3beta1ExportAgentRequestGitDestination
    includeBigqueryExportSettings: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportAgentRequestGitDestination(
    typing_extensions.TypedDict, total=False
):
    commitMessage: str
    trackingBranch: str

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
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON_PACKAGE"
    ]
    entityTypes: _list[str]
    entityTypesContentInline: bool
    entityTypesUri: str
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportFlowRequest(
    typing_extensions.TypedDict, total=False
):
    flowUri: str
    includeReferencedFlows: bool

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
class GoogleCloudDialogflowCxV3beta1ExportIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON", "CSV"
    ]
    intents: _list[str]
    intentsContentInline: bool
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intentsContent: GoogleCloudDialogflowCxV3beta1InlineDestination
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportPlaybookRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    playbookUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    filter: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExportToolsRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    tools: _list[str]
    toolsContentInline: bool
    toolsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FilterSpecs(
    typing_extensions.TypedDict, total=False
):
    dataStores: _list[str]
    filter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Flow(typing_extensions.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    description: str
    displayName: str
    eventHandlers: _list[GoogleCloudDialogflowCxV3beta1EventHandler]
    knowledgeConnectorSettings: GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettings
    locked: bool
    multiLanguageSettings: GoogleCloudDialogflowCxV3beta1FlowMultiLanguageSettings
    name: str
    nluSettings: GoogleCloudDialogflowCxV3beta1NluSettings
    transitionRouteGroups: _list[str]
    transitionRoutes: _list[GoogleCloudDialogflowCxV3beta1TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowImportStrategy(
    typing_extensions.TypedDict, total=False
):
    globalImportStrategy: typing_extensions.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowInvocation(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    flow: str
    flowState: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    enableMultiLanguageDetection: bool
    supportedResponseLanguageCodes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowValidationResult(
    typing_extensions.TypedDict, total=False
):
    name: str
    updateTime: str
    validationMessages: _list[GoogleCloudDialogflowCxV3beta1ValidationMessage]

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
class GoogleCloudDialogflowCxV3beta1FulfillIntentRequest(
    typing_extensions.TypedDict, total=False
):
    match: GoogleCloudDialogflowCxV3beta1Match
    matchIntentRequest: GoogleCloudDialogflowCxV3beta1MatchIntentRequest
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillIntentResponse(
    typing_extensions.TypedDict, total=False
):
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3beta1QueryResult
    responseId: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Fulfillment(
    typing_extensions.TypedDict, total=False
):
    advancedSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettings
    conditionalCases: _list[GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCases]
    enableGenerativeFallback: bool
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
class GoogleCloudDialogflowCxV3beta1GenerativeInfo(
    typing_extensions.TypedDict, total=False
):
    actionTracingInfo: GoogleCloudDialogflowCxV3beta1Example
    currentPlaybooks: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettings(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    promptTemplates: _list[
        GoogleCloudDialogflowCxV3beta1GenerativeSettingsFallbackSettingsPromptTemplate
    ]
    selectedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettingsFallbackSettingsPromptTemplate(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    frozen: bool
    promptText: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettingsKnowledgeConnectorSettings(
    typing_extensions.TypedDict, total=False
):
    agent: str
    agentIdentity: str
    agentScope: str
    business: str
    businessDescription: str
    disableDataStoreFallback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Generator(typing_extensions.TypedDict, total=False):
    displayName: str
    llmModelSettings: GoogleCloudDialogflowCxV3beta1LlmModelSettings
    modelParameter: GoogleCloudDialogflowCxV3beta1GeneratorModelParameter
    name: str
    placeholders: _list[GoogleCloudDialogflowCxV3beta1GeneratorPlaceholder]
    promptText: GoogleCloudDialogflowCxV3beta1Phrase

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GeneratorModelParameter(
    typing_extensions.TypedDict, total=False
):
    maxDecodeSteps: int
    temperature: float
    topK: int
    topP: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GeneratorPlaceholder(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3beta1InlineSource
    entityTypesUri: str
    mergeOption: typing_extensions.Literal[
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
class GoogleCloudDialogflowCxV3beta1ImportFlowRequest(
    typing_extensions.TypedDict, total=False
):
    flowContent: str
    flowImportStrategy: GoogleCloudDialogflowCxV3beta1FlowImportStrategy
    flowUri: str
    importOption: typing_extensions.Literal[
        "IMPORT_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"
    ]

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
class GoogleCloudDialogflowCxV3beta1ImportIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    intentsContent: GoogleCloudDialogflowCxV3beta1InlineSource
    intentsUri: str
    mergeOption: typing_extensions.Literal[
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
class GoogleCloudDialogflowCxV3beta1ImportPlaybookRequest(
    typing_extensions.TypedDict, total=False
):
    importStrategy: GoogleCloudDialogflowCxV3beta1PlaybookImportStrategy
    playbookContent: str
    playbookUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestCaseError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ImportTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    content: str
    gcsUri: str

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
class GoogleCloudDialogflowCxV3beta1InlineSchema(
    typing_extensions.TypedDict, total=False
):
    items: GoogleCloudDialogflowCxV3beta1TypeSchema
    type: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "STRING", "NUMBER", "BOOLEAN", "ARRAY"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1InlineSource(
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
class GoogleCloudDialogflowCxV3beta1IntentCoverage(
    typing_extensions.TypedDict, total=False
):
    coverageScore: float
    intents: _list[GoogleCloudDialogflowCxV3beta1IntentCoverageIntent]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentCoverageIntent(
    typing_extensions.TypedDict, total=False
):
    covered: bool
    intent: str

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
class GoogleCloudDialogflowCxV3beta1ListAgentsResponse(
    typing_extensions.TypedDict, total=False
):
    agents: _list[GoogleCloudDialogflowCxV3beta1Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListChangelogsResponse(
    typing_extensions.TypedDict, total=False
):
    changelogs: _list[GoogleCloudDialogflowCxV3beta1Changelog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponse(
    typing_extensions.TypedDict, total=False
):
    continuousTestResults: _list[GoogleCloudDialogflowCxV3beta1ContinuousTestResult]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversations: _list[GoogleCloudDialogflowCxV3beta1Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListDeploymentsResponse(
    typing_extensions.TypedDict, total=False
):
    deployments: _list[GoogleCloudDialogflowCxV3beta1Deployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowCxV3beta1EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowCxV3beta1Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListExamplesResponse(
    typing_extensions.TypedDict, total=False
):
    examples: _list[GoogleCloudDialogflowCxV3beta1Example]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListExperimentsResponse(
    typing_extensions.TypedDict, total=False
):
    experiments: _list[GoogleCloudDialogflowCxV3beta1Experiment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListFlowsResponse(
    typing_extensions.TypedDict, total=False
):
    flows: _list[GoogleCloudDialogflowCxV3beta1Flow]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListGeneratorsResponse(
    typing_extensions.TypedDict, total=False
):
    generators: _list[GoogleCloudDialogflowCxV3beta1Generator]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: _list[GoogleCloudDialogflowCxV3beta1Intent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPagesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pages: _list[GoogleCloudDialogflowCxV3beta1Page]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    playbookVersions: _list[GoogleCloudDialogflowCxV3beta1PlaybookVersion]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPlaybooksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    playbooks: _list[GoogleCloudDialogflowCxV3beta1Playbook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securitySettings: _list[GoogleCloudDialogflowCxV3beta1SecuritySettings]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3beta1SessionEntityType]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    testCaseResults: _list[GoogleCloudDialogflowCxV3beta1TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    testCases: _list[GoogleCloudDialogflowCxV3beta1TestCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListToolsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tools: _list[GoogleCloudDialogflowCxV3beta1Tool]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    transitionRouteGroups: _list[GoogleCloudDialogflowCxV3beta1TransitionRouteGroup]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    versions: _list[GoogleCloudDialogflowCxV3beta1Version]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListWebhooksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    webhooks: _list[GoogleCloudDialogflowCxV3beta1Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LlmModelSettings(
    typing_extensions.TypedDict, total=False
):
    model: str
    promptText: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LoadVersionRequest(
    typing_extensions.TypedDict, total=False
):
    allowOverrideAgentResources: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponse(
    typing_extensions.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowCxV3beta1Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Match(typing_extensions.TypedDict, total=False):
    confidence: float
    event: str
    intent: GoogleCloudDialogflowCxV3beta1Intent
    matchType: typing_extensions.Literal[
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
class GoogleCloudDialogflowCxV3beta1MatchIntentRequest(
    typing_extensions.TypedDict, total=False
):
    persistParameterChanges: bool
    queryInput: GoogleCloudDialogflowCxV3beta1QueryInput
    queryParams: GoogleCloudDialogflowCxV3beta1QueryParameters

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1MatchIntentResponse(
    typing_extensions.TypedDict, total=False
):
    currentPage: GoogleCloudDialogflowCxV3beta1Page
    matches: _list[GoogleCloudDialogflowCxV3beta1Match]
    text: str
    transcript: str
    triggerEvent: str
    triggerIntent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1NluSettings(
    typing_extensions.TypedDict, total=False
):
    classificationThreshold: float
    modelTrainingMode: typing_extensions.Literal[
        "MODEL_TRAINING_MODE_UNSPECIFIED",
        "MODEL_TRAINING_MODE_AUTOMATIC",
        "MODEL_TRAINING_MODE_MANUAL",
    ]
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED", "MODEL_TYPE_STANDARD", "MODEL_TYPE_ADVANCED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1OutputAudioConfig(
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
    synthesizeSpeechConfig: GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig

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
class GoogleCloudDialogflowCxV3beta1ParameterDefinition(
    typing_extensions.TypedDict, total=False
):
    description: str
    name: str
    type: typing_extensions.Literal[
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
class GoogleCloudDialogflowCxV3beta1Phrase(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Playbook(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    goal: str
    inputParameterDefinitions: _list[GoogleCloudDialogflowCxV3beta1ParameterDefinition]
    instruction: GoogleCloudDialogflowCxV3beta1PlaybookInstruction
    llmModelSettings: GoogleCloudDialogflowCxV3beta1LlmModelSettings
    name: str
    outputParameterDefinitions: _list[GoogleCloudDialogflowCxV3beta1ParameterDefinition]
    referencedFlows: _list[str]
    referencedPlaybooks: _list[str]
    referencedTools: _list[str]
    speechSettings: GoogleCloudDialogflowCxV3beta1AdvancedSettingsSpeechSettings
    tokenCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookImportStrategy(
    typing_extensions.TypedDict, total=False
):
    mainPlaybookImportStrategy: typing_extensions.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]
    nestedResourceImportStrategy: typing_extensions.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]
    toolImportStrategy: typing_extensions.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookInput(
    typing_extensions.TypedDict, total=False
):
    actionParameters: dict[str, typing.Any]
    precedingConversationSummary: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookInstruction(
    typing_extensions.TypedDict, total=False
):
    guidelines: str
    steps: _list[GoogleCloudDialogflowCxV3beta1PlaybookStep]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookInvocation(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    playbook: str
    playbookInput: GoogleCloudDialogflowCxV3beta1PlaybookInput
    playbookOutput: GoogleCloudDialogflowCxV3beta1PlaybookOutput
    playbookState: typing_extensions.Literal[
        "OUTPUT_STATE_UNSPECIFIED",
        "OUTPUT_STATE_OK",
        "OUTPUT_STATE_CANCELLED",
        "OUTPUT_STATE_FAILED",
        "OUTPUT_STATE_ESCALATED",
        "OUTPUT_STATE_PENDING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookOutput(
    typing_extensions.TypedDict, total=False
):
    actionParameters: dict[str, typing.Any]
    executionSummary: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookStep(
    typing_extensions.TypedDict, total=False
):
    steps: _list[GoogleCloudDialogflowCxV3beta1PlaybookStep]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookVersion(
    typing_extensions.TypedDict, total=False
):
    description: str
    examples: _list[GoogleCloudDialogflowCxV3beta1Example]
    name: str
    playbook: GoogleCloudDialogflowCxV3beta1Playbook
    updateTime: str

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
class GoogleCloudDialogflowCxV3beta1QueryParameters(
    typing_extensions.TypedDict, total=False
):
    analyzeQueryTextSentiment: bool
    channel: str
    currentPage: str
    currentPlaybook: str
    disableWebhook: bool
    endUserMetadata: dict[str, typing.Any]
    flowVersions: _list[str]
    geoLocation: GoogleTypeLatLng
    llmModelSettings: GoogleCloudDialogflowCxV3beta1LlmModelSettings
    parameters: dict[str, typing.Any]
    payload: dict[str, typing.Any]
    populateDataStoreConnectionSignals: bool
    searchConfig: GoogleCloudDialogflowCxV3beta1SearchConfig
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3beta1SessionEntityType]
    sessionTtl: str
    timeZone: str
    webhookHeaders: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1QueryResult(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudDialogflowCxV3beta1ResourceName(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str

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
class GoogleCloudDialogflowCxV3beta1RestoreAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str
    gitSource: GoogleCloudDialogflowCxV3beta1RestoreAgentRequestGitSource
    restoreOption: typing_extensions.Literal[
        "RESTORE_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestoreAgentRequestGitSource(
    typing_extensions.TypedDict, total=False
):
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionResponse(
    typing_extensions.TypedDict, total=False
):
    playbook: GoogleCloudDialogflowCxV3beta1Playbook

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RolloutConfig(
    typing_extensions.TypedDict, total=False
):
    failureCondition: str
    rolloutCondition: str
    rolloutSteps: _list[GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStep]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStep(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    minDuration: str
    trafficPercent: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RolloutState(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    step: str
    stepIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3beta1TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunContinuousTestRequest(
    typing_extensions.TypedDict, total=False
): ...

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
class GoogleCloudDialogflowCxV3beta1RunTestCaseRequest(
    typing_extensions.TypedDict, total=False
):
    environment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RunTestCaseResponse(
    typing_extensions.TypedDict, total=False
):
    result: GoogleCloudDialogflowCxV3beta1TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SafetySettings(
    typing_extensions.TypedDict, total=False
):
    bannedPhrases: _list[GoogleCloudDialogflowCxV3beta1SafetySettingsPhrase]
    defaultBannedPhraseMatchStrategy: typing_extensions.Literal[
        "PHRASE_MATCH_STRATEGY_UNSPECIFIED", "PARTIAL_MATCH", "WORD_MATCH"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SafetySettingsPhrase(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SearchConfig(
    typing_extensions.TypedDict, total=False
):
    boostSpecs: _list[GoogleCloudDialogflowCxV3beta1BoostSpecs]
    filterSpecs: _list[GoogleCloudDialogflowCxV3beta1FilterSpecs]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SecuritySettings(
    typing_extensions.TypedDict, total=False
):
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
        typing_extensions.Literal["PURGE_DATA_TYPE_UNSPECIFIED", "DIALOGFLOW_HISTORY"]
    ]
    redactionScope: typing_extensions.Literal[
        "REDACTION_SCOPE_UNSPECIFIED", "REDACT_DISK_STORAGE"
    ]
    redactionStrategy: typing_extensions.Literal[
        "REDACTION_STRATEGY_UNSPECIFIED", "REDACT_WITH_SERVICE"
    ]
    retentionStrategy: typing_extensions.Literal[
        "RETENTION_STRATEGY_UNSPECIFIED", "REMOVE_AFTER_CONVERSATION"
    ]
    retentionWindowDays: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SecuritySettingsAudioExportSettings(
    typing_extensions.TypedDict, total=False
):
    audioExportPattern: str
    audioFormat: typing_extensions.Literal[
        "AUDIO_FORMAT_UNSPECIFIED", "MULAW", "MP3", "OGG"
    ]
    enableAudioRedaction: bool
    gcsBucket: str
    storeTtsAudio: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SecuritySettingsInsightsExportSettings(
    typing_extensions.TypedDict, total=False
):
    enableInsightsExport: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDialogflowCxV3beta1EntityTypeEntity]
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionInfo(
    typing_extensions.TypedDict, total=False
):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SpeechToTextSettings(
    typing_extensions.TypedDict, total=False
):
    enableSpeechAdaptation: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1StartExperimentRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1StopExperimentRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SubmitAnswerFeedbackRequest(
    typing_extensions.TypedDict, total=False
):
    answerFeedback: GoogleCloudDialogflowCxV3beta1AnswerFeedback
    responseId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig(
    typing_extensions.TypedDict, total=False
):
    effectsProfileId: _list[str]
    pitch: float
    speakingRate: float
    voice: GoogleCloudDialogflowCxV3beta1VoiceSelectionParams
    volumeGainDb: float

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
class GoogleCloudDialogflowCxV3beta1TextToSpeechSettings(
    typing_extensions.TypedDict, total=False
):
    synthesizeSpeechConfigs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Tool(typing_extensions.TypedDict, total=False):
    dataStoreSpec: GoogleCloudDialogflowCxV3beta1ToolDataStoreTool
    description: str
    displayName: str
    extensionSpec: GoogleCloudDialogflowCxV3beta1ToolExtensionTool
    functionSpec: GoogleCloudDialogflowCxV3beta1ToolFunctionTool
    name: str
    openApiSpec: GoogleCloudDialogflowCxV3beta1ToolOpenApiTool
    toolType: typing_extensions.Literal[
        "TOOL_TYPE_UNSPECIFIED", "CUSTOMIZED_TOOL", "BUILTIN_TOOL"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthentication(
    typing_extensions.TypedDict, total=False
):
    apiKeyConfig: GoogleCloudDialogflowCxV3beta1ToolAuthenticationApiKeyConfig
    bearerTokenConfig: GoogleCloudDialogflowCxV3beta1ToolAuthenticationBearerTokenConfig
    oauthConfig: GoogleCloudDialogflowCxV3beta1ToolAuthenticationOAuthConfig
    serviceAgentAuthConfig: (
        GoogleCloudDialogflowCxV3beta1ToolAuthenticationServiceAgentAuthConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationApiKeyConfig(
    typing_extensions.TypedDict, total=False
):
    apiKey: str
    keyName: str
    requestLocation: typing_extensions.Literal[
        "REQUEST_LOCATION_UNSPECIFIED", "HEADER", "QUERY_STRING"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationBearerTokenConfig(
    typing_extensions.TypedDict, total=False
):
    token: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationOAuthConfig(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    oauthGrantType: typing_extensions.Literal[
        "OAUTH_GRANT_TYPE_UNSPECIFIED", "CLIENT_CREDENTIAL"
    ]
    scopes: _list[str]
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolAuthenticationServiceAgentAuthConfig(
    typing_extensions.TypedDict, total=False
):
    serviceAgentAuth: typing_extensions.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "ID_TOKEN", "ACCESS_TOKEN"
    ]

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
class GoogleCloudDialogflowCxV3beta1ToolDataStoreTool(
    typing_extensions.TypedDict, total=False
):
    dataStoreConnections: _list[GoogleCloudDialogflowCxV3beta1DataStoreConnection]
    fallbackPrompt: GoogleCloudDialogflowCxV3beta1ToolDataStoreToolFallbackPrompt

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolDataStoreToolFallbackPrompt(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolExtensionTool(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolFunctionTool(
    typing_extensions.TypedDict, total=False
):
    inputSchema: dict[str, typing.Any]
    outputSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolOpenApiTool(
    typing_extensions.TypedDict, total=False
):
    authentication: GoogleCloudDialogflowCxV3beta1ToolAuthentication
    serviceDirectoryConfig: GoogleCloudDialogflowCxV3beta1ToolServiceDirectoryConfig
    textSchema: str
    tlsConfig: GoogleCloudDialogflowCxV3beta1ToolTLSConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolServiceDirectoryConfig(
    typing_extensions.TypedDict, total=False
):
    service: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolTLSConfig(
    typing_extensions.TypedDict, total=False
):
    caCerts: _list[GoogleCloudDialogflowCxV3beta1ToolTLSConfigCACert]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolTLSConfigCACert(
    typing_extensions.TypedDict, total=False
):
    cert: str
    displayName: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolUse(typing_extensions.TypedDict, total=False):
    action: str
    displayName: str
    inputActionParameters: dict[str, typing.Any]
    outputActionParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TrainFlowRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionCoverage(
    typing_extensions.TypedDict, total=False
):
    coverageScore: float
    transitions: _list[GoogleCloudDialogflowCxV3beta1TransitionCoverageTransition]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionCoverageTransition(
    typing_extensions.TypedDict, total=False
):
    covered: bool
    eventHandler: GoogleCloudDialogflowCxV3beta1EventHandler
    index: int
    source: GoogleCloudDialogflowCxV3beta1TransitionCoverageTransitionNode
    target: GoogleCloudDialogflowCxV3beta1TransitionCoverageTransitionNode
    transitionRoute: GoogleCloudDialogflowCxV3beta1TransitionRoute

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionCoverageTransitionNode(
    typing_extensions.TypedDict, total=False
):
    flow: GoogleCloudDialogflowCxV3beta1Flow
    page: GoogleCloudDialogflowCxV3beta1Page

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
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroup(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    transitionRoutes: _list[GoogleCloudDialogflowCxV3beta1TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverage(
    typing_extensions.TypedDict, total=False
):
    coverageScore: float
    coverages: _list[GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverage(
    typing_extensions.TypedDict, total=False
):
    coverageScore: float
    routeGroup: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup
    transitions: _list[
        GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverageTransition
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupCoverageCoverageTransition(
    typing_extensions.TypedDict, total=False
):
    covered: bool
    transitionRoute: GoogleCloudDialogflowCxV3beta1TransitionRoute

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
class GoogleCloudDialogflowCxV3beta1TypeSchema(
    typing_extensions.TypedDict, total=False
):
    inlineSchema: GoogleCloudDialogflowCxV3beta1InlineSchema
    schemaReference: GoogleCloudDialogflowCxV3beta1TypeSchemaSchemaReference

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TypeSchemaSchemaReference(
    typing_extensions.TypedDict, total=False
):
    schema: str
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1UserUtterance(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ValidateAgentRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ValidateFlowRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ValidationMessage(
    typing_extensions.TypedDict, total=False
):
    detail: str
    resourceNames: _list[GoogleCloudDialogflowCxV3beta1ResourceName]
    resourceType: typing_extensions.Literal[
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
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VariantsHistory(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    versionVariants: GoogleCloudDialogflowCxV3beta1VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1Version(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    nluSettings: GoogleCloudDialogflowCxV3beta1NluSettings
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VersionVariants(
    typing_extensions.TypedDict, total=False
):
    variants: _list[GoogleCloudDialogflowCxV3beta1VersionVariantsVariant]

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VersionVariantsVariant(
    typing_extensions.TypedDict, total=False
):
    isControlGroup: bool
    trafficAllocation: float
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VoiceSelectionParams(
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
    tokenEndpoint: str

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
class GoogleCloudDialogflowV2AnnotatedMessagePart(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    formattedValue: typing.Any
    text: str

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
class GoogleCloudDialogflowV2BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowV2EntityType]

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
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2Context(typing_extensions.TypedDict, total=False):
    lifespanCount: int
    name: str
    parameters: dict[str, typing.Any]

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
class GoogleCloudDialogflowV2CreateConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str
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
class GoogleCloudDialogflowV2DeleteConversationDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowV2DeleteConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str

@typing.type_check_only
class GoogleCloudDialogflowV2DeployConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str

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
class GoogleCloudDialogflowV2EntityTypeEntity(typing_extensions.TypedDict, total=False):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowV2EventInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowV2ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

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
class GoogleCloudDialogflowV2GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudDialogflowV2HumanAgentAssistantEvent(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    participant: str
    suggestionResults: _list[GoogleCloudDialogflowV2SuggestionResult]

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
class GoogleCloudDialogflowV2ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    warnings: _list[GoogleRpcStatus]

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
class GoogleCloudDialogflowV2KnowledgeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    exportOperationMetadata: GoogleCloudDialogflowV2ExportOperationMetadata
    knowledgeBase: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

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
class GoogleCloudDialogflowV2OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    payload: dict[str, typing.Any]
    source: str
    version: str

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
class GoogleCloudDialogflowV2Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

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
        "KNOWLEDGE_SEARCH",
        "KNOWLEDGE_ASSIST",
    ]

@typing.type_check_only
class GoogleCloudDialogflowV2SmartReplyAnswer(typing_extensions.TypedDict, total=False):
    answerRecord: str
    confidence: float
    reply: str

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
class GoogleCloudDialogflowV2SuggestArticlesResponse(
    typing_extensions.TypedDict, total=False
):
    articleAnswers: _list[GoogleCloudDialogflowV2ArticleAnswer]
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
class GoogleCloudDialogflowV2SuggestKnowledgeAssistResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    knowledgeAssistAnswer: GoogleCloudDialogflowV2KnowledgeAssistAnswer
    latestMessage: str

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestSmartRepliesResponse(
    typing_extensions.TypedDict, total=False
):
    contextSize: int
    latestMessage: str
    smartReplyAnswers: _list[GoogleCloudDialogflowV2SmartReplyAnswer]

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestionResult(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    suggestArticlesResponse: GoogleCloudDialogflowV2SuggestArticlesResponse
    suggestFaqAnswersResponse: GoogleCloudDialogflowV2SuggestFaqAnswersResponse
    suggestKnowledgeAssistResponse: (
        GoogleCloudDialogflowV2SuggestKnowledgeAssistResponse
    )
    suggestSmartRepliesResponse: GoogleCloudDialogflowV2SuggestSmartRepliesResponse

@typing.type_check_only
class GoogleCloudDialogflowV2UndeployConversationModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversationModel: str
    createTime: str

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
class GoogleCloudDialogflowV2beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    uri: str

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
        "DTMF_DIGITS",
        "END_OF_SINGLE_UTTERANCE",
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
