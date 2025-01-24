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
class GoogleCloudDialogflowCxV3Agent(typing_extensions.TypedDict, total=False):
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
    supportedLanguageCodes: _list[str]
    textToSpeechSettings: GoogleCloudDialogflowCxV3TextToSpeechSettings
    timeZone: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentAnswerFeedbackSettings(
    typing_extensions.TypedDict, total=False
):
    enableAnswerFeedback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentClientCertificateSettings(
    typing_extensions.TypedDict, total=False
):
    passphrase: str
    privateKey: str
    sslCertificate: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentGenAppBuilderSettings(
    typing_extensions.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentGitIntegrationSettings(
    typing_extensions.TypedDict, total=False
):
    githubSettings: GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsGithubSettings

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentGitIntegrationSettingsGithubSettings(
    typing_extensions.TypedDict, total=False
):
    accessToken: str
    branches: _list[str]
    displayName: str
    repositoryUri: str
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentPersonalizationSettings(
    typing_extensions.TypedDict, total=False
):
    defaultEndUserMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentValidationResult(
    typing_extensions.TypedDict, total=False
):
    flowValidationResults: _list[GoogleCloudDialogflowCxV3FlowValidationResult]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3AnswerFeedback(typing_extensions.TypedDict, total=False):
    customRating: str
    rating: typing_extensions.Literal["RATING_UNSPECIFIED", "THUMBS_UP", "THUMBS_DOWN"]
    ratingReason: GoogleCloudDialogflowCxV3AnswerFeedbackRatingReason

@typing.type_check_only
class GoogleCloudDialogflowCxV3AnswerFeedbackRatingReason(
    typing_extensions.TypedDict, total=False
):
    feedback: str
    reasonLabels: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3AudioInput(typing_extensions.TypedDict, total=False):
    audio: str
    config: GoogleCloudDialogflowCxV3InputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3BargeInConfig(typing_extensions.TypedDict, total=False):
    noBargeInDuration: str
    totalDuration: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    environment: str
    testCases: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BatchRunTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    results: _list[GoogleCloudDialogflowCxV3TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpec(typing_extensions.TypedDict, total=False):
    conditionBoostSpecs: _list[GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpec]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: (
        GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpec
    )
    condition: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3BoostSpecs(typing_extensions.TypedDict, total=False):
    dataStores: _list[str]
    spec: _list[GoogleCloudDialogflowCxV3BoostSpec]

@typing.type_check_only
class GoogleCloudDialogflowCxV3CalculateCoverageResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str
    intentCoverage: GoogleCloudDialogflowCxV3IntentCoverage
    routeGroupCoverage: GoogleCloudDialogflowCxV3TransitionRouteGroupCoverage
    transitionCoverage: GoogleCloudDialogflowCxV3TransitionCoverage

@typing.type_check_only
class GoogleCloudDialogflowCxV3Changelog(typing_extensions.TypedDict, total=False):
    action: str
    createTime: str
    displayName: str
    languageCode: str
    name: str
    resource: str
    type: str
    userEmail: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3CompareVersionsRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    targetVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3CompareVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    baseVersionContentJson: str
    compareTime: str
    targetVersionContentJson: str

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
class GoogleCloudDialogflowCxV3DataStoreConnectionSignals(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsAnswerPart(
    typing_extensions.TypedDict, total=False
):
    supportingIndices: _list[int]
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsCitedSnippet(
    typing_extensions.TypedDict, total=False
):
    searchSnippet: GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSearchSnippet
    snippetIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsGroundingSignals(
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
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsRewriterModelCallSignals(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelOutput: str
    renderedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSafetySignals(
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
class GoogleCloudDialogflowCxV3DataStoreConnectionSignalsSearchSnippet(
    typing_extensions.TypedDict, total=False
):
    documentTitle: str
    documentUri: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowMetadata(
    typing_extensions.TypedDict, total=False
):
    testErrors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowRequest(
    typing_extensions.TypedDict, total=False
):
    flowVersion: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeployFlowResponse(
    typing_extensions.TypedDict, total=False
):
    deployment: str
    environment: GoogleCloudDialogflowCxV3Environment

@typing.type_check_only
class GoogleCloudDialogflowCxV3Deployment(typing_extensions.TypedDict, total=False):
    endTime: str
    flowVersion: str
    name: str
    result: GoogleCloudDialogflowCxV3DeploymentResult
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeploymentResult(
    typing_extensions.TypedDict, total=False
):
    deploymentTestResults: _list[str]
    experiment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3DetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig
    queryInput: GoogleCloudDialogflowCxV3QueryInput
    queryParams: GoogleCloudDialogflowCxV3QueryParameters

@typing.type_check_only
class GoogleCloudDialogflowCxV3DetectIntentResponse(
    typing_extensions.TypedDict, total=False
):
    allowCancellation: bool
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3QueryResult
    responseId: str
    responseType: typing_extensions.Literal[
        "RESPONSE_TYPE_UNSPECIFIED", "PARTIAL", "FINAL"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3DtmfInput(typing_extensions.TypedDict, total=False):
    digits: str
    finishDigit: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3EntityType(typing_extensions.TypedDict, total=False):
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    displayName: str
    enableFuzzyExtraction: bool
    entities: _list[GoogleCloudDialogflowCxV3EntityTypeEntity]
    excludedPhrases: _list[GoogleCloudDialogflowCxV3EntityTypeExcludedPhrase]
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    name: str
    redact: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3EntityTypeEntity(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]
    value: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3EntityTypeExcludedPhrase(
    typing_extensions.TypedDict, total=False
):
    value: str

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
class GoogleCloudDialogflowCxV3Experiment(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "DRAFT", "RUNNING", "DONE", "ROLLOUT_FAILED"
    ]
    variantsHistory: _list[GoogleCloudDialogflowCxV3VariantsHistory]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentDefinition(
    typing_extensions.TypedDict, total=False
):
    condition: str
    versionVariants: GoogleCloudDialogflowCxV3VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentResult(
    typing_extensions.TypedDict, total=False
):
    lastUpdateTime: str
    versionMetrics: _list[GoogleCloudDialogflowCxV3ExperimentResultVersionMetrics]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentResultConfidenceInterval(
    typing_extensions.TypedDict, total=False
):
    confidenceLevel: float
    lowerBound: float
    ratio: float
    upperBound: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentResultMetric(
    typing_extensions.TypedDict, total=False
):
    confidenceInterval: GoogleCloudDialogflowCxV3ExperimentResultConfidenceInterval
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
class GoogleCloudDialogflowCxV3ExperimentResultVersionMetrics(
    typing_extensions.TypedDict, total=False
):
    metrics: _list[GoogleCloudDialogflowCxV3ExperimentResultMetric]
    sessionCount: int
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON_PACKAGE"
    ]
    environment: str
    gitDestination: GoogleCloudDialogflowCxV3ExportAgentRequestGitDestination
    includeBigqueryExportSettings: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportAgentRequestGitDestination(
    typing_extensions.TypedDict, total=False
):
    commitMessage: str
    trackingBranch: str

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
class GoogleCloudDialogflowCxV3ExportEntityTypesRequest(
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
class GoogleCloudDialogflowCxV3ExportEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3InlineDestination
    entityTypesUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportFlowRequest(
    typing_extensions.TypedDict, total=False
):
    flowUri: str
    includeReferencedFlows: bool

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
class GoogleCloudDialogflowCxV3ExportIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON", "CSV"
    ]
    intents: _list[str]
    intentsContentInline: bool
    intentsUri: str

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
class GoogleCloudDialogflowCxV3ExportTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal["DATA_FORMAT_UNSPECIFIED", "BLOB", "JSON"]
    filter: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    content: str
    gcsUri: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3FilterSpecs(typing_extensions.TypedDict, total=False):
    dataStores: _list[str]
    filter: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Flow(typing_extensions.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    description: str
    displayName: str
    eventHandlers: _list[GoogleCloudDialogflowCxV3EventHandler]
    knowledgeConnectorSettings: GoogleCloudDialogflowCxV3KnowledgeConnectorSettings
    locked: bool
    multiLanguageSettings: GoogleCloudDialogflowCxV3FlowMultiLanguageSettings
    name: str
    nluSettings: GoogleCloudDialogflowCxV3NluSettings
    transitionRouteGroups: _list[str]
    transitionRoutes: _list[GoogleCloudDialogflowCxV3TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowImportStrategy(
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
class GoogleCloudDialogflowCxV3FlowMultiLanguageSettings(
    typing_extensions.TypedDict, total=False
):
    enableMultiLanguageDetection: bool
    supportedResponseLanguageCodes: _list[str]

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowValidationResult(
    typing_extensions.TypedDict, total=False
):
    name: str
    updateTime: str
    validationMessages: _list[GoogleCloudDialogflowCxV3ValidationMessage]

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
class GoogleCloudDialogflowCxV3FulfillIntentRequest(
    typing_extensions.TypedDict, total=False
):
    match: GoogleCloudDialogflowCxV3Match
    matchIntentRequest: GoogleCloudDialogflowCxV3MatchIntentRequest
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillIntentResponse(
    typing_extensions.TypedDict, total=False
):
    outputAudio: str
    outputAudioConfig: GoogleCloudDialogflowCxV3OutputAudioConfig
    queryResult: GoogleCloudDialogflowCxV3QueryResult
    responseId: str

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
class GoogleCloudDialogflowCxV3GenerativeSettings(
    typing_extensions.TypedDict, total=False
):
    fallbackSettings: GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettings
    generativeSafetySettings: GoogleCloudDialogflowCxV3SafetySettings
    knowledgeConnectorSettings: (
        GoogleCloudDialogflowCxV3GenerativeSettingsKnowledgeConnectorSettings
    )
    languageCode: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettings(
    typing_extensions.TypedDict, total=False
):
    promptTemplates: _list[
        GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettingsPromptTemplate
    ]
    selectedPrompt: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3GenerativeSettingsFallbackSettingsPromptTemplate(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    frozen: bool
    promptText: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3GenerativeSettingsKnowledgeConnectorSettings(
    typing_extensions.TypedDict, total=False
):
    agent: str
    agentIdentity: str
    agentScope: str
    business: str
    businessDescription: str
    disableDataStoreFallback: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3Generator(typing_extensions.TypedDict, total=False):
    displayName: str
    modelParameter: GoogleCloudDialogflowCxV3GeneratorModelParameter
    name: str
    placeholders: _list[GoogleCloudDialogflowCxV3GeneratorPlaceholder]
    promptText: GoogleCloudDialogflowCxV3Phrase

@typing.type_check_only
class GoogleCloudDialogflowCxV3GeneratorModelParameter(
    typing_extensions.TypedDict, total=False
):
    maxDecodeSteps: int
    temperature: float
    topK: int
    topP: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3GeneratorPlaceholder(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ImportEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    entityTypesContent: GoogleCloudDialogflowCxV3InlineSource
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
class GoogleCloudDialogflowCxV3ImportFlowRequest(
    typing_extensions.TypedDict, total=False
):
    flowContent: str
    flowImportStrategy: GoogleCloudDialogflowCxV3FlowImportStrategy
    flowUri: str
    importOption: typing_extensions.Literal[
        "IMPORT_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"
    ]

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
class GoogleCloudDialogflowCxV3ImportIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    intentsContent: GoogleCloudDialogflowCxV3InlineSource
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
class GoogleCloudDialogflowCxV3ImportTestCasesRequest(
    typing_extensions.TypedDict, total=False
):
    content: str
    gcsUri: str

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
class GoogleCloudDialogflowCxV3InlineSource(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3IntentCoverage(typing_extensions.TypedDict, total=False):
    coverageScore: float
    intents: _list[GoogleCloudDialogflowCxV3IntentCoverageIntent]

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentCoverageIntent(
    typing_extensions.TypedDict, total=False
):
    covered: bool
    intent: str

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
class GoogleCloudDialogflowCxV3ListAgentsResponse(
    typing_extensions.TypedDict, total=False
):
    agents: _list[GoogleCloudDialogflowCxV3Agent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListChangelogsResponse(
    typing_extensions.TypedDict, total=False
):
    changelogs: _list[GoogleCloudDialogflowCxV3Changelog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse(
    typing_extensions.TypedDict, total=False
):
    continuousTestResults: _list[GoogleCloudDialogflowCxV3ContinuousTestResult]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListDeploymentsResponse(
    typing_extensions.TypedDict, total=False
):
    deployments: _list[GoogleCloudDialogflowCxV3Deployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudDialogflowCxV3EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListEnvironmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowCxV3Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListExperimentsResponse(
    typing_extensions.TypedDict, total=False
):
    experiments: _list[GoogleCloudDialogflowCxV3Experiment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListFlowsResponse(
    typing_extensions.TypedDict, total=False
):
    flows: _list[GoogleCloudDialogflowCxV3Flow]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListGeneratorsResponse(
    typing_extensions.TypedDict, total=False
):
    generators: _list[GoogleCloudDialogflowCxV3Generator]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: _list[GoogleCloudDialogflowCxV3Intent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListPagesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pages: _list[GoogleCloudDialogflowCxV3Page]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListSecuritySettingsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securitySettings: _list[GoogleCloudDialogflowCxV3SecuritySettings]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3SessionEntityType]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTestCaseResultsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    testCaseResults: _list[GoogleCloudDialogflowCxV3TestCaseResult]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    testCases: _list[GoogleCloudDialogflowCxV3TestCase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    transitionRouteGroups: _list[GoogleCloudDialogflowCxV3TransitionRouteGroup]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    versions: _list[GoogleCloudDialogflowCxV3Version]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListWebhooksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    webhooks: _list[GoogleCloudDialogflowCxV3Webhook]

@typing.type_check_only
class GoogleCloudDialogflowCxV3LoadVersionRequest(
    typing_extensions.TypedDict, total=False
):
    allowOverrideAgentResources: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse(
    typing_extensions.TypedDict, total=False
):
    environments: _list[GoogleCloudDialogflowCxV3Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3Match(typing_extensions.TypedDict, total=False):
    confidence: float
    event: str
    intent: GoogleCloudDialogflowCxV3Intent
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
class GoogleCloudDialogflowCxV3MatchIntentRequest(
    typing_extensions.TypedDict, total=False
):
    persistParameterChanges: bool
    queryInput: GoogleCloudDialogflowCxV3QueryInput
    queryParams: GoogleCloudDialogflowCxV3QueryParameters

@typing.type_check_only
class GoogleCloudDialogflowCxV3MatchIntentResponse(
    typing_extensions.TypedDict, total=False
):
    currentPage: GoogleCloudDialogflowCxV3Page
    matches: _list[GoogleCloudDialogflowCxV3Match]
    text: str
    transcript: str
    triggerEvent: str
    triggerIntent: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3NluSettings(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDialogflowCxV3OutputAudioConfig(
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
    synthesizeSpeechConfig: GoogleCloudDialogflowCxV3SynthesizeSpeechConfig

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
class GoogleCloudDialogflowCxV3Phrase(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3QueryInput(typing_extensions.TypedDict, total=False):
    audio: GoogleCloudDialogflowCxV3AudioInput
    dtmf: GoogleCloudDialogflowCxV3DtmfInput
    event: GoogleCloudDialogflowCxV3EventInput
    intent: GoogleCloudDialogflowCxV3IntentInput
    languageCode: str
    text: GoogleCloudDialogflowCxV3TextInput

@typing.type_check_only
class GoogleCloudDialogflowCxV3QueryParameters(
    typing_extensions.TypedDict, total=False
):
    analyzeQueryTextSentiment: bool
    channel: str
    currentPage: str
    disableWebhook: bool
    endUserMetadata: dict[str, typing.Any]
    flowVersions: _list[str]
    geoLocation: GoogleTypeLatLng
    parameters: dict[str, typing.Any]
    payload: dict[str, typing.Any]
    populateDataStoreConnectionSignals: bool
    searchConfig: GoogleCloudDialogflowCxV3SearchConfig
    sessionEntityTypes: _list[GoogleCloudDialogflowCxV3SessionEntityType]
    sessionTtl: str
    timeZone: str
    webhookHeaders: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3QueryResult(typing_extensions.TypedDict, total=False):
    advancedSettings: GoogleCloudDialogflowCxV3AdvancedSettings
    allowAnswerFeedback: bool
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
    transcript: str
    triggerEvent: str
    triggerIntent: str
    webhookPayloads: _list[dict[str, typing.Any]]
    webhookStatuses: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDialogflowCxV3ResourceName(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str

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
class GoogleCloudDialogflowCxV3RestoreAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str
    gitSource: GoogleCloudDialogflowCxV3RestoreAgentRequestGitSource
    restoreOption: typing_extensions.Literal[
        "RESTORE_OPTION_UNSPECIFIED", "KEEP", "FALLBACK"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RestoreAgentRequestGitSource(
    typing_extensions.TypedDict, total=False
):
    trackingBranch: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3RolloutConfig(typing_extensions.TypedDict, total=False):
    failureCondition: str
    rolloutCondition: str
    rolloutSteps: _list[GoogleCloudDialogflowCxV3RolloutConfigRolloutStep]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RolloutConfigRolloutStep(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    minDuration: str
    trafficPercent: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3RolloutState(typing_extensions.TypedDict, total=False):
    startTime: str
    step: str
    stepIndex: int

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudDialogflowCxV3TestError]

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunContinuousTestRequest(
    typing_extensions.TypedDict, total=False
): ...

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
class GoogleCloudDialogflowCxV3RunTestCaseRequest(
    typing_extensions.TypedDict, total=False
):
    environment: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3RunTestCaseResponse(
    typing_extensions.TypedDict, total=False
):
    result: GoogleCloudDialogflowCxV3TestCaseResult

@typing.type_check_only
class GoogleCloudDialogflowCxV3SafetySettings(typing_extensions.TypedDict, total=False):
    bannedPhrases: _list[GoogleCloudDialogflowCxV3SafetySettingsPhrase]

@typing.type_check_only
class GoogleCloudDialogflowCxV3SafetySettingsPhrase(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SearchConfig(typing_extensions.TypedDict, total=False):
    boostSpecs: _list[GoogleCloudDialogflowCxV3BoostSpecs]
    filterSpecs: _list[GoogleCloudDialogflowCxV3FilterSpecs]

@typing.type_check_only
class GoogleCloudDialogflowCxV3SecuritySettings(
    typing_extensions.TypedDict, total=False
):
    audioExportSettings: GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettings
    deidentifyTemplate: str
    displayName: str
    insightsExportSettings: (
        GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettings
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
class GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettings(
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
class GoogleCloudDialogflowCxV3SecuritySettingsInsightsExportSettings(
    typing_extensions.TypedDict, total=False
):
    enableInsightsExport: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudDialogflowCxV3SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDialogflowCxV3EntityTypeEntity]
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SessionInfo(typing_extensions.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    session: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SpeechToTextSettings(
    typing_extensions.TypedDict, total=False
):
    enableSpeechAdaptation: bool

@typing.type_check_only
class GoogleCloudDialogflowCxV3StartExperimentRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3StopExperimentRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest(
    typing_extensions.TypedDict, total=False
):
    answerFeedback: GoogleCloudDialogflowCxV3AnswerFeedback
    responseId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3SynthesizeSpeechConfig(
    typing_extensions.TypedDict, total=False
):
    effectsProfileId: _list[str]
    pitch: float
    speakingRate: float
    voice: GoogleCloudDialogflowCxV3VoiceSelectionParams
    volumeGainDb: float

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
class GoogleCloudDialogflowCxV3TextToSpeechSettings(
    typing_extensions.TypedDict, total=False
):
    synthesizeSpeechConfigs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TrainFlowRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionCoverage(
    typing_extensions.TypedDict, total=False
):
    coverageScore: float
    transitions: _list[GoogleCloudDialogflowCxV3TransitionCoverageTransition]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionCoverageTransition(
    typing_extensions.TypedDict, total=False
):
    covered: bool
    eventHandler: GoogleCloudDialogflowCxV3EventHandler
    index: int
    source: GoogleCloudDialogflowCxV3TransitionCoverageTransitionNode
    target: GoogleCloudDialogflowCxV3TransitionCoverageTransitionNode
    transitionRoute: GoogleCloudDialogflowCxV3TransitionRoute

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionCoverageTransitionNode(
    typing_extensions.TypedDict, total=False
):
    flow: GoogleCloudDialogflowCxV3Flow
    page: GoogleCloudDialogflowCxV3Page

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
class GoogleCloudDialogflowCxV3TransitionRouteGroup(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    transitionRoutes: _list[GoogleCloudDialogflowCxV3TransitionRoute]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRouteGroupCoverage(
    typing_extensions.TypedDict, total=False
):
    coverageScore: float
    coverages: _list[GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverage]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverage(
    typing_extensions.TypedDict, total=False
):
    coverageScore: float
    routeGroup: GoogleCloudDialogflowCxV3TransitionRouteGroup
    transitions: _list[
        GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransition
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRouteGroupCoverageCoverageTransition(
    typing_extensions.TypedDict, total=False
):
    covered: bool
    transitionRoute: GoogleCloudDialogflowCxV3TransitionRoute

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
class GoogleCloudDialogflowCxV3ValidateAgentRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ValidateFlowRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3ValidationMessage(
    typing_extensions.TypedDict, total=False
):
    detail: str
    resourceNames: _list[GoogleCloudDialogflowCxV3ResourceName]
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
class GoogleCloudDialogflowCxV3VariantsHistory(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    versionVariants: GoogleCloudDialogflowCxV3VersionVariants

@typing.type_check_only
class GoogleCloudDialogflowCxV3Version(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    nluSettings: GoogleCloudDialogflowCxV3NluSettings
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDialogflowCxV3VersionVariants(
    typing_extensions.TypedDict, total=False
):
    variants: _list[GoogleCloudDialogflowCxV3VersionVariantsVariant]

@typing.type_check_only
class GoogleCloudDialogflowCxV3VersionVariantsVariant(
    typing_extensions.TypedDict, total=False
):
    isControlGroup: bool
    trafficAllocation: float
    version: str

@typing.type_check_only
class GoogleCloudDialogflowCxV3VoiceSelectionParams(
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
