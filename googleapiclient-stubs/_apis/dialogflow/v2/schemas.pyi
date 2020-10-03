import typing

import typing_extensions

class GoogleCloudDialogflowV2BatchUpdateIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    intentView: typing_extensions.Literal["INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"]
    updateMask: str
    intentBatchInline: GoogleCloudDialogflowV2IntentBatch
    languageCode: str
    intentBatchUri: str

class GoogleCloudDialogflowV2beta1Intent(typing_extensions.TypedDict, total=False):
    displayName: str
    rootFollowupIntentName: str
    priority: int
    endInteraction: bool
    mlEnabled: bool
    messages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    defaultResponsePlatforms: typing.List[str]
    parentFollowupIntentName: str
    action: str
    followupIntentInfo: typing.List[
        GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo
    ]
    isFallback: bool
    inputContextNames: typing.List[str]
    events: typing.List[str]
    resetContexts: bool
    name: str
    trainingPhrases: typing.List[GoogleCloudDialogflowV2beta1IntentTrainingPhrase]
    parameters: typing.List[GoogleCloudDialogflowV2beta1IntentParameter]
    mlDisabled: bool
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]

class GoogleCloudDialogflowV3alpha1CreateVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

class GoogleCloudDialogflowV2BatchDeleteEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    entityTypeNames: typing.List[str]

class GoogleCloudDialogflowV2beta1IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

class GoogleCloudDialogflowV2RestoreAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowV2IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    subtitle: str
    items: typing.List[GoogleCloudDialogflowV2IntentMessageListSelectItem]
    title: str

class GoogleCloudDialogflowV2beta1IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]
    parts: typing.List[GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart]
    timesAddedCount: int
    name: str

class GoogleCloudDialogflowV2SearchAgentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    agents: typing.List[GoogleCloudDialogflowV2Agent]

class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo(
    typing_extensions.TypedDict, total=False
):
    value: typing.Any
    justCollected: bool
    state: typing_extensions.Literal[
        "PARAMETER_STATE_UNSPECIFIED", "EMPTY", "INVALID", "FILLED"
    ]
    required: bool
    displayName: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard(
    typing_extensions.TypedDict, total=False
):
    cardContents: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent]
    cardWidth: typing_extensions.Literal["CARD_WIDTH_UNSPECIFIED", "SMALL", "MEDIUM"]

class GoogleCloudDialogflowV2beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    largeImage: GoogleCloudDialogflowV2beta1IntentMessageImage
    contentUrl: str
    description: str
    name: str
    icon: GoogleCloudDialogflowV2beta1IntentMessageImage

class GoogleCloudDialogflowV2IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

class GoogleCloudDialogflowV2beta1IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    header: str
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]

class GoogleCloudDialogflowV2DetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    outputAudioConfigMask: str
    outputAudioConfig: GoogleCloudDialogflowV2OutputAudioConfig
    inputAudio: str
    queryInput: GoogleCloudDialogflowV2QueryInput
    queryParams: GoogleCloudDialogflowV2QueryParameters

class GoogleCloudDialogflowV2IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    dividerAfter: bool
    cells: typing.List[GoogleCloudDialogflowV2IntentMessageTableCardCell]

class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse
    ]

class GoogleCloudDialogflowV2BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2EntityType]

class GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    key: str
    synonyms: typing.List[str]

class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    url: str
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]

class GoogleCloudDialogflowV2BatchDeleteEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    entityValues: typing.List[str]

class GoogleCloudDialogflowCxV3beta1SessionInfo(
    typing_extensions.TypedDict, total=False
):
    parameters: typing.Dict[str, typing.Any]
    session: str

class GoogleCloudDialogflowV2IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    formattedText: str
    subtitle: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    title: str
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageBasicCardButton]

class GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowV3alpha1ExportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    content: str

class GoogleCloudDialogflowV2BatchCreateEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    entities: typing.List[GoogleCloudDialogflowV2EntityTypeEntity]

class GoogleCloudDialogflowV2beta1SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2beta1Sentiment

class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    uri: str
    audio: str

class GoogleCloudDialogflowV2ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction(
    typing_extensions.TypedDict, total=False
):
    openUrl: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri
    postbackData: str
    dial: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial
    shareLocation: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation
    text: str

class GoogleCloudDialogflowV2beta1KnowledgeAnswers(
    typing_extensions.TypedDict, total=False
):
    answers: typing.List[GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer]

class GoogleCloudDialogflowV2DetectIntentResponse(
    typing_extensions.TypedDict, total=False
):
    queryResult: GoogleCloudDialogflowV2QueryResult
    outputAudio: str
    webhookStatus: GoogleRpcStatus
    responseId: str
    outputAudioConfig: GoogleCloudDialogflowV2OutputAudioConfig

class GoogleCloudDialogflowV2IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    text: str
    postback: str

class GoogleCloudDialogflowV2BatchDeleteIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2Intent]

class GoogleCloudDialogflowV2Message(typing_extensions.TypedDict, total=False):
    content: str
    messageAnnotation: GoogleCloudDialogflowV2MessageAnnotation
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    createTime: str
    name: str
    participant: str
    languageCode: str

class GoogleCloudDialogflowV2beta1IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    title: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo

class GoogleCloudDialogflowV2ListIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    intents: typing.List[GoogleCloudDialogflowV2Intent]

class GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio(
    typing_extensions.TypedDict, total=False
):
    audioUri: str

class GoogleCloudDialogflowV2beta1IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]

class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowV2AnnotatedMessagePart(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    formattedValue: typing.Any
    text: str

class GoogleCloudDialogflowV2IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    subtitle: str
    title: str
    imageUri: str
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageCardButton]

class GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText(
    typing_extensions.TypedDict, total=False
):
    text: str
    allowPlaybackInterruption: bool
    ssml: str

class GoogleCloudDialogflowCxV3beta1ImportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str

class GoogleCloudDialogflowV2EventInput(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    languageCode: str
    name: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion(
    typing_extensions.TypedDict, total=False
):
    reply: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply
    action: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction

class GoogleCloudDialogflowV2beta1IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    title: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    subtitle: str
    formattedText: str
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    response: typing.Dict[str, typing.Any]
    done: bool
    metadata: typing.Dict[str, typing.Any]
    name: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer(
    typing_extensions.TypedDict, total=False
):
    matchConfidenceLevel: typing_extensions.Literal[
        "MATCH_CONFIDENCE_LEVEL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    source: str
    faqQuestion: str
    matchConfidence: float
    answer: str

class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    title: str
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage

class GoogleCloudDialogflowV3alpha1ExportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2beta1KnowledgeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

class GoogleCloudDialogflowV2MessageAnnotation(
    typing_extensions.TypedDict, total=False
):
    containEntities: bool
    parts: typing.List[GoogleCloudDialogflowV2AnnotatedMessagePart]

class GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard(
    typing_extensions.TypedDict, total=False
):
    thumbnailImageAlignment: typing_extensions.Literal[
        "THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT"
    ]
    cardOrientation: typing_extensions.Literal[
        "CARD_ORIENTATION_UNSPECIFIED", "HORIZONTAL", "VERTICAL"
    ]
    cardContent: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent

class GoogleCloudDialogflowV2Fulfillment(typing_extensions.TypedDict, total=False):
    features: typing.List[GoogleCloudDialogflowV2FulfillmentFeature]
    genericWebService: GoogleCloudDialogflowV2FulfillmentGenericWebService
    enabled: bool
    name: str
    displayName: str

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
    items: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem
    ]

class GoogleCloudDialogflowV2IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

class GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    icon: GoogleCloudDialogflowV2IntentMessageImage
    name: str
    contentUrl: str
    description: str
    largeImage: GoogleCloudDialogflowV2IntentMessageImage

class GoogleCloudDialogflowV2IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    quickReplies: typing.List[str]
    title: str

class GoogleCloudDialogflowV2SynthesizeSpeechConfig(
    typing_extensions.TypedDict, total=False
):
    pitch: float
    speakingRate: float
    volumeGainDb: float
    effectsProfileId: typing.List[str]
    voice: GoogleCloudDialogflowV2VoiceSelectionParams

class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo(
    typing_extensions.TypedDict, total=False
):
    lastMatchedIntent: str
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    image: GoogleCloudDialogflowV2IntentMessageImage
    title: str
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo
    description: str

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[
        GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment
    ]

class GoogleCloudDialogflowCxV3beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
    targetPage: str
    fulfillmentResponse: GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    targetFlow: str
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
    alternativeQueryResults: typing.List[GoogleCloudDialogflowV2beta1QueryResult]
    responseId: str
    originalDetectIntentRequest: GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest
    session: str
    queryResult: GoogleCloudDialogflowV2beta1QueryResult

class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction
    title: str

class GoogleCloudDialogflowV2ValidationError(typing_extensions.TypedDict, total=False):
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "CRITICAL"
    ]
    entries: typing.List[str]
    errorMessage: str

class GoogleCloudDialogflowV2WebhookRequest(typing_extensions.TypedDict, total=False):
    responseId: str
    queryResult: GoogleCloudDialogflowV2QueryResult
    originalDetectIntentRequest: GoogleCloudDialogflowV2OriginalDetectIntentRequest
    session: str

class GoogleCloudDialogflowV2beta1EntityType(typing_extensions.TypedDict, total=False):
    enableFuzzyExtraction: bool
    displayName: str
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    name: str

class GoogleCloudDialogflowV2FulfillmentFeature(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SMALLTALK"]

class GoogleCloudDialogflowV2IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    textToSpeech: str
    displayText: str
    ssml: str

class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    title: str
    footer: str

class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[
        GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItem
    ]
    imageDisplayOptions: typing_extensions.Literal[
        "IMAGE_DISPLAY_OPTIONS_UNSPECIFIED",
        "GRAY",
        "WHITE",
        "CROPPED",
        "BLURRED_BACKGROUND",
    ]

class GoogleCloudDialogflowV2ImportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff(
    typing_extensions.TypedDict, total=False
):
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: typing.List[GoogleCloudDialogflowV2IntentMessageSimpleResponse]

class GoogleCloudDialogflowV2IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: typing.List[GoogleCloudDialogflowV2IntentMessageSuggestion]

class GoogleCloudDialogflowV2BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2Intent]

class GoogleCloudDialogflowCxV3beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
    intentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo
    detectIntentResponseId: str
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    messages: typing.List[GoogleCloudDialogflowCxV3beta1ResponseMessage]
    payload: typing.Dict[str, typing.Any]
    fulfillmentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo

class GoogleCloudDialogflowV2SentimentAnalysisRequestConfig(
    typing_extensions.TypedDict, total=False
):
    analyzeQueryTextSentiment: bool

class GoogleCloudDialogflowV2beta1EventInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    followupIntentName: str
    parentFollowupIntentName: str

class GoogleCloudDialogflowV2beta1AnnotatedConversationDataset(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    exampleCount: str
    completedExampleCount: str
    questionTypeName: str
    createTime: str
    name: str
    description: str

class GoogleCloudDialogflowV3alpha1ImportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2beta1EntityTypeEntity(
    typing_extensions.TypedDict, total=False
):
    value: str
    synonyms: typing.List[str]

class GoogleCloudDialogflowV2WebhookResponse(typing_extensions.TypedDict, total=False):
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    payload: typing.Dict[str, typing.Any]
    source: str
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2SessionEntityType]
    fulfillmentText: str
    followupEventInput: GoogleCloudDialogflowV2EventInput

class GoogleCloudDialogflowV2IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]
    header: str

class GoogleCloudDialogflowV2OutputAudioConfig(
    typing_extensions.TypedDict, total=False
):
    audioEncoding: typing_extensions.Literal[
        "OUTPUT_AUDIO_ENCODING_UNSPECIFIED",
        "OUTPUT_AUDIO_ENCODING_LINEAR_16",
        "OUTPUT_AUDIO_ENCODING_MP3",
        "OUTPUT_AUDIO_ENCODING_OGG_OPUS",
    ]
    sampleRateHertz: int
    synthesizeSpeechConfig: GoogleCloudDialogflowV2SynthesizeSpeechConfig

class GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    version: str
    source: str
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2beta1Intent]

class GoogleCloudDialogflowV2IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo
    title: str
    image: GoogleCloudDialogflowV2IntentMessageImage

class GoogleCloudDialogflowV2FulfillmentGenericWebService(
    typing_extensions.TypedDict, total=False
):
    username: str
    uri: str
    isCloudFunction: bool
    requestHeaders: typing.Dict[str, typing.Any]
    password: str

class GoogleCloudDialogflowV2beta1IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2beta1IntentMessageListSelectItem]
    title: str
    subtitle: str

class GoogleCloudDialogflowV2beta1Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

class GoogleCloudDialogflowV2SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2Sentiment

class GoogleCloudDialogflowV2beta1QueryResult(typing_extensions.TypedDict, total=False):
    action: str
    languageCode: str
    webhookSource: str
    diagnosticInfo: typing.Dict[str, typing.Any]
    parameters: typing.Dict[str, typing.Any]
    allRequiredParamsPresent: bool
    webhookPayload: typing.Dict[str, typing.Any]
    knowledgeAnswers: GoogleCloudDialogflowV2beta1KnowledgeAnswers
    speechRecognitionConfidence: float
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    fulfillmentText: str
    sentimentAnalysisResult: GoogleCloudDialogflowV2beta1SentimentAnalysisResult
    queryText: str
    intent: GoogleCloudDialogflowV2beta1Intent
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    intentDetectionConfidence: float

class GoogleCloudDialogflowCxV3beta1ResponseMessageText(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    text: typing.List[str]

class GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo(
    typing_extensions.TypedDict, total=False
):
    tag: str

class GoogleCloudDialogflowV2IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    name: str
    timesAddedCount: int
    parts: typing.List[GoogleCloudDialogflowV2IntentTrainingPhrasePart]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]

class GoogleCloudDialogflowV2InputAudioConfig(typing_extensions.TypedDict, total=False):
    sampleRateHertz: int
    speechContexts: typing.List[GoogleCloudDialogflowV2SpeechContext]
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED",
        "AUDIO_ENCODING_LINEAR_16",
        "AUDIO_ENCODING_FLAC",
        "AUDIO_ENCODING_MULAW",
        "AUDIO_ENCODING_AMR",
        "AUDIO_ENCODING_AMR_WB",
        "AUDIO_ENCODING_OGG_OPUS",
        "AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE",
    ]
    modelVariant: typing_extensions.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]
    model: str
    enableWordInfo: bool
    singleUtterance: bool
    phraseHints: typing.List[str]
    languageCode: str

class GoogleCloudDialogflowV2IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    synonyms: typing.List[str]
    key: str

class GoogleCloudDialogflowV2beta1IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]
    mediaObjects: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject
    ]

class GoogleCloudDialogflowV2beta1IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    postback: str
    text: str

class GoogleCloudDialogflowV2BatchUpdateEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    languageCode: str
    entities: typing.List[GoogleCloudDialogflowV2EntityTypeEntity]

class GoogleCloudDialogflowV2TextInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str

class GoogleCloudDialogflowV2Sentiment(typing_extensions.TypedDict, total=False):
    score: float
    magnitude: float

class GoogleCloudDialogflowV2IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    title: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageBasicCardButton]
    columnProperties: typing.List[GoogleCloudDialogflowV2IntentMessageColumnProperties]
    subtitle: str
    rows: typing.List[GoogleCloudDialogflowV2IntentMessageTableCardRow]

class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia(
    typing_extensions.TypedDict, total=False
):
    height: typing_extensions.Literal["HEIGHT_UNSPECIFIED", "SHORT", "MEDIUM", "TALL"]
    thumbnailUri: str
    fileUri: str

class GoogleCloudDialogflowV2Agent(typing_extensions.TypedDict, total=False):
    supportedLanguageCodes: typing.List[str]
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED", "TIER_STANDARD", "TIER_ENTERPRISE", "TIER_ENTERPRISE_PLUS"
    ]
    description: str
    parent: str
    enableLogging: bool
    apiVersion: typing_extensions.Literal[
        "API_VERSION_UNSPECIFIED",
        "API_VERSION_V1",
        "API_VERSION_V2",
        "API_VERSION_V2_BETA_1",
    ]
    defaultLanguageCode: str
    matchMode: typing_extensions.Literal[
        "MATCH_MODE_UNSPECIFIED", "MATCH_MODE_HYBRID", "MATCH_MODE_ML_ONLY"
    ]
    classificationThreshold: float
    avatarUri: str
    timeZone: str
    displayName: str

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent(
    typing_extensions.TypedDict, total=False
):
    suggestions: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]
    title: str
    description: str
    media: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia

class GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess(
    typing_extensions.TypedDict, total=False
):
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    destinationName: str
    uri: str

class GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    entityTypeBatchInline: GoogleCloudDialogflowV2EntityTypeBatch
    languageCode: str
    updateMask: str
    entityTypeBatchUri: str

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudDialogflowCxV3beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

class GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2beta1EntityType]

class GoogleCloudDialogflowV2EntityTypeBatch(typing_extensions.TypedDict, total=False):
    entityTypes: typing.List[GoogleCloudDialogflowV2EntityType]

class GoogleCloudDialogflowV2Environment(typing_extensions.TypedDict, total=False):
    updateTime: str
    name: str
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STOPPED", "LOADING", "RUNNING"
    ]
    agentVersion: str

class GoogleCloudDialogflowV2QueryResult(typing_extensions.TypedDict, total=False):
    diagnosticInfo: typing.Dict[str, typing.Any]
    fulfillmentText: str
    webhookPayload: typing.Dict[str, typing.Any]
    queryText: str
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    sentimentAnalysisResult: GoogleCloudDialogflowV2SentimentAnalysisResult
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    action: str
    intentDetectionConfidence: float
    speechRecognitionConfidence: float
    intent: GoogleCloudDialogflowV2Intent
    allRequiredParamsPresent: bool
    languageCode: str
    parameters: typing.Dict[str, typing.Any]
    webhookSource: str

class GoogleCloudDialogflowV2beta1AutoApproveSmartMessagingEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    disabledCount: int
    enabledCount: int
    unreviewedCount: int

class GoogleCloudDialogflowV2EntityType(typing_extensions.TypedDict, total=False):
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    name: str
    displayName: str
    enableFuzzyExtraction: bool
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    entities: typing.List[GoogleCloudDialogflowV2EntityTypeEntity]

class GoogleCloudDialogflowV2IntentParameter(typing_extensions.TypedDict, total=False):
    defaultValue: str
    mandatory: bool
    entityTypeDisplayName: str
    displayName: str
    value: str
    name: str
    prompts: typing.List[str]
    isList: bool

class GoogleCloudDialogflowV2Context(typing_extensions.TypedDict, total=False):
    lifespanCount: int
    parameters: typing.Dict[str, typing.Any]
    name: str

class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem]

class GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech(
    typing_extensions.TypedDict, total=False
):
    text: str
    ssml: str

class GoogleCloudDialogflowV2IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    imageUri: str
    accessibilityText: str

class GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    destinationName: str
    uri: str

class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValue(
    typing_extensions.TypedDict, total=False
):
    resolvedValue: typing.Any
    originalValue: str

class GoogleCloudDialogflowV2beta1IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    imageUri: str
    title: str
    subtitle: str
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageCardButton]

class GoogleCloudDialogflowV2beta1IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    imageUri: str
    accessibilityText: str

class GoogleCloudDialogflowV2beta1IntentMessage(
    typing_extensions.TypedDict, total=False
):
    text: GoogleCloudDialogflowV2beta1IntentMessageText
    payload: typing.Dict[str, typing.Any]
    telephonySynthesizeSpeech: GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech
    card: GoogleCloudDialogflowV2beta1IntentMessageCard
    listSelect: GoogleCloudDialogflowV2beta1IntentMessageListSelect
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    browseCarouselCard: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard
    rbmCarouselRichCard: GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard
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
    linkOutSuggestion: GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion
    rbmText: GoogleCloudDialogflowV2beta1IntentMessageRbmText
    suggestions: GoogleCloudDialogflowV2beta1IntentMessageSuggestions
    telephonyPlayAudio: GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio
    tableCard: GoogleCloudDialogflowV2beta1IntentMessageTableCard
    telephonyTransferCall: GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall
    mediaContent: GoogleCloudDialogflowV2beta1IntentMessageMediaContent
    rbmStandaloneRichCard: GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard
    simpleResponses: GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses
    quickReplies: GoogleCloudDialogflowV2beta1IntentMessageQuickReplies
    carouselSelect: GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect
    basicCard: GoogleCloudDialogflowV2beta1IntentMessageBasicCard

class GoogleCloudDialogflowV2beta1IntentParameter(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    entityTypeDisplayName: str
    value: str
    defaultValue: str
    isList: bool
    mandatory: bool
    prompts: typing.List[str]

class GoogleCloudDialogflowV2beta1IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    columnProperties: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageColumnProperties
    ]
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    subtitle: str
    title: str
    rows: typing.List[GoogleCloudDialogflowV2beta1IntentMessageTableCardRow]

class GoogleCloudDialogflowV2IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    alias: str
    text: str
    userDefined: bool
    entityType: str

class GoogleCloudDialogflowV2IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]

class GoogleCloudDialogflowV2ListContextsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    contexts: typing.List[GoogleCloudDialogflowV2Context]

class GoogleCloudDialogflowV2IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2IntentMessageCarouselSelectItem]

class GoogleCloudDialogflowV3alpha1ImportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str

class GoogleCloudDialogflowV2beta1IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

class GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse(
    typing_extensions.TypedDict, total=False
):
    mergeBehavior: typing_extensions.Literal[
        "MERGE_BEHAVIOR_UNSPECIFIED", "APPEND", "REPLACE"
    ]
    messages: typing.List[GoogleCloudDialogflowCxV3beta1ResponseMessage]

class GoogleCloudDialogflowV2EntityTypeEntity(typing_extensions.TypedDict, total=False):
    synonyms: typing.List[str]
    value: str

class GoogleCloudDialogflowV2ConversationEvent(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    newMessagePayload: GoogleCloudDialogflowV2Message
    errorStatus: GoogleRpcStatus
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CONVERSATION_STARTED",
        "CONVERSATION_FINISHED",
        "HUMAN_INTERVENTION_NEEDED",
        "NEW_MESSAGE",
        "UNRECOVERABLE_ERROR",
    ]

class GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audioUri: str

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

class GoogleCloudDialogflowV2SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entities: typing.List[GoogleCloudDialogflowV2EntityTypeEntity]
    name: str
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]

class GoogleCloudDialogflowV2beta1Context(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    lifespanCount: int
    name: str

class GoogleCloudDialogflowV2Intent(typing_extensions.TypedDict, total=False):
    mlDisabled: bool
    followupIntentInfo: typing.List[GoogleCloudDialogflowV2IntentFollowupIntentInfo]
    resetContexts: bool
    displayName: str
    trainingPhrases: typing.List[GoogleCloudDialogflowV2IntentTrainingPhrase]
    rootFollowupIntentName: str
    parentFollowupIntentName: str
    isFallback: bool
    name: str
    inputContextNames: typing.List[str]
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]
    defaultResponsePlatforms: typing.List[str]
    events: typing.List[str]
    action: str
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    parameters: typing.List[GoogleCloudDialogflowV2IntentParameter]
    messages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    priority: int

class GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction(
    typing_extensions.TypedDict, total=False
): ...
class GoogleCloudDialogflowV2TrainAgentRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV3alpha1ImportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    names: typing.List[str]

class GoogleCloudDialogflowV2ValidationResult(typing_extensions.TypedDict, total=False):
    validationErrors: typing.List[GoogleCloudDialogflowV2ValidationError]

class GoogleCloudDialogflowV2IntentMessage(typing_extensions.TypedDict, total=False):
    suggestions: GoogleCloudDialogflowV2IntentMessageSuggestions
    browseCarouselCard: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard
    simpleResponses: GoogleCloudDialogflowV2IntentMessageSimpleResponses
    quickReplies: GoogleCloudDialogflowV2IntentMessageQuickReplies
    mediaContent: GoogleCloudDialogflowV2IntentMessageMediaContent
    image: GoogleCloudDialogflowV2IntentMessageImage
    text: GoogleCloudDialogflowV2IntentMessageText
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
    card: GoogleCloudDialogflowV2IntentMessageCard
    basicCard: GoogleCloudDialogflowV2IntentMessageBasicCard
    payload: typing.Dict[str, typing.Any]
    tableCard: GoogleCloudDialogflowV2IntentMessageTableCard
    carouselSelect: GoogleCloudDialogflowV2IntentMessageCarouselSelect
    linkOutSuggestion: GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion
    listSelect: GoogleCloudDialogflowV2IntentMessageListSelect

class GoogleCloudDialogflowV2IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]
    mediaObjects: typing.List[
        GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject
    ]

class GoogleCloudDialogflowV2beta1IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: typing.List[GoogleCloudDialogflowV2beta1IntentMessageSuggestion]

class GoogleCloudDialogflowV2beta1IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    cells: typing.List[GoogleCloudDialogflowV2beta1IntentMessageTableCardCell]
    dividerAfter: bool

class GoogleCloudDialogflowV2QueryParameters(typing_extensions.TypedDict, total=False):
    sentimentAnalysisRequestConfig: GoogleCloudDialogflowV2SentimentAnalysisRequestConfig
    payload: typing.Dict[str, typing.Any]
    contexts: typing.List[GoogleCloudDialogflowV2Context]
    timeZone: str
    resetContexts: bool
    geoLocation: GoogleTypeLatLng
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2SessionEntityType]

class GoogleCloudDialogflowV2IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction
    title: str

class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing_extensions.TypedDict, total=False
):
    footer: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    title: str
    description: str
    openUriAction: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction

class GoogleCloudDialogflowV3alpha1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply(
    typing_extensions.TypedDict, total=False
):
    postbackData: str
    text: str

class GoogleCloudDialogflowCxV3beta1PageInfoFormInfo(
    typing_extensions.TypedDict, total=False
):
    parameterInfo: typing.List[
        GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo
    ]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2QueryInput(typing_extensions.TypedDict, total=False):
    text: GoogleCloudDialogflowV2TextInput
    event: GoogleCloudDialogflowV2EventInput
    audioConfig: GoogleCloudDialogflowV2InputAudioConfig

class GoogleCloudDialogflowV2OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    version: str
    payload: typing.Dict[str, typing.Any]
    source: str

class GoogleCloudDialogflowV2SpeechContext(typing_extensions.TypedDict, total=False):
    phrases: typing.List[str]
    boost: float

class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]
    url: str

class GoogleCloudDialogflowV2ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    entityTypes: typing.List[GoogleCloudDialogflowV2EntityType]

class GoogleCloudDialogflowCxV3beta1PageInfo(typing_extensions.TypedDict, total=False):
    formInfo: GoogleCloudDialogflowCxV3beta1PageInfoFormInfo
    currentPage: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmText(
    typing_extensions.TypedDict, total=False
):
    text: str
    rbmSuggestion: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]

class GoogleCloudDialogflowV2beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2beta1SessionEntityType]
    followupEventInput: GoogleCloudDialogflowV2beta1EventInput
    fulfillmentText: str
    endInteraction: bool
    source: str
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

class GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    text: str
    alias: str
    userDefined: bool
    entityType: str

class GoogleCloudDialogflowV2IntentBatch(typing_extensions.TypedDict, total=False):
    intents: typing.List[GoogleCloudDialogflowV2Intent]

class GoogleCloudDialogflowV2ListSessionEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2SessionEntityType]

class GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    followupIntentName: str
    parentFollowupIntentName: str

class GoogleCloudDialogflowCxV3beta1ResponseMessage(
    typing_extensions.TypedDict, total=False
):
    liveAgentHandoff: GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff
    text: GoogleCloudDialogflowCxV3beta1ResponseMessageText
    endInteraction: GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction
    outputAudioText: GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText
    payload: typing.Dict[str, typing.Any]
    mixedAudio: GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio
    conversationSuccess: GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess
    playAudio: GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio

class GoogleCloudDialogflowV2beta1LabelConversationResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedConversationDataset: GoogleCloudDialogflowV2beta1AnnotatedConversationDataset

class GoogleCloudDialogflowV2beta1IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    title: str
    quickReplies: typing.List[str]

class GoogleCloudDialogflowV2ExportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentUri: str

class GoogleCloudDialogflowV2ListEnvironmentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    environments: typing.List[GoogleCloudDialogflowV2Environment]

class GoogleCloudDialogflowV2beta1SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    name: str
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]

class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    displayText: str
    textToSpeech: str
    ssml: str
