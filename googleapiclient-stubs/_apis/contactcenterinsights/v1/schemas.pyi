import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1Analysis(
    typing_extensions.TypedDict, total=False
):
    analysisResult: GoogleCloudContactcenterinsightsV1AnalysisResult
    createTime: str
    name: str
    requestTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisResult(
    typing_extensions.TypedDict, total=False
):
    callAnalysisMetadata: GoogleCloudContactcenterinsightsV1AnalysisResultCallAnalysisMetadata
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
    sentiments: _list[GoogleCloudContactcenterinsightsV1ConversationLevelSentiment]

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnnotationBoundary(
    typing_extensions.TypedDict, total=False
):
    transcriptIndex: int
    wordIndex: int

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
    conversationCountTimeSeries: GoogleCloudContactcenterinsightsV1CalculateStatsResponseTimeSeries
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
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "PHONE_CALL", "CHAT"]
    name: str
    obfuscatedUserId: str
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
    conversation: str
    createTime: str
    endTime: str

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
    bigQueryDestination: GoogleCloudContactcenterinsightsV1ExportInsightsDataRequestBigQueryDestination
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
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueAssignment(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    issue: str
    score: float

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    inputDataConfig: GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig
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
class GoogleCloudContactcenterinsightsV1ListAnalysesResponse(
    typing_extensions.TypedDict, total=False
):
    analyses: _list[GoogleCloudContactcenterinsightsV1Analysis]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversations: _list[GoogleCloudContactcenterinsightsV1Conversation]
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
class GoogleCloudContactcenterinsightsV1RuntimeAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationId: str
    answerFeedback: GoogleCloudContactcenterinsightsV1AnswerFeedback
    articleSuggestion: GoogleCloudContactcenterinsightsV1ArticleSuggestionData
    createTime: str
    dialogflowInteraction: GoogleCloudContactcenterinsightsV1DialogflowInteractionData
    endBoundary: GoogleCloudContactcenterinsightsV1AnnotationBoundary
    faqAnswer: GoogleCloudContactcenterinsightsV1FaqAnswerData
    smartComposeSuggestion: GoogleCloudContactcenterinsightsV1SmartComposeSuggestionData
    smartReply: GoogleCloudContactcenterinsightsV1SmartReplyData
    startBoundary: GoogleCloudContactcenterinsightsV1AnnotationBoundary

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
    updateTime: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SettingsAnalysisConfig(
    typing_extensions.TypedDict, total=False
):
    runtimeIntegrationAnalysisPercentage: float

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
class GoogleCloudContactcenterinsightsV1View(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    updateTime: str
    value: str

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1alpha1CreateAnalysisOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    createTime: str
    endTime: str

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
class GoogleCloudContactcenterinsightsV1alpha1IssueModel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    inputDataConfig: GoogleCloudContactcenterinsightsV1alpha1IssueModelInputDataConfig
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
