import typing

_list = list

@typing.type_check_only
class GoogleCloudCesV1mainAgentTransfer(typing.TypedDict, total=False):
    displayName: str
    targetAgent: str

@typing.type_check_only
class GoogleCloudCesV1mainBlob(typing.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudCesV1mainChunk(typing.TypedDict, total=False):
    agentTransfer: GoogleCloudCesV1mainAgentTransfer
    blob: GoogleCloudCesV1mainBlob
    defaultVariables: dict[str, typing.Any]
    image: GoogleCloudCesV1mainImage
    payload: dict[str, typing.Any]
    text: str
    toolCall: GoogleCloudCesV1mainToolCall
    toolResponse: GoogleCloudCesV1mainToolResponse
    transcript: str
    updatedVariables: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudCesV1mainEndSession(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudCesV1mainImage(typing.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudCesV1mainMessage(typing.TypedDict, total=False):
    chunks: _list[GoogleCloudCesV1mainChunk]
    eventTime: str
    role: str

@typing.type_check_only
class GoogleCloudCesV1mainSpan(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    childSpans: _list[GoogleCloudCesV1mainSpan]
    duration: str
    endTime: str
    name: str
    startTime: str

@typing.type_check_only
class GoogleCloudCesV1mainToolCall(typing.TypedDict, total=False):
    agentName: str
    args: dict[str, typing.Any]
    displayName: str
    id: str
    parentToolCallId: str
    tool: str
    toolsetTool: GoogleCloudCesV1mainToolsetTool

@typing.type_check_only
class GoogleCloudCesV1mainToolResponse(typing.TypedDict, total=False):
    agentName: str
    displayName: str
    id: str
    parentToolCallId: str
    response: dict[str, typing.Any]
    tool: str
    toolsetTool: GoogleCloudCesV1mainToolsetTool

@typing.type_check_only
class GoogleCloudCesV1mainToolsetTool(typing.TypedDict, total=False):
    toolId: str
    toolset: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Analysis(typing.TypedDict, total=False):
    analysisResult: GoogleCloudContactcenterinsightsV1AnalysisResult
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    createTime: str
    name: str
    requestTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisResult(typing.TypedDict, total=False):
    callAnalysisMetadata: (
        GoogleCloudContactcenterinsightsV1AnalysisResultCallAnalysisMetadata
    )
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisResultCallAnalysisMetadata(
    typing.TypedDict, total=False
):
    annotations: _list[GoogleCloudContactcenterinsightsV1CallAnnotation]
    entities: dict[str, typing.Any]
    intents: dict[str, typing.Any]
    issueModelResult: GoogleCloudContactcenterinsightsV1IssueModelResult
    phraseMatchers: dict[str, typing.Any]
    qaScorecardResults: _list[GoogleCloudContactcenterinsightsV1QaScorecardResult]
    sentiments: _list[GoogleCloudContactcenterinsightsV1ConversationLevelSentiment]
    silence: GoogleCloudContactcenterinsightsV1ConversationLevelSilence

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisRule(typing.TypedDict, total=False):
    active: bool
    analysisPercentage: float
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    conversationFilter: str
    createTime: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotationBoundary(
    typing.TypedDict, total=False
):
    transcriptIndex: int
    wordIndex: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotatorSelector(
    typing.TypedDict, total=False
):
    issueModels: _list[str]
    phraseMatchers: _list[str]
    qaConfig: GoogleCloudContactcenterinsightsV1AnnotatorSelectorQaConfig
    runAutoLabelingAnnotator: bool
    runEntityAnnotator: bool
    runIntentAnnotator: bool
    runInterruptionAnnotator: bool
    runIssueModelAnnotator: bool
    runPhraseMatcherAnnotator: bool
    runQaAnnotator: bool
    runSentimentAnnotator: bool
    runSilenceAnnotator: bool
    runSummarizationAnnotator: bool
    summarizationConfig: (
        GoogleCloudContactcenterinsightsV1AnnotatorSelectorSummarizationConfig
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotatorSelectorQaConfig(
    typing.TypedDict, total=False
):
    scorecardList: (
        GoogleCloudContactcenterinsightsV1AnnotatorSelectorQaConfigScorecardList
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotatorSelectorQaConfigScorecardList(
    typing.TypedDict, total=False
):
    qaScorecardRevisions: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotatorSelectorSummarizationConfig(
    typing.TypedDict, total=False
):
    conversationProfile: str
    generator: str
    summarizationModel: typing.Literal[
        "SUMMARIZATION_MODEL_UNSPECIFIED", "BASELINE_MODEL", "BASELINE_MODEL_V2_0"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnswerFeedback(typing.TypedDict, total=False):
    clicked: bool
    correctnessLevel: typing.Literal[
        "CORRECTNESS_LEVEL_UNSPECIFIED",
        "NOT_CORRECT",
        "PARTIALLY_CORRECT",
        "FULLY_CORRECT",
    ]
    displayed: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AppealAssessmentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ArticleSuggestionData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    source: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Assessment(typing.TypedDict, total=False):
    agentInfo: GoogleCloudContactcenterinsightsV1ConversationQualityMetadataAgentInfo
    createTime: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DRAFT", "PUBLISHED", "APPEALED", "FINALIZED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AssessmentRule(typing.TypedDict, total=False):
    active: bool
    createTime: str
    displayName: str
    name: str
    sampleRule: GoogleCloudContactcenterinsightsV1SampleRule
    scheduleInfo: GoogleCloudContactcenterinsightsV1ScheduleInfo
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AssistantChunk(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AssistantMessage(typing.TypedDict, total=False):
    chunks: _list[GoogleCloudContactcenterinsightsV1AssistantChunk]
    eventTime: str
    role: typing.Literal["ROLE_UNSPECIFIED", "USER", "MODEL"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AssistantSession(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    messages: _list[GoogleCloudContactcenterinsightsV1AssistantMessage]
    name: str
    requester: str
    state: typing.Literal["STATE_UNSPECIFIED", "PROCESSING", "IDLE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AuthorizedView(typing.TypedDict, total=False):
    conversationFilter: str
    createTime: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AuthorizedViewSet(
    typing.TypedDict, total=False
):
    createTime: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AutoLabelingRule(typing.TypedDict, total=False):
    active: bool
    conditions: _list[
        GoogleCloudContactcenterinsightsV1AutoLabelingRuleLabelingCondition
    ]
    createTime: str
    description: str
    displayName: str
    labelKey: str
    labelKeyType: typing.Literal["LABEL_KEY_TYPE_UNSPECIFIED", "LABEL_KEY_TYPE_CUSTOM"]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AutoLabelingRuleLabelingCondition(
    typing.TypedDict, total=False
):
    condition: str
    value: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsMetadata(
    typing.TypedDict, total=False
):
    completedAnalysesCount: int
    createTime: str
    endTime: str
    failedAnalysesCount: int
    partialErrors: _list[GoogleRpcStatus]
    relabel: bool
    request: GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsRequest
    totalRequestedAnalysesCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsRequest(
    typing.TypedDict, total=False
):
    analysisPercentage: float
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    filter: str
    parent: str
    relabel: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsResponse(
    typing.TypedDict, total=False
):
    failedAnalysisCount: int
    successfulAnalysisCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest(
    typing.TypedDict, total=False
):
    filter: str
    force: bool
    maxDeleteCount: int
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteFeedbackLabelsMetadata(
    typing.TypedDict, total=False
):
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1BulkDeleteFeedbackLabelsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteFeedbackLabelsRequest(
    typing.TypedDict, total=False
):
    filter: str
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteFeedbackLabelsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    downloadStats: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsMetadataDownloadStats
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsMetadataDownloadStats(
    typing.TypedDict, total=False
):
    fileNames: _list[str]
    processedObjectCount: int
    successfulDownloadCount: int
    totalFilesWritten: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequest(
    typing.TypedDict, total=False
):
    conversationFilter: str
    feedbackLabelType: typing.Literal[
        "FEEDBACK_LABEL_TYPE_UNSPECIFIED",
        "QUALITY_AI",
        "TOPIC_MODELING",
        "AGENT_ASSIST_SUMMARY",
    ]
    filter: str
    gcsDestination: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequestGcsDestination
    maxDownloadCount: int
    parent: str
    sheetsDestination: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequestSheetsDestination
    templateQaScorecardId: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequestGcsDestination(
    typing.TypedDict, total=False
):
    addWhitespace: bool
    alwaysPrintEmptyFields: bool
    format: typing.Literal["FORMAT_UNSPECIFIED", "CSV", "JSON"]
    objectUri: str
    recordsPerFileCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequestSheetsDestination(
    typing.TypedDict, total=False
):
    sheetTitle: str
    spreadsheetUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequest(
    typing.TypedDict, total=False
):
    gcsSource: (
        GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequestGcsSource
    )
    sheetsSource: (
        GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequestSheetsSource
    )
    validateOnly: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequestGcsSource(
    typing.TypedDict, total=False
):
    format: typing.Literal["FORMAT_UNSPECIFIED", "CSV", "JSON"]
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequestSheetsSource(
    typing.TypedDict, total=False
):
    spreadsheetUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponse(
    typing.TypedDict, total=False
):
    currentStats: GoogleCloudContactcenterinsightsV1IssueModelLabelStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsRequest(
    typing.TypedDict, total=False
):
    filter: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsResponse(
    typing.TypedDict, total=False
):
    averageDuration: str
    averageTurnCount: int
    conversationCount: int
    conversationCountTimeSeries: (
        GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeries
    )
    customHighlighterMatches: dict[str, typing.Any]
    issueMatches: dict[str, typing.Any]
    issueMatchesStats: dict[str, typing.Any]
    smartHighlighterMatches: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeries(
    typing.TypedDict, total=False
):
    intervalDuration: str
    points: _list[
        GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeriesInterval
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeriesInterval(
    typing.TypedDict, total=False
):
    conversationCount: int
    startTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CallAnnotation(typing.TypedDict, total=False):
    annotationEndBoundary: GoogleCloudContactcenterinsightsV1AnnotationBoundary
    annotationStartBoundary: GoogleCloudContactcenterinsightsV1AnnotationBoundary
    channelTag: int
    entityMentionData: GoogleCloudContactcenterinsightsV1EntityMentionData
    holdData: GoogleCloudContactcenterinsightsV1HoldData
    intentMatchData: GoogleCloudContactcenterinsightsV1IntentMatchData
    interruptionData: GoogleCloudContactcenterinsightsV1InterruptionData
    issueMatchData: GoogleCloudContactcenterinsightsV1IssueMatchData
    phraseMatchData: GoogleCloudContactcenterinsightsV1PhraseMatchData
    sentimentData: GoogleCloudContactcenterinsightsV1SentimentData
    silenceData: GoogleCloudContactcenterinsightsV1SilenceData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CesEndSessionAnnotation(
    typing.TypedDict, total=False
):
    endSession: GoogleCloudCesV1mainEndSession

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CesTurnAnnotation(
    typing.TypedDict, total=False
):
    messages: _list[GoogleCloudCesV1mainMessage]
    rootSpan: GoogleCloudCesV1mainSpan

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Chart(typing.TypedDict, total=False):
    action: GoogleCloudContactcenterinsightsV1ChartAction
    chartType: typing.Literal[
        "CHART_TYPE_UNSPECIFIED", "SYSTEM_DEFINED", "USER_DEFINED"
    ]
    chartVisualizationType: typing.Literal[
        "CHART_VISUALIZATION_TYPE_UNSPECIFIED",
        "BAR",
        "LINE",
        "AREA",
        "PIE",
        "SCATTER",
        "TABLE",
        "SCORE_CARD",
        "SUNBURST",
        "GAUGE",
        "SANKEY",
    ]
    createTime: str
    dataSource: GoogleCloudContactcenterinsightsV1ChartDataSource
    dateRangeConfig: GoogleCloudContactcenterinsightsV1DateRangeConfig
    description: str
    displayName: str
    filter: str
    height: int
    name: str
    updateTime: str
    width: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ChartAction(typing.TypedDict, total=False):
    conversationFilter: str
    redirectAction: GoogleCloudContactcenterinsightsV1RedirectAction

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ChartDataSource(typing.TypedDict, total=False):
    generativeInsights: GoogleCloudContactcenterinsightsV1GenerativeInsights
    queryMetrics: GoogleCloudContactcenterinsightsV1QueryMetrics

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConstraintEvaluationResult(
    typing.TypedDict, total=False
):
    conversationA: str
    conversationB: str
    ruleConstraintResults: _list[
        GoogleCloudContactcenterinsightsV1ConstraintEvaluationResultRuleConstraintResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConstraintEvaluationResultRuleConstraintResult(
    typing.TypedDict, total=False
):
    constraintMet: bool
    error: GoogleRpcStatus
    ruleId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Container(typing.TypedDict, total=False):
    containerId: str
    dateRangeConfig: GoogleCloudContactcenterinsightsV1DateRangeConfig
    description: str
    displayName: str
    filter: str
    height: int
    widgets: _list[GoogleCloudContactcenterinsightsV1Widget]
    width: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Conversation(typing.TypedDict, total=False):
    agentId: str
    callMetadata: GoogleCloudContactcenterinsightsV1ConversationCallMetadata
    correlationInfo: GoogleCloudContactcenterinsightsV1ConversationCorrelationInfo
    createTime: str
    dataSource: GoogleCloudContactcenterinsightsV1ConversationDataSource
    dialogflowIntents: dict[str, typing.Any]
    duration: str
    expireTime: str
    labels: dict[str, typing.Any]
    languageCode: str
    latestAnalysis: GoogleCloudContactcenterinsightsV1Analysis
    latestSummary: (
        GoogleCloudContactcenterinsightsV1ConversationSummarizationSuggestionData
    )
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    metadataJson: str
    name: str
    obfuscatedUserId: str
    qualityMetadata: GoogleCloudContactcenterinsightsV1ConversationQualityMetadata
    runtimeAnnotations: _list[GoogleCloudContactcenterinsightsV1RuntimeAnnotation]
    startTime: str
    transcript: GoogleCloudContactcenterinsightsV1ConversationTranscript
    ttl: str
    turnCount: int
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationCallMetadata(
    typing.TypedDict, total=False
):
    agentChannel: int
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationCorrelationInfo(
    typing.TypedDict, total=False
):
    correlationTypes: _list[
        typing.Literal[
            "CORRELATION_TYPE_UNSPECIFIED", "SEGMENT", "PARTIAL", "FULL", "SYNTHETIC"
        ]
    ]
    fullConversationCorrelationId: str
    mergedFullConversationCorrelationId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationCorrelationResult(
    typing.TypedDict, total=False
):
    conversation: str
    ruleResults: _list[
        GoogleCloudContactcenterinsightsV1ConversationCorrelationResultRuleCorrelationResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationCorrelationResultRuleCorrelationResult(
    typing.TypedDict, total=False
):
    correlationId: str
    error: GoogleRpcStatus
    ruleId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationDataOptions(
    typing.TypedDict, total=False
):
    includeDialogflowInteractionData: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationDataSource(
    typing.TypedDict, total=False
):
    dialogflowSource: GoogleCloudContactcenterinsightsV1DialogflowSource
    gcsSource: GoogleCloudContactcenterinsightsV1GcsSource
    metadataUri: str
    turnLevelAudios: _list[
        GoogleCloudContactcenterinsightsV1ConversationDataSourceTurnLevelAudio
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationDataSourceTurnLevelAudio(
    typing.TypedDict, total=False
):
    audioDuration: str
    audioGcsUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationLevelSentiment(
    typing.TypedDict, total=False
):
    channelTag: int
    sentimentData: GoogleCloudContactcenterinsightsV1SentimentData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationLevelSilence(
    typing.TypedDict, total=False
):
    silenceDuration: str
    silencePercentage: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationParticipant(
    typing.TypedDict, total=False
):
    dialogflowParticipant: str
    dialogflowParticipantName: str
    obfuscatedExternalUserId: str
    role: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    userId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationQualityMetadata(
    typing.TypedDict, total=False
):
    agentInfo: _list[
        GoogleCloudContactcenterinsightsV1ConversationQualityMetadataAgentInfo
    ]
    customerSatisfactionRating: int
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1FeedbackLabel]
    menuPath: str
    waitDuration: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationQualityMetadataAgentInfo(
    typing.TypedDict, total=False
):
    agentId: str
    agentType: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    deploymentDisplayName: str
    deploymentId: str
    displayName: str
    dispositionCode: str
    entrySubagentDisplayName: str
    entrySubagentId: str
    location: str
    team: str
    teams: _list[str]
    versionDisplayName: str
    versionId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationSummarizationSuggestionData(
    typing.TypedDict, total=False
):
    answerRecord: str
    confidence: float
    conversationModel: str
    generatorId: str
    metadata: dict[str, typing.Any]
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscript(
    typing.TypedDict, total=False
):
    transcriptSegments: _list[
        GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegment
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegment(
    typing.TypedDict, total=False
):
    channelTag: int
    confidence: float
    dialogflowSegmentMetadata: GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata
    languageCode: str
    messageTime: str
    segmentParticipant: GoogleCloudContactcenterinsightsV1ConversationParticipant
    sentiment: GoogleCloudContactcenterinsightsV1SentimentData
    text: str
    turnLevelAudio: (
        GoogleCloudContactcenterinsightsV1ConversationDataSourceTurnLevelAudio
    )
    words: _list[
        GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentWordInfo
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata(
    typing.TypedDict, total=False
):
    smartReplyAllowlistCovered: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentWordInfo(
    typing.TypedDict, total=False
):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CorrelationConfig(
    typing.TypedDict, total=False
):
    createTime: str
    fullConversationConfig: GoogleCloudContactcenterinsightsV1CorrelationTypeConfig
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CorrelationRule(typing.TypedDict, total=False):
    active: bool
    constraintExpression: str
    joinKeyExpression: str
    ruleId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CorrelationTypeConfig(
    typing.TypedDict, total=False
):
    correlationRules: _list[GoogleCloudContactcenterinsightsV1CorrelationRule]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateAnalysisOperationMetadata(
    typing.TypedDict, total=False
):
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    conversation: str
    createTime: str
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1CreateIssueRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1CreateIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueModelRequest(
    typing.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1IssueModel
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueRequest(
    typing.TypedDict, total=False
):
    issue: GoogleCloudContactcenterinsightsV1Issue
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Dashboard(typing.TypedDict, total=False):
    createTime: str
    dateRangeConfig: GoogleCloudContactcenterinsightsV1DateRangeConfig
    description: str
    displayName: str
    filter: str
    name: str
    readOnly: bool
    rootContainer: GoogleCloudContactcenterinsightsV1Container
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Dataset(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    ttl: str
    type: typing.Literal["TYPE_UNSPECIFIED", "EVAL", "LIVE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DateRangeConfig(typing.TypedDict, total=False):
    absoluteDateRange: GoogleCloudContactcenterinsightsV1QueryInterval
    relativeDateRange: (
        GoogleCloudContactcenterinsightsV1DateRangeConfigRelativeDateRange
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DateRangeConfigRelativeDateRange(
    typing.TypedDict, total=False
):
    quantity: str
    unit: typing.Literal[
        "TIME_UNIT_UNSPECIFIED", "DAY", "WEEK", "MONTH", "QUARTER", "YEAR"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeleteIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1DeleteIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeleteIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeleteQaQuestionTagMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1DeleteQaQuestionTagRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeleteQaQuestionTagRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1DeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployQaScorecardRevisionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DialogflowIntent(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DialogflowInteractionData(
    typing.TypedDict, total=False
):
    confidence: float
    dialogflowIntentId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DialogflowSource(typing.TypedDict, total=False):
    audioUri: str
    dialogflowConversation: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Dimension(typing.TypedDict, total=False):
    agentDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionAgentDimensionMetadata
    )
    clientSentimentCategoryDimensionMetadata: GoogleCloudContactcenterinsightsV1DimensionClientSentimentCategoryDimensionMetadata
    conversationProfileDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionConversationProfileDimensionMetadata
    )
    conversationalAgentsPlaybookDimensionMetadata: GoogleCloudContactcenterinsightsV1DimensionConversationalAgentsPlaybookDimensionMetadata
    conversationalAgentsToolDimensionMetadata: GoogleCloudContactcenterinsightsV1DimensionConversationalAgentsToolDimensionMetadata
    dimensionKey: typing.Literal[
        "DIMENSION_KEY_UNSPECIFIED",
        "ISSUE",
        "ISSUE_NAME",
        "AGENT",
        "AGENT_TEAM",
        "QA_QUESTION_ID",
        "QA_QUESTION_ANSWER_VALUE",
        "QA_SCORECARD_ID",
        "CONVERSATION_PROFILE_ID",
        "MEDIUM",
        "CONVERSATIONAL_AGENTS_PLAYBOOK_ID",
        "CONVERSATIONAL_AGENTS_PLAYBOOK_NAME",
        "CONVERSATIONAL_AGENTS_TOOL_ID",
        "CONVERSATIONAL_AGENTS_TOOL_NAME",
        "CLIENT_SENTIMENT_CATEGORY",
        "AGENT_VERSION_ID",
        "AGENT_DEPLOYMENT_ID",
        "AGENT_ASSIST_SUPERVISOR_ID",
        "LABEL_KEY",
        "LABEL_VALUE",
        "LABEL_KEY_AND_VALUE",
        "LAST_TRANSFER_SUB_AGENT_NAME",
    ]
    issueDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionIssueDimensionMetadata
    )
    labelDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionLabelDimensionMetadata
    )
    mediumDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionMediumDimensionMetadata
    )
    qaQuestionAnswerDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionQaQuestionAnswerDimensionMetadata
    )
    qaQuestionDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionQaQuestionDimensionMetadata
    )
    qaScorecardDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionQaScorecardDimensionMetadata
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionAgentDimensionMetadata(
    typing.TypedDict, total=False
):
    agentDeploymentDisplayName: str
    agentDeploymentId: str
    agentDisplayName: str
    agentId: str
    agentTeam: str
    agentVersionDisplayName: str
    agentVersionId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionClientSentimentCategoryDimensionMetadata(
    typing.TypedDict, total=False
):
    sentimentCategory: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionConversationProfileDimensionMetadata(
    typing.TypedDict, total=False
):
    conversationProfileId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionConversationalAgentsPlaybookDimensionMetadata(
    typing.TypedDict, total=False
):
    playbookDisplayName: str
    playbookId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionConversationalAgentsToolDimensionMetadata(
    typing.TypedDict, total=False
):
    toolDisplayName: str
    toolId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionIssueDimensionMetadata(
    typing.TypedDict, total=False
):
    issueDisplayName: str
    issueId: str
    issueModelId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionLabelDimensionMetadata(
    typing.TypedDict, total=False
):
    labelKey: str
    labelValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionMediumDimensionMetadata(
    typing.TypedDict, total=False
):
    medium: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionQaQuestionAnswerDimensionMetadata(
    typing.TypedDict, total=False
):
    answerValue: str
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionQaQuestionDimensionMetadata(
    typing.TypedDict, total=False
):
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionQaScorecardDimensionMetadata(
    typing.TypedDict, total=False
):
    qaScorecardId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1EncryptionSpec(typing.TypedDict, total=False):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Entity(typing.TypedDict, total=False):
    displayName: str
    metadata: dict[str, typing.Any]
    salience: float
    sentiment: GoogleCloudContactcenterinsightsV1SentimentData
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "EVENT",
        "WORK_OF_ART",
        "CONSUMER_GOOD",
        "OTHER",
        "PHONE_NUMBER",
        "ADDRESS",
        "DATE",
        "NUMBER",
        "PRICE",
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1EntityMentionData(
    typing.TypedDict, total=False
):
    entityUniqueId: str
    sentiment: GoogleCloudContactcenterinsightsV1SentimentData
    type: typing.Literal["MENTION_TYPE_UNSPECIFIED", "PROPER", "COMMON"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExactMatchConfig(typing.TypedDict, total=False):
    caseSensitive: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataMetadata(
    typing.TypedDict, total=False
):
    completedExportCount: int
    createTime: str
    endTime: str
    failedExportCount: int
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest(
    typing.TypedDict, total=False
):
    bigQueryDestination: (
        GoogleCloudContactcenterinsightsV1ExportInsightsDataRequestBigQueryDestination
    )
    exportSchemaVersion: typing.Literal[
        "EXPORT_SCHEMA_VERSION_UNSPECIFIED",
        "EXPORT_V1",
        "EXPORT_V2",
        "EXPORT_V3",
        "EXPORT_V4",
        "EXPORT_V5",
        "EXPORT_V6",
        "EXPORT_V7",
        "EXPORT_V8",
        "EXPORT_V9",
        "EXPORT_V10",
        "EXPORT_V11",
        "EXPORT_V12",
        "EXPORT_V13",
        "EXPORT_V14",
        "EXPORT_V15",
        "EXPORT_V16",
        "EXPORT_V17",
        "EXPORT_VERSION_LATEST_AVAILABLE",
    ]
    filter: str
    kmsKey: str
    parent: str
    writeDisposition: typing.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataRequestBigQueryDestination(
    typing.TypedDict, total=False
):
    dataset: str
    projectId: str
    table: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1ExportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelRequest(
    typing.TypedDict, total=False
):
    gcsDestination: (
        GoogleCloudContactcenterinsightsV1ExportIssueModelRequestGcsDestination
    )
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelRequestGcsDestination(
    typing.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1FaqAnswerData(typing.TypedDict, total=False):
    answer: str
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    question: str
    source: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1FeedbackLabel(typing.TypedDict, total=False):
    createTime: str
    label: str
    labeledResource: str
    name: str
    qaAnswerLabel: GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1FinalizeAssessmentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GcsSource(typing.TypedDict, total=False):
    audioUri: str
    transcriptUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerateConversationSignedAudioResponse(
    typing.TypedDict, total=False
):
    signedAudioUris: GoogleCloudContactcenterinsightsV1SignedAudioUris

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscript(
    typing.TypedDict, total=False
):
    conversationId: str
    createTime: str
    messages: _list[
        GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessage
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessage(
    typing.TypedDict, total=False
):
    createTime: str
    messageId: str
    systemMessageWrapper: GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageSystemMessages
    userMessage: GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageUserMessage

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageSystemMessage(
    typing.TypedDict, total=False
):
    chartSpec: dict[str, typing.Any]
    generatedSqlQuery: str
    textMessage: GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageSystemMessageTextOutput
    userProvidedChartSpec: dict[str, typing.Any]
    userProvidedSqlQuery: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageSystemMessageTextOutput(
    typing.TypedDict, total=False
):
    text: _list[str]
    textType: typing.Literal[
        "TYPE_UNSPECIFIED", "THOUGHT", "FINAL_RESPONSE", "PROGRESS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageSystemMessages(
    typing.TypedDict, total=False
):
    systemMessages: _list[
        GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageSystemMessage
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscriptMessageUserMessage(
    typing.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsights(
    typing.TypedDict, total=False
):
    chartCheckpoint: GoogleCloudContactcenterinsightsV1GenerativeInsightsChartCheckpoint
    chartConversations: _list[
        GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversation
    ]
    chartSpec: dict[str, typing.Any]
    request: dict[str, typing.Any]
    sqlComparisonKey: str
    sqlQuery: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsChartCheckpoint(
    typing.TypedDict, total=False
):
    revisionId: str
    sessionId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversation(
    typing.TypedDict, total=False
):
    conversationId: str
    createTime: str
    messages: _list[
        GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessage
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessage(
    typing.TypedDict, total=False
):
    createTime: str
    messageId: str
    systemMessage: GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessageSystemMessage
    userMessage: GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessageUserMessage

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessageSystemMessage(
    typing.TypedDict, total=False
):
    chartSpec: dict[str, typing.Any]
    generatedSqlQuery: str
    textOutput: GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessageSystemMessageTextOutput

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessageSystemMessageTextOutput(
    typing.TypedDict, total=False
):
    texts: _list[str]
    type: typing.Literal["TYPE_UNSPECIFIED", "THOUGHT", "FINAL_RESPONSE", "PROGRESS"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsChartConversationMessageUserMessage(
    typing.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsMetadata(
    typing.TypedDict, total=False
):
    errorMessages: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsRequest(
    typing.TypedDict, total=False
):
    chart: str
    comparisonFilter: str
    filter: str
    naturalLanguageQuery: str
    revisionId: str
    sessionId: str
    sqlComparisonKey: str
    sqlQuery: str
    userProvidedChartSpec: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsResponse(
    typing.TypedDict, total=False
):
    generativeResponses: _list[
        GoogleCloudContactcenterinsightsV1GenerativeInsightsResponseGenerativeResponse
    ]
    transcript: (
        GoogleCloudContactcenterinsightsV1GenerativeInsightConversationTranscript
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsResponseGenerativeResponse(
    typing.TypedDict, total=False
):
    chartSpec: dict[str, typing.Any]
    generatedSqlQuery: str
    textMessage: GoogleCloudContactcenterinsightsV1GenerativeInsightsResponseGenerativeResponseTextOutput
    textOutput: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GenerativeInsightsResponseGenerativeResponseTextOutput(
    typing.TypedDict, total=False
):
    text: _list[str]
    textType: typing.Literal[
        "TYPE_UNSPECIFIED", "THOUGHT", "FINAL_RESPONSE", "PROGRESS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1HoldData(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1ImportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelRequest(
    typing.TypedDict, total=False
):
    createNewModel: bool
    gcsSource: GoogleCloudContactcenterinsightsV1ImportIssueModelRequestGcsSource
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelRequestGcsSource(
    typing.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelResponse(
    typing.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1IssueModel

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    ingestConversationsStats: GoogleCloudContactcenterinsightsV1IngestConversationsMetadataIngestConversationsStats
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1IngestConversationsRequest
    sampledConversations: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsMetadataIngestConversationsStats(
    typing.TypedDict, total=False
):
    duplicatesSkippedCount: int
    failedIngestCount: int
    processedObjectCount: int
    successfulIngestCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsRequest(
    typing.TypedDict, total=False
):
    conversationConfig: (
        GoogleCloudContactcenterinsightsV1IngestConversationsRequestConversationConfig
    )
    gcsSource: GoogleCloudContactcenterinsightsV1IngestConversationsRequestGcsSource
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1RedactionConfig
    sampleSize: int
    speechConfig: GoogleCloudContactcenterinsightsV1SpeechConfig
    transcriptObjectConfig: GoogleCloudContactcenterinsightsV1IngestConversationsRequestTranscriptObjectConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsRequestConversationConfig(
    typing.TypedDict, total=False
):
    agentChannel: int
    agentId: str
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsRequestGcsSource(
    typing.TypedDict, total=False
):
    audioBucketUri: str
    bucketObjectType: typing.Literal[
        "BUCKET_OBJECT_TYPE_UNSPECIFIED", "TRANSCRIPT", "AUDIO"
    ]
    bucketUri: str
    customMetadataKeys: _list[str]
    metadataBucketUri: str
    transcriptBucketUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsRequestTranscriptObjectConfig(
    typing.TypedDict, total=False
):
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecRequest(
    typing.TypedDict, total=False
):
    encryptionSpec: GoogleCloudContactcenterinsightsV1EncryptionSpec

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Intent(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IntentMatchData(typing.TypedDict, total=False):
    intentUniqueId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InterruptionData(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Issue(typing.TypedDict, total=False):
    createTime: str
    displayDescription: str
    displayName: str
    name: str
    sampleUtterances: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueAssignment(typing.TypedDict, total=False):
    displayName: str
    issue: str
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueMatchData(typing.TypedDict, total=False):
    issueAssignment: GoogleCloudContactcenterinsightsV1IssueAssignment

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModel(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    inputDataConfig: GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig
    issueCount: str
    languageCode: str
    modelType: typing.Literal["MODEL_TYPE_UNSPECIFIED", "TYPE_V1", "TYPE_V2"]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "UNDEPLOYED",
        "DEPLOYING",
        "DEPLOYED",
        "UNDEPLOYING",
        "DELETING",
    ]
    trainingStats: GoogleCloudContactcenterinsightsV1IssueModelLabelStats
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig(
    typing.TypedDict, total=False
):
    filter: str
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    trainingConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelLabelStats(
    typing.TypedDict, total=False
):
    analyzedConversationsCount: str
    issueStats: dict[str, typing.Any]
    unclassifiedConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelLabelStatsIssueStats(
    typing.TypedDict, total=False
):
    displayName: str
    issue: str
    labeledConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelResult(typing.TypedDict, total=False):
    issueModel: str
    issues: _list[GoogleCloudContactcenterinsightsV1IssueAssignment]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponse(
    typing.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAnalysesResponse(
    typing.TypedDict, total=False
):
    analyses: _list[GoogleCloudContactcenterinsightsV1Analysis]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponse(
    typing.TypedDict, total=False
):
    analysisRules: _list[GoogleCloudContactcenterinsightsV1AnalysisRule]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAssessmentRulesResponse(
    typing.TypedDict, total=False
):
    assessmentRules: _list[GoogleCloudContactcenterinsightsV1AssessmentRule]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAssessmentsResponse(
    typing.TypedDict, total=False
):
    assessments: _list[GoogleCloudContactcenterinsightsV1Assessment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAssistantSessionsResponse(
    typing.TypedDict, total=False
):
    assistantSessions: _list[GoogleCloudContactcenterinsightsV1AssistantSession]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAuthorizedViewSetsResponse(
    typing.TypedDict, total=False
):
    authorizedViewSets: _list[GoogleCloudContactcenterinsightsV1AuthorizedViewSet]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAuthorizedViewsResponse(
    typing.TypedDict, total=False
):
    authorizedViews: _list[GoogleCloudContactcenterinsightsV1AuthorizedView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAutoLabelingRulesResponse(
    typing.TypedDict, total=False
):
    autoLabelingRules: _list[GoogleCloudContactcenterinsightsV1AutoLabelingRule]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListChartsResponse(
    typing.TypedDict, total=False
):
    charts: _list[GoogleCloudContactcenterinsightsV1Chart]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListConversationsResponse(
    typing.TypedDict, total=False
):
    conversations: _list[GoogleCloudContactcenterinsightsV1Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListDashboardsResponse(
    typing.TypedDict, total=False
):
    dashboards: _list[GoogleCloudContactcenterinsightsV1Dashboard]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListDatasetsResponse(
    typing.TypedDict, total=False
):
    datasets: _list[GoogleCloudContactcenterinsightsV1Dataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponse(
    typing.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssueModelsResponse(
    typing.TypedDict, total=False
):
    issueModels: _list[GoogleCloudContactcenterinsightsV1IssueModel]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssuesResponse(
    typing.TypedDict, total=False
):
    issues: _list[GoogleCloudContactcenterinsightsV1Issue]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListNotesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notes: _list[GoogleCloudContactcenterinsightsV1Note]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    phraseMatchers: _list[GoogleCloudContactcenterinsightsV1PhraseMatcher]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaQuestionTagsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    qaQuestionTags: _list[GoogleCloudContactcenterinsightsV1QaQuestionTag]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaQuestionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    qaQuestions: _list[GoogleCloudContactcenterinsightsV1QaQuestion]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    qaScorecardRevisions: _list[GoogleCloudContactcenterinsightsV1QaScorecardRevision]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaScorecardsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    qaScorecards: _list[GoogleCloudContactcenterinsightsV1QaScorecard]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListViewsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    views: _list[GoogleCloudContactcenterinsightsV1View]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1MetricDefinition(typing.TypedDict, total=False):
    displayName: str
    sourceId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Note(typing.TypedDict, total=False):
    assessmentNote: GoogleCloudContactcenterinsightsV1NoteAssessmentNote
    content: str
    conversationTurnNote: GoogleCloudContactcenterinsightsV1NoteConversationTurnNote
    createTime: str
    name: str
    noteCreator: GoogleCloudContactcenterinsightsV1UserInfo
    qaQuestionNote: GoogleCloudContactcenterinsightsV1NoteQaQuestionNote
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1NoteAssessmentNote(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1NoteConversationTurnNote(
    typing.TypedDict, total=False
):
    turnIndex: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1NoteQaQuestionNote(
    typing.TypedDict, total=False
):
    qaQuestion: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchData(typing.TypedDict, total=False):
    displayName: str
    phraseMatcher: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchRule(typing.TypedDict, total=False):
    config: GoogleCloudContactcenterinsightsV1PhraseMatchRuleConfig
    negated: bool
    query: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchRuleConfig(
    typing.TypedDict, total=False
):
    exactMatchConfig: GoogleCloudContactcenterinsightsV1ExactMatchConfig
    regexMatchConfig: GoogleCloudContactcenterinsightsV1RegexMatchConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup(
    typing.TypedDict, total=False
):
    phraseMatchRules: _list[GoogleCloudContactcenterinsightsV1PhraseMatchRule]
    type: typing.Literal["PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED", "ALL_OF", "ANY_OF"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatcher(typing.TypedDict, total=False):
    activationUpdateTime: str
    active: bool
    displayName: str
    name: str
    phraseMatchRuleGroups: _list[GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup]
    revisionCreateTime: str
    revisionId: str
    roleMatch: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    type: typing.Literal["PHRASE_MATCHER_TYPE_UNSPECIFIED", "ALL_OF", "ANY_OF"]
    updateTime: str
    versionTag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PublishAssessmentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaAnswer(typing.TypedDict, total=False):
    answerSources: _list[GoogleCloudContactcenterinsightsV1QaAnswerAnswerSource]
    answerValue: GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue
    conversation: str
    qaQuestion: str
    questionBody: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaAnswerAnswerSource(
    typing.TypedDict, total=False
):
    answerValue: GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED", "MANUAL_EDIT"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue(
    typing.TypedDict, total=False
):
    boolValue: bool
    key: str
    naValue: bool
    normalizedScore: float
    numValue: float
    potentialScore: float
    score: float
    skipValue: bool
    strValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestion(typing.TypedDict, total=False):
    abbreviation: str
    answerChoices: _list[GoogleCloudContactcenterinsightsV1QaQuestionAnswerChoice]
    answerInstructions: str
    createTime: str
    metrics: GoogleCloudContactcenterinsightsV1QaQuestionMetrics
    name: str
    order: int
    predefinedQuestionConfig: (
        GoogleCloudContactcenterinsightsV1QaQuestionPredefinedQuestionConfig
    )
    qaQuestionDataOptions: (
        GoogleCloudContactcenterinsightsV1QaQuestionQaQuestionDataOptions
    )
    questionBody: str
    questionType: typing.Literal[
        "QA_QUESTION_TYPE_UNSPECIFIED", "CUSTOMIZABLE", "PREDEFINED"
    ]
    tags: _list[str]
    tuningMetadata: GoogleCloudContactcenterinsightsV1QaQuestionTuningMetadata
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionAnswerChoice(
    typing.TypedDict, total=False
):
    boolValue: bool
    key: str
    naValue: bool
    numValue: float
    score: float
    strValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionMetrics(
    typing.TypedDict, total=False
):
    accuracy: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionPredefinedQuestionConfig(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "PREDEFINED_QUESTION_TYPE_UNSPECIFIED",
        "CONVERSATION_OUTCOME",
        "CONVERSATION_OUTCOME_ESCALATION_INITIATOR_ROLE",
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionQaQuestionDataOptions(
    typing.TypedDict, total=False
):
    conversationDataOptions: GoogleCloudContactcenterinsightsV1ConversationDataOptions

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionTag(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    qaQuestionIds: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionTuningMetadata(
    typing.TypedDict, total=False
):
    datasetValidationWarnings: _list[
        typing.Literal[
            "DATASET_VALIDATION_WARNING_UNSPECIFIED",
            "TOO_MANY_INVALID_FEEDBACK_LABELS",
            "INSUFFICIENT_FEEDBACK_LABELS",
            "INSUFFICIENT_FEEDBACK_LABELS_PER_ANSWER",
            "ALL_FEEDBACK_LABELS_HAVE_THE_SAME_ANSWER",
        ]
    ]
    totalValidLabelCount: str
    tuningError: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecard(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    isDefault: bool
    name: str
    source: typing.Literal[
        "QA_SCORECARD_SOURCE_UNSPECIFIED",
        "QA_SCORECARD_SOURCE_CUSTOMER_DEFINED",
        "QA_SCORECARD_SOURCE_DISCOVERY_ENGINE",
        "QA_SCORECARD_SOURCE_INTENT_TAXONOMY",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardResult(
    typing.TypedDict, total=False
):
    agentId: str
    conversation: str
    createTime: str
    name: str
    normalizedScore: float
    potentialScore: float
    qaAnswers: _list[GoogleCloudContactcenterinsightsV1QaAnswer]
    qaScorecardRevision: str
    qaTagResults: _list[GoogleCloudContactcenterinsightsV1QaScorecardResultQaTagResult]
    score: float
    scoreSources: _list[GoogleCloudContactcenterinsightsV1QaScorecardResultScoreSource]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardResultQaTagResult(
    typing.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    score: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardResultScoreSource(
    typing.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    qaTagResults: _list[GoogleCloudContactcenterinsightsV1QaScorecardResultQaTagResult]
    score: float
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED_ONLY", "INCLUDES_MANUAL_EDITS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardRevision(
    typing.TypedDict, total=False
):
    alternateIds: _list[str]
    createTime: str
    name: str
    snapshot: GoogleCloudContactcenterinsightsV1QaScorecard
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "EDITABLE",
        "TRAINING",
        "TRAINING_FAILED",
        "READY",
        "DELETING",
        "TRAINING_CANCELLED",
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetrics(typing.TypedDict, total=False):
    request: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsMetadata(
    typing.TypedDict, total=False
):
    resultIsTruncated: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[GoogleCloudContactcenterinsightsV1Dimension]
    filter: str
    measureMask: str
    timeGranularity: typing.Literal[
        "TIME_GRANULARITY_UNSPECIFIED",
        "NONE",
        "DAILY",
        "HOURLY",
        "PER_MINUTE",
        "PER_5_MINUTES",
        "MONTHLY",
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponse(
    typing.TypedDict, total=False
):
    location: str
    macroAverageSlice: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSlice
    slices: _list[GoogleCloudContactcenterinsightsV1QueryMetricsResponseSlice]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSlice(
    typing.TypedDict, total=False
):
    dimensions: _list[GoogleCloudContactcenterinsightsV1Dimension]
    timeSeries: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceTimeSeries
    total: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPoint

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPoint(
    typing.TypedDict, total=False
):
    conversationMeasure: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasure
    dialogflowInteractionMeasure: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointDialogflowInteractionMeasure
    interval: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasure(
    typing.TypedDict, total=False
):
    aaSupervisorAssignedConversationsCount: int
    aaSupervisorDroppedConversationsCount: int
    aaSupervisorEscalatedConversationsCount: int
    aaSupervisorMonitoredConversationsCount: int
    aaSupervisorTransferredToHumanAgentConvCount: int
    aiCoachSuggestionAgentMessageTriggerCount: int
    aiCoachSuggestionAgentUsageCount: int
    aiCoachSuggestionAgentUsageRatio: float
    aiCoachSuggestionCustomerMessageTriggerCount: int
    aiCoachSuggestionCustomerMessageTriggerRatio: float
    aiCoachSuggestionMessageTriggerCount: int
    aiCoachSuggestionMessageTriggerRatio: float
    averageAgentSentimentScore: float
    averageClientSentimentScore: float
    averageCustomerSatisfactionRating: float
    averageDuration: str
    averageQaNormalizedScore: float
    averageQaQuestionNormalizedScore: float
    averageSilencePercentage: float
    averageSummarizationSuggestionEditDistance: float
    averageSummarizationSuggestionNormalizedEditDistance: float
    averageTurnCount: float
    avgConversationClientTurnSentimentEma: float
    containedConversationCount: int
    containedConversationRatio: float
    conversationAiCoachSuggestionCount: int
    conversationAiCoachSuggestionRatio: float
    conversationCount: int
    conversationSuggestedSummaryRatio: float
    conversationTotalAgentMessageCount: int
    conversationTotalCustomerMessageCount: int
    conversationalAgentsAverageAudioInAudioOutLatency: float
    conversationalAgentsAverageEndToEndLatency: float
    conversationalAgentsAverageLlmCallLatency: float
    conversationalAgentsAverageTtsLatency: float
    dialogflowAverageWebhookLatency: float
    dialogflowConversationsEscalationCount: float
    dialogflowConversationsEscalationRatio: float
    dialogflowInteractionsNoInputRatio: float
    dialogflowInteractionsNoMatchRatio: float
    dialogflowWebhookFailureRatio: float
    dialogflowWebhookTimeoutRatio: float
    knowledgeAssistNegativeFeedbackRatio: float
    knowledgeAssistPositiveFeedbackRatio: float
    knowledgeAssistResultCount: int
    knowledgeAssistUriClickRatio: float
    knowledgeSearchAgentQuerySourceRatio: float
    knowledgeSearchNegativeFeedbackRatio: float
    knowledgeSearchPositiveFeedbackRatio: float
    knowledgeSearchResultCount: int
    knowledgeSearchSuggestedQuerySourceRatio: float
    knowledgeSearchUriClickRatio: float
    qaTagScores: _list[
        GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore
    ]
    summarizationSuggestionEditRatio: float
    summarizationSuggestionResultCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore(
    typing.TypedDict, total=False
):
    averageTagNormalizedScore: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointDialogflowInteractionMeasure(
    typing.TypedDict, total=False
):
    percentileAudioInAudioOutLatency: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointPercentileResult
    percentileEndToEndLatency: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointPercentileResult
    percentileLlmCallLatency: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointPercentileResult
    percentileToolUseLatency: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointPercentileResult
    percentileTtsLatency: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointPercentileResult

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointPercentileResult(
    typing.TypedDict, total=False
):
    p50: float
    p90: float
    p99: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceTimeSeries(
    typing.TypedDict, total=False
):
    dataPoints: _list[
        GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPoint
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryPerformanceOverviewMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryPerformanceOverviewRequest(
    typing.TypedDict, total=False
):
    agentPerformanceSource: (
        GoogleCloudContactcenterinsightsV1QueryPerformanceOverviewRequestAgentSource
    )
    comparisonQueryInterval: GoogleCloudContactcenterinsightsV1QueryInterval
    filter: str
    queryInterval: GoogleCloudContactcenterinsightsV1QueryInterval

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryPerformanceOverviewRequestAgentSource(
    typing.TypedDict, total=False
):
    agentId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryPerformanceOverviewResponse(
    typing.TypedDict, total=False
):
    summaryText: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1RedactionConfig(typing.TypedDict, total=False):
    deidentifyTemplate: str
    inspectTemplate: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1RedirectAction(typing.TypedDict, total=False):
    queryParams: dict[str, typing.Any]
    relativePath: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1RegexMatchConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1RuntimeAnnotation(
    typing.TypedDict, total=False
):
    annotationId: str
    answerFeedback: GoogleCloudContactcenterinsightsV1AnswerFeedback
    articleSuggestion: GoogleCloudContactcenterinsightsV1ArticleSuggestionData
    cesEndSessionAnnotation: GoogleCloudContactcenterinsightsV1CesEndSessionAnnotation
    cesTurnAnnotation: GoogleCloudContactcenterinsightsV1CesTurnAnnotation
    conversationSummarizationSuggestion: (
        GoogleCloudContactcenterinsightsV1ConversationSummarizationSuggestionData
    )
    createTime: str
    dialogflowInteraction: GoogleCloudContactcenterinsightsV1DialogflowInteractionData
    endBoundary: GoogleCloudContactcenterinsightsV1AnnotationBoundary
    faqAnswer: GoogleCloudContactcenterinsightsV1FaqAnswerData
    smartComposeSuggestion: GoogleCloudContactcenterinsightsV1SmartComposeSuggestionData
    smartReply: GoogleCloudContactcenterinsightsV1SmartReplyData
    startBoundary: GoogleCloudContactcenterinsightsV1AnnotationBoundary
    userInput: GoogleCloudContactcenterinsightsV1RuntimeAnnotationUserInput

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1RuntimeAnnotationUserInput(
    typing.TypedDict, total=False
):
    generatorName: str
    query: str
    querySource: typing.Literal[
        "QUERY_SOURCE_UNSPECIFIED", "AGENT_QUERY", "SUGGESTED_QUERY"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SampleConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1SampleConversationsRequest
    sampleConversationsStats: GoogleCloudContactcenterinsightsV1SampleConversationsMetadataSampleConversationsStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SampleConversationsMetadataSampleConversationsStats(
    typing.TypedDict, total=False
):
    failedSampleCount: int
    successfulSampleCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SampleConversationsRequest(
    typing.TypedDict, total=False
):
    destinationDataset: GoogleCloudContactcenterinsightsV1Dataset
    parent: str
    sampleRule: GoogleCloudContactcenterinsightsV1SampleRule

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SampleConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SampleRule(typing.TypedDict, total=False):
    conversationFilter: str
    dimension: str
    samplePercentage: float
    sampleRow: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ScheduleInfo(typing.TypedDict, total=False):
    endTime: str
    schedule: str
    startTime: str
    timeZone: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SearchAuthorizedViewsResponse(
    typing.TypedDict, total=False
):
    authorizedViews: _list[GoogleCloudContactcenterinsightsV1AuthorizedView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SentimentData(typing.TypedDict, total=False):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Settings(typing.TypedDict, total=False):
    analysisConfig: GoogleCloudContactcenterinsightsV1SettingsAnalysisConfig
    conversationTtl: str
    createTime: str
    diagnosticMetricConfig: (
        GoogleCloudContactcenterinsightsV1SettingsDiagnosticMetricConfig
    )
    languageCode: str
    name: str
    pubsubNotificationSettings: dict[str, typing.Any]
    redactionConfig: GoogleCloudContactcenterinsightsV1RedactionConfig
    screenRecordingBucketUri: str
    speechConfig: GoogleCloudContactcenterinsightsV1SpeechConfig
    timeZone: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SettingsAnalysisConfig(
    typing.TypedDict, total=False
):
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    runtimeIntegrationAnalysisPercentage: float
    uploadConversationAnalysisPercentage: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SettingsDiagnosticMetricConfig(
    typing.TypedDict, total=False
):
    metrics: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SignedAudioUris(typing.TypedDict, total=False):
    signedDialogflowAudioUri: str
    signedGcsAudioUri: str
    signedTurnLevelAudios: _list[
        GoogleCloudContactcenterinsightsV1ConversationDataSourceTurnLevelAudio
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SilenceData(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SmartComposeSuggestionData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    suggestion: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SmartReplyData(typing.TypedDict, total=False):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    reply: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SpeechConfig(typing.TypedDict, total=False):
    disableWordTimeOffsets: bool
    speechRecognizer: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1StreamChatRequest(
    typing.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1StreamChatResponse(
    typing.TypedDict, total=False
):
    chunk: GoogleCloudContactcenterinsightsV1AssistantChunk
    eventId: str
    eventTime: str
    statusMessage: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestAutoLabelingRuleRequest(
    typing.TypedDict, total=False
):
    autoLabelingRule: GoogleCloudContactcenterinsightsV1AutoLabelingRule
    conversation: GoogleCloudContactcenterinsightsV1Conversation

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestAutoLabelingRuleResponse(
    typing.TypedDict, total=False
):
    labelResult: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestCorrelationConfigMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    dataset: str
    stats: GoogleCloudContactcenterinsightsV1TestCorrelationConfigMetadataFullConversationCorrelationStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestCorrelationConfigMetadataFullConversationCorrelationStats(
    typing.TypedDict, total=False
):
    conversationCorrelationErrors: _list[
        GoogleCloudContactcenterinsightsV1TestCorrelationConfigMetadataFullConversationCorrelationStatsConversationCorrelationError
    ]
    correlatedConversationsCount: int
    failedConversationsCount: int
    partialErrors: _list[GoogleRpcStatus]
    sampledConversationsCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestCorrelationConfigMetadataFullConversationCorrelationStatsConversationCorrelationError(
    typing.TypedDict, total=False
):
    conversation: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestCorrelationConfigRequest(
    typing.TypedDict, total=False
):
    conversations: (
        GoogleCloudContactcenterinsightsV1TestCorrelationConfigRequestConversations
    )
    correlationConfig: GoogleCloudContactcenterinsightsV1CorrelationConfig
    filter: str
    maxSampleCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestCorrelationConfigRequestConversations(
    typing.TypedDict, total=False
):
    conversations: _list[GoogleCloudContactcenterinsightsV1Conversation]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestCorrelationConfigResponse(
    typing.TypedDict, total=False
):
    detailedResults: GoogleCloudContactcenterinsightsV1TestCorrelationConfigResponseDetailedCorrelationResults
    partialErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TestCorrelationConfigResponseDetailedCorrelationResults(
    typing.TypedDict, total=False
):
    constraintResults: _list[
        GoogleCloudContactcenterinsightsV1ConstraintEvaluationResult
    ]
    joinKeyResults: _list[
        GoogleCloudContactcenterinsightsV1ConversationCorrelationResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TuneQaScorecardRevisionRequest(
    typing.TypedDict, total=False
):
    filter: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1UndeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployQaScorecardRevisionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UpdateQaQuestionTagMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1UpdateQaQuestionTagRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UpdateQaQuestionTagRequest(
    typing.TypedDict, total=False
):
    qaQuestionTag: GoogleCloudContactcenterinsightsV1QaQuestionTag
    updateMask: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UploadConversationMetadata(
    typing.TypedDict, total=False
):
    analysisOperation: str
    appliedRedactionConfig: GoogleCloudContactcenterinsightsV1RedactionConfig
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1UploadConversationRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UploadConversationRequest(
    typing.TypedDict, total=False
):
    conversation: GoogleCloudContactcenterinsightsV1Conversation
    conversationId: str
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1RedactionConfig
    speechConfig: GoogleCloudContactcenterinsightsV1SpeechConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UserInfo(typing.TypedDict, total=False):
    username: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1View(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    updateTime: str
    value: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Widget(typing.TypedDict, total=False):
    chart: GoogleCloudContactcenterinsightsV1Chart
    chartReference: str
    container: GoogleCloudContactcenterinsightsV1Container
    filter: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Analysis(typing.TypedDict, total=False):
    analysisResult: GoogleCloudContactcenterinsightsV1alpha1AnalysisResult
    annotatorSelector: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector
    createTime: str
    name: str
    requestTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnalysisResult(
    typing.TypedDict, total=False
):
    callAnalysisMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1AnalysisResultCallAnalysisMetadata
    )
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnalysisResultCallAnalysisMetadata(
    typing.TypedDict, total=False
):
    annotations: _list[GoogleCloudContactcenterinsightsV1alpha1CallAnnotation]
    entities: dict[str, typing.Any]
    intents: dict[str, typing.Any]
    issueModelResult: GoogleCloudContactcenterinsightsV1alpha1IssueModelResult
    phraseMatchers: dict[str, typing.Any]
    qaScorecardResults: _list[GoogleCloudContactcenterinsightsV1alpha1QaScorecardResult]
    sentiments: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSentiment
    ]
    silence: GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSilence

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary(
    typing.TypedDict, total=False
):
    transcriptIndex: int
    wordIndex: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector(
    typing.TypedDict, total=False
):
    issueModels: _list[str]
    phraseMatchers: _list[str]
    qaConfig: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorQaConfig
    runAutoLabelingAnnotator: bool
    runEntityAnnotator: bool
    runIntentAnnotator: bool
    runInterruptionAnnotator: bool
    runIssueModelAnnotator: bool
    runPhraseMatcherAnnotator: bool
    runQaAnnotator: bool
    runSentimentAnnotator: bool
    runSilenceAnnotator: bool
    runSummarizationAnnotator: bool
    summarizationConfig: (
        GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorSummarizationConfig
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorQaConfig(
    typing.TypedDict, total=False
):
    scorecardList: (
        GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorQaConfigScorecardList
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorQaConfigScorecardList(
    typing.TypedDict, total=False
):
    qaScorecardRevisions: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorSummarizationConfig(
    typing.TypedDict, total=False
):
    conversationProfile: str
    generator: str
    summarizationModel: typing.Literal[
        "SUMMARIZATION_MODEL_UNSPECIFIED", "BASELINE_MODEL", "BASELINE_MODEL_V2_0"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnswerFeedback(
    typing.TypedDict, total=False
):
    clicked: bool
    correctnessLevel: typing.Literal[
        "CORRECTNESS_LEVEL_UNSPECIFIED",
        "NOT_CORRECT",
        "PARTIALLY_CORRECT",
        "FULLY_CORRECT",
    ]
    displayed: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ArticleSuggestionData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    source: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsMetadata(
    typing.TypedDict, total=False
):
    completedAnalysesCount: int
    createTime: str
    endTime: str
    failedAnalysesCount: int
    partialErrors: _list[GoogleRpcStatus]
    relabel: bool
    request: GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsRequest
    totalRequestedAnalysesCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsRequest(
    typing.TypedDict, total=False
):
    analysisPercentage: float
    annotatorSelector: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector
    filter: str
    parent: str
    relabel: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsResponse(
    typing.TypedDict, total=False
):
    failedAnalysisCount: int
    successfulAnalysisCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsRequest(
    typing.TypedDict, total=False
):
    filter: str
    force: bool
    maxDeleteCount: int
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteFeedbackLabelsMetadata(
    typing.TypedDict, total=False
):
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1BulkDeleteFeedbackLabelsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteFeedbackLabelsRequest(
    typing.TypedDict, total=False
):
    filter: str
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteFeedbackLabelsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CallAnnotation(
    typing.TypedDict, total=False
):
    annotationEndBoundary: GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary
    annotationStartBoundary: GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary
    channelTag: int
    entityMentionData: GoogleCloudContactcenterinsightsV1alpha1EntityMentionData
    holdData: GoogleCloudContactcenterinsightsV1alpha1HoldData
    intentMatchData: GoogleCloudContactcenterinsightsV1alpha1IntentMatchData
    interruptionData: GoogleCloudContactcenterinsightsV1alpha1InterruptionData
    issueMatchData: GoogleCloudContactcenterinsightsV1alpha1IssueMatchData
    phraseMatchData: GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData
    sentimentData: GoogleCloudContactcenterinsightsV1alpha1SentimentData
    silenceData: GoogleCloudContactcenterinsightsV1alpha1SilenceData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CesEndSessionAnnotation(
    typing.TypedDict, total=False
):
    endSession: GoogleCloudCesV1mainEndSession

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CesTurnAnnotation(
    typing.TypedDict, total=False
):
    messages: _list[GoogleCloudCesV1mainMessage]
    rootSpan: GoogleCloudCesV1mainSpan

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConstraintEvaluationResult(
    typing.TypedDict, total=False
):
    conversationA: str
    conversationB: str
    ruleConstraintResults: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConstraintEvaluationResultRuleConstraintResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConstraintEvaluationResultRuleConstraintResult(
    typing.TypedDict, total=False
):
    constraintMet: bool
    error: GoogleRpcStatus
    ruleId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Conversation(
    typing.TypedDict, total=False
):
    agentId: str
    callMetadata: GoogleCloudContactcenterinsightsV1alpha1ConversationCallMetadata
    correlationInfo: GoogleCloudContactcenterinsightsV1alpha1ConversationCorrelationInfo
    createTime: str
    dataSource: GoogleCloudContactcenterinsightsV1alpha1ConversationDataSource
    dialogflowIntents: dict[str, typing.Any]
    duration: str
    expireTime: str
    labels: dict[str, typing.Any]
    languageCode: str
    latestAnalysis: GoogleCloudContactcenterinsightsV1alpha1Analysis
    latestSummary: (
        GoogleCloudContactcenterinsightsV1alpha1ConversationSummarizationSuggestionData
    )
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    metadataJson: str
    name: str
    obfuscatedUserId: str
    qualityMetadata: GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadata
    runtimeAnnotations: _list[GoogleCloudContactcenterinsightsV1alpha1RuntimeAnnotation]
    startTime: str
    transcript: GoogleCloudContactcenterinsightsV1alpha1ConversationTranscript
    ttl: str
    turnCount: int
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationCallMetadata(
    typing.TypedDict, total=False
):
    agentChannel: int
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationCorrelationInfo(
    typing.TypedDict, total=False
):
    correlationTypes: _list[
        typing.Literal[
            "CORRELATION_TYPE_UNSPECIFIED", "SEGMENT", "PARTIAL", "FULL", "SYNTHETIC"
        ]
    ]
    fullConversationCorrelationId: str
    mergedFullConversationCorrelationId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationCorrelationResult(
    typing.TypedDict, total=False
):
    conversation: str
    ruleResults: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationCorrelationResultRuleCorrelationResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationCorrelationResultRuleCorrelationResult(
    typing.TypedDict, total=False
):
    correlationId: str
    error: GoogleRpcStatus
    ruleId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationDataSource(
    typing.TypedDict, total=False
):
    dialogflowSource: GoogleCloudContactcenterinsightsV1alpha1DialogflowSource
    gcsSource: GoogleCloudContactcenterinsightsV1alpha1GcsSource
    metadataUri: str
    turnLevelAudios: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationDataSourceTurnLevelAudio
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationDataSourceTurnLevelAudio(
    typing.TypedDict, total=False
):
    audioDuration: str
    audioGcsUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSentiment(
    typing.TypedDict, total=False
):
    channelTag: int
    sentimentData: GoogleCloudContactcenterinsightsV1alpha1SentimentData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSilence(
    typing.TypedDict, total=False
):
    silenceDuration: str
    silencePercentage: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationParticipant(
    typing.TypedDict, total=False
):
    dialogflowParticipant: str
    dialogflowParticipantName: str
    obfuscatedExternalUserId: str
    role: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    userId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadata(
    typing.TypedDict, total=False
):
    agentInfo: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadataAgentInfo
    ]
    customerSatisfactionRating: int
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1alpha1FeedbackLabel]
    menuPath: str
    waitDuration: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadataAgentInfo(
    typing.TypedDict, total=False
):
    agentId: str
    agentType: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    deploymentDisplayName: str
    deploymentId: str
    displayName: str
    dispositionCode: str
    entrySubagentDisplayName: str
    entrySubagentId: str
    location: str
    team: str
    teams: _list[str]
    versionDisplayName: str
    versionId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationSummarizationSuggestionData(
    typing.TypedDict, total=False
):
    answerRecord: str
    confidence: float
    conversationModel: str
    generatorId: str
    metadata: dict[str, typing.Any]
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscript(
    typing.TypedDict, total=False
):
    transcriptSegments: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegment
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegment(
    typing.TypedDict, total=False
):
    channelTag: int
    confidence: float
    dialogflowSegmentMetadata: GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata
    languageCode: str
    messageTime: str
    segmentParticipant: GoogleCloudContactcenterinsightsV1alpha1ConversationParticipant
    sentiment: GoogleCloudContactcenterinsightsV1alpha1SentimentData
    text: str
    turnLevelAudio: (
        GoogleCloudContactcenterinsightsV1alpha1ConversationDataSourceTurnLevelAudio
    )
    words: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentWordInfo
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata(
    typing.TypedDict, total=False
):
    smartReplyAllowlistCovered: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentWordInfo(
    typing.TypedDict, total=False
):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateAnalysisOperationMetadata(
    typing.TypedDict, total=False
):
    annotatorSelector: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector
    conversation: str
    createTime: str
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1CreateIssueRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1CreateIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueModelRequest(
    typing.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1alpha1IssueModel
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueRequest(
    typing.TypedDict, total=False
):
    issue: GoogleCloudContactcenterinsightsV1alpha1Issue
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Dataset(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    ttl: str
    type: typing.Literal["TYPE_UNSPECIFIED", "EVAL", "LIVE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeleteIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1DeleteIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeleteIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeleteQaQuestionTagMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1DeleteQaQuestionTagRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeleteQaQuestionTagRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DialogflowIntent(
    typing.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DialogflowInteractionData(
    typing.TypedDict, total=False
):
    confidence: float
    dialogflowIntentId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DialogflowSource(
    typing.TypedDict, total=False
):
    audioUri: str
    dialogflowConversation: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Dimension(typing.TypedDict, total=False):
    agentDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionAgentDimensionMetadata
    )
    clientSentimentCategoryDimensionMetadata: GoogleCloudContactcenterinsightsV1alpha1DimensionClientSentimentCategoryDimensionMetadata
    conversationProfileDimensionMetadata: GoogleCloudContactcenterinsightsV1alpha1DimensionConversationProfileDimensionMetadata
    conversationalAgentsPlaybookDimensionMetadata: GoogleCloudContactcenterinsightsV1alpha1DimensionConversationalAgentsPlaybookDimensionMetadata
    conversationalAgentsToolDimensionMetadata: GoogleCloudContactcenterinsightsV1alpha1DimensionConversationalAgentsToolDimensionMetadata
    dimensionKey: typing.Literal[
        "DIMENSION_KEY_UNSPECIFIED",
        "ISSUE",
        "ISSUE_NAME",
        "AGENT",
        "AGENT_TEAM",
        "QA_QUESTION_ID",
        "QA_QUESTION_ANSWER_VALUE",
        "QA_SCORECARD_ID",
        "CONVERSATION_PROFILE_ID",
        "MEDIUM",
        "CONVERSATIONAL_AGENTS_PLAYBOOK_ID",
        "CONVERSATIONAL_AGENTS_PLAYBOOK_NAME",
        "CONVERSATIONAL_AGENTS_TOOL_ID",
        "CONVERSATIONAL_AGENTS_TOOL_NAME",
        "CLIENT_SENTIMENT_CATEGORY",
        "AGENT_VERSION_ID",
        "AGENT_DEPLOYMENT_ID",
        "AGENT_ASSIST_SUPERVISOR_ID",
        "LABEL_KEY",
        "LABEL_VALUE",
        "LABEL_KEY_AND_VALUE",
        "LAST_TRANSFER_SUB_AGENT_NAME",
    ]
    issueDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionIssueDimensionMetadata
    )
    labelDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionLabelDimensionMetadata
    )
    mediumDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionMediumDimensionMetadata
    )
    qaQuestionAnswerDimensionMetadata: GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionAnswerDimensionMetadata
    qaQuestionDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionDimensionMetadata
    )
    qaScorecardDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionQaScorecardDimensionMetadata
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionAgentDimensionMetadata(
    typing.TypedDict, total=False
):
    agentDeploymentDisplayName: str
    agentDeploymentId: str
    agentDisplayName: str
    agentId: str
    agentTeam: str
    agentVersionDisplayName: str
    agentVersionId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionClientSentimentCategoryDimensionMetadata(
    typing.TypedDict, total=False
):
    sentimentCategory: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionConversationProfileDimensionMetadata(
    typing.TypedDict, total=False
):
    conversationProfileId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionConversationalAgentsPlaybookDimensionMetadata(
    typing.TypedDict, total=False
):
    playbookDisplayName: str
    playbookId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionConversationalAgentsToolDimensionMetadata(
    typing.TypedDict, total=False
):
    toolDisplayName: str
    toolId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionIssueDimensionMetadata(
    typing.TypedDict, total=False
):
    issueDisplayName: str
    issueId: str
    issueModelId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionLabelDimensionMetadata(
    typing.TypedDict, total=False
):
    labelKey: str
    labelValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionMediumDimensionMetadata(
    typing.TypedDict, total=False
):
    medium: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionAnswerDimensionMetadata(
    typing.TypedDict, total=False
):
    answerValue: str
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionDimensionMetadata(
    typing.TypedDict, total=False
):
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionQaScorecardDimensionMetadata(
    typing.TypedDict, total=False
):
    qaScorecardId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1EncryptionSpec(
    typing.TypedDict, total=False
):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Entity(typing.TypedDict, total=False):
    displayName: str
    metadata: dict[str, typing.Any]
    salience: float
    sentiment: GoogleCloudContactcenterinsightsV1alpha1SentimentData
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "EVENT",
        "WORK_OF_ART",
        "CONSUMER_GOOD",
        "OTHER",
        "PHONE_NUMBER",
        "ADDRESS",
        "DATE",
        "NUMBER",
        "PRICE",
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1EntityMentionData(
    typing.TypedDict, total=False
):
    entityUniqueId: str
    sentiment: GoogleCloudContactcenterinsightsV1alpha1SentimentData
    type: typing.Literal["MENTION_TYPE_UNSPECIFIED", "PROPER", "COMMON"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataMetadata(
    typing.TypedDict, total=False
):
    completedExportCount: int
    createTime: str
    endTime: str
    failedExportCount: int
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequest(
    typing.TypedDict, total=False
):
    bigQueryDestination: GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination
    exportSchemaVersion: typing.Literal[
        "EXPORT_SCHEMA_VERSION_UNSPECIFIED",
        "EXPORT_V1",
        "EXPORT_V2",
        "EXPORT_V3",
        "EXPORT_V4",
        "EXPORT_V5",
        "EXPORT_V6",
        "EXPORT_V7",
        "EXPORT_V8",
        "EXPORT_V9",
        "EXPORT_V10",
        "EXPORT_V11",
        "EXPORT_V12",
        "EXPORT_V13",
        "EXPORT_V14",
        "EXPORT_V15",
        "EXPORT_V16",
        "EXPORT_V17",
        "EXPORT_VERSION_LATEST_AVAILABLE",
    ]
    filter: str
    kmsKey: str
    parent: str
    writeDisposition: typing.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination(
    typing.TypedDict, total=False
):
    dataset: str
    projectId: str
    table: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequest(
    typing.TypedDict, total=False
):
    gcsDestination: (
        GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequestGcsDestination
    )
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequestGcsDestination(
    typing.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1FaqAnswerData(
    typing.TypedDict, total=False
):
    answer: str
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    question: str
    source: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1FeedbackLabel(
    typing.TypedDict, total=False
):
    createTime: str
    label: str
    labeledResource: str
    name: str
    qaAnswerLabel: GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GcsSource(typing.TypedDict, total=False):
    audioUri: str
    transcriptUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscript(
    typing.TypedDict, total=False
):
    conversationId: str
    createTime: str
    messages: _list[
        GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessage
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessage(
    typing.TypedDict, total=False
):
    createTime: str
    messageId: str
    systemMessageWrapper: GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageSystemMessages
    userMessage: GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageUserMessage

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageSystemMessage(
    typing.TypedDict, total=False
):
    chartSpec: dict[str, typing.Any]
    generatedSqlQuery: str
    textMessage: GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageSystemMessageTextOutput
    userProvidedChartSpec: dict[str, typing.Any]
    userProvidedSqlQuery: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageSystemMessageTextOutput(
    typing.TypedDict, total=False
):
    text: _list[str]
    textType: typing.Literal[
        "TYPE_UNSPECIFIED", "THOUGHT", "FINAL_RESPONSE", "PROGRESS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageSystemMessages(
    typing.TypedDict, total=False
):
    systemMessages: _list[
        GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageSystemMessage
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscriptMessageUserMessage(
    typing.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightsMetadata(
    typing.TypedDict, total=False
):
    errorMessages: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightsResponse(
    typing.TypedDict, total=False
):
    generativeResponses: _list[
        GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightsResponseGenerativeResponse
    ]
    transcript: (
        GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightConversationTranscript
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightsResponseGenerativeResponse(
    typing.TypedDict, total=False
):
    chartSpec: dict[str, typing.Any]
    generatedSqlQuery: str
    textMessage: GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightsResponseGenerativeResponseTextOutput
    textOutput: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GenerativeInsightsResponseGenerativeResponseTextOutput(
    typing.TypedDict, total=False
):
    text: _list[str]
    textType: typing.Literal[
        "TYPE_UNSPECIFIED", "THOUGHT", "FINAL_RESPONSE", "PROGRESS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1HoldData(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequest(
    typing.TypedDict, total=False
):
    createNewModel: bool
    gcsSource: GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequestGcsSource
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequestGcsSource(
    typing.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelResponse(
    typing.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1alpha1IssueModel

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    ingestConversationsStats: GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadataIngestConversationsStats
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequest
    sampledConversations: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadataIngestConversationsStats(
    typing.TypedDict, total=False
):
    duplicatesSkippedCount: int
    failedIngestCount: int
    processedObjectCount: int
    successfulIngestCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequest(
    typing.TypedDict, total=False
):
    conversationConfig: GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestConversationConfig
    gcsSource: (
        GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestGcsSource
    )
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1alpha1RedactionConfig
    sampleSize: int
    speechConfig: GoogleCloudContactcenterinsightsV1alpha1SpeechConfig
    transcriptObjectConfig: GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestTranscriptObjectConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestConversationConfig(
    typing.TypedDict, total=False
):
    agentChannel: int
    agentId: str
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestGcsSource(
    typing.TypedDict, total=False
):
    audioBucketUri: str
    bucketObjectType: typing.Literal[
        "BUCKET_OBJECT_TYPE_UNSPECIFIED", "TRANSCRIPT", "AUDIO"
    ]
    bucketUri: str
    customMetadataKeys: _list[str]
    metadataBucketUri: str
    transcriptBucketUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestTranscriptObjectConfig(
    typing.TypedDict, total=False
):
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecRequest(
    typing.TypedDict, total=False
):
    encryptionSpec: GoogleCloudContactcenterinsightsV1alpha1EncryptionSpec

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Intent(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IntentMatchData(
    typing.TypedDict, total=False
):
    intentUniqueId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InterruptionData(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Issue(typing.TypedDict, total=False):
    createTime: str
    displayDescription: str
    displayName: str
    name: str
    sampleUtterances: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueAssignment(
    typing.TypedDict, total=False
):
    displayName: str
    issue: str
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueMatchData(
    typing.TypedDict, total=False
):
    issueAssignment: GoogleCloudContactcenterinsightsV1alpha1IssueAssignment

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModel(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    inputDataConfig: GoogleCloudContactcenterinsightsV1alpha1IssueModelInputDataConfig
    issueCount: str
    languageCode: str
    modelType: typing.Literal["MODEL_TYPE_UNSPECIFIED", "TYPE_V1", "TYPE_V2"]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "UNDEPLOYED",
        "DEPLOYING",
        "DEPLOYED",
        "UNDEPLOYING",
        "DELETING",
    ]
    trainingStats: GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStats
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModelInputDataConfig(
    typing.TypedDict, total=False
):
    filter: str
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    trainingConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStats(
    typing.TypedDict, total=False
):
    analyzedConversationsCount: str
    issueStats: dict[str, typing.Any]
    unclassifiedConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStatsIssueStats(
    typing.TypedDict, total=False
):
    displayName: str
    issue: str
    labeledConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModelResult(
    typing.TypedDict, total=False
):
    issueModel: str
    issues: _list[GoogleCloudContactcenterinsightsV1alpha1IssueAssignment]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ListAllFeedbackLabelsResponse(
    typing.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1alpha1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ListFeedbackLabelsResponse(
    typing.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1alpha1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData(
    typing.TypedDict, total=False
):
    displayName: str
    phraseMatcher: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaAnswer(typing.TypedDict, total=False):
    answerSources: _list[GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerSource]
    answerValue: GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue
    conversation: str
    qaQuestion: str
    questionBody: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerSource(
    typing.TypedDict, total=False
):
    answerValue: GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED", "MANUAL_EDIT"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue(
    typing.TypedDict, total=False
):
    boolValue: bool
    key: str
    naValue: bool
    normalizedScore: float
    numValue: float
    potentialScore: float
    score: float
    skipValue: bool
    strValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaQuestionTag(
    typing.TypedDict, total=False
):
    createTime: str
    displayName: str
    name: str
    qaQuestionIds: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaScorecardResult(
    typing.TypedDict, total=False
):
    agentId: str
    conversation: str
    createTime: str
    name: str
    normalizedScore: float
    potentialScore: float
    qaAnswers: _list[GoogleCloudContactcenterinsightsV1alpha1QaAnswer]
    qaScorecardRevision: str
    qaTagResults: _list[
        GoogleCloudContactcenterinsightsV1alpha1QaScorecardResultQaTagResult
    ]
    score: float
    scoreSources: _list[
        GoogleCloudContactcenterinsightsV1alpha1QaScorecardResultScoreSource
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaScorecardResultQaTagResult(
    typing.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    score: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaScorecardResultScoreSource(
    typing.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    qaTagResults: _list[
        GoogleCloudContactcenterinsightsV1alpha1QaScorecardResultQaTagResult
    ]
    score: float
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED_ONLY", "INCLUDES_MANUAL_EDITS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsMetadata(
    typing.TypedDict, total=False
):
    resultIsTruncated: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponse(
    typing.TypedDict, total=False
):
    location: str
    macroAverageSlice: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSlice
    slices: _list[GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSlice]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSlice(
    typing.TypedDict, total=False
):
    dimensions: _list[GoogleCloudContactcenterinsightsV1alpha1Dimension]
    timeSeries: (
        GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceTimeSeries
    )
    total: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPoint

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPoint(
    typing.TypedDict, total=False
):
    conversationMeasure: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasure
    dialogflowInteractionMeasure: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointDialogflowInteractionMeasure
    interval: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasure(
    typing.TypedDict, total=False
):
    aaSupervisorAssignedConversationsCount: int
    aaSupervisorDroppedConversationsCount: int
    aaSupervisorEscalatedConversationsCount: int
    aaSupervisorMonitoredConversationsCount: int
    aaSupervisorTransferredToHumanAgentConvCount: int
    aiCoachSuggestionAgentMessageTriggerCount: int
    aiCoachSuggestionAgentUsageCount: int
    aiCoachSuggestionAgentUsageRatio: float
    aiCoachSuggestionCustomerMessageTriggerCount: int
    aiCoachSuggestionCustomerMessageTriggerRatio: float
    aiCoachSuggestionMessageTriggerCount: int
    aiCoachSuggestionMessageTriggerRatio: float
    averageAgentSentimentScore: float
    averageClientSentimentScore: float
    averageCustomerSatisfactionRating: float
    averageDuration: str
    averageQaNormalizedScore: float
    averageQaQuestionNormalizedScore: float
    averageSilencePercentage: float
    averageSummarizationSuggestionEditDistance: float
    averageSummarizationSuggestionNormalizedEditDistance: float
    averageTurnCount: float
    avgConversationClientTurnSentimentEma: float
    containedConversationCount: int
    containedConversationRatio: float
    conversationAiCoachSuggestionCount: int
    conversationAiCoachSuggestionRatio: float
    conversationCount: int
    conversationSuggestedSummaryRatio: float
    conversationTotalAgentMessageCount: int
    conversationTotalCustomerMessageCount: int
    conversationalAgentsAverageAudioInAudioOutLatency: float
    conversationalAgentsAverageEndToEndLatency: float
    conversationalAgentsAverageLlmCallLatency: float
    conversationalAgentsAverageTtsLatency: float
    dialogflowAverageWebhookLatency: float
    dialogflowConversationsEscalationCount: float
    dialogflowConversationsEscalationRatio: float
    dialogflowInteractionsNoInputRatio: float
    dialogflowInteractionsNoMatchRatio: float
    dialogflowWebhookFailureRatio: float
    dialogflowWebhookTimeoutRatio: float
    knowledgeAssistNegativeFeedbackRatio: float
    knowledgeAssistPositiveFeedbackRatio: float
    knowledgeAssistResultCount: int
    knowledgeAssistUriClickRatio: float
    knowledgeSearchAgentQuerySourceRatio: float
    knowledgeSearchNegativeFeedbackRatio: float
    knowledgeSearchPositiveFeedbackRatio: float
    knowledgeSearchResultCount: int
    knowledgeSearchSuggestedQuerySourceRatio: float
    knowledgeSearchUriClickRatio: float
    qaTagScores: _list[
        GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore
    ]
    summarizationSuggestionEditRatio: float
    summarizationSuggestionResultCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore(
    typing.TypedDict, total=False
):
    averageTagNormalizedScore: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointDialogflowInteractionMeasure(
    typing.TypedDict, total=False
):
    percentileAudioInAudioOutLatency: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointPercentileResult
    percentileEndToEndLatency: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointPercentileResult
    percentileLlmCallLatency: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointPercentileResult
    percentileToolUseLatency: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointPercentileResult
    percentileTtsLatency: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointPercentileResult

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointPercentileResult(
    typing.TypedDict, total=False
):
    p50: float
    p90: float
    p99: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceTimeSeries(
    typing.TypedDict, total=False
):
    dataPoints: _list[
        GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPoint
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryPerformanceOverviewMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryPerformanceOverviewResponse(
    typing.TypedDict, total=False
):
    summaryText: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1RedactionConfig(
    typing.TypedDict, total=False
):
    deidentifyTemplate: str
    inspectTemplate: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1RuntimeAnnotation(
    typing.TypedDict, total=False
):
    annotationId: str
    answerFeedback: GoogleCloudContactcenterinsightsV1alpha1AnswerFeedback
    articleSuggestion: GoogleCloudContactcenterinsightsV1alpha1ArticleSuggestionData
    cesEndSessionAnnotation: (
        GoogleCloudContactcenterinsightsV1alpha1CesEndSessionAnnotation
    )
    cesTurnAnnotation: GoogleCloudContactcenterinsightsV1alpha1CesTurnAnnotation
    conversationSummarizationSuggestion: (
        GoogleCloudContactcenterinsightsV1alpha1ConversationSummarizationSuggestionData
    )
    createTime: str
    dialogflowInteraction: (
        GoogleCloudContactcenterinsightsV1alpha1DialogflowInteractionData
    )
    endBoundary: GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary
    faqAnswer: GoogleCloudContactcenterinsightsV1alpha1FaqAnswerData
    smartComposeSuggestion: (
        GoogleCloudContactcenterinsightsV1alpha1SmartComposeSuggestionData
    )
    smartReply: GoogleCloudContactcenterinsightsV1alpha1SmartReplyData
    startBoundary: GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary
    userInput: GoogleCloudContactcenterinsightsV1alpha1RuntimeAnnotationUserInput

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1RuntimeAnnotationUserInput(
    typing.TypedDict, total=False
):
    generatorName: str
    query: str
    querySource: typing.Literal[
        "QUERY_SOURCE_UNSPECIFIED", "AGENT_QUERY", "SUGGESTED_QUERY"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SampleConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1SampleConversationsRequest
    sampleConversationsStats: GoogleCloudContactcenterinsightsV1alpha1SampleConversationsMetadataSampleConversationsStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SampleConversationsMetadataSampleConversationsStats(
    typing.TypedDict, total=False
):
    failedSampleCount: int
    successfulSampleCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SampleConversationsRequest(
    typing.TypedDict, total=False
):
    destinationDataset: GoogleCloudContactcenterinsightsV1alpha1Dataset
    parent: str
    sampleRule: GoogleCloudContactcenterinsightsV1alpha1SampleRule

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SampleConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SampleRule(typing.TypedDict, total=False):
    conversationFilter: str
    dimension: str
    samplePercentage: float
    sampleRow: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SentimentData(
    typing.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SilenceData(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SmartComposeSuggestionData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    suggestion: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SmartReplyData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    reply: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SpeechConfig(
    typing.TypedDict, total=False
):
    disableWordTimeOffsets: bool
    speechRecognizer: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    dataset: str
    stats: GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigMetadataFullConversationCorrelationStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigMetadataFullConversationCorrelationStats(
    typing.TypedDict, total=False
):
    conversationCorrelationErrors: _list[
        GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigMetadataFullConversationCorrelationStatsConversationCorrelationError
    ]
    correlatedConversationsCount: int
    failedConversationsCount: int
    partialErrors: _list[GoogleRpcStatus]
    sampledConversationsCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigMetadataFullConversationCorrelationStatsConversationCorrelationError(
    typing.TypedDict, total=False
):
    conversation: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigResponse(
    typing.TypedDict, total=False
):
    detailedResults: GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigResponseDetailedCorrelationResults
    partialErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1TestCorrelationConfigResponseDetailedCorrelationResults(
    typing.TypedDict, total=False
):
    constraintResults: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConstraintEvaluationResult
    ]
    joinKeyResults: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationCorrelationResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UpdateQaQuestionTagMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1UpdateQaQuestionTagRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UpdateQaQuestionTagRequest(
    typing.TypedDict, total=False
):
    qaQuestionTag: GoogleCloudContactcenterinsightsV1alpha1QaQuestionTag
    updateMask: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UploadConversationMetadata(
    typing.TypedDict, total=False
):
    analysisOperation: str
    appliedRedactionConfig: GoogleCloudContactcenterinsightsV1alpha1RedactionConfig
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1UploadConversationRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UploadConversationRequest(
    typing.TypedDict, total=False
):
    conversation: GoogleCloudContactcenterinsightsV1alpha1Conversation
    conversationId: str
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1alpha1RedactionConfig
    speechConfig: GoogleCloudContactcenterinsightsV1alpha1SpeechConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnalysis(typing.TypedDict, total=False):
    analysisResult: GoogleCloudContactcenterinsightsV1mainAnalysisResult
    annotatorSelector: GoogleCloudContactcenterinsightsV1mainAnnotatorSelector
    createTime: str
    name: str
    requestTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnalysisResult(
    typing.TypedDict, total=False
):
    callAnalysisMetadata: (
        GoogleCloudContactcenterinsightsV1mainAnalysisResultCallAnalysisMetadata
    )
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnalysisResultCallAnalysisMetadata(
    typing.TypedDict, total=False
):
    annotations: _list[GoogleCloudContactcenterinsightsV1mainCallAnnotation]
    entities: dict[str, typing.Any]
    intents: dict[str, typing.Any]
    issueModelResult: GoogleCloudContactcenterinsightsV1mainIssueModelResult
    phraseMatchers: dict[str, typing.Any]
    qaScorecardResults: _list[GoogleCloudContactcenterinsightsV1mainQaScorecardResult]
    sentiments: _list[GoogleCloudContactcenterinsightsV1mainConversationLevelSentiment]
    silence: GoogleCloudContactcenterinsightsV1mainConversationLevelSilence

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnnotationBoundary(
    typing.TypedDict, total=False
):
    transcriptIndex: int
    wordIndex: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnnotatorSelector(
    typing.TypedDict, total=False
):
    issueModels: _list[str]
    phraseMatchers: _list[str]
    qaConfig: GoogleCloudContactcenterinsightsV1mainAnnotatorSelectorQaConfig
    runAutoLabelingAnnotator: bool
    runEntityAnnotator: bool
    runIntentAnnotator: bool
    runInterruptionAnnotator: bool
    runIssueModelAnnotator: bool
    runPhraseMatcherAnnotator: bool
    runQaAnnotator: bool
    runSentimentAnnotator: bool
    runSilenceAnnotator: bool
    runSummarizationAnnotator: bool
    summarizationConfig: (
        GoogleCloudContactcenterinsightsV1mainAnnotatorSelectorSummarizationConfig
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnnotatorSelectorQaConfig(
    typing.TypedDict, total=False
):
    scorecardList: (
        GoogleCloudContactcenterinsightsV1mainAnnotatorSelectorQaConfigScorecardList
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnnotatorSelectorQaConfigScorecardList(
    typing.TypedDict, total=False
):
    qaScorecardRevisions: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnnotatorSelectorSummarizationConfig(
    typing.TypedDict, total=False
):
    conversationProfile: str
    generator: str
    summarizationModel: typing.Literal[
        "SUMMARIZATION_MODEL_UNSPECIFIED", "BASELINE_MODEL", "BASELINE_MODEL_V2_0"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainAnswerFeedback(
    typing.TypedDict, total=False
):
    clicked: bool
    correctnessLevel: typing.Literal[
        "CORRECTNESS_LEVEL_UNSPECIFIED",
        "NOT_CORRECT",
        "PARTIALLY_CORRECT",
        "FULLY_CORRECT",
    ]
    displayed: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainArticleSuggestionData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    source: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkAnalyzeConversationsMetadata(
    typing.TypedDict, total=False
):
    completedAnalysesCount: int
    createTime: str
    endTime: str
    failedAnalysesCount: int
    partialErrors: _list[GoogleRpcStatus]
    relabel: bool
    request: GoogleCloudContactcenterinsightsV1mainBulkAnalyzeConversationsRequest
    totalRequestedAnalysesCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkAnalyzeConversationsRequest(
    typing.TypedDict, total=False
):
    analysisPercentage: float
    annotatorSelector: GoogleCloudContactcenterinsightsV1mainAnnotatorSelector
    filter: str
    parent: str
    relabel: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkAnalyzeConversationsResponse(
    typing.TypedDict, total=False
):
    failedAnalysisCount: int
    successfulAnalysisCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDeleteConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1mainBulkDeleteConversationsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDeleteConversationsRequest(
    typing.TypedDict, total=False
):
    filter: str
    force: bool
    maxDeleteCount: int
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDeleteConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDeleteFeedbackLabelsMetadata(
    typing.TypedDict, total=False
):
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1mainBulkDeleteFeedbackLabelsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDeleteFeedbackLabelsRequest(
    typing.TypedDict, total=False
):
    filter: str
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDeleteFeedbackLabelsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    downloadStats: GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsMetadataDownloadStats
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsMetadataDownloadStats(
    typing.TypedDict, total=False
):
    fileNames: _list[str]
    processedObjectCount: int
    successfulDownloadCount: int
    totalFilesWritten: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsRequest(
    typing.TypedDict, total=False
):
    conversationFilter: str
    feedbackLabelType: typing.Literal[
        "FEEDBACK_LABEL_TYPE_UNSPECIFIED",
        "QUALITY_AI",
        "TOPIC_MODELING",
        "AGENT_ASSIST_SUMMARY",
    ]
    filter: str
    gcsDestination: GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsRequestGcsDestination
    maxDownloadCount: int
    parent: str
    sheetsDestination: GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsRequestSheetsDestination
    templateQaScorecardId: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsRequestGcsDestination(
    typing.TypedDict, total=False
):
    addWhitespace: bool
    alwaysPrintEmptyFields: bool
    format: typing.Literal["FORMAT_UNSPECIFIED", "CSV", "JSON"]
    objectUri: str
    recordsPerFileCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsRequestSheetsDestination(
    typing.TypedDict, total=False
):
    sheetTitle: str
    spreadsheetUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainBulkDownloadFeedbackLabelsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCallAnnotation(
    typing.TypedDict, total=False
):
    annotationEndBoundary: GoogleCloudContactcenterinsightsV1mainAnnotationBoundary
    annotationStartBoundary: GoogleCloudContactcenterinsightsV1mainAnnotationBoundary
    channelTag: int
    entityMentionData: GoogleCloudContactcenterinsightsV1mainEntityMentionData
    holdData: GoogleCloudContactcenterinsightsV1mainHoldData
    intentMatchData: GoogleCloudContactcenterinsightsV1mainIntentMatchData
    interruptionData: GoogleCloudContactcenterinsightsV1mainInterruptionData
    issueMatchData: GoogleCloudContactcenterinsightsV1mainIssueMatchData
    phraseMatchData: GoogleCloudContactcenterinsightsV1mainPhraseMatchData
    sentimentData: GoogleCloudContactcenterinsightsV1mainSentimentData
    silenceData: GoogleCloudContactcenterinsightsV1mainSilenceData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCesEndSessionAnnotation(
    typing.TypedDict, total=False
):
    endSession: GoogleCloudCesV1mainEndSession

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCesTurnAnnotation(
    typing.TypedDict, total=False
):
    messages: _list[GoogleCloudCesV1mainMessage]
    rootSpan: GoogleCloudCesV1mainSpan

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConstraintEvaluationResult(
    typing.TypedDict, total=False
):
    conversationA: str
    conversationB: str
    ruleConstraintResults: _list[
        GoogleCloudContactcenterinsightsV1mainConstraintEvaluationResultRuleConstraintResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConstraintEvaluationResultRuleConstraintResult(
    typing.TypedDict, total=False
):
    constraintMet: bool
    error: GoogleRpcStatus
    ruleId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversation(typing.TypedDict, total=False):
    agentId: str
    callMetadata: GoogleCloudContactcenterinsightsV1mainConversationCallMetadata
    correlationInfo: GoogleCloudContactcenterinsightsV1mainConversationCorrelationInfo
    createTime: str
    dataSource: GoogleCloudContactcenterinsightsV1mainConversationDataSource
    dialogflowIntents: dict[str, typing.Any]
    duration: str
    expireTime: str
    labels: dict[str, typing.Any]
    languageCode: str
    latestAnalysis: GoogleCloudContactcenterinsightsV1mainAnalysis
    latestSummary: (
        GoogleCloudContactcenterinsightsV1mainConversationSummarizationSuggestionData
    )
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    metadataJson: str
    name: str
    obfuscatedUserId: str
    qualityMetadata: GoogleCloudContactcenterinsightsV1mainConversationQualityMetadata
    runtimeAnnotations: _list[GoogleCloudContactcenterinsightsV1mainRuntimeAnnotation]
    startTime: str
    transcript: GoogleCloudContactcenterinsightsV1mainConversationTranscript
    ttl: str
    turnCount: int
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationCallMetadata(
    typing.TypedDict, total=False
):
    agentChannel: int
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationCorrelationInfo(
    typing.TypedDict, total=False
):
    correlationTypes: _list[
        typing.Literal[
            "CORRELATION_TYPE_UNSPECIFIED", "SEGMENT", "PARTIAL", "FULL", "SYNTHETIC"
        ]
    ]
    fullConversationCorrelationId: str
    mergedFullConversationCorrelationId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationCorrelationResult(
    typing.TypedDict, total=False
):
    conversation: str
    ruleResults: _list[
        GoogleCloudContactcenterinsightsV1mainConversationCorrelationResultRuleCorrelationResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationCorrelationResultRuleCorrelationResult(
    typing.TypedDict, total=False
):
    correlationId: str
    error: GoogleRpcStatus
    ruleId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationDataSource(
    typing.TypedDict, total=False
):
    dialogflowSource: GoogleCloudContactcenterinsightsV1mainDialogflowSource
    gcsSource: GoogleCloudContactcenterinsightsV1mainGcsSource
    metadataUri: str
    turnLevelAudios: _list[
        GoogleCloudContactcenterinsightsV1mainConversationDataSourceTurnLevelAudio
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationDataSourceTurnLevelAudio(
    typing.TypedDict, total=False
):
    audioDuration: str
    audioGcsUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationLevelSentiment(
    typing.TypedDict, total=False
):
    channelTag: int
    sentimentData: GoogleCloudContactcenterinsightsV1mainSentimentData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationLevelSilence(
    typing.TypedDict, total=False
):
    silenceDuration: str
    silencePercentage: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationParticipant(
    typing.TypedDict, total=False
):
    dialogflowParticipant: str
    dialogflowParticipantName: str
    obfuscatedExternalUserId: str
    role: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    userId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationQualityMetadata(
    typing.TypedDict, total=False
):
    agentInfo: _list[
        GoogleCloudContactcenterinsightsV1mainConversationQualityMetadataAgentInfo
    ]
    customerSatisfactionRating: int
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1mainFeedbackLabel]
    menuPath: str
    waitDuration: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationQualityMetadataAgentInfo(
    typing.TypedDict, total=False
):
    agentId: str
    agentType: typing.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    deploymentDisplayName: str
    deploymentId: str
    displayName: str
    dispositionCode: str
    entrySubagentDisplayName: str
    entrySubagentId: str
    location: str
    team: str
    teams: _list[str]
    versionDisplayName: str
    versionId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationSummarizationSuggestionData(
    typing.TypedDict, total=False
):
    answerRecord: str
    confidence: float
    conversationModel: str
    generatorId: str
    metadata: dict[str, typing.Any]
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationTranscript(
    typing.TypedDict, total=False
):
    transcriptSegments: _list[
        GoogleCloudContactcenterinsightsV1mainConversationTranscriptTranscriptSegment
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationTranscriptTranscriptSegment(
    typing.TypedDict, total=False
):
    channelTag: int
    confidence: float
    dialogflowSegmentMetadata: GoogleCloudContactcenterinsightsV1mainConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata
    languageCode: str
    messageTime: str
    segmentParticipant: GoogleCloudContactcenterinsightsV1mainConversationParticipant
    sentiment: GoogleCloudContactcenterinsightsV1mainSentimentData
    text: str
    turnLevelAudio: (
        GoogleCloudContactcenterinsightsV1mainConversationDataSourceTurnLevelAudio
    )
    words: _list[
        GoogleCloudContactcenterinsightsV1mainConversationTranscriptTranscriptSegmentWordInfo
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata(
    typing.TypedDict, total=False
):
    smartReplyAllowlistCovered: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainConversationTranscriptTranscriptSegmentWordInfo(
    typing.TypedDict, total=False
):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCreateAnalysisOperationMetadata(
    typing.TypedDict, total=False
):
    annotatorSelector: GoogleCloudContactcenterinsightsV1mainAnnotatorSelector
    conversation: str
    createTime: str
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCreateIssueMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainCreateIssueRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCreateIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainCreateIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCreateIssueModelRequest(
    typing.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1mainIssueModel
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainCreateIssueRequest(
    typing.TypedDict, total=False
):
    issue: GoogleCloudContactcenterinsightsV1mainIssue
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDataset(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    ttl: str
    type: typing.Literal["TYPE_UNSPECIFIED", "EVAL", "LIVE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDeleteIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainDeleteIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDeleteIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDeleteQaQuestionTagMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainDeleteQaQuestionTagRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDeleteQaQuestionTagRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDeployIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainDeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDeployIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDeployIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDialogflowIntent(
    typing.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDialogflowInteractionData(
    typing.TypedDict, total=False
):
    confidence: float
    dialogflowIntentId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDialogflowSource(
    typing.TypedDict, total=False
):
    audioUri: str
    dialogflowConversation: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimension(typing.TypedDict, total=False):
    agentDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1mainDimensionAgentDimensionMetadata
    )
    clientSentimentCategoryDimensionMetadata: GoogleCloudContactcenterinsightsV1mainDimensionClientSentimentCategoryDimensionMetadata
    conversationProfileDimensionMetadata: GoogleCloudContactcenterinsightsV1mainDimensionConversationProfileDimensionMetadata
    conversationalAgentsPlaybookDimensionMetadata: GoogleCloudContactcenterinsightsV1mainDimensionConversationalAgentsPlaybookDimensionMetadata
    conversationalAgentsToolDimensionMetadata: GoogleCloudContactcenterinsightsV1mainDimensionConversationalAgentsToolDimensionMetadata
    dimensionKey: typing.Literal[
        "DIMENSION_KEY_UNSPECIFIED",
        "ISSUE",
        "ISSUE_NAME",
        "AGENT",
        "AGENT_TEAM",
        "QA_QUESTION_ID",
        "QA_QUESTION_ANSWER_VALUE",
        "QA_SCORECARD_ID",
        "CONVERSATION_PROFILE_ID",
        "MEDIUM",
        "CONVERSATIONAL_AGENTS_PLAYBOOK_ID",
        "CONVERSATIONAL_AGENTS_PLAYBOOK_NAME",
        "CONVERSATIONAL_AGENTS_TOOL_ID",
        "CONVERSATIONAL_AGENTS_TOOL_NAME",
        "CLIENT_SENTIMENT_CATEGORY",
        "AGENT_VERSION_ID",
        "AGENT_DEPLOYMENT_ID",
        "AGENT_ASSIST_SUPERVISOR_ID",
        "LABEL_KEY",
        "LABEL_VALUE",
        "LABEL_KEY_AND_VALUE",
        "LAST_TRANSFER_SUB_AGENT_NAME",
    ]
    issueDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1mainDimensionIssueDimensionMetadata
    )
    labelDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1mainDimensionLabelDimensionMetadata
    )
    mediumDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1mainDimensionMediumDimensionMetadata
    )
    qaQuestionAnswerDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1mainDimensionQaQuestionAnswerDimensionMetadata
    )
    qaQuestionDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1mainDimensionQaQuestionDimensionMetadata
    )
    qaScorecardDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1mainDimensionQaScorecardDimensionMetadata
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionAgentDimensionMetadata(
    typing.TypedDict, total=False
):
    agentDeploymentDisplayName: str
    agentDeploymentId: str
    agentDisplayName: str
    agentId: str
    agentTeam: str
    agentVersionDisplayName: str
    agentVersionId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionClientSentimentCategoryDimensionMetadata(
    typing.TypedDict, total=False
):
    sentimentCategory: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionConversationProfileDimensionMetadata(
    typing.TypedDict, total=False
):
    conversationProfileId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionConversationalAgentsPlaybookDimensionMetadata(
    typing.TypedDict, total=False
):
    playbookDisplayName: str
    playbookId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionConversationalAgentsToolDimensionMetadata(
    typing.TypedDict, total=False
):
    toolDisplayName: str
    toolId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionIssueDimensionMetadata(
    typing.TypedDict, total=False
):
    issueDisplayName: str
    issueId: str
    issueModelId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionLabelDimensionMetadata(
    typing.TypedDict, total=False
):
    labelKey: str
    labelValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionMediumDimensionMetadata(
    typing.TypedDict, total=False
):
    medium: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionQaQuestionAnswerDimensionMetadata(
    typing.TypedDict, total=False
):
    answerValue: str
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionQaQuestionDimensionMetadata(
    typing.TypedDict, total=False
):
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainDimensionQaScorecardDimensionMetadata(
    typing.TypedDict, total=False
):
    qaScorecardId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainEncryptionSpec(
    typing.TypedDict, total=False
):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainEntity(typing.TypedDict, total=False):
    displayName: str
    metadata: dict[str, typing.Any]
    salience: float
    sentiment: GoogleCloudContactcenterinsightsV1mainSentimentData
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "EVENT",
        "WORK_OF_ART",
        "CONSUMER_GOOD",
        "OTHER",
        "PHONE_NUMBER",
        "ADDRESS",
        "DATE",
        "NUMBER",
        "PRICE",
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainEntityMentionData(
    typing.TypedDict, total=False
):
    entityUniqueId: str
    sentiment: GoogleCloudContactcenterinsightsV1mainSentimentData
    type: typing.Literal["MENTION_TYPE_UNSPECIFIED", "PROPER", "COMMON"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportInsightsDataMetadata(
    typing.TypedDict, total=False
):
    completedExportCount: int
    createTime: str
    endTime: str
    failedExportCount: int
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1mainExportInsightsDataRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportInsightsDataRequest(
    typing.TypedDict, total=False
):
    bigQueryDestination: GoogleCloudContactcenterinsightsV1mainExportInsightsDataRequestBigQueryDestination
    exportSchemaVersion: typing.Literal[
        "EXPORT_SCHEMA_VERSION_UNSPECIFIED",
        "EXPORT_V1",
        "EXPORT_V2",
        "EXPORT_V3",
        "EXPORT_V4",
        "EXPORT_V5",
        "EXPORT_V6",
        "EXPORT_V7",
        "EXPORT_V8",
        "EXPORT_V9",
        "EXPORT_V10",
        "EXPORT_V11",
        "EXPORT_V12",
        "EXPORT_V13",
        "EXPORT_V14",
        "EXPORT_V15",
        "EXPORT_V16",
        "EXPORT_V17",
        "EXPORT_VERSION_LATEST_AVAILABLE",
    ]
    filter: str
    kmsKey: str
    parent: str
    writeDisposition: typing.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportInsightsDataRequestBigQueryDestination(
    typing.TypedDict, total=False
):
    dataset: str
    projectId: str
    table: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportInsightsDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainExportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportIssueModelRequest(
    typing.TypedDict, total=False
):
    gcsDestination: (
        GoogleCloudContactcenterinsightsV1mainExportIssueModelRequestGcsDestination
    )
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportIssueModelRequestGcsDestination(
    typing.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainExportIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainFaqAnswerData(
    typing.TypedDict, total=False
):
    answer: str
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    question: str
    source: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainFeedbackLabel(
    typing.TypedDict, total=False
):
    createTime: str
    label: str
    labeledResource: str
    name: str
    qaAnswerLabel: GoogleCloudContactcenterinsightsV1mainQaAnswerAnswerValue
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGcsSource(typing.TypedDict, total=False):
    audioUri: str
    transcriptUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscript(
    typing.TypedDict, total=False
):
    conversationId: str
    createTime: str
    messages: _list[
        GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessage
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessage(
    typing.TypedDict, total=False
):
    createTime: str
    messageId: str
    systemMessageWrapper: GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageSystemMessages
    userMessage: GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageUserMessage

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageSystemMessage(
    typing.TypedDict, total=False
):
    chartSpec: dict[str, typing.Any]
    generatedSqlQuery: str
    textMessage: GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageSystemMessageTextOutput
    userProvidedChartSpec: dict[str, typing.Any]
    userProvidedSqlQuery: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageSystemMessageTextOutput(
    typing.TypedDict, total=False
):
    text: _list[str]
    textType: typing.Literal[
        "TYPE_UNSPECIFIED", "THOUGHT", "FINAL_RESPONSE", "PROGRESS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageSystemMessages(
    typing.TypedDict, total=False
):
    systemMessages: _list[
        GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageSystemMessage
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscriptMessageUserMessage(
    typing.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightsMetadata(
    typing.TypedDict, total=False
):
    errorMessages: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightsResponse(
    typing.TypedDict, total=False
):
    generativeResponses: _list[
        GoogleCloudContactcenterinsightsV1mainGenerativeInsightsResponseGenerativeResponse
    ]
    transcript: (
        GoogleCloudContactcenterinsightsV1mainGenerativeInsightConversationTranscript
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightsResponseGenerativeResponse(
    typing.TypedDict, total=False
):
    chartSpec: dict[str, typing.Any]
    generatedSqlQuery: str
    textMessage: GoogleCloudContactcenterinsightsV1mainGenerativeInsightsResponseGenerativeResponseTextOutput
    textOutput: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainGenerativeInsightsResponseGenerativeResponseTextOutput(
    typing.TypedDict, total=False
):
    text: _list[str]
    textType: typing.Literal[
        "TYPE_UNSPECIFIED", "THOUGHT", "FINAL_RESPONSE", "PROGRESS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainHoldData(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainImportIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainImportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainImportIssueModelRequest(
    typing.TypedDict, total=False
):
    createNewModel: bool
    gcsSource: GoogleCloudContactcenterinsightsV1mainImportIssueModelRequestGcsSource
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainImportIssueModelRequestGcsSource(
    typing.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainImportIssueModelResponse(
    typing.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1mainIssueModel

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIngestConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    ingestConversationsStats: GoogleCloudContactcenterinsightsV1mainIngestConversationsMetadataIngestConversationsStats
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1mainIngestConversationsRequest
    sampledConversations: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIngestConversationsMetadataIngestConversationsStats(
    typing.TypedDict, total=False
):
    duplicatesSkippedCount: int
    failedIngestCount: int
    processedObjectCount: int
    successfulIngestCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIngestConversationsRequest(
    typing.TypedDict, total=False
):
    conversationConfig: GoogleCloudContactcenterinsightsV1mainIngestConversationsRequestConversationConfig
    gcsSource: GoogleCloudContactcenterinsightsV1mainIngestConversationsRequestGcsSource
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1mainRedactionConfig
    sampleSize: int
    speechConfig: GoogleCloudContactcenterinsightsV1mainSpeechConfig
    transcriptObjectConfig: GoogleCloudContactcenterinsightsV1mainIngestConversationsRequestTranscriptObjectConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIngestConversationsRequestConversationConfig(
    typing.TypedDict, total=False
):
    agentChannel: int
    agentId: str
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIngestConversationsRequestGcsSource(
    typing.TypedDict, total=False
):
    audioBucketUri: str
    bucketObjectType: typing.Literal[
        "BUCKET_OBJECT_TYPE_UNSPECIFIED", "TRANSCRIPT", "AUDIO"
    ]
    bucketUri: str
    customMetadataKeys: _list[str]
    metadataBucketUri: str
    transcriptBucketUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIngestConversationsRequestTranscriptObjectConfig(
    typing.TypedDict, total=False
):
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIngestConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainInitializeEncryptionSpecMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1mainInitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainInitializeEncryptionSpecRequest(
    typing.TypedDict, total=False
):
    encryptionSpec: GoogleCloudContactcenterinsightsV1mainEncryptionSpec

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainInitializeEncryptionSpecResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIntent(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIntentMatchData(
    typing.TypedDict, total=False
):
    intentUniqueId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainInterruptionData(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssue(typing.TypedDict, total=False):
    createTime: str
    displayDescription: str
    displayName: str
    name: str
    sampleUtterances: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssueAssignment(
    typing.TypedDict, total=False
):
    displayName: str
    issue: str
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssueMatchData(
    typing.TypedDict, total=False
):
    issueAssignment: GoogleCloudContactcenterinsightsV1mainIssueAssignment

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssueModel(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    inputDataConfig: GoogleCloudContactcenterinsightsV1mainIssueModelInputDataConfig
    issueCount: str
    languageCode: str
    modelType: typing.Literal["MODEL_TYPE_UNSPECIFIED", "TYPE_V1", "TYPE_V2"]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "UNDEPLOYED",
        "DEPLOYING",
        "DEPLOYED",
        "UNDEPLOYING",
        "DELETING",
    ]
    trainingStats: GoogleCloudContactcenterinsightsV1mainIssueModelLabelStats
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssueModelInputDataConfig(
    typing.TypedDict, total=False
):
    filter: str
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    trainingConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssueModelLabelStats(
    typing.TypedDict, total=False
):
    analyzedConversationsCount: str
    issueStats: dict[str, typing.Any]
    unclassifiedConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssueModelLabelStatsIssueStats(
    typing.TypedDict, total=False
):
    displayName: str
    issue: str
    labeledConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainIssueModelResult(
    typing.TypedDict, total=False
):
    issueModel: str
    issues: _list[GoogleCloudContactcenterinsightsV1mainIssueAssignment]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainListAllFeedbackLabelsResponse(
    typing.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1mainFeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainListFeedbackLabelsResponse(
    typing.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1mainFeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainPhraseMatchData(
    typing.TypedDict, total=False
):
    displayName: str
    phraseMatcher: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQaAnswer(typing.TypedDict, total=False):
    answerSources: _list[GoogleCloudContactcenterinsightsV1mainQaAnswerAnswerSource]
    answerValue: GoogleCloudContactcenterinsightsV1mainQaAnswerAnswerValue
    conversation: str
    qaQuestion: str
    questionBody: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQaAnswerAnswerSource(
    typing.TypedDict, total=False
):
    answerValue: GoogleCloudContactcenterinsightsV1mainQaAnswerAnswerValue
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED", "MANUAL_EDIT"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQaAnswerAnswerValue(
    typing.TypedDict, total=False
):
    boolValue: bool
    key: str
    naValue: bool
    normalizedScore: float
    numValue: float
    potentialScore: float
    score: float
    skipValue: bool
    strValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQaQuestionTag(
    typing.TypedDict, total=False
):
    createTime: str
    displayName: str
    name: str
    qaQuestionIds: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQaScorecardResult(
    typing.TypedDict, total=False
):
    agentId: str
    conversation: str
    createTime: str
    name: str
    normalizedScore: float
    potentialScore: float
    qaAnswers: _list[GoogleCloudContactcenterinsightsV1mainQaAnswer]
    qaScorecardRevision: str
    qaTagResults: _list[
        GoogleCloudContactcenterinsightsV1mainQaScorecardResultQaTagResult
    ]
    score: float
    scoreSources: _list[
        GoogleCloudContactcenterinsightsV1mainQaScorecardResultScoreSource
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQaScorecardResultQaTagResult(
    typing.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    score: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQaScorecardResultScoreSource(
    typing.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    qaTagResults: _list[
        GoogleCloudContactcenterinsightsV1mainQaScorecardResultQaTagResult
    ]
    score: float
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED_ONLY", "INCLUDES_MANUAL_EDITS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsMetadata(
    typing.TypedDict, total=False
):
    resultIsTruncated: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponse(
    typing.TypedDict, total=False
):
    location: str
    macroAverageSlice: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSlice
    slices: _list[GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSlice]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSlice(
    typing.TypedDict, total=False
):
    dimensions: _list[GoogleCloudContactcenterinsightsV1mainDimension]
    timeSeries: (
        GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceTimeSeries
    )
    total: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPoint

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPoint(
    typing.TypedDict, total=False
):
    conversationMeasure: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointConversationMeasure
    dialogflowInteractionMeasure: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointDialogflowInteractionMeasure
    interval: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointConversationMeasure(
    typing.TypedDict, total=False
):
    aaSupervisorAssignedConversationsCount: int
    aaSupervisorDroppedConversationsCount: int
    aaSupervisorEscalatedConversationsCount: int
    aaSupervisorMonitoredConversationsCount: int
    aaSupervisorTransferredToHumanAgentConvCount: int
    aiCoachSuggestionAgentMessageTriggerCount: int
    aiCoachSuggestionAgentUsageCount: int
    aiCoachSuggestionAgentUsageRatio: float
    aiCoachSuggestionCustomerMessageTriggerCount: int
    aiCoachSuggestionCustomerMessageTriggerRatio: float
    aiCoachSuggestionMessageTriggerCount: int
    aiCoachSuggestionMessageTriggerRatio: float
    averageAgentSentimentScore: float
    averageClientSentimentScore: float
    averageCustomerSatisfactionRating: float
    averageDuration: str
    averageQaNormalizedScore: float
    averageQaQuestionNormalizedScore: float
    averageSilencePercentage: float
    averageSummarizationSuggestionEditDistance: float
    averageSummarizationSuggestionNormalizedEditDistance: float
    averageTurnCount: float
    avgConversationClientTurnSentimentEma: float
    containedConversationCount: int
    containedConversationRatio: float
    conversationAiCoachSuggestionCount: int
    conversationAiCoachSuggestionRatio: float
    conversationCount: int
    conversationSuggestedSummaryRatio: float
    conversationTotalAgentMessageCount: int
    conversationTotalCustomerMessageCount: int
    conversationalAgentsAverageAudioInAudioOutLatency: float
    conversationalAgentsAverageEndToEndLatency: float
    conversationalAgentsAverageLlmCallLatency: float
    conversationalAgentsAverageTtsLatency: float
    dialogflowAverageWebhookLatency: float
    dialogflowConversationsEscalationCount: float
    dialogflowConversationsEscalationRatio: float
    dialogflowInteractionsNoInputRatio: float
    dialogflowInteractionsNoMatchRatio: float
    dialogflowWebhookFailureRatio: float
    dialogflowWebhookTimeoutRatio: float
    knowledgeAssistNegativeFeedbackRatio: float
    knowledgeAssistPositiveFeedbackRatio: float
    knowledgeAssistResultCount: int
    knowledgeAssistUriClickRatio: float
    knowledgeSearchAgentQuerySourceRatio: float
    knowledgeSearchNegativeFeedbackRatio: float
    knowledgeSearchPositiveFeedbackRatio: float
    knowledgeSearchResultCount: int
    knowledgeSearchSuggestedQuerySourceRatio: float
    knowledgeSearchUriClickRatio: float
    qaTagScores: _list[
        GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointConversationMeasureQaTagScore
    ]
    summarizationSuggestionEditRatio: float
    summarizationSuggestionResultCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointConversationMeasureQaTagScore(
    typing.TypedDict, total=False
):
    averageTagNormalizedScore: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointDialogflowInteractionMeasure(
    typing.TypedDict, total=False
):
    percentileAudioInAudioOutLatency: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointPercentileResult
    percentileEndToEndLatency: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointPercentileResult
    percentileLlmCallLatency: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointPercentileResult
    percentileToolUseLatency: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointPercentileResult
    percentileTtsLatency: GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointPercentileResult

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPointPercentileResult(
    typing.TypedDict, total=False
):
    p50: float
    p90: float
    p99: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceTimeSeries(
    typing.TypedDict, total=False
):
    dataPoints: _list[
        GoogleCloudContactcenterinsightsV1mainQueryMetricsResponseSliceDataPoint
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryPerformanceOverviewMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainQueryPerformanceOverviewResponse(
    typing.TypedDict, total=False
):
    summaryText: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainRedactionConfig(
    typing.TypedDict, total=False
):
    deidentifyTemplate: str
    inspectTemplate: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainRuntimeAnnotation(
    typing.TypedDict, total=False
):
    annotationId: str
    answerFeedback: GoogleCloudContactcenterinsightsV1mainAnswerFeedback
    articleSuggestion: GoogleCloudContactcenterinsightsV1mainArticleSuggestionData
    cesEndSessionAnnotation: (
        GoogleCloudContactcenterinsightsV1mainCesEndSessionAnnotation
    )
    cesTurnAnnotation: GoogleCloudContactcenterinsightsV1mainCesTurnAnnotation
    conversationSummarizationSuggestion: (
        GoogleCloudContactcenterinsightsV1mainConversationSummarizationSuggestionData
    )
    createTime: str
    dialogflowInteraction: (
        GoogleCloudContactcenterinsightsV1mainDialogflowInteractionData
    )
    endBoundary: GoogleCloudContactcenterinsightsV1mainAnnotationBoundary
    faqAnswer: GoogleCloudContactcenterinsightsV1mainFaqAnswerData
    smartComposeSuggestion: (
        GoogleCloudContactcenterinsightsV1mainSmartComposeSuggestionData
    )
    smartReply: GoogleCloudContactcenterinsightsV1mainSmartReplyData
    startBoundary: GoogleCloudContactcenterinsightsV1mainAnnotationBoundary
    userInput: GoogleCloudContactcenterinsightsV1mainRuntimeAnnotationUserInput

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainRuntimeAnnotationUserInput(
    typing.TypedDict, total=False
):
    generatorName: str
    query: str
    querySource: typing.Literal[
        "QUERY_SOURCE_UNSPECIFIED", "AGENT_QUERY", "SUGGESTED_QUERY"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSampleConversationsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1mainSampleConversationsRequest
    sampleConversationsStats: GoogleCloudContactcenterinsightsV1mainSampleConversationsMetadataSampleConversationsStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSampleConversationsMetadataSampleConversationsStats(
    typing.TypedDict, total=False
):
    failedSampleCount: int
    successfulSampleCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSampleConversationsRequest(
    typing.TypedDict, total=False
):
    destinationDataset: GoogleCloudContactcenterinsightsV1mainDataset
    parent: str
    sampleRule: GoogleCloudContactcenterinsightsV1mainSampleRule

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSampleConversationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSampleRule(typing.TypedDict, total=False):
    conversationFilter: str
    dimension: str
    samplePercentage: float
    sampleRow: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSentimentData(
    typing.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSilenceData(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSmartComposeSuggestionData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    suggestion: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSmartReplyData(
    typing.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    reply: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainSpeechConfig(typing.TypedDict, total=False):
    disableWordTimeOffsets: bool
    speechRecognizer: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    dataset: str
    stats: GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigMetadataFullConversationCorrelationStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigMetadataFullConversationCorrelationStats(
    typing.TypedDict, total=False
):
    conversationCorrelationErrors: _list[
        GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigMetadataFullConversationCorrelationStatsConversationCorrelationError
    ]
    correlatedConversationsCount: int
    failedConversationsCount: int
    partialErrors: _list[GoogleRpcStatus]
    sampledConversationsCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigMetadataFullConversationCorrelationStatsConversationCorrelationError(
    typing.TypedDict, total=False
):
    conversation: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigResponse(
    typing.TypedDict, total=False
):
    detailedResults: GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigResponseDetailedCorrelationResults
    partialErrors: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainTestCorrelationConfigResponseDetailedCorrelationResults(
    typing.TypedDict, total=False
):
    constraintResults: _list[
        GoogleCloudContactcenterinsightsV1mainConstraintEvaluationResult
    ]
    joinKeyResults: _list[
        GoogleCloudContactcenterinsightsV1mainConversationCorrelationResult
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainUndeployIssueModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainUndeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainUndeployIssueModelRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainUndeployIssueModelResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainUpdateQaQuestionTagMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainUpdateQaQuestionTagRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainUpdateQaQuestionTagRequest(
    typing.TypedDict, total=False
):
    qaQuestionTag: GoogleCloudContactcenterinsightsV1mainQaQuestionTag
    updateMask: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainUploadConversationMetadata(
    typing.TypedDict, total=False
):
    analysisOperation: str
    appliedRedactionConfig: GoogleCloudContactcenterinsightsV1mainRedactionConfig
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1mainUploadConversationRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1mainUploadConversationRequest(
    typing.TypedDict, total=False
):
    conversation: GoogleCloudContactcenterinsightsV1mainConversation
    conversationId: str
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1mainRedactionConfig
    speechConfig: GoogleCloudContactcenterinsightsV1mainSpeechConfig

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

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
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleTypeInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str
