import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Analysis(
    typing_extensions.TypedDict, total=False
):
    analysisResult: GoogleCloudContactcenterinsightsV1AnalysisResult
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    createTime: str
    name: str
    requestTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisResult(
    typing_extensions.TypedDict, total=False
):
    callAnalysisMetadata: (
        GoogleCloudContactcenterinsightsV1AnalysisResultCallAnalysisMetadata
    )
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisResultCallAnalysisMetadata(
    typing_extensions.TypedDict, total=False
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
class GoogleCloudContactcenterinsightsV1AnalysisRule(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    transcriptIndex: int
    wordIndex: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotatorSelector(
    typing_extensions.TypedDict, total=False
):
    issueModels: _list[str]
    phraseMatchers: _list[str]
    qaConfig: GoogleCloudContactcenterinsightsV1AnnotatorSelectorQaConfig
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
    typing_extensions.TypedDict, total=False
):
    scorecardList: (
        GoogleCloudContactcenterinsightsV1AnnotatorSelectorQaConfigScorecardList
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotatorSelectorQaConfigScorecardList(
    typing_extensions.TypedDict, total=False
):
    qaScorecardRevisions: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotatorSelectorSummarizationConfig(
    typing_extensions.TypedDict, total=False
):
    conversationProfile: str
    summarizationModel: typing_extensions.Literal[
        "SUMMARIZATION_MODEL_UNSPECIFIED", "BASELINE_MODEL", "BASELINE_MODEL_V2_0"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnswerFeedback(
    typing_extensions.TypedDict, total=False
):
    clicked: bool
    correctnessLevel: typing_extensions.Literal[
        "CORRECTNESS_LEVEL_UNSPECIFIED",
        "NOT_CORRECT",
        "PARTIALLY_CORRECT",
        "FULLY_CORRECT",
    ]
    displayed: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ArticleSuggestionData(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    source: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsMetadata(
    typing_extensions.TypedDict, total=False
):
    completedAnalysesCount: int
    createTime: str
    endTime: str
    failedAnalysesCount: int
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsRequest
    totalRequestedAnalysesCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsRequest(
    typing_extensions.TypedDict, total=False
):
    analysisPercentage: float
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    filter: str
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    failedAnalysisCount: int
    successfulAnalysisCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteConversationsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool
    maxDeleteCount: int
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDeleteConversationsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    downloadStats: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsMetadataDownloadStats
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsMetadataDownloadStats(
    typing_extensions.TypedDict, total=False
):
    fileNames: _list[str]
    processedObjectCount: int
    successfulDownloadCount: int
    totalFilesWritten: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequest(
    typing_extensions.TypedDict, total=False
):
    conversationFilter: str
    feedbackLabelType: typing_extensions.Literal[
        "FEEDBACK_LABEL_TYPE_UNSPECIFIED", "QUALITY_AI", "TOPIC_MODELING"
    ]
    filter: str
    gcsDestination: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequestGcsDestination
    maxDownloadCount: int
    parent: str
    templateQaScorecardId: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequestGcsDestination(
    typing_extensions.TypedDict, total=False
):
    addWhitespace: bool
    alwaysPrintEmptyFields: bool
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "CSV", "JSON"]
    objectUri: str
    recordsPerFileCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequest(
    typing_extensions.TypedDict, total=False
):
    gcsSource: (
        GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequestGcsSource
    )
    validateOnly: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequestGcsSource(
    typing_extensions.TypedDict, total=False
):
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "CSV", "JSON"]
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponse(
    typing_extensions.TypedDict, total=False
):
    currentStats: GoogleCloudContactcenterinsightsV1IssueModelLabelStats

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsResponse(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    intervalDuration: str
    points: _list[
        GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeriesInterval
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeriesInterval(
    typing_extensions.TypedDict, total=False
):
    conversationCount: int
    startTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CallAnnotation(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudContactcenterinsightsV1Conversation(
    typing_extensions.TypedDict, total=False
):
    agentId: str
    callMetadata: GoogleCloudContactcenterinsightsV1ConversationCallMetadata
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
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
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
    typing_extensions.TypedDict, total=False
):
    agentChannel: int
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationDataSource(
    typing_extensions.TypedDict, total=False
):
    dialogflowSource: GoogleCloudContactcenterinsightsV1DialogflowSource
    gcsSource: GoogleCloudContactcenterinsightsV1GcsSource

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationLevelSentiment(
    typing_extensions.TypedDict, total=False
):
    channelTag: int
    sentimentData: GoogleCloudContactcenterinsightsV1SentimentData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationLevelSilence(
    typing_extensions.TypedDict, total=False
):
    silenceDuration: str
    silencePercentage: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationParticipant(
    typing_extensions.TypedDict, total=False
):
    dialogflowParticipant: str
    dialogflowParticipantName: str
    obfuscatedExternalUserId: str
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    userId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationQualityMetadata(
    typing_extensions.TypedDict, total=False
):
    agentInfo: _list[
        GoogleCloudContactcenterinsightsV1ConversationQualityMetadataAgentInfo
    ]
    customerSatisfactionRating: int
    menuPath: str
    waitDuration: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationQualityMetadataAgentInfo(
    typing_extensions.TypedDict, total=False
):
    agentId: str
    agentType: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    displayName: str
    dispositionCode: str
    location: str
    team: str
    teams: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationSummarizationSuggestionData(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    confidence: float
    conversationModel: str
    metadata: dict[str, typing.Any]
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscript(
    typing_extensions.TypedDict, total=False
):
    transcriptSegments: _list[
        GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegment
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegment(
    typing_extensions.TypedDict, total=False
):
    channelTag: int
    confidence: float
    dialogflowSegmentMetadata: GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata
    languageCode: str
    messageTime: str
    segmentParticipant: GoogleCloudContactcenterinsightsV1ConversationParticipant
    sentiment: GoogleCloudContactcenterinsightsV1SentimentData
    text: str
    words: _list[
        GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentWordInfo
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata(
    typing_extensions.TypedDict, total=False
):
    smartReplyAllowlistCovered: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentWordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateAnalysisOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    conversation: str
    createTime: str
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1CreateIssueRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1CreateIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1IssueModel
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CreateIssueRequest(
    typing_extensions.TypedDict, total=False
):
    issue: GoogleCloudContactcenterinsightsV1Issue
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeleteIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1DeleteIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeleteIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1DeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployIssueModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DeployQaScorecardRevisionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DialogflowIntent(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DialogflowInteractionData(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    dialogflowIntentId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DialogflowSource(
    typing_extensions.TypedDict, total=False
):
    audioUri: str
    dialogflowConversation: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Dimension(
    typing_extensions.TypedDict, total=False
):
    agentDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionAgentDimensionMetadata
    )
    dimensionKey: typing_extensions.Literal[
        "DIMENSION_KEY_UNSPECIFIED",
        "ISSUE",
        "AGENT",
        "AGENT_TEAM",
        "QA_QUESTION_ID",
        "QA_QUESTION_ANSWER_VALUE",
        "CONVERSATION_PROFILE_ID",
    ]
    issueDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionIssueDimensionMetadata
    )
    qaQuestionAnswerDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionQaQuestionAnswerDimensionMetadata
    )
    qaQuestionDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1DimensionQaQuestionDimensionMetadata
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionAgentDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    agentDisplayName: str
    agentId: str
    agentTeam: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionIssueDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    issueDisplayName: str
    issueId: str
    issueModelId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionQaQuestionAnswerDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    answerValue: str
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DimensionQaQuestionDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1EncryptionSpec(
    typing_extensions.TypedDict, total=False
):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Entity(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    metadata: dict[str, typing.Any]
    salience: float
    sentiment: GoogleCloudContactcenterinsightsV1SentimentData
    type: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    entityUniqueId: str
    sentiment: GoogleCloudContactcenterinsightsV1SentimentData
    type: typing_extensions.Literal["MENTION_TYPE_UNSPECIFIED", "PROPER", "COMMON"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExactMatchConfig(
    typing_extensions.TypedDict, total=False
):
    caseSensitive: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest(
    typing_extensions.TypedDict, total=False
):
    bigQueryDestination: (
        GoogleCloudContactcenterinsightsV1ExportInsightsDataRequestBigQueryDestination
    )
    filter: str
    kmsKey: str
    parent: str
    writeDisposition: typing_extensions.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataRequestBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    projectId: str
    table: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportInsightsDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1ExportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: (
        GoogleCloudContactcenterinsightsV1ExportIssueModelRequestGcsDestination
    )
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelRequestGcsDestination(
    typing_extensions.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ExportIssueModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1FaqAnswerData(
    typing_extensions.TypedDict, total=False
):
    answer: str
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    question: str
    source: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1FeedbackLabel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    label: str
    labeledResource: str
    name: str
    qaAnswerLabel: GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1GcsSource(
    typing_extensions.TypedDict, total=False
):
    audioUri: str
    transcriptUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1HoldData(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1ImportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    createNewModel: bool
    gcsSource: GoogleCloudContactcenterinsightsV1ImportIssueModelRequestGcsSource
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelRequestGcsSource(
    typing_extensions.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ImportIssueModelResponse(
    typing_extensions.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1IssueModel

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    ingestConversationsStats: GoogleCloudContactcenterinsightsV1IngestConversationsMetadataIngestConversationsStats
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1IngestConversationsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsMetadataIngestConversationsStats(
    typing_extensions.TypedDict, total=False
):
    duplicatesSkippedCount: int
    failedIngestCount: int
    processedObjectCount: int
    successfulIngestCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsRequest(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    agentChannel: int
    agentId: str
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsRequestGcsSource(
    typing_extensions.TypedDict, total=False
):
    bucketObjectType: typing_extensions.Literal[
        "BUCKET_OBJECT_TYPE_UNSPECIFIED", "TRANSCRIPT", "AUDIO"
    ]
    bucketUri: str
    customMetadataKeys: _list[str]
    metadataBucketUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsRequestTranscriptObjectConfig(
    typing_extensions.TypedDict, total=False
):
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IngestConversationsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecRequest(
    typing_extensions.TypedDict, total=False
):
    encryptionSpec: GoogleCloudContactcenterinsightsV1EncryptionSpec

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Intent(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IntentMatchData(
    typing_extensions.TypedDict, total=False
):
    intentUniqueId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1InterruptionData(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Issue(typing_extensions.TypedDict, total=False):
    createTime: str
    displayDescription: str
    displayName: str
    name: str
    sampleUtterances: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueAssignment(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    issue: str
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueMatchData(
    typing_extensions.TypedDict, total=False
):
    issueAssignment: GoogleCloudContactcenterinsightsV1IssueAssignment

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    inputDataConfig: GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig
    issueCount: str
    languageCode: str
    modelType: typing_extensions.Literal["MODEL_TYPE_UNSPECIFIED", "TYPE_V1", "TYPE_V2"]
    name: str
    state: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    filter: str
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    trainingConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelLabelStats(
    typing_extensions.TypedDict, total=False
):
    analyzedConversationsCount: str
    issueStats: dict[str, typing.Any]
    unclassifiedConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelLabelStatsIssueStats(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    issue: str
    labeledConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelResult(
    typing_extensions.TypedDict, total=False
):
    issueModel: str
    issues: _list[GoogleCloudContactcenterinsightsV1IssueAssignment]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponse(
    typing_extensions.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAnalysesResponse(
    typing_extensions.TypedDict, total=False
):
    analyses: _list[GoogleCloudContactcenterinsightsV1Analysis]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponse(
    typing_extensions.TypedDict, total=False
):
    analysisRules: _list[GoogleCloudContactcenterinsightsV1AnalysisRule]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversations: _list[GoogleCloudContactcenterinsightsV1Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponse(
    typing_extensions.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssueModelsResponse(
    typing_extensions.TypedDict, total=False
):
    issueModels: _list[GoogleCloudContactcenterinsightsV1IssueModel]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssuesResponse(
    typing_extensions.TypedDict, total=False
):
    issues: _list[GoogleCloudContactcenterinsightsV1Issue]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    phraseMatchers: _list[GoogleCloudContactcenterinsightsV1PhraseMatcher]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaQuestionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    qaQuestions: _list[GoogleCloudContactcenterinsightsV1QaQuestion]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    qaScorecardRevisions: _list[GoogleCloudContactcenterinsightsV1QaScorecardRevision]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaScorecardsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    qaScorecards: _list[GoogleCloudContactcenterinsightsV1QaScorecard]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListViewsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    views: _list[GoogleCloudContactcenterinsightsV1View]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchData(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    phraseMatcher: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchRule(
    typing_extensions.TypedDict, total=False
):
    config: GoogleCloudContactcenterinsightsV1PhraseMatchRuleConfig
    negated: bool
    query: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchRuleConfig(
    typing_extensions.TypedDict, total=False
):
    exactMatchConfig: GoogleCloudContactcenterinsightsV1ExactMatchConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup(
    typing_extensions.TypedDict, total=False
):
    phraseMatchRules: _list[GoogleCloudContactcenterinsightsV1PhraseMatchRule]
    type: typing_extensions.Literal[
        "PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED", "ALL_OF", "ANY_OF"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatcher(
    typing_extensions.TypedDict, total=False
):
    activationUpdateTime: str
    active: bool
    displayName: str
    name: str
    phraseMatchRuleGroups: _list[GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup]
    revisionCreateTime: str
    revisionId: str
    roleMatch: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    type: typing_extensions.Literal[
        "PHRASE_MATCHER_TYPE_UNSPECIFIED", "ALL_OF", "ANY_OF"
    ]
    updateTime: str
    versionTag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaAnswer(
    typing_extensions.TypedDict, total=False
):
    answerSources: _list[GoogleCloudContactcenterinsightsV1QaAnswerAnswerSource]
    answerValue: GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue
    conversation: str
    qaQuestion: str
    questionBody: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaAnswerAnswerSource(
    typing_extensions.TypedDict, total=False
):
    answerValue: GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue
    sourceType: typing_extensions.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED", "MANUAL_EDIT"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaAnswerAnswerValue(
    typing_extensions.TypedDict, total=False
):
    boolValue: bool
    key: str
    naValue: bool
    normalizedScore: float
    numValue: float
    potentialScore: float
    score: float
    strValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestion(
    typing_extensions.TypedDict, total=False
):
    abbreviation: str
    answerChoices: _list[GoogleCloudContactcenterinsightsV1QaQuestionAnswerChoice]
    answerInstructions: str
    createTime: str
    metrics: GoogleCloudContactcenterinsightsV1QaQuestionMetrics
    name: str
    order: int
    questionBody: str
    tags: _list[str]
    tuningMetadata: GoogleCloudContactcenterinsightsV1QaQuestionTuningMetadata
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionAnswerChoice(
    typing_extensions.TypedDict, total=False
):
    boolValue: bool
    key: str
    naValue: bool
    numValue: float
    score: float
    strValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionMetrics(
    typing_extensions.TypedDict, total=False
):
    accuracy: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionTuningMetadata(
    typing_extensions.TypedDict, total=False
):
    datasetValidationWarnings: _list[
        typing_extensions.Literal[
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
class GoogleCloudContactcenterinsightsV1QaScorecard(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardResult(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    score: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardResultScoreSource(
    typing_extensions.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    qaTagResults: _list[GoogleCloudContactcenterinsightsV1QaScorecardResultQaTagResult]
    score: float
    sourceType: typing_extensions.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED_ONLY", "INCLUDES_MANUAL_EDITS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardRevision(
    typing_extensions.TypedDict, total=False
):
    alternateIds: _list[str]
    createTime: str
    name: str
    snapshot: GoogleCloudContactcenterinsightsV1QaScorecard
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "EDITABLE",
        "TRAINING",
        "TRAINING_FAILED",
        "READY",
        "DELETING",
        "TRAINING_CANCELLED",
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsMetadata(
    typing_extensions.TypedDict, total=False
):
    resultIsTruncated: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[GoogleCloudContactcenterinsightsV1Dimension]
    filter: str
    measureMask: str
    timeGranularity: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    location: str
    macroAverageSlice: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSlice
    slices: _list[GoogleCloudContactcenterinsightsV1QueryMetricsResponseSlice]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSlice(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[GoogleCloudContactcenterinsightsV1Dimension]
    timeSeries: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceTimeSeries
    total: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPoint

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPoint(
    typing_extensions.TypedDict, total=False
):
    conversationMeasure: GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasure
    interval: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasure(
    typing_extensions.TypedDict, total=False
):
    averageAgentSentimentScore: float
    averageClientSentimentScore: float
    averageCustomerSatisfactionRating: float
    averageDuration: str
    averageQaNormalizedScore: float
    averageQaQuestionNormalizedScore: float
    averageSilencePercentage: float
    averageTurnCount: float
    conversationCount: int
    qaTagScores: _list[
        GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore(
    typing_extensions.TypedDict, total=False
):
    averageTagNormalizedScore: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceTimeSeries(
    typing_extensions.TypedDict, total=False
):
    dataPoints: _list[
        GoogleCloudContactcenterinsightsV1QueryMetricsResponseSliceDataPoint
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1RedactionConfig(
    typing_extensions.TypedDict, total=False
):
    deidentifyTemplate: str
    inspectTemplate: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1RuntimeAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationId: str
    answerFeedback: GoogleCloudContactcenterinsightsV1AnswerFeedback
    articleSuggestion: GoogleCloudContactcenterinsightsV1ArticleSuggestionData
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
    typing_extensions.TypedDict, total=False
):
    generatorName: str
    query: str
    querySource: typing_extensions.Literal[
        "QUERY_SOURCE_UNSPECIFIED", "AGENT_QUERY", "SUGGESTED_QUERY"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SentimentData(
    typing_extensions.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Settings(
    typing_extensions.TypedDict, total=False
):
    analysisConfig: GoogleCloudContactcenterinsightsV1SettingsAnalysisConfig
    conversationTtl: str
    createTime: str
    languageCode: str
    name: str
    pubsubNotificationSettings: dict[str, typing.Any]
    redactionConfig: GoogleCloudContactcenterinsightsV1RedactionConfig
    speechConfig: GoogleCloudContactcenterinsightsV1SpeechConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SettingsAnalysisConfig(
    typing_extensions.TypedDict, total=False
):
    annotatorSelector: GoogleCloudContactcenterinsightsV1AnnotatorSelector
    runtimeIntegrationAnalysisPercentage: float
    uploadConversationAnalysisPercentage: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SilenceData(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SmartComposeSuggestionData(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    suggestion: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SmartReplyData(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    reply: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SpeechConfig(
    typing_extensions.TypedDict, total=False
):
    speechRecognizer: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1TuneQaScorecardRevisionRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1UndeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployIssueModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UndeployQaScorecardRevisionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UploadConversationMetadata(
    typing_extensions.TypedDict, total=False
):
    analysisOperation: str
    appliedRedactionConfig: GoogleCloudContactcenterinsightsV1RedactionConfig
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1UploadConversationRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1UploadConversationRequest(
    typing_extensions.TypedDict, total=False
):
    conversation: GoogleCloudContactcenterinsightsV1Conversation
    conversationId: str
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1RedactionConfig
    speechConfig: GoogleCloudContactcenterinsightsV1SpeechConfig

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1View(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    updateTime: str
    value: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Analysis(
    typing_extensions.TypedDict, total=False
):
    analysisResult: GoogleCloudContactcenterinsightsV1alpha1AnalysisResult
    annotatorSelector: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector
    createTime: str
    name: str
    requestTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnalysisResult(
    typing_extensions.TypedDict, total=False
):
    callAnalysisMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1AnalysisResultCallAnalysisMetadata
    )
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnalysisResultCallAnalysisMetadata(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    transcriptIndex: int
    wordIndex: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector(
    typing_extensions.TypedDict, total=False
):
    issueModels: _list[str]
    phraseMatchers: _list[str]
    qaConfig: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorQaConfig
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
    typing_extensions.TypedDict, total=False
):
    scorecardList: (
        GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorQaConfigScorecardList
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorQaConfigScorecardList(
    typing_extensions.TypedDict, total=False
):
    qaScorecardRevisions: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorSummarizationConfig(
    typing_extensions.TypedDict, total=False
):
    conversationProfile: str
    summarizationModel: typing_extensions.Literal[
        "SUMMARIZATION_MODEL_UNSPECIFIED", "BASELINE_MODEL", "BASELINE_MODEL_V2_0"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1AnswerFeedback(
    typing_extensions.TypedDict, total=False
):
    clicked: bool
    correctnessLevel: typing_extensions.Literal[
        "CORRECTNESS_LEVEL_UNSPECIFIED",
        "NOT_CORRECT",
        "PARTIALLY_CORRECT",
        "FULLY_CORRECT",
    ]
    displayed: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ArticleSuggestionData(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    source: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsMetadata(
    typing_extensions.TypedDict, total=False
):
    completedAnalysesCount: int
    createTime: str
    endTime: str
    failedAnalysesCount: int
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsRequest
    totalRequestedAnalysesCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsRequest(
    typing_extensions.TypedDict, total=False
):
    analysisPercentage: float
    annotatorSelector: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector
    filter: str
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    failedAnalysisCount: int
    successfulAnalysisCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool
    maxDeleteCount: int
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1BulkDeleteConversationsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CallAnnotation(
    typing_extensions.TypedDict, total=False
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
class GoogleCloudContactcenterinsightsV1alpha1Conversation(
    typing_extensions.TypedDict, total=False
):
    agentId: str
    callMetadata: GoogleCloudContactcenterinsightsV1alpha1ConversationCallMetadata
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
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
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
    typing_extensions.TypedDict, total=False
):
    agentChannel: int
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationDataSource(
    typing_extensions.TypedDict, total=False
):
    dialogflowSource: GoogleCloudContactcenterinsightsV1alpha1DialogflowSource
    gcsSource: GoogleCloudContactcenterinsightsV1alpha1GcsSource

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSentiment(
    typing_extensions.TypedDict, total=False
):
    channelTag: int
    sentimentData: GoogleCloudContactcenterinsightsV1alpha1SentimentData

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSilence(
    typing_extensions.TypedDict, total=False
):
    silenceDuration: str
    silencePercentage: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationParticipant(
    typing_extensions.TypedDict, total=False
):
    dialogflowParticipant: str
    dialogflowParticipantName: str
    obfuscatedExternalUserId: str
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    userId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadata(
    typing_extensions.TypedDict, total=False
):
    agentInfo: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadataAgentInfo
    ]
    customerSatisfactionRating: int
    menuPath: str
    waitDuration: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadataAgentInfo(
    typing_extensions.TypedDict, total=False
):
    agentId: str
    agentType: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER", "ANY_AGENT"
    ]
    displayName: str
    dispositionCode: str
    location: str
    team: str
    teams: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationSummarizationSuggestionData(
    typing_extensions.TypedDict, total=False
):
    answerRecord: str
    confidence: float
    conversationModel: str
    metadata: dict[str, typing.Any]
    text: str
    textSections: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscript(
    typing_extensions.TypedDict, total=False
):
    transcriptSegments: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegment
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegment(
    typing_extensions.TypedDict, total=False
):
    channelTag: int
    confidence: float
    dialogflowSegmentMetadata: GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata
    languageCode: str
    messageTime: str
    segmentParticipant: GoogleCloudContactcenterinsightsV1alpha1ConversationParticipant
    sentiment: GoogleCloudContactcenterinsightsV1alpha1SentimentData
    text: str
    words: _list[
        GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentWordInfo
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata(
    typing_extensions.TypedDict, total=False
):
    smartReplyAllowlistCovered: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentWordInfo(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    endOffset: str
    startOffset: str
    word: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateAnalysisOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    annotatorSelector: GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelector
    conversation: str
    createTime: str
    endTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1CreateIssueRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1CreateIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1alpha1IssueModel
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateIssueRequest(
    typing_extensions.TypedDict, total=False
):
    issue: GoogleCloudContactcenterinsightsV1alpha1Issue
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeleteIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1DeleteIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeleteIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DeployIssueModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DialogflowIntent(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DialogflowInteractionData(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    dialogflowIntentId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DialogflowSource(
    typing_extensions.TypedDict, total=False
):
    audioUri: str
    dialogflowConversation: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Dimension(
    typing_extensions.TypedDict, total=False
):
    agentDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionAgentDimensionMetadata
    )
    dimensionKey: typing_extensions.Literal[
        "DIMENSION_KEY_UNSPECIFIED",
        "ISSUE",
        "AGENT",
        "AGENT_TEAM",
        "QA_QUESTION_ID",
        "QA_QUESTION_ANSWER_VALUE",
        "CONVERSATION_PROFILE_ID",
    ]
    issueDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionIssueDimensionMetadata
    )
    qaQuestionAnswerDimensionMetadata: GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionAnswerDimensionMetadata
    qaQuestionDimensionMetadata: (
        GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionDimensionMetadata
    )

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionAgentDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    agentDisplayName: str
    agentId: str
    agentTeam: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionIssueDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    issueDisplayName: str
    issueId: str
    issueModelId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionAnswerDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    answerValue: str
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1DimensionQaQuestionDimensionMetadata(
    typing_extensions.TypedDict, total=False
):
    qaQuestionId: str
    qaScorecardId: str
    questionBody: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1EncryptionSpec(
    typing_extensions.TypedDict, total=False
):
    kmsKey: str
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Entity(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    metadata: dict[str, typing.Any]
    salience: float
    sentiment: GoogleCloudContactcenterinsightsV1alpha1SentimentData
    type: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    entityUniqueId: str
    sentiment: GoogleCloudContactcenterinsightsV1alpha1SentimentData
    type: typing_extensions.Literal["MENTION_TYPE_UNSPECIFIED", "PROPER", "COMMON"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequest(
    typing_extensions.TypedDict, total=False
):
    bigQueryDestination: GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination
    filter: str
    kmsKey: str
    parent: str
    writeDisposition: typing_extensions.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    projectId: str
    table: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: (
        GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequestGcsDestination
    )
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelRequestGcsDestination(
    typing_extensions.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ExportIssueModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1FaqAnswerData(
    typing_extensions.TypedDict, total=False
):
    answer: str
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    question: str
    source: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1FeedbackLabel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    label: str
    labeledResource: str
    name: str
    qaAnswerLabel: GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1GcsSource(
    typing_extensions.TypedDict, total=False
):
    audioUri: str
    transcriptUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1HoldData(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    createNewModel: bool
    gcsSource: GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequestGcsSource
    parent: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelRequestGcsSource(
    typing_extensions.TypedDict, total=False
):
    objectUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ImportIssueModelResponse(
    typing_extensions.TypedDict, total=False
):
    issueModel: GoogleCloudContactcenterinsightsV1alpha1IssueModel

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    ingestConversationsStats: GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadataIngestConversationsStats
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadataIngestConversationsStats(
    typing_extensions.TypedDict, total=False
):
    duplicatesSkippedCount: int
    failedIngestCount: int
    processedObjectCount: int
    successfulIngestCount: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequest(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    agentChannel: int
    agentId: str
    customerChannel: int

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestGcsSource(
    typing_extensions.TypedDict, total=False
):
    bucketObjectType: typing_extensions.Literal[
        "BUCKET_OBJECT_TYPE_UNSPECIFIED", "TRANSCRIPT", "AUDIO"
    ]
    bucketUri: str
    customMetadataKeys: _list[str]
    metadataBucketUri: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestTranscriptObjectConfig(
    typing_extensions.TypedDict, total=False
):
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IngestConversationsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    partialErrors: _list[GoogleRpcStatus]
    request: GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecRequest(
    typing_extensions.TypedDict, total=False
):
    encryptionSpec: GoogleCloudContactcenterinsightsV1alpha1EncryptionSpec

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InitializeEncryptionSpecResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Intent(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IntentMatchData(
    typing_extensions.TypedDict, total=False
):
    intentUniqueId: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1InterruptionData(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1Issue(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayDescription: str
    displayName: str
    name: str
    sampleUtterances: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueAssignment(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    issue: str
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueMatchData(
    typing_extensions.TypedDict, total=False
):
    issueAssignment: GoogleCloudContactcenterinsightsV1alpha1IssueAssignment

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    inputDataConfig: GoogleCloudContactcenterinsightsV1alpha1IssueModelInputDataConfig
    issueCount: str
    languageCode: str
    modelType: typing_extensions.Literal["MODEL_TYPE_UNSPECIFIED", "TYPE_V1", "TYPE_V2"]
    name: str
    state: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    filter: str
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    trainingConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStats(
    typing_extensions.TypedDict, total=False
):
    analyzedConversationsCount: str
    issueStats: dict[str, typing.Any]
    unclassifiedConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStatsIssueStats(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    issue: str
    labeledConversationsCount: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1IssueModelResult(
    typing_extensions.TypedDict, total=False
):
    issueModel: str
    issues: _list[GoogleCloudContactcenterinsightsV1alpha1IssueAssignment]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ListAllFeedbackLabelsResponse(
    typing_extensions.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1alpha1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1ListFeedbackLabelsResponse(
    typing_extensions.TypedDict, total=False
):
    feedbackLabels: _list[GoogleCloudContactcenterinsightsV1alpha1FeedbackLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    phraseMatcher: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaAnswer(
    typing_extensions.TypedDict, total=False
):
    answerSources: _list[GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerSource]
    answerValue: GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue
    conversation: str
    qaQuestion: str
    questionBody: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerSource(
    typing_extensions.TypedDict, total=False
):
    answerValue: GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue
    sourceType: typing_extensions.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED", "MANUAL_EDIT"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaAnswerAnswerValue(
    typing_extensions.TypedDict, total=False
):
    boolValue: bool
    key: str
    naValue: bool
    normalizedScore: float
    numValue: float
    potentialScore: float
    score: float
    strValue: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaScorecardResult(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    score: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QaScorecardResultScoreSource(
    typing_extensions.TypedDict, total=False
):
    normalizedScore: float
    potentialScore: float
    qaTagResults: _list[
        GoogleCloudContactcenterinsightsV1alpha1QaScorecardResultQaTagResult
    ]
    score: float
    sourceType: typing_extensions.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "SYSTEM_GENERATED_ONLY", "INCLUDES_MANUAL_EDITS"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsMetadata(
    typing_extensions.TypedDict, total=False
):
    resultIsTruncated: bool

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponse(
    typing_extensions.TypedDict, total=False
):
    location: str
    macroAverageSlice: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSlice
    slices: _list[GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSlice]
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSlice(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[GoogleCloudContactcenterinsightsV1alpha1Dimension]
    timeSeries: (
        GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceTimeSeries
    )
    total: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPoint

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPoint(
    typing_extensions.TypedDict, total=False
):
    conversationMeasure: GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasure
    interval: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasure(
    typing_extensions.TypedDict, total=False
):
    averageAgentSentimentScore: float
    averageClientSentimentScore: float
    averageCustomerSatisfactionRating: float
    averageDuration: str
    averageQaNormalizedScore: float
    averageQaQuestionNormalizedScore: float
    averageSilencePercentage: float
    averageTurnCount: float
    conversationCount: int
    qaTagScores: _list[
        GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPointConversationMeasureQaTagScore(
    typing_extensions.TypedDict, total=False
):
    averageTagNormalizedScore: float
    tag: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceTimeSeries(
    typing_extensions.TypedDict, total=False
):
    dataPoints: _list[
        GoogleCloudContactcenterinsightsV1alpha1QueryMetricsResponseSliceDataPoint
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1RedactionConfig(
    typing_extensions.TypedDict, total=False
):
    deidentifyTemplate: str
    inspectTemplate: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1RuntimeAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationId: str
    answerFeedback: GoogleCloudContactcenterinsightsV1alpha1AnswerFeedback
    articleSuggestion: GoogleCloudContactcenterinsightsV1alpha1ArticleSuggestionData
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
    typing_extensions.TypedDict, total=False
):
    generatorName: str
    query: str
    querySource: typing_extensions.Literal[
        "QUERY_SOURCE_UNSPECIFIED", "AGENT_QUERY", "SUGGESTED_QUERY"
    ]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SentimentData(
    typing_extensions.TypedDict, total=False
):
    magnitude: float
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SilenceData(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SmartComposeSuggestionData(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    suggestion: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SmartReplyData(
    typing_extensions.TypedDict, total=False
):
    confidenceScore: float
    metadata: dict[str, typing.Any]
    queryRecord: str
    reply: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1SpeechConfig(
    typing_extensions.TypedDict, total=False
):
    speechRecognizer: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UndeployIssueModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UploadConversationMetadata(
    typing_extensions.TypedDict, total=False
):
    analysisOperation: str
    appliedRedactionConfig: GoogleCloudContactcenterinsightsV1alpha1RedactionConfig
    createTime: str
    endTime: str
    request: GoogleCloudContactcenterinsightsV1alpha1UploadConversationRequest

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1UploadConversationRequest(
    typing_extensions.TypedDict, total=False
):
    conversation: GoogleCloudContactcenterinsightsV1alpha1Conversation
    conversationId: str
    parent: str
    redactionConfig: GoogleCloudContactcenterinsightsV1alpha1RedactionConfig
    speechConfig: GoogleCloudContactcenterinsightsV1alpha1SpeechConfig

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
class GoogleTypeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
