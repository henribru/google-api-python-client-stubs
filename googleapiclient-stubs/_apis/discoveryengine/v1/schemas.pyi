import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiDistribution(typing_extensions.TypedDict, total=False):
    bucketCounts: _list[str]
    bucketOptions: GoogleApiDistributionBucketOptions
    count: str
    exemplars: _list[GoogleApiDistributionExemplar]
    mean: float
    range: GoogleApiDistributionRange
    sumOfSquaredDeviation: float

@typing.type_check_only
class GoogleApiDistributionBucketOptions(typing_extensions.TypedDict, total=False):
    explicitBuckets: GoogleApiDistributionBucketOptionsExplicit
    exponentialBuckets: GoogleApiDistributionBucketOptionsExponential
    linearBuckets: GoogleApiDistributionBucketOptionsLinear

@typing.type_check_only
class GoogleApiDistributionBucketOptionsExplicit(
    typing_extensions.TypedDict, total=False
):
    bounds: _list[float]

@typing.type_check_only
class GoogleApiDistributionBucketOptionsExponential(
    typing_extensions.TypedDict, total=False
):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

@typing.type_check_only
class GoogleApiDistributionBucketOptionsLinear(
    typing_extensions.TypedDict, total=False
):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class GoogleApiDistributionExemplar(typing_extensions.TypedDict, total=False):
    attachments: _list[dict[str, typing.Any]]
    timestamp: str
    value: float

@typing.type_check_only
class GoogleApiDistributionRange(typing_extensions.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleApiMetric(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleApiMonitoredResource(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleApiMonitoredResourceMetadata(typing_extensions.TypedDict, total=False):
    systemLabels: dict[str, typing.Any]
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingErrorContext(
    typing_extensions.TypedDict, total=False
):
    httpRequest: GoogleCloudDiscoveryengineLoggingHttpRequestContext
    reportLocation: GoogleCloudDiscoveryengineLoggingSourceLocation

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingErrorLog(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudDiscoveryengineLoggingErrorContext
    importPayload: GoogleCloudDiscoveryengineLoggingImportErrorContext
    message: str
    requestPayload: dict[str, typing.Any]
    responsePayload: dict[str, typing.Any]
    serviceContext: GoogleCloudDiscoveryengineLoggingServiceContext
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingHttpRequestContext(
    typing_extensions.TypedDict, total=False
):
    responseStatusCode: int

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingImportErrorContext(
    typing_extensions.TypedDict, total=False
):
    document: str
    gcsPath: str
    lineNumber: str
    operation: str
    userEvent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingServiceContext(
    typing_extensions.TypedDict, total=False
):
    service: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingSourceLocation(
    typing_extensions.TypedDict, total=False
):
    functionName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AdvancedSiteSearchConfig(
    typing_extensions.TypedDict, total=False
):
    disableAutomaticRefresh: bool
    disableInitialIndex: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AlloyDbSource(
    typing_extensions.TypedDict, total=False
):
    clusterId: str
    databaseId: str
    gcsStagingDir: str
    locationId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Answer(typing_extensions.TypedDict, total=False):
    answerSkippedReasons: _list[
        typing_extensions.Literal[
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "STREAMING"
    ]
    steps: _list[GoogleCloudDiscoveryengineV1AnswerStep]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerCitation(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1AnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerCitationSource(
    typing_extensions.TypedDict, total=False
):
    referenceId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerGroundingSupport(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    groundingCheckRequired: bool
    groundingScore: float
    sources: _list[GoogleCloudDiscoveryengineV1AnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequest(
    typing_extensions.TypedDict, total=False
):
    answerGenerationSpec: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpec
    )
    asynchronousMode: bool
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
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    modelVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestAnswerGenerationSpecPromptSpec(
    typing_extensions.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestGroundingSpec(
    typing_extensions.TypedDict, total=False
):
    filteringLevel: typing_extensions.Literal[
        "FILTERING_LEVEL_UNSPECIFIED", "FILTERING_LEVEL_LOW", "FILTERING_LEVEL_HIGH"
    ]
    includeGroundingSupports: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpec(
    typing_extensions.TypedDict, total=False
):
    queryClassificationSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec
    queryRephraserSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec(
    typing_extensions.TypedDict, total=False
):
    types: _list[
        typing_extensions.Literal[
            "TYPE_UNSPECIFIED",
            "ADVERSARIAL_QUERY",
            "NON_ANSWER_SEEKING_QUERY",
            "JAIL_BREAKING_QUERY",
            "NON_ANSWER_SEEKING_QUERY_V2",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec(
    typing_extensions.TypedDict, total=False
):
    disable: bool
    maxRephraseSteps: int
    modelSpec: GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpecModelSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpecModelSpec(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal["MODEL_TYPE_UNSPECIFIED", "SMALL", "LARGE"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestRelatedQuestionsSpec(
    typing_extensions.TypedDict, total=False
):
    enable: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSafetySpec(
    typing_extensions.TypedDict, total=False
):
    enable: bool
    safetySettings: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSafetySpecSafetySetting
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSafetySpecSafetySetting(
    typing_extensions.TypedDict, total=False
):
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    threshold: typing_extensions.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpec(
    typing_extensions.TypedDict, total=False
):
    searchParams: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchParams
    searchResultList: (
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultList
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchParams(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestDataStoreSpec]
    filter: str
    maxReturnResults: int
    orderBy: str
    searchResultMode: typing_extensions.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultList(
    typing_extensions.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResult(
    typing_extensions.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo
    unstructuredDocumentInfo: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo(
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str
    documentMetadata: GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfoDocumentMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfoDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveAnswer(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveSegment(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryResponse(
    typing_extensions.TypedDict, total=False
):
    answer: GoogleCloudDiscoveryengineV1Answer
    answerQueryToken: str
    session: GoogleCloudDiscoveryengineV1Session

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryUnderstandingInfo(
    typing_extensions.TypedDict, total=False
):
    queryClassificationInfo: _list[
        GoogleCloudDiscoveryengineV1AnswerQueryUnderstandingInfoQueryClassificationInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryUnderstandingInfoQueryClassificationInfo(
    typing_extensions.TypedDict, total=False
):
    positive: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "ADVERSARIAL_QUERY",
        "NON_ANSWER_SEEKING_QUERY",
        "JAIL_BREAKING_QUERY",
        "NON_ANSWER_SEEKING_QUERY_V2",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReference(
    typing_extensions.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfo
    structuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1AnswerReferenceStructuredDocumentInfo
    )
    unstructuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1AnswerReferenceUnstructuredDocumentInfo
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfo(
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str
    documentMetadata: (
        GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfoDocumentMetadata
    )
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceChunkInfoDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    document: str
    pageIdentifier: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceStructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    document: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerReferenceUnstructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStep(typing_extensions.TypedDict, total=False):
    actions: _list[GoogleCloudDiscoveryengineV1AnswerStepAction]
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED"
    ]
    thought: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepAction(
    typing_extensions.TypedDict, total=False
):
    observation: GoogleCloudDiscoveryengineV1AnswerStepActionObservation
    searchAction: GoogleCloudDiscoveryengineV1AnswerStepActionSearchAction

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionObservation(
    typing_extensions.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResult(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionObservationSearchResultSnippetInfo(
    typing_extensions.TypedDict, total=False
):
    snippet: str
    snippetStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerStepActionSearchAction(
    typing_extensions.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSitesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudDiscoveryengineV1CreateTargetSiteRequest]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponse(
    typing_extensions.TypedDict, total=False
):
    documentsMetadata: _list[
        GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadata
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    dataIngestionSource: str
    lastRefreshedTime: str
    matcherValue: GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadataMatcherValue
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "INDEXED", "NOT_IN_TARGET_SITE", "NOT_IN_INDEX"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseDocumentMetadataMatcherValue(
    typing_extensions.TypedDict, total=False
):
    fhirResource: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchVerifyTargetSitesRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigQuerySource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigtableOptions(
    typing_extensions.TypedDict, total=False
):
    families: dict[str, typing.Any]
    keyFieldName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BigtableOptionsBigtableColumn(
    typing_extensions.TypedDict, total=False
):
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "TEXT", "BINARY"]
    fieldName: str
    qualifier: str
    type: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    columns: _list[GoogleCloudDiscoveryengineV1BigtableOptionsBigtableColumn]
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "TEXT", "BINARY"]
    fieldName: str
    type: typing_extensions.Literal[
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
class GoogleCloudDiscoveryengineV1BigtableSource(
    typing_extensions.TypedDict, total=False
):
    bigtableOptions: GoogleCloudDiscoveryengineV1BigtableOptions
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingRequest(
    typing_extensions.TypedDict, total=False
):
    answerCandidate: str
    facts: _list[GoogleCloudDiscoveryengineV1GroundingFact]
    groundingSpec: GoogleCloudDiscoveryengineV1CheckGroundingSpec
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingResponse(
    typing_extensions.TypedDict, total=False
):
    citedChunks: _list[GoogleCloudDiscoveryengineV1FactChunk]
    citedFacts: _list[
        GoogleCloudDiscoveryengineV1CheckGroundingResponseCheckGroundingFactChunk
    ]
    claims: _list[GoogleCloudDiscoveryengineV1CheckGroundingResponseClaim]
    supportScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingResponseCheckGroundingFactChunk(
    typing_extensions.TypedDict, total=False
):
    chunkText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingResponseClaim(
    typing_extensions.TypedDict, total=False
):
    citationIndices: _list[int]
    claimText: str
    endPos: int
    groundingCheckRequired: bool
    startPos: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingSpec(
    typing_extensions.TypedDict, total=False
):
    citationThreshold: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Chunk(typing_extensions.TypedDict, total=False):
    chunkMetadata: GoogleCloudDiscoveryengineV1ChunkChunkMetadata
    content: str
    derivedStructData: dict[str, typing.Any]
    documentMetadata: GoogleCloudDiscoveryengineV1ChunkDocumentMetadata
    id: str
    name: str
    pageSpan: GoogleCloudDiscoveryengineV1ChunkPageSpan
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkChunkMetadata(
    typing_extensions.TypedDict, total=False
):
    nextChunks: _list[GoogleCloudDiscoveryengineV1Chunk]
    previousChunks: _list[GoogleCloudDiscoveryengineV1Chunk]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ChunkPageSpan(
    typing_extensions.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CloudSqlSource(
    typing_extensions.TypedDict, total=False
):
    databaseId: str
    gcsStagingDir: str
    instanceId: str
    offload: bool
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CmekConfig(typing_extensions.TypedDict, total=False):
    isDefault: bool
    kmsKey: str
    kmsKeyVersion: str
    lastRotationTimestampMicros: str
    name: str
    singleRegionKeys: _list[GoogleCloudDiscoveryengineV1SingleRegionKey]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "KEY_ISSUE",
        "DELETING",
        "UNUSABLE",
        "ACTIVE_ROTATING",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompleteQueryResponse(
    typing_extensions.TypedDict, total=False
):
    querySuggestions: _list[
        GoogleCloudDiscoveryengineV1CompleteQueryResponseQuerySuggestion
    ]
    tailMatchTriggered: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompleteQueryResponseQuerySuggestion(
    typing_extensions.TypedDict, total=False
):
    completableFieldPaths: _list[str]
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompletionInfo(
    typing_extensions.TypedDict, total=False
):
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompletionSuggestion(
    typing_extensions.TypedDict, total=False
):
    alternativePhrases: _list[str]
    frequency: str
    globalScore: float
    groupId: str
    groupScore: float
    languageCode: str
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Condition(typing_extensions.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1ConditionTimeRange]
    queryRegex: str
    queryTerms: _list[GoogleCloudDiscoveryengineV1ConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Control(typing_extensions.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1ControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1Condition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1ControlFilterAction
    name: str
    promoteAction: GoogleCloudDiscoveryengineV1ControlPromoteAction
    redirectAction: GoogleCloudDiscoveryengineV1ControlRedirectAction
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1ControlSynonymsAction
    useCases: _list[
        typing_extensions.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlBoostAction(
    typing_extensions.TypedDict, total=False
):
    boost: float
    dataStore: str
    filter: str
    fixedBoost: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlFilterAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlPromoteAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    searchLinkPromotion: GoogleCloudDiscoveryengineV1SearchLinkPromotion

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlSynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Conversation(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    messages: _list[GoogleCloudDiscoveryengineV1ConversationMessage]
    name: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETED"]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConversationContext(
    typing_extensions.TypedDict, total=False
):
    activeDocument: str
    contextDocuments: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConversationMessage(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    reply: GoogleCloudDiscoveryengineV1Reply
    userInput: GoogleCloudDiscoveryengineV1TextInput

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConverseConversationRequest(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    conversation: GoogleCloudDiscoveryengineV1Conversation
    reply: GoogleCloudDiscoveryengineV1Reply
    searchResults: _list[GoogleCloudDiscoveryengineV1SearchResponseSearchResult]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateTargetSiteRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    targetSite: GoogleCloudDiscoveryengineV1TargetSite

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CustomAttribute(
    typing_extensions.TypedDict, total=False
):
    numbers: _list[float]
    text: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CustomTuningModel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    errorMessage: str
    metrics: dict[str, typing.Any]
    modelState: typing_extensions.Literal[
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
class GoogleCloudDiscoveryengineV1DataStore(typing_extensions.TypedDict, total=False):
    advancedSiteSearchConfig: GoogleCloudDiscoveryengineV1AdvancedSiteSearchConfig
    billingEstimation: GoogleCloudDiscoveryengineV1DataStoreBillingEstimation
    cmekConfig: GoogleCloudDiscoveryengineV1CmekConfig
    contentConfig: typing_extensions.Literal[
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
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    isInfobotFaqDataStore: bool
    kmsKeyName: str
    name: str
    servingConfigDataStore: GoogleCloudDiscoveryengineV1DataStoreServingConfigDataStore
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1Schema
    workspaceConfig: GoogleCloudDiscoveryengineV1WorkspaceConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreBillingEstimation(
    typing_extensions.TypedDict, total=False
):
    structuredDataSize: str
    structuredDataUpdateTime: str
    unstructuredDataSize: str
    unstructuredDataUpdateTime: str
    websiteDataSize: str
    websiteDataUpdateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreServingConfigDataStore(
    typing_extensions.TypedDict, total=False
):
    disabledForServing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteIdentityMappingStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Document(typing_extensions.TypedDict, total=False):
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
class GoogleCloudDiscoveryengineV1DocumentContent(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    rawBytes: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentIndexStatus(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    indexTime: str
    pendingMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentInfo(
    typing_extensions.TypedDict, total=False
):
    conversionValue: float
    id: str
    joined: bool
    name: str
    promotionIds: _list[str]
    quantity: int
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfig
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Engine(typing_extensions.TypedDict, total=False):
    chatEngineConfig: GoogleCloudDiscoveryengineV1EngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1EngineChatEngineMetadata
    commonConfig: GoogleCloudDiscoveryengineV1EngineCommonConfig
    createTime: str
    dataStoreIds: _list[str]
    disableAnalytics: bool
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    name: str
    searchEngineConfig: GoogleCloudDiscoveryengineV1EngineSearchEngineConfig
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineConfig(
    typing_extensions.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1EngineChatEngineConfigAgentCreationConfig
    )
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineConfigAgentCreationConfig(
    typing_extensions.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineCommonConfig(
    typing_extensions.TypedDict, total=False
):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineSearchEngineConfig(
    typing_extensions.TypedDict, total=False
):
    searchAddOns: _list[
        typing_extensions.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing_extensions.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FactChunk(typing_extensions.TypedDict, total=False):
    chunkText: str
    index: int
    source: str
    sourceMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FhirStoreSource(
    typing_extensions.TypedDict, total=False
):
    fhirStore: str
    gcsStagingDir: str
    resourceTypes: _list[str]
    updateFromLatestPredefinedSchema: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FirestoreSource(
    typing_extensions.TypedDict, total=False
):
    collectionId: str
    databaseId: str
    gcsStagingDir: str
    projectId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GcsSource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequest(
    typing_extensions.TypedDict, total=False
):
    contents: _list[GoogleCloudDiscoveryengineV1GroundedGenerationContent]
    generationSpec: (
        GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGenerationSpec
    )
    groundingSpec: (
        GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSpec
    )
    systemInstruction: GoogleCloudDiscoveryengineV1GroundedGenerationContent
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestDynamicRetrievalConfiguration(
    typing_extensions.TypedDict, total=False
):
    predictor: GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestDynamicRetrievalConfigurationDynamicRetrievalPredictor

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestDynamicRetrievalConfigurationDynamicRetrievalPredictor(
    typing_extensions.TypedDict, total=False
):
    threshold: float
    version: typing_extensions.Literal["VERSION_UNSPECIFIED", "V1_INDEPENDENT"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGenerationSpec(
    typing_extensions.TypedDict, total=False
):
    frequencyPenalty: float
    languageCode: str
    maxOutputTokens: int
    modelId: str
    presencePenalty: float
    seed: int
    temperature: float
    topK: int
    topP: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSource(
    typing_extensions.TypedDict, total=False
):
    googleSearchSource: GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSourceGoogleSearchSource
    inlineSource: GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSourceInlineSource
    searchSource: GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSourceSearchSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSourceGoogleSearchSource(
    typing_extensions.TypedDict, total=False
):
    dynamicRetrievalConfig: GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestDynamicRetrievalConfiguration

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSourceInlineSource(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    groundingFacts: _list[GoogleCloudDiscoveryengineV1GroundingFact]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSourceSearchSource(
    typing_extensions.TypedDict, total=False
):
    filter: str
    maxResultCount: int
    safeSearch: bool
    servingConfig: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSpec(
    typing_extensions.TypedDict, total=False
):
    groundingSources: _list[
        GoogleCloudDiscoveryengineV1GenerateGroundedContentRequestGroundingSource
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponse(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[
        GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidate
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidate(
    typing_extensions.TypedDict, total=False
):
    content: GoogleCloudDiscoveryengineV1GroundedGenerationContent
    groundingMetadata: GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadata
    groundingScore: float
    index: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadata(
    typing_extensions.TypedDict, total=False
):
    groundingSupport: _list[
        GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataGroundingSupport
    ]
    retrievalMetadata: _list[
        GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataRetrievalMetadata
    ]
    searchEntryPoint: GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataSearchEntryPoint
    supportChunks: _list[GoogleCloudDiscoveryengineV1FactChunk]
    webSearchQueries: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataDynamicRetrievalMetadata(
    typing_extensions.TypedDict, total=False
):
    predictorMetadata: GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataDynamicRetrievalPredictorMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataDynamicRetrievalPredictorMetadata(
    typing_extensions.TypedDict, total=False
):
    prediction: float
    version: typing_extensions.Literal["VERSION_UNSPECIFIED", "V1_INDEPENDENT"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataGroundingSupport(
    typing_extensions.TypedDict, total=False
):
    claimText: str
    supportChunkIndices: _list[int]
    supportScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataRetrievalMetadata(
    typing_extensions.TypedDict, total=False
):
    dynamicRetrievalMetadata: GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataDynamicRetrievalMetadata
    source: typing_extensions.Literal[
        "SOURCE_UNSPECIFIED",
        "VERTEX_AI_SEARCH",
        "GOOGLE_SEARCH",
        "INLINE_CONTENT",
        "GOOGLE_MAPS",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseCandidateGroundingMetadataSearchEntryPoint(
    typing_extensions.TypedDict, total=False
):
    renderedContent: str
    sdkBlob: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GroundedGenerationContent(
    typing_extensions.TypedDict, total=False
):
    parts: _list[GoogleCloudDiscoveryengineV1GroundedGenerationContentPart]
    role: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GroundedGenerationContentPart(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GroundingFact(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    factText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1BigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    suggestions: _list[GoogleCloudDiscoveryengineV1CompletionSuggestion]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
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
    reconciliationMode: typing_extensions.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    spannerSource: GoogleCloudDiscoveryengineV1SpannerSource
    updateMask: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1Document]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequest(
    typing_extensions.TypedDict, total=False
):
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleCloudDiscoveryengineV1SuggestionDenyListEntry]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1BigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: GoogleCloudDiscoveryengineV1ImportUserEventsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudDiscoveryengineV1UserEvent]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Interval(typing_extensions.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListControlsResponse(
    typing_extensions.TypedDict, total=False
):
    controls: _list[GoogleCloudDiscoveryengineV1Control]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversations: _list[GoogleCloudDiscoveryengineV1Conversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListCustomModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudDiscoveryengineV1CustomTuningModel]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListDataStoresResponse(
    typing_extensions.TypedDict, total=False
):
    dataStores: _list[GoogleCloudDiscoveryengineV1DataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1Document]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListEnginesResponse(
    typing_extensions.TypedDict, total=False
):
    engines: _list[GoogleCloudDiscoveryengineV1Engine]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListSchemasResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    schemas: _list[GoogleCloudDiscoveryengineV1Schema]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListSessionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessions: _list[GoogleCloudDiscoveryengineV1Session]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1MediaInfo(typing_extensions.TypedDict, total=False):
    mediaProgressDuration: str
    mediaProgressPercentage: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PageInfo(typing_extensions.TypedDict, total=False):
    pageCategory: str
    pageviewId: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PanelInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    documents: _list[GoogleCloudDiscoveryengineV1DocumentInfo]
    panelId: str
    panelPosition: int
    totalPanels: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Project(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectServiceTerms(
    typing_extensions.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProvisionProjectMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProvisionProjectRequest(
    typing_extensions.TypedDict, total=False
):
    acceptDataUseTerms: bool
    dataUseTermsVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeSucceeded: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1PurgeErrorConfig
    filter: str
    force: bool
    gcsSource: GoogleCloudDiscoveryengineV1GcsSource
    inlineSource: GoogleCloudDiscoveryengineV1PurgeDocumentsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    documents: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Query(typing_extensions.TypedDict, total=False):
    queryId: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RankRequest(typing_extensions.TypedDict, total=False):
    ignoreRecordDetailsInResponse: bool
    model: str
    query: str
    records: _list[GoogleCloudDiscoveryengineV1RankingRecord]
    topN: int
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RankResponse(
    typing_extensions.TypedDict, total=False
):
    records: _list[GoogleCloudDiscoveryengineV1RankingRecord]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RankingRecord(
    typing_extensions.TypedDict, total=False
):
    content: str
    id: str
    score: float
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecommendRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    params: dict[str, typing.Any]
    userEvent: GoogleCloudDiscoveryengineV1UserEvent
    userLabels: dict[str, typing.Any]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecommendResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudDiscoveryengineV1RecommendResponseRecommendationResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecommendResponseRecommendationResult(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDiscoveryengineV1Document
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecrawlUrisRequest(
    typing_extensions.TypedDict, total=False
):
    siteCredential: str
    uris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Reply(typing_extensions.TypedDict, total=False):
    summary: GoogleCloudDiscoveryengineV1SearchResponseSummary

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SafetyRating(
    typing_extensions.TypedDict, total=False
):
    blocked: bool
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    probability: typing_extensions.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]
    probabilityScore: float
    severity: typing_extensions.Literal[
        "HARM_SEVERITY_UNSPECIFIED",
        "HARM_SEVERITY_NEGLIGIBLE",
        "HARM_SEVERITY_LOW",
        "HARM_SEVERITY_MEDIUM",
        "HARM_SEVERITY_HIGH",
    ]
    severityScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Schema(typing_extensions.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchInfo(typing_extensions.TypedDict, total=False):
    offset: int
    orderBy: str
    searchQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchLinkPromotion(
    typing_extensions.TypedDict, total=False
):
    description: str
    enabled: bool
    imageUri: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestDataStoreSpec]
    facetSpecs: _list[GoogleCloudDiscoveryengineV1SearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1SearchRequestImageQuery
    languageCode: str
    offset: int
    oneBoxPageSize: int
    orderBy: str
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1SearchRequestQueryExpansionSpec
    safeSearch: bool
    searchAsYouTypeSpec: GoogleCloudDiscoveryengineV1SearchRequestSearchAsYouTypeSpec
    session: str
    sessionSpec: GoogleCloudDiscoveryengineV1SearchRequestSessionSpec
    spellCorrectionSpec: GoogleCloudDiscoveryengineV1SearchRequestSpellCorrectionSpec
    userInfo: GoogleCloudDiscoveryengineV1UserInfo
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpec(
    typing_extensions.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: (
        GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecExtractiveContentSpec
    )
    searchResultMode: typing_extensions.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    snippetSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSnippetSpec
    summarySpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecChunkSpec(
    typing_extensions.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecExtractiveContentSpec(
    typing_extensions.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSnippetSpec(
    typing_extensions.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpec(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpecSummarySpecModelSpec(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestDataStoreSpec(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1SearchRequestBoostSpec
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1SearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestSearchAsYouTypeSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestSessionSpec(
    typing_extensions.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    correctedQuery: str
    facets: _list[GoogleCloudDiscoveryengineV1SearchResponseFacet]
    nextPageToken: str
    queryExpansionInfo: GoogleCloudDiscoveryengineV1SearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudDiscoveryengineV1SearchResponseSearchResult]
    searchLinkPromotions: _list[GoogleCloudDiscoveryengineV1SearchLinkPromotion]
    sessionInfo: GoogleCloudDiscoveryengineV1SearchResponseSessionInfo
    summary: GoogleCloudDiscoveryengineV1SearchResponseSummary
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseFacet(
    typing_extensions.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudDiscoveryengineV1SearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseFacetFacetValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    interval: GoogleCloudDiscoveryengineV1Interval
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseQueryExpansionInfo(
    typing_extensions.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSearchResult(
    typing_extensions.TypedDict, total=False
):
    chunk: GoogleCloudDiscoveryengineV1Chunk
    document: GoogleCloudDiscoveryengineV1Document
    id: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSessionInfo(
    typing_extensions.TypedDict, total=False
):
    name: str
    queryId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummary(
    typing_extensions.TypedDict, total=False
):
    safetyAttributes: GoogleCloudDiscoveryengineV1SearchResponseSummarySafetyAttributes
    summarySkippedReasons: _list[
        typing_extensions.Literal[
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
        ]
    ]
    summaryText: str
    summaryWithMetadata: (
        GoogleCloudDiscoveryengineV1SearchResponseSummarySummaryWithMetadata
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryCitation(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationMetadata(
    typing_extensions.TypedDict, total=False
):
    citations: _list[GoogleCloudDiscoveryengineV1SearchResponseSummaryCitation]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationSource(
    typing_extensions.TypedDict, total=False
):
    referenceIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryReference(
    typing_extensions.TypedDict, total=False
):
    chunkContents: _list[
        GoogleCloudDiscoveryengineV1SearchResponseSummaryReferenceChunkContent
    ]
    document: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummaryReferenceChunkContent(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummarySafetyAttributes(
    typing_extensions.TypedDict, total=False
):
    categories: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseSummarySummaryWithMetadata(
    typing_extensions.TypedDict, total=False
):
    citationMetadata: GoogleCloudDiscoveryengineV1SearchResponseSummaryCitationMetadata
    references: _list[GoogleCloudDiscoveryengineV1SearchResponseSummaryReference]
    summary: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ServingConfig(
    typing_extensions.TypedDict, total=False
):
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
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsControlIds: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ServingConfigGenericConfig(
    typing_extensions.TypedDict, total=False
):
    contentSearchSpec: GoogleCloudDiscoveryengineV1SearchRequestContentSearchSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ServingConfigMediaConfig(
    typing_extensions.TypedDict, total=False
):
    contentFreshnessCutoffDays: int
    contentWatchedPercentageThreshold: float
    contentWatchedSecondsThreshold: float
    demoteContentWatchedPastDays: int
    demotionEventType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Session(typing_extensions.TypedDict, total=False):
    displayName: str
    endTime: str
    isPinned: bool
    name: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "IN_PROGRESS"]
    turns: _list[GoogleCloudDiscoveryengineV1SessionTurn]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SessionTurn(typing_extensions.TypedDict, total=False):
    answer: str
    detailedAnswer: GoogleCloudDiscoveryengineV1Answer
    query: GoogleCloudDiscoveryengineV1Query

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SingleRegionKey(
    typing_extensions.TypedDict, total=False
):
    kmsKey: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SiteSearchEngine(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SpannerSource(
    typing_extensions.TypedDict, total=False
):
    databaseId: str
    enableDataBoost: bool
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SuggestionDenyListEntry(
    typing_extensions.TypedDict, total=False
):
    blockPhrase: str
    matchOperator: typing_extensions.Literal[
        "MATCH_OPERATOR_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSite(typing_extensions.TypedDict, total=False):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1TargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing_extensions.Literal[
        "INDEXING_STATUS_UNSPECIFIED", "PENDING", "FAILED", "SUCCEEDED", "DELETING"
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1SiteVerificationInfo
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSiteFailureReason(
    typing_extensions.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1TargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSiteFailureReasonQuotaFailure(
    typing_extensions.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TextInput(typing_extensions.TypedDict, total=False):
    context: GoogleCloudDiscoveryengineV1ConversationContext
    input: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelRequest(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    gcsTrainingInput: (
        GoogleCloudDiscoveryengineV1TrainCustomModelRequestGcsTrainingInput
    )
    modelId: str
    modelType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelRequestGcsTrainingInput(
    typing_extensions.TypedDict, total=False
):
    corpusDataPath: str
    queryDataPath: str
    testDataPath: str
    trainDataPath: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TrainCustomModelResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TransactionInfo(
    typing_extensions.TypedDict, total=False
):
    cost: float
    currency: str
    discountValue: float
    tax: float
    transactionId: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateCmekConfigMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UserEvent(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    attributionToken: str
    completionInfo: GoogleCloudDiscoveryengineV1CompletionInfo
    conversionType: str
    dataStore: str
    directUserRequest: bool
    documents: _list[GoogleCloudDiscoveryengineV1DocumentInfo]
    engine: str
    eventTime: str
    eventType: str
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
class GoogleCloudDiscoveryengineV1UserInfo(typing_extensions.TypedDict, total=False):
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1WorkspaceConfig(
    typing_extensions.TypedDict, total=False
):
    dasherCustomerId: str
    superAdminEmailAddress: str
    superAdminServiceAccount: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "GOOGLE_DRIVE",
        "GOOGLE_MAIL",
        "GOOGLE_SITES",
        "GOOGLE_CALENDAR",
        "GOOGLE_CHAT",
        "GOOGLE_GROUPS",
        "GOOGLE_KEEP",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAclConfig(
    typing_extensions.TypedDict, total=False
):
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaActionConfig(
    typing_extensions.TypedDict, total=False
):
    actionParams: dict[str, typing.Any]
    isActionConfigured: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedSiteSearchConfig(
    typing_extensions.TypedDict, total=False
):
    disableAutomaticRefresh: bool
    disableInitialIndex: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswer(typing_extensions.TypedDict, total=False):
    answerSkippedReasons: _list[
        typing_extensions.Literal[
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
        ]
    ]
    answerText: str
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "STREAMING"
    ]
    steps: _list[GoogleCloudDiscoveryengineV1alphaAnswerStep]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerCitation(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerCitationSource(
    typing_extensions.TypedDict, total=False
):
    referenceId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerGroundingSupport(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    groundingCheckRequired: bool
    groundingScore: float
    sources: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfo(
    typing_extensions.TypedDict, total=False
):
    queryClassificationInfo: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfoQueryClassificationInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfoQueryClassificationInfo(
    typing_extensions.TypedDict, total=False
):
    positive: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "ADVERSARIAL_QUERY",
        "NON_ANSWER_SEEKING_QUERY",
        "JAIL_BREAKING_QUERY",
        "NON_ANSWER_SEEKING_QUERY_V2",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReference(
    typing_extensions.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfo
    structuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceStructuredDocumentInfo
    )
    unstructuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfo
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfo(
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str
    documentMetadata: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfoDocumentMetadata
    )
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfoDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    document: str
    pageIdentifier: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceStructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    document: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStep(
    typing_extensions.TypedDict, total=False
):
    actions: _list[GoogleCloudDiscoveryengineV1alphaAnswerStepAction]
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED"
    ]
    thought: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepAction(
    typing_extensions.TypedDict, total=False
):
    observation: GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservation
    searchAction: GoogleCloudDiscoveryengineV1alphaAnswerStepActionSearchAction

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservation(
    typing_extensions.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResult(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultSnippetInfo(
    typing_extensions.TypedDict, total=False
):
    snippet: str
    snippetStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionSearchAction(
    typing_extensions.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCmekConfig(
    typing_extensions.TypedDict, total=False
):
    isDefault: bool
    kmsKey: str
    kmsKeyVersion: str
    lastRotationTimestampMicros: str
    name: str
    singleRegionKeys: _list[GoogleCloudDiscoveryengineV1alphaSingleRegionKey]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "KEY_ISSUE",
        "DELETING",
        "UNUSABLE",
        "ACTIVE_ROTATING",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCollection(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataConnector: GoogleCloudDiscoveryengineV1alphaDataConnector
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCondition(
    typing_extensions.TypedDict, total=False
):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1alphaConditionTimeRange]
    queryRegex: str
    queryTerms: _list[GoogleCloudDiscoveryengineV1alphaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConnectorRun(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    entityRuns: _list[GoogleCloudDiscoveryengineV1alphaConnectorRunEntityRun]
    errors: _list[GoogleRpcStatus]
    latestPauseTime: str
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "OVERRUN",
        "CANCELLED",
        "PENDING",
        "WARNING",
    ]
    stateUpdateTime: str
    trigger: typing_extensions.Literal[
        "TRIGGER_UNSPECIFIED", "SCHEDULER", "INITIALIZATION", "RESUME", "MANUAL"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConnectorRunEntityRun(
    typing_extensions.TypedDict, total=False
):
    entityName: str
    errorRecordCount: str
    errors: _list[GoogleRpcStatus]
    extractedRecordCount: str
    indexedRecordCount: str
    sourceApiRequestCount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "OVERRUN",
        "CANCELLED",
        "PENDING",
        "WARNING",
    ]
    stateUpdateTime: str
    statsUpdateTime: str
    syncType: typing_extensions.Literal["SYNC_TYPE_UNSPECIFIED", "FULL", "INCREMENTAL"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControl(
    typing_extensions.TypedDict, total=False
):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1alphaControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1alphaCondition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1alphaControlFilterAction
    name: str
    promoteAction: GoogleCloudDiscoveryengineV1alphaControlPromoteAction
    redirectAction: GoogleCloudDiscoveryengineV1alphaControlRedirectAction
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1alphaControlSynonymsAction
    useCases: _list[
        typing_extensions.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlBoostAction(
    typing_extensions.TypedDict, total=False
):
    boost: float
    dataStore: str
    filter: str
    fixedBoost: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlFilterAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlPromoteAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    searchLinkPromotion: GoogleCloudDiscoveryengineV1alphaSearchLinkPromotion

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlSynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries(
    typing_extensions.TypedDict, total=False
):
    qpsTimeSeries: GoogleMonitoringV3TimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateEvaluationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateSitemapMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec(
    typing_extensions.TypedDict, total=False
):
    enableSearchAdaptor: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnector(
    typing_extensions.TypedDict, total=False
):
    actionConfig: GoogleCloudDiscoveryengineV1alphaActionConfig
    autoRunDisabled: bool
    blockingReasons: _list[
        typing_extensions.Literal[
            "BLOCKING_REASON_UNSPECIFIED",
            "ALLOWLIST_STATIC_IP",
            "ALLOWLIST_IN_SERVICE_ATTACHMENT",
        ]
    ]
    createTime: str
    dataSource: str
    destinationConfigs: _list[GoogleCloudDiscoveryengineV1alphaDestinationConfig]
    entities: _list[GoogleCloudDiscoveryengineV1alphaDataConnectorSourceEntity]
    errors: _list[GoogleRpcStatus]
    identityRefreshInterval: str
    identityScheduleConfig: GoogleCloudDiscoveryengineV1alphaIdentityScheduleConfig
    kmsKeyName: str
    lastSyncTime: str
    latestPauseTime: str
    name: str
    nextSyncTime: GoogleTypeDateTime
    params: dict[str, typing.Any]
    privateConnectivityProjectId: str
    refreshInterval: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "RUNNING", "WARNING"
    ]
    staticIpAddresses: _list[str]
    staticIpEnabled: bool
    syncMode: typing_extensions.Literal["PERIODIC"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorSourceEntity(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    entityName: str
    keyPropertyMappings: dict[str, typing.Any]
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStore(
    typing_extensions.TypedDict, total=False
):
    aclEnabled: bool
    advancedSiteSearchConfig: GoogleCloudDiscoveryengineV1alphaAdvancedSiteSearchConfig
    billingEstimation: GoogleCloudDiscoveryengineV1alphaDataStoreBillingEstimation
    cmekConfig: GoogleCloudDiscoveryengineV1alphaCmekConfig
    contentConfig: typing_extensions.Literal[
        "CONTENT_CONFIG_UNSPECIFIED",
        "NO_CONTENT",
        "CONTENT_REQUIRED",
        "PUBLIC_WEBSITE",
        "GOOGLE_WORKSPACE",
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    industryVertical: typing_extensions.Literal[
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
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1alphaSchema
    workspaceConfig: GoogleCloudDiscoveryengineV1alphaWorkspaceConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreBillingEstimation(
    typing_extensions.TypedDict, total=False
):
    structuredDataSize: str
    structuredDataUpdateTime: str
    unstructuredDataSize: str
    unstructuredDataUpdateTime: str
    websiteDataSize: str
    websiteDataUpdateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreServingConfigDataStore(
    typing_extensions.TypedDict, total=False
):
    disabledForServing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDedicatedCrawlRateTimeSeries(
    typing_extensions.TypedDict, total=False
):
    autoRefreshCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries
    userTriggeredCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteCollectionMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteIdentityMappingStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteSessionRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteSitemapMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDestinationConfig(
    typing_extensions.TypedDict, total=False
):
    destinations: _list[GoogleCloudDiscoveryengineV1alphaDestinationConfigDestination]
    key: str
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDestinationConfigDestination(
    typing_extensions.TypedDict, total=False
):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngine(typing_extensions.TypedDict, total=False):
    chatEngineConfig: GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata
    commonConfig: GoogleCloudDiscoveryengineV1alphaEngineCommonConfig
    createTime: str
    dataStoreIds: _list[str]
    disableAnalytics: bool
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    mediaRecommendationEngineConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig
    )
    name: str
    recommendationMetadata: (
        GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata
    )
    searchEngineConfig: GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig
    similarDocumentsConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfig
    )
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig(
    typing_extensions.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig
    )
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig(
    typing_extensions.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineCommonConfig(
    typing_extensions.TypedDict, total=False
):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig(
    typing_extensions.TypedDict, total=False
):
    optimizationObjective: str
    optimizationObjectiveConfig: GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig
    trainingState: typing_extensions.Literal[
        "TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"
    ]
    type: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    targetField: str
    targetFieldValueFloat: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata(
    typing_extensions.TypedDict, total=False
):
    dataState: typing_extensions.Literal[
        "DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"
    ]
    lastTuneTime: str
    servingState: typing_extensions.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    tuningOperation: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig(
    typing_extensions.TypedDict, total=False
):
    searchAddOns: _list[
        typing_extensions.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing_extensions.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeResponse(
    typing_extensions.TypedDict, total=False
):
    dataSizeBytes: str
    documentCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluation(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    errorSamples: _list[GoogleRpcStatus]
    evaluationSpec: GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpec
    name: str
    qualityMetrics: GoogleCloudDiscoveryengineV1alphaQualityMetrics
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpec(
    typing_extensions.TypedDict, total=False
):
    querySetSpec: GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpecQuerySetSpec
    searchRequest: GoogleCloudDiscoveryengineV1alphaSearchRequest

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpecQuerySetSpec(
    typing_extensions.TypedDict, total=False
):
    sampleQuerySet: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponse(
    typing_extensions.TypedDict, total=False
):
    sitemapsMetadata: _list[
        GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponseSitemapMetadata
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponseSitemapMetadata(
    typing_extensions.TypedDict, total=False
):
    sitemap: GoogleCloudDiscoveryengineV1alphaSitemap

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFieldConfig(
    typing_extensions.TypedDict, total=False
):
    advancedSiteSearchDataSources: _list[
        typing_extensions.Literal[
            "ADVANCED_SITE_SEARCH_DATA_SOURCE_UNSPECIFIED",
            "METATAGS",
            "PAGEMAP",
            "URI_PATTERN_MAPPING",
            "SCHEMA_ORG",
        ]
    ]
    completableOption: typing_extensions.Literal[
        "COMPLETABLE_OPTION_UNSPECIFIED", "COMPLETABLE_ENABLED", "COMPLETABLE_DISABLED"
    ]
    dynamicFacetableOption: typing_extensions.Literal[
        "DYNAMIC_FACETABLE_OPTION_UNSPECIFIED",
        "DYNAMIC_FACETABLE_ENABLED",
        "DYNAMIC_FACETABLE_DISABLED",
    ]
    fieldPath: str
    fieldType: typing_extensions.Literal[
        "FIELD_TYPE_UNSPECIFIED",
        "OBJECT",
        "STRING",
        "NUMBER",
        "INTEGER",
        "BOOLEAN",
        "GEOLOCATION",
        "DATETIME",
    ]
    indexableOption: typing_extensions.Literal[
        "INDEXABLE_OPTION_UNSPECIFIED", "INDEXABLE_ENABLED", "INDEXABLE_DISABLED"
    ]
    keyPropertyType: str
    metatagName: str
    recsFilterableOption: typing_extensions.Literal[
        "FILTERABLE_OPTION_UNSPECIFIED", "FILTERABLE_ENABLED", "FILTERABLE_DISABLED"
    ]
    retrievableOption: typing_extensions.Literal[
        "RETRIEVABLE_OPTION_UNSPECIFIED", "RETRIEVABLE_ENABLED", "RETRIEVABLE_DISABLED"
    ]
    schemaOrgPaths: _list[str]
    searchableOption: typing_extensions.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetSessionRequest(
    typing_extensions.TypedDict, total=False
):
    includeAnswerDetails: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetUriPatternDocumentDataResponse(
    typing_extensions.TypedDict, total=False
):
    documentDataMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdentityScheduleConfig(
    typing_extensions.TypedDict, total=False
):
    nextSyncTime: GoogleTypeDateTime
    refreshInterval: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdpConfig(
    typing_extensions.TypedDict, total=False
):
    externalIdpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfigExternalIdpConfig
    idpType: typing_extensions.Literal["IDP_TYPE_UNSPECIFIED", "GSUITE", "THIRD_PARTY"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdpConfigExternalIdpConfig(
    typing_extensions.TypedDict, total=False
):
    workforcePoolName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaInterval(
    typing_extensions.TypedDict, total=False
):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaLanguageInfo(
    typing_extensions.TypedDict, total=False
):
    language: str
    languageCode: str
    normalizedLanguageCode: str
    region: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSessionsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str
    parent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSessionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessions: _list[GoogleCloudDiscoveryengineV1alphaSession]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaNaturalLanguageQueryUnderstandingConfig(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaObtainCrawlRateResponse(
    typing_extensions.TypedDict, total=False
):
    dedicatedCrawlRateTimeSeries: (
        GoogleCloudDiscoveryengineV1alphaDedicatedCrawlRateTimeSeries
    )
    error: GoogleRpcStatus
    organicCrawlRateTimeSeries: (
        GoogleCloudDiscoveryengineV1alphaOrganicCrawlRateTimeSeries
    )
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaOrganicCrawlRateTimeSeries(
    typing_extensions.TypedDict, total=False
):
    googleOrganicCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries
    vertexAiOrganicCrawlRate: GoogleCloudDiscoveryengineV1alphaCrawlRateTimeSeries

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProject(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectServiceTerms(
    typing_extensions.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProvisionProjectMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeSucceeded: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQualityMetrics(
    typing_extensions.TypedDict, total=False
):
    docNdcg: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    docPrecision: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    docRecall: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    pageNdcg: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    pageRecall: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics(
    typing_extensions.TypedDict, total=False
):
    top1: float
    top10: float
    top3: float
    top5: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQuery(typing_extensions.TypedDict, total=False):
    queryId: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    invalidUris: _list[str]
    invalidUrisCount: int
    pendingCount: int
    quotaExceededCount: int
    successCount: int
    updateTime: str
    urisNotMatchingTargetSites: _list[str]
    urisNotMatchingTargetSitesCount: int
    validUrisCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponse(
    typing_extensions.TypedDict, total=False
):
    failedUris: _list[str]
    failureSamples: _list[
        GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfo(
    typing_extensions.TypedDict, total=False
):
    failureReasons: _list[
        GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason
    ]
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason(
    typing_extensions.TypedDict, total=False
):
    corpusType: typing_extensions.Literal[
        "CORPUS_TYPE_UNSPECIFIED", "DESKTOP", "MOBILE"
    ]
    errorMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveDedicatedCrawlRateMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveDedicatedCrawlRateResponse(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSafetyRating(
    typing_extensions.TypedDict, total=False
):
    blocked: bool
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    probability: typing_extensions.Literal[
        "HARM_PROBABILITY_UNSPECIFIED", "NEGLIGIBLE", "LOW", "MEDIUM", "HIGH"
    ]
    probabilityScore: float
    severity: typing_extensions.Literal[
        "HARM_SEVERITY_UNSPECIFIED",
        "HARM_SEVERITY_NEGLIGIBLE",
        "HARM_SEVERITY_LOW",
        "HARM_SEVERITY_MEDIUM",
        "HARM_SEVERITY_HIGH",
    ]
    severityScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSchema(typing_extensions.TypedDict, total=False):
    fieldConfigs: _list[GoogleCloudDiscoveryengineV1alphaFieldConfig]
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchLinkPromotion(
    typing_extensions.TypedDict, total=False
):
    description: str
    enabled: bool
    imageUri: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec
    customFineTuningSpec: GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec]
    embeddingSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpec
    facetSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1alphaSearchRequestImageQuery
    languageCode: str
    naturalLanguageQueryUnderstandingSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestNaturalLanguageQueryUnderstandingSpec
    offset: int
    oneBoxPageSize: int
    orderBy: str
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    personalizationSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestPersonalizationSpec
    )
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestQueryExpansionSpec
    rankingExpression: str
    regionCode: str
    relevanceThreshold: typing_extensions.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    safeSearch: bool
    searchAsYouTypeSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAsYouTypeSpec
    )
    servingConfig: str
    session: str
    sessionSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestSessionSpec
    spellCorrectionSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestSpellCorrectionSpec
    )
    userInfo: GoogleCloudDiscoveryengineV1alphaUserInfo
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec(
    typing_extensions.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecExtractiveContentSpec
    searchResultMode: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecExtractiveContentSpec(
    typing_extensions.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSnippetSpec(
    typing_extensions.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpec(
    typing_extensions.TypedDict, total=False
):
    ignoreAdversarialQuery: bool
    ignoreJailBreakingQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelSpec
    summaryResultCount: int
    useSemanticChunks: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelPromptSpec(
    typing_extensions.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelSpec(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpec(
    typing_extensions.TypedDict, total=False
):
    embeddingVectors: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpecEmbeddingVector
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpecEmbeddingVector(
    typing_extensions.TypedDict, total=False
):
    fieldPath: str
    vector: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestNaturalLanguageQueryUnderstandingSpec(
    typing_extensions.TypedDict, total=False
):
    filterExtractionCondition: typing_extensions.Literal[
        "CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    geoSearchQueryDetectionFieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestPersonalizationSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAsYouTypeSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSessionSpec(
    typing_extensions.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSession(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    endTime: str
    isPinned: bool
    name: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "IN_PROGRESS"]
    turns: _list[GoogleCloudDiscoveryengineV1alphaSessionTurn]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSessionTurn(
    typing_extensions.TypedDict, total=False
):
    answer: str
    detailedAnswer: GoogleCloudDiscoveryengineV1alphaAnswer
    query: GoogleCloudDiscoveryengineV1alphaQuery

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetDedicatedCrawlRateMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetDedicatedCrawlRateResponse(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUpDataConnectorMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSingleRegionKey(
    typing_extensions.TypedDict, total=False
):
    kmsKey: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSitemap(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSite(
    typing_extensions.TypedDict, total=False
):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing_extensions.Literal[
        "INDEXING_STATUS_UNSPECIFIED", "PENDING", "FAILED", "SUCCEEDED", "DELETING"
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1alphaSiteVerificationInfo
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReason(
    typing_extensions.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReasonQuotaFailure(
    typing_extensions.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateCmekConfigMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateCollectionMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateSessionRequest(
    typing_extensions.TypedDict, total=False
):
    session: GoogleCloudDiscoveryengineV1alphaSession
    updateMask: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserInfo(
    typing_extensions.TypedDict, total=False
):
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWorkspaceConfig(
    typing_extensions.TypedDict, total=False
):
    dasherCustomerId: str
    superAdminEmailAddress: str
    superAdminServiceAccount: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "GOOGLE_DRIVE",
        "GOOGLE_MAIL",
        "GOOGLE_SITES",
        "GOOGLE_CALENDAR",
        "GOOGLE_CHAT",
        "GOOGLE_GROUPS",
        "GOOGLE_KEEP",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaAdvancedSiteSearchConfig(
    typing_extensions.TypedDict, total=False
):
    disableAutomaticRefresh: bool
    disableInitialIndex: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1betaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCmekConfig(
    typing_extensions.TypedDict, total=False
):
    isDefault: bool
    kmsKey: str
    kmsKeyVersion: str
    lastRotationTimestampMicros: str
    name: str
    singleRegionKeys: _list[GoogleCloudDiscoveryengineV1betaSingleRegionKey]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "KEY_ISSUE",
        "DELETING",
        "UNUSABLE",
        "ACTIVE_ROTATING",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCondition(
    typing_extensions.TypedDict, total=False
):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1betaConditionTimeRange]
    queryRegex: str
    queryTerms: _list[GoogleCloudDiscoveryengineV1betaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControl(typing_extensions.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1betaControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1betaCondition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1betaControlFilterAction
    name: str
    promoteAction: GoogleCloudDiscoveryengineV1betaControlPromoteAction
    redirectAction: GoogleCloudDiscoveryengineV1betaControlRedirectAction
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1betaControlSynonymsAction
    useCases: _list[
        typing_extensions.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlBoostAction(
    typing_extensions.TypedDict, total=False
):
    boost: float
    dataStore: str
    filter: str
    fixedBoost: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlFilterAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlPromoteAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    searchLinkPromotion: GoogleCloudDiscoveryengineV1betaSearchLinkPromotion

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlSynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateEvaluationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateSitemapMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStore(
    typing_extensions.TypedDict, total=False
):
    advancedSiteSearchConfig: GoogleCloudDiscoveryengineV1betaAdvancedSiteSearchConfig
    billingEstimation: GoogleCloudDiscoveryengineV1betaDataStoreBillingEstimation
    cmekConfig: GoogleCloudDiscoveryengineV1betaCmekConfig
    contentConfig: typing_extensions.Literal[
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
    industryVertical: typing_extensions.Literal[
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
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1betaSchema
    workspaceConfig: GoogleCloudDiscoveryengineV1betaWorkspaceConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreBillingEstimation(
    typing_extensions.TypedDict, total=False
):
    structuredDataSize: str
    structuredDataUpdateTime: str
    unstructuredDataSize: str
    unstructuredDataUpdateTime: str
    websiteDataSize: str
    websiteDataUpdateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreServingConfigDataStore(
    typing_extensions.TypedDict, total=False
):
    disabledForServing: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteIdentityMappingStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteSitemapMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngine(typing_extensions.TypedDict, total=False):
    chatEngineConfig: GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata
    commonConfig: GoogleCloudDiscoveryengineV1betaEngineCommonConfig
    createTime: str
    dataStoreIds: _list[str]
    disableAnalytics: bool
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    name: str
    searchEngineConfig: GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig(
    typing_extensions.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1betaEngineChatEngineConfigAgentCreationConfig
    )
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineConfigAgentCreationConfig(
    typing_extensions.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineCommonConfig(
    typing_extensions.TypedDict, total=False
):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig(
    typing_extensions.TypedDict, total=False
):
    searchAddOns: _list[
        typing_extensions.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing_extensions.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluation(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    errorSamples: _list[GoogleRpcStatus]
    evaluationSpec: GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpec
    name: str
    qualityMetrics: GoogleCloudDiscoveryengineV1betaQualityMetrics
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpec(
    typing_extensions.TypedDict, total=False
):
    querySetSpec: GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpecQuerySetSpec
    searchRequest: GoogleCloudDiscoveryengineV1betaSearchRequest

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpecQuerySetSpec(
    typing_extensions.TypedDict, total=False
):
    sampleQuerySet: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaFetchSitemapsResponse(
    typing_extensions.TypedDict, total=False
):
    sitemapsMetadata: _list[
        GoogleCloudDiscoveryengineV1betaFetchSitemapsResponseSitemapMetadata
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaFetchSitemapsResponseSitemapMetadata(
    typing_extensions.TypedDict, total=False
):
    sitemap: GoogleCloudDiscoveryengineV1betaSitemap

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSampleQueriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSampleQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaInterval(
    typing_extensions.TypedDict, total=False
):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaLanguageInfo(
    typing_extensions.TypedDict, total=False
):
    language: str
    languageCode: str
    normalizedLanguageCode: str
    region: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaNaturalLanguageQueryUnderstandingConfig(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProject(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectServiceTerms(
    typing_extensions.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProvisionProjectMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaQualityMetrics(
    typing_extensions.TypedDict, total=False
):
    docNdcg: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    docPrecision: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    docRecall: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    pageNdcg: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    pageRecall: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics(
    typing_extensions.TypedDict, total=False
):
    top1: float
    top10: float
    top3: float
    top5: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSchema(typing_extensions.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchLinkPromotion(
    typing_extensions.TypedDict, total=False
):
    description: str
    enabled: bool
    imageUri: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestDataStoreSpec]
    embeddingSpec: GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpec
    facetSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1betaSearchRequestImageQuery
    languageCode: str
    naturalLanguageQueryUnderstandingSpec: GoogleCloudDiscoveryengineV1betaSearchRequestNaturalLanguageQueryUnderstandingSpec
    offset: int
    oneBoxPageSize: int
    orderBy: str
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    personalizationSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestPersonalizationSpec
    )
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec
    rankingExpression: str
    regionCode: str
    relevanceThreshold: typing_extensions.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    safeSearch: bool
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
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec(
    typing_extensions.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec
    searchResultMode: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec(
    typing_extensions.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSnippetSpec(
    typing_extensions.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpec(
    typing_extensions.TypedDict, total=False
):
    ignoreAdversarialQuery: bool
    ignoreJailBreakingQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelSpec
    summaryResultCount: int
    useSemanticChunks: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelPromptSpec(
    typing_extensions.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelSpec(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestDataStoreSpec(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpec(
    typing_extensions.TypedDict, total=False
):
    embeddingVectors: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpecEmbeddingVector
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpecEmbeddingVector(
    typing_extensions.TypedDict, total=False
):
    fieldPath: str
    vector: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestNaturalLanguageQueryUnderstandingSpec(
    typing_extensions.TypedDict, total=False
):
    filterExtractionCondition: typing_extensions.Literal[
        "CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    geoSearchQueryDetectionFieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestPersonalizationSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSearchAsYouTypeSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSessionSpec(
    typing_extensions.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSingleRegionKey(
    typing_extensions.TypedDict, total=False
):
    kmsKey: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSitemap(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSite(
    typing_extensions.TypedDict, total=False
):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing_extensions.Literal[
        "INDEXING_STATUS_UNSPECIFIED", "PENDING", "FAILED", "SUCCEEDED", "DELETING"
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1betaSiteVerificationInfo
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason(
    typing_extensions.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1betaTargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSiteFailureReasonQuotaFailure(
    typing_extensions.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTrainCustomModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTrainCustomModelResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTuneEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTuneEngineResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUpdateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUpdateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserInfo(
    typing_extensions.TypedDict, total=False
):
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaWorkspaceConfig(
    typing_extensions.TypedDict, total=False
):
    dasherCustomerId: str
    superAdminEmailAddress: str
    superAdminServiceAccount: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "GOOGLE_DRIVE",
        "GOOGLE_MAIL",
        "GOOGLE_SITES",
        "GOOGLE_CALENDAR",
        "GOOGLE_CHAT",
        "GOOGLE_GROUPS",
        "GOOGLE_KEEP",
    ]

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
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
class GoogleMonitoringV3Point(typing_extensions.TypedDict, total=False):
    interval: GoogleMonitoringV3TimeInterval
    value: GoogleMonitoringV3TypedValue

@typing.type_check_only
class GoogleMonitoringV3TimeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleMonitoringV3TimeSeries(typing_extensions.TypedDict, total=False):
    description: str
    metadata: GoogleApiMonitoredResourceMetadata
    metric: GoogleApiMetric
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    points: _list[GoogleMonitoringV3Point]
    resource: GoogleApiMonitoredResource
    unit: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]

@typing.type_check_only
class GoogleMonitoringV3TypedValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    distributionValue: GoogleApiDistribution
    doubleValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeDateTime(typing_extensions.TypedDict, total=False):
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
class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str
