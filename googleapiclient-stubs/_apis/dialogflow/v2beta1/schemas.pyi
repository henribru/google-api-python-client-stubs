import typing

import typing_extensions

class GoogleCloudDialogflowV2beta1ValidationResult(
    typing_extensions.TypedDict, total=False
):
    validationErrors: typing.List[GoogleCloudDialogflowV2beta1ValidationError]

class GoogleCloudDialogflowV2beta1IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageCardButton]
    subtitle: str
    imageUri: str
    title: str

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[GoogleLongrunningOperation]
    nextPageToken: str

class GoogleCloudDialogflowCxV3beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowV2beta1Document(typing_extensions.TypedDict, total=False):
    rawContent: str
    contentUri: str
    content: str
    latestReloadStatus: GoogleCloudDialogflowV2beta1DocumentReloadStatus
    enableAutoReload: bool
    name: str
    displayName: str
    knowledgeTypes: typing.List[str]
    mimeType: str

class GoogleCloudDialogflowV2beta1IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: typing.List[GoogleCloudDialogflowV2beta1IntentMessageSuggestion]

class GoogleCloudDialogflowV2beta1Sentiment(typing_extensions.TypedDict, total=False):
    score: float
    magnitude: float

class GoogleCloudDialogflowV2MessageAnnotation(
    typing_extensions.TypedDict, total=False
):
    parts: typing.List[GoogleCloudDialogflowV2AnnotatedMessagePart]
    containEntities: bool

class GoogleCloudDialogflowV2SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    name: str
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    entities: typing.List[GoogleCloudDialogflowV2EntityTypeEntity]

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    response: typing.Dict[str, typing.Any]
    done: bool
    metadata: typing.Dict[str, typing.Any]
    name: str

class GoogleCloudDialogflowV2beta1ListDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    documents: typing.List[GoogleCloudDialogflowV2beta1Document]
    nextPageToken: str

class GoogleCloudDialogflowV2beta1IntentParameter(
    typing_extensions.TypedDict, total=False
):
    value: str
    entityTypeDisplayName: str
    isList: bool
    prompts: typing.List[str]
    displayName: str
    defaultValue: str
    name: str
    mandatory: bool

class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowV2beta1IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    text: str
    postback: str

class GoogleCloudDialogflowV2beta1KnowledgeAnswers(
    typing_extensions.TypedDict, total=False
):
    answers: typing.List[GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer]

class GoogleCloudDialogflowV2IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]
    header: str

class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValue(
    typing_extensions.TypedDict, total=False
):
    resolvedValue: typing.Any
    originalValue: str

class GoogleCloudDialogflowV2beta1SpeechContext(
    typing_extensions.TypedDict, total=False
):
    phrases: typing.List[str]
    boost: float

class GoogleCloudDialogflowV2beta1IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    accessibilityText: str
    imageUri: str

class GoogleCloudDialogflowV2EventInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    entityTypeBatchInline: GoogleCloudDialogflowV2beta1EntityTypeBatch
    entityTypeBatchUri: str
    updateMask: str

class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    url: str
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]

class GoogleCloudDialogflowV2beta1BatchCreateEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    languageCode: str

class GoogleCloudDialogflowV2IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    image: GoogleCloudDialogflowV2IntentMessageImage
    description: str
    title: str
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo

class GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff(
    typing_extensions.TypedDict, total=False
):
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1BatchDeleteEntityTypesRequest(
    typing_extensions.TypedDict, total=False
):
    entityTypeNames: typing.List[str]

class GoogleCloudDialogflowV2beta1AutoApproveSmartMessagingEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    disabledCount: int
    unreviewedCount: int
    enabledCount: int

class GoogleCloudDialogflowV2beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
    responseId: str
    originalDetectIntentRequest: GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest
    queryResult: GoogleCloudDialogflowV2beta1QueryResult
    session: str
    alternativeQueryResults: typing.List[GoogleCloudDialogflowV2beta1QueryResult]

class GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer(
    typing_extensions.TypedDict, total=False
):
    matchConfidenceLevel: typing_extensions.Literal[
        "MATCH_CONFIDENCE_LEVEL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    source: str
    answer: str
    matchConfidence: float
    faqQuestion: str

class GoogleCloudDialogflowV2beta1Environment(typing_extensions.TypedDict, total=False):
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STOPPED", "LOADING", "RUNNING"
    ]
    agentVersion: str
    name: str
    updateTime: str

class GoogleCloudDialogflowV2IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    title: str
    imageUri: str
    subtitle: str
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageCardButton]

class GoogleCloudDialogflowV2beta1IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]

class GoogleCloudDialogflowV3alpha1ImportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction(
    typing_extensions.TypedDict, total=False
):
    openUrl: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri
    postbackData: str
    shareLocation: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation
    text: str
    dial: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial

class GoogleCloudDialogflowV2beta1QueryResult(typing_extensions.TypedDict, total=False):
    knowledgeAnswers: GoogleCloudDialogflowV2beta1KnowledgeAnswers
    webhookSource: str
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    allRequiredParamsPresent: bool
    diagnosticInfo: typing.Dict[str, typing.Any]
    sentimentAnalysisResult: GoogleCloudDialogflowV2beta1SentimentAnalysisResult
    intent: GoogleCloudDialogflowV2beta1Intent
    intentDetectionConfidence: float
    languageCode: str
    webhookPayload: typing.Dict[str, typing.Any]
    queryText: str
    speechRecognitionConfidence: float
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    fulfillmentText: str
    parameters: typing.Dict[str, typing.Any]
    action: str

class GoogleCloudDialogflowV2beta1BatchUpdateEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    updateMask: str
    languageCode: str

class GoogleCloudDialogflowV2beta1VoiceSelectionParams(
    typing_extensions.TypedDict, total=False
):
    name: str
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED",
        "SSML_VOICE_GENDER_MALE",
        "SSML_VOICE_GENDER_FEMALE",
        "SSML_VOICE_GENDER_NEUTRAL",
    ]

class GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

class GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo(
    typing_extensions.TypedDict, total=False
):
    value: typing.Any
    required: bool
    displayName: str
    justCollected: bool
    state: typing_extensions.Literal[
        "PARAMETER_STATE_UNSPECIFIED", "EMPTY", "INVALID", "FILLED"
    ]

class GoogleCloudDialogflowV2beta1IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]
    header: str

class GoogleCloudDialogflowV2beta1QueryInput(typing_extensions.TypedDict, total=False):
    text: GoogleCloudDialogflowV2beta1TextInput
    event: GoogleCloudDialogflowV2beta1EventInput
    audioConfig: GoogleCloudDialogflowV2beta1InputAudioConfig

class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleCloudDialogflowV2Message(typing_extensions.TypedDict, total=False):
    createTime: str
    messageAnnotation: GoogleCloudDialogflowV2MessageAnnotation
    participant: str
    name: str
    languageCode: str
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    content: str

class GoogleCloudDialogflowV2Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

class GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText(
    typing_extensions.TypedDict, total=False
):
    ssml: str
    text: str
    allowPlaybackInterruption: bool

class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    image: GoogleCloudDialogflowV2IntentMessageImage
    footer: str
    description: str
    title: str

class GoogleCloudDialogflowV2Context(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    name: str
    lifespanCount: int

class GoogleCloudDialogflowCxV3beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
    targetFlow: str
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    fulfillmentResponse: GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse
    payload: typing.Dict[str, typing.Any]
    targetPage: str
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo

class GoogleCloudDialogflowV2IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: typing.List[GoogleCloudDialogflowV2IntentMessageSimpleResponse]

class GoogleCloudDialogflowV2beta1ListEnvironmentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    environments: typing.List[GoogleCloudDialogflowV2beta1Environment]

class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse
    ]

class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    ssml: str
    textToSpeech: str
    displayText: str

class GoogleCloudDialogflowV2IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    dividerAfter: bool
    cells: typing.List[GoogleCloudDialogflowV2IntentMessageTableCardCell]

class GoogleCloudDialogflowV2beta1FulfillmentGenericWebService(
    typing_extensions.TypedDict, total=False
):
    uri: str
    isCloudFunction: bool
    username: str
    requestHeaders: typing.Dict[str, typing.Any]
    password: str

class GoogleCloudDialogflowV2ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

class GoogleCloudDialogflowV2beta1ImportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

class GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    uri: str
    destinationName: str

class GoogleCloudDialogflowV2beta1Context(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    name: str
    lifespanCount: int

class GoogleCloudDialogflowV2IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo
    title: str
    image: GoogleCloudDialogflowV2IntentMessageImage

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

class GoogleCloudDialogflowV2IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2IntentMessageCarouselSelectItem]

class GoogleCloudDialogflowV2IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    subtitle: str
    title: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    formattedText: str
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageBasicCardButton]

class GoogleCloudDialogflowV2IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    synonyms: typing.List[str]
    key: str

class GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    destinationName: str
    uri: str

class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo(
    typing_extensions.TypedDict, total=False
):
    parameters: typing.Dict[str, typing.Any]
    lastMatchedIntent: str

class GoogleCloudDialogflowV2beta1IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    description: str
    title: str
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo

class GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio(
    typing_extensions.TypedDict, total=False
):
    audioUri: str

class GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    icon: GoogleCloudDialogflowV2IntentMessageImage
    contentUrl: str
    largeImage: GoogleCloudDialogflowV2IntentMessageImage
    description: str
    name: str

class GoogleCloudDialogflowV2beta1IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class GoogleCloudDialogflowV2beta1ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2beta1EntityType]
    nextPageToken: str

class GoogleCloudDialogflowCxV3beta1ResponseMessage(
    typing_extensions.TypedDict, total=False
):
    endInteraction: GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction
    mixedAudio: GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio
    liveAgentHandoff: GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff
    playAudio: GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio
    text: GoogleCloudDialogflowCxV3beta1ResponseMessageText
    payload: typing.Dict[str, typing.Any]
    conversationSuccess: GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess
    outputAudioText: GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText

class GoogleCloudDialogflowV2beta1EntityTypeBatch(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2beta1EntityType]

class GoogleCloudDialogflowV2beta1FulfillmentFeature(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SMALLTALK"]

class GoogleCloudDialogflowV2EntityTypeEntity(typing_extensions.TypedDict, total=False):
    synonyms: typing.List[str]
    value: str

class GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    audioUri: str

class GoogleCloudDialogflowV2IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    quickReplies: typing.List[str]
    title: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmText(
    typing_extensions.TypedDict, total=False
):
    rbmSuggestion: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]
    text: str

class GoogleCloudDialogflowV2beta1ReloadDocumentRequest(
    typing_extensions.TypedDict, total=False
):
    gcsSource: GoogleCloudDialogflowV2beta1GcsSource

class GoogleCloudDialogflowCxV3beta1PageInfoFormInfo(
    typing_extensions.TypedDict, total=False
):
    parameterInfo: typing.List[
        GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo
    ]

class GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    knowledgeBases: typing.List[GoogleCloudDialogflowV2beta1KnowledgeBase]

class GoogleCloudDialogflowV2IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    subtitle: str
    items: typing.List[GoogleCloudDialogflowV2IntentMessageListSelectItem]
    title: str

class GoogleCloudDialogflowV2beta1DetectIntentResponse(
    typing_extensions.TypedDict, total=False
):
    queryResult: GoogleCloudDialogflowV2beta1QueryResult
    webhookStatus: GoogleRpcStatus
    outputAudioConfig: GoogleCloudDialogflowV2beta1OutputAudioConfig
    outputAudio: str
    responseId: str
    alternativeQueryResults: typing.List[GoogleCloudDialogflowV2beta1QueryResult]

class GoogleCloudDialogflowV2IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    imageUri: str
    accessibilityText: str

class GoogleCloudDialogflowV2QueryResult(typing_extensions.TypedDict, total=False):
    fulfillmentText: str
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    diagnosticInfo: typing.Dict[str, typing.Any]
    action: str
    webhookPayload: typing.Dict[str, typing.Any]
    sentimentAnalysisResult: GoogleCloudDialogflowV2SentimentAnalysisResult
    queryText: str
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    languageCode: str
    speechRecognitionConfidence: float
    webhookSource: str
    allRequiredParamsPresent: bool
    intent: GoogleCloudDialogflowV2Intent
    parameters: typing.Dict[str, typing.Any]
    intentDetectionConfidence: float

class GoogleCloudDialogflowV2beta1SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2beta1Sentiment

class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem]

class GoogleCloudDialogflowV2IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: typing.List[GoogleCloudDialogflowV2IntentMessageSuggestion]

class GoogleCloudDialogflowV2beta1IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    title: str
    subtitle: str
    items: typing.List[GoogleCloudDialogflowV2beta1IntentMessageListSelectItem]

class GoogleCloudDialogflowV2beta1IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    quickReplies: typing.List[str]
    title: str

class GoogleCloudDialogflowV2beta1TrainAgentRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2beta1LabelConversationResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedConversationDataset: GoogleCloudDialogflowV2beta1AnnotatedConversationDataset

class GoogleCloudDialogflowV2ConversationEvent(
    typing_extensions.TypedDict, total=False
):
    newMessagePayload: GoogleCloudDialogflowV2Message
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CONVERSATION_STARTED",
        "CONVERSATION_FINISHED",
        "HUMAN_INTERVENTION_NEEDED",
        "NEW_MESSAGE",
        "UNRECOVERABLE_ERROR",
    ]
    conversation: str
    errorStatus: GoogleRpcStatus

class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]
    url: str

class GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse(
    typing_extensions.TypedDict, total=False
):
    messages: typing.List[GoogleCloudDialogflowCxV3beta1ResponseMessage]
    mergeBehavior: typing_extensions.Literal[
        "MERGE_BEHAVIOR_UNSPECIFIED", "APPEND", "REPLACE"
    ]

class GoogleCloudDialogflowV2beta1OutputAudioConfig(
    typing_extensions.TypedDict, total=False
):
    sampleRateHertz: int
    audioEncoding: typing_extensions.Literal[
        "OUTPUT_AUDIO_ENCODING_UNSPECIFIED",
        "OUTPUT_AUDIO_ENCODING_LINEAR_16",
        "OUTPUT_AUDIO_ENCODING_MP3",
        "OUTPUT_AUDIO_ENCODING_OGG_OPUS",
    ]
    synthesizeSpeechConfig: GoogleCloudDialogflowV2beta1SynthesizeSpeechConfig

class GoogleCloudDialogflowV2IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    subtitle: str
    columnProperties: typing.List[GoogleCloudDialogflowV2IntentMessageColumnProperties]
    image: GoogleCloudDialogflowV2IntentMessageImage
    title: str
    rows: typing.List[GoogleCloudDialogflowV2IntentMessageTableCardRow]
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageBasicCardButton]

class GoogleCloudDialogflowV2beta1ExportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentUri: str

class GoogleCloudDialogflowV2SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2Sentiment

class GoogleCloudDialogflowV2IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

class GoogleCloudDialogflowV2beta1SynthesizeSpeechConfig(
    typing_extensions.TypedDict, total=False
):
    pitch: float
    effectsProfileId: typing.List[str]
    volumeGainDb: float
    speakingRate: float
    voice: GoogleCloudDialogflowV2beta1VoiceSelectionParams

class GoogleCloudDialogflowCxV3beta1ImportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str

class GoogleCloudDialogflowV2beta1RestoreAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess(
    typing_extensions.TypedDict, total=False
):
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2EntityType]

class GoogleCloudDialogflowV2beta1Fulfillment(typing_extensions.TypedDict, total=False):
    displayName: str
    enabled: bool
    features: typing.List[GoogleCloudDialogflowV2beta1FulfillmentFeature]
    name: str
    genericWebService: GoogleCloudDialogflowV2beta1FulfillmentGenericWebService

class GoogleCloudDialogflowV2beta1Agent(typing_extensions.TypedDict, total=False):
    defaultLanguageCode: str
    parent: str
    apiVersion: typing_extensions.Literal[
        "API_VERSION_UNSPECIFIED",
        "API_VERSION_V1",
        "API_VERSION_V2",
        "API_VERSION_V2_BETA_1",
    ]
    avatarUri: str
    enableLogging: bool
    timeZone: str
    supportedLanguageCodes: typing.List[str]
    displayName: str
    classificationThreshold: float
    matchMode: typing_extensions.Literal[
        "MATCH_MODE_UNSPECIFIED", "MATCH_MODE_HYBRID", "MATCH_MODE_ML_ONLY"
    ]
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED", "TIER_STANDARD", "TIER_ENTERPRISE", "TIER_ENTERPRISE_PLUS"
    ]
    description: str

class GoogleCloudDialogflowV2beta1EventInput(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    name: str
    languageCode: str

class GoogleCloudDialogflowV2beta1IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

class GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2beta1SessionEntityType]

class GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

class GoogleCloudDialogflowV2beta1SentimentAnalysisRequestConfig(
    typing_extensions.TypedDict, total=False
):
    analyzeQueryTextSentiment: bool

class GoogleCloudDialogflowV2beta1GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2beta1EntityType]

class GoogleCloudDialogflowCxV3beta1PageInfo(typing_extensions.TypedDict, total=False):
    formInfo: GoogleCloudDialogflowCxV3beta1PageInfoFormInfo
    currentPage: str

class GoogleCloudDialogflowV2beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    source: str
    payload: typing.Dict[str, typing.Any]
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    followupEventInput: GoogleCloudDialogflowV2beta1EventInput
    fulfillmentText: str
    endInteraction: bool
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2beta1SessionEntityType]

class GoogleCloudDialogflowV2beta1BatchDeleteEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    entityValues: typing.List[str]

class GoogleCloudDialogflowV2beta1KnowledgeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

class GoogleCloudDialogflowV2beta1EntityType(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    displayName: str
    name: str
    enableFuzzyExtraction: bool
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]

class GoogleCloudDialogflowV2beta1EntityTypeEntity(
    typing_extensions.TypedDict, total=False
):
    synonyms: typing.List[str]
    value: str

class GoogleCloudDialogflowV2beta1Intent(typing_extensions.TypedDict, total=False):
    parentFollowupIntentName: str
    name: str
    rootFollowupIntentName: str
    mlEnabled: bool
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]
    parameters: typing.List[GoogleCloudDialogflowV2beta1IntentParameter]
    resetContexts: bool
    priority: int
    displayName: str
    mlDisabled: bool
    endInteraction: bool
    defaultResponsePlatforms: typing.List[str]
    inputContextNames: typing.List[str]
    isFallback: bool
    messages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    action: str
    events: typing.List[str]
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    trainingPhrases: typing.List[GoogleCloudDialogflowV2beta1IntentTrainingPhrase]
    followupIntentInfo: typing.List[
        GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo
    ]

class GoogleCloudDialogflowV3alpha1ExportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    content: str

class GoogleCloudDialogflowV2beta1AnnotatedConversationDataset(
    typing_extensions.TypedDict, total=False
):
    name: str
    questionTypeName: str
    displayName: str
    completedExampleCount: str
    exampleCount: str
    createTime: str
    description: str

class GoogleCloudDialogflowV3alpha1ImportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str

class GoogleCloudDialogflowV2beta1IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    columnProperties: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageColumnProperties
    ]
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    rows: typing.List[GoogleCloudDialogflowV2beta1IntentMessageTableCardRow]
    title: str
    subtitle: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard(
    typing_extensions.TypedDict, total=False
):
    cardContent: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent
    thumbnailImageAlignment: typing_extensions.Literal[
        "THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT"
    ]
    cardOrientation: typing_extensions.Literal[
        "CARD_ORIENTATION_UNSPECIFIED", "HORIZONTAL", "VERTICAL"
    ]

class GoogleCloudDialogflowV2beta1ListIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2beta1Intent]
    nextPageToken: str

class GoogleCloudDialogflowV2IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    name: str
    parts: typing.List[GoogleCloudDialogflowV2IntentTrainingPhrasePart]
    timesAddedCount: int
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]

class GoogleCloudDialogflowV2beta1KnowledgeBase(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    languageCode: str
    name: str

class GoogleCloudDialogflowV2WebhookResponse(typing_extensions.TypedDict, total=False):
    payload: typing.Dict[str, typing.Any]
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2SessionEntityType]
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    source: str
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    fulfillmentText: str
    followupEventInput: GoogleCloudDialogflowV2EventInput

class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent(
    typing_extensions.TypedDict, total=False
):
    description: str
    title: str
    media: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia
    suggestions: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]

class GoogleCloudDialogflowV2beta1IntentBatch(typing_extensions.TypedDict, total=False):
    intents: typing.List[GoogleCloudDialogflowV2beta1Intent]

class GoogleCloudDialogflowV2beta1TextInput(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia(
    typing_extensions.TypedDict, total=False
):
    thumbnailUri: str
    fileUri: str
    height: typing_extensions.Literal["HEIGHT_UNSPECIFIED", "SHORT", "MEDIUM", "TALL"]

class GoogleCloudDialogflowV3alpha1ImportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    names: typing.List[str]

class GoogleCloudDialogflowCxV3beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
    payload: typing.Dict[str, typing.Any]
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo
    fulfillmentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo
    messages: typing.List[GoogleCloudDialogflowCxV3beta1ResponseMessage]
    detectIntentResponseId: str
    intentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo

class GoogleCloudDialogflowV2beta1ValidationError(
    typing_extensions.TypedDict, total=False
):
    errorMessage: str
    entries: typing.List[str]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "CRITICAL"
    ]

class GoogleCloudDialogflowV2AnnotatedMessagePart(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    text: str
    formattedValue: typing.Any

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudDialogflowV2IntentMessage(typing_extensions.TypedDict, total=False):
    linkOutSuggestion: GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion
    mediaContent: GoogleCloudDialogflowV2IntentMessageMediaContent
    basicCard: GoogleCloudDialogflowV2IntentMessageBasicCard
    listSelect: GoogleCloudDialogflowV2IntentMessageListSelect
    carouselSelect: GoogleCloudDialogflowV2IntentMessageCarouselSelect
    payload: typing.Dict[str, typing.Any]
    simpleResponses: GoogleCloudDialogflowV2IntentMessageSimpleResponses
    text: GoogleCloudDialogflowV2IntentMessageText
    browseCarouselCard: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard
    tableCard: GoogleCloudDialogflowV2IntentMessageTableCard
    image: GoogleCloudDialogflowV2IntentMessageImage
    suggestions: GoogleCloudDialogflowV2IntentMessageSuggestions
    card: GoogleCloudDialogflowV2IntentMessageCard
    quickReplies: GoogleCloudDialogflowV2IntentMessageQuickReplies
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

class GoogleCloudDialogflowV2beta1IntentMessage(
    typing_extensions.TypedDict, total=False
):
    text: GoogleCloudDialogflowV2beta1IntentMessageText
    telephonyPlayAudio: GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio
    mediaContent: GoogleCloudDialogflowV2beta1IntentMessageMediaContent
    suggestions: GoogleCloudDialogflowV2beta1IntentMessageSuggestions
    rbmStandaloneRichCard: GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard
    telephonyTransferCall: GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall
    payload: typing.Dict[str, typing.Any]
    quickReplies: GoogleCloudDialogflowV2beta1IntentMessageQuickReplies
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
    listSelect: GoogleCloudDialogflowV2beta1IntentMessageListSelect
    linkOutSuggestion: GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion
    basicCard: GoogleCloudDialogflowV2beta1IntentMessageBasicCard
    card: GoogleCloudDialogflowV2beta1IntentMessageCard
    carouselSelect: GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    simpleResponses: GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses
    tableCard: GoogleCloudDialogflowV2beta1IntentMessageTableCard
    telephonySynthesizeSpeech: GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech
    rbmText: GoogleCloudDialogflowV2beta1IntentMessageRbmText
    browseCarouselCard: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard

class GoogleCloudDialogflowV2beta1SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply(
    typing_extensions.TypedDict, total=False
):
    postbackData: str
    text: str

class GoogleCloudDialogflowV2Intent(typing_extensions.TypedDict, total=False):
    inputContextNames: typing.List[str]
    priority: int
    defaultResponsePlatforms: typing.List[str]
    parameters: typing.List[GoogleCloudDialogflowV2IntentParameter]
    action: str
    displayName: str
    isFallback: bool
    resetContexts: bool
    events: typing.List[str]
    parentFollowupIntentName: str
    messages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    name: str
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    followupIntentInfo: typing.List[GoogleCloudDialogflowV2IntentFollowupIntentInfo]
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]
    rootFollowupIntentName: str
    mlDisabled: bool
    trainingPhrases: typing.List[GoogleCloudDialogflowV2IntentTrainingPhrase]

class GoogleCloudDialogflowV2beta1DocumentReloadStatus(
    typing_extensions.TypedDict, total=False
):
    status: GoogleRpcStatus
    time: str

class GoogleCloudDialogflowV2beta1SubAgent(typing_extensions.TypedDict, total=False):
    environment: str
    project: str

class GoogleCloudDialogflowV2IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction
    title: str

class GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    version: str
    source: str
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo(
    typing_extensions.TypedDict, total=False
):
    tag: str

class GoogleCloudDialogflowV2IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    alias: str
    userDefined: bool
    text: str

class GoogleCloudDialogflowV2beta1IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    title: str
    subtitle: str
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    formattedText: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage

class GoogleCloudDialogflowV2EntityType(typing_extensions.TypedDict, total=False):
    enableFuzzyExtraction: bool
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    name: str
    entities: typing.List[GoogleCloudDialogflowV2EntityTypeEntity]
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    displayName: str

class GoogleCloudDialogflowV2beta1BatchDeleteIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2beta1Intent]

class GoogleCloudDialogflowV2BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2Intent]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

class GoogleCloudDialogflowV3alpha1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowV2IntentParameter(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    defaultValue: str
    isList: bool
    value: str
    mandatory: bool
    entityTypeDisplayName: str
    prompts: typing.List[str]

class GoogleCloudDialogflowCxV3beta1ResponseMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]
    allowPlaybackInterruption: bool

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

class GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2beta1Intent]

class GoogleCloudDialogflowV2beta1InputAudioConfig(
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
    ]
    speechContexts: typing.List[GoogleCloudDialogflowV2beta1SpeechContext]
    phraseHints: typing.List[str]
    singleUtterance: bool
    model: str
    enableWordInfo: bool
    sampleRateHertz: int
    languageCode: str
    modelVariant: typing_extensions.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]

class GoogleCloudDialogflowV2WebhookRequest(typing_extensions.TypedDict, total=False):
    responseId: str
    queryResult: GoogleCloudDialogflowV2QueryResult
    session: str
    originalDetectIntentRequest: GoogleCloudDialogflowV2OriginalDetectIntentRequest

class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing_extensions.TypedDict, total=False
):
    title: str
    footer: str
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage

class GoogleCloudDialogflowV2IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]

class GoogleCloudDialogflowV3alpha1CreateVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

class GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    followupIntentName: str
    parentFollowupIntentName: str

class GoogleCloudDialogflowV2beta1BatchUpdateIntentsRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    intentView: typing_extensions.Literal["INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"]
    intentBatchInline: GoogleCloudDialogflowV2beta1IntentBatch
    languageCode: str
    intentBatchUri: str

class GoogleCloudDialogflowV2IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    text: str
    postback: str

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
    items: typing.List[
        GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItem
    ]

class GoogleCloudDialogflowV2OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    source: str
    version: str
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1QueryParameters(
    typing_extensions.TypedDict, total=False
):
    geoLocation: GoogleTypeLatLng
    resetContexts: bool
    subAgents: typing.List[GoogleCloudDialogflowV2beta1SubAgent]
    contexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    webhookHeaders: typing.Dict[str, typing.Any]
    payload: typing.Dict[str, typing.Any]
    sentimentAnalysisRequestConfig: GoogleCloudDialogflowV2beta1SentimentAnalysisRequestConfig
    timeZone: str
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2beta1SessionEntityType]
    knowledgeBaseNames: typing.List[str]

class GoogleCloudDialogflowV2IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    textToSpeech: str
    ssml: str
    displayText: str

class GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech(
    typing_extensions.TypedDict, total=False
):
    text: str
    ssml: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard(
    typing_extensions.TypedDict, total=False
):
    cardContents: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent]
    cardWidth: typing_extensions.Literal["CARD_WIDTH_UNSPECIFIED", "SMALL", "MEDIUM"]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowV2IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    parentFollowupIntentName: str
    followupIntentName: str

class GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    userDefined: bool
    entityType: str
    text: str
    alias: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

class GoogleCloudDialogflowV2beta1SearchAgentsResponse(
    typing_extensions.TypedDict, total=False
):
    agents: typing.List[GoogleCloudDialogflowV2beta1Agent]
    nextPageToken: str

class GoogleCloudDialogflowV3alpha1ExportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2beta1IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]
    mediaObjects: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject
    ]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion(
    typing_extensions.TypedDict, total=False
):
    action: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction
    reply: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply

class GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    key: str
    synonyms: typing.List[str]

class GoogleCloudDialogflowV2beta1DetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    queryInput: GoogleCloudDialogflowV2beta1QueryInput
    inputAudio: str
    outputAudioConfig: GoogleCloudDialogflowV2beta1OutputAudioConfig
    outputAudioConfigMask: str
    queryParams: GoogleCloudDialogflowV2beta1QueryParameters

class GoogleCloudDialogflowV2beta1IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    timesAddedCount: int
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]
    parts: typing.List[GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart]

class GoogleCloudDialogflowV2IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaObjects: typing.List[
        GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject
    ]
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]

class GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    icon: GoogleCloudDialogflowV2beta1IntentMessageImage
    description: str
    largeImage: GoogleCloudDialogflowV2beta1IntentMessageImage
    contentUrl: str
    name: str

class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    title: str
    description: str
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    image: GoogleCloudDialogflowV2beta1IntentMessageImage

class GoogleCloudDialogflowV2beta1IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    cells: typing.List[GoogleCloudDialogflowV2beta1IntentMessageTableCardCell]
    dividerAfter: bool

class GoogleCloudDialogflowCxV3beta1SessionInfo(
    typing_extensions.TypedDict, total=False
):
    parameters: typing.Dict[str, typing.Any]
    session: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[
        GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment
    ]

class GoogleCloudDialogflowV2beta1ListContextsResponse(
    typing_extensions.TypedDict, total=False
):
    contexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    nextPageToken: str

class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction
    title: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment(
    typing_extensions.TypedDict, total=False
):
    allowPlaybackInterruption: bool
    uri: str
    audio: str
