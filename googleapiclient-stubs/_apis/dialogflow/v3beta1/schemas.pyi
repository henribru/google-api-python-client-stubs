import typing

import typing_extensions

class GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig(
    typing_extensions.TypedDict, total=False
):
    pitch: float
    volumeGainDb: float
    voice: GoogleCloudDialogflowCxV3beta1VoiceSelectionParams
    effectsProfileId: typing.List[str]
    speakingRate: float

class GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard(
    typing_extensions.TypedDict, total=False
):
    cardWidth: typing_extensions.Literal["CARD_WIDTH_UNSPECIFIED", "SMALL", "MEDIUM"]
    cardContents: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent]

class GoogleCloudDialogflowCxV3beta1InputAudioConfig(
    typing_extensions.TypedDict, total=False
):
    singleUtterance: bool
    enableWordInfo: bool
    modelVariant: typing_extensions.Literal[
        "SPEECH_MODEL_VARIANT_UNSPECIFIED",
        "USE_BEST_AVAILABLE",
        "USE_STANDARD",
        "USE_ENHANCED",
    ]
    model: str
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
    sampleRateHertz: int
    phraseHints: typing.List[str]

class GoogleCloudDialogflowV2IntentParameter(typing_extensions.TypedDict, total=False):
    isList: bool
    entityTypeDisplayName: str
    mandatory: bool
    name: str
    defaultValue: str
    value: str
    prompts: typing.List[str]
    displayName: str

class GoogleCloudDialogflowV2AnnotatedMessagePart(
    typing_extensions.TypedDict, total=False
):
    text: str
    formattedValue: typing.Any
    entityType: str

class GoogleCloudDialogflowCxV3beta1CreateVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

class GoogleCloudDialogflowCxV3beta1ListWebhooksResponse(
    typing_extensions.TypedDict, total=False
):
    webhooks: typing.List[GoogleCloudDialogflowCxV3beta1Webhook]
    nextPageToken: str

class GoogleCloudDialogflowV2IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    text: str
    entityType: str
    alias: str
    userDefined: bool

class GoogleCloudDialogflowCxV3beta1SessionInfo(
    typing_extensions.TypedDict, total=False
):
    parameters: typing.Dict[str, typing.Any]
    session: str

class GoogleCloudDialogflowV2beta1EntityTypeEntity(
    typing_extensions.TypedDict, total=False
):
    synonyms: typing.List[str]
    value: str

class GoogleCloudDialogflowV2IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]

class GoogleCloudDialogflowV3alpha1ExportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowCxV3beta1Page(typing_extensions.TypedDict, total=False):
    name: str
    form: GoogleCloudDialogflowCxV3beta1Form
    transitionRouteGroups: typing.List[str]
    displayName: str
    eventHandlers: typing.List[GoogleCloudDialogflowCxV3beta1EventHandler]
    transitionRoutes: typing.List[GoogleCloudDialogflowCxV3beta1TransitionRoute]
    entryFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment

class GoogleCloudDialogflowV2beta1SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2beta1Sentiment

class GoogleCloudDialogflowCxV3beta1Form(typing.Dict[str, typing.Any]): ...

class GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    environments: typing.List[GoogleCloudDialogflowCxV3beta1Environment]

class GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    uri: str
    destinationName: str

class GoogleCloudDialogflowV2BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2EntityType]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply(
    typing_extensions.TypedDict, total=False
):
    text: str
    postbackData: str

class GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion(
    typing_extensions.TypedDict, total=False
):
    destinationName: str
    uri: str

class GoogleCloudDialogflowV2ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowCxV3beta1EventHandler(typing.Dict[str, typing.Any]): ...

class GoogleCloudDialogflowV2beta1IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

class GoogleCloudDialogflowCxV3beta1ResponseMessage(
    typing_extensions.TypedDict, total=False
):
    playAudio: GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio
    endInteraction: GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction
    text: GoogleCloudDialogflowCxV3beta1ResponseMessageText
    liveAgentHandoff: GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff
    mixedAudio: GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio
    conversationSuccess: GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess
    outputAudioText: GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowCxV3beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    messages: typing.List[GoogleCloudDialogflowCxV3beta1ResponseMessage]
    fulfillmentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo
    detectIntentResponseId: str
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo
    payload: typing.Dict[str, typing.Any]
    intentInfo: GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo

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

class GoogleCloudDialogflowV3alpha1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

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

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowV3alpha1ExportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    content: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmText(
    typing_extensions.TypedDict, total=False
):
    text: str
    rbmSuggestion: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]

class GoogleCloudDialogflowV2beta1EntityType(typing_extensions.TypedDict, total=False):
    enableFuzzyExtraction: bool
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    displayName: str
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    name: str

class GoogleCloudDialogflowV2IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    accessibilityText: str
    imageUri: str

class GoogleCloudDialogflowCxV3beta1VoiceSelectionParams(
    typing_extensions.TypedDict, total=False
):
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED",
        "SSML_VOICE_GENDER_MALE",
        "SSML_VOICE_GENDER_FEMALE",
        "SSML_VOICE_GENDER_NEUTRAL",
    ]
    name: str

class GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    payload: typing.Dict[str, typing.Any]
    version: str
    source: str

class GoogleCloudDialogflowCxV3beta1QueryInput(
    typing_extensions.TypedDict, total=False
):
    audio: GoogleCloudDialogflowCxV3beta1AudioInput
    event: GoogleCloudDialogflowCxV3beta1EventInput
    intent: GoogleCloudDialogflowCxV3beta1IntentInput
    text: GoogleCloudDialogflowCxV3beta1TextInput
    languageCode: str

class GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    sessionEntityTypes: typing.List[GoogleCloudDialogflowCxV3beta1SessionEntityType]
    nextPageToken: str

class GoogleCloudDialogflowV2WebhookRequest(typing_extensions.TypedDict, total=False):
    queryResult: GoogleCloudDialogflowV2QueryResult
    responseId: str
    session: str
    originalDetectIntentRequest: GoogleCloudDialogflowV2OriginalDetectIntentRequest

class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    footer: str
    title: str
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction

class GoogleCloudDialogflowCxV3beta1ListAgentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    agents: typing.List[GoogleCloudDialogflowCxV3beta1Agent]

class GoogleCloudDialogflowV2beta1IntentMessageImage(
    typing_extensions.TypedDict, total=False
):
    imageUri: str
    accessibilityText: str

class GoogleCloudDialogflowV3alpha1ImportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageOutputAudioText(
    typing_extensions.TypedDict, total=False
):
    ssml: str
    allowPlaybackInterruption: bool
    text: str

class GoogleCloudDialogflowCxV3beta1IntentInput(
    typing_extensions.TypedDict, total=False
):
    intent: str

class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCases(
    typing_extensions.TypedDict, total=False
):
    cases: typing.List[GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCase]

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudDialogflowV2IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    quickReplies: typing.List[str]
    title: str

class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    displayText: str
    textToSpeech: str
    ssml: str

class GoogleCloudDialogflowV2IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    title: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo

class GoogleCloudDialogflowCxV3beta1ImportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agent: str

class GoogleCloudDialogflowCxV3beta1EventInput(
    typing_extensions.TypedDict, total=False
):
    event: str

class GoogleCloudDialogflowV3alpha1ImportTestCasesResponse(
    typing_extensions.TypedDict, total=False
):
    names: typing.List[str]

class GoogleCloudDialogflowCxV3beta1EntityType(
    typing_extensions.TypedDict, total=False
):
    entities: typing.List[GoogleCloudDialogflowCxV3beta1EntityTypeEntity]
    excludedPhrases: typing.List[GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase]
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED", "KIND_MAP", "KIND_LIST", "KIND_REGEXP"
    ]
    enableFuzzyExtraction: bool
    displayName: str
    name: str
    autoExpansionMode: typing_extensions.Literal[
        "AUTO_EXPANSION_MODE_UNSPECIFIED", "AUTO_EXPANSION_MODE_DEFAULT"
    ]

class GoogleCloudDialogflowCxV3beta1Fulfillment(typing.Dict[str, typing.Any]): ...

class GoogleCloudDialogflowCxV3beta1Match(typing_extensions.TypedDict, total=False):
    resolvedInput: str
    parameters: typing.Dict[str, typing.Any]
    intent: GoogleCloudDialogflowCxV3beta1Intent
    confidence: float
    matchType: typing_extensions.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "INTENT",
        "DIRECT_INTENT",
        "PARAMETER_FILLING",
        "NO_MATCH",
        "NO_INPUT",
    ]

class GoogleCloudDialogflowCxV3beta1ListFlowsResponse(
    typing_extensions.TypedDict, total=False
):
    flows: typing.List[GoogleCloudDialogflowCxV3beta1Flow]
    nextPageToken: str

class GoogleCloudDialogflowV2beta1LabelConversationResponse(
    typing_extensions.TypedDict, total=False
):
    annotatedConversationDataset: GoogleCloudDialogflowV2beta1AnnotatedConversationDataset

class GoogleCloudDialogflowCxV3beta1DetectIntentResponse(
    typing_extensions.TypedDict, total=False
):
    responseId: str
    outputAudio: str
    queryResult: GoogleCloudDialogflowCxV3beta1QueryResult
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig

class GoogleCloudDialogflowV2QueryResult(typing_extensions.TypedDict, total=False):
    intent: GoogleCloudDialogflowV2Intent
    webhookSource: str
    allRequiredParamsPresent: bool
    diagnosticInfo: typing.Dict[str, typing.Any]
    languageCode: str
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    queryText: str
    sentimentAnalysisResult: GoogleCloudDialogflowV2SentimentAnalysisResult
    action: str
    speechRecognitionConfidence: float
    fulfillmentText: str
    webhookPayload: typing.Dict[str, typing.Any]
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    intentDetectionConfidence: float
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCaseCaseContent(
    typing_extensions.TypedDict, total=False
):
    additionalCases: GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCases
    message: GoogleCloudDialogflowCxV3beta1ResponseMessage

class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia(
    typing_extensions.TypedDict, total=False
):
    fileUri: str
    thumbnailUri: str
    height: typing_extensions.Literal["HEIGHT_UNSPECIFIED", "SHORT", "MEDIUM", "TALL"]

class GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech(
    typing_extensions.TypedDict, total=False
):
    ssml: str
    text: str

class GoogleCloudDialogflowV2beta1BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2beta1Intent]

class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]
    url: str

class GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    followupIntentName: str
    parentFollowupIntentName: str

class GoogleCloudDialogflowCxV3beta1MatchIntentResponse(
    typing_extensions.TypedDict, total=False
):
    matches: typing.List[GoogleCloudDialogflowCxV3beta1Match]
    currentPage: GoogleCloudDialogflowCxV3beta1Page
    text: str
    transcript: str
    triggerIntent: str

class GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: typing.List[GoogleCloudDialogflowV2beta1EntityType]

class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleCloudDialogflowCxV3beta1FulfillIntentRequest(
    typing_extensions.TypedDict, total=False
):
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    matchIntentRequest: GoogleCloudDialogflowCxV3beta1MatchIntentRequest
    match: GoogleCloudDialogflowCxV3beta1Match

class GoogleCloudDialogflowV2beta1EventInput(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    languageCode: str
    name: str

class GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItem(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction
    footer: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    description: str
    title: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion(
    typing_extensions.TypedDict, total=False
):
    action: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction
    reply: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedReply

class GoogleCloudDialogflowCxV3beta1LoadVersionRequest(
    typing_extensions.TypedDict, total=False
):
    allowOverrideAgentResources: bool

class GoogleCloudDialogflowV2IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    text: str
    postback: str

class GoogleCloudDialogflowV2Message(typing_extensions.TypedDict, total=False):
    messageAnnotation: GoogleCloudDialogflowV2MessageAnnotation
    participantRole: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "HUMAN_AGENT", "AUTOMATED_AGENT", "END_USER"
    ]
    participant: str
    content: str
    name: str
    languageCode: str
    createTime: str

class GoogleCloudDialogflowCxV3beta1PageInfoFormInfo(
    typing_extensions.TypedDict, total=False
):
    parameterInfo: typing.List[
        GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo
    ]

class GoogleCloudDialogflowV2IntentMessage(typing_extensions.TypedDict, total=False):
    payload: typing.Dict[str, typing.Any]
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
    carouselSelect: GoogleCloudDialogflowV2IntentMessageCarouselSelect
    tableCard: GoogleCloudDialogflowV2IntentMessageTableCard
    quickReplies: GoogleCloudDialogflowV2IntentMessageQuickReplies
    card: GoogleCloudDialogflowV2IntentMessageCard
    text: GoogleCloudDialogflowV2IntentMessageText
    image: GoogleCloudDialogflowV2IntentMessageImage
    listSelect: GoogleCloudDialogflowV2IntentMessageListSelect
    simpleResponses: GoogleCloudDialogflowV2IntentMessageSimpleResponses
    linkOutSuggestion: GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion
    browseCarouselCard: GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard
    basicCard: GoogleCloudDialogflowV2IntentMessageBasicCard
    suggestions: GoogleCloudDialogflowV2IntentMessageSuggestions
    mediaContent: GoogleCloudDialogflowV2IntentMessageMediaContent

class GoogleCloudDialogflowV2ConversationEvent(
    typing_extensions.TypedDict, total=False
):
    conversation: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CONVERSATION_STARTED",
        "CONVERSATION_FINISHED",
        "HUMAN_INTERVENTION_NEEDED",
        "NEW_MESSAGE",
        "UNRECOVERABLE_ERROR",
    ]
    newMessagePayload: GoogleCloudDialogflowV2Message
    errorStatus: GoogleRpcStatus

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
    ]
    synthesizeSpeechConfig: GoogleCloudDialogflowCxV3beta1SynthesizeSpeechConfig
    sampleRateHertz: int

class GoogleCloudDialogflowV2IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    imageUri: str
    subtitle: str
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageCardButton]
    title: str

class GoogleCloudDialogflowV2beta1IntentMessageCardButton(
    typing_extensions.TypedDict, total=False
):
    text: str
    postback: str

class GoogleCloudDialogflowV2beta1IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    name: str
    parts: typing.List[GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]
    timesAddedCount: int

class GoogleCloudDialogflowV2EntityTypeEntity(typing_extensions.TypedDict, total=False):
    value: str
    synonyms: typing.List[str]

class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment(
    typing_extensions.TypedDict, total=False
):
    audio: str
    allowPlaybackInterruption: bool
    uri: str

class GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    text: str
    parameterId: str

class GoogleCloudDialogflowCxV3beta1Webhook(typing_extensions.TypedDict, total=False):
    timeout: str
    disabled: bool
    genericWebService: GoogleCloudDialogflowCxV3beta1WebhookGenericWebService
    displayName: str
    name: str

class GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    transitionRouteGroups: typing.List[
        GoogleCloudDialogflowCxV3beta1TransitionRouteGroup
    ]
    nextPageToken: str

class GoogleCloudDialogflowV2IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

class GoogleCloudDialogflowV2beta1IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2beta1IntentMessageListSelectItem]
    title: str
    subtitle: str

class GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer(
    typing_extensions.TypedDict, total=False
):
    faqQuestion: str
    answer: str
    source: str
    matchConfidenceLevel: typing_extensions.Literal[
        "MATCH_CONFIDENCE_LEVEL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    matchConfidence: float

class GoogleCloudDialogflowV2IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: typing.List[GoogleCloudDialogflowV2IntentMessageSimpleResponse]

class GoogleCloudDialogflowCxV3beta1EntityTypeEntity(
    typing_extensions.TypedDict, total=False
):
    synonyms: typing.List[str]
    value: str

class GoogleCloudDialogflowV2Sentiment(typing_extensions.TypedDict, total=False):
    score: float
    magnitude: float

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class GoogleCloudDialogflowCxV3beta1QueryParameters(
    typing_extensions.TypedDict, total=False
):
    sessionEntityTypes: typing.List[GoogleCloudDialogflowCxV3beta1SessionEntityType]
    geoLocation: GoogleTypeLatLng
    parameters: typing.Dict[str, typing.Any]
    analyzeQueryTextSentiment: bool
    timeZone: str
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction
    title: str

class GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    id: str
    parts: typing.List[GoogleCloudDialogflowCxV3beta1IntentTrainingPhrasePart]
    repeatCount: int

class GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses(
    typing_extensions.TypedDict, total=False
):
    simpleResponses: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageSimpleResponse
    ]

class GoogleCloudDialogflowV2beta1KnowledgeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "RUNNING", "DONE"]

class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfoIntentParameterValue(
    typing_extensions.TypedDict, total=False
):
    originalValue: str
    resolvedValue: typing.Any

class GoogleCloudDialogflowCxV3beta1Environment(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    versionConfigs: typing.List[GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfig]
    updateTime: str
    name: str
    description: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction(
    typing_extensions.TypedDict, total=False
):
    text: str
    openUrl: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri
    dial: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial
    postbackData: str
    shareLocation: GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation

class GoogleCloudDialogflowCxV3beta1FulfillIntentResponse(
    typing_extensions.TypedDict, total=False
):
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    outputAudio: str
    responseId: str
    queryResult: GoogleCloudDialogflowCxV3beta1QueryResult

class GoogleCloudDialogflowV2IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: typing.List[GoogleCloudDialogflowV2IntentMessageSuggestion]

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

class GoogleCloudDialogflowV2beta1IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    rows: typing.List[GoogleCloudDialogflowV2beta1IntentMessageTableCardRow]
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    subtitle: str
    columnProperties: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageColumnProperties
    ]
    title: str
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]

class GoogleCloudDialogflowV2Intent(typing_extensions.TypedDict, total=False):
    resetContexts: bool
    displayName: str
    inputContextNames: typing.List[str]
    mlDisabled: bool
    parameters: typing.List[GoogleCloudDialogflowV2IntentParameter]
    parentFollowupIntentName: str
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]
    name: str
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    isFallback: bool
    messages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    events: typing.List[str]
    rootFollowupIntentName: str
    priority: int
    trainingPhrases: typing.List[GoogleCloudDialogflowV2IntentTrainingPhrase]
    defaultResponsePlatforms: typing.List[str]
    followupIntentInfo: typing.List[GoogleCloudDialogflowV2IntentFollowupIntentInfo]
    action: str

class GoogleCloudDialogflowV2IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    title: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    info: GoogleCloudDialogflowV2IntentMessageSelectItemInfo

class GoogleCloudDialogflowV2beta1Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

class GoogleCloudDialogflowCxV3beta1WebhookGenericWebService(
    typing_extensions.TypedDict, total=False
):
    uri: str
    username: str
    password: str
    requestHeaders: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowCxV3beta1SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    score: float
    magnitude: float

class GoogleCloudDialogflowV2IntentMessageTableCardCell(
    typing_extensions.TypedDict, total=False
):
    text: str

class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem]

class GoogleCloudDialogflowV2EventInput(typing_extensions.TypedDict, total=False):
    name: str
    languageCode: str
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    dividerAfter: bool
    cells: typing.List[GoogleCloudDialogflowV2IntentMessageTableCardCell]

class GoogleCloudDialogflowCxV3beta1MatchIntentRequest(
    typing_extensions.TypedDict, total=False
):
    queryInput: GoogleCloudDialogflowCxV3beta1QueryInput
    queryParams: GoogleCloudDialogflowCxV3beta1QueryParameters

class GoogleCloudDialogflowV2beta1WebhookRequest(
    typing_extensions.TypedDict, total=False
):
    queryResult: GoogleCloudDialogflowV2beta1QueryResult
    session: str
    responseId: str
    originalDetectIntentRequest: GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest
    alternativeQueryResults: typing.List[GoogleCloudDialogflowV2beta1QueryResult]

class GoogleCloudDialogflowV2beta1IntentMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]

class GoogleCloudDialogflowV2IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowV2IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaObjects: typing.List[
        GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject
    ]
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]

class GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard(
    typing_extensions.TypedDict, total=False
):
    cardOrientation: typing_extensions.Literal[
        "CARD_ORIENTATION_UNSPECIFIED", "HORIZONTAL", "VERTICAL"
    ]
    thumbnailImageAlignment: typing_extensions.Literal[
        "THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT"
    ]
    cardContent: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent

class GoogleCloudDialogflowV2IntentMessageSimpleResponse(
    typing_extensions.TypedDict, total=False
):
    displayText: str
    ssml: str
    textToSpeech: str

class GoogleCloudDialogflowV2IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    title: str
    image: GoogleCloudDialogflowV2IntentMessageImage
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageBasicCardButton]
    formattedText: str
    subtitle: str

class GoogleCloudDialogflowV2beta1IntentMessageSuggestion(
    typing_extensions.TypedDict, total=False
):
    title: str

class GoogleCloudDialogflowCxV3beta1NluSettings(
    typing_extensions.TypedDict, total=False
):
    modelTrainingMode: typing_extensions.Literal[
        "MODEL_TRAINING_MODE_UNSPECIFIED",
        "MODEL_TRAINING_MODE_AUTOMATIC",
        "MODEL_TRAINING_MODE_MANUAL",
    ]
    classificationThreshold: float
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED", "MODEL_TYPE_STANDARD", "MODEL_TYPE_ADVANCED"
    ]

class GoogleCloudDialogflowV2beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    source: str
    fulfillmentText: str
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    followupEventInput: GoogleCloudDialogflowV2beta1EventInput
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2beta1SessionEntityType]
    payload: typing.Dict[str, typing.Any]
    endInteraction: bool

class GoogleCloudDialogflowCxV3beta1PageInfo(typing_extensions.TypedDict, total=False):
    formInfo: GoogleCloudDialogflowCxV3beta1PageInfoFormInfo
    currentPage: str

class GoogleCloudDialogflowCxV3beta1WebhookRequestIntentInfo(
    typing_extensions.TypedDict, total=False
):
    lastMatchedIntent: str
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    largeImage: GoogleCloudDialogflowV2IntentMessageImage
    contentUrl: str
    icon: GoogleCloudDialogflowV2IntentMessageImage
    name: str
    description: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent(
    typing_extensions.TypedDict, total=False
):
    media: GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia
    title: str
    description: str
    suggestions: typing.List[GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestion]

class GoogleCloudDialogflowCxV3beta1TrainFlowRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowV2beta1IntentMessageSuggestions(
    typing_extensions.TypedDict, total=False
):
    suggestions: typing.List[GoogleCloudDialogflowV2beta1IntentMessageSuggestion]

class GoogleCloudDialogflowV2SentimentAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    queryTextSentiment: GoogleCloudDialogflowV2Sentiment

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    name: str
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1AutoApproveSmartMessagingEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    unreviewedCount: int
    enabledCount: int
    disabledCount: int

class GoogleCloudDialogflowCxV3beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

class GoogleCloudDialogflowCxV3beta1ResponseMessagePlayAudio(
    typing_extensions.TypedDict, total=False
):
    audioUri: str
    allowPlaybackInterruption: bool

class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction(
    typing_extensions.TypedDict, total=False
):
    uri: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageText(
    typing_extensions.TypedDict, total=False
):
    text: typing.List[str]
    allowPlaybackInterruption: bool

class GoogleCloudDialogflowV2beta1IntentMessage(
    typing_extensions.TypedDict, total=False
):
    text: GoogleCloudDialogflowV2beta1IntentMessageText
    listSelect: GoogleCloudDialogflowV2beta1IntentMessageListSelect
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    telephonySynthesizeSpeech: GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech
    rbmStandaloneRichCard: GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard
    quickReplies: GoogleCloudDialogflowV2beta1IntentMessageQuickReplies
    card: GoogleCloudDialogflowV2beta1IntentMessageCard
    suggestions: GoogleCloudDialogflowV2beta1IntentMessageSuggestions
    rbmCarouselRichCard: GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard
    simpleResponses: GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses
    basicCard: GoogleCloudDialogflowV2beta1IntentMessageBasicCard
    browseCarouselCard: GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard
    carouselSelect: GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect
    telephonyPlayAudio: GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio
    payload: typing.Dict[str, typing.Any]
    telephonyTransferCall: GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall
    rbmText: GoogleCloudDialogflowV2beta1IntentMessageRbmText
    mediaContent: GoogleCloudDialogflowV2beta1IntentMessageMediaContent
    linkOutSuggestion: GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion
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
    tableCard: GoogleCloudDialogflowV2beta1IntentMessageTableCard

class GoogleCloudDialogflowV2Context(typing_extensions.TypedDict, total=False):
    name: str
    lifespanCount: int
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall(
    typing_extensions.TypedDict, total=False
):
    phoneNumber: str

class GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environments: typing.List[GoogleCloudDialogflowCxV3beta1Environment]
    nextPageToken: str

class GoogleCloudDialogflowV2beta1IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    header: str
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]

class GoogleCloudDialogflowV2beta1IntentMessageCarouselSelectItem(
    typing_extensions.TypedDict, total=False
):
    title: str
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    description: str
    image: GoogleCloudDialogflowV2beta1IntentMessageImage

class GoogleCloudDialogflowV2WebhookResponse(typing_extensions.TypedDict, total=False):
    fulfillmentText: str
    sessionEntityTypes: typing.List[GoogleCloudDialogflowV2SessionEntityType]
    outputContexts: typing.List[GoogleCloudDialogflowV2Context]
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2IntentMessage]
    followupEventInput: GoogleCloudDialogflowV2EventInput
    source: str
    payload: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2beta1SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entities: typing.List[GoogleCloudDialogflowV2beta1EntityTypeEntity]
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

class GoogleCloudDialogflowV2beta1QueryResult(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    diagnosticInfo: typing.Dict[str, typing.Any]
    action: str
    webhookSource: str
    fulfillmentMessages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    webhookPayload: typing.Dict[str, typing.Any]
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    intentDetectionConfidence: float
    queryText: str
    sentimentAnalysisResult: GoogleCloudDialogflowV2beta1SentimentAnalysisResult
    allRequiredParamsPresent: bool
    speechRecognitionConfidence: float
    fulfillmentText: str
    intent: GoogleCloudDialogflowV2beta1Intent
    languageCode: str
    knowledgeAnswers: GoogleCloudDialogflowV2beta1KnowledgeAnswers

class GoogleCloudDialogflowV2IntentTrainingPhrase(
    typing_extensions.TypedDict, total=False
):
    name: str
    parts: typing.List[GoogleCloudDialogflowV2IntentTrainingPhrasePart]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXAMPLE", "TEMPLATE"]
    timesAddedCount: int

class GoogleCloudDialogflowV2beta1AnnotatedConversationDataset(
    typing_extensions.TypedDict, total=False
):
    exampleCount: str
    displayName: str
    completedExampleCount: str
    createTime: str
    questionTypeName: str
    name: str
    description: str

class GoogleCloudDialogflowCxV3beta1ExportAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentUri: str

class GoogleCloudDialogflowCxV3beta1AudioInput(
    typing_extensions.TypedDict, total=False
):
    audio: str
    config: GoogleCloudDialogflowCxV3beta1InputAudioConfig

class GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart(
    typing_extensions.TypedDict, total=False
):
    text: str
    alias: str
    entityType: str
    userDefined: bool

class GoogleCloudDialogflowCxV3beta1WebhookRequestFulfillmentInfo(
    typing_extensions.TypedDict, total=False
):
    tag: str

class GoogleCloudDialogflowCxV3beta1ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    entityTypes: typing.List[GoogleCloudDialogflowCxV3beta1EntityType]

class GoogleCloudDialogflowV2IntentMessageTableCard(
    typing_extensions.TypedDict, total=False
):
    image: GoogleCloudDialogflowV2IntentMessageImage
    buttons: typing.List[GoogleCloudDialogflowV2IntentMessageBasicCardButton]
    rows: typing.List[GoogleCloudDialogflowV2IntentMessageTableCardRow]
    subtitle: str
    title: str
    columnProperties: typing.List[GoogleCloudDialogflowV2IntentMessageColumnProperties]

class GoogleCloudDialogflowV2beta1IntentMessageQuickReplies(
    typing_extensions.TypedDict, total=False
):
    quickReplies: typing.List[str]
    title: str

class GoogleCloudDialogflowV2IntentMessageCarouselSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2IntentMessageCarouselSelectItem]

class GoogleCloudDialogflowCxV3beta1TransitionRouteGroup(
    typing.Dict[str, typing.Any]
): ...

class GoogleCloudDialogflowCxV3beta1Intent(typing_extensions.TypedDict, total=False):
    isFallback: bool
    parameters: typing.List[GoogleCloudDialogflowCxV3beta1IntentParameter]
    priority: int
    name: str
    trainingPhrases: typing.List[GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase]
    displayName: str

class GoogleCloudDialogflowCxV3beta1ListPagesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pages: typing.List[GoogleCloudDialogflowCxV3beta1Page]

class GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse(
    typing_extensions.TypedDict, total=False
):
    mergeBehavior: typing_extensions.Literal[
        "MERGE_BEHAVIOR_UNSPECIFIED", "APPEND", "REPLACE"
    ]
    messages: typing.List[GoogleCloudDialogflowCxV3beta1ResponseMessage]

class GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject(
    typing_extensions.TypedDict, total=False
):
    contentUrl: str
    name: str
    icon: GoogleCloudDialogflowV2beta1IntentMessageImage
    largeImage: GoogleCloudDialogflowV2beta1IntentMessageImage
    description: str

class GoogleCloudDialogflowV3alpha1ImportTestCasesMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowCxV3beta1SpeechToTextSettings(
    typing_extensions.TypedDict, total=False
):
    enableSpeechAdaptation: bool

class GoogleCloudDialogflowCxV3beta1ListVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    versions: typing.List[GoogleCloudDialogflowCxV3beta1Version]

class GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudio(
    typing_extensions.TypedDict, total=False
):
    segments: typing.List[
        GoogleCloudDialogflowCxV3beta1ResponseMessageMixedAudioSegment
    ]

class GoogleCloudDialogflowCxV3beta1FulfillmentSetParameterAction(
    typing_extensions.TypedDict, total=False
):
    value: typing.Any
    parameter: str

class GoogleCloudDialogflowCxV3beta1PageInfoFormInfoParameterInfo(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    state: typing_extensions.Literal[
        "PARAMETER_STATE_UNSPECIFIED", "EMPTY", "INVALID", "FILLED"
    ]
    justCollected: bool
    value: typing.Any
    required: bool

class GoogleCloudDialogflowCxV3beta1FormParameterFillBehavior(
    typing_extensions.TypedDict, total=False
):
    initialPromptFulfillment: GoogleCloudDialogflowCxV3beta1Fulfillment
    repromptEventHandlers: typing.List[GoogleCloudDialogflowCxV3beta1EventHandler]

class GoogleCloudDialogflowCxV3beta1Version(typing_extensions.TypedDict, total=False):
    name: str
    nluSettings: GoogleCloudDialogflowCxV3beta1NluSettings
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"
    ]
    displayName: str
    description: str

class GoogleCloudDialogflowCxV3beta1WebhookResponse(
    typing_extensions.TypedDict, total=False
):
    pageInfo: GoogleCloudDialogflowCxV3beta1PageInfo
    sessionInfo: GoogleCloudDialogflowCxV3beta1SessionInfo
    targetFlow: str
    targetPage: str
    payload: typing.Dict[str, typing.Any]
    fulfillmentResponse: GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse

class GoogleCloudDialogflowV2beta1IntentMessageTableCardRow(
    typing_extensions.TypedDict, total=False
):
    dividerAfter: bool
    cells: typing.List[GoogleCloudDialogflowV2beta1IntentMessageTableCardCell]

class GoogleCloudDialogflowV2SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    name: str
    entities: typing.List[GoogleCloudDialogflowV2EntityTypeEntity]
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]

class GoogleCloudDialogflowCxV3beta1TextInput(typing_extensions.TypedDict, total=False):
    text: str

class GoogleCloudDialogflowCxV3beta1IntentParameter(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    redact: bool
    id: str
    isList: bool

class GoogleCloudDialogflowV2beta1IntentMessageBasicCard(
    typing_extensions.TypedDict, total=False
):
    title: str
    formattedText: str
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton]
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    subtitle: str

class GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase(
    typing_extensions.TypedDict, total=False
):
    value: str

class GoogleCloudDialogflowV2beta1IntentMessageCard(
    typing_extensions.TypedDict, total=False
):
    title: str
    subtitle: str
    imageUri: str
    buttons: typing.List[GoogleCloudDialogflowV2beta1IntentMessageCardButton]

class GoogleCloudDialogflowCxV3beta1EnvironmentVersionConfig(
    typing_extensions.TypedDict, total=False
):
    version: str

class GoogleCloudDialogflowCxV3beta1ResponseMessageLiveAgentHandoff(
    typing_extensions.TypedDict, total=False
):
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentMessageListSelect(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[GoogleCloudDialogflowV2IntentMessageListSelectItem]
    title: str
    subtitle: str

class GoogleCloudDialogflowV2beta1IntentMessageBasicCardButton(
    typing_extensions.TypedDict, total=False
):
    openUriAction: GoogleCloudDialogflowV2beta1IntentMessageBasicCardButtonOpenUriAction
    title: str

class GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionShareLocation(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudDialogflowCxV3beta1DetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    outputAudioConfig: GoogleCloudDialogflowCxV3beta1OutputAudioConfig
    queryParams: GoogleCloudDialogflowCxV3beta1QueryParameters
    queryInput: GoogleCloudDialogflowCxV3beta1QueryInput

class GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    key: str
    synonyms: typing.List[str]

class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItemOpenUrlAction(
    typing_extensions.TypedDict, total=False
):
    url: str
    urlTypeHint: typing_extensions.Literal[
        "URL_TYPE_HINT_UNSPECIFIED", "AMP_ACTION", "AMP_CONTENT"
    ]

class GoogleCloudDialogflowV2OriginalDetectIntentRequest(
    typing_extensions.TypedDict, total=False
):
    source: str
    payload: typing.Dict[str, typing.Any]
    version: str

class GoogleCloudDialogflowV2beta1Intent(typing_extensions.TypedDict, total=False):
    inputContextNames: typing.List[str]
    mlDisabled: bool
    events: typing.List[str]
    resetContexts: bool
    action: str
    outputContexts: typing.List[GoogleCloudDialogflowV2beta1Context]
    displayName: str
    messages: typing.List[GoogleCloudDialogflowV2beta1IntentMessage]
    parentFollowupIntentName: str
    mlEnabled: bool
    defaultResponsePlatforms: typing.List[str]
    priority: int
    endInteraction: bool
    webhookState: typing_extensions.Literal[
        "WEBHOOK_STATE_UNSPECIFIED",
        "WEBHOOK_STATE_ENABLED",
        "WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING",
    ]
    name: str
    isFallback: bool
    rootFollowupIntentName: str
    parameters: typing.List[GoogleCloudDialogflowV2beta1IntentParameter]
    trainingPhrases: typing.List[GoogleCloudDialogflowV2beta1IntentTrainingPhrase]
    followupIntentInfo: typing.List[
        GoogleCloudDialogflowV2beta1IntentFollowupIntentInfo
    ]

class GoogleCloudDialogflowCxV3beta1ResponseMessageEndInteraction(
    typing_extensions.TypedDict, total=False
): ...
class GoogleCloudDialogflowCxV3beta1FulfillmentConditionalCasesCase(
    typing.Dict[str, typing.Any]
): ...
class GoogleCloudDialogflowCxV3beta1Flow(typing.Dict[str, typing.Any]): ...

class GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem
    ]
    imageDisplayOptions: typing_extensions.Literal[
        "IMAGE_DISPLAY_OPTIONS_UNSPECIFIED",
        "GRAY",
        "WHITE",
        "CROPPED",
        "BLURRED_BACKGROUND",
    ]

class GoogleCloudDialogflowV2beta1IntentParameter(
    typing_extensions.TypedDict, total=False
):
    prompts: typing.List[str]
    name: str
    entityTypeDisplayName: str
    isList: bool
    defaultValue: str
    mandatory: bool
    value: str
    displayName: str

class GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio(
    typing_extensions.TypedDict, total=False
):
    audioUri: str

class GoogleCloudDialogflowCxV3beta1QueryResult(typing.Dict[str, typing.Any]): ...

class GoogleCloudDialogflowCxV3beta1Agent(typing_extensions.TypedDict, total=False):
    displayName: str
    timeZone: str
    speechToTextSettings: GoogleCloudDialogflowCxV3beta1SpeechToTextSettings
    description: str
    defaultLanguageCode: str
    enableSpellCorrection: bool
    startFlow: str
    name: str
    avatarUri: str
    enableStackdriverLogging: bool

class GoogleCloudDialogflowV2IntentMessageColumnProperties(
    typing_extensions.TypedDict, total=False
):
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "LEADING", "CENTER", "TRAILING"
    ]
    header: str

class GoogleCloudDialogflowV2BatchUpdateIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    intents: typing.List[GoogleCloudDialogflowV2Intent]

class GoogleCloudDialogflowCxV3beta1ResponseMessageConversationSuccess(
    typing_extensions.TypedDict, total=False
):
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowCxV3beta1RestoreAgentRequest(
    typing_extensions.TypedDict, total=False
):
    agentContent: str
    agentUri: str

class GoogleCloudDialogflowCxV3beta1TransitionRoute(typing.Dict[str, typing.Any]): ...

class GoogleCloudDialogflowV2beta1IntentMessageMediaContent(
    typing_extensions.TypedDict, total=False
):
    mediaType: typing_extensions.Literal["RESPONSE_MEDIA_TYPE_UNSPECIFIED", "AUDIO"]
    mediaObjects: typing.List[
        GoogleCloudDialogflowV2beta1IntentMessageMediaContentResponseMediaObject
    ]

class GoogleCloudDialogflowCxV3beta1ListIntentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    intents: typing.List[GoogleCloudDialogflowCxV3beta1Intent]

class GoogleCloudDialogflowV2beta1IntentMessageListSelectItem(
    typing_extensions.TypedDict, total=False
):
    title: str
    info: GoogleCloudDialogflowV2beta1IntentMessageSelectItemInfo
    image: GoogleCloudDialogflowV2beta1IntentMessageImage
    description: str

class GoogleCloudDialogflowV2beta1ExportAgentResponse(
    typing_extensions.TypedDict, total=False
):
    agentUri: str
    agentContent: str

class GoogleCloudDialogflowV2beta1KnowledgeAnswers(
    typing_extensions.TypedDict, total=False
):
    answers: typing.List[GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer]

class GoogleCloudDialogflowV2MessageAnnotation(
    typing_extensions.TypedDict, total=False
):
    parts: typing.List[GoogleCloudDialogflowV2AnnotatedMessagePart]
    containEntities: bool

class GoogleCloudDialogflowV2beta1Context(typing_extensions.TypedDict, total=False):
    lifespanCount: int
    name: str
    parameters: typing.Dict[str, typing.Any]

class GoogleCloudDialogflowV2IntentFollowupIntentInfo(
    typing_extensions.TypedDict, total=False
):
    parentFollowupIntentName: str
    followupIntentName: str

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[GoogleLongrunningOperation]
    nextPageToken: str

class GoogleCloudDialogflowCxV3beta1FormParameter(typing.Dict[str, typing.Any]): ...

class GoogleCloudDialogflowV2IntentMessageSelectItemInfo(
    typing_extensions.TypedDict, total=False
):
    synonyms: typing.List[str]
    key: str

class GoogleCloudDialogflowCxV3beta1SessionEntityType(
    typing_extensions.TypedDict, total=False
):
    entities: typing.List[GoogleCloudDialogflowCxV3beta1EntityTypeEntity]
    entityOverrideMode: typing_extensions.Literal[
        "ENTITY_OVERRIDE_MODE_UNSPECIFIED",
        "ENTITY_OVERRIDE_MODE_OVERRIDE",
        "ENTITY_OVERRIDE_MODE_SUPPLEMENT",
    ]
    name: str

class GoogleCloudDialogflowV3alpha1CreateVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str
