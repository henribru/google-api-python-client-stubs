import typing

_list = list

@typing.type_check_only
class A2aV1APIKeySecurityScheme(typing.TypedDict, total=False):
    description: str
    location: str
    name: str

@typing.type_check_only
class A2aV1AgentCapabilities(typing.TypedDict, total=False):
    extensions: _list[A2aV1AgentExtension]
    pushNotifications: bool
    streaming: bool

@typing.type_check_only
class A2aV1AgentCard(typing.TypedDict, total=False):
    additionalInterfaces: _list[A2aV1AgentInterface]
    capabilities: A2aV1AgentCapabilities
    defaultInputModes: _list[str]
    defaultOutputModes: _list[str]
    description: str
    documentationUrl: str
    iconUrl: str
    name: str
    preferredTransport: str
    protocolVersion: str
    provider: A2aV1AgentProvider
    security: _list[A2aV1Security]
    securitySchemes: dict[str, typing.Any]
    signatures: _list[A2aV1AgentCardSignature]
    skills: _list[A2aV1AgentSkill]
    supportsAuthenticatedExtendedCard: bool
    url: str
    version: str

@typing.type_check_only
class A2aV1AgentCardSignature(typing.TypedDict, total=False):
    header: dict[str, typing.Any]
    protected: str
    signature: str

@typing.type_check_only
class A2aV1AgentExtension(typing.TypedDict, total=False):
    description: str
    params: dict[str, typing.Any]
    required: bool
    uri: str

@typing.type_check_only
class A2aV1AgentInterface(typing.TypedDict, total=False):
    tenant: str
    transport: str
    url: str

@typing.type_check_only
class A2aV1AgentProvider(typing.TypedDict, total=False):
    organization: str
    url: str

@typing.type_check_only
class A2aV1AgentSkill(typing.TypedDict, total=False):
    description: str
    examples: _list[str]
    id: str
    inputModes: _list[str]
    name: str
    outputModes: _list[str]
    security: _list[A2aV1Security]
    tags: _list[str]

@typing.type_check_only
class A2aV1Artifact(typing.TypedDict, total=False):
    artifactId: str
    description: str
    extensions: _list[str]
    metadata: dict[str, typing.Any]
    name: str
    parts: _list[A2aV1Part]

@typing.type_check_only
class A2aV1AuthenticationInfo(typing.TypedDict, total=False):
    credentials: str
    schemes: _list[str]

@typing.type_check_only
class A2aV1AuthorizationCodeOAuthFlow(typing.TypedDict, total=False):
    authorizationUrl: str
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class A2aV1CancelTaskRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class A2aV1ClientCredentialsOAuthFlow(typing.TypedDict, total=False):
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class A2aV1DataPart(typing.TypedDict, total=False):
    data: dict[str, typing.Any]

@typing.type_check_only
class A2aV1FilePart(typing.TypedDict, total=False):
    fileWithBytes: str
    fileWithUri: str
    mimeType: str
    name: str

@typing.type_check_only
class A2aV1HTTPAuthSecurityScheme(typing.TypedDict, total=False):
    bearerFormat: str
    description: str
    scheme: str

@typing.type_check_only
class A2aV1ImplicitOAuthFlow(typing.TypedDict, total=False):
    authorizationUrl: str
    refreshUrl: str
    scopes: dict[str, typing.Any]

@typing.type_check_only
class A2aV1ListTaskPushNotificationConfigResponse(typing.TypedDict, total=False):
    configs: _list[A2aV1TaskPushNotificationConfig]
    nextPageToken: str

@typing.type_check_only
class A2aV1Message(typing.TypedDict, total=False):
    content: _list[A2aV1Part]
    contextId: str
    extensions: _list[str]
    messageId: str
    metadata: dict[str, typing.Any]
    role: typing.Literal["ROLE_UNSPECIFIED", "ROLE_USER", "ROLE_AGENT"]
    taskId: str

@typing.type_check_only
class A2aV1MutualTlsSecurityScheme(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class A2aV1OAuth2SecurityScheme(typing.TypedDict, total=False):
    description: str
    flows: A2aV1OAuthFlows
    oauth2MetadataUrl: str

@typing.type_check_only
class A2aV1OAuthFlows(typing.TypedDict, total=False):
    authorizationCode: A2aV1AuthorizationCodeOAuthFlow
    clientCredentials: A2aV1ClientCredentialsOAuthFlow
    implicit: A2aV1ImplicitOAuthFlow
    password: A2aV1PasswordOAuthFlow

@typing.type_check_only
class A2aV1OpenIdConnectSecurityScheme(typing.TypedDict, total=False):
    description: str
    openIdConnectUrl: str

@typing.type_check_only
class A2aV1Part(typing.TypedDict, total=False):
    data: A2aV1DataPart
    file: A2aV1FilePart
    metadata: dict[str, typing.Any]
    text: str

@typing.type_check_only
class A2aV1PasswordOAuthFlow(typing.TypedDict, total=False):
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class A2aV1PushNotificationConfig(typing.TypedDict, total=False):
    authentication: A2aV1AuthenticationInfo
    id: str
    token: str
    url: str

@typing.type_check_only
class A2aV1Security(typing.TypedDict, total=False):
    schemes: dict[str, typing.Any]

@typing.type_check_only
class A2aV1SecurityScheme(typing.TypedDict, total=False):
    apiKeySecurityScheme: A2aV1APIKeySecurityScheme
    httpAuthSecurityScheme: A2aV1HTTPAuthSecurityScheme
    mtlsSecurityScheme: A2aV1MutualTlsSecurityScheme
    oauth2SecurityScheme: A2aV1OAuth2SecurityScheme
    openIdConnectSecurityScheme: A2aV1OpenIdConnectSecurityScheme

@typing.type_check_only
class A2aV1SendMessageConfiguration(typing.TypedDict, total=False):
    acceptedOutputModes: _list[str]
    blocking: bool
    historyLength: int
    pushNotification: A2aV1PushNotificationConfig

@typing.type_check_only
class A2aV1SendMessageRequest(typing.TypedDict, total=False):
    configuration: A2aV1SendMessageConfiguration
    message: A2aV1Message
    metadata: dict[str, typing.Any]

@typing.type_check_only
class A2aV1SendMessageResponse(typing.TypedDict, total=False):
    message: A2aV1Message
    task: A2aV1Task

@typing.type_check_only
class A2aV1StreamResponse(typing.TypedDict, total=False):
    artifactUpdate: A2aV1TaskArtifactUpdateEvent
    message: A2aV1Message
    statusUpdate: A2aV1TaskStatusUpdateEvent
    task: A2aV1Task

@typing.type_check_only
class A2aV1StringList(typing.TypedDict, total=False):
    list: _list[str]

@typing.type_check_only
class A2aV1Task(typing.TypedDict, total=False):
    artifacts: _list[A2aV1Artifact]
    contextId: str
    history: _list[A2aV1Message]
    id: str
    metadata: dict[str, typing.Any]
    status: A2aV1TaskStatus

@typing.type_check_only
class A2aV1TaskArtifactUpdateEvent(typing.TypedDict, total=False):
    append: bool
    artifact: A2aV1Artifact
    contextId: str
    lastChunk: bool
    metadata: dict[str, typing.Any]
    taskId: str

@typing.type_check_only
class A2aV1TaskPushNotificationConfig(typing.TypedDict, total=False):
    name: str
    pushNotificationConfig: A2aV1PushNotificationConfig

@typing.type_check_only
class A2aV1TaskStatus(typing.TypedDict, total=False):
    message: A2aV1Message
    state: typing.Literal[
        "TASK_STATE_UNSPECIFIED",
        "TASK_STATE_SUBMITTED",
        "TASK_STATE_WORKING",
        "TASK_STATE_COMPLETED",
        "TASK_STATE_FAILED",
        "TASK_STATE_CANCELLED",
        "TASK_STATE_INPUT_REQUIRED",
        "TASK_STATE_REJECTED",
        "TASK_STATE_AUTH_REQUIRED",
    ]
    timestamp: str

@typing.type_check_only
class A2aV1TaskStatusUpdateEvent(typing.TypedDict, total=False):
    contextId: str
    final: bool
    metadata: dict[str, typing.Any]
    status: A2aV1TaskStatus
    taskId: str

@typing.type_check_only
class GoogleApiDistribution(typing.TypedDict, total=False):
    bucketCounts: _list[str]
    bucketOptions: GoogleApiDistributionBucketOptions
    count: str
    exemplars: _list[GoogleApiDistributionExemplar]
    mean: float
    range: GoogleApiDistributionRange
    sumOfSquaredDeviation: float

@typing.type_check_only
class GoogleApiDistributionBucketOptions(typing.TypedDict, total=False):
    explicitBuckets: GoogleApiDistributionBucketOptionsExplicit
    exponentialBuckets: GoogleApiDistributionBucketOptionsExponential
    linearBuckets: GoogleApiDistributionBucketOptionsLinear

@typing.type_check_only
class GoogleApiDistributionBucketOptionsExplicit(typing.TypedDict, total=False):
    bounds: _list[float]

@typing.type_check_only
class GoogleApiDistributionBucketOptionsExponential(typing.TypedDict, total=False):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

@typing.type_check_only
class GoogleApiDistributionBucketOptionsLinear(typing.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class GoogleApiDistributionExemplar(typing.TypedDict, total=False):
    attachments: _list[dict[str, typing.Any]]
    timestamp: str
    value: float

@typing.type_check_only
class GoogleApiDistributionRange(typing.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class GoogleApiHttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleApiMetric(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleApiMonitoredResource(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleApiMonitoredResourceMetadata(typing.TypedDict, total=False):
    systemLabels: dict[str, typing.Any]
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingConnectorRunErrorContext(
    typing.TypedDict, total=False
):
    connectorRun: str
    dataConnector: str
    endTime: str
    entity: str
    operation: str
    startTime: str
    syncType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingErrorContext(typing.TypedDict, total=False):
    httpRequest: GoogleCloudDiscoveryengineLoggingHttpRequestContext
    reportLocation: GoogleCloudDiscoveryengineLoggingSourceLocation

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingErrorLog(typing.TypedDict, total=False):
    connectorRunPayload: GoogleCloudDiscoveryengineLoggingConnectorRunErrorContext
    context: GoogleCloudDiscoveryengineLoggingErrorContext
    importPayload: GoogleCloudDiscoveryengineLoggingImportErrorContext
    message: str
    requestPayload: dict[str, typing.Any]
    responsePayload: dict[str, typing.Any]
    serviceContext: GoogleCloudDiscoveryengineLoggingServiceContext
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingHttpRequestContext(
    typing.TypedDict, total=False
):
    responseStatusCode: int

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingImportErrorContext(
    typing.TypedDict, total=False
):
    document: str
    gcsPath: str
    lineNumber: str
    operation: str
    userEvent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingServiceContext(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingSourceLocation(typing.TypedDict, total=False):
    functionName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AclConfig(typing.TypedDict, total=False):
    idpConfig: GoogleCloudDiscoveryengineV1IdpConfig
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ActionConfig(typing.TypedDict, total=False):
    actionParams: dict[str, typing.Any]
    createBapConnection: bool
    isActionConfigured: bool
    jsonActionParams: str
    serviceName: str
    useStaticSecrets: bool
    userDefinedScopesMapping: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ActionConfigScopeList(typing.TypedDict, total=False):
    scopes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryRequest(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1AdvancedCompleteQueryRequestBoostSpec
    experimentIds: _list[str]
    includeTailSuggestions: bool
    query: str
    queryModel: str
    suggestionTypeSpecs: _list[
        GoogleCloudDiscoveryengineV1AdvancedCompleteQueryRequestSuggestionTypeSpec
    ]
    suggestionTypes: _list[
        typing.Literal[
            "SUGGESTION_TYPE_UNSPECIFIED",
            "QUERY",
            "PEOPLE",
            "CONTENT",
            "RECENT_SEARCH",
            "GOOGLE_WORKSPACE",
        ]
    ]
    userInfo: GoogleCloudDiscoveryengineV1UserInfo
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryRequestBoostSpec(
    typing.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1AdvancedCompleteQueryRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryRequestSuggestionTypeSpec(
    typing.TypedDict, total=False
):
    maxSuggestions: int
    suggestionType: typing.Literal[
        "SUGGESTION_TYPE_UNSPECIFIED",
        "QUERY",
        "PEOPLE",
        "CONTENT",
        "RECENT_SEARCH",
        "GOOGLE_WORKSPACE",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponse(
    typing.TypedDict, total=False
):
    contentSuggestions: _list[
        GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponseContentSuggestion
    ]
    peopleSuggestions: _list[
        GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponsePersonSuggestion
    ]
    querySuggestions: _list[
        GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponseQuerySuggestion
    ]
    recentSearchSuggestions: _list[
        GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponseRecentSearchSuggestion
    ]
    tailMatchTriggered: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponseContentSuggestion(
    typing.TypedDict, total=False
):
    contentType: typing.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "GOOGLE_WORKSPACE", "THIRD_PARTY"
    ]
    dataStore: str
    destinationUri: str
    document: GoogleCloudDiscoveryengineV1Document
    iconUri: str
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponsePersonSuggestion(
    typing.TypedDict, total=False
):
    dataStore: str
    destinationUri: str
    displayPhotoUri: str
    document: GoogleCloudDiscoveryengineV1Document
    personType: typing.Literal[
        "PERSON_TYPE_UNSPECIFIED",
        "CLOUD_IDENTITY",
        "THIRD_PARTY_IDENTITY",
        "GOOGLE_GROUP",
    ]
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponseQuerySuggestion(
    typing.TypedDict, total=False
):
    completableFieldPaths: _list[str]
    dataStore: _list[str]
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedCompleteQueryResponseRecentSearchSuggestion(
    typing.TypedDict, total=False
):
    recentSearchTime: str
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedSiteSearchConfig(
    typing.TypedDict, total=False
):
    disableAutomaticRefresh: bool
    disableInitialIndex: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AgentGatewaySetting(typing.TypedDict, total=False):
    defaultEgressAgentGateway: (
        GoogleCloudDiscoveryengineV1AgentGatewaySettingAgentGatewayReference
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AgentGatewaySettingAgentGatewayReference(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AlertPolicyConfig(typing.TypedDict, total=False):
    alertEnrollments: _list[
        GoogleCloudDiscoveryengineV1AlertPolicyConfigAlertEnrollment
    ]
    alertPolicyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AlertPolicyConfigAlertEnrollment(
    typing.TypedDict, total=False
):
    alertId: str
    enrollState: typing.Literal["ENROLL_STATES_UNSPECIFIED", "ENROLLED", "DECLINED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AlloyDbSource(typing.TypedDict, total=False):
    clusterId: str
    databaseId: str
    gcsStagingDir: str
    locationId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Answer(typing.TypedDict, total=False):
    answerSkippedReasons: _list[
        typing.Literal[
            "ANSWER_SKIPPED_REASON_UNSPECIFIED",
            "ADVERSARIAL_QUERY_IGNORED",
            "NON_ANSWER_SEEKING_QUERY_IGNORED",
            "OUT_OF_DOMAIN_QUERY_IGNORED",
            "POTENTIAL_POLICY_VIOLATION",
            "NO_RELEVANT_CONTENT",
            "JAIL_BREAKING_QUERY_IGNORED",
            "CUSTOMER_POLICY_VIOLATION",
            "NON_ANSWER_SEEKING_QUERY_IGNORED_V2",
            "LOW_GROUNDED_ANSWER",
            "USER_DEFINED_CLASSIFICATION_QUERY_IGNORED",
            "UNHELPFUL_ANSWER",
        ]
    ]
    answerText: str
    citations: _list[GoogleCloudDiscoveryengineV1AnswerCitation]
    completeTime: str
    createTime: str
    groundingScore: float
    groundingSupports: _list[GoogleCloudDiscoveryengineV1AnswerGroundingSupport]
    name: str
    queryUnderstandingInfo: GoogleCloudDiscoveryengineV1AnswerQueryUnderstandingInfo
    references: _list[GoogleCloudDiscoveryengineV1AnswerReference]
    relatedQuestions: _list[str]
    safetyRatings: _list[GoogleCloudDiscoveryengineV1SafetyRating]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "STREAMING"
    ]
    steps: _list[GoogleCloudDiscoveryengineV1AnswerStep]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerCitation(typing.TypedDict, total=False):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1AnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerCitationSource(typing.TypedDict, total=False):
    referenceId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerGenerationSpec(typing.TypedDict, total=False):
    userDefinedClassifierSpec: (
        GoogleCloudDiscoveryengineV1AnswerGenerationSpecUserDefinedClassifierSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerGenerationSpecUserDefinedClassifierSpec(
    typing.TypedDict, total=False
):
    enableUserDefinedClassifier: bool
    modelId: str
    preamble: str
    seed: int
    taskMarker: str
    temperature: float
    topK: str
    topP: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerGroundingSupport(typing.TypedDict, total=False):
    endIndex: str
    groundingCheckRequired: bool
    groundingScore: float
    sources: _list[GoogleCloudDiscoveryengineV1AnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequest(typing.TypedDict, total=False):
    answerGenerationSpec: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpec
    )
    asynchronousMode: bool
    endUserSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpec
    groundingSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestGroundingSpec
    query: GoogleCloudDiscoveryengineV1Query
    queryUnderstandingSpec: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpec
    )
    relatedQuestionsSpec: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestRelatedQuestionsSpec
    )
    safetySpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestSafetySpec
    searchSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpec
    session: str
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpec(
    typing.TypedDict, total=False
):
    answerLanguageCode: str
    ignoreAdversarialQuery: bool
    ignoreJailBreakingQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonAnswerSeekingQuery: bool
    includeCitations: bool
    modelSpec: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpecModelSpec
    )
    promptSpec: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpecPromptSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpecModelSpec(
    typing.TypedDict, total=False
):
    modelVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpecPromptSpec(
    typing.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpec(
    typing.TypedDict, total=False
):
    endUserMetadata: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpecEndUserMetaData
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpecEndUserMetaData(
    typing.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfo(
    typing.TypedDict, total=False
):
    content: str
    documentMetadata: GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfoDocumentMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfoDocumentMetadata(
    typing.TypedDict, total=False
):
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestGroundingSpec(
    typing.TypedDict, total=False
):
    filteringLevel: typing.Literal[
        "FILTERING_LEVEL_UNSPECIFIED", "FILTERING_LEVEL_LOW", "FILTERING_LEVEL_HIGH"
    ]
    includeGroundingSupports: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpec(
    typing.TypedDict, total=False
):
    disableSpellCorrection: bool
    queryClassificationSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec
    queryRephraserSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec(
    typing.TypedDict, total=False
):
    types: _list[
        typing.Literal[
            "TYPE_UNSPECIFIED",
            "ADVERSARIAL_QUERY",
            "NON_ANSWER_SEEKING_QUERY",
            "JAIL_BREAKING_QUERY",
            "NON_ANSWER_SEEKING_QUERY_V2",
            "USER_DEFINED_CLASSIFICATION_QUERY",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec(
    typing.TypedDict, total=False
):
    disable: bool
    maxRephraseSteps: int
    modelSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpecModelSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpecModelSpec(
    typing.TypedDict, total=False
):
    modelType: typing.Literal["MODEL_TYPE_UNSPECIFIED", "SMALL", "LARGE"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestRelatedQuestionsSpec(
    typing.TypedDict, total=False
):
    enable: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSafetySpec(
    typing.TypedDict, total=False
):
    enable: bool
    safetySettings: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSafetySpecSafetySetting
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSafetySpecSafetySetting(
    typing.TypedDict, total=False
):
    category: typing.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    threshold: typing.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpec(
    typing.TypedDict, total=False
):
    searchParams: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchParams
    searchResultList: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultList
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchParams(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestDataStoreSpec]
    filter: str
    maxReturnResults: int
    orderBy: str
    searchResultMode: typing.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultList(
    typing.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResult(
    typing.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo
    unstructuredDocumentInfo: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo(
    typing.TypedDict, total=False
):
    chunk: str
    content: str
    documentMetadata: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfoDocumentMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfoDocumentMetadata(
    typing.TypedDict, total=False
):
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo(
    typing.TypedDict, total=False
):
    document: str
    documentContexts: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoDocumentContext
    ]
    extractiveAnswers: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveAnswer
    ]
    extractiveSegments: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveSegment
    ]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoDocumentContext(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveAnswer(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveSegment(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryResponse(typing.TypedDict, total=False):
    answer: GoogleCloudDiscoveryengineV1Answer
    answerQueryToken: str
    session: GoogleCloudDiscoveryengineV1Session

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryUnderstandingInfo(
    typing.TypedDict, total=False
):
    queryClassificationInfo: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryUnderstandingInfoQueryClassificationInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryUnderstandingInfoQueryClassificationInfo(
    typing.TypedDict, total=False
):
    positive: bool
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ADVERSARIAL_QUERY",
        "NON_ANSWER_SEEKING_QUERY",
        "JAIL_BREAKING_QUERY",
        "NON_ANSWER_SEEKING_QUERY_V2",
        "USER_DEFINED_CLASSIFICATION_QUERY",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReference(typing.TypedDict, total=False):
    chunkInfo: GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfo
    structuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1AnswerReferenceStructuredDocumentInfo
    )
    unstructuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1AnswerReferenceUnstructuredDocumentInfo
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfo(
    typing.TypedDict, total=False
):
    chunk: str
    content: str
    documentMetadata: (
        GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfoDocumentMetadata
    )
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfoDocumentMetadata(
    typing.TypedDict, total=False
):
    document: str
    pageIdentifier: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceStructuredDocumentInfo(
    typing.TypedDict, total=False
):
    document: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceUnstructuredDocumentInfo(
    typing.TypedDict, total=False
):
    chunkContents: _list[
        GoogleCloudDiscoveryengineV1AnswerReferenceUnstructuredDocumentInfoChunkContent
    ]
    document: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceUnstructuredDocumentInfoChunkContent(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStep(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDiscoveryengineV1AnswerStepAction]
    description: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]
    thought: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepAction(typing.TypedDict, total=False):
    observation: GoogleCloudDiscoveryengineV1AnswerStepActionObservation
    searchAction: GoogleCloudDiscoveryengineV1AnswerStepActionSearchAction

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionObservation(
    typing.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResult(
    typing.TypedDict, total=False
):
    chunkInfo: _list[
        GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResultChunkInfo
    ]
    document: str
    snippetInfo: _list[
        GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResultSnippetInfo
    ]
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResultChunkInfo(
    typing.TypedDict, total=False
):
    chunk: str
    content: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResultSnippetInfo(
    typing.TypedDict, total=False
):
    snippet: str
    snippetStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionSearchAction(
    typing.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistAnswer(typing.TypedDict, total=False):
    assistSkippedReasons: _list[
        typing.Literal[
            "ASSIST_SKIPPED_REASON_UNSPECIFIED",
            "NON_ASSIST_SEEKING_QUERY_IGNORED",
            "CUSTOMER_POLICY_VIOLATION",
        ]
    ]
    customerPolicyEnforcementResult: (
        GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResult
    )
    name: str
    replies: _list[GoogleCloudDiscoveryengineV1AssistAnswerReply]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
        "SKIPPED",
        "CANCELLED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResult(
    typing.TypedDict, total=False
):
    policyResults: _list[
        GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResultPolicyEnforcementResult
    ]
    verdict: typing.Literal["UNSPECIFIED", "ALLOW", "BLOCK"]
    violationSource: typing.Literal[
        "VIOLATION_SOURCE_UNSPECIFIED", "SYSTEM", "PROMPT", "ATTACHMENT"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResultBannedPhraseEnforcementResult(
    typing.TypedDict, total=False
):
    bannedPhrases: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResultModelArmorEnforcementResult(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    modelArmorViolation: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResultPolicyEnforcementResult(
    typing.TypedDict, total=False
):
    bannedPhraseEnforcementResult: GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResultBannedPhraseEnforcementResult
    modelArmorEnforcementResult: GoogleCloudDiscoveryengineV1AssistAnswerCustomerPolicyEnforcementResultModelArmorEnforcementResult

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistAnswerReply(typing.TypedDict, total=False):
    createTime: str
    groundedContent: GoogleCloudDiscoveryengineV1AssistantGroundedContent

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistUserMetadata(typing.TypedDict, total=False):
    preferredLanguageCode: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Assistant(typing.TypedDict, total=False):
    createTime: str
    customerPolicy: GoogleCloudDiscoveryengineV1AssistantCustomerPolicy
    defaultWebGroundingToggleOff: bool
    description: str
    displayName: str
    enabledTools: dict[str, typing.Any]
    generationConfig: GoogleCloudDiscoveryengineV1AssistantGenerationConfig
    name: str
    updateTime: str
    webGroundingType: typing.Literal[
        "WEB_GROUNDING_TYPE_UNSPECIFIED",
        "WEB_GROUNDING_TYPE_DISABLED",
        "WEB_GROUNDING_TYPE_GOOGLE_SEARCH",
        "WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantContent(typing.TypedDict, total=False):
    codeExecutionResult: GoogleCloudDiscoveryengineV1AssistantContentCodeExecutionResult
    executableCode: GoogleCloudDiscoveryengineV1AssistantContentExecutableCode
    file: GoogleCloudDiscoveryengineV1AssistantContentFile
    inlineData: GoogleCloudDiscoveryengineV1AssistantContentBlob
    role: str
    text: str
    thought: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantContentBlob(typing.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantContentCodeExecutionResult(
    typing.TypedDict, total=False
):
    outcome: typing.Literal[
        "OUTCOME_UNSPECIFIED",
        "OUTCOME_OK",
        "OUTCOME_FAILED",
        "OUTCOME_DEADLINE_EXCEEDED",
    ]
    output: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantContentExecutableCode(
    typing.TypedDict, total=False
):
    code: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantContentFile(typing.TypedDict, total=False):
    fileId: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantCustomerPolicy(
    typing.TypedDict, total=False
):
    bannedPhrases: _list[
        GoogleCloudDiscoveryengineV1AssistantCustomerPolicyBannedPhrase
    ]
    modelArmorConfig: (
        GoogleCloudDiscoveryengineV1AssistantCustomerPolicyModelArmorConfig
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantCustomerPolicyBannedPhrase(
    typing.TypedDict, total=False
):
    ignoreDiacritics: bool
    matchType: typing.Literal[
        "BANNED_PHRASE_MATCH_TYPE_UNSPECIFIED",
        "SIMPLE_STRING_MATCH",
        "WORD_BOUNDARY_STRING_MATCH",
    ]
    phrase: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantCustomerPolicyModelArmorConfig(
    typing.TypedDict, total=False
):
    failureMode: typing.Literal["FAILURE_MODE_UNSPECIFIED", "FAIL_OPEN", "FAIL_CLOSED"]
    responseTemplate: str
    userPromptTemplate: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGenerationConfig(
    typing.TypedDict, total=False
):
    allowedModelIds: _list[str]
    defaultLanguage: str
    defaultModelId: str
    systemInstruction: (
        GoogleCloudDiscoveryengineV1AssistantGenerationConfigSystemInstruction
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGenerationConfigSystemInstruction(
    typing.TypedDict, total=False
):
    additionalSystemInstruction: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGroundedContent(
    typing.TypedDict, total=False
):
    citationMetadata: GoogleCloudDiscoveryengineV1CitationMetadata
    content: GoogleCloudDiscoveryengineV1AssistantContent
    textGroundingMetadata: (
        GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadata
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadata(
    typing.TypedDict, total=False
):
    references: _list[
        GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataReference
    ]
    segments: _list[
        GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataSegment
    ]
    visualSegments: _list[
        GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataVisualSegment
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataReference(
    typing.TypedDict, total=False
):
    codeSnippet: str
    content: str
    documentMetadata: GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataReferenceDocumentMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataReferenceDocumentMetadata(
    typing.TypedDict, total=False
):
    document: str
    domain: str
    language: typing.Literal["LANGUAGE_UNSPECIFIED", "PYTHON", "SQL"]
    mimeType: str
    pageIdentifier: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataSegment(
    typing.TypedDict, total=False
):
    endIndex: str
    groundingScore: float
    referenceIndices: _list[int]
    startIndex: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantGroundedContentTextGroundingMetadataVisualSegment(
    typing.TypedDict, total=False
):
    contentId: str
    referenceIndices: _list[int]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantToolInfo(typing.TypedDict, total=False):
    toolDisplayName: str
    toolName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AssistantToolList(typing.TypedDict, total=False):
    toolInfo: _list[GoogleCloudDiscoveryengineV1AssistantToolInfo]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BAPConfig(typing.TypedDict, total=False):
    enabledActions: _list[str]
    supportedConnectorModes: _list[
        typing.Literal[
            "CONNECTOR_MODE_UNSPECIFIED",
            "DATA_INGESTION",
            "ACTIONS",
            "END_USER_AUTHENTICATION",
        ]
    ]
    toolspecOverride: GoogleCloudDiscoveryengineV1BAPConfigToolspecOverride

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BAPConfigToolspecOverride(
    typing.TypedDict, total=False
):
    baseVersion: str
    tools: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSitesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudDiscoveryengineV1CreateTargetSiteRequest]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSitesResponse(
    typing.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponse(
    typing.TypedDict, total=False
):
    documentsMetadata: _list[
        GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadata
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadata(
    typing.TypedDict, total=False
):
    dataIngestionSource: str
    lastRefreshedTime: str
    matcherValue: GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadataMatcherValue
    state: typing.Literal[
        "STATE_UNSPECIFIED", "INDEXED", "NOT_IN_TARGET_SITE", "NOT_IN_INDEX"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadataMatcherValue(
    typing.TypedDict, total=False
):
    fhirResource: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchUpdateUserLicensesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchUpdateUserLicensesRequest(
    typing.TypedDict, total=False
):
    deleteUnassignedUserLicenses: bool
    inlineSource: GoogleCloudDiscoveryengineV1BatchUpdateUserLicensesRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchUpdateUserLicensesRequestInlineSource(
    typing.TypedDict, total=False
):
    updateMask: str
    userLicenses: _list[GoogleCloudDiscoveryengineV1UserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchUpdateUserLicensesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    userLicenses: _list[GoogleCloudDiscoveryengineV1UserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchVerifyTargetSitesRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigQuerySource(typing.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigtableOptions(typing.TypedDict, total=False):
    families: dict[str, typing.Any]
    keyFieldName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigtableOptionsBigtableColumn(
    typing.TypedDict, total=False
):
    encoding: typing.Literal["ENCODING_UNSPECIFIED", "TEXT", "BINARY"]
    fieldName: str
    qualifier: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "STRING",
        "NUMBER",
        "INTEGER",
        "VAR_INTEGER",
        "BIG_NUMERIC",
        "BOOLEAN",
        "JSON",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigtableOptionsBigtableColumnFamily(
    typing.TypedDict, total=False
):
    columns: _list[GoogleCloudDiscoveryengineV1BigtableOptionsBigtableColumn]
    encoding: typing.Literal["ENCODING_UNSPECIFIED", "TEXT", "BINARY"]
    fieldName: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "STRING",
        "NUMBER",
        "INTEGER",
        "VAR_INTEGER",
        "BIG_NUMERIC",
        "BOOLEAN",
        "JSON",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigtableSource(typing.TypedDict, total=False):
    bigtableOptions: GoogleCloudDiscoveryengineV1BigtableOptions
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingRequest(typing.TypedDict, total=False):
    answerCandidate: str
    facts: _list[GoogleCloudDiscoveryengineV1GroundingFact]
    groundingSpec: GoogleCloudDiscoveryengineV1CheckGroundingSpec
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingResponse(typing.TypedDict, total=False):
    citedChunks: _list[GoogleCloudDiscoveryengineV1FactChunk]
    citedFacts: _list[
        GoogleCloudDiscoveryengineV1CheckGroundingResponseCheckGroundingFactChunk
    ]
    claims: _list[GoogleCloudDiscoveryengineV1CheckGroundingResponseClaim]
    supportScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingResponseCheckGroundingFactChunk(
    typing.TypedDict, total=False
):
    chunkText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingResponseClaim(
    typing.TypedDict, total=False
):
    citationIndices: _list[int]
    claimText: str
    endPos: int
    groundingCheckRequired: bool
    score: float
    startPos: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingSpec(typing.TypedDict, total=False):
    citationThreshold: float
    enableClaimLevelScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Chunk(typing.TypedDict, total=False):
    annotationContents: _list[str]
    annotationMetadata: _list[GoogleCloudDiscoveryengineV1ChunkAnnotationMetadata]
    chunkMetadata: GoogleCloudDiscoveryengineV1ChunkChunkMetadata
    content: str
    dataUrls: _list[str]
    derivedStructData: dict[str, typing.Any]
    documentMetadata: GoogleCloudDiscoveryengineV1ChunkDocumentMetadata
    id: str
    name: str
    pageSpan: GoogleCloudDiscoveryengineV1ChunkPageSpan
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkAnnotationMetadata(
    typing.TypedDict, total=False
):
    imageId: str
    structuredContent: GoogleCloudDiscoveryengineV1ChunkStructuredContent

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkChunkMetadata(typing.TypedDict, total=False):
    nextChunks: _list[GoogleCloudDiscoveryengineV1Chunk]
    previousChunks: _list[GoogleCloudDiscoveryengineV1Chunk]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkDocumentMetadata(typing.TypedDict, total=False):
    mimeType: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkPageSpan(typing.TypedDict, total=False):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkStructuredContent(typing.TypedDict, total=False):
    content: str
    structureType: typing.Literal[
        "STRUCTURE_TYPE_UNSPECIFIED",
        "SHAREHOLDER_STRUCTURE",
        "SIGNATURE_STRUCTURE",
        "CHECKBOX_STRUCTURE",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Citation(typing.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: GoogleTypeDate
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CitationMetadata(typing.TypedDict, total=False):
    citations: _list[GoogleCloudDiscoveryengineV1Citation]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CliConfig(typing.TypedDict, total=False):
    enabledActions: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CloudSqlSource(typing.TypedDict, total=False):
    databaseId: str
    gcsStagingDir: str
    instanceId: str
    offload: bool
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CmekConfig(typing.TypedDict, total=False):
    isDefault: bool
    kmsKey: str
    kmsKeyVersion: str
    lastRotationTimestampMicros: str
    name: str
    notebooklmState: typing.Literal[
        "NOTEBOOK_LM_STATE_UNSPECIFIED",
        "NOTEBOOK_LM_NOT_READY",
        "NOTEBOOK_LM_READY",
        "NOTEBOOK_LM_NOT_ENABLED",
    ]
    singleRegionKeys: _list[GoogleCloudDiscoveryengineV1SingleRegionKey]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "KEY_ISSUE",
        "DELETING",
        "DELETE_FAILED",
        "UNUSABLE",
        "ACTIVE_ROTATING",
        "DELETED",
        "EXPIRED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Collection(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompleteQueryResponse(typing.TypedDict, total=False):
    querySuggestions: _list[
        GoogleCloudDiscoveryengineV1CompleteQueryResponseQuerySuggestion
    ]
    tailMatchTriggered: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompleteQueryResponseQuerySuggestion(
    typing.TypedDict, total=False
):
    completableFieldPaths: _list[str]
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompletionInfo(typing.TypedDict, total=False):
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompletionSuggestion(typing.TypedDict, total=False):
    alternativePhrases: _list[str]
    frequency: str
    globalScore: float
    groupId: str
    groupScore: float
    languageCode: str
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Condition(typing.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1ConditionTimeRange]
    queryRegex: str
    queryTerms: _list[GoogleCloudDiscoveryengineV1ConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConditionQueryTerm(typing.TypedDict, total=False):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConditionTimeRange(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Control(typing.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1ControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1Condition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1ControlFilterAction
    name: str
    promoteAction: GoogleCloudDiscoveryengineV1ControlPromoteAction
    redirectAction: GoogleCloudDiscoveryengineV1ControlRedirectAction
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1ControlSynonymsAction
    useCases: _list[
        typing.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlBoostAction(typing.TypedDict, total=False):
    boost: float
    dataStore: str
    filter: str
    fixedBoost: float
    interpolationBoostSpec: (
        GoogleCloudDiscoveryengineV1ControlBoostActionInterpolationBoostSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlBoostActionInterpolationBoostSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1ControlBoostActionInterpolationBoostSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlBoostActionInterpolationBoostSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlFilterAction(typing.TypedDict, total=False):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlPromoteAction(typing.TypedDict, total=False):
    dataStore: str
    searchLinkPromotion: GoogleCloudDiscoveryengineV1SearchLinkPromotion

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlRedirectAction(typing.TypedDict, total=False):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlSynonymsAction(typing.TypedDict, total=False):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Conversation(typing.TypedDict, total=False):
    endTime: str
    messages: _list[GoogleCloudDiscoveryengineV1ConversationMessage]
    name: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETED"]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConversationContext(typing.TypedDict, total=False):
    activeDocument: str
    contextDocuments: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConversationMessage(typing.TypedDict, total=False):
    createTime: str
    reply: GoogleCloudDiscoveryengineV1Reply
    userInput: GoogleCloudDiscoveryengineV1TextInput

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConverseConversationRequest(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpec
    conversation: GoogleCloudDiscoveryengineV1Conversation
    filter: str
    query: GoogleCloudDiscoveryengineV1TextInput
    safeSearch: bool
    servingConfig: str
    summarySpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpec
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConverseConversationResponse(
    typing.TypedDict, total=False
):
    conversation: GoogleCloudDiscoveryengineV1Conversation
    reply: GoogleCloudDiscoveryengineV1Reply
    searchResults: _list[GoogleCloudDiscoveryengineV1SearchResponseSearchResult]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateDataStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateEngineMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateSchemaMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateSitemapMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateTargetSiteRequest(
    typing.TypedDict, total=False
):
    parent: str
    targetSite: GoogleCloudDiscoveryengineV1TargetSite

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CustomAttribute(typing.TypedDict, total=False):
    numbers: _list[float]
    text: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CustomTuningModel(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    errorMessage: str
    metrics: dict[str, typing.Any]
    modelState: typing.Literal[
        "MODEL_STATE_UNSPECIFIED",
        "TRAINING_PAUSED",
        "TRAINING",
        "TRAINING_COMPLETE",
        "READY_FOR_SERVING",
        "TRAINING_FAILED",
        "NO_IMPROVEMENT",
        "INPUT_VALIDATION_FAILED",
    ]
    modelVersion: str
    name: str
    trainingStartTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataConnector(typing.TypedDict, total=False):
    aclEnabled: bool
    actionConfig: GoogleCloudDiscoveryengineV1ActionConfig
    actionState: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "RUNNING",
        "WARNING",
        "INITIALIZATION_FAILED",
        "UPDATING",
    ]
    alertPolicyConfigs: _list[GoogleCloudDiscoveryengineV1AlertPolicyConfig]
    autoRunDisabled: bool
    bapConfig: GoogleCloudDiscoveryengineV1BAPConfig
    blockingReasons: _list[
        typing.Literal[
            "BLOCKING_REASON_UNSPECIFIED",
            "ALLOWLIST_STATIC_IP",
            "ALLOWLIST_IN_SERVICE_ATTACHMENT",
            "ALLOWLIST_SERVICE_ACCOUNT",
        ]
    ]
    cliConfig: GoogleCloudDiscoveryengineV1CliConfig
    connectorModes: _list[
        typing.Literal[
            "CONNECTOR_MODE_UNSPECIFIED",
            "DATA_INGESTION",
            "ACTIONS",
            "FEDERATED",
            "EUA",
            "FEDERATED_AND_EUA",
        ]
    ]
    connectorSourceId: str
    connectorType: typing.Literal[
        "CONNECTOR_TYPE_UNSPECIFIED",
        "THIRD_PARTY",
        "GCP_FHIR",
        "BIG_QUERY",
        "GCS",
        "GOOGLE_MAIL",
        "GOOGLE_CALENDAR",
        "GOOGLE_DRIVE",
        "NATIVE_CLOUD_IDENTITY",
        "THIRD_PARTY_FEDERATED",
        "THIRD_PARTY_EUA",
        "GCNV",
        "GOOGLE_CHAT",
        "GOOGLE_SITES",
        "REMOTE_MCP",
        "GOOGLE_WORKSPACE",
    ]
    createEuaSaas: bool
    createTime: str
    dataSource: str
    destinationConfigs: _list[GoogleCloudDiscoveryengineV1DestinationConfig]
    dynamicTools: _list[GoogleCloudDiscoveryengineV1DynamicTool]
    egressFqdns: _list[str]
    endUserConfig: GoogleCloudDiscoveryengineV1DataConnectorEndUserConfig
    entities: _list[GoogleCloudDiscoveryengineV1DataConnectorSourceEntity]
    errors: _list[GoogleRpcStatus]
    federatedConfig: GoogleCloudDiscoveryengineV1DataConnectorFederatedConfig
    hybridIngestionDisabled: bool
    identityRefreshInterval: str
    identityScheduleConfig: GoogleCloudDiscoveryengineV1IdentityScheduleConfig
    incrementalRefreshInterval: str
    incrementalSyncDisabled: bool
    jsonParams: str
    kmsKeyName: str
    lastSyncTime: str
    latestPauseTime: str
    metadata: GoogleCloudDiscoveryengineV1DataConnectorConnectorMetadata
    name: str
    nextSyncTime: GoogleTypeDateTime
    oauthStaticIpAddresses: _list[str]
    params: dict[str, typing.Any]
    privateConnectivityProjectId: str
    realtimeState: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "RUNNING",
        "WARNING",
        "INITIALIZATION_FAILED",
        "UPDATING",
    ]
    realtimeSyncConfig: GoogleCloudDiscoveryengineV1DataConnectorRealtimeSyncConfig
    refreshInterval: str
    removeParamKeys: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "RUNNING",
        "WARNING",
        "INITIALIZATION_FAILED",
        "UPDATING",
    ]
    staticIpAddresses: _list[str]
    staticIpEnabled: bool
    syncMode: typing.Literal["PERIODIC", "STREAMING", "UNSPECIFIED"]
    tag: str
    updateTime: str
    vpcscEnabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataConnectorConnectorMetadata(
    typing.TypedDict, total=False
):
    author: str
    description: str
    note: str
    shortDescription: str
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataConnectorEndUserConfig(
    typing.TypedDict, total=False
):
    additionalParams: dict[str, typing.Any]
    authParams: dict[str, typing.Any]
    jsonAuthParams: str
    tenant: GoogleCloudDiscoveryengineV1Tenant

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataConnectorFederatedConfig(
    typing.TypedDict, total=False
):
    additionalParams: dict[str, typing.Any]
    authParams: dict[str, typing.Any]
    jsonAuthParams: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataConnectorRealtimeSyncConfig(
    typing.TypedDict, total=False
):
    realtimeSyncSecret: str
    streamingError: (
        GoogleCloudDiscoveryengineV1DataConnectorRealtimeSyncConfigStreamingError
    )
    webhookUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataConnectorRealtimeSyncConfigStreamingError(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    streamingErrorReason: typing.Literal[
        "STREAMING_ERROR_REASON_UNSPECIFIED",
        "STREAMING_SETUP_ERROR",
        "STREAMING_SYNC_ERROR",
        "INGRESS_ENDPOINT_REQUIRED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataConnectorSourceEntity(
    typing.TypedDict, total=False
):
    dataStore: str
    entityName: str
    healthcareFhirConfig: GoogleCloudDiscoveryengineV1HealthcareFhirConfig
    jsonParams: str
    keyPropertyMappings: dict[str, typing.Any]
    params: dict[str, typing.Any]
    startingSchema: GoogleCloudDiscoveryengineV1Schema

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStore(typing.TypedDict, total=False):
    aclEnabled: bool
    advancedSiteSearchConfig: GoogleCloudDiscoveryengineV1AdvancedSiteSearchConfig
    billingEstimation: GoogleCloudDiscoveryengineV1DataStoreBillingEstimation
    cmekConfig: GoogleCloudDiscoveryengineV1CmekConfig
    configurableBillingApproach: typing.Literal[
        "CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED",
        "CONFIGURABLE_SUBSCRIPTION_INDEXING_CORE",
        "CONFIGURABLE_CONSUMPTION_EMBEDDING",
    ]
    configurableBillingApproachUpdateTime: str
    contentConfig: typing.Literal[
        "CONTENT_CONFIG_UNSPECIFIED",
        "NO_CONTENT",
        "CONTENT_REQUIRED",
        "PUBLIC_WEBSITE",
        "GOOGLE_WORKSPACE",
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfig
    federatedSearchConfig: GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfig
    healthcareFhirConfig: GoogleCloudDiscoveryengineV1HealthcareFhirConfig
    identityMappingStore: str
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    isInfobotFaqDataStore: bool
    kmsKeyName: str
    name: str
    naturalLanguageQueryUnderstandingConfig: (
        GoogleCloudDiscoveryengineV1NaturalLanguageQueryUnderstandingConfig
    )
    servingConfigDataStore: GoogleCloudDiscoveryengineV1DataStoreServingConfigDataStore
    solutionTypes: _list[
        typing.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
            "SOLUTION_TYPE_AI_MODE",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1Schema
    workspaceConfig: GoogleCloudDiscoveryengineV1WorkspaceConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreBillingEstimation(
    typing.TypedDict, total=False
):
    structuredDataSize: str
    structuredDataUpdateTime: str
    unstructuredDataSize: str
    unstructuredDataUpdateTime: str
    websiteDataSize: str
    websiteDataUpdateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfig(
    typing.TypedDict, total=False
):
    alloyDbConfig: (
        GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigAlloyDbConfig
    )
    notebooklmConfig: (
        GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigNotebooklmConfig
    )
    thirdPartyOauthConfig: (
        GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigThirdPartyOauthConfig
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigAlloyDbConfig(
    typing.TypedDict, total=False
):
    alloydbAiNlConfig: GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigAlloyDbConfigAlloyDbAiNaturalLanguageConfig
    alloydbConnectionConfig: GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigAlloyDbConfigAlloyDbConnectionConfig
    returnedFields: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigAlloyDbConfigAlloyDbAiNaturalLanguageConfig(
    typing.TypedDict, total=False
):
    nlConfigId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigAlloyDbConfigAlloyDbConnectionConfig(
    typing.TypedDict, total=False
):
    authMode: typing.Literal[
        "AUTH_MODE_UNSPECIFIED",
        "AUTH_MODE_SERVICE_ACCOUNT",
        "AUTH_MODE_END_USER_ACCOUNT",
    ]
    database: str
    enablePsvs: bool
    instance: str
    password: str
    user: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigNotebooklmConfig(
    typing.TypedDict, total=False
):
    searchConfig: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreFederatedSearchConfigThirdPartyOauthConfig(
    typing.TypedDict, total=False
):
    appName: str
    instanceName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreServingConfigDataStore(
    typing.TypedDict, total=False
):
    disabledForServing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteCmekConfigMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteCollectionMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteDataStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteEngineMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteIdentityMappingStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteSchemaMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteSitemapMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DestinationConfig(typing.TypedDict, total=False):
    destinations: _list[GoogleCloudDiscoveryengineV1DestinationConfigDestination]
    jsonParams: str
    key: str
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DestinationConfigDestination(
    typing.TypedDict, total=False
):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DistributeLicenseConfigRequest(
    typing.TypedDict, total=False
):
    licenseConfigId: str
    licenseCount: str
    location: str
    projectNumber: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DistributeLicenseConfigResponse(
    typing.TypedDict, total=False
):
    licenseConfig: GoogleCloudDiscoveryengineV1LicenseConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Document(typing.TypedDict, total=False):
    aclInfo: GoogleCloudDiscoveryengineV1DocumentAclInfo
    content: GoogleCloudDiscoveryengineV1DocumentContent
    derivedStructData: dict[str, typing.Any]
    id: str
    indexStatus: GoogleCloudDiscoveryengineV1DocumentIndexStatus
    indexTime: str
    jsonData: str
    name: str
    parentDocumentId: str
    schemaId: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentAclInfo(typing.TypedDict, total=False):
    readers: _list[GoogleCloudDiscoveryengineV1DocumentAclInfoAccessRestriction]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentAclInfoAccessRestriction(
    typing.TypedDict, total=False
):
    idpWide: bool
    principals: _list[GoogleCloudDiscoveryengineV1Principal]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentContent(typing.TypedDict, total=False):
    mimeType: str
    rawBytes: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentIndexStatus(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    indexTime: str
    pendingMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentInfo(typing.TypedDict, total=False):
    conversionValue: float
    id: str
    joined: bool
    name: str
    promotionIds: _list[str]
    quantity: int
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfig(
    typing.TypedDict, total=False
):
    chunkingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfig
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfig(
    typing.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig(
    typing.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing.TypedDict, total=False
):
    enableGetProcessedDocument: bool
    enableImageAnnotation: bool
    enableLlmLayoutParsing: bool
    enableTableAnnotation: bool
    excludeHtmlClasses: _list[str]
    excludeHtmlElements: _list[str]
    excludeHtmlIds: _list[str]
    structuredContentTypes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DoubleList(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DynamicTool(typing.TypedDict, total=False):
    description: str
    displayName: str
    enabled: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Engine(typing.TypedDict, total=False):
    agentGatewaySetting: GoogleCloudDiscoveryengineV1AgentGatewaySetting
    appType: typing.Literal["APP_TYPE_UNSPECIFIED", "APP_TYPE_INTRANET"]
    associatedAgentRegistry: str
    chatEngineConfig: GoogleCloudDiscoveryengineV1EngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1EngineChatEngineMetadata
    cmekConfig: GoogleCloudDiscoveryengineV1CmekConfig
    commonConfig: GoogleCloudDiscoveryengineV1EngineCommonConfig
    configurableBillingApproach: typing.Literal[
        "CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED",
        "CONFIGURABLE_BILLING_APPROACH_ENABLED",
    ]
    connectorTenantInfo: dict[str, typing.Any]
    createTime: str
    dataStoreIds: _list[str]
    disableAnalytics: bool
    displayName: str
    features: dict[str, typing.Any]
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    knowledgeGraphConfig: GoogleCloudDiscoveryengineV1EngineKnowledgeGraphConfig
    marketplaceAgentVisibility: typing.Literal[
        "MARKETPLACE_AGENT_VISIBILITY_UNSPECIFIED",
        "SHOW_AVAILABLE_AGENTS_ONLY",
        "SHOW_AGENTS_ALREADY_INTEGRATED",
        "SHOW_AGENTS_ALREADY_PURCHASED",
        "SHOW_ALL_AGENTS",
    ]
    mediaRecommendationEngineConfig: (
        GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfig
    )
    modelConfigs: dict[str, typing.Any]
    name: str
    observabilityConfig: GoogleCloudDiscoveryengineV1ObservabilityConfig
    procurementContactEmails: _list[str]
    searchEngineConfig: GoogleCloudDiscoveryengineV1EngineSearchEngineConfig
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineConfig(typing.TypedDict, total=False):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1EngineChatEngineConfigAgentCreationConfig
    )
    allowCrossRegion: bool
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineConfigAgentCreationConfig(
    typing.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineMetadata(
    typing.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineCommonConfig(typing.TypedDict, total=False):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineKnowledgeGraphConfig(
    typing.TypedDict, total=False
):
    cloudKnowledgeGraphTypes: _list[str]
    enableCloudKnowledgeGraph: bool
    enablePrivateKnowledgeGraph: bool
    featureConfig: GoogleCloudDiscoveryengineV1EngineKnowledgeGraphConfigFeatureConfig
    privateKnowledgeGraphTypes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineKnowledgeGraphConfigFeatureConfig(
    typing.TypedDict, total=False
):
    disablePrivateKgAutoComplete: bool
    disablePrivateKgEnrichment: bool
    disablePrivateKgQueryUiChips: bool
    disablePrivateKgQueryUnderstanding: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfig(
    typing.TypedDict, total=False
):
    engineFeaturesConfig: GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigEngineFeaturesConfig
    optimizationObjective: str
    optimizationObjectiveConfig: GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigOptimizationObjectiveConfig
    trainingState: typing.Literal["TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"]
    type: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigEngineFeaturesConfig(
    typing.TypedDict, total=False
):
    mostPopularConfig: GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigMostPopularFeatureConfig
    recommendedForYouConfig: GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigRecommendedForYouFeatureConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigMostPopularFeatureConfig(
    typing.TypedDict, total=False
):
    timeWindowDays: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigOptimizationObjectiveConfig(
    typing.TypedDict, total=False
):
    targetField: str
    targetFieldValueFloat: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineMediaRecommendationEngineConfigRecommendedForYouFeatureConfig(
    typing.TypedDict, total=False
):
    contextEventType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineSearchEngineConfig(
    typing.TypedDict, total=False
):
    requiredSubscriptionTier: typing.Literal[
        "SUBSCRIPTION_TIER_UNSPECIFIED",
        "SUBSCRIPTION_TIER_SEARCH",
        "SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT",
        "SUBSCRIPTION_TIER_NOTEBOOK_LM",
        "SUBSCRIPTION_TIER_FRONTLINE_WORKER",
        "SUBSCRIPTION_TIER_AGENTSPACE_STARTER",
        "SUBSCRIPTION_TIER_AGENTSPACE_BUSINESS",
        "SUBSCRIPTION_TIER_ENTERPRISE",
        "SUBSCRIPTION_TIER_ENTERPRISE_EMERGING",
        "SUBSCRIPTION_TIER_EDU",
        "SUBSCRIPTION_TIER_EDU_PRO",
        "SUBSCRIPTION_TIER_EDU_EMERGING",
        "SUBSCRIPTION_TIER_EDU_PRO_EMERGING",
        "SUBSCRIPTION_TIER_FRONTLINE_STARTER",
        "SUBSCRIPTION_TIER_CONSUMPTION_ONLY",
        "SUBSCRIPTION_TIER_EDU_GOV_EMERGING",
    ]
    searchAddOns: _list[
        typing.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FactChunk(typing.TypedDict, total=False):
    chunkText: str
    domain: str
    index: int
    source: str
    sourceMetadata: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Feedback(typing.TypedDict, total=False):
    comment: str
    componentVersion: str
    conversationInfo: GoogleCloudDiscoveryengineV1FeedbackConversationInfo
    dataTermsAccepted: bool
    feedbackSource: typing.Literal[
        "FEEDBACK_SOURCE_UNSPECIFIED",
        "GOOGLE_CONSOLE",
        "GOOGLE_WIDGET",
        "GOOGLE_WEBAPP",
        "GOOGLE_AGENTSPACE_MOBILE",
    ]
    feedbackType: typing.Literal["FEEDBACK_TYPE_UNSPECIFIED", "LIKE", "DISLIKE"]
    llmModelVersion: str
    reasons: _list[
        typing.Literal[
            "REASON_UNSPECIFIED",
            "INACCURATE_RESPONSE",
            "NOT_RELEVANT",
            "INCOMPREHENSIVE",
            "OFFENSIVE_OR_UNSAFE",
            "FORMAT_AND_STYLES",
            "BAD_CITATION",
            "CANVAS_NOT_GENERATED",
            "CANVAS_QUALITY_BAD",
            "CANVAS_EXPORT_FAILED",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FeedbackConversationInfo(
    typing.TypedDict, total=False
):
    answerQueryToken: str
    assistToken: str
    query: GoogleCloudDiscoveryengineV1Query
    questionIndex: int
    session: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FetchSitemapsResponse(typing.TypedDict, total=False):
    sitemapsMetadata: _list[
        GoogleCloudDiscoveryengineV1FetchSitemapsResponseSitemapMetadata
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FetchSitemapsResponseSitemapMetadata(
    typing.TypedDict, total=False
):
    sitemap: GoogleCloudDiscoveryengineV1Sitemap

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FhirStoreSource(typing.TypedDict, total=False):
    fhirStore: str
    gcsStagingDir: str
    resourceTypes: _list[str]
    updateFromLatestPredefinedSchema: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FirestoreSource(typing.TypedDict, total=False):
    collectionId: str
    databaseId: str
    gcsStagingDir: str
    projectId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GcsSource(typing.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GroundingFact(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    factText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1HealthcareFhirConfig(typing.TypedDict, total=False):
    enableConfigurableSchema: bool
    enableStaticIndexingForBatchIngestion: bool
    initialFilterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1IdentityMappingEntry(typing.TypedDict, total=False):
    externalIdentity: str
    externalIdentityName: str
    groupId: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1IdentityMappingEntryOperationMetadata(
    typing.TypedDict, total=False
):
    failureCount: str
    successCount: str
    totalCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1IdentityMappingStore(typing.TypedDict, total=False):
    cmekConfig: GoogleCloudDiscoveryengineV1CmekConfig
    kmsKeyName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1IdentityScheduleConfig(typing.TypedDict, total=False):
    nextSyncTime: GoogleTypeDateTime
    refreshInterval: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1IdpConfig(typing.TypedDict, total=False):
    externalIdpConfig: GoogleCloudDiscoveryengineV1IdpConfigExternalIdpConfig
    idpType: typing.Literal["IDP_TYPE_UNSPECIFIED", "GSUITE", "THIRD_PARTY"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1IdpConfigExternalIdpConfig(
    typing.TypedDict, total=False
):
    workforcePoolName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequest(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1BigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequestInlineSource(
    typing.TypedDict, total=False
):
    suggestions: _list[GoogleCloudDiscoveryengineV1CompletionSuggestion]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsRequest(typing.TypedDict, total=False):
    alloyDbSource: GoogleCloudDiscoveryengineV1AlloyDbSource
    autoGenerateIds: bool
    bigquerySource: GoogleCloudDiscoveryengineV1BigQuerySource
    bigtableSource: GoogleCloudDiscoveryengineV1BigtableSource
    cloudSqlSource: GoogleCloudDiscoveryengineV1CloudSqlSource
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    fhirStoreSource: GoogleCloudDiscoveryengineV1FhirStoreSource
    firestoreSource: GoogleCloudDiscoveryengineV1FirestoreSource
    forceRefreshContent: bool
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    idField: str
    inlineSource: GoogleCloudDiscoveryengineV1ImportDocumentsRequestInlineSource
    reconciliationMode: typing.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    spannerSource: GoogleCloudDiscoveryengineV1SpannerSource
    updateMask: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsRequestInlineSource(
    typing.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1Document]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportErrorConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportIdentityMappingsRequest(
    typing.TypedDict, total=False
):
    inlineSource: GoogleCloudDiscoveryengineV1ImportIdentityMappingsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportIdentityMappingsRequestInlineSource(
    typing.TypedDict, total=False
):
    identityMappingEntries: _list[GoogleCloudDiscoveryengineV1IdentityMappingEntry]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportIdentityMappingsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequest(
    typing.TypedDict, total=False
):
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequestInlineSource(
    typing.TypedDict, total=False
):
    entries: _list[GoogleCloudDiscoveryengineV1SuggestionDenyListEntry]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsRequest(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1BigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: GoogleCloudDiscoveryengineV1ImportUserEventsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsRequestInlineSource(
    typing.TypedDict, total=False
):
    userEvents: _list[GoogleCloudDiscoveryengineV1UserEvent]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Interval(typing.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1LicenseConfig(typing.TypedDict, total=False):
    autoRenew: bool
    earlyTerminated: bool
    earlyTerminationDate: GoogleTypeDate
    endDate: GoogleTypeDate
    freeTrial: bool
    geminiBundle: bool
    lastUserUpdateTime: str
    licenseCount: str
    name: str
    startDate: GoogleTypeDate
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "EXPIRED",
        "NOT_STARTED",
        "WITHDRAWN",
        "DEACTIVATING",
    ]
    subscriptionTerm: typing.Literal[
        "SUBSCRIPTION_TERM_UNSPECIFIED",
        "SUBSCRIPTION_TERM_ONE_MONTH",
        "SUBSCRIPTION_TERM_ONE_YEAR",
        "SUBSCRIPTION_TERM_THREE_YEARS",
        "SUBSCRIPTION_TERM_CUSTOM",
    ]
    subscriptionTier: typing.Literal[
        "SUBSCRIPTION_TIER_UNSPECIFIED",
        "SUBSCRIPTION_TIER_SEARCH",
        "SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT",
        "SUBSCRIPTION_TIER_NOTEBOOK_LM",
        "SUBSCRIPTION_TIER_FRONTLINE_WORKER",
        "SUBSCRIPTION_TIER_AGENTSPACE_STARTER",
        "SUBSCRIPTION_TIER_AGENTSPACE_BUSINESS",
        "SUBSCRIPTION_TIER_ENTERPRISE",
        "SUBSCRIPTION_TIER_ENTERPRISE_EMERGING",
        "SUBSCRIPTION_TIER_EDU",
        "SUBSCRIPTION_TIER_EDU_PRO",
        "SUBSCRIPTION_TIER_EDU_EMERGING",
        "SUBSCRIPTION_TIER_EDU_PRO_EMERGING",
        "SUBSCRIPTION_TIER_FRONTLINE_STARTER",
        "SUBSCRIPTION_TIER_CONSUMPTION_ONLY",
        "SUBSCRIPTION_TIER_EDU_GOV_EMERGING",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1LicenseConfigUsageStats(
    typing.TypedDict, total=False
):
    licenseConfig: str
    usedLicenseCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListAssistantsResponse(typing.TypedDict, total=False):
    assistants: _list[GoogleCloudDiscoveryengineV1Assistant]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListCmekConfigsResponse(
    typing.TypedDict, total=False
):
    cmekConfigs: _list[GoogleCloudDiscoveryengineV1CmekConfig]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListControlsResponse(typing.TypedDict, total=False):
    controls: _list[GoogleCloudDiscoveryengineV1Control]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListConversationsResponse(
    typing.TypedDict, total=False
):
    conversations: _list[GoogleCloudDiscoveryengineV1Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListCustomModelsResponse(
    typing.TypedDict, total=False
):
    models: _list[GoogleCloudDiscoveryengineV1CustomTuningModel]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListDataStoresResponse(typing.TypedDict, total=False):
    dataStores: _list[GoogleCloudDiscoveryengineV1DataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListDocumentsResponse(typing.TypedDict, total=False):
    documents: _list[GoogleCloudDiscoveryengineV1Document]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListEnginesResponse(typing.TypedDict, total=False):
    engines: _list[GoogleCloudDiscoveryengineV1Engine]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListIdentityMappingStoresResponse(
    typing.TypedDict, total=False
):
    identityMappingStores: _list[GoogleCloudDiscoveryengineV1IdentityMappingStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListIdentityMappingsResponse(
    typing.TypedDict, total=False
):
    identityMappingEntries: _list[GoogleCloudDiscoveryengineV1IdentityMappingEntry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListLicenseConfigsResponse(
    typing.TypedDict, total=False
):
    licenseConfigs: _list[GoogleCloudDiscoveryengineV1LicenseConfig]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListLicenseConfigsUsageStatsResponse(
    typing.TypedDict, total=False
):
    licenseConfigUsageStats: _list[GoogleCloudDiscoveryengineV1LicenseConfigUsageStats]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListSchemasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[GoogleCloudDiscoveryengineV1Schema]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListServingConfigsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudDiscoveryengineV1ServingConfig]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[GoogleCloudDiscoveryengineV1Session]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListTargetSitesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListUserLicensesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    userLicenses: _list[GoogleCloudDiscoveryengineV1UserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1MediaInfo(typing.TypedDict, total=False):
    mediaProgressDuration: str
    mediaProgressPercentage: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1NaturalLanguageQueryUnderstandingConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ObservabilityConfig(typing.TypedDict, total=False):
    observabilityEnabled: bool
    sensitiveLoggingEnabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PageInfo(typing.TypedDict, total=False):
    pageCategory: str
    pageviewId: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PanelInfo(typing.TypedDict, total=False):
    displayName: str
    documents: _list[GoogleCloudDiscoveryengineV1DocumentInfo]
    panelId: str
    panelPosition: int
    totalPanels: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Principal(typing.TypedDict, total=False):
    externalEntityId: str
    groupId: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Project(typing.TypedDict, total=False):
    configurableBillingStatus: (
        GoogleCloudDiscoveryengineV1ProjectConfigurableBillingStatus
    )
    createTime: str
    customerProvidedConfig: GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfig
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectConfigurableBillingStatus(
    typing.TypedDict, total=False
):
    agentSearchTokenSubscriptionStatuses: _list[
        GoogleCloudDiscoveryengineV1ProjectConfigurableBillingStatusAgentSearchTokenSubscriptionStatus
    ]
    effectiveIndexingCoreThreshold: str
    effectiveSearchQpmThreshold: str
    indexingCoreThresholdNextUpdateTime: str
    searchQpmThresholdNextUpdateTime: str
    startTime: str
    terminateTime: str
    updateType: typing.Literal[
        "UPDATE_TYPE_UNSPECIFIED", "CREATE", "DELETE", "SCALE_UP", "SCALE_DOWN"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectConfigurableBillingStatusAgentSearchTokenSubscriptionStatus(
    typing.TypedDict, total=False
):
    effectiveTpmThreshold: str
    modelVersion: str
    startTime: str
    terminateTime: str
    tpmThresholdNextUpdateTime: str
    updateType: typing.Literal[
        "UPDATE_TYPE_UNSPECIFIED", "CREATE", "DELETE", "SCALE_UP", "SCALE_DOWN"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfig(
    typing.TypedDict, total=False
):
    notebooklmConfig: (
        GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfig
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfig(
    typing.TypedDict, total=False
):
    dataProtectionPolicy: GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicy
    modelArmorConfig: GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfigModelArmorConfig
    observabilityConfig: GoogleCloudDiscoveryengineV1ObservabilityConfig
    optOutNotebookSharing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicy(
    typing.TypedDict, total=False
):
    sensitiveDataProtectionPolicy: GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicySensitiveDataProtectionPolicy

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicySensitiveDataProtectionPolicy(
    typing.TypedDict, total=False
):
    policy: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectCustomerProvidedConfigNotebooklmConfigModelArmorConfig(
    typing.TypedDict, total=False
):
    responseTemplate: str
    userPromptTemplate: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectServiceTerms(typing.TypedDict, total=False):
    acceptTime: str
    declineTime: str
    id: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProvisionProjectMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProvisionProjectRequest(
    typing.TypedDict, total=False
):
    acceptDataUseTerms: bool
    dataUseTermsVersion: str
    saasParams: GoogleCloudDiscoveryengineV1ProvisionProjectRequestSaasParams

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProvisionProjectRequestSaasParams(
    typing.TypedDict, total=False
):
    acceptBizQos: bool
    isBiz: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeSucceeded: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsRequest(typing.TypedDict, total=False):
    errorConfig: GoogleCloudDiscoveryengineV1PurgeErrorConfig
    filter: str
    force: bool
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: GoogleCloudDiscoveryengineV1PurgeDocumentsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsRequestInlineSource(
    typing.TypedDict, total=False
):
    documents: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeErrorConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeIdentityMappingsRequest(
    typing.TypedDict, total=False
):
    filter: str
    force: bool
    inlineSource: GoogleCloudDiscoveryengineV1PurgeIdentityMappingsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeIdentityMappingsRequestInlineSource(
    typing.TypedDict, total=False
):
    identityMappingEntries: _list[GoogleCloudDiscoveryengineV1IdentityMappingEntry]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeUserEventsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Query(typing.TypedDict, total=False):
    queryId: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RankRequest(typing.TypedDict, total=False):
    ignoreRecordDetailsInResponse: bool
    model: str
    query: str
    records: _list[GoogleCloudDiscoveryengineV1RankingRecord]
    topN: int
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RankResponse(typing.TypedDict, total=False):
    records: _list[GoogleCloudDiscoveryengineV1RankingRecord]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RankingRecord(typing.TypedDict, total=False):
    content: str
    id: str
    score: float
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecommendRequest(typing.TypedDict, total=False):
    filter: str
    pageSize: int
    params: dict[str, typing.Any]
    userEvent: GoogleCloudDiscoveryengineV1UserEvent
    userLabels: dict[str, typing.Any]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecommendResponse(typing.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudDiscoveryengineV1RecommendResponseRecommendationResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecommendResponseRecommendationResult(
    typing.TypedDict, total=False
):
    document: GoogleCloudDiscoveryengineV1Document
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecrawlUrisRequest(typing.TypedDict, total=False):
    siteCredential: str
    uris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Reply(typing.TypedDict, total=False):
    summary: GoogleCloudDiscoveryengineV1SearchResponseSummary

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RetractLicenseConfigRequest(
    typing.TypedDict, total=False
):
    fullRetract: bool
    licenseConfig: str
    licenseCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RetractLicenseConfigResponse(
    typing.TypedDict, total=False
):
    licenseConfig: GoogleCloudDiscoveryengineV1LicenseConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SafetyRating(typing.TypedDict, total=False):
    blocked: bool
    category: typing.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    probability: typing.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]
    probabilityScore: float
    severity: typing.Literal[
        "HARM_SEVERITY_UNSPECIFIED",
        "HARM_SEVERITY_NEGLIGIBLE",
        "HARM_SEVERITY_LOW",
        "HARM_SEVERITY_MEDIUM",
        "HARM_SEVERITY_HIGH",
    ]
    severityScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Schema(typing.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchInfo(typing.TypedDict, total=False):
    offset: int
    orderBy: str
    searchQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchLinkPromotion(typing.TypedDict, total=False):
    description: str
    document: str
    enabled: bool
    imageUri: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequest(typing.TypedDict, total=False):
    boostSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpec
    crowdingSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestCrowdingSpec]
    customRankingParams: GoogleCloudDiscoveryengineV1SearchRequestCustomRankingParams
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestDataStoreSpec]
    displaySpec: GoogleCloudDiscoveryengineV1SearchRequestDisplaySpec
    entity: str
    facetSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1SearchRequestImageQuery
    languageCode: str
    naturalLanguageQueryUnderstandingSpec: (
        GoogleCloudDiscoveryengineV1SearchRequestNaturalLanguageQueryUnderstandingSpec
    )
    numResultsPerDataStore: int
    offset: int
    oneBoxPageSize: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1SearchRequestQueryExpansionSpec
    rankingExpression: str
    rankingExpressionBackend: typing.Literal[
        "RANKING_EXPRESSION_BACKEND_UNSPECIFIED",
        "BYOE",
        "CLEARBOX",
        "RANK_BY_EMBEDDING",
        "RANK_BY_FORMULA",
    ]
    relevanceFilterSpec: GoogleCloudDiscoveryengineV1SearchRequestRelevanceFilterSpec
    relevanceScoreSpec: GoogleCloudDiscoveryengineV1SearchRequestRelevanceScoreSpec
    relevanceThreshold: typing.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    safeSearch: bool
    searchAsYouTypeSpec: GoogleCloudDiscoveryengineV1SearchRequestSearchAsYouTypeSpec
    session: str
    sessionSpec: GoogleCloudDiscoveryengineV1SearchRequestSessionSpec
    spellCorrectionSpec: GoogleCloudDiscoveryengineV1SearchRequestSpellCorrectionSpec
    userInfo: GoogleCloudDiscoveryengineV1UserInfo
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpec(typing.TypedDict, total=False):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpec(
    typing.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: (
        GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecExtractiveContentSpec
    )
    searchResultMode: typing.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    snippetSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSnippetSpec
    summarySpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecChunkSpec(
    typing.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecExtractiveContentSpec(
    typing.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSnippetSpec(
    typing.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpec(
    typing.TypedDict, total=False
):
    ignoreAdversarialQuery: bool
    ignoreJailBreakingQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: (
        GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpecModelSpec
    )
    summaryResultCount: int
    useSemanticChunks: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpecModelPromptSpec(
    typing.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpecModelSpec(
    typing.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestCrowdingSpec(
    typing.TypedDict, total=False
):
    field: str
    maxCount: int
    mode: typing.Literal[
        "MODE_UNSPECIFIED", "DROP_CROWDED_RESULTS", "DEMOTE_CROWDED_RESULTS_TO_END"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestCustomRankingParams(
    typing.TypedDict, total=False
):
    expressionsToPrecompute: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestDataStoreSpec(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpec
    customSearchOperators: str
    dataStore: str
    filter: str
    numResults: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestDisplaySpec(
    typing.TypedDict, total=False
):
    matchHighlightingCondition: typing.Literal[
        "MATCH_HIGHLIGHTING_CONDITION_UNSPECIFIED",
        "MATCH_HIGHLIGHTING_DISABLED",
        "MATCH_HIGHLIGHTING_ENABLED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestFacetSpec(typing.TypedDict, total=False):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1SearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestFacetSpecFacetKey(
    typing.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudDiscoveryengineV1Interval]
    key: str
    orderBy: str
    prefixes: _list[str]
    restrictedValues: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestImageQuery(
    typing.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestNaturalLanguageQueryUnderstandingSpec(
    typing.TypedDict, total=False
):
    allowedFieldNames: _list[str]
    extractedFilterBehavior: typing.Literal[
        "EXTRACTED_FILTER_BEHAVIOR_UNSPECIFIED", "HARD_FILTER", "SOFT_BOOST"
    ]
    filterExtractionCondition: typing.Literal[
        "CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    geoSearchQueryDetectionFieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestQueryExpansionSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestRelevanceFilterSpec(
    typing.TypedDict, total=False
):
    keywordSearchThreshold: GoogleCloudDiscoveryengineV1SearchRequestRelevanceFilterSpecRelevanceThresholdSpec
    semanticSearchThreshold: GoogleCloudDiscoveryengineV1SearchRequestRelevanceFilterSpecRelevanceThresholdSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestRelevanceFilterSpecRelevanceThresholdSpec(
    typing.TypedDict, total=False
):
    relevanceThreshold: typing.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    semanticRelevanceThreshold: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestRelevanceScoreSpec(
    typing.TypedDict, total=False
):
    returnRelevanceScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestSearchAsYouTypeSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestSessionSpec(
    typing.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestSpellCorrectionSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponse(typing.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    correctedQuery: str
    facets: _list[GoogleCloudDiscoveryengineV1SearchResponseFacet]
    naturalLanguageQueryUnderstandingInfo: (
        GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfo
    )
    nextPageToken: str
    queryExpansionInfo: GoogleCloudDiscoveryengineV1SearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudDiscoveryengineV1SearchResponseSearchResult]
    searchLinkPromotions: _list[GoogleCloudDiscoveryengineV1SearchLinkPromotion]
    semanticState: typing.Literal["SEMANTIC_STATE_UNSPECIFIED", "DISABLED", "ENABLED"]
    sessionInfo: GoogleCloudDiscoveryengineV1SearchResponseSessionInfo
    summary: GoogleCloudDiscoveryengineV1SearchResponseSummary
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseFacet(typing.TypedDict, total=False):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudDiscoveryengineV1SearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseFacetFacetValue(
    typing.TypedDict, total=False
):
    count: str
    interval: GoogleCloudDiscoveryengineV1Interval
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfo(
    typing.TypedDict, total=False
):
    classifiedIntents: _list[str]
    extractedFilters: str
    rewrittenQuery: str
    structuredExtractedFilter: GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilter

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilter(
    typing.TypedDict, total=False
):
    expression: GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterAndExpression(
    typing.TypedDict, total=False
):
    expressions: _list[
        GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression(
    typing.TypedDict, total=False
):
    andExpr: GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterAndExpression
    geolocationConstraint: GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterGeolocationConstraint
    numberConstraint: GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterNumberConstraint
    orExpr: GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterOrExpression
    stringConstraint: GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterStringConstraint

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterGeolocationConstraint(
    typing.TypedDict, total=False
):
    address: str
    fieldName: str
    latitude: float
    longitude: float
    radiusInMeters: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterNumberConstraint(
    typing.TypedDict, total=False
):
    comparison: typing.Literal[
        "COMPARISON_UNSPECIFIED",
        "EQUALS",
        "LESS_THAN_EQUALS",
        "LESS_THAN",
        "GREATER_THAN_EQUALS",
        "GREATER_THAN",
    ]
    fieldName: str
    querySegment: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterOrExpression(
    typing.TypedDict, total=False
):
    expressions: _list[
        GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterStringConstraint(
    typing.TypedDict, total=False
):
    fieldName: str
    querySegment: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseQueryExpansionInfo(
    typing.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSearchResult(
    typing.TypedDict, total=False
):
    chunk: GoogleCloudDiscoveryengineV1Chunk
    document: GoogleCloudDiscoveryengineV1Document
    id: str
    modelScores: dict[str, typing.Any]
    rankSignals: GoogleCloudDiscoveryengineV1SearchResponseSearchResultRankSignals
    retrievalSignals: (
        GoogleCloudDiscoveryengineV1SearchResponseSearchResultRetrievalSignals
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSearchResultRankSignals(
    typing.TypedDict, total=False
):
    boostingFactor: float
    customSignals: _list[
        GoogleCloudDiscoveryengineV1SearchResponseSearchResultRankSignalsCustomSignal
    ]
    defaultRank: float
    documentAge: float
    keywordSimilarityScore: float
    pctrRank: float
    precomputedExpressionValues: _list[float]
    relevanceScore: float
    semanticSimilarityScore: float
    topicalityRank: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSearchResultRankSignalsCustomSignal(
    typing.TypedDict, total=False
):
    name: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSearchResultRetrievalSignals(
    typing.TypedDict, total=False
):
    retrievalSources: _list[
        typing.Literal[
            "RETRIEVAL_SOURCE_UNSPECIFIED", "KEYWORD_SEARCH", "SEMANTIC_SEARCH"
        ]
    ]
    semanticRelevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSessionInfo(
    typing.TypedDict, total=False
):
    name: str
    queryId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummary(typing.TypedDict, total=False):
    safetyAttributes: GoogleCloudDiscoveryengineV1SearchResponseSummarySafetyAttributes
    summarySkippedReasons: _list[
        typing.Literal[
            "SUMMARY_SKIPPED_REASON_UNSPECIFIED",
            "ADVERSARIAL_QUERY_IGNORED",
            "NON_SUMMARY_SEEKING_QUERY_IGNORED",
            "OUT_OF_DOMAIN_QUERY_IGNORED",
            "POTENTIAL_POLICY_VIOLATION",
            "LLM_ADDON_NOT_ENABLED",
            "NO_RELEVANT_CONTENT",
            "JAIL_BREAKING_QUERY_IGNORED",
            "CUSTOMER_POLICY_VIOLATION",
            "NON_SUMMARY_SEEKING_QUERY_IGNORED_V2",
            "TIME_OUT",
        ]
    ]
    summaryText: str
    summaryWithMetadata: (
        GoogleCloudDiscoveryengineV1SearchResponseSummarySummaryWithMetadata
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryCitation(
    typing.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationMetadata(
    typing.TypedDict, total=False
):
    citations: _list[GoogleCloudDiscoveryengineV1SearchResponseSummaryCitation]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationSource(
    typing.TypedDict, total=False
):
    referenceIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryReference(
    typing.TypedDict, total=False
):
    chunkContents: _list[
        GoogleCloudDiscoveryengineV1SearchResponseSummaryReferenceChunkContent
    ]
    document: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryReferenceChunkContent(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummarySafetyAttributes(
    typing.TypedDict, total=False
):
    categories: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummarySummaryWithMetadata(
    typing.TypedDict, total=False
):
    citationMetadata: GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationMetadata
    references: _list[GoogleCloudDiscoveryengineV1SearchResponseSummaryReference]
    summary: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ServingConfig(typing.TypedDict, total=False):
    answerGenerationSpec: GoogleCloudDiscoveryengineV1AnswerGenerationSpec
    boostControlIds: _list[str]
    createTime: str
    displayName: str
    dissociateControlIds: _list[str]
    diversityLevel: str
    filterControlIds: _list[str]
    genericConfig: GoogleCloudDiscoveryengineV1ServingConfigGenericConfig
    ignoreControlIds: _list[str]
    mediaConfig: GoogleCloudDiscoveryengineV1ServingConfigMediaConfig
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    promoteControlIds: _list[str]
    rankingExpression: str
    redirectControlIds: _list[str]
    replacementControlIds: _list[str]
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    synonymsControlIds: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ServingConfigGenericConfig(
    typing.TypedDict, total=False
):
    contentSearchSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ServingConfigMediaConfig(
    typing.TypedDict, total=False
):
    contentFreshnessCutoffDays: int
    contentWatchedPercentageThreshold: float
    contentWatchedSecondsThreshold: float
    demoteContentWatchedPastDays: int
    demotionEventType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Session(typing.TypedDict, total=False):
    displayName: str
    endTime: str
    isPinned: bool
    labels: _list[str]
    name: str
    pendingAsyncAssistOperationId: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS"]
    turns: _list[GoogleCloudDiscoveryengineV1SessionTurn]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SessionTurn(typing.TypedDict, total=False):
    answer: str
    detailedAnswer: GoogleCloudDiscoveryengineV1Answer
    detailedAssistAnswer: GoogleCloudDiscoveryengineV1AssistAnswer
    live: bool
    query: GoogleCloudDiscoveryengineV1Query
    queryConfig: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SetUpDataConnectorMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SetUpDataConnectorRequest(
    typing.TypedDict, total=False
):
    collectionDisplayName: str
    collectionId: str
    dataConnector: GoogleCloudDiscoveryengineV1DataConnector

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SingleRegionKey(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SiteSearchEngine(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SiteVerificationInfo(typing.TypedDict, total=False):
    siteVerificationState: typing.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Sitemap(typing.TypedDict, total=False):
    createTime: str
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SpannerSource(typing.TypedDict, total=False):
    databaseId: str
    enableDataBoost: bool
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistRequest(typing.TypedDict, total=False):
    generationSpec: GoogleCloudDiscoveryengineV1StreamAssistRequestGenerationSpec
    query: GoogleCloudDiscoveryengineV1Query
    session: str
    toolsSpec: GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpec
    userMetadata: GoogleCloudDiscoveryengineV1AssistUserMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistRequestGenerationSpec(
    typing.TypedDict, total=False
):
    modelId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpec(
    typing.TypedDict, total=False
):
    imageGenerationSpec: (
        GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecImageGenerationSpec
    )
    vertexAiSearchSpec: (
        GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecVertexAiSearchSpec
    )
    videoGenerationSpec: (
        GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecVideoGenerationSpec
    )
    webGroundingSpec: (
        GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecWebGroundingSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecImageGenerationSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecVertexAiSearchSpec(
    typing.TypedDict, total=False
):
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestDataStoreSpec]
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecVideoGenerationSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistRequestToolsSpecWebGroundingSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistResponse(typing.TypedDict, total=False):
    answer: GoogleCloudDiscoveryengineV1AssistAnswer
    assistToken: str
    connectorAuthErrors: _list[
        GoogleCloudDiscoveryengineV1StreamAssistResponseConnectorAuthError
    ]
    invocationTools: _list[str]
    invokedSkills: _list[GoogleCloudDiscoveryengineV1StreamAssistResponseInvokedSkill]
    sessionInfo: GoogleCloudDiscoveryengineV1StreamAssistResponseSessionInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistResponseConnectorAuthError(
    typing.TypedDict, total=False
):
    dataConnector: str
    errorMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistResponseInvokedSkill(
    typing.TypedDict, total=False
):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1StreamAssistResponseSessionInfo(
    typing.TypedDict, total=False
):
    session: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SuggestionDenyListEntry(
    typing.TypedDict, total=False
):
    blockPhrase: str
    matchOperator: typing.Literal[
        "MATCH_OPERATOR_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSite(typing.TypedDict, total=False):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1TargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing.Literal[
        "INDEXING_STATUS_UNSPECIFIED",
        "PENDING",
        "FAILED",
        "SUCCEEDED",
        "DELETING",
        "CANCELLABLE",
        "CANCELLED",
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1SiteVerificationInfo
    type: typing.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSiteFailureReason(
    typing.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1TargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSiteFailureReasonQuotaFailure(
    typing.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Tenant(typing.TypedDict, total=False):
    displayName: str
    id: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TextInput(typing.TypedDict, total=False):
    context: GoogleCloudDiscoveryengineV1ConversationContext
    input: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelRequest(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    gcsTrainingInput: (
        GoogleCloudDiscoveryengineV1TrainCustomModelRequestGcsTrainingInput
    )
    modelId: str
    modelType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelRequestGcsTrainingInput(
    typing.TypedDict, total=False
):
    corpusDataPath: str
    queryDataPath: str
    testDataPath: str
    trainDataPath: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TransactionInfo(typing.TypedDict, total=False):
    cost: float
    currency: str
    discountValue: float
    tax: float
    transactionId: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateCmekConfigMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateSchemaMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UserEvent(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    attributionToken: str
    completionInfo: GoogleCloudDiscoveryengineV1CompletionInfo
    conversionType: str
    dataStore: str
    directUserRequest: bool
    documents: _list[GoogleCloudDiscoveryengineV1DocumentInfo]
    engine: str
    entity: str
    eventTime: str
    eventType: str
    feedback: GoogleCloudDiscoveryengineV1Feedback
    filter: str
    mediaInfo: GoogleCloudDiscoveryengineV1MediaInfo
    pageInfo: GoogleCloudDiscoveryengineV1PageInfo
    panel: GoogleCloudDiscoveryengineV1PanelInfo
    panels: _list[GoogleCloudDiscoveryengineV1PanelInfo]
    promotionIds: _list[str]
    searchInfo: GoogleCloudDiscoveryengineV1SearchInfo
    sessionId: str
    tagIds: _list[str]
    transactionInfo: GoogleCloudDiscoveryengineV1TransactionInfo
    userInfo: GoogleCloudDiscoveryengineV1UserInfo
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UserInfo(typing.TypedDict, total=False):
    preciseLocation: GoogleCloudDiscoveryengineV1UserInfoPreciseLocation
    timeZone: str
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UserInfoPreciseLocation(
    typing.TypedDict, total=False
):
    address: str
    point: GoogleTypeLatLng

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UserLicense(typing.TypedDict, total=False):
    createTime: str
    lastLoginTime: str
    licenseAssignmentState: typing.Literal[
        "LICENSE_ASSIGNMENT_STATE_UNSPECIFIED",
        "ASSIGNED",
        "UNASSIGNED",
        "NO_LICENSE",
        "NO_LICENSE_ATTEMPTED_LOGIN",
        "BLOCKED",
    ]
    licenseConfig: str
    updateTime: str
    userPrincipal: str
    userProfile: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UserStore(typing.TypedDict, total=False):
    defaultLicenseConfig: str
    displayName: str
    enableExpiredLicenseAutoUpdate: bool
    enableLicenseAutoRegister: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfig(typing.TypedDict, total=False):
    accessSettings: GoogleCloudDiscoveryengineV1WidgetConfigAccessSettings
    allowPublicAccess: bool
    allowlistedDomains: _list[str]
    assistantSettings: GoogleCloudDiscoveryengineV1WidgetConfigAssistantSettings
    batchAuthStatuses: _list[GoogleCloudDiscoveryengineV1WidgetConfigBatchAuthStatus]
    collectionComponents: _list[
        GoogleCloudDiscoveryengineV1WidgetConfigCollectionComponent
    ]
    configId: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpec
    createTime: str
    customerProvidedConfig: (
        GoogleCloudDiscoveryengineV1WidgetConfigCustomerProvidedConfig
    )
    dataStoreType: typing.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED",
        "SITE_SEARCH",
        "STRUCTURED",
        "UNSTRUCTURED",
        "BLENDED",
    ]
    dataStoreUiConfigs: _list[GoogleCloudDiscoveryengineV1WidgetConfigDataStoreUiConfig]
    defaultSearchRequestOrderBy: str
    displayName: str
    enableAutocomplete: bool
    enableConversationalSearch: bool
    enablePrivateKnowledgeGraph: bool
    enableQualityFeedback: bool
    enableResultScore: bool
    enableSafeSearch: bool
    enableSearchAsYouType: bool
    enableSnippetResultSummary: bool
    enableSummarization: bool
    enableWebApp: bool
    facetField: _list[GoogleCloudDiscoveryengineV1WidgetConfigFacetField]
    fieldsUiComponentsMap: dict[str, typing.Any]
    geminiBundle: bool
    homepageSetting: GoogleCloudDiscoveryengineV1WidgetConfigHomepageSetting
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    llmEnabled: bool
    minimumDataTermAccepted: bool
    name: str
    nodes: _list[GoogleCloudDiscoveryengineV1WidgetConfigNode]
    resultDisplayType: typing.Literal[
        "RESULT_DISPLAY_TYPE_UNSPECIFIED", "SNIPPET", "EXTRACTIVE_ANSWER"
    ]
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    uiBranding: GoogleCloudDiscoveryengineV1WidgetConfigUiBrandingSettings
    uiSettings: GoogleCloudDiscoveryengineV1WidgetConfigUiSettings
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigAccessSettings(
    typing.TypedDict, total=False
):
    allowPublicAccess: bool
    allowlistedDomains: _list[str]
    enableWebApp: bool
    languageCode: str
    workforceIdentityPoolProvider: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigAssistantSettings(
    typing.TypedDict, total=False
):
    defaultWebGroundingToggleOff: bool
    disableLocationContext: bool
    googleSearchGroundingEnabled: bool
    webGroundingType: typing.Literal[
        "WEB_GROUNDING_TYPE_UNSPECIFIED",
        "WEB_GROUNDING_TYPE_DISABLED",
        "WEB_GROUNDING_TYPE_GOOGLE_SEARCH",
        "WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigBatchAuthStatus(
    typing.TypedDict, total=False
):
    batchAuthorizationGroup: str
    connectorAuthState: GoogleCloudDiscoveryengineV1WidgetConfigConnectorAuthState
    placeholder: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigCollectionComponent(
    typing.TypedDict, total=False
):
    connectorAuthState: GoogleCloudDiscoveryengineV1WidgetConfigConnectorAuthState
    connectorIconLink: str
    dataSource: str
    dataSourceDisplayName: str
    dataSourceEndUserDisplayName: str
    dataSourceVersion: float
    dataStoreComponents: _list[
        GoogleCloudDiscoveryengineV1WidgetConfigDataStoreComponent
    ]
    displayName: str
    id: str
    isFirstParty: bool
    metadata: GoogleCloudDiscoveryengineV1DataConnectorConnectorMetadata
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigConnectorAuthState(
    typing.TypedDict, total=False
):
    authState: typing.Literal[
        "AUTH_STATE_UNSPECIFIED", "AUTHORIZED", "EXPIRED", "ACTIONS_DISABLED", "NO_AUTH"
    ]
    authorizationUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigCustomerProvidedConfig(
    typing.TypedDict, total=False
):
    customerType: typing.Literal["DEFAULT_CUSTOMER", "GOVERNMENT_CUSTOMER"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigDataStoreComponent(
    typing.TypedDict, total=False
):
    dataStoreConfigType: typing.Literal[
        "DATA_STORE_CONFIG_TYPE_UNSPECIFIED",
        "ALLOW_DB_CONFIG",
        "THIRD_PARTY_OAUTH_CONFIG",
        "NOTEBOOKLM_CONFIG",
    ]
    displayName: str
    entityName: str
    id: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigDataStoreUiConfig(
    typing.TypedDict, total=False
):
    facetField: _list[GoogleCloudDiscoveryengineV1WidgetConfigFacetField]
    fieldsUiComponentsMap: dict[str, typing.Any]
    id: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigFacetField(typing.TypedDict, total=False):
    displayName: str
    field: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigHomepageSetting(
    typing.TypedDict, total=False
):
    shortcuts: _list[GoogleCloudDiscoveryengineV1WidgetConfigHomepageSettingShortcut]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigHomepageSettingShortcut(
    typing.TypedDict, total=False
):
    destinationUri: str
    icon: GoogleCloudDiscoveryengineV1WidgetConfigImage
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigImage(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigNode(typing.TypedDict, total=False):
    description: str
    displayName: str
    iconUrl: str
    outputSchema: dict[str, typing.Any]
    parameterSchema: dict[str, typing.Any]
    type: typing.Literal["TYPE_UNSPECIFIED", "TRIGGER", "FLOW", "CONNECTOR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigUIComponentField(
    typing.TypedDict, total=False
):
    deviceVisibility: _list[
        typing.Literal["DEVICE_VISIBILITY_UNSPECIFIED", "MOBILE", "DESKTOP"]
    ]
    displayTemplate: str
    field: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigUiBrandingSettings(
    typing.TypedDict, total=False
):
    logo: GoogleCloudDiscoveryengineV1WidgetConfigImage

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigUiSettings(typing.TypedDict, total=False):
    dataStoreUiConfigs: _list[GoogleCloudDiscoveryengineV1WidgetConfigDataStoreUiConfig]
    defaultSearchRequestOrderBy: str
    disableUserEventsCollection: bool
    enableAutocomplete: bool
    enableCreateAgentButton: bool
    enablePeopleSearch: bool
    enableQualityFeedback: bool
    enableSafeSearch: bool
    enableSearchAsYouType: bool
    enableVisualContentSummary: bool
    features: dict[str, typing.Any]
    generativeAnswerConfig: (
        GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsGenerativeAnswerConfig
    )
    googleDrivePickerEnabled: bool
    interactionType: typing.Literal[
        "INTERACTION_TYPE_UNSPECIFIED",
        "SEARCH_ONLY",
        "SEARCH_WITH_ANSWER",
        "SEARCH_WITH_FOLLOW_UPS",
    ]
    modelConfigInfo: GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsModelConfigInfo
    modelConfigs: dict[str, typing.Any]
    onedrivePickerEnabled: bool
    resultDescriptionType: typing.Literal[
        "RESULT_DISPLAY_TYPE_UNSPECIFIED", "SNIPPET", "EXTRACTIVE_ANSWER"
    ]
    sourceAdminDisplayNameEnabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsGenerativeAnswerConfig(
    typing.TypedDict, total=False
):
    disableRelatedQuestions: bool
    ignoreAdversarialQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonAnswerSeekingQuery: bool
    imageSource: typing.Literal[
        "IMAGE_SOURCE_UNSPECIFIED",
        "ALL_AVAILABLE_SOURCES",
        "CORPUS_IMAGE_ONLY",
        "FIGURE_GENERATION_ONLY",
    ]
    languageCode: str
    maxRephraseSteps: int
    modelPromptPreamble: str
    modelVersion: str
    resultCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsModelConfigInfo(
    typing.TypedDict, total=False
):
    defaultModelId: str
    resolvedModels: _list[
        GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsModelConfigInfoResolvedModel
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsModelConfigInfoResolvedModel(
    typing.TypedDict, total=False
):
    adminView: GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsModelConfigInfoResolvedModelAdminView
    description: str
    displayName: str
    icon: str
    isPreview: bool
    label: str
    modelId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WidgetConfigUiSettingsModelConfigInfoResolvedModelAdminView(
    typing.TypedDict, total=False
):
    adminOverridable: bool
    enabledByDefault: bool
    regions: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WorkspaceConfig(typing.TypedDict, total=False):
    dasherCustomerId: str
    superAdminEmailAddress: str
    superAdminServiceAccount: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "GOOGLE_DRIVE",
        "GOOGLE_MAIL",
        "GOOGLE_SITES",
        "GOOGLE_CALENDAR",
        "GOOGLE_CHAT",
        "GOOGLE_GROUPS",
        "GOOGLE_KEEP",
        "GOOGLE_PEOPLE",
        "GOOGLE_WORKSPACE",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAclConfig(typing.TypedDict, total=False):
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaActionConfig(typing.TypedDict, total=False):
    actionParams: dict[str, typing.Any]
    createBapConnection: bool
    isActionConfigured: bool
    jsonActionParams: str
    serviceName: str
    useStaticSecrets: bool
    userDefinedScopesMapping: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaActionConfigScopeList(
    typing.TypedDict, total=False
):
    scopes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAddPatientFilterRequest(
    typing.TypedDict, total=False
):
    dataStore: str
    filterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedSiteSearchConfig(
    typing.TypedDict, total=False
):
    disableAutomaticRefresh: bool
    disableInitialIndex: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAgentGatewaySetting(
    typing.TypedDict, total=False
):
    defaultEgressAgentGateway: (
        GoogleCloudDiscoveryengineV1alphaAgentGatewaySettingAgentGatewayReference
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAgentGatewaySettingAgentGatewayReference(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlertPolicyConfig(typing.TypedDict, total=False):
    alertEnrollments: _list[
        GoogleCloudDiscoveryengineV1alphaAlertPolicyConfigAlertEnrollment
    ]
    alertPolicyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlertPolicyConfigAlertEnrollment(
    typing.TypedDict, total=False
):
    alertId: str
    enrollState: typing.Literal["ENROLL_STATES_UNSPECIFIED", "ENROLLED", "DECLINED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlertPolicyResourceConfig(
    typing.TypedDict, total=False
):
    alertEnrollments: _list[
        GoogleCloudDiscoveryengineV1alphaAlertPolicyResourceConfigAlertEnrollment
    ]
    alertPolicy: str
    contactDetails: _list[GoogleCloudDiscoveryengineV1alphaContactDetails]
    languageCode: str
    regionCode: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlertPolicyResourceConfigAlertEnrollment(
    typing.TypedDict, total=False
):
    alertId: str
    enrollState: typing.Literal["ENROLL_STATE_UNSPECIFIED", "ENROLLED", "DECLINED"]
    notificationParams: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationInsights(
    typing.TypedDict, total=False
):
    insights: _list[
        GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationInsightsAlphaEvolveEvaluationInsight
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationInsightsAlphaEvolveEvaluationInsight(
    typing.TypedDict, total=False
):
    label: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationScores(
    typing.TypedDict, total=False
):
    scores: _list[
        GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationScoresAlphaEvolveEvaluationScore
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationScoresAlphaEvolveEvaluationScore(
    typing.TypedDict, total=False
):
    metric: str
    score: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperiment(
    typing.TypedDict, total=False
):
    config: GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfig
    createTime: str
    initialAlphaEvolveProgram: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "PAUSED", "COMPLETED", "FAILED"
    ]
    stats: GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentStats

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfig(
    typing.TypedDict, total=False
):
    evolutionSettings: (
        GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigEvolutionSettings
    )
    generationSettings: (
        GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigGenerationSettings
    )
    problemDescription: str
    programLanguage: str
    runSettings: GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigRunSettings
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigEvolutionSettings(
    typing.TypedDict, total=False
):
    parentSamplingConfig: GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigEvolutionSettingsParentSamplingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigEvolutionSettingsParentSamplingConfig(
    typing.TypedDict, total=False
):
    paretoSamplingConfig: GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigEvolutionSettingsParentSamplingConfigParetoSamplingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigEvolutionSettingsParentSamplingConfigParetoSamplingConfig(
    typing.TypedDict, total=False
):
    paretoSamplingProbability: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigGenerationSettings(
    typing.TypedDict, total=False
):
    context: str
    includeFullProgramInPrompt: bool
    models: _list[
        GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigGenerationSettingsModelConfig
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigGenerationSettingsModelConfig(
    typing.TypedDict, total=False
):
    name: str
    weight: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentConfigRunSettings(
    typing.TypedDict, total=False
):
    concurrency: int
    maxDuration: str
    maxPrograms: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperimentStats(
    typing.TypedDict, total=False
):
    candidatesCount: int
    evaluatedCandidatesCount: int
    inputTokenCount: str
    outputTokenCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgram(
    typing.TypedDict, total=False
):
    content: GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgramContent
    createTime: str
    evaluation: GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgramEvaluation
    lockToken: str
    name: str
    parentPrograms: _list[str]
    state: typing.Literal[
        "PROGRAM_STATE_UNSPECIFIED",
        "INITIALIZED",
        "GENERATING",
        "EVALUATING",
        "COMPLETED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgramContent(
    typing.TypedDict, total=False
):
    description: str
    files: _list[GoogleCloudDiscoveryengineV1alphaAlphaEvolveSourceFile]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgramEvaluation(
    typing.TypedDict, total=False
):
    insights: GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationInsights
    scores: GoogleCloudDiscoveryengineV1alphaAlphaEvolveEvaluationScores

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveSourceFile(
    typing.TypedDict, total=False
):
    content: str
    description: str
    path: str
    programLanguage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswer(typing.TypedDict, total=False):
    answerSkippedReasons: _list[
        typing.Literal[
            "ANSWER_SKIPPED_REASON_UNSPECIFIED",
            "ADVERSARIAL_QUERY_IGNORED",
            "NON_ANSWER_SEEKING_QUERY_IGNORED",
            "OUT_OF_DOMAIN_QUERY_IGNORED",
            "POTENTIAL_POLICY_VIOLATION",
            "NO_RELEVANT_CONTENT",
            "JAIL_BREAKING_QUERY_IGNORED",
            "CUSTOMER_POLICY_VIOLATION",
            "NON_ANSWER_SEEKING_QUERY_IGNORED_V2",
            "LOW_GROUNDED_ANSWER",
            "USER_DEFINED_CLASSIFICATION_QUERY_IGNORED",
            "UNHELPFUL_ANSWER",
        ]
    ]
    answerText: str
    blobAttachments: _list[GoogleCloudDiscoveryengineV1alphaAnswerBlobAttachment]
    citations: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitation]
    completeTime: str
    createTime: str
    groundingScore: float
    groundingSupports: _list[GoogleCloudDiscoveryengineV1alphaAnswerGroundingSupport]
    name: str
    queryUnderstandingInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfo
    )
    references: _list[GoogleCloudDiscoveryengineV1alphaAnswerReference]
    relatedQuestions: _list[str]
    safetyRatings: _list[GoogleCloudDiscoveryengineV1alphaSafetyRating]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "STREAMING"
    ]
    steps: _list[GoogleCloudDiscoveryengineV1alphaAnswerStep]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerBlobAttachment(
    typing.TypedDict, total=False
):
    attributionType: typing.Literal[
        "ATTRIBUTION_TYPE_UNSPECIFIED", "CORPUS", "GENERATED"
    ]
    data: GoogleCloudDiscoveryengineV1alphaAnswerBlobAttachmentBlob

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerBlobAttachmentBlob(
    typing.TypedDict, total=False
):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerCitation(typing.TypedDict, total=False):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerCitationSource(
    typing.TypedDict, total=False
):
    referenceId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerGroundingSupport(
    typing.TypedDict, total=False
):
    endIndex: str
    groundingCheckRequired: bool
    groundingScore: float
    sources: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfo(
    typing.TypedDict, total=False
):
    queryClassificationInfo: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfoQueryClassificationInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfoQueryClassificationInfo(
    typing.TypedDict, total=False
):
    positive: bool
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "ADVERSARIAL_QUERY",
        "NON_ANSWER_SEEKING_QUERY",
        "JAIL_BREAKING_QUERY",
        "NON_ANSWER_SEEKING_QUERY_V2",
        "USER_DEFINED_CLASSIFICATION_QUERY",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReference(typing.TypedDict, total=False):
    chunkInfo: GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfo
    structuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceStructuredDocumentInfo
    )
    unstructuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfo
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfo(
    typing.TypedDict, total=False
):
    blobAttachmentIndexes: _list[str]
    chunk: str
    content: str
    documentMetadata: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfoDocumentMetadata
    )
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfoDocumentMetadata(
    typing.TypedDict, total=False
):
    document: str
    pageIdentifier: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceStructuredDocumentInfo(
    typing.TypedDict, total=False
):
    document: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfo(
    typing.TypedDict, total=False
):
    chunkContents: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfoChunkContent
    ]
    document: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfoChunkContent(
    typing.TypedDict, total=False
):
    blobAttachmentIndexes: _list[str]
    content: str
    pageIdentifier: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStep(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDiscoveryengineV1alphaAnswerStepAction]
    description: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]
    thought: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepAction(typing.TypedDict, total=False):
    observation: GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservation
    searchAction: GoogleCloudDiscoveryengineV1alphaAnswerStepActionSearchAction

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservation(
    typing.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResult(
    typing.TypedDict, total=False
):
    chunkInfo: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultChunkInfo
    ]
    document: str
    snippetInfo: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultSnippetInfo
    ]
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultChunkInfo(
    typing.TypedDict, total=False
):
    chunk: str
    content: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultSnippetInfo(
    typing.TypedDict, total=False
):
    snippet: str
    snippetStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionSearchAction(
    typing.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistAnswer(typing.TypedDict, total=False):
    assistSkippedReasons: _list[
        typing.Literal[
            "ASSIST_SKIPPED_REASON_UNSPECIFIED",
            "NON_ASSIST_SEEKING_QUERY_IGNORED",
            "CUSTOMER_POLICY_VIOLATION",
        ]
    ]
    customerPolicyEnforcementResult: (
        GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResult
    )
    name: str
    replies: _list[GoogleCloudDiscoveryengineV1alphaAssistAnswerReply]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
        "SKIPPED",
        "CANCELLED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResult(
    typing.TypedDict, total=False
):
    policyResults: _list[
        GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResultPolicyEnforcementResult
    ]
    verdict: typing.Literal["UNSPECIFIED", "ALLOW", "BLOCK"]
    violationSource: typing.Literal[
        "VIOLATION_SOURCE_UNSPECIFIED", "SYSTEM", "PROMPT", "ATTACHMENT"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResultBannedPhraseEnforcementResult(
    typing.TypedDict, total=False
):
    bannedPhrases: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResultModelArmorEnforcementResult(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    modelArmorViolation: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResultPolicyEnforcementResult(
    typing.TypedDict, total=False
):
    bannedPhraseEnforcementResult: GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResultBannedPhraseEnforcementResult
    modelArmorEnforcementResult: GoogleCloudDiscoveryengineV1alphaAssistAnswerCustomerPolicyEnforcementResultModelArmorEnforcementResult

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistAnswerReply(typing.TypedDict, total=False):
    createTime: str
    groundedContent: GoogleCloudDiscoveryengineV1alphaAssistantGroundedContent
    replyId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantContent(typing.TypedDict, total=False):
    codeExecutionResult: (
        GoogleCloudDiscoveryengineV1alphaAssistantContentCodeExecutionResult
    )
    executableCode: GoogleCloudDiscoveryengineV1alphaAssistantContentExecutableCode
    file: GoogleCloudDiscoveryengineV1alphaAssistantContentFile
    inlineData: GoogleCloudDiscoveryengineV1alphaAssistantContentBlob
    role: str
    text: str
    thought: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantContentBlob(
    typing.TypedDict, total=False
):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantContentCodeExecutionResult(
    typing.TypedDict, total=False
):
    outcome: typing.Literal[
        "OUTCOME_UNSPECIFIED",
        "OUTCOME_OK",
        "OUTCOME_FAILED",
        "OUTCOME_DEADLINE_EXCEEDED",
    ]
    output: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantContentExecutableCode(
    typing.TypedDict, total=False
):
    code: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantContentFile(
    typing.TypedDict, total=False
):
    fileId: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGroundedContent(
    typing.TypedDict, total=False
):
    citationMetadata: GoogleCloudDiscoveryengineV1alphaCitationMetadata
    content: GoogleCloudDiscoveryengineV1alphaAssistantContent
    textGroundingMetadata: (
        GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadata
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadata(
    typing.TypedDict, total=False
):
    references: _list[
        GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataReference
    ]
    segments: _list[
        GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataSegment
    ]
    visualSegments: _list[
        GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataVisualSegment
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataReference(
    typing.TypedDict, total=False
):
    codeSnippet: str
    content: str
    documentMetadata: GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataReferenceDocumentMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataReferenceDocumentMetadata(
    typing.TypedDict, total=False
):
    document: str
    domain: str
    language: typing.Literal["LANGUAGE_UNSPECIFIED", "PYTHON", "SQL"]
    mimeType: str
    pageIdentifier: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataSegment(
    typing.TypedDict, total=False
):
    endIndex: str
    groundingScore: float
    referenceIndices: _list[int]
    startIndex: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGroundedContentTextGroundingMetadataVisualSegment(
    typing.TypedDict, total=False
):
    contentId: str
    referenceIndices: _list[int]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBAPConfig(typing.TypedDict, total=False):
    enabledActions: _list[str]
    supportedConnectorModes: _list[
        typing.Literal[
            "CONNECTOR_MODE_UNSPECIFIED",
            "DATA_INGESTION",
            "ACTIONS",
            "END_USER_AUTHENTICATION",
        ]
    ]
    toolspecOverride: GoogleCloudDiscoveryengineV1alphaBAPConfigToolspecOverride

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBAPConfigToolspecOverride(
    typing.TypedDict, total=False
):
    baseVersion: str
    tools: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponse(
    typing.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    userLicenses: _list[GoogleCloudDiscoveryengineV1alphaUserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCitation(typing.TypedDict, total=False):
    endIndex: int
    license: str
    publicationDate: GoogleTypeDate
    startIndex: int
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCitationMetadata(typing.TypedDict, total=False):
    citations: _list[GoogleCloudDiscoveryengineV1alphaCitation]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCliConfig(typing.TypedDict, total=False):
    enabledActions: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCmekConfig(typing.TypedDict, total=False):
    isDefault: bool
    kmsKey: str
    kmsKeyVersion: str
    lastRotationTimestampMicros: str
    name: str
    notebooklmState: typing.Literal[
        "NOTEBOOK_LM_STATE_UNSPECIFIED",
        "NOTEBOOK_LM_NOT_READY",
        "NOTEBOOK_LM_READY",
        "NOTEBOOK_LM_NOT_ENABLED",
    ]
    singleRegionKeys: _list[GoogleCloudDiscoveryengineV1alphaSingleRegionKey]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "KEY_ISSUE",
        "DELETING",
        "DELETE_FAILED",
        "UNUSABLE",
        "ACTIVE_ROTATING",
        "DELETED",
        "EXPIRED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCollection(typing.TypedDict, total=False):
    createTime: str
    dataConnector: GoogleCloudDiscoveryengineV1alphaDataConnector
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCondition(typing.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1alphaConditionTimeRange]
    queryRegex: str
    queryTerms: _list[GoogleCloudDiscoveryengineV1alphaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConditionQueryTerm(
    typing.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConditionTimeRange(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConnectorRun(typing.TypedDict, total=False):
    endTime: str
    entityRuns: _list[GoogleCloudDiscoveryengineV1alphaConnectorRunEntityRun]
    errors: _list[GoogleRpcStatus]
    latestPauseTime: str
    name: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "OVERRUN",
        "CANCELLED",
        "PENDING",
        "WARNING",
        "SKIPPED",
    ]
    stateUpdateTime: str
    trigger: typing.Literal[
        "TRIGGER_UNSPECIFIED", "SCHEDULER", "INITIALIZATION", "RESUME", "MANUAL"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConnectorRunEntityRun(
    typing.TypedDict, total=False
):
    deletedRecordCount: str
    entityName: str
    errorRecordCount: str
    errors: _list[GoogleRpcStatus]
    extractedRecordCount: str
    indexedRecordCount: str
    progress: GoogleCloudDiscoveryengineV1alphaConnectorRunEntityRunProgress
    scheduledRecordCount: str
    sourceApiRequestCount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "OVERRUN",
        "CANCELLED",
        "PENDING",
        "WARNING",
        "SKIPPED",
    ]
    stateUpdateTime: str
    statsUpdateTime: str
    syncType: typing.Literal[
        "SYNC_TYPE_UNSPECIFIED", "FULL", "INCREMENTAL", "REALTIME", "SCALA_SYNC"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConnectorRunEntityRunProgress(
    typing.TypedDict, total=False
):
    currentCount: str
    percentile: float
    totalCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaContactDetails(typing.TypedDict, total=False):
    emailAddress: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControl(typing.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1alphaControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1alphaCondition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1alphaControlFilterAction
    name: str
    promoteAction: GoogleCloudDiscoveryengineV1alphaControlPromoteAction
    redirectAction: GoogleCloudDiscoveryengineV1alphaControlRedirectAction
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1alphaControlSynonymsAction
    useCases: _list[
        typing.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlBoostAction(
    typing.TypedDict, total=False
):
    boost: float
    dataStore: str
    filter: str
    fixedBoost: float
    interpolationBoostSpec: (
        GoogleCloudDiscoveryengineV1alphaControlBoostActionInterpolationBoostSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlBoostActionInterpolationBoostSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1alphaControlBoostActionInterpolationBoostSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlBoostActionInterpolationBoostSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlFilterAction(
    typing.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlPromoteAction(
    typing.TypedDict, total=False
):
    dataStore: str
    searchLinkPromotion: GoogleCloudDiscoveryengineV1alphaSearchLinkPromotion

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlRedirectAction(
    typing.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlSynonymsAction(
    typing.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries(
    typing.TypedDict, total=False
):
    qpsTimeSeries: GoogleMonitoringV3TimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateDataStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateEngineMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateEvaluationMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateSchemaMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateSitemapMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec(
    typing.TypedDict, total=False
):
    enableSearchAdaptor: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnector(typing.TypedDict, total=False):
    aclEnabled: bool
    actionConfig: GoogleCloudDiscoveryengineV1alphaActionConfig
    actionState: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "RUNNING",
        "WARNING",
        "INITIALIZATION_FAILED",
        "UPDATING",
    ]
    alertPolicyConfigs: _list[GoogleCloudDiscoveryengineV1alphaAlertPolicyConfig]
    autoRunDisabled: bool
    bapConfig: GoogleCloudDiscoveryengineV1alphaBAPConfig
    blockingReasons: _list[
        typing.Literal[
            "BLOCKING_REASON_UNSPECIFIED",
            "ALLOWLIST_STATIC_IP",
            "ALLOWLIST_IN_SERVICE_ATTACHMENT",
            "ALLOWLIST_SERVICE_ACCOUNT",
        ]
    ]
    cliConfig: GoogleCloudDiscoveryengineV1alphaCliConfig
    connectorModes: _list[
        typing.Literal[
            "CONNECTOR_MODE_UNSPECIFIED",
            "DATA_INGESTION",
            "ACTIONS",
            "FEDERATED",
            "EUA",
            "FEDERATED_AND_EUA",
        ]
    ]
    connectorSourceId: str
    connectorType: typing.Literal[
        "CONNECTOR_TYPE_UNSPECIFIED",
        "THIRD_PARTY",
        "GCP_FHIR",
        "BIG_QUERY",
        "GCS",
        "GOOGLE_MAIL",
        "GOOGLE_CALENDAR",
        "GOOGLE_DRIVE",
        "NATIVE_CLOUD_IDENTITY",
        "THIRD_PARTY_FEDERATED",
        "THIRD_PARTY_EUA",
        "GCNV",
        "GOOGLE_CHAT",
        "GOOGLE_SITES",
        "REMOTE_MCP",
        "GOOGLE_WORKSPACE",
    ]
    createEuaSaas: bool
    createTime: str
    dataProtectionPolicy: GoogleCloudDiscoveryengineV1alphaDataProtectionPolicy
    dataSource: str
    destinationConfigs: _list[GoogleCloudDiscoveryengineV1alphaDestinationConfig]
    dynamicTools: _list[GoogleCloudDiscoveryengineV1alphaDynamicTool]
    egressFqdns: _list[str]
    endUserConfig: GoogleCloudDiscoveryengineV1alphaDataConnectorEndUserConfig
    entities: _list[GoogleCloudDiscoveryengineV1alphaDataConnectorSourceEntity]
    errors: _list[GoogleRpcStatus]
    federatedConfig: GoogleCloudDiscoveryengineV1alphaDataConnectorFederatedConfig
    hybridIngestionDisabled: bool
    identityRefreshInterval: str
    identityScheduleConfig: GoogleCloudDiscoveryengineV1alphaIdentityScheduleConfig
    incrementalRefreshInterval: str
    incrementalSyncDisabled: bool
    jsonParams: str
    kmsKeyName: str
    lastSyncTime: str
    latestPauseTime: str
    metadata: GoogleCloudDiscoveryengineV1alphaDataConnectorConnectorMetadata
    name: str
    nextSyncTime: GoogleTypeDateTime
    oauthStaticIpAddresses: _list[str]
    params: dict[str, typing.Any]
    privateConnectivityProjectId: str
    realtimeState: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "RUNNING",
        "WARNING",
        "INITIALIZATION_FAILED",
        "UPDATING",
    ]
    realtimeSyncConfig: GoogleCloudDiscoveryengineV1alphaDataConnectorRealtimeSyncConfig
    refreshInterval: str
    removeParamKeys: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "RUNNING",
        "WARNING",
        "INITIALIZATION_FAILED",
        "UPDATING",
    ]
    staticIpAddresses: _list[str]
    staticIpEnabled: bool
    syncMode: typing.Literal["PERIODIC", "STREAMING", "UNSPECIFIED"]
    tag: str
    updateTime: str
    vpcscEnabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorConnectorMetadata(
    typing.TypedDict, total=False
):
    author: str
    description: str
    note: str
    shortDescription: str
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorEndUserConfig(
    typing.TypedDict, total=False
):
    additionalParams: dict[str, typing.Any]
    authParams: dict[str, typing.Any]
    jsonAuthParams: str
    tenant: GoogleCloudDiscoveryengineV1alphaTenant

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorFederatedConfig(
    typing.TypedDict, total=False
):
    additionalParams: dict[str, typing.Any]
    authParams: dict[str, typing.Any]
    jsonAuthParams: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorRealtimeSyncConfig(
    typing.TypedDict, total=False
):
    realtimeSyncSecret: str
    streamingError: (
        GoogleCloudDiscoveryengineV1alphaDataConnectorRealtimeSyncConfigStreamingError
    )
    webhookUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorRealtimeSyncConfigStreamingError(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    streamingErrorReason: typing.Literal[
        "STREAMING_ERROR_REASON_UNSPECIFIED",
        "STREAMING_SETUP_ERROR",
        "STREAMING_SYNC_ERROR",
        "INGRESS_ENDPOINT_REQUIRED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorSourceEntity(
    typing.TypedDict, total=False
):
    dataStore: str
    entityName: str
    healthcareFhirConfig: GoogleCloudDiscoveryengineV1alphaHealthcareFhirConfig
    jsonParams: str
    keyPropertyMappings: dict[str, typing.Any]
    params: dict[str, typing.Any]
    startingSchema: GoogleCloudDiscoveryengineV1alphaSchema

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataProtectionPolicy(
    typing.TypedDict, total=False
):
    sensitiveDataProtectionPolicy: GoogleCloudDiscoveryengineV1alphaDataProtectionPolicySensitiveDataProtectionPolicy

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataProtectionPolicySensitiveDataProtectionPolicy(
    typing.TypedDict, total=False
):
    policy: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStore(typing.TypedDict, total=False):
    aclEnabled: bool
    advancedSiteSearchConfig: GoogleCloudDiscoveryengineV1alphaAdvancedSiteSearchConfig
    billingEstimation: GoogleCloudDiscoveryengineV1alphaDataStoreBillingEstimation
    cmekConfig: GoogleCloudDiscoveryengineV1alphaCmekConfig
    configurableBillingApproach: typing.Literal[
        "CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED",
        "CONFIGURABLE_SUBSCRIPTION_INDEXING_CORE",
        "CONFIGURABLE_CONSUMPTION_EMBEDDING",
    ]
    configurableBillingApproachUpdateTime: str
    contentConfig: typing.Literal[
        "CONTENT_CONFIG_UNSPECIFIED",
        "NO_CONTENT",
        "CONTENT_REQUIRED",
        "PUBLIC_WEBSITE",
        "GOOGLE_WORKSPACE",
    ]
    createTime: str
    dataProtectionPolicy: GoogleCloudDiscoveryengineV1alphaDataProtectionPolicy
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig
    federatedSearchConfig: (
        GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfig
    )
    healthcareFhirConfig: GoogleCloudDiscoveryengineV1alphaHealthcareFhirConfig
    iconUri: str
    identityMappingStore: str
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    isInfobotFaqDataStore: bool
    kmsKeyName: str
    languageInfo: GoogleCloudDiscoveryengineV1alphaLanguageInfo
    name: str
    naturalLanguageQueryUnderstandingConfig: (
        GoogleCloudDiscoveryengineV1alphaNaturalLanguageQueryUnderstandingConfig
    )
    servingConfigDataStore: (
        GoogleCloudDiscoveryengineV1alphaDataStoreServingConfigDataStore
    )
    solutionTypes: _list[
        typing.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
            "SOLUTION_TYPE_AI_MODE",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1alphaSchema
    workspaceConfig: GoogleCloudDiscoveryengineV1alphaWorkspaceConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreBillingEstimation(
    typing.TypedDict, total=False
):
    structuredDataSize: str
    structuredDataUpdateTime: str
    unstructuredDataSize: str
    unstructuredDataUpdateTime: str
    websiteDataSize: str
    websiteDataUpdateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfig(
    typing.TypedDict, total=False
):
    alloyDbConfig: (
        GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigAlloyDbConfig
    )
    notebooklmConfig: (
        GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigNotebooklmConfig
    )
    thirdPartyOauthConfig: GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigThirdPartyOauthConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigAlloyDbConfig(
    typing.TypedDict, total=False
):
    alloydbAiNlConfig: GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbAiNaturalLanguageConfig
    alloydbConnectionConfig: GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbConnectionConfig
    returnedFields: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbAiNaturalLanguageConfig(
    typing.TypedDict, total=False
):
    nlConfigId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbConnectionConfig(
    typing.TypedDict, total=False
):
    authMode: typing.Literal[
        "AUTH_MODE_UNSPECIFIED",
        "AUTH_MODE_SERVICE_ACCOUNT",
        "AUTH_MODE_END_USER_ACCOUNT",
    ]
    database: str
    enablePsvs: bool
    instance: str
    password: str
    user: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigNotebooklmConfig(
    typing.TypedDict, total=False
):
    searchConfig: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreFederatedSearchConfigThirdPartyOauthConfig(
    typing.TypedDict, total=False
):
    appName: str
    instanceName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreServingConfigDataStore(
    typing.TypedDict, total=False
):
    disabledForServing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDedicatedCrawlRateTimeSeries(
    typing.TypedDict, total=False
):
    autoRefreshCrawlErrorRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries
    autoRefreshCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries
    userTriggeredCrawlErrorRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries
    userTriggeredCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteAgentMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteCmekConfigMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteCollectionMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteDataStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteEngineMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteIdentityMappingStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeletePatientFiltersRequest(
    typing.TypedDict, total=False
):
    dataStore: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteSchemaMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteSessionRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteSitemapMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteUserStoreMetadata(
    typing.TypedDict, total=False
):
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDestinationConfig(typing.TypedDict, total=False):
    destinations: _list[GoogleCloudDiscoveryengineV1alphaDestinationConfigDestination]
    jsonParams: str
    key: str
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDestinationConfigDestination(
    typing.TypedDict, total=False
):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig(
    typing.TypedDict, total=False
):
    chunkingConfig: (
        GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfig
    )
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfig(
    typing.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfig(
    typing.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing.TypedDict, total=False
):
    enableGetProcessedDocument: bool
    enableImageAnnotation: bool
    enableLlmLayoutParsing: bool
    enableTableAnnotation: bool
    excludeHtmlClasses: _list[str]
    excludeHtmlElements: _list[str]
    excludeHtmlIds: _list[str]
    structuredContentTypes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDynamicTool(typing.TypedDict, total=False):
    description: str
    displayName: str
    enabled: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngine(typing.TypedDict, total=False):
    agentGatewaySetting: GoogleCloudDiscoveryengineV1alphaAgentGatewaySetting
    appType: typing.Literal["APP_TYPE_UNSPECIFIED", "APP_TYPE_INTRANET"]
    associatedAgentRegistry: str
    chatEngineConfig: GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata
    cmekConfig: GoogleCloudDiscoveryengineV1alphaCmekConfig
    commonConfig: GoogleCloudDiscoveryengineV1alphaEngineCommonConfig
    configurableBillingApproach: typing.Literal[
        "CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED",
        "CONFIGURABLE_BILLING_APPROACH_ENABLED",
    ]
    connectorTenantInfo: dict[str, typing.Any]
    createTime: str
    dataStoreIds: _list[str]
    disableAnalytics: bool
    displayName: str
    features: dict[str, typing.Any]
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    knowledgeGraphConfig: GoogleCloudDiscoveryengineV1alphaEngineKnowledgeGraphConfig
    marketplaceAgentVisibility: typing.Literal[
        "MARKETPLACE_AGENT_VISIBILITY_UNSPECIFIED",
        "SHOW_AVAILABLE_AGENTS_ONLY",
        "SHOW_AGENTS_ALREADY_INTEGRATED",
        "SHOW_AGENTS_ALREADY_PURCHASED",
        "SHOW_ALL_AGENTS",
    ]
    mediaRecommendationEngineConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig
    )
    modelConfigs: dict[str, typing.Any]
    name: str
    observabilityConfig: GoogleCloudDiscoveryengineV1alphaObservabilityConfig
    procurementContactEmails: _list[str]
    recommendationMetadata: (
        GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata
    )
    searchEngineConfig: GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig
    similarDocumentsConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfig
    )
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig(
    typing.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig
    )
    allowCrossRegion: bool
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig(
    typing.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata(
    typing.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineCommonConfig(
    typing.TypedDict, total=False
):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineKnowledgeGraphConfig(
    typing.TypedDict, total=False
):
    cloudKnowledgeGraphTypes: _list[str]
    enableCloudKnowledgeGraph: bool
    enablePrivateKnowledgeGraph: bool
    featureConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineKnowledgeGraphConfigFeatureConfig
    )
    privateKnowledgeGraphTypes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineKnowledgeGraphConfigFeatureConfig(
    typing.TypedDict, total=False
):
    disablePrivateKgAutoComplete: bool
    disablePrivateKgEnrichment: bool
    disablePrivateKgQueryUiChips: bool
    disablePrivateKgQueryUnderstanding: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig(
    typing.TypedDict, total=False
):
    engineFeaturesConfig: GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigEngineFeaturesConfig
    optimizationObjective: str
    optimizationObjectiveConfig: GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig
    trainingState: typing.Literal["TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"]
    type: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigEngineFeaturesConfig(
    typing.TypedDict, total=False
):
    mostPopularConfig: GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigMostPopularFeatureConfig
    recommendedForYouConfig: GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigRecommendedForYouFeatureConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigMostPopularFeatureConfig(
    typing.TypedDict, total=False
):
    timeWindowDays: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig(
    typing.TypedDict, total=False
):
    targetField: str
    targetFieldValueFloat: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigRecommendedForYouFeatureConfig(
    typing.TypedDict, total=False
):
    contextEventType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata(
    typing.TypedDict, total=False
):
    dataState: typing.Literal["DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"]
    lastTrainTime: str
    lastTuneTime: str
    servingState: typing.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    tuningOperation: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig(
    typing.TypedDict, total=False
):
    requiredSubscriptionTier: typing.Literal[
        "SUBSCRIPTION_TIER_UNSPECIFIED",
        "SUBSCRIPTION_TIER_SEARCH",
        "SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT",
        "SUBSCRIPTION_TIER_NOTEBOOK_LM",
        "SUBSCRIPTION_TIER_FRONTLINE_WORKER",
        "SUBSCRIPTION_TIER_AGENTSPACE_STARTER",
        "SUBSCRIPTION_TIER_AGENTSPACE_BUSINESS",
        "SUBSCRIPTION_TIER_ENTERPRISE",
        "SUBSCRIPTION_TIER_ENTERPRISE_EMERGING",
        "SUBSCRIPTION_TIER_EDU",
        "SUBSCRIPTION_TIER_EDU_PRO",
        "SUBSCRIPTION_TIER_EDU_EMERGING",
        "SUBSCRIPTION_TIER_EDU_PRO_EMERGING",
        "SUBSCRIPTION_TIER_FRONTLINE_STARTER",
        "SUBSCRIPTION_TIER_CONSUMPTION_ONLY",
        "SUBSCRIPTION_TIER_EDU_GOV_EMERGING",
    ]
    searchAddOns: _list[
        typing.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeMetadata(
    typing.TypedDict, total=False
):
    createTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeResponse(
    typing.TypedDict, total=False
):
    dataSizeBytes: str
    documentCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluation(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    errorSamples: _list[GoogleRpcStatus]
    evaluationSpec: GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpec
    name: str
    qualityMetrics: GoogleCloudDiscoveryengineV1alphaQualityMetrics
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpec(
    typing.TypedDict, total=False
):
    querySetSpec: GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpecQuerySetSpec
    searchRequest: GoogleCloudDiscoveryengineV1alphaSearchRequest

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpecQuerySetSpec(
    typing.TypedDict, total=False
):
    sampleQuerySet: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExportMetricsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExportMetricsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFieldConfig(typing.TypedDict, total=False):
    advancedSiteSearchDataSources: _list[
        typing.Literal[
            "ADVANCED_SITE_SEARCH_DATA_SOURCE_UNSPECIFIED",
            "METATAGS",
            "PAGEMAP",
            "URI_PATTERN_MAPPING",
            "SCHEMA_ORG",
        ]
    ]
    completableOption: typing.Literal[
        "COMPLETABLE_OPTION_UNSPECIFIED", "COMPLETABLE_ENABLED", "COMPLETABLE_DISABLED"
    ]
    dynamicFacetableOption: typing.Literal[
        "DYNAMIC_FACETABLE_OPTION_UNSPECIFIED",
        "DYNAMIC_FACETABLE_ENABLED",
        "DYNAMIC_FACETABLE_DISABLED",
    ]
    fieldPath: str
    fieldType: typing.Literal[
        "FIELD_TYPE_UNSPECIFIED",
        "OBJECT",
        "STRING",
        "NUMBER",
        "INTEGER",
        "BOOLEAN",
        "GEOLOCATION",
        "DATETIME",
    ]
    indexableOption: typing.Literal[
        "INDEXABLE_OPTION_UNSPECIFIED", "INDEXABLE_ENABLED", "INDEXABLE_DISABLED"
    ]
    keyPropertyType: str
    metatagName: str
    recsFilterableOption: typing.Literal[
        "FILTERABLE_OPTION_UNSPECIFIED", "FILTERABLE_ENABLED", "FILTERABLE_DISABLED"
    ]
    retrievableOption: typing.Literal[
        "RETRIEVABLE_OPTION_UNSPECIFIED", "RETRIEVABLE_ENABLED", "RETRIEVABLE_DISABLED"
    ]
    schemaOrgPaths: _list[str]
    searchableFieldImportance: typing.Literal[
        "SEARCHABLE_FIELD_IMPORTANCE_UNSPECIFIED",
        "VERY_LOW_IMPORTANCE",
        "LOW_IMPORTANCE",
        "DEFAULT_IMPORTANCE",
        "HIGH_IMPORTANCE",
        "VERY_HIGH_IMPORTANCE",
    ]
    searchableOption: typing.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetSessionRequest(typing.TypedDict, total=False):
    includeAnswerDetails: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetUriPatternDocumentDataResponse(
    typing.TypedDict, total=False
):
    documentDataMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaHealthcareFhirConfig(
    typing.TypedDict, total=False
):
    enableConfigurableSchema: bool
    enableStaticIndexingForBatchIngestion: bool
    initialFilterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdentityMappingEntryOperationMetadata(
    typing.TypedDict, total=False
):
    failureCount: str
    successCount: str
    totalCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdentityScheduleConfig(
    typing.TypedDict, total=False
):
    nextSyncTime: GoogleTypeDateTime
    refreshInterval: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdpConfig(typing.TypedDict, total=False):
    externalIdpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfigExternalIdpConfig
    idpType: typing.Literal["IDP_TYPE_UNSPECIFIED", "GSUITE", "THIRD_PARTY"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdpConfigExternalIdpConfig(
    typing.TypedDict, total=False
):
    workforcePoolName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportErrorConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportIdentityMappingsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaInterval(typing.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaLanguageInfo(typing.TypedDict, total=False):
    language: str
    languageCode: str
    normalizedLanguageCode: str
    region: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaLicenseConfig(typing.TypedDict, total=False):
    alertPolicyResourceConfig: (
        GoogleCloudDiscoveryengineV1alphaAlertPolicyResourceConfig
    )
    autoRenew: bool
    earlyTerminated: bool
    earlyTerminationDate: GoogleTypeDate
    endDate: GoogleTypeDate
    freeTrial: bool
    geminiBundle: bool
    lastUserUpdateTime: str
    licenseCount: str
    name: str
    startDate: GoogleTypeDate
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "EXPIRED",
        "NOT_STARTED",
        "WITHDRAWN",
        "DEACTIVATING",
    ]
    subscriptionTerm: typing.Literal[
        "SUBSCRIPTION_TERM_UNSPECIFIED",
        "SUBSCRIPTION_TERM_ONE_MONTH",
        "SUBSCRIPTION_TERM_ONE_YEAR",
        "SUBSCRIPTION_TERM_THREE_YEARS",
        "SUBSCRIPTION_TERM_CUSTOM",
    ]
    subscriptionTier: typing.Literal[
        "SUBSCRIPTION_TIER_UNSPECIFIED",
        "SUBSCRIPTION_TIER_SEARCH",
        "SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT",
        "SUBSCRIPTION_TIER_NOTEBOOK_LM",
        "SUBSCRIPTION_TIER_FRONTLINE_WORKER",
        "SUBSCRIPTION_TIER_AGENTSPACE_STARTER",
        "SUBSCRIPTION_TIER_AGENTSPACE_BUSINESS",
        "SUBSCRIPTION_TIER_ENTERPRISE",
        "SUBSCRIPTION_TIER_ENTERPRISE_EMERGING",
        "SUBSCRIPTION_TIER_EDU",
        "SUBSCRIPTION_TIER_EDU_PRO",
        "SUBSCRIPTION_TIER_EDU_EMERGING",
        "SUBSCRIPTION_TIER_EDU_PRO_EMERGING",
        "SUBSCRIPTION_TIER_FRONTLINE_STARTER",
        "SUBSCRIPTION_TIER_CONSUMPTION_ONLY",
        "SUBSCRIPTION_TIER_EDU_GOV_EMERGING",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSessionsRequest(
    typing.TypedDict, total=False
):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str
    parent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSessionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sessions: _list[GoogleCloudDiscoveryengineV1alphaSession]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaNaturalLanguageQueryUnderstandingConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaObservabilityConfig(
    typing.TypedDict, total=False
):
    observabilityEnabled: bool
    sensitiveLoggingEnabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaObtainCrawlRateResponse(
    typing.TypedDict, total=False
):
    dedicatedCrawlRateTimeSeries: (
        GoogleCloudDiscoveryengineV1alphaDedicatedCrawlRateTimeSeries
    )
    error: GoogleRpcStatus
    organicCrawlRateTimeSeries: (
        GoogleCloudDiscoveryengineV1alphaOrganicCrawlRateTimeSeries
    )
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaOrganicCrawlRateTimeSeries(
    typing.TypedDict, total=False
):
    googleOrganicCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries
    vertexAiOrganicCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPatientFilterOperationMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    filtersAddedCount: str
    filtersRemovedCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProject(typing.TypedDict, total=False):
    configurableBillingStatus: (
        GoogleCloudDiscoveryengineV1alphaProjectConfigurableBillingStatus
    )
    createTime: str
    customerProvidedConfig: (
        GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfig
    )
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectConfigurableBillingStatus(
    typing.TypedDict, total=False
):
    agentSearchTokenSubscriptionStatuses: _list[
        GoogleCloudDiscoveryengineV1alphaProjectConfigurableBillingStatusAgentSearchTokenSubscriptionStatus
    ]
    effectiveIndexingCoreThreshold: str
    effectiveSearchQpmThreshold: str
    indexingCoreThresholdNextUpdateTime: str
    searchQpmThresholdNextUpdateTime: str
    startTime: str
    terminateTime: str
    updateType: typing.Literal[
        "UPDATE_TYPE_UNSPECIFIED", "CREATE", "DELETE", "SCALE_UP", "SCALE_DOWN"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectConfigurableBillingStatusAgentSearchTokenSubscriptionStatus(
    typing.TypedDict, total=False
):
    effectiveTpmThreshold: str
    modelVersion: str
    startTime: str
    terminateTime: str
    tpmThresholdNextUpdateTime: str
    updateType: typing.Literal[
        "UPDATE_TYPE_UNSPECIFIED", "CREATE", "DELETE", "SCALE_UP", "SCALE_DOWN"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfig(
    typing.TypedDict, total=False
):
    notebooklmConfig: (
        GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfig
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfig(
    typing.TypedDict, total=False
):
    dataProtectionPolicy: GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicy
    modelArmorConfig: GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfigModelArmorConfig
    observabilityConfig: GoogleCloudDiscoveryengineV1alphaObservabilityConfig
    optOutNotebookSharing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicy(
    typing.TypedDict, total=False
):
    sensitiveDataProtectionPolicy: GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicySensitiveDataProtectionPolicy

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicySensitiveDataProtectionPolicy(
    typing.TypedDict, total=False
):
    policy: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectCustomerProvidedConfigNotebooklmConfigModelArmorConfig(
    typing.TypedDict, total=False
):
    responseTemplate: str
    userPromptTemplate: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectServiceTerms(
    typing.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProvisionProjectMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeSucceeded: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponse(
    typing.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponse(
    typing.TypedDict, total=False
):
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQualityMetrics(typing.TypedDict, total=False):
    docNdcg: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    docPrecision: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    docRecall: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    pageNdcg: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    pageRecall: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics(
    typing.TypedDict, total=False
):
    top1: float
    top10: float
    top3: float
    top5: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQuery(typing.TypedDict, total=False):
    createTime: str
    parts: _list[GoogleCloudDiscoveryengineV1alphaQueryPart]
    queryId: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQueryPart(typing.TypedDict, total=False):
    documentReference: GoogleCloudDiscoveryengineV1alphaQueryPartDocumentReference
    driveDocumentReference: (
        GoogleCloudDiscoveryengineV1alphaQueryPartDriveDocumentReference
    )
    mimeType: str
    personReference: GoogleCloudDiscoveryengineV1alphaQueryPartPersonReference
    text: str
    uiJsonPayload: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQueryPartDocumentReference(
    typing.TypedDict, total=False
):
    destinationUri: str
    displayTitle: str
    documentName: str
    fileId: str
    iconUri: str
    urlForConnector: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQueryPartDriveDocumentReference(
    typing.TypedDict, total=False
):
    destinationUri: str
    displayTitle: str
    documentName: str
    driveId: str
    fileId: str
    iconUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQueryPartPersonReference(
    typing.TypedDict, total=False
):
    destinationUri: str
    displayName: str
    displayPhotoUri: str
    documentName: str
    email: str
    fileId: str
    personId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    invalidUris: _list[str]
    invalidUrisCount: int
    noindexUris: _list[str]
    noindexUrisCount: int
    pendingCount: int
    quotaExceededCount: int
    successCount: int
    updateTime: str
    urisNotMatchingTargetSites: _list[str]
    urisNotMatchingTargetSitesCount: int
    validUrisCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponse(
    typing.TypedDict, total=False
):
    failedUris: _list[str]
    failureSamples: _list[
        GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfo(
    typing.TypedDict, total=False
):
    failureReasons: _list[
        GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason
    ]
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason(
    typing.TypedDict, total=False
):
    corpusType: typing.Literal["CORPUS_TYPE_UNSPECIFIED", "DESKTOP", "MOBILE"]
    errorMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveDedicatedCrawlRateMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveDedicatedCrawlRateResponse(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemovePatientFilterRequest(
    typing.TypedDict, total=False
):
    dataStore: str
    filterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReplacePatientFilterRequest(
    typing.TypedDict, total=False
):
    dataStore: str
    filterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaResumeExperimentMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSafetyRating(typing.TypedDict, total=False):
    blocked: bool
    category: typing.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    probability: typing.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]
    probabilityScore: float
    severity: typing.Literal[
        "HARM_SEVERITY_UNSPECIFIED",
        "HARM_SEVERITY_NEGLIGIBLE",
        "HARM_SEVERITY_LOW",
        "HARM_SEVERITY_MEDIUM",
        "HARM_SEVERITY_HIGH",
    ]
    severityScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSchema(typing.TypedDict, total=False):
    fieldConfigs: _list[GoogleCloudDiscoveryengineV1alphaFieldConfig]
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchLinkPromotion(
    typing.TypedDict, total=False
):
    description: str
    document: str
    enabled: bool
    imageUri: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequest(typing.TypedDict, total=False):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec
    crowdingSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestCrowdingSpec]
    customFineTuningSpec: GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec
    customRankingParams: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestCustomRankingParams
    )
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec]
    displaySpec: GoogleCloudDiscoveryengineV1alphaSearchRequestDisplaySpec
    embeddingSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpec
    entity: str
    facetSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1alphaSearchRequestImageQuery
    languageCode: str
    naturalLanguageQueryUnderstandingSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestNaturalLanguageQueryUnderstandingSpec
    numResultsPerDataStore: int
    offset: int
    oneBoxPageSize: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    personalizationSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestPersonalizationSpec
    )
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestQueryExpansionSpec
    rankingExpression: str
    rankingExpressionBackend: typing.Literal[
        "RANKING_EXPRESSION_BACKEND_UNSPECIFIED",
        "BYOE",
        "CLEARBOX",
        "RANK_BY_EMBEDDING",
        "RANK_BY_FORMULA",
    ]
    regionCode: str
    relevanceFilterSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestRelevanceFilterSpec
    )
    relevanceScoreSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestRelevanceScoreSpec
    relevanceThreshold: typing.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    safeSearch: bool
    searchAddonSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAddonSpec
    searchAsYouTypeSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAsYouTypeSpec
    )
    servingConfig: str
    session: str
    sessionSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestSessionSpec
    spellCorrectionSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestSpellCorrectionSpec
    )
    useLatestData: bool
    userInfo: GoogleCloudDiscoveryengineV1alphaUserInfo
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec(
    typing.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec(
    typing.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecExtractiveContentSpec
    searchResultMode: typing.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    snippetSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSnippetSpec
    )
    summarySpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecChunkSpec(
    typing.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecExtractiveContentSpec(
    typing.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSnippetSpec(
    typing.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpec(
    typing.TypedDict, total=False
):
    ignoreAdversarialQuery: bool
    ignoreJailBreakingQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelSpec
    multimodalSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecMultiModalSpec
    summaryResultCount: int
    useSemanticChunks: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelPromptSpec(
    typing.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelSpec(
    typing.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecMultiModalSpec(
    typing.TypedDict, total=False
):
    imageSource: typing.Literal[
        "IMAGE_SOURCE_UNSPECIFIED",
        "ALL_AVAILABLE_SOURCES",
        "CORPUS_IMAGE_ONLY",
        "FIGURE_GENERATION_ONLY",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestCrowdingSpec(
    typing.TypedDict, total=False
):
    field: str
    maxCount: int
    mode: typing.Literal[
        "MODE_UNSPECIFIED", "DROP_CROWDED_RESULTS", "DEMOTE_CROWDED_RESULTS_TO_END"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestCustomRankingParams(
    typing.TypedDict, total=False
):
    expressionsToPrecompute: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    customSearchOperators: str
    dataStore: str
    filter: str
    numResults: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestDisplaySpec(
    typing.TypedDict, total=False
):
    matchHighlightingCondition: typing.Literal[
        "MATCH_HIGHLIGHTING_CONDITION_UNSPECIFIED",
        "MATCH_HIGHLIGHTING_DISABLED",
        "MATCH_HIGHLIGHTING_ENABLED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpec(
    typing.TypedDict, total=False
):
    embeddingVectors: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpecEmbeddingVector
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpecEmbeddingVector(
    typing.TypedDict, total=False
):
    fieldPath: str
    vector: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpec(
    typing.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpecFacetKey(
    typing.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudDiscoveryengineV1alphaInterval]
    key: str
    orderBy: str
    prefixes: _list[str]
    restrictedValues: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestImageQuery(
    typing.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestNaturalLanguageQueryUnderstandingSpec(
    typing.TypedDict, total=False
):
    allowedFieldNames: _list[str]
    extractedFilterBehavior: typing.Literal[
        "EXTRACTED_FILTER_BEHAVIOR_UNSPECIFIED", "HARD_FILTER", "SOFT_BOOST"
    ]
    filterExtractionCondition: typing.Literal[
        "CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    geoSearchQueryDetectionFieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestPersonalizationSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestQueryExpansionSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestRelevanceFilterSpec(
    typing.TypedDict, total=False
):
    keywordSearchThreshold: GoogleCloudDiscoveryengineV1alphaSearchRequestRelevanceFilterSpecRelevanceThresholdSpec
    semanticSearchThreshold: GoogleCloudDiscoveryengineV1alphaSearchRequestRelevanceFilterSpecRelevanceThresholdSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestRelevanceFilterSpecRelevanceThresholdSpec(
    typing.TypedDict, total=False
):
    relevanceThreshold: typing.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    semanticRelevanceThreshold: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestRelevanceScoreSpec(
    typing.TypedDict, total=False
):
    returnRelevanceScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAddonSpec(
    typing.TypedDict, total=False
):
    disableGenerativeAnswerAddOn: bool
    disableKpiPersonalizationAddOn: bool
    disableSemanticAddOn: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAsYouTypeSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSessionSpec(
    typing.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSpellCorrectionSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSession(typing.TypedDict, total=False):
    displayName: str
    endTime: str
    isPinned: bool
    labels: _list[str]
    name: str
    pendingAsyncAssistOperationId: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS"]
    turns: _list[GoogleCloudDiscoveryengineV1alphaSessionTurn]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSessionTurn(typing.TypedDict, total=False):
    answer: str
    detailedAnswer: GoogleCloudDiscoveryengineV1alphaAnswer
    detailedAssistAnswer: GoogleCloudDiscoveryengineV1alphaAssistAnswer
    live: bool
    query: GoogleCloudDiscoveryengineV1alphaQuery
    queryConfig: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetDedicatedCrawlRateMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetDedicatedCrawlRateResponse(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUpDataConnectorMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSingleRegionKey(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSiteVerificationInfo(
    typing.TypedDict, total=False
):
    siteVerificationState: typing.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSitemap(typing.TypedDict, total=False):
    createTime: str
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStartExperimentMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStartExperimentRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSite(typing.TypedDict, total=False):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing.Literal[
        "INDEXING_STATUS_UNSPECIFIED",
        "PENDING",
        "FAILED",
        "SUCCEEDED",
        "DELETING",
        "CANCELLABLE",
        "CANCELLED",
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1alphaSiteVerificationInfo
    type: typing.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReason(
    typing.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReasonQuotaFailure(
    typing.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTenant(typing.TypedDict, total=False):
    displayName: str
    id: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineMetadata(
    typing.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateCmekConfigMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateCollectionMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateSchemaMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateSessionRequest(
    typing.TypedDict, total=False
):
    session: GoogleCloudDiscoveryengineV1alphaSession
    updateMask: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserInfo(typing.TypedDict, total=False):
    preciseLocation: GoogleCloudDiscoveryengineV1alphaUserInfoPreciseLocation
    timeZone: str
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserInfoPreciseLocation(
    typing.TypedDict, total=False
):
    address: str
    point: GoogleTypeLatLng

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserLicense(typing.TypedDict, total=False):
    createTime: str
    lastLoginTime: str
    licenseAssignmentState: typing.Literal[
        "LICENSE_ASSIGNMENT_STATE_UNSPECIFIED",
        "ASSIGNED",
        "UNASSIGNED",
        "NO_LICENSE",
        "NO_LICENSE_ATTEMPTED_LOGIN",
        "BLOCKED",
    ]
    licenseConfig: str
    updateTime: str
    userPrincipal: str
    userProfile: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWorkspaceConfig(typing.TypedDict, total=False):
    dasherCustomerId: str
    superAdminEmailAddress: str
    superAdminServiceAccount: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "GOOGLE_DRIVE",
        "GOOGLE_MAIL",
        "GOOGLE_SITES",
        "GOOGLE_CALENDAR",
        "GOOGLE_CHAT",
        "GOOGLE_GROUPS",
        "GOOGLE_KEEP",
        "GOOGLE_PEOPLE",
        "GOOGLE_WORKSPACE",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaAclConfig(typing.TypedDict, total=False):
    idpConfig: GoogleCloudDiscoveryengineV1betaIdpConfig
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaAdvancedSiteSearchConfig(
    typing.TypedDict, total=False
):
    disableAutomaticRefresh: bool
    disableInitialIndex: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaAgentGatewaySetting(
    typing.TypedDict, total=False
):
    defaultEgressAgentGateway: (
        GoogleCloudDiscoveryengineV1betaAgentGatewaySettingAgentGatewayReference
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaAgentGatewaySettingAgentGatewayReference(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSitesResponse(
    typing.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1betaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchUpdateUserLicensesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchUpdateUserLicensesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    userLicenses: _list[GoogleCloudDiscoveryengineV1betaUserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCmekConfig(typing.TypedDict, total=False):
    isDefault: bool
    kmsKey: str
    kmsKeyVersion: str
    lastRotationTimestampMicros: str
    name: str
    notebooklmState: typing.Literal[
        "NOTEBOOK_LM_STATE_UNSPECIFIED",
        "NOTEBOOK_LM_NOT_READY",
        "NOTEBOOK_LM_READY",
        "NOTEBOOK_LM_NOT_ENABLED",
    ]
    singleRegionKeys: _list[GoogleCloudDiscoveryengineV1betaSingleRegionKey]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "KEY_ISSUE",
        "DELETING",
        "DELETE_FAILED",
        "UNUSABLE",
        "ACTIVE_ROTATING",
        "DELETED",
        "EXPIRED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCondition(typing.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1betaConditionTimeRange]
    queryRegex: str
    queryTerms: _list[GoogleCloudDiscoveryengineV1betaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConditionQueryTerm(typing.TypedDict, total=False):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConditionTimeRange(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControl(typing.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1betaControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1betaCondition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1betaControlFilterAction
    name: str
    promoteAction: GoogleCloudDiscoveryengineV1betaControlPromoteAction
    redirectAction: GoogleCloudDiscoveryengineV1betaControlRedirectAction
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1betaControlSynonymsAction
    useCases: _list[
        typing.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlBoostAction(typing.TypedDict, total=False):
    boost: float
    dataStore: str
    filter: str
    fixedBoost: float
    interpolationBoostSpec: (
        GoogleCloudDiscoveryengineV1betaControlBoostActionInterpolationBoostSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlBoostActionInterpolationBoostSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1betaControlBoostActionInterpolationBoostSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlBoostActionInterpolationBoostSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlFilterAction(
    typing.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlPromoteAction(
    typing.TypedDict, total=False
):
    dataStore: str
    searchLinkPromotion: GoogleCloudDiscoveryengineV1betaSearchLinkPromotion

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlRedirectAction(
    typing.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlSynonymsAction(
    typing.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCrawlRateTimeSeries(
    typing.TypedDict, total=False
):
    qpsTimeSeries: GoogleMonitoringV3TimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateDataStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateEngineMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateEvaluationMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateSchemaMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateSitemapMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStore(typing.TypedDict, total=False):
    aclEnabled: bool
    advancedSiteSearchConfig: GoogleCloudDiscoveryengineV1betaAdvancedSiteSearchConfig
    billingEstimation: GoogleCloudDiscoveryengineV1betaDataStoreBillingEstimation
    cmekConfig: GoogleCloudDiscoveryengineV1betaCmekConfig
    configurableBillingApproach: typing.Literal[
        "CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED",
        "CONFIGURABLE_SUBSCRIPTION_INDEXING_CORE",
        "CONFIGURABLE_CONSUMPTION_EMBEDDING",
    ]
    configurableBillingApproachUpdateTime: str
    contentConfig: typing.Literal[
        "CONTENT_CONFIG_UNSPECIFIED",
        "NO_CONTENT",
        "CONTENT_REQUIRED",
        "PUBLIC_WEBSITE",
        "GOOGLE_WORKSPACE",
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfig
    federatedSearchConfig: (
        GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfig
    )
    healthcareFhirConfig: GoogleCloudDiscoveryengineV1betaHealthcareFhirConfig
    identityMappingStore: str
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    isInfobotFaqDataStore: bool
    kmsKeyName: str
    languageInfo: GoogleCloudDiscoveryengineV1betaLanguageInfo
    name: str
    naturalLanguageQueryUnderstandingConfig: (
        GoogleCloudDiscoveryengineV1betaNaturalLanguageQueryUnderstandingConfig
    )
    servingConfigDataStore: (
        GoogleCloudDiscoveryengineV1betaDataStoreServingConfigDataStore
    )
    solutionTypes: _list[
        typing.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
            "SOLUTION_TYPE_AI_MODE",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1betaSchema
    workspaceConfig: GoogleCloudDiscoveryengineV1betaWorkspaceConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreBillingEstimation(
    typing.TypedDict, total=False
):
    structuredDataSize: str
    structuredDataUpdateTime: str
    unstructuredDataSize: str
    unstructuredDataUpdateTime: str
    websiteDataSize: str
    websiteDataUpdateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfig(
    typing.TypedDict, total=False
):
    alloyDbConfig: (
        GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigAlloyDbConfig
    )
    notebooklmConfig: (
        GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigNotebooklmConfig
    )
    thirdPartyOauthConfig: GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigThirdPartyOauthConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigAlloyDbConfig(
    typing.TypedDict, total=False
):
    alloydbAiNlConfig: GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbAiNaturalLanguageConfig
    alloydbConnectionConfig: GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbConnectionConfig
    returnedFields: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbAiNaturalLanguageConfig(
    typing.TypedDict, total=False
):
    nlConfigId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigAlloyDbConfigAlloyDbConnectionConfig(
    typing.TypedDict, total=False
):
    authMode: typing.Literal[
        "AUTH_MODE_UNSPECIFIED",
        "AUTH_MODE_SERVICE_ACCOUNT",
        "AUTH_MODE_END_USER_ACCOUNT",
    ]
    database: str
    enablePsvs: bool
    instance: str
    password: str
    user: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigNotebooklmConfig(
    typing.TypedDict, total=False
):
    searchConfig: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreFederatedSearchConfigThirdPartyOauthConfig(
    typing.TypedDict, total=False
):
    appName: str
    instanceName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreServingConfigDataStore(
    typing.TypedDict, total=False
):
    disabledForServing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDedicatedCrawlRateTimeSeries(
    typing.TypedDict, total=False
):
    autoRefreshCrawlErrorRate: GoogleCloudDiscoveryengineV1betaCrawlRateTimeSeries
    autoRefreshCrawlRate: GoogleCloudDiscoveryengineV1betaCrawlRateTimeSeries
    userTriggeredCrawlErrorRate: GoogleCloudDiscoveryengineV1betaCrawlRateTimeSeries
    userTriggeredCrawlRate: GoogleCloudDiscoveryengineV1betaCrawlRateTimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteDataStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteEngineMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteIdentityMappingStoreMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteSchemaMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteSitemapMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfig(
    typing.TypedDict, total=False
):
    chunkingConfig: (
        GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfig
    )
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfig(
    typing.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfig(
    typing.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing.TypedDict, total=False
):
    enableGetProcessedDocument: bool
    enableImageAnnotation: bool
    enableLlmLayoutParsing: bool
    enableTableAnnotation: bool
    excludeHtmlClasses: _list[str]
    excludeHtmlElements: _list[str]
    excludeHtmlIds: _list[str]
    structuredContentTypes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngine(typing.TypedDict, total=False):
    agentGatewaySetting: GoogleCloudDiscoveryengineV1betaAgentGatewaySetting
    appType: typing.Literal["APP_TYPE_UNSPECIFIED", "APP_TYPE_INTRANET"]
    associatedAgentRegistry: str
    chatEngineConfig: GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata
    cmekConfig: GoogleCloudDiscoveryengineV1betaCmekConfig
    commonConfig: GoogleCloudDiscoveryengineV1betaEngineCommonConfig
    configurableBillingApproach: typing.Literal[
        "CONFIGURABLE_BILLING_APPROACH_UNSPECIFIED",
        "CONFIGURABLE_BILLING_APPROACH_ENABLED",
    ]
    connectorTenantInfo: dict[str, typing.Any]
    createTime: str
    dataStoreIds: _list[str]
    disableAnalytics: bool
    displayName: str
    features: dict[str, typing.Any]
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    knowledgeGraphConfig: GoogleCloudDiscoveryengineV1betaEngineKnowledgeGraphConfig
    marketplaceAgentVisibility: typing.Literal[
        "MARKETPLACE_AGENT_VISIBILITY_UNSPECIFIED",
        "SHOW_AVAILABLE_AGENTS_ONLY",
        "SHOW_AGENTS_ALREADY_INTEGRATED",
        "SHOW_AGENTS_ALREADY_PURCHASED",
        "SHOW_ALL_AGENTS",
    ]
    mediaRecommendationEngineConfig: (
        GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfig
    )
    modelConfigs: dict[str, typing.Any]
    name: str
    observabilityConfig: GoogleCloudDiscoveryengineV1betaObservabilityConfig
    procurementContactEmails: _list[str]
    searchEngineConfig: GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig
    solutionType: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
        "SOLUTION_TYPE_AI_MODE",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig(
    typing.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1betaEngineChatEngineConfigAgentCreationConfig
    )
    allowCrossRegion: bool
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineConfigAgentCreationConfig(
    typing.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata(
    typing.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineCommonConfig(typing.TypedDict, total=False):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineKnowledgeGraphConfig(
    typing.TypedDict, total=False
):
    cloudKnowledgeGraphTypes: _list[str]
    enableCloudKnowledgeGraph: bool
    enablePrivateKnowledgeGraph: bool
    featureConfig: (
        GoogleCloudDiscoveryengineV1betaEngineKnowledgeGraphConfigFeatureConfig
    )
    privateKnowledgeGraphTypes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineKnowledgeGraphConfigFeatureConfig(
    typing.TypedDict, total=False
):
    disablePrivateKgAutoComplete: bool
    disablePrivateKgEnrichment: bool
    disablePrivateKgQueryUiChips: bool
    disablePrivateKgQueryUnderstanding: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfig(
    typing.TypedDict, total=False
):
    engineFeaturesConfig: GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigEngineFeaturesConfig
    optimizationObjective: str
    optimizationObjectiveConfig: GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig
    trainingState: typing.Literal["TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"]
    type: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigEngineFeaturesConfig(
    typing.TypedDict, total=False
):
    mostPopularConfig: GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigMostPopularFeatureConfig
    recommendedForYouConfig: GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigRecommendedForYouFeatureConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigMostPopularFeatureConfig(
    typing.TypedDict, total=False
):
    timeWindowDays: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig(
    typing.TypedDict, total=False
):
    targetField: str
    targetFieldValueFloat: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineMediaRecommendationEngineConfigRecommendedForYouFeatureConfig(
    typing.TypedDict, total=False
):
    contextEventType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig(
    typing.TypedDict, total=False
):
    requiredSubscriptionTier: typing.Literal[
        "SUBSCRIPTION_TIER_UNSPECIFIED",
        "SUBSCRIPTION_TIER_SEARCH",
        "SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT",
        "SUBSCRIPTION_TIER_NOTEBOOK_LM",
        "SUBSCRIPTION_TIER_FRONTLINE_WORKER",
        "SUBSCRIPTION_TIER_AGENTSPACE_STARTER",
        "SUBSCRIPTION_TIER_AGENTSPACE_BUSINESS",
        "SUBSCRIPTION_TIER_ENTERPRISE",
        "SUBSCRIPTION_TIER_ENTERPRISE_EMERGING",
        "SUBSCRIPTION_TIER_EDU",
        "SUBSCRIPTION_TIER_EDU_PRO",
        "SUBSCRIPTION_TIER_EDU_EMERGING",
        "SUBSCRIPTION_TIER_EDU_PRO_EMERGING",
        "SUBSCRIPTION_TIER_FRONTLINE_STARTER",
        "SUBSCRIPTION_TIER_CONSUMPTION_ONLY",
        "SUBSCRIPTION_TIER_EDU_GOV_EMERGING",
    ]
    searchAddOns: _list[
        typing.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluation(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    errorSamples: _list[GoogleRpcStatus]
    evaluationSpec: GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpec
    name: str
    qualityMetrics: GoogleCloudDiscoveryengineV1betaQualityMetrics
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpec(
    typing.TypedDict, total=False
):
    querySetSpec: GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpecQuerySetSpec
    searchRequest: GoogleCloudDiscoveryengineV1betaSearchRequest

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpecQuerySetSpec(
    typing.TypedDict, total=False
):
    sampleQuerySet: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaHealthcareFhirConfig(
    typing.TypedDict, total=False
):
    enableConfigurableSchema: bool
    enableStaticIndexingForBatchIngestion: bool
    initialFilterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaIdentityMappingEntryOperationMetadata(
    typing.TypedDict, total=False
):
    failureCount: str
    successCount: str
    totalCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaIdpConfig(typing.TypedDict, total=False):
    externalIdpConfig: GoogleCloudDiscoveryengineV1betaIdpConfigExternalIdpConfig
    idpType: typing.Literal["IDP_TYPE_UNSPECIFIED", "GSUITE", "THIRD_PARTY"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaIdpConfigExternalIdpConfig(
    typing.TypedDict, total=False
):
    workforcePoolName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportCompletionSuggestionsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportErrorConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportIdentityMappingsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSampleQueriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSampleQueriesResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaInterval(typing.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaLanguageInfo(typing.TypedDict, total=False):
    language: str
    languageCode: str
    normalizedLanguageCode: str
    region: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaLicenseConfig(typing.TypedDict, total=False):
    autoRenew: bool
    earlyTerminated: bool
    earlyTerminationDate: GoogleTypeDate
    endDate: GoogleTypeDate
    freeTrial: bool
    geminiBundle: bool
    lastUserUpdateTime: str
    licenseCount: str
    name: str
    startDate: GoogleTypeDate
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "EXPIRED",
        "NOT_STARTED",
        "WITHDRAWN",
        "DEACTIVATING",
    ]
    subscriptionTerm: typing.Literal[
        "SUBSCRIPTION_TERM_UNSPECIFIED",
        "SUBSCRIPTION_TERM_ONE_MONTH",
        "SUBSCRIPTION_TERM_ONE_YEAR",
        "SUBSCRIPTION_TERM_THREE_YEARS",
        "SUBSCRIPTION_TERM_CUSTOM",
    ]
    subscriptionTier: typing.Literal[
        "SUBSCRIPTION_TIER_UNSPECIFIED",
        "SUBSCRIPTION_TIER_SEARCH",
        "SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT",
        "SUBSCRIPTION_TIER_NOTEBOOK_LM",
        "SUBSCRIPTION_TIER_FRONTLINE_WORKER",
        "SUBSCRIPTION_TIER_AGENTSPACE_STARTER",
        "SUBSCRIPTION_TIER_AGENTSPACE_BUSINESS",
        "SUBSCRIPTION_TIER_ENTERPRISE",
        "SUBSCRIPTION_TIER_ENTERPRISE_EMERGING",
        "SUBSCRIPTION_TIER_EDU",
        "SUBSCRIPTION_TIER_EDU_PRO",
        "SUBSCRIPTION_TIER_EDU_EMERGING",
        "SUBSCRIPTION_TIER_EDU_PRO_EMERGING",
        "SUBSCRIPTION_TIER_FRONTLINE_STARTER",
        "SUBSCRIPTION_TIER_CONSUMPTION_ONLY",
        "SUBSCRIPTION_TIER_EDU_GOV_EMERGING",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaNaturalLanguageQueryUnderstandingConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaObservabilityConfig(
    typing.TypedDict, total=False
):
    observabilityEnabled: bool
    sensitiveLoggingEnabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaObtainCrawlRateResponse(
    typing.TypedDict, total=False
):
    dedicatedCrawlRateTimeSeries: (
        GoogleCloudDiscoveryengineV1betaDedicatedCrawlRateTimeSeries
    )
    error: GoogleRpcStatus
    organicCrawlRateTimeSeries: (
        GoogleCloudDiscoveryengineV1betaOrganicCrawlRateTimeSeries
    )
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaOrganicCrawlRateTimeSeries(
    typing.TypedDict, total=False
):
    googleOrganicCrawlRate: GoogleCloudDiscoveryengineV1betaCrawlRateTimeSeries
    vertexAiOrganicCrawlRate: GoogleCloudDiscoveryengineV1betaCrawlRateTimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProject(typing.TypedDict, total=False):
    configurableBillingStatus: (
        GoogleCloudDiscoveryengineV1betaProjectConfigurableBillingStatus
    )
    createTime: str
    customerProvidedConfig: (
        GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfig
    )
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectConfigurableBillingStatus(
    typing.TypedDict, total=False
):
    agentSearchTokenSubscriptionStatuses: _list[
        GoogleCloudDiscoveryengineV1betaProjectConfigurableBillingStatusAgentSearchTokenSubscriptionStatus
    ]
    effectiveIndexingCoreThreshold: str
    effectiveSearchQpmThreshold: str
    indexingCoreThresholdNextUpdateTime: str
    searchQpmThresholdNextUpdateTime: str
    startTime: str
    terminateTime: str
    updateType: typing.Literal[
        "UPDATE_TYPE_UNSPECIFIED", "CREATE", "DELETE", "SCALE_UP", "SCALE_DOWN"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectConfigurableBillingStatusAgentSearchTokenSubscriptionStatus(
    typing.TypedDict, total=False
):
    effectiveTpmThreshold: str
    modelVersion: str
    startTime: str
    terminateTime: str
    tpmThresholdNextUpdateTime: str
    updateType: typing.Literal[
        "UPDATE_TYPE_UNSPECIFIED", "CREATE", "DELETE", "SCALE_UP", "SCALE_DOWN"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfig(
    typing.TypedDict, total=False
):
    notebooklmConfig: (
        GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfig
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfig(
    typing.TypedDict, total=False
):
    dataProtectionPolicy: GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicy
    modelArmorConfig: GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfigModelArmorConfig
    observabilityConfig: GoogleCloudDiscoveryengineV1betaObservabilityConfig
    optOutNotebookSharing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicy(
    typing.TypedDict, total=False
):
    sensitiveDataProtectionPolicy: GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicySensitiveDataProtectionPolicy

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfigDataProtectionPolicySensitiveDataProtectionPolicy(
    typing.TypedDict, total=False
):
    policy: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectCustomerProvidedConfigNotebooklmConfigModelArmorConfig(
    typing.TypedDict, total=False
):
    responseTemplate: str
    userPromptTemplate: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectServiceTerms(
    typing.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProvisionProjectMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponse(
    typing.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaQualityMetrics(typing.TypedDict, total=False):
    docNdcg: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    docPrecision: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    docRecall: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    pageNdcg: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    pageRecall: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics(
    typing.TypedDict, total=False
):
    top1: float
    top10: float
    top3: float
    top5: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRemoveDedicatedCrawlRateMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRemoveDedicatedCrawlRateResponse(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSchema(typing.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchLinkPromotion(
    typing.TypedDict, total=False
):
    description: str
    document: str
    enabled: bool
    imageUri: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequest(typing.TypedDict, total=False):
    boostSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec
    crowdingSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestCrowdingSpec]
    customRankingParams: (
        GoogleCloudDiscoveryengineV1betaSearchRequestCustomRankingParams
    )
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestDataStoreSpec]
    displaySpec: GoogleCloudDiscoveryengineV1betaSearchRequestDisplaySpec
    embeddingSpec: GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpec
    entity: str
    facetSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1betaSearchRequestImageQuery
    languageCode: str
    naturalLanguageQueryUnderstandingSpec: GoogleCloudDiscoveryengineV1betaSearchRequestNaturalLanguageQueryUnderstandingSpec
    numResultsPerDataStore: int
    offset: int
    oneBoxPageSize: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    personalizationSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestPersonalizationSpec
    )
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec
    rankingExpression: str
    rankingExpressionBackend: typing.Literal[
        "RANKING_EXPRESSION_BACKEND_UNSPECIFIED",
        "BYOE",
        "CLEARBOX",
        "RANK_BY_EMBEDDING",
        "RANK_BY_FORMULA",
    ]
    regionCode: str
    relevanceFilterSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestRelevanceFilterSpec
    )
    relevanceScoreSpec: GoogleCloudDiscoveryengineV1betaSearchRequestRelevanceScoreSpec
    relevanceThreshold: typing.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    safeSearch: bool
    searchAddonSpec: GoogleCloudDiscoveryengineV1betaSearchRequestSearchAddonSpec
    searchAsYouTypeSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestSearchAsYouTypeSpec
    )
    servingConfig: str
    session: str
    sessionSpec: GoogleCloudDiscoveryengineV1betaSearchRequestSessionSpec
    spellCorrectionSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestSpellCorrectionSpec
    )
    userInfo: GoogleCloudDiscoveryengineV1betaUserInfo
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec(
    typing.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing.TypedDict, total=False
):
    attributeType: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing.Literal["INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec(
    typing.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec
    searchResultMode: typing.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    snippetSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSnippetSpec
    )
    summarySpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecChunkSpec(
    typing.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec(
    typing.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSnippetSpec(
    typing.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpec(
    typing.TypedDict, total=False
):
    ignoreAdversarialQuery: bool
    ignoreJailBreakingQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelSpec
    multimodalSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecMultiModalSpec
    summaryResultCount: int
    useSemanticChunks: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelPromptSpec(
    typing.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelSpec(
    typing.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecMultiModalSpec(
    typing.TypedDict, total=False
):
    imageSource: typing.Literal[
        "IMAGE_SOURCE_UNSPECIFIED",
        "ALL_AVAILABLE_SOURCES",
        "CORPUS_IMAGE_ONLY",
        "FIGURE_GENERATION_ONLY",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestCrowdingSpec(
    typing.TypedDict, total=False
):
    field: str
    maxCount: int
    mode: typing.Literal[
        "MODE_UNSPECIFIED", "DROP_CROWDED_RESULTS", "DEMOTE_CROWDED_RESULTS_TO_END"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestCustomRankingParams(
    typing.TypedDict, total=False
):
    expressionsToPrecompute: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestDataStoreSpec(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec
    customSearchOperators: str
    dataStore: str
    filter: str
    numResults: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestDisplaySpec(
    typing.TypedDict, total=False
):
    matchHighlightingCondition: typing.Literal[
        "MATCH_HIGHLIGHTING_CONDITION_UNSPECIFIED",
        "MATCH_HIGHLIGHTING_DISABLED",
        "MATCH_HIGHLIGHTING_ENABLED",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpec(
    typing.TypedDict, total=False
):
    embeddingVectors: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpecEmbeddingVector
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpecEmbeddingVector(
    typing.TypedDict, total=False
):
    fieldPath: str
    vector: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpec(
    typing.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpecFacetKey(
    typing.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudDiscoveryengineV1betaInterval]
    key: str
    orderBy: str
    prefixes: _list[str]
    restrictedValues: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestImageQuery(
    typing.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestNaturalLanguageQueryUnderstandingSpec(
    typing.TypedDict, total=False
):
    allowedFieldNames: _list[str]
    extractedFilterBehavior: typing.Literal[
        "EXTRACTED_FILTER_BEHAVIOR_UNSPECIFIED", "HARD_FILTER", "SOFT_BOOST"
    ]
    filterExtractionCondition: typing.Literal[
        "CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    geoSearchQueryDetectionFieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestPersonalizationSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestRelevanceFilterSpec(
    typing.TypedDict, total=False
):
    keywordSearchThreshold: GoogleCloudDiscoveryengineV1betaSearchRequestRelevanceFilterSpecRelevanceThresholdSpec
    semanticSearchThreshold: GoogleCloudDiscoveryengineV1betaSearchRequestRelevanceFilterSpecRelevanceThresholdSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestRelevanceFilterSpecRelevanceThresholdSpec(
    typing.TypedDict, total=False
):
    relevanceThreshold: typing.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    semanticRelevanceThreshold: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestRelevanceScoreSpec(
    typing.TypedDict, total=False
):
    returnRelevanceScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSearchAddonSpec(
    typing.TypedDict, total=False
):
    disableGenerativeAnswerAddOn: bool
    disableKpiPersonalizationAddOn: bool
    disableSemanticAddOn: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSearchAsYouTypeSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSessionSpec(
    typing.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSpellCorrectionSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSetDedicatedCrawlRateMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSetDedicatedCrawlRateResponse(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSingleRegionKey(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSiteVerificationInfo(
    typing.TypedDict, total=False
):
    siteVerificationState: typing.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSitemap(typing.TypedDict, total=False):
    createTime: str
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSite(typing.TypedDict, total=False):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing.Literal[
        "INDEXING_STATUS_UNSPECIFIED",
        "PENDING",
        "FAILED",
        "SUCCEEDED",
        "DELETING",
        "CANCELLABLE",
        "CANCELLED",
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1betaSiteVerificationInfo
    type: typing.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason(
    typing.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1betaTargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSiteFailureReasonQuotaFailure(
    typing.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTrainCustomModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTrainCustomModelResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTuneEngineMetadata(typing.TypedDict, total=False):
    engine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTuneEngineResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUpdateSchemaMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUpdateTargetSiteMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserInfo(typing.TypedDict, total=False):
    preciseLocation: GoogleCloudDiscoveryengineV1betaUserInfoPreciseLocation
    timeZone: str
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserInfoPreciseLocation(
    typing.TypedDict, total=False
):
    address: str
    point: GoogleTypeLatLng

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserLicense(typing.TypedDict, total=False):
    createTime: str
    lastLoginTime: str
    licenseAssignmentState: typing.Literal[
        "LICENSE_ASSIGNMENT_STATE_UNSPECIFIED",
        "ASSIGNED",
        "UNASSIGNED",
        "NO_LICENSE",
        "NO_LICENSE_ATTEMPTED_LOGIN",
        "BLOCKED",
    ]
    licenseConfig: str
    updateTime: str
    userPrincipal: str
    userProfile: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserStore(typing.TypedDict, total=False):
    defaultLicenseConfig: str
    displayName: str
    enableExpiredLicenseAutoUpdate: bool
    enableLicenseAutoRegister: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaWorkspaceConfig(typing.TypedDict, total=False):
    dasherCustomerId: str
    superAdminEmailAddress: str
    superAdminServiceAccount: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "GOOGLE_DRIVE",
        "GOOGLE_MAIL",
        "GOOGLE_SITES",
        "GOOGLE_CALENDAR",
        "GOOGLE_CHAT",
        "GOOGLE_GROUPS",
        "GOOGLE_KEEP",
        "GOOGLE_PEOPLE",
        "GOOGLE_WORKSPACE",
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

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
class GoogleMonitoringV3Point(typing.TypedDict, total=False):
    interval: GoogleMonitoringV3TimeInterval
    value: GoogleMonitoringV3TypedValue

@typing.type_check_only
class GoogleMonitoringV3TimeInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleMonitoringV3TimeSeries(typing.TypedDict, total=False):
    description: str
    metadata: GoogleApiMonitoredResourceMetadata
    metric: GoogleApiMetric
    metricKind: typing.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    points: _list[GoogleMonitoringV3Point]
    resource: GoogleApiMonitoredResource
    unit: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]

@typing.type_check_only
class GoogleMonitoringV3TypedValue(typing.TypedDict, total=False):
    boolValue: bool
    distributionValue: GoogleApiDistribution
    doubleValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeDateTime(typing.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: GoogleTypeTimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleTypeLatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class GoogleTypeTimeZone(typing.TypedDict, total=False):
    id: str
    version: str
