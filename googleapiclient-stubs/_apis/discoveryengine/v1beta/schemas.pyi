import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

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
class GoogleCloudDiscoveryengineV1BatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]

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
class GoogleCloudDiscoveryengineV1DataStore(typing_extensions.TypedDict, total=False):
    contentConfig: typing_extensions.Literal[
        "CONTENT_CONFIG_UNSPECIFIED", "NO_CONTENT", "CONTENT_REQUIRED", "PUBLIC_WEBSITE"
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfig
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA"
    ]
    name: str
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1Schema

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
class GoogleCloudDiscoveryengineV1DigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
):
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1DigitalParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1OcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

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
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA"
    ]
    name: str
    searchEngineConfig: GoogleCloudDiscoveryengineV1EngineSearchEngineConfig
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
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
class GoogleCloudDiscoveryengineV1ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

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
class GoogleCloudDiscoveryengineV1ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1OcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

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
class GoogleCloudDiscoveryengineV1PurgeDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Schema(typing_extensions.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

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
class GoogleCloudDiscoveryengineV1alphaAclConfig(
    typing_extensions.TypedDict, total=False
):
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    name: str

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
class GoogleCloudDiscoveryengineV1alphaCreateSchemaMetadata(
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
class GoogleCloudDiscoveryengineV1alphaDataStore(
    typing_extensions.TypedDict, total=False
):
    aclEnabled: bool
    contentConfig: typing_extensions.Literal[
        "CONTENT_CONFIG_UNSPECIFIED", "NO_CONTENT", "CONTENT_REQUIRED", "PUBLIC_WEBSITE"
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA"
    ]
    name: str
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1alphaSchema

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
class GoogleCloudDiscoveryengineV1alphaDeleteSchemaMetadata(
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
class GoogleCloudDiscoveryengineV1alphaDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

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
    ocrConfig: GoogleCloudDiscoveryengineV1alphaOcrConfig
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
    digitalParsingConfig: GoogleCloudDiscoveryengineV1alphaDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1alphaLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1alphaOcrParsingConfig

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
    allowMultipleDataStoresSearchEngine: bool
    chatEngineConfig: GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata
    commonConfig: GoogleCloudDiscoveryengineV1alphaEngineCommonConfig
    createTime: str
    dataStoreIds: _list[str]
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA"
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
class GoogleCloudDiscoveryengineV1alphaFieldConfig(
    typing_extensions.TypedDict, total=False
):
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
    recsFilterableOption: typing_extensions.Literal[
        "FILTERABLE_OPTION_UNSPECIFIED", "FILTERABLE_ENABLED", "FILTERABLE_DISABLED"
    ]
    retrievableOption: typing_extensions.Literal[
        "RETRIEVABLE_OPTION_UNSPECIFIED", "RETRIEVABLE_ENABLED", "RETRIEVABLE_DISABLED"
    ]
    searchableOption: typing_extensions.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]

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
class GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
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
class GoogleCloudDiscoveryengineV1alphaLayoutParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaOcrConfig(
    typing_extensions.TypedDict, total=False
):
    enabled: bool
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

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
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    invalidUris: _list[str]
    pendingCount: int
    quotaExceededCount: int
    successCount: int
    updateTime: str
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
class GoogleCloudDiscoveryengineV1alphaSchema(typing_extensions.TypedDict, total=False):
    fieldConfigs: _list[GoogleCloudDiscoveryengineV1alphaFieldConfig]
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

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
class GoogleCloudDiscoveryengineV1alphaUpdateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSitesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudDiscoveryengineV1betaCreateTargetSiteRequest]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1betaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchVerifyTargetSitesRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCompleteQueryResponse(
    typing_extensions.TypedDict, total=False
):
    querySuggestions: _list[
        GoogleCloudDiscoveryengineV1betaCompleteQueryResponseQuerySuggestion
    ]
    tailMatchTriggered: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCompleteQueryResponseQuerySuggestion(
    typing_extensions.TypedDict, total=False
):
    completableFieldPaths: _list[str]
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCompletionInfo(
    typing_extensions.TypedDict, total=False
):
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConversation(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    messages: _list[GoogleCloudDiscoveryengineV1betaConversationMessage]
    name: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETED"]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConversationContext(
    typing_extensions.TypedDict, total=False
):
    activeDocument: str
    contextDocuments: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConversationMessage(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    reply: GoogleCloudDiscoveryengineV1betaReply
    userInput: GoogleCloudDiscoveryengineV1betaTextInput

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConverseConversationRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec
    conversation: GoogleCloudDiscoveryengineV1betaConversation
    filter: str
    query: GoogleCloudDiscoveryengineV1betaTextInput
    safeSearch: bool
    servingConfig: str
    summarySpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpec
    )
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConverseConversationResponse(
    typing_extensions.TypedDict, total=False
):
    conversation: GoogleCloudDiscoveryengineV1betaConversation
    relatedQuestions: _list[str]
    reply: GoogleCloudDiscoveryengineV1betaReply
    searchResults: _list[GoogleCloudDiscoveryengineV1betaSearchResponseSearchResult]

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
class GoogleCloudDiscoveryengineV1betaCreateSchemaMetadata(
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
class GoogleCloudDiscoveryengineV1betaCreateTargetSiteRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    targetSite: GoogleCloudDiscoveryengineV1betaTargetSite

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCustomAttribute(
    typing_extensions.TypedDict, total=False
):
    numbers: _list[float]
    text: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStore(
    typing_extensions.TypedDict, total=False
):
    contentConfig: typing_extensions.Literal[
        "CONTENT_CONFIG_UNSPECIFIED", "NO_CONTENT", "CONTENT_REQUIRED", "PUBLIC_WEBSITE"
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfig
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA"
    ]
    name: str
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1betaSchema

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
class GoogleCloudDiscoveryengineV1betaDeleteSchemaMetadata(
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
class GoogleCloudDiscoveryengineV1betaDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocument(
    typing_extensions.TypedDict, total=False
):
    content: GoogleCloudDiscoveryengineV1betaDocumentContent
    derivedStructData: dict[str, typing.Any]
    id: str
    indexTime: str
    jsonData: str
    name: str
    parentDocumentId: str
    schemaId: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentContent(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    rawBytes: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str
    promotionIds: _list[str]
    quantity: int
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
):
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1betaDigitalParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1betaOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDoubleList(
    typing_extensions.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEmbeddingConfig(
    typing_extensions.TypedDict, total=False
):
    fieldPath: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchRequest(
    typing_extensions.TypedDict, total=False
): ...

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
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA"
    ]
    name: str
    searchEngineConfig: GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
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
class GoogleCloudDiscoveryengineV1betaFetchDomainVerificationStatusResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1betaTargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaGcsSource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    autoGenerateIds: bool
    bigquerySource: GoogleCloudDiscoveryengineV1betaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1betaGcsSource
    idField: str
    inlineSource: GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSource
    reconciliationMode: typing_extensions.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1betaDocument]

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
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesRequest(
    typing_extensions.TypedDict, total=False
):
    gcsSource: GoogleCloudDiscoveryengineV1betaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleCloudDiscoveryengineV1betaSuggestionDenyListEntry]

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
class GoogleCloudDiscoveryengineV1betaImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1betaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1betaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudDiscoveryengineV1betaUserEvent]

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
class GoogleCloudDiscoveryengineV1betaListConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversations: _list[GoogleCloudDiscoveryengineV1betaConversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListDataStoresResponse(
    typing_extensions.TypedDict, total=False
):
    dataStores: _list[GoogleCloudDiscoveryengineV1betaDataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1betaDocument]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListEnginesResponse(
    typing_extensions.TypedDict, total=False
):
    engines: _list[GoogleCloudDiscoveryengineV1betaEngine]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListSchemasResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    schemas: _list[GoogleCloudDiscoveryengineV1betaSchema]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListServingConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudDiscoveryengineV1betaServingConfig]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1betaTargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaMediaInfo(
    typing_extensions.TypedDict, total=False
):
    mediaProgressDuration: str
    mediaProgressPercentage: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPageInfo(
    typing_extensions.TypedDict, total=False
):
    pageCategory: str
    pageviewId: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPanelInfo(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    panelId: str
    panelPosition: int
    totalPanels: int

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
class GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

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
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecommendRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    params: dict[str, typing.Any]
    userEvent: GoogleCloudDiscoveryengineV1betaUserEvent
    userLabels: dict[str, typing.Any]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecommendResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    missingIds: _list[str]
    results: _list[
        GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResult
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResult(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDiscoveryengineV1betaDocument
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecrawlUrisRequest(
    typing_extensions.TypedDict, total=False
):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaReply(typing_extensions.TypedDict, total=False):
    references: _list[GoogleCloudDiscoveryengineV1betaReplyReference]
    reply: str
    summary: GoogleCloudDiscoveryengineV1betaSearchResponseSummary

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaReplyReference(
    typing_extensions.TypedDict, total=False
):
    anchorText: str
    end: int
    start: int
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSchema(typing_extensions.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchInfo(
    typing_extensions.TypedDict, total=False
):
    offset: int
    orderBy: str
    searchQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec
    embeddingSpec: GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpec
    facetSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1betaSearchRequestImageQuery
    offset: int
    orderBy: str
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec
    rankingExpression: str
    safeSearch: bool
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
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec(
    typing_extensions.TypedDict, total=False
):
    extractiveContentSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec
    snippetSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSnippetSpec
    )
    summarySpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec(
    typing_extensions.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int

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
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelSpec
    summaryResultCount: int

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
class GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponse(
    typing_extensions.TypedDict, total=False
):
    appliedControls: _list[str]
    attributionToken: str
    correctedQuery: str
    facets: _list[GoogleCloudDiscoveryengineV1betaSearchResponseFacet]
    geoSearchDebugInfo: _list[
        GoogleCloudDiscoveryengineV1betaSearchResponseGeoSearchDebugInfo
    ]
    guidedSearchResult: GoogleCloudDiscoveryengineV1betaSearchResponseGuidedSearchResult
    nextPageToken: str
    queryExpansionInfo: GoogleCloudDiscoveryengineV1betaSearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudDiscoveryengineV1betaSearchResponseSearchResult]
    summary: GoogleCloudDiscoveryengineV1betaSearchResponseSummary
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseFacet(
    typing_extensions.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudDiscoveryengineV1betaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseFacetFacetValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    interval: GoogleCloudDiscoveryengineV1betaInterval
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseGeoSearchDebugInfo(
    typing_extensions.TypedDict, total=False
):
    errorMessage: str
    originalAddressQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseGuidedSearchResult(
    typing_extensions.TypedDict, total=False
):
    followUpQuestions: _list[str]
    refinementAttributes: _list[
        GoogleCloudDiscoveryengineV1betaSearchResponseGuidedSearchResultRefinementAttribute
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseGuidedSearchResultRefinementAttribute(
    typing_extensions.TypedDict, total=False
):
    attributeKey: str
    attributeValue: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseQueryExpansionInfo(
    typing_extensions.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSearchResult(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDiscoveryengineV1betaDocument
    id: str
    modelScores: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSummary(
    typing_extensions.TypedDict, total=False
):
    safetyAttributes: (
        GoogleCloudDiscoveryengineV1betaSearchResponseSummarySafetyAttributes
    )
    summarySkippedReasons: _list[
        typing_extensions.Literal[
            "SUMMARY_SKIPPED_REASON_UNSPECIFIED",
            "ADVERSARIAL_QUERY_IGNORED",
            "NON_SUMMARY_SEEKING_QUERY_IGNORED",
            "OUT_OF_DOMAIN_QUERY_IGNORED",
            "POTENTIAL_POLICY_VIOLATION",
            "LLM_ADDON_NOT_ENABLED",
        ]
    ]
    summaryText: str
    summaryWithMetadata: (
        GoogleCloudDiscoveryengineV1betaSearchResponseSummarySummaryWithMetadata
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSummaryCitation(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1betaSearchResponseSummaryCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSummaryCitationMetadata(
    typing_extensions.TypedDict, total=False
):
    citations: _list[GoogleCloudDiscoveryengineV1betaSearchResponseSummaryCitation]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSummaryCitationSource(
    typing_extensions.TypedDict, total=False
):
    referenceIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSummaryReference(
    typing_extensions.TypedDict, total=False
):
    document: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSummarySafetyAttributes(
    typing_extensions.TypedDict, total=False
):
    categories: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseSummarySummaryWithMetadata(
    typing_extensions.TypedDict, total=False
):
    citationMetadata: (
        GoogleCloudDiscoveryengineV1betaSearchResponseSummaryCitationMetadata
    )
    references: _list[GoogleCloudDiscoveryengineV1betaSearchResponseSummaryReference]
    summary: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaServingConfig(
    typing_extensions.TypedDict, total=False
):
    boostControlIds: _list[str]
    createTime: str
    displayName: str
    dissociateControlIds: _list[str]
    diversityLevel: str
    embeddingConfig: GoogleCloudDiscoveryengineV1betaEmbeddingConfig
    filterControlIds: _list[str]
    genericConfig: GoogleCloudDiscoveryengineV1betaServingConfigGenericConfig
    ignoreControlIds: _list[str]
    mediaConfig: GoogleCloudDiscoveryengineV1betaServingConfigMediaConfig
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    rankingExpression: str
    redirectControlIds: _list[str]
    replacementControlIds: _list[str]
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
    ]
    synonymsControlIds: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaServingConfigGenericConfig(
    typing_extensions.TypedDict, total=False
):
    contentSearchSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaServingConfigMediaConfig(
    typing_extensions.TypedDict, total=False
):
    contentFreshnessCutoffDays: int
    contentWatchedMinutesThreshold: float
    contentWatchedPercentageThreshold: float
    contentWatchedSecondsThreshold: float
    demotionEventType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSiteSearchEngine(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSuggestionDenyListEntry(
    typing_extensions.TypedDict, total=False
):
    blockPhrase: str
    matchOperator: typing_extensions.Literal[
        "MATCH_OPERATOR_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"
    ]

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
class GoogleCloudDiscoveryengineV1betaTextInput(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudDiscoveryengineV1betaConversationContext
    input: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTransactionInfo(
    typing_extensions.TypedDict, total=False
):
    cost: float
    currency: str
    discountValue: float
    tax: float
    transactionId: str
    value: float

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
class GoogleCloudDiscoveryengineV1betaUserEvent(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    attributionToken: str
    completionInfo: GoogleCloudDiscoveryengineV1betaCompletionInfo
    directUserRequest: bool
    documents: _list[GoogleCloudDiscoveryengineV1betaDocumentInfo]
    eventTime: str
    eventType: str
    filter: str
    mediaInfo: GoogleCloudDiscoveryengineV1betaMediaInfo
    pageInfo: GoogleCloudDiscoveryengineV1betaPageInfo
    panel: GoogleCloudDiscoveryengineV1betaPanelInfo
    promotionIds: _list[str]
    searchInfo: GoogleCloudDiscoveryengineV1betaSearchInfo
    sessionId: str
    tagIds: _list[str]
    transactionInfo: GoogleCloudDiscoveryengineV1betaTransactionInfo
    userInfo: GoogleCloudDiscoveryengineV1betaUserInfo
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserInfo(
    typing_extensions.TypedDict, total=False
):
    userAgent: str
    userId: str

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
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int
