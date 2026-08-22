import typing

_list = list

@typing.type_check_only
class GoogleCloudDialogflowCxV3Action(typing.TypedDict, total=False):
    agentUtterance: GoogleCloudDialogflowCxV3AgentUtterance
    flowInvocation: GoogleCloudDialogflowCxV3FlowInvocation
    flowTransition: GoogleCloudDialogflowCxV3FlowTransition
    playbookInvocation: GoogleCloudDialogflowCxV3PlaybookInvocation
    playbookTransition: GoogleCloudDialogflowCxV3PlaybookTransition
    toolUse: GoogleCloudDialogflowCxV3ToolUse
    userUtterance: GoogleCloudDialogflowCxV3UserUtterance

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
class GoogleCloudDialogflowCxV3Agent(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    answerFeedbackSettings: GoogleCloudDialogflowCxV3AgentAnswerFeedbackSettings
    avatarUri: str
    clientCertificateSettings: GoogleCloudDialogflowCxV3AgentClientCertificateSettings
    defaultLanguageCode: str
    description: str
    displayName: str
    enableMultiLanguageTraining: bool
    enableSpellCorrection: bool
    enableStackdriverLogging: bool
    genAppBuilderSettings: GoogleCloudDialogflowCxV3AgentGenAppBuilderSettings
    gitIntegrationSettings: GoogleCloudDialogflowCxV3AgentGitIntegrationSettings
    locked: bool
    name: str
    personalizationSettings: GoogleCloudDialogflowCxV3AgentPersonalizationSettings
    satisfiesPzi: bool
    satisfiesPzs: bool
    securitySettings: str
    speechToTextSettings: GoogleCloudDialogflowCxV3SpeechToTextSettings
    startFlow: str
    startPlaybook: str
    supportedLanguageCodes: _list[str]
    textToSpeechSettings: GoogleCloudDialogflowCxV3TextToSpeechSettings
    timeZone: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentAnswerFeedbackSettings(
    typing.TypedDict, total=False
):
    enableAnswerFeedback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentClientCertificateSettings(
    typing.TypedDict, total=False
):
    passphrase: str
    privateKey: str
    sslCertificate: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentGenAppBuilderSettings(
    typing.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentGitIntegrationSettings(
    typing.TypedDict, total=False
):
    githubSettings: GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsGithubSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsGithubSettings(
    typing.TypedDict, total=False
):
    accessToken: str
    branches: _list[str]
    displayName: str
    repositoryUri: str
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentPersonalizationSettings(
    typing.TypedDict, total=False
):
    defaultEndUserMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentUtterance(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentValidationResult(typing.TypedDict, total=False):
    flowValidationResults: _list[GoogleCloudDialogflowCxV3FlowValidationResult]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AnswerFeedback(typing.TypedDict, total=False):
    customRating: str
    rating: typing.Literal["RATING_UNSPECIFIED", "THUMBS_UP", "THUMBS_DOWN"]
    ratingReason: GoogleCloudDialogflowCxV3AnswerFeedbackRatingReason

@typing.type_check_only
class GoogleCloudDialogflowCxV3AnswerFeedbackRatingReason(
    typing.TypedDict, total=False
):
    feedback: str
    reasonLabels: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3AudioInput(typing.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowCxV3InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3BargeInConfig(typing.TypedDict, total=False):
    noBargeInDuration: str
    totalDuration: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesMetadata(typing.TypedDict, total=False):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesRequest(typing.TypedDict, total=False):
    environment: str
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesResponse(typing.TypedDict, total=False):
    results: _list[GoogleCloudDialogflowCxV3TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpec(typing.TypedDict, total=False):
    conditionBoostSpecs: _list[GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpec]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    boostControlSpec: (
        GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpec
    )
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecs(typing.TypedDict, total=False):
    dataStores: _list[str]
    spec: _list[GoogleCloudDialogflowCxV3BoostSpec]

@typing.type_check_only
class GoogleCloudDialogflowCxV3CalculateCoverageResponse(typing.TypedDict, total=False):
    agent: str
    intentCoverage: GoogleCloudDialogflowCxV3IntentCoverage
    routeGroupCoverage: GoogleCloudDialogflowCxV3TransitionRouteGroupCoverage
    transitionCoverage: GoogleCloudDialogflowCxV3TransitionCoverage

@typing.type_check_only
class GoogleCloudDialogflowCxV3Changelog(typing.TypedDict, total=False):
    action: str
    createTime: str
    displayName: str
    languageCode: str
    name: str
    resource: str
    type: str
    userEmail: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3CodeBlock(typing.TypedDict, total=False):
    code: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3CompareVersionsRequest(typing.TypedDict, total=False):
    languageCode: str
    targetVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3CompareVersionsResponse(typing.TypedDict, total=False):
    baseVersionContentJson: str
    compareTime: str
    targetVersionContentJson: str

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
class GoogleCloudDialogflowCxV3DataStoreConnectionSignals(
    typing.TypedDict, total=False
):
    answer: str
    answerGenerationModelCallSignals: GoogleCloudDialogflowCxV3DataStoreConnectionSignalsAnswerGenerationModelCallSignals
    answerParts: _list[GoogleCloudDialogflowCxV3DataStoreConnectionSignalsAnswerPart]
    citedSnippets: _list[
        GoogleCloudDialogflowCxV3DataStoreConnectionSignalsCitedSnippet
    ]
    groundingSignals: (
        GoogleCloudDialogflowCxV3DataStoreConnectionSignalsGroundingSignals
    )
    rewriterModelCallSignals: (
        GoogleCloudDialogflowCxV3DataStoreConnectionSignalsRewriterModelCallSignals
    )
    rewrittenQuery: str
    safetySignals: GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSafetySignals
    searchSnippets: _list[
        GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSearchSnippet
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsAnswerGenerationModelCallSignals(
    typing.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsAnswerPart(
    typing.TypedDict, total=False
):
    supportingIndices: _list[int]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsCitedSnippet(
    typing.TypedDict, total=False
):
    searchSnippet: GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSearchSnippet
    snippetIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsGroundingSignals(
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
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsRewriterModelCallSignals(
    typing.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSafetySignals(
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
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSearchSnippet(
    typing.TypedDict, total=False
):
    documentTitle: str
    documentUri: str
    metadata: dict[str, typing.Any]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowMetadata(typing.TypedDict, total=False):
    testErrors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowRequest(typing.TypedDict, total=False):
    flowVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowResponse(typing.TypedDict, total=False):
    deployment: str
    environment: GoogleCloudDialogflowCxV3Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3Deployment(typing.TypedDict, total=False):
    endTime: str
    flowVersion: str
    name: str
    result: GoogleCloudDialogflowCxV3DeploymentResult
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeploymentResult(typing.TypedDict, total=False):
    deploymentTestResults: _list[str]
    experiment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DetectIntentRequest(typing.TypedDict, total=False):
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig
    queryInput: GoogleCloudDialogflowCxV3QueryInput
    queryParams: GoogleCloudDialogflowCxV3QueryParameters
    responseView: typing.Literal[
        "DETECT_INTENT_RESPONSE_VIEW_UNSPECIFIED",
        "DETECT_INTENT_RESPONSE_VIEW_FULL",
        "DETECT_INTENT_RESPONSE_VIEW_BASIC",
        "DETECT_INTENT_RESPONSE_VIEW_DEFAULT",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DetectIntentResponse(typing.TypedDict, total=False):
    allowCancellation: bool
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3QueryResult
    responseId: str
    responseType: typing.Literal["RESPONSE_TYPE_UNSPECIFIED", "PARTIAL", "FINAL"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DtmfInput(typing.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3EntityType(typing.TypedDict, total=False):
    autoExpansionMode: typing.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowCxV3EntityTypeEntity]
    excludedPhrases: _list[GoogleCloudDialogflowCxV3EntityTypeExcludedPhrase]
    kind: typing.Literal["KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"]
    name: str
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3EntityTypeEntity(typing.TypedDict, total=False):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3EntityTypeExcludedPhrase(typing.TypedDict, total=False):
    value: str

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
class GoogleCloudDialogflowCxV3Example(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDialogflowCxV3Action]
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
    playbookInput: GoogleCloudDialogflowCxV3PlaybookInput
    playbookOutput: GoogleCloudDialogflowCxV3PlaybookOutput
    tokenCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Experiment(typing.TypedDict, total=False):
    createTime: str
    definition: GoogleCloudDialogflowCxV3ExperimentDefinition
    description: str
    displayName: str
    endTime: str
    experimentLength: str
    lastUpdateTime: str
    name: str
    result: GoogleCloudDialogflowCxV3ExperimentResult
    rolloutConfig: GoogleCloudDialogflowCxV3RolloutConfig
    rolloutFailureReason: str
    rolloutState: GoogleCloudDialogflowCxV3RolloutState
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DRAFT", "RUNNING", "DONE", "ROLLOUT_FAILED"
    ]
    variantsHistory: _list[GoogleCloudDialogflowCxV3VariantsHistory]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentDefinition(typing.TypedDict, total=False):
    condition: str
    versionVariants: GoogleCloudDialogflowCxV3VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentResult(typing.TypedDict, total=False):
    lastUpdateTime: str
    versionMetrics: _list[GoogleCloudDialogflowCxV3ExperimentResultVersionMetrics]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentResultConfidenceInterval(
    typing.TypedDict, total=False
):
    confidenceLevel: float
    lowerBound: float
    ratio: float
    upperBound: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentResultMetric(typing.TypedDict, total=False):
    confidenceInterval: GoogleCloudDialogflowCxV3ExperimentResultConfidenceInterval
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
class GoogleCloudDialogflowCxV3ExperimentResultVersionMetrics(
    typing.TypedDict, total=False
):
    metrics: _list[GoogleCloudDialogflowCxV3ExperimentResultMetric]
    sessionCount: int
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportAgentRequest(typing.TypedDict, total=False):
    agentUri: str
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON_PACKAGE"]
    environment: str
    gitDestination: GoogleCloudDialogflowCxV3ExportAgentRequestGitDestination
    includeBigqueryExportSettings: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportAgentRequestGitDestination(
    typing.TypedDict, total=False
):
    commitMessage: str
    trackingBranch: str

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
class GoogleCloudDialogflowCxV3ExportEntityTypesRequest(typing.TypedDict, total=False):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON_PACKAGE"]
    entityTypes: _list[str]
    entityTypesContentInline: bool
    entityTypesUri: str
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportEntityTypesResponse(typing.TypedDict, total=False):
    entityTypesContent: GoogleCloudDialogflowCxV3InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportFlowRequest(typing.TypedDict, total=False):
    flowUri: str
    includeReferencedFlows: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportFlowResponse(typing.TypedDict, total=False):
    flowContent: str
    flowUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportIntentsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportIntentsRequest(typing.TypedDict, total=False):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON", "CSV"]
    intents: _list[str]
    intentsContentInline: bool
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportIntentsResponse(typing.TypedDict, total=False):
    intentsContent: GoogleCloudDialogflowCxV3InlineDestination
    intentsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportPlaybookRequest(typing.TypedDict, total=False):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    playbookUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesRequest(typing.TypedDict, total=False):
    dataFormat: typing.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    filter: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesResponse(typing.TypedDict, total=False):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FilterSpecs(typing.TypedDict, total=False):
    dataStores: _list[str]
    filter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Flow(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    description: str
    displayName: str
    eventHandlers: _list[GoogleCloudDialogflowCxV3EventHandler]
    inputParameterDefinitions: _list[GoogleCloudDialogflowCxV3ParameterDefinition]
    knowledgeConnectorSettings: GoogleCloudDialogflowCxV3KnowledgeConnectorSettings
    locked: bool
    multiLanguageSettings: GoogleCloudDialogflowCxV3FlowMultiLanguageSettings
    name: str
    nluSettings: GoogleCloudDialogflowCxV3NluSettings
    outputParameterDefinitions: _list[GoogleCloudDialogflowCxV3ParameterDefinition]
    transitionRouteGroups: _list[str]
    transitionRoutes: _list[GoogleCloudDialogflowCxV3TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowImportStrategy(typing.TypedDict, total=False):
    globalImportStrategy: typing.Literal[
        "IMPORT_STRATEGY_UNSPECIFIED",
        "IMPORT_STRATEGY_CREATE_NEW",
        "IMPORT_STRATEGY_REPLACE",
        "IMPORT_STRATEGY_KEEP",
        "IMPORT_STRATEGY_MERGE",
        "IMPORT_STRATEGY_THROW_ERROR",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowInvocation(typing.TypedDict, total=False):
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

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowMultiLanguageSettings(typing.TypedDict, total=False):
    enableMultiLanguageDetection: bool
    supportedResponseLanguageCodes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowTraceMetadata(typing.TypedDict, total=False):
    displayName: str
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowTransition(typing.TypedDict, total=False):
    displayName: str
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowValidationResult(typing.TypedDict, total=False):
    name: str
    updateTime: str
    validationMessages: _list[GoogleCloudDialogflowCxV3ValidationMessage]

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
class GoogleCloudDialogflowCxV3FulfillIntentRequest(typing.TypedDict, total=False):
    match: GoogleCloudDialogflowCxV3Match
    matchIntentRequest: GoogleCloudDialogflowCxV3MatchIntentRequest
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillIntentResponse(typing.TypedDict, total=False):
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3QueryResult
    responseId: str

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
class GoogleCloudDialogflowCxV3GenerativeSettings(typing.TypedDict, total=False):
    fallbackSettings: GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettings
    generativeSafetySettings: GoogleCloudDialogflowCxV3SafetySettings
    knowledgeConnectorSettings: (
        GoogleCloudDialogflowCxV3GenerativeSettingsKnowledgeConnectorSettings
    )
    languageCode: str
    llmModelSettings: GoogleCloudDialogflowCxV3LlmModelSettings
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettings(
    typing.TypedDict, total=False
):
    promptTemplates: _list[
        GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettingsPromptTemplate
    ]
    selectedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettingsPromptTemplate(
    typing.TypedDict, total=False
):
    displayName: str
    frozen: bool
    promptText: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3GenerativeSettingsKnowledgeConnectorSettings(
    typing.TypedDict, total=False
):
    agent: str
    agentIdentity: str
    agentScope: str
    business: str
    businessDescription: str
    disableDataStoreFallback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3Generator(typing.TypedDict, total=False):
    displayName: str
    llmModelSettings: GoogleCloudDialogflowCxV3LlmModelSettings
    modelParameter: GoogleCloudDialogflowCxV3GeneratorModelParameter
    name: str
    placeholders: _list[GoogleCloudDialogflowCxV3GeneratorPlaceholder]
    promptText: GoogleCloudDialogflowCxV3Phrase

@typing.type_check_only
class GoogleCloudDialogflowCxV3GeneratorModelParameter(typing.TypedDict, total=False):
    maxDecodeSteps: int
    temperature: float
    topK: int
    topP: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3GeneratorPlaceholder(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Handler(typing.TypedDict, total=False):
    eventHandler: GoogleCloudDialogflowCxV3HandlerEventHandler
    lifecycleHandler: GoogleCloudDialogflowCxV3HandlerLifecycleHandler

@typing.type_check_only
class GoogleCloudDialogflowCxV3HandlerEventHandler(typing.TypedDict, total=False):
    condition: str
    event: str
    fulfillment: GoogleCloudDialogflowCxV3Fulfillment

@typing.type_check_only
class GoogleCloudDialogflowCxV3HandlerLifecycleHandler(typing.TypedDict, total=False):
    condition: str
    fulfillment: GoogleCloudDialogflowCxV3Fulfillment
    lifecycleStage: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesRequest(typing.TypedDict, total=False):
    entityTypesContent: GoogleCloudDialogflowCxV3InlineSource
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
class GoogleCloudDialogflowCxV3ImportFlowRequest(typing.TypedDict, total=False):
    flowContent: str
    flowImportStrategy: GoogleCloudDialogflowCxV3FlowImportStrategy
    flowUri: str
    importOption: typing.Literal["IMPORT_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportFlowResponse(typing.TypedDict, total=False):
    flow: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportIntentsRequest(typing.TypedDict, total=False):
    intentsContent: GoogleCloudDialogflowCxV3InlineSource
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
class GoogleCloudDialogflowCxV3ImportPlaybookRequest(typing.TypedDict, total=False):
    importStrategy: GoogleCloudDialogflowCxV3PlaybookImportStrategy
    playbookContent: str
    playbookUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportTestCasesMetadata(typing.TypedDict, total=False):
    errors: _list[GoogleCloudDialogflowCxV3TestCaseError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportTestCasesRequest(typing.TypedDict, total=False):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportTestCasesResponse(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3InlineDestination(typing.TypedDict, total=False):
    content: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3InlineSchema(typing.TypedDict, total=False):
    items: GoogleCloudDialogflowCxV3TypeSchema
    type: typing.Literal[
        "DATA_TYPE_UNSPECIFIED", "STRING", "NUMBER", "BOOLEAN", "ARRAY"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3InlineSource(typing.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3IntentCoverage(typing.TypedDict, total=False):
    coverageScore: float
    intents: _list[GoogleCloudDialogflowCxV3IntentCoverageIntent]

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentCoverageIntent(typing.TypedDict, total=False):
    covered: bool
    intent: str

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
class GoogleCloudDialogflowCxV3ListAgentsResponse(typing.TypedDict, total=False):
    agents: _list[GoogleCloudDialogflowCxV3Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListChangelogsResponse(typing.TypedDict, total=False):
    changelogs: _list[GoogleCloudDialogflowCxV3Changelog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse(
    typing.TypedDict, total=False
):
    continuousTestResults: _list[GoogleCloudDialogflowCxV3ContinuousTestResult]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListDeploymentsResponse(typing.TypedDict, total=False):
    deployments: _list[GoogleCloudDialogflowCxV3Deployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListEntityTypesResponse(typing.TypedDict, total=False):
    entityTypes: _list[GoogleCloudDialogflowCxV3EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListEnvironmentsResponse(typing.TypedDict, total=False):
    environments: _list[GoogleCloudDialogflowCxV3Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListExamplesResponse(typing.TypedDict, total=False):
    examples: _list[GoogleCloudDialogflowCxV3Example]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListExperimentsResponse(typing.TypedDict, total=False):
    experiments: _list[GoogleCloudDialogflowCxV3Experiment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListFlowsResponse(typing.TypedDict, total=False):
    flows: _list[GoogleCloudDialogflowCxV3Flow]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListGeneratorsResponse(typing.TypedDict, total=False):
    generators: _list[GoogleCloudDialogflowCxV3Generator]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListIntentsResponse(typing.TypedDict, total=False):
    intents: _list[GoogleCloudDialogflowCxV3Intent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListPagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pages: _list[GoogleCloudDialogflowCxV3Page]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListPlaybookVersionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    playbookVersions: _list[GoogleCloudDialogflowCxV3PlaybookVersion]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListPlaybooksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    playbooks: _list[GoogleCloudDialogflowCxV3Playbook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListSecuritySettingsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    securitySettings: _list[GoogleCloudDialogflowCxV3SecuritySettings]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3SessionEntityType]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTestCaseResultsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    testCaseResults: _list[GoogleCloudDialogflowCxV3TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTestCasesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    testCases: _list[GoogleCloudDialogflowCxV3TestCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListToolVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    toolVersions: _list[GoogleCloudDialogflowCxV3ToolVersion]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListToolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tools: _list[GoogleCloudDialogflowCxV3Tool]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    transitionRouteGroups: _list[GoogleCloudDialogflowCxV3TransitionRouteGroup]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[GoogleCloudDialogflowCxV3Version]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListWebhooksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    webhooks: _list[GoogleCloudDialogflowCxV3Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3LlmModelSettings(typing.TypedDict, total=False):
    model: str
    promptText: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3LoadVersionRequest(typing.TypedDict, total=False):
    allowOverrideAgentResources: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse(
    typing.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowCxV3Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Match(typing.TypedDict, total=False):
    confidence: float
    event: str
    intent: GoogleCloudDialogflowCxV3Intent
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
class GoogleCloudDialogflowCxV3MatchIntentRequest(typing.TypedDict, total=False):
    persistParameterChanges: bool
    queryInput: GoogleCloudDialogflowCxV3QueryInput
    queryParams: GoogleCloudDialogflowCxV3QueryParameters

@typing.type_check_only
class GoogleCloudDialogflowCxV3MatchIntentResponse(typing.TypedDict, total=False):
    currentPage: GoogleCloudDialogflowCxV3Page
    matches: _list[GoogleCloudDialogflowCxV3Match]
    text: str
    transcript: str
    triggerEvent: str
    triggerIntent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3NluSettings(typing.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3OutputAudioConfig(typing.TypedDict, total=False):
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
    synthesizeSpeechConfig: GoogleCloudDialogflowCxV3SynthesizeSpeechConfig

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
class GoogleCloudDialogflowCxV3ParameterDefinition(typing.TypedDict, total=False):
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
    typeSchema: GoogleCloudDialogflowCxV3TypeSchema

@typing.type_check_only
class GoogleCloudDialogflowCxV3Phrase(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Playbook(typing.TypedDict, total=False):
    codeBlock: GoogleCloudDialogflowCxV3CodeBlock
    createTime: str
    displayName: str
    goal: str
    handlers: _list[GoogleCloudDialogflowCxV3Handler]
    inlineActions: _list[str]
    inputParameterDefinitions: _list[GoogleCloudDialogflowCxV3ParameterDefinition]
    instruction: GoogleCloudDialogflowCxV3PlaybookInstruction
    llmModelSettings: GoogleCloudDialogflowCxV3LlmModelSettings
    name: str
    outputParameterDefinitions: _list[GoogleCloudDialogflowCxV3ParameterDefinition]
    playbookType: typing.Literal["PLAYBOOK_TYPE_UNSPECIFIED", "TASK", "ROUTINE"]
    referencedFlows: _list[str]
    referencedPlaybooks: _list[str]
    referencedTools: _list[str]
    tokenCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookImportStrategy(typing.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3PlaybookInput(typing.TypedDict, total=False):
    precedingConversationSummary: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookInstruction(typing.TypedDict, total=False):
    guidelines: str
    steps: _list[GoogleCloudDialogflowCxV3PlaybookStep]

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookInvocation(typing.TypedDict, total=False):
    displayName: str
    playbook: str
    playbookInput: GoogleCloudDialogflowCxV3PlaybookInput
    playbookOutput: GoogleCloudDialogflowCxV3PlaybookOutput
    playbookState: typing.Literal[
        "OUTPUT_STATE_UNSPECIFIED",
        "OUTPUT_STATE_OK",
        "OUTPUT_STATE_CANCELLED",
        "OUTPUT_STATE_FAILED",
        "OUTPUT_STATE_ESCALATED",
        "OUTPUT_STATE_PENDING",
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookOutput(typing.TypedDict, total=False):
    executionSummary: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookStep(typing.TypedDict, total=False):
    steps: _list[GoogleCloudDialogflowCxV3PlaybookStep]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookTraceMetadata(typing.TypedDict, total=False):
    displayName: str
    playbook: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookTransition(typing.TypedDict, total=False):
    displayName: str
    playbook: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3PlaybookVersion(typing.TypedDict, total=False):
    description: str
    examples: _list[GoogleCloudDialogflowCxV3Example]
    name: str
    playbook: GoogleCloudDialogflowCxV3Playbook
    updateTime: str

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
class GoogleCloudDialogflowCxV3QueryParameters(typing.TypedDict, total=False):
    analyzeQueryTextSentiment: bool
    channel: str
    currentPage: str
    currentPlaybook: str
    disableWebhook: bool
    endUserMetadata: dict[str, typing.Any]
    flowVersions: _list[str]
    geoLocation: GoogleTypeLatLng
    llmModelSettings: GoogleCloudDialogflowCxV3LlmModelSettings
    parameterScope: str
    parameters: dict[str, typing.Any]
    payload: dict[str, typing.Any]
    populateDataStoreConnectionSignals: bool
    searchConfig: GoogleCloudDialogflowCxV3SearchConfig
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3SessionEntityType]
    sessionTtl: str
    timeZone: str
    webhookHeaders: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3QueryResult(typing.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    allowAnswerFeedback: bool
    currentFlow: GoogleCloudDialogflowCxV3Flow
    currentPage: GoogleCloudDialogflowCxV3Page
    dataStoreConnectionSignals: GoogleCloudDialogflowCxV3DataStoreConnectionSignals
    diagnosticInfo: dict[str, typing.Any]
    dtmf: GoogleCloudDialogflowCxV3DtmfInput
    intent: GoogleCloudDialogflowCxV3Intent
    intentDetectionConfidence: float
    languageCode: str
    match: GoogleCloudDialogflowCxV3Match
    parameters: dict[str, typing.Any]
    responseMessages: _list[GoogleCloudDialogflowCxV3ResponseMessage]
    sentimentAnalysisResult: GoogleCloudDialogflowCxV3SentimentAnalysisResult
    text: str
    traceBlocks: _list[GoogleCloudDialogflowCxV3TraceBlock]
    transcript: str
    triggerEvent: str
    triggerIntent: str
    webhookPayloads: _list[dict[str, typing.Any]]
    webhookStatuses: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResourceName(typing.TypedDict, total=False):
    displayName: str
    name: str

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
class GoogleCloudDialogflowCxV3RestoreAgentRequest(typing.TypedDict, total=False):
    agentContent: str
    agentUri: str
    gitSource: GoogleCloudDialogflowCxV3RestoreAgentRequestGitSource
    restoreOption: typing.Literal["RESTORE_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RestoreAgentRequestGitSource(
    typing.TypedDict, total=False
):
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3RestorePlaybookVersionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3RestorePlaybookVersionResponse(
    typing.TypedDict, total=False
):
    playbook: GoogleCloudDialogflowCxV3Playbook

@typing.type_check_only
class GoogleCloudDialogflowCxV3RestoreToolVersionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3RestoreToolVersionResponse(
    typing.TypedDict, total=False
):
    tool: GoogleCloudDialogflowCxV3Tool

@typing.type_check_only
class GoogleCloudDialogflowCxV3RolloutConfig(typing.TypedDict, total=False):
    failureCondition: str
    rolloutCondition: str
    rolloutSteps: _list[GoogleCloudDialogflowCxV3RolloutConfigRolloutStep]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RolloutConfigRolloutStep(typing.TypedDict, total=False):
    displayName: str
    minDuration: str
    trafficPercent: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3RolloutState(typing.TypedDict, total=False):
    startTime: str
    step: str
    stepIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestMetadata(typing.TypedDict, total=False):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestResponse(typing.TypedDict, total=False):
    continuousTestResult: GoogleCloudDialogflowCxV3ContinuousTestResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseRequest(typing.TypedDict, total=False):
    environment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseResponse(typing.TypedDict, total=False):
    result: GoogleCloudDialogflowCxV3TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3SafetySettings(typing.TypedDict, total=False):
    bannedPhrases: _list[GoogleCloudDialogflowCxV3SafetySettingsPhrase]
    defaultBannedPhraseMatchStrategy: typing.Literal[
        "PHRASE_MATCH_STRATEGY_UNSPECIFIED", "PARTIAL_MATCH", "WORD_MATCH"
    ]
    defaultRaiSettings: GoogleCloudDialogflowCxV3SafetySettingsRaiSettings
    promptSecuritySettings: (
        GoogleCloudDialogflowCxV3SafetySettingsPromptSecuritySettings
    )
    raiSettings: GoogleCloudDialogflowCxV3SafetySettingsRaiSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3SafetySettingsPhrase(typing.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SafetySettingsPromptSecuritySettings(
    typing.TypedDict, total=False
):
    enablePromptSecurity: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3SafetySettingsRaiSettings(typing.TypedDict, total=False):
    categoryFilters: _list[
        GoogleCloudDialogflowCxV3SafetySettingsRaiSettingsCategoryFilter
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3SafetySettingsRaiSettingsCategoryFilter(
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
class GoogleCloudDialogflowCxV3SearchConfig(typing.TypedDict, total=False):
    boostSpecs: _list[GoogleCloudDialogflowCxV3BoostSpecs]
    filterSpecs: _list[GoogleCloudDialogflowCxV3FilterSpecs]

@typing.type_check_only
class GoogleCloudDialogflowCxV3SecuritySettings(typing.TypedDict, total=False):
    audioExportSettings: GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettings
    deidentifyTemplate: str
    displayName: str
    insightsExportSettings: (
        GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettings
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
class GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettings(
    typing.TypedDict, total=False
):
    audioExportPattern: str
    audioFormat: typing.Literal["AUDIO_FORMAT_UNSPECIFIED", "MULAW", "MP3", "OGG"]
    enableAudioRedaction: bool
    gcsBucket: str
    storeTtsAudio: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettings(
    typing.TypedDict, total=False
):
    enableInsightsExport: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3SentimentAnalysisResult(typing.TypedDict, total=False):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3SessionEntityType(typing.TypedDict, total=False):
    entities: _list[GoogleCloudDialogflowCxV3EntityTypeEntity]
    entityOverrideMode: typing.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SessionInfo(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SpeechProcessingMetadata(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SpeechToTextSettings(typing.TypedDict, total=False):
    enableSpeechAdaptation: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3StartExperimentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3StopExperimentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest(
    typing.TypedDict, total=False
):
    answerFeedback: GoogleCloudDialogflowCxV3AnswerFeedback
    responseId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SynthesizeSpeechConfig(typing.TypedDict, total=False):
    effectsProfileId: _list[str]
    pitch: float
    speakingRate: float
    voice: GoogleCloudDialogflowCxV3VoiceSelectionParams
    volumeGainDb: float

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
class GoogleCloudDialogflowCxV3TextToSpeechSettings(typing.TypedDict, total=False):
    synthesizeSpeechConfigs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3Tool(typing.TypedDict, total=False):
    dataStoreSpec: GoogleCloudDialogflowCxV3ToolDataStoreTool
    description: str
    displayName: str
    functionSpec: GoogleCloudDialogflowCxV3ToolFunctionTool
    name: str
    openApiSpec: GoogleCloudDialogflowCxV3ToolOpenApiTool
    toolType: typing.Literal["TOOL_TYPE_UNSPECIFIED", "CUSTOMIZED_TOOL", "BUILTIN_TOOL"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolAuthentication(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudDialogflowCxV3ToolAuthenticationApiKeyConfig
    bearerTokenConfig: GoogleCloudDialogflowCxV3ToolAuthenticationBearerTokenConfig
    oauthConfig: GoogleCloudDialogflowCxV3ToolAuthenticationOAuthConfig
    serviceAccountAuthConfig: (
        GoogleCloudDialogflowCxV3ToolAuthenticationServiceAccountAuthConfig
    )
    serviceAgentAuthConfig: (
        GoogleCloudDialogflowCxV3ToolAuthenticationServiceAgentAuthConfig
    )

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolAuthenticationApiKeyConfig(
    typing.TypedDict, total=False
):
    apiKey: str
    keyName: str
    requestLocation: typing.Literal[
        "REQUEST_LOCATION_UNSPECIFIED", "HEADER", "QUERY_STRING"
    ]
    secretVersionForApiKey: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolAuthenticationBearerTokenConfig(
    typing.TypedDict, total=False
):
    secretVersionForToken: str
    token: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolAuthenticationOAuthConfig(
    typing.TypedDict, total=False
):
    clientId: str
    clientSecret: str
    oauthGrantType: typing.Literal["OAUTH_GRANT_TYPE_UNSPECIFIED", "CLIENT_CREDENTIAL"]
    scopes: _list[str]
    secretVersionForClientSecret: str
    tokenEndpoint: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolAuthenticationServiceAccountAuthConfig(
    typing.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolAuthenticationServiceAgentAuthConfig(
    typing.TypedDict, total=False
):
    serviceAgentAuth: typing.Literal[
        "SERVICE_AGENT_AUTH_UNSPECIFIED", "ID_TOKEN", "ACCESS_TOKEN"
    ]

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
class GoogleCloudDialogflowCxV3ToolDataStoreTool(typing.TypedDict, total=False):
    dataStoreConnections: _list[GoogleCloudDialogflowCxV3DataStoreConnection]
    fallbackPrompt: GoogleCloudDialogflowCxV3ToolDataStoreToolFallbackPrompt

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolDataStoreToolFallbackPrompt(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolFunctionTool(typing.TypedDict, total=False):
    inputSchema: dict[str, typing.Any]
    outputSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolOpenApiTool(typing.TypedDict, total=False):
    authentication: GoogleCloudDialogflowCxV3ToolAuthentication
    serviceDirectoryConfig: GoogleCloudDialogflowCxV3ToolServiceDirectoryConfig
    textSchema: str
    tlsConfig: GoogleCloudDialogflowCxV3ToolTLSConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolServiceDirectoryConfig(
    typing.TypedDict, total=False
):
    service: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolTLSConfig(typing.TypedDict, total=False):
    caCerts: _list[GoogleCloudDialogflowCxV3ToolTLSConfigCACert]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolTLSConfigCACert(typing.TypedDict, total=False):
    cert: str
    displayName: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolUse(typing.TypedDict, total=False):
    action: str
    displayName: str
    inputActionParameters: dict[str, typing.Any]
    outputActionParameters: dict[str, typing.Any]
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ToolVersion(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    tool: GoogleCloudDialogflowCxV3Tool
    updateTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TraceBlock(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDialogflowCxV3Action]
    completeTime: str
    endState: typing.Literal[
        "OUTPUT_STATE_UNSPECIFIED",
        "OUTPUT_STATE_OK",
        "OUTPUT_STATE_CANCELLED",
        "OUTPUT_STATE_FAILED",
        "OUTPUT_STATE_ESCALATED",
        "OUTPUT_STATE_PENDING",
    ]
    flowTraceMetadata: GoogleCloudDialogflowCxV3FlowTraceMetadata
    inputParameters: dict[str, typing.Any]
    outputParameters: dict[str, typing.Any]
    playbookTraceMetadata: GoogleCloudDialogflowCxV3PlaybookTraceMetadata
    speechProcessingMetadata: GoogleCloudDialogflowCxV3SpeechProcessingMetadata
    startTime: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3TrainFlowRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionCoverage(typing.TypedDict, total=False):
    coverageScore: float
    transitions: _list[GoogleCloudDialogflowCxV3TransitionCoverageTransition]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionCoverageTransition(
    typing.TypedDict, total=False
):
    covered: bool
    eventHandler: GoogleCloudDialogflowCxV3EventHandler
    index: int
    source: GoogleCloudDialogflowCxV3TransitionCoverageTransitionNode
    target: GoogleCloudDialogflowCxV3TransitionCoverageTransitionNode
    transitionRoute: GoogleCloudDialogflowCxV3TransitionRoute

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionCoverageTransitionNode(
    typing.TypedDict, total=False
):
    flow: GoogleCloudDialogflowCxV3Flow
    page: GoogleCloudDialogflowCxV3Page

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
class GoogleCloudDialogflowCxV3TransitionRouteGroup(typing.TypedDict, total=False):
    displayName: str
    name: str
    transitionRoutes: _list[GoogleCloudDialogflowCxV3TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRouteGroupCoverage(
    typing.TypedDict, total=False
):
    coverageScore: float
    coverages: _list[GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverage(
    typing.TypedDict, total=False
):
    coverageScore: float
    routeGroup: GoogleCloudDialogflowCxV3TransitionRouteGroup
    transitions: _list[
        GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransition
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransition(
    typing.TypedDict, total=False
):
    covered: bool
    transitionRoute: GoogleCloudDialogflowCxV3TransitionRoute

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
class GoogleCloudDialogflowCxV3TypeSchema(typing.TypedDict, total=False):
    inlineSchema: GoogleCloudDialogflowCxV3InlineSchema
    schemaReference: GoogleCloudDialogflowCxV3TypeSchemaSchemaReference

@typing.type_check_only
class GoogleCloudDialogflowCxV3TypeSchemaSchemaReference(typing.TypedDict, total=False):
    schema: str
    tool: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3UserUtterance(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ValidateAgentRequest(typing.TypedDict, total=False):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ValidateFlowRequest(typing.TypedDict, total=False):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ValidationMessage(typing.TypedDict, total=False):
    detail: str
    resourceNames: _list[GoogleCloudDialogflowCxV3ResourceName]
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
class GoogleCloudDialogflowCxV3VariantsHistory(typing.TypedDict, total=False):
    updateTime: str
    versionVariants: GoogleCloudDialogflowCxV3VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3Version(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    nluSettings: GoogleCloudDialogflowCxV3NluSettings
    state: typing.Literal["STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDialogflowCxV3VersionVariants(typing.TypedDict, total=False):
    variants: _list[GoogleCloudDialogflowCxV3VersionVariantsVariant]

@typing.type_check_only
class GoogleCloudDialogflowCxV3VersionVariantsVariant(typing.TypedDict, total=False):
    isControlGroup: bool
    trafficAllocation: float
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3VoiceSelectionParams(typing.TypedDict, total=False):
    name: str
    ssmlGender: typing.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED",
        "SSML_VOICE_GENDER_MALE",
        "SSML_VOICE_GENDER_FEMALE",
        "SSML_VOICE_GENDER_NEUTRAL",
    ]

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
