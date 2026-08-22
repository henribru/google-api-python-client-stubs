import typing

_list = list

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
class GoogleCloudDiscoveryengineV1BatchCreateTargetSitesResponse(
    typing.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchUpdateUserLicensesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchUpdateUserLicensesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    userLicenses: _list[GoogleCloudDiscoveryengineV1UserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CliConfig(typing.TypedDict, total=False):
    enabledActions: _list[str]

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
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDiscoveryengineV1HealthcareFhirConfig(typing.TypedDict, total=False):
    enableConfigurableSchema: bool
    enableStaticIndexingForBatchIngestion: bool
    initialFilterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1IdentityMappingEntryOperationMetadata(
    typing.TypedDict, total=False
):
    failureCount: str
    successCount: str
    totalCount: str

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
class GoogleCloudDiscoveryengineV1ImportDocumentsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportErrorConfig(typing.TypedDict, total=False):
    gcsPrefix: str

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
class GoogleCloudDiscoveryengineV1ImportUserEventsResponse(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

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
class GoogleCloudDiscoveryengineV1NaturalLanguageQueryUnderstandingConfig(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ObservabilityConfig(typing.TypedDict, total=False):
    observabilityEnabled: bool
    sensitiveLoggingEnabled: bool

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
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

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
class GoogleCloudDiscoveryengineV1PurgeDocumentsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Schema(typing.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchLinkPromotion(typing.TypedDict, total=False):
    description: str
    document: str
    enabled: bool
    imageUri: str
    title: str
    uri: str

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
class GoogleCloudDiscoveryengineV1SetUpDataConnectorMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SingleRegionKey(typing.TypedDict, total=False):
    kmsKey: str

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
class GoogleCloudDiscoveryengineV1TrainCustomModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

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
class GoogleCloudDiscoveryengineV1alphaA2AAgentDefinition(
    typing.TypedDict, total=False
):
    cloudMarketplaceConfig: (
        GoogleCloudDiscoveryengineV1alphaA2AAgentDefinitionCloudMarketplaceConfig
    )
    jsonAgentCard: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaA2AAgentDefinitionCloudMarketplaceConfig(
    typing.TypedDict, total=False
):
    entitlement: str
    order: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAclConfig(typing.TypedDict, total=False):
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAcquireAccessTokenRequest(
    typing.TypedDict, total=False
):
    action: str
    scope: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAcquireAccessTokenResponse(
    typing.TypedDict, total=False
):
    accessToken: str
    refreshTokenInfo: GoogleCloudDiscoveryengineV1alphaRefreshTokenInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAcquireProgramsRequest(
    typing.TypedDict, total=False
):
    desiredProgramsCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAcquireProgramsResponse(
    typing.TypedDict, total=False
):
    programs: _list[GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgram]

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
class GoogleCloudDiscoveryengineV1alphaAdkAgentDefinition(
    typing.TypedDict, total=False
):
    provisionedReasoningEngine: (
        GoogleCloudDiscoveryengineV1alphaAdkAgentDefinitionProvisionedReasoningEngine
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdkAgentDefinitionProvisionedReasoningEngine(
    typing.TypedDict, total=False
):
    reasoningEngine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequest(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequestBoostSpec
    experimentIds: _list[str]
    includeTailSuggestions: bool
    query: str
    queryModel: str
    suggestionTypeSpecs: _list[
        GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequestSuggestionTypeSpec
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
    userInfo: GoogleCloudDiscoveryengineV1alphaUserInfo
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequestBoostSpec(
    typing.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequestSuggestionTypeSpec(
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
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponse(
    typing.TypedDict, total=False
):
    contentSuggestions: _list[
        GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseContentSuggestion
    ]
    peopleSuggestions: _list[
        GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponsePersonSuggestion
    ]
    querySuggestions: _list[
        GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseQuerySuggestion
    ]
    recentSearchSuggestions: _list[
        GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseRecentSearchSuggestion
    ]
    tailMatchTriggered: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseContentSuggestion(
    typing.TypedDict, total=False
):
    contentType: typing.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "GOOGLE_WORKSPACE", "THIRD_PARTY"
    ]
    dataStore: str
    destinationUri: str
    document: GoogleCloudDiscoveryengineV1alphaDocument
    iconUri: str
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponsePersonSuggestion(
    typing.TypedDict, total=False
):
    dataStore: str
    destinationUri: str
    displayPhotoUri: str
    document: GoogleCloudDiscoveryengineV1alphaDocument
    personType: typing.Literal[
        "PERSON_TYPE_UNSPECIFIED",
        "CLOUD_IDENTITY",
        "THIRD_PARTY_IDENTITY",
        "GOOGLE_GROUP",
    ]
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseQuerySuggestion(
    typing.TypedDict, total=False
):
    completableFieldPaths: _list[str]
    dataStore: _list[str]
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseRecentSearchSuggestion(
    typing.TypedDict, total=False
):
    recentSearchTime: str
    score: float
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedSiteSearchConfig(
    typing.TypedDict, total=False
):
    disableAutomaticRefresh: bool
    disableInitialIndex: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAgent(typing.TypedDict, total=False):
    a2aAgentDefinition: GoogleCloudDiscoveryengineV1alphaA2AAgentDefinition
    adkAgentDefinition: GoogleCloudDiscoveryengineV1alphaAdkAgentDefinition
    authorizationConfig: GoogleCloudDiscoveryengineV1alphaAuthorizationConfig
    createTime: str
    creationFailureReason: str
    customPlaceholderText: str
    deploymentFailureReason: str
    description: str
    dialogflowAgentDefinition: (
        GoogleCloudDiscoveryengineV1alphaDialogflowAgentDefinition
    )
    displayName: str
    icon: GoogleCloudDiscoveryengineV1alphaAgentImage
    languageCode: str
    managedAgentDefinition: GoogleCloudDiscoveryengineV1alphaManagedAgentDefinition
    name: str
    observabilityConfig: GoogleCloudDiscoveryengineV1alphaObservabilityConfig
    rejectionReason: str
    sharingConfig: GoogleCloudDiscoveryengineV1alphaAgentSharingConfig
    starterPrompts: _list[GoogleCloudDiscoveryengineV1alphaAgentStarterPrompt]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CONFIGURED",
        "DEPLOYING",
        "DISABLED",
        "DEPLOYMENT_FAILED",
        "PRIVATE",
        "ENABLED",
        "SUSPENDED",
        "CREATING",
        "CREATION_FAILED",
    ]
    suspensionReason: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAgentFile(typing.TypedDict, total=False):
    fileName: str
    mimeType: str
    name: str

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
class GoogleCloudDiscoveryengineV1alphaAgentImage(typing.TypedDict, total=False):
    content: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAgentSharingConfig(
    typing.TypedDict, total=False
):
    scope: typing.Literal["SCOPE_UNSPECIFIED", "RESTRICTED", "ALL_USERS"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAgentStarterPrompt(
    typing.TypedDict, total=False
):
    text: str

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
class GoogleCloudDiscoveryengineV1alphaAlloyDbSource(typing.TypedDict, total=False):
    clusterId: str
    databaseId: str
    gcsStagingDir: str
    locationId: str
    projectId: str
    tableId: str

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
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgramEvaluationSubmission(
    typing.TypedDict, total=False
):
    evaluation: GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgramEvaluation
    lockToken: str
    program: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlphaEvolveSourceFile(
    typing.TypedDict, total=False
):
    content: str
    description: str
    path: str
    programLanguage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnalyticsConfig(typing.TypedDict, total=False):
    name: str
    userLevelMetricsEnabled: bool

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
class GoogleCloudDiscoveryengineV1alphaAnswerGenerationSpec(
    typing.TypedDict, total=False
):
    userDefinedClassifierSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerGenerationSpecUserDefinedClassifierSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerGenerationSpecUserDefinedClassifierSpec(
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
class GoogleCloudDiscoveryengineV1alphaAnswerGroundingSupport(
    typing.TypedDict, total=False
):
    endIndex: str
    groundingCheckRequired: bool
    groundingScore: float
    sources: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest(
    typing.TypedDict, total=False
):
    answerGenerationSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpec
    )
    asynchronousMode: bool
    endUserSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpec
    groundingSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestGroundingSpec
    query: GoogleCloudDiscoveryengineV1alphaQuery
    queryUnderstandingSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpec
    )
    relatedQuestionsSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestRelatedQuestionsSpec
    )
    safetySpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSafetySpec
    searchSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpec
    session: str
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpec(
    typing.TypedDict, total=False
):
    answerLanguageCode: str
    ignoreAdversarialQuery: bool
    ignoreJailBreakingQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonAnswerSeekingQuery: bool
    includeCitations: bool
    modelSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecModelSpec
    )
    multimodalSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecMultimodalSpec
    promptSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecPromptSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecModelSpec(
    typing.TypedDict, total=False
):
    modelVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecMultimodalSpec(
    typing.TypedDict, total=False
):
    imageSource: typing.Literal[
        "IMAGE_SOURCE_UNSPECIFIED",
        "ALL_AVAILABLE_SOURCES",
        "CORPUS_IMAGE_ONLY",
        "FIGURE_GENERATION_ONLY",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecPromptSpec(
    typing.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpec(
    typing.TypedDict, total=False
):
    endUserMetadata: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpecEndUserMetaData
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpecEndUserMetaData(
    typing.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfo(
    typing.TypedDict, total=False
):
    content: str
    documentMetadata: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfoDocumentMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestEndUserSpecEndUserMetaDataChunkInfoDocumentMetadata(
    typing.TypedDict, total=False
):
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestGroundingSpec(
    typing.TypedDict, total=False
):
    filteringLevel: typing.Literal[
        "FILTERING_LEVEL_UNSPECIFIED", "FILTERING_LEVEL_LOW", "FILTERING_LEVEL_HIGH"
    ]
    includeGroundingSupports: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpec(
    typing.TypedDict, total=False
):
    disableSpellCorrection: bool
    queryClassificationSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec
    queryRephraserSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec(
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
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec(
    typing.TypedDict, total=False
):
    disable: bool
    maxRephraseSteps: int
    modelSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpecModelSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpecModelSpec(
    typing.TypedDict, total=False
):
    modelType: typing.Literal["MODEL_TYPE_UNSPECIFIED", "SMALL", "LARGE"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestRelatedQuestionsSpec(
    typing.TypedDict, total=False
):
    enable: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSafetySpec(
    typing.TypedDict, total=False
):
    enable: bool
    safetySettings: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSafetySpecSafetySetting
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSafetySpecSafetySetting(
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
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpec(
    typing.TypedDict, total=False
):
    searchParams: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchParams
    )
    searchResultList: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultList
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchParams(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    customFineTuningSpec: GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec]
    filter: str
    maxReturnResults: int
    naturalLanguageQueryUnderstandingSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestNaturalLanguageQueryUnderstandingSpec
    orderBy: str
    searchResultMode: typing.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultList(
    typing.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResult(
    typing.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo
    unstructuredDocumentInfo: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo(
    typing.TypedDict, total=False
):
    chunk: str
    content: str
    documentMetadata: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfoDocumentMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfoDocumentMetadata(
    typing.TypedDict, total=False
):
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo(
    typing.TypedDict, total=False
):
    document: str
    documentContexts: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoDocumentContext
    ]
    extractiveAnswers: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveAnswer
    ]
    extractiveSegments: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveSegment
    ]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoDocumentContext(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveAnswer(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveSegment(
    typing.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryResponse(
    typing.TypedDict, total=False
):
    answer: GoogleCloudDiscoveryengineV1alphaAnswer
    answerQueryToken: str
    session: GoogleCloudDiscoveryengineV1alphaSession

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
class GoogleCloudDiscoveryengineV1alphaAssistUserMetadata(
    typing.TypedDict, total=False
):
    preferredLanguageCode: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistant(typing.TypedDict, total=False):
    createTime: str
    customerPolicy: GoogleCloudDiscoveryengineV1alphaAssistantCustomerPolicy
    defaultWebGroundingToggleOff: bool
    description: str
    disableLocationContext: bool
    displayName: str
    enabledTools: dict[str, typing.Any]
    generationConfig: GoogleCloudDiscoveryengineV1alphaAssistantGenerationConfig
    name: str
    updateTime: str
    webGroundingType: typing.Literal[
        "WEB_GROUNDING_TYPE_UNSPECIFIED",
        "WEB_GROUNDING_TYPE_DISABLED",
        "WEB_GROUNDING_TYPE_GOOGLE_SEARCH",
        "WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH",
    ]

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
class GoogleCloudDiscoveryengineV1alphaAssistantCustomerPolicy(
    typing.TypedDict, total=False
):
    bannedPhrases: _list[
        GoogleCloudDiscoveryengineV1alphaAssistantCustomerPolicyBannedPhrase
    ]
    dataProtectionPolicy: GoogleCloudDiscoveryengineV1alphaDataProtectionPolicy
    modelArmorConfig: (
        GoogleCloudDiscoveryengineV1alphaAssistantCustomerPolicyModelArmorConfig
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantCustomerPolicyBannedPhrase(
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
class GoogleCloudDiscoveryengineV1alphaAssistantCustomerPolicyModelArmorConfig(
    typing.TypedDict, total=False
):
    failureMode: typing.Literal["FAILURE_MODE_UNSPECIFIED", "FAIL_OPEN", "FAIL_CLOSED"]
    responseTemplate: str
    userPromptTemplate: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGenerationConfig(
    typing.TypedDict, total=False
):
    allowedModelIds: _list[str]
    defaultLanguage: str
    defaultModelId: str
    systemInstruction: (
        GoogleCloudDiscoveryengineV1alphaAssistantGenerationConfigSystemInstruction
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantGenerationConfigSystemInstruction(
    typing.TypedDict, total=False
):
    additionalSystemInstruction: str

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
class GoogleCloudDiscoveryengineV1alphaAssistantToolInfo(typing.TypedDict, total=False):
    toolDisplayName: str
    toolName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantToolList(typing.TypedDict, total=False):
    toolInfo: _list[GoogleCloudDiscoveryengineV1alphaAssistantToolInfo]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAuthorization(typing.TypedDict, total=False):
    displayName: str
    name: str
    serverSideOauth2: GoogleCloudDiscoveryengineV1alphaAuthorizationServerSideOAuth2

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAuthorizationConfig(
    typing.TypedDict, total=False
):
    agentAuthorization: str
    toolAuthorizations: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAuthorizationServerSideOAuth2(
    typing.TypedDict, total=False
):
    authorizationUri: str
    clientId: str
    clientSecret: str
    pkceVerificationEnabled: bool
    scopes: _list[str]
    tokenUri: str

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
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudDiscoveryengineV1alphaCreateTargetSiteRequest]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponse(
    typing.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponse(
    typing.TypedDict, total=False
):
    documentsMetadata: _list[
        GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponseDocumentMetadata
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponseDocumentMetadata(
    typing.TypedDict, total=False
):
    dataIngestionSource: str
    lastRefreshedTime: str
    matcherValue: GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponseDocumentMetadataMatcherValue
    state: typing.Literal[
        "STATE_UNSPECIFIED", "INDEXED", "NOT_IN_TARGET_SITE", "NOT_IN_INDEX"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponseDocumentMetadataMatcherValue(
    typing.TypedDict, total=False
):
    fhirResource: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesRequest(
    typing.TypedDict, total=False
):
    deleteUnassignedUserLicenses: bool
    inlineSource: (
        GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesRequestInlineSource(
    typing.TypedDict, total=False
):
    updateMask: str
    userLicenses: _list[GoogleCloudDiscoveryengineV1alphaUserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    userLicenses: _list[GoogleCloudDiscoveryengineV1alphaUserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchVerifyTargetSitesRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigQueryDestination(
    typing.TypedDict, total=False
):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigQuerySource(typing.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigtableOptions(typing.TypedDict, total=False):
    families: dict[str, typing.Any]
    keyFieldName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigtableOptionsBigtableColumn(
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
class GoogleCloudDiscoveryengineV1alphaBigtableOptionsBigtableColumnFamily(
    typing.TypedDict, total=False
):
    columns: _list[GoogleCloudDiscoveryengineV1alphaBigtableOptionsBigtableColumn]
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
class GoogleCloudDiscoveryengineV1alphaBigtableSource(typing.TypedDict, total=False):
    bigtableOptions: GoogleCloudDiscoveryengineV1alphaBigtableOptions
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBillingAccountLicenseConfig(
    typing.TypedDict, total=False
):
    autoRenew: bool
    earlyTerminated: bool
    earlyTerminationDate: GoogleTypeDate
    endDate: GoogleTypeDate
    geminiBundle: bool
    licenseConfigDistributions: dict[str, typing.Any]
    licenseCount: str
    name: str
    procurementEntitlementId: str
    startDate: GoogleTypeDate
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "EXPIRED", "NOT_STARTED", "DEACTIVATING"
    ]
    subscriptionDisplayName: str
    subscriptionName: str
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
class GoogleCloudDiscoveryengineV1alphaBranch(typing.TypedDict, total=False):
    branchStats: GoogleCloudDiscoveryengineV1alphaBranchBranchStats
    displayName: str
    isDefault: bool
    lastDocumentImportTime: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBranchBranchStats(typing.TypedDict, total=False):
    documentCounts: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCannedQuery(typing.TypedDict, total=False):
    defaultTexts: GoogleCloudDiscoveryengineV1alphaCannedQueryCannedQueryTexts
    displayName: str
    enabled: bool
    googleDefined: bool
    localizedTexts: dict[str, typing.Any]
    name: str
    requiredCapabilities: _list[
        GoogleCloudDiscoveryengineV1alphaCannedQueryAssistantCapability
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCannedQueryAssistantCapability(
    typing.TypedDict, total=False
):
    actionName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCannedQueryCannedQueryTexts(
    typing.TypedDict, total=False
):
    prefix: str
    suggestedPrompts: _list[GoogleCloudDiscoveryengineV1alphaCannedQuerySuggestedPrompt]
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCannedQuerySuggestedPrompt(
    typing.TypedDict, total=False
):
    promptText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingRequest(
    typing.TypedDict, total=False
):
    answerCandidate: str
    facts: _list[GoogleCloudDiscoveryengineV1alphaGroundingFact]
    groundingSpec: GoogleCloudDiscoveryengineV1alphaCheckGroundingSpec
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingResponse(
    typing.TypedDict, total=False
):
    citedChunks: _list[GoogleCloudDiscoveryengineV1alphaFactChunk]
    citedFacts: _list[
        GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseCheckGroundingFactChunk
    ]
    claims: _list[GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseClaim]
    supportScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseCheckGroundingFactChunk(
    typing.TypedDict, total=False
):
    chunkText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseClaim(
    typing.TypedDict, total=False
):
    citationIndices: _list[int]
    claimText: str
    endPos: int
    groundingCheckRequired: bool
    score: float
    startPos: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingSpec(
    typing.TypedDict, total=False
):
    citationThreshold: float
    enableClaimLevelScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRefreshTokenResponse(
    typing.TypedDict, total=False
):
    refreshTokenInfo: GoogleCloudDiscoveryengineV1alphaRefreshTokenInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRequirementRequest(
    typing.TypedDict, total=False
):
    requirementType: str
    resources: _list[GoogleApiMonitoredResource]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRequirementResponse(
    typing.TypedDict, total=False
):
    metricResults: _list[
        GoogleCloudDiscoveryengineV1alphaCheckRequirementResponseMetricQueryResult
    ]
    oldestMetricTimestamp: str
    requirement: GoogleCloudDiscoveryengineV1alphaRequirement
    requirementCondition: GoogleTypeExpr
    result: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRequirementResponseMetricQueryResult(
    typing.TypedDict, total=False
):
    metricType: str
    name: str
    timestamp: str
    unit: str
    value: GoogleMonitoringV3TypedValue

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunk(typing.TypedDict, total=False):
    annotationContents: _list[str]
    annotationMetadata: _list[GoogleCloudDiscoveryengineV1alphaChunkAnnotationMetadata]
    chunkMetadata: GoogleCloudDiscoveryengineV1alphaChunkChunkMetadata
    content: str
    dataUrls: _list[str]
    derivedStructData: dict[str, typing.Any]
    documentMetadata: GoogleCloudDiscoveryengineV1alphaChunkDocumentMetadata
    id: str
    name: str
    pageSpan: GoogleCloudDiscoveryengineV1alphaChunkPageSpan
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkAnnotationMetadata(
    typing.TypedDict, total=False
):
    imageId: str
    structuredContent: GoogleCloudDiscoveryengineV1alphaChunkStructuredContent

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkChunkMetadata(
    typing.TypedDict, total=False
):
    nextChunks: _list[GoogleCloudDiscoveryengineV1alphaChunk]
    previousChunks: _list[GoogleCloudDiscoveryengineV1alphaChunk]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkDocumentMetadata(
    typing.TypedDict, total=False
):
    mimeType: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkPageSpan(typing.TypedDict, total=False):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkStructuredContent(
    typing.TypedDict, total=False
):
    content: str
    structureType: typing.Literal[
        "STRUCTURE_TYPE_UNSPECIFIED",
        "SHAREHOLDER_STRUCTURE",
        "SIGNATURE_STRUCTURE",
        "CHECKBOX_STRUCTURE",
    ]

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
class GoogleCloudDiscoveryengineV1alphaCloudSqlSource(typing.TypedDict, total=False):
    databaseId: str
    gcsStagingDir: str
    instanceId: str
    offload: bool
    projectId: str
    tableId: str

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
class GoogleCloudDiscoveryengineV1alphaCompleteExternalIdentitiesResponse(
    typing.TypedDict, total=False
):
    externalIdentities: _list[GoogleCloudDiscoveryengineV1alphaExternalIdentity]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompleteQueryResponse(
    typing.TypedDict, total=False
):
    querySuggestions: _list[
        GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseQuerySuggestion
    ]
    tailMatchTriggered: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseQuerySuggestion(
    typing.TypedDict, total=False
):
    completableFieldPaths: _list[str]
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompletionConfig(typing.TypedDict, total=False):
    enableMode: typing.Literal["ENABLE_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"]
    filterPiiSuggestionsUsingDlp: bool
    matchingOrder: str
    maxSuggestions: int
    minPrefixLength: int
    name: str
    numUniqueUsersThreshold: int
    queryFrequencyThreshold: int
    queryModel: str
    shouldServeContentSuggestions: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompletionInfo(typing.TypedDict, total=False):
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompletionSuggestion(
    typing.TypedDict, total=False
):
    alternativePhrases: _list[str]
    frequency: str
    globalScore: float
    groupId: str
    groupScore: float
    languageCode: str
    suggestion: str

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
class GoogleCloudDiscoveryengineV1alphaConversation(typing.TypedDict, total=False):
    endTime: str
    messages: _list[GoogleCloudDiscoveryengineV1alphaConversationMessage]
    name: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETED"]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConversationContext(
    typing.TypedDict, total=False
):
    activeDocument: str
    contextDocuments: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConversationMessage(
    typing.TypedDict, total=False
):
    createTime: str
    reply: GoogleCloudDiscoveryengineV1alphaReply
    userInput: GoogleCloudDiscoveryengineV1alphaTextInput

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConverseConversationRequest(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    conversation: GoogleCloudDiscoveryengineV1alphaConversation
    filter: str
    query: GoogleCloudDiscoveryengineV1alphaTextInput
    safeSearch: bool
    servingConfig: str
    summarySpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpec
    )
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConverseConversationResponse(
    typing.TypedDict, total=False
):
    conversation: GoogleCloudDiscoveryengineV1alphaConversation
    relatedQuestions: _list[str]
    reply: GoogleCloudDiscoveryengineV1alphaReply
    searchResults: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult]

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
class GoogleCloudDiscoveryengineV1alphaCreateTargetSiteRequest(
    typing.TypedDict, total=False
):
    parent: str
    targetSite: GoogleCloudDiscoveryengineV1alphaTargetSite

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomAttribute(typing.TypedDict, total=False):
    numbers: _list[float]
    text: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec(
    typing.TypedDict, total=False
):
    enableSearchAdaptor: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomTuningModel(typing.TypedDict, total=False):
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
class GoogleCloudDiscoveryengineV1alphaDialogflowAgentDefinition(
    typing.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDistributeLicenseConfigRequest(
    typing.TypedDict, total=False
):
    licenseConfigId: str
    licenseCount: str
    location: str
    projectNumber: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDistributeLicenseConfigResponse(
    typing.TypedDict, total=False
):
    licenseConfig: GoogleCloudDiscoveryengineV1alphaLicenseConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocument(typing.TypedDict, total=False):
    aclInfo: GoogleCloudDiscoveryengineV1alphaDocumentAclInfo
    content: GoogleCloudDiscoveryengineV1alphaDocumentContent
    derivedStructData: dict[str, typing.Any]
    id: str
    indexStatus: GoogleCloudDiscoveryengineV1alphaDocumentIndexStatus
    indexTime: str
    jsonData: str
    name: str
    parentDocumentId: str
    schemaId: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentAclInfo(typing.TypedDict, total=False):
    readers: _list[GoogleCloudDiscoveryengineV1alphaDocumentAclInfoAccessRestriction]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentAclInfoAccessRestriction(
    typing.TypedDict, total=False
):
    idpWide: bool
    principals: _list[GoogleCloudDiscoveryengineV1alphaPrincipal]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentContent(typing.TypedDict, total=False):
    mimeType: str
    rawBytes: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentIndexStatus(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    indexTime: str
    pendingMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentInfo(typing.TypedDict, total=False):
    conversionValue: float
    id: str
    joined: bool
    name: str
    promotionIds: _list[str]
    quantity: int
    uri: str

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
class GoogleCloudDiscoveryengineV1alphaDoubleList(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDynamicTool(typing.TypedDict, total=False):
    description: str
    displayName: str
    enabled: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEmbeddingConfig(typing.TypedDict, total=False):
    fieldPath: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchRequest(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequest(
    typing.TypedDict, total=False
):
    fileDataSource: (
        GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestFileDataSource
    )
    websiteDataSource: (
        GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestFileDataSource(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSource(
    typing.TypedDict, total=False
):
    estimatorUriPatterns: _list[
        GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSourceEstimatorUriPattern
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSourceEstimatorUriPattern(
    typing.TypedDict, total=False
):
    exactMatch: bool
    exclusive: bool
    providedUriPattern: str

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
class GoogleCloudDiscoveryengineV1alphaExportMetricsRequest(
    typing.TypedDict, total=False
):
    outputConfig: GoogleCloudDiscoveryengineV1alphaOutputConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExportMetricsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExportUserLicensesRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExportUserLicensesResponse(
    typing.TypedDict, total=False
):
    csvData: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExternalIdentity(typing.TypedDict, total=False):
    displayName: str
    externalId: str
    groupMetadata: GoogleCloudDiscoveryengineV1alphaExternalIdentityGroupMetadata
    subject: str
    userMetadata: GoogleCloudDiscoveryengineV1alphaExternalIdentityUserMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExternalIdentityGroupMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaExternalIdentityUserMetadata(
    typing.TypedDict, total=False
):
    familyName: str
    givenName: str
    primaryEmail: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFactChunk(typing.TypedDict, total=False):
    chunkText: str
    domain: str
    index: int
    source: str
    sourceMetadata: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFeedback(typing.TypedDict, total=False):
    comment: str
    componentVersion: str
    conversationInfo: GoogleCloudDiscoveryengineV1alphaFeedbackConversationInfo
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
class GoogleCloudDiscoveryengineV1alphaFeedbackConversationInfo(
    typing.TypedDict, total=False
):
    answerQueryToken: str
    assistToken: str
    query: GoogleCloudDiscoveryengineV1alphaQuery
    questionIndex: int
    session: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponse(
    typing.TypedDict, total=False
):
    sitemapsMetadata: _list[
        GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponseSitemapMetadata
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponseSitemapMetadata(
    typing.TypedDict, total=False
):
    sitemap: GoogleCloudDiscoveryengineV1alphaSitemap

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFhirStoreSource(typing.TypedDict, total=False):
    fhirStore: str
    gcsStagingDir: str
    resourceTypes: _list[str]
    updateFromLatestPredefinedSchema: bool

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
class GoogleCloudDiscoveryengineV1alphaFileCharacteristics(
    typing.TypedDict, total=False
):
    characteristics: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFileMetadata(typing.TypedDict, total=False):
    byteSize: str
    downloadUri: str
    fileId: str
    fileOriginType: typing.Literal[
        "FILE_ORIGIN_TYPE_UNSPECIFIED",
        "USER_PROVIDED",
        "AI_GENERATED",
        "INTERNALLY_GENERATED",
    ]
    lastAddTime: str
    metadata: dict[str, typing.Any]
    mimeType: str
    name: str
    originalSourceType: typing.Literal[
        "FILE_SOURCE_UNSPECIFIED",
        "FILE_SOURCE_INLINE",
        "FILE_SOURCE_LOCAL",
        "FILE_SOURCE_CLOUD_STORAGE",
        "FILE_SOURCE_CLOUD_DRIVE",
        "FILE_SOURCE_URL",
    ]
    originalUri: str
    uploadTime: str
    views: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFileView(typing.TypedDict, total=False):
    byteSize: str
    createTime: str
    fileCharacteristics: GoogleCloudDiscoveryengineV1alphaFileCharacteristics
    imageCharacteristics: GoogleCloudDiscoveryengineV1alphaImageCharacteristics
    mimeType: str
    uri: str
    videoCharacteristics: GoogleCloudDiscoveryengineV1alphaVideoCharacteristics
    viewId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFirestoreSource(typing.TypedDict, total=False):
    collectionId: str
    databaseId: str
    gcsStagingDir: str
    projectId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGcsSource(typing.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetConnectorSecretResponse(
    typing.TypedDict, total=False
):
    app: str
    authorizationUri: str
    clientId: str
    instance: str
    redirectUri: str
    tenantId: str

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
class GoogleCloudDiscoveryengineV1alphaGroundingFact(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    factText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGuidedSearchSpec(typing.TypedDict, total=False):
    enableRefinementAttributes: bool
    enableRelatedQuestions: bool
    maxRelatedQuestions: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaHealthcareFhirConfig(
    typing.TypedDict, total=False
):
    enableConfigurableSchema: bool
    enableStaticIndexingForBatchIngestion: bool
    initialFilterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdentityMappingEntry(
    typing.TypedDict, total=False
):
    externalIdentity: str
    externalIdentityName: str
    groupId: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdentityMappingEntryOperationMetadata(
    typing.TypedDict, total=False
):
    failureCount: str
    successCount: str
    totalCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdentityMappingStore(
    typing.TypedDict, total=False
):
    cmekConfig: GoogleCloudDiscoveryengineV1alphaCmekConfig
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    kmsKeyName: str
    name: str

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
class GoogleCloudDiscoveryengineV1alphaImageCharacteristics(
    typing.TypedDict, total=False
):
    bitDepth: int
    colorSpace: typing.Literal[
        "COLOR_SPACE_UNSPECIFIED",
        "RGB",
        "CMYK",
        "GRAYSCALE",
        "YUV",
        "OTHER_COLOR_SPACE",
    ]
    height: int
    width: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportAgentFileRequest(
    typing.TypedDict, total=False
):
    fileName: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportAgentFileResponse(
    typing.TypedDict, total=False
):
    agentFile: GoogleCloudDiscoveryengineV1alphaAgentFile

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequest(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequestInlineSource(
    typing.TypedDict, total=False
):
    suggestions: _list[GoogleCloudDiscoveryengineV1alphaCompletionSuggestion]

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
class GoogleCloudDiscoveryengineV1alphaImportDocumentsRequest(
    typing.TypedDict, total=False
):
    alloyDbSource: GoogleCloudDiscoveryengineV1alphaAlloyDbSource
    autoGenerateIds: bool
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    bigtableSource: GoogleCloudDiscoveryengineV1alphaBigtableSource
    cloudSqlSource: GoogleCloudDiscoveryengineV1alphaCloudSqlSource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    fhirStoreSource: GoogleCloudDiscoveryengineV1alphaFhirStoreSource
    firestoreSource: GoogleCloudDiscoveryengineV1alphaFirestoreSource
    forceRefreshContent: bool
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    idField: str
    inlineSource: GoogleCloudDiscoveryengineV1alphaImportDocumentsRequestInlineSource
    reconciliationMode: typing.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    spannerSource: GoogleCloudDiscoveryengineV1alphaSpannerSource
    updateMask: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsRequestInlineSource(
    typing.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1alphaDocument]

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
class GoogleCloudDiscoveryengineV1alphaImportIdentityMappingsRequest(
    typing.TypedDict, total=False
):
    inlineSource: (
        GoogleCloudDiscoveryengineV1alphaImportIdentityMappingsRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportIdentityMappingsRequestInlineSource(
    typing.TypedDict, total=False
):
    identityMappingEntries: _list[GoogleCloudDiscoveryengineV1alphaIdentityMappingEntry]

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
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesRequest(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1alphaImportSampleQueriesRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesRequestInlineSource(
    typing.TypedDict, total=False
):
    sampleQueries: _list[GoogleCloudDiscoveryengineV1alphaSampleQuery]

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
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequest(
    typing.TypedDict, total=False
):
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequestInlineSource(
    typing.TypedDict, total=False
):
    entries: _list[GoogleCloudDiscoveryengineV1alphaSuggestionDenyListEntry]

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
class GoogleCloudDiscoveryengineV1alphaImportUserEventsRequest(
    typing.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1alphaImportUserEventsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsRequestInlineSource(
    typing.TypedDict, total=False
):
    userEvents: _list[GoogleCloudDiscoveryengineV1alphaUserEvent]

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
class GoogleCloudDiscoveryengineV1alphaLicenseConfigUsageStats(
    typing.TypedDict, total=False
):
    licenseConfig: str
    usedLicenseCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAgentsResponse(
    typing.TypedDict, total=False
):
    agents: _list[GoogleCloudDiscoveryengineV1alphaAgent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAlphaEvolveExperimentsResponse(
    typing.TypedDict, total=False
):
    alphaEvolveExperiments: _list[
        GoogleCloudDiscoveryengineV1alphaAlphaEvolveExperiment
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAlphaEvolveProgramsResponse(
    typing.TypedDict, total=False
):
    alphaEvolvePrograms: _list[GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgram]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAssistantsResponse(
    typing.TypedDict, total=False
):
    assistants: _list[GoogleCloudDiscoveryengineV1alphaAssistant]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAuthorizationsResponse(
    typing.TypedDict, total=False
):
    authorizations: _list[GoogleCloudDiscoveryengineV1alphaAuthorization]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListBillingAccountLicenseConfigsResponse(
    typing.TypedDict, total=False
):
    billingAccountLicenseConfigs: _list[
        GoogleCloudDiscoveryengineV1alphaBillingAccountLicenseConfig
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListBranchesResponse(
    typing.TypedDict, total=False
):
    branches: _list[GoogleCloudDiscoveryengineV1alphaBranch]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCannedQueriesResponse(
    typing.TypedDict, total=False
):
    cannedQueries: _list[GoogleCloudDiscoveryengineV1alphaCannedQuery]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListChunksResponse(
    typing.TypedDict, total=False
):
    chunks: _list[GoogleCloudDiscoveryengineV1alphaChunk]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCmekConfigsResponse(
    typing.TypedDict, total=False
):
    cmekConfigs: _list[GoogleCloudDiscoveryengineV1alphaCmekConfig]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCollectionsResponse(
    typing.TypedDict, total=False
):
    collections: _list[GoogleCloudDiscoveryengineV1alphaCollection]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListConnectorRunsResponse(
    typing.TypedDict, total=False
):
    connectorRuns: _list[GoogleCloudDiscoveryengineV1alphaConnectorRun]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListControlsResponse(
    typing.TypedDict, total=False
):
    controls: _list[GoogleCloudDiscoveryengineV1alphaControl]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListConversationsResponse(
    typing.TypedDict, total=False
):
    conversations: _list[GoogleCloudDiscoveryengineV1alphaConversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCustomModelsResponse(
    typing.TypedDict, total=False
):
    models: _list[GoogleCloudDiscoveryengineV1alphaCustomTuningModel]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListDataStoresResponse(
    typing.TypedDict, total=False
):
    dataStores: _list[GoogleCloudDiscoveryengineV1alphaDataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListDocumentsResponse(
    typing.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1alphaDocument]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEnginesResponse(
    typing.TypedDict, total=False
):
    engines: _list[GoogleCloudDiscoveryengineV1alphaEngine]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponse(
    typing.TypedDict, total=False
):
    evaluationResults: _list[
        GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseEvaluationResult
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseEvaluationResult(
    typing.TypedDict, total=False
):
    qualityMetrics: GoogleCloudDiscoveryengineV1alphaQualityMetrics
    sampleQuery: GoogleCloudDiscoveryengineV1alphaSampleQuery

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationsResponse(
    typing.TypedDict, total=False
):
    evaluations: _list[GoogleCloudDiscoveryengineV1alphaEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListFilesResponse(typing.TypedDict, total=False):
    files: _list[GoogleCloudDiscoveryengineV1alphaFileMetadata]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListIdentityMappingStoresResponse(
    typing.TypedDict, total=False
):
    identityMappingStores: _list[GoogleCloudDiscoveryengineV1alphaIdentityMappingStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListIdentityMappingsResponse(
    typing.TypedDict, total=False
):
    identityMappingEntries: _list[GoogleCloudDiscoveryengineV1alphaIdentityMappingEntry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListLicenseConfigsResponse(
    typing.TypedDict, total=False
):
    licenseConfigs: _list[GoogleCloudDiscoveryengineV1alphaLicenseConfig]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListLicenseConfigsUsageStatsResponse(
    typing.TypedDict, total=False
):
    licenseConfigUsageStats: _list[
        GoogleCloudDiscoveryengineV1alphaLicenseConfigUsageStats
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sampleQueries: _list[GoogleCloudDiscoveryengineV1alphaSampleQuery]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sampleQuerySets: _list[GoogleCloudDiscoveryengineV1alphaSampleQuerySet]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSchemasResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    schemas: _list[GoogleCloudDiscoveryengineV1alphaSchema]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListServingConfigsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudDiscoveryengineV1alphaServingConfig]

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
class GoogleCloudDiscoveryengineV1alphaListTargetSitesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListUserLicensesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    userLicenses: _list[GoogleCloudDiscoveryengineV1alphaUserLicense]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaManagedAgentDefinition(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaMediaInfo(typing.TypedDict, total=False):
    mediaProgressDuration: str
    mediaProgressPercentage: float

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
class GoogleCloudDiscoveryengineV1alphaObtainCrawlRateRequest(
    typing.TypedDict, total=False
):
    crawlRateScope: str

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
class GoogleCloudDiscoveryengineV1alphaOutputConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudDiscoveryengineV1alphaBigQueryDestination

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPageInfo(typing.TypedDict, total=False):
    pageCategory: str
    pageviewId: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPanelInfo(typing.TypedDict, total=False):
    displayName: str
    documents: _list[GoogleCloudDiscoveryengineV1alphaDocumentInfo]
    panelId: str
    panelPosition: int
    totalPanels: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPatientFilterOperationMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    filtersAddedCount: str
    filtersRemovedCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPauseEngineRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPrincipal(typing.TypedDict, total=False):
    externalEntityId: str
    groupId: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProcessedDocument(typing.TypedDict, total=False):
    document: str
    jsonData: str

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
class GoogleCloudDiscoveryengineV1alphaProvisionProjectRequest(
    typing.TypedDict, total=False
):
    acceptDataUseTerms: bool
    dataUseTermsVersion: str
    saasParams: GoogleCloudDiscoveryengineV1alphaProvisionProjectRequestSaasParams

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProvisionProjectRequestSaasParams(
    typing.TypedDict, total=False
):
    acceptBizQos: bool
    isBiz: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsRequest(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequest(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaPurgeErrorConfig
    filter: str
    force: bool
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequestInlineSource(
    typing.TypedDict, total=False
):
    documents: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponse(
    typing.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeErrorConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeIdentityMappingsRequest(
    typing.TypedDict, total=False
):
    filter: str
    force: bool
    inlineSource: (
        GoogleCloudDiscoveryengineV1alphaPurgeIdentityMappingsRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeIdentityMappingsRequestInlineSource(
    typing.TypedDict, total=False
):
    identityMappingEntries: _list[GoogleCloudDiscoveryengineV1alphaIdentityMappingEntry]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesRequest(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsRequest(
    typing.TypedDict, total=False
):
    filter: str
    force: bool

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
class GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponse(
    typing.TypedDict, total=False
):
    metricUsages: _list[
        GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponseMetricUsage
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponseDatedUsage(
    typing.TypedDict, total=False
):
    date: GoogleTypeDate
    usage: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponseMetricUsage(
    typing.TypedDict, total=False
):
    datedUsages: _list[
        GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponseDatedUsage
    ]
    metricType: typing.Literal[
        "BILLING_METRIC_TYPE_UNSPECIFIED",
        "DAILY_MDN_QPM",
        "DAILY_MIN_QPM",
        "DAILY_MAX_QPM",
        "DAILY_SEARCH_REQUEST",
        "TOTAL_STORAGE",
    ]
    totalUsage: float

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
class GoogleCloudDiscoveryengineV1alphaRankRequest(typing.TypedDict, total=False):
    ignoreRecordDetailsInResponse: bool
    model: str
    query: str
    records: _list[GoogleCloudDiscoveryengineV1alphaRankingRecord]
    topN: int
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRankResponse(typing.TypedDict, total=False):
    records: _list[GoogleCloudDiscoveryengineV1alphaRankingRecord]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRankingRecord(typing.TypedDict, total=False):
    content: str
    id: str
    score: float
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecommendRequest(typing.TypedDict, total=False):
    filter: str
    pageSize: int
    params: dict[str, typing.Any]
    userEvent: GoogleCloudDiscoveryengineV1alphaUserEvent
    userLabels: dict[str, typing.Any]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecommendResponse(typing.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[
        GoogleCloudDiscoveryengineV1alphaRecommendResponseRecommendationResult
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecommendResponseRecommendationResult(
    typing.TypedDict, total=False
):
    document: GoogleCloudDiscoveryengineV1alphaDocument
    id: str
    metadata: dict[str, typing.Any]

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
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisRequest(
    typing.TypedDict, total=False
):
    siteCredential: str
    uris: _list[str]

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
class GoogleCloudDiscoveryengineV1alphaRefreshTokenInfo(typing.TypedDict, total=False):
    name: str
    scopes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveDedicatedCrawlRateMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveDedicatedCrawlRateRequest(
    typing.TypedDict, total=False
):
    crawlRateScope: str

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
class GoogleCloudDiscoveryengineV1alphaRemoveSuggestionRequest(
    typing.TypedDict, total=False
):
    removeAllSearchHistorySuggestions: bool
    removeTime: str
    searchHistorySuggestion: str
    userInfo: GoogleCloudDiscoveryengineV1alphaUserInfo
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveSuggestionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReplacePatientFilterRequest(
    typing.TypedDict, total=False
):
    dataStore: str
    filterGroups: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReply(typing.TypedDict, total=False):
    references: _list[GoogleCloudDiscoveryengineV1alphaReplyReference]
    reply: str
    summary: GoogleCloudDiscoveryengineV1alphaSearchResponseSummary

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReplyReference(typing.TypedDict, total=False):
    anchorText: str
    end: int
    start: int
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReportConsentChangeRequest(
    typing.TypedDict, total=False
):
    consentChangeAction: typing.Literal["CONSENT_CHANGE_ACTION_UNSPECIFIED", "ACCEPT"]
    serviceTermId: str
    serviceTermVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirement(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    description: str
    displayName: str
    metricBindings: _list[GoogleCloudDiscoveryengineV1alphaRequirementMetricBinding]
    severity: _list[str]
    thresholdBindings: _list[
        GoogleCloudDiscoveryengineV1alphaRequirementThresholdBinding
    ]
    type: str
    violationSamplesBindings: _list[
        GoogleCloudDiscoveryengineV1alphaRequirementViolationSamplesBinding
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirementMetricBinding(
    typing.TypedDict, total=False
):
    category: str
    description: str
    metricFilter: str
    resourceType: str
    variableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirementThresholdBinding(
    typing.TypedDict, total=False
):
    description: str
    thresholdValues: _list[
        GoogleCloudDiscoveryengineV1alphaRequirementThresholdBindingThresholdValue
    ]
    variableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirementThresholdBindingThresholdValue(
    typing.TypedDict, total=False
):
    severity: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirementViolationSamplesBinding(
    typing.TypedDict, total=False
):
    description: str
    sampleFilter: str
    variableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaResumeEngineRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaResumeExperimentMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaResumeExperimentRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRetractLicenseConfigRequest(
    typing.TypedDict, total=False
):
    fullRetract: bool
    licenseConfig: str
    licenseCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRetractLicenseConfigResponse(
    typing.TypedDict, total=False
):
    licenseConfig: GoogleCloudDiscoveryengineV1alphaLicenseConfig

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
class GoogleCloudDiscoveryengineV1alphaSampleQuery(typing.TypedDict, total=False):
    createTime: str
    name: str
    queryEntry: GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntry

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntry(
    typing.TypedDict, total=False
):
    query: str
    targets: _list[GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntryTarget]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntryTarget(
    typing.TypedDict, total=False
):
    pageNumbers: _list[int]
    score: float
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQuerySet(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSchema(typing.TypedDict, total=False):
    fieldConfigs: _list[GoogleCloudDiscoveryengineV1alphaFieldConfig]
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchInfo(typing.TypedDict, total=False):
    offset: int
    orderBy: str
    searchQuery: str

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
class GoogleCloudDiscoveryengineV1alphaSearchResponse(typing.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    correctedQuery: str
    facets: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseFacet]
    geoSearchDebugInfo: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseGeoSearchDebugInfo
    ]
    guidedSearchResult: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResult
    )
    naturalLanguageQueryUnderstandingInfo: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfo
    nextPageToken: str
    oneBoxResults: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseOneBoxResult]
    queryExpansionInfo: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseQueryExpansionInfo
    )
    redirectUri: str
    results: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult]
    searchLinkPromotions: _list[GoogleCloudDiscoveryengineV1alphaSearchLinkPromotion]
    semanticState: typing.Literal["SEMANTIC_STATE_UNSPECIFIED", "DISABLED", "ENABLED"]
    sessionInfo: GoogleCloudDiscoveryengineV1alphaSearchResponseSessionInfo
    suggestedQuery: str
    summary: GoogleCloudDiscoveryengineV1alphaSearchResponseSummary
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseFacet(
    typing.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseFacetFacetValue(
    typing.TypedDict, total=False
):
    count: str
    interval: GoogleCloudDiscoveryengineV1alphaInterval
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseGeoSearchDebugInfo(
    typing.TypedDict, total=False
):
    errorMessage: str
    originalAddressQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResult(
    typing.TypedDict, total=False
):
    followUpQuestions: _list[str]
    refinementAttributes: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResultRefinementAttribute
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResultRefinementAttribute(
    typing.TypedDict, total=False
):
    attributeKey: str
    attributeValue: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfo(
    typing.TypedDict, total=False
):
    classifiedIntents: _list[str]
    extractedFilters: str
    rewrittenQuery: str
    structuredExtractedFilter: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilter

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilter(
    typing.TypedDict, total=False
):
    expression: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterAndExpression(
    typing.TypedDict, total=False
):
    expressions: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression(
    typing.TypedDict, total=False
):
    andExpr: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterAndExpression
    geolocationConstraint: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterGeolocationConstraint
    numberConstraint: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterNumberConstraint
    orExpr: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterOrExpression
    stringConstraint: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterStringConstraint

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterGeolocationConstraint(
    typing.TypedDict, total=False
):
    address: str
    fieldName: str
    latitude: float
    longitude: float
    radiusInMeters: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterNumberConstraint(
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
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterOrExpression(
    typing.TypedDict, total=False
):
    expressions: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterStringConstraint(
    typing.TypedDict, total=False
):
    fieldName: str
    querySegment: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseOneBoxResult(
    typing.TypedDict, total=False
):
    oneBoxType: typing.Literal[
        "ONE_BOX_TYPE_UNSPECIFIED", "PEOPLE", "ORGANIZATION", "SLACK", "KNOWLEDGE_GRAPH"
    ]
    searchResults: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseQueryExpansionInfo(
    typing.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult(
    typing.TypedDict, total=False
):
    chunk: GoogleCloudDiscoveryengineV1alphaChunk
    document: GoogleCloudDiscoveryengineV1alphaDocument
    id: str
    modelScores: dict[str, typing.Any]
    rankSignals: GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResultRankSignals
    retrievalSignals: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResultRetrievalSignals
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResultRankSignals(
    typing.TypedDict, total=False
):
    boostingFactor: float
    customSignals: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResultRankSignalsCustomSignal
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
class GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResultRankSignalsCustomSignal(
    typing.TypedDict, total=False
):
    name: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResultRetrievalSignals(
    typing.TypedDict, total=False
):
    retrievalSources: _list[
        typing.Literal[
            "RETRIEVAL_SOURCE_UNSPECIFIED", "KEYWORD_SEARCH", "SEMANTIC_SEARCH"
        ]
    ]
    semanticRelevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSessionInfo(
    typing.TypedDict, total=False
):
    name: str
    queryId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummary(
    typing.TypedDict, total=False
):
    safetyAttributes: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySafetyAttributes
    )
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
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummaryWithMetadata
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryBlobAttachment(
    typing.TypedDict, total=False
):
    attributionType: typing.Literal[
        "ATTRIBUTION_TYPE_UNSPECIFIED", "CORPUS", "GENERATED"
    ]
    data: GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryBlobAttachmentBlob

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryBlobAttachmentBlob(
    typing.TypedDict, total=False
):
    data: str
    mimeType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitation(
    typing.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationMetadata(
    typing.TypedDict, total=False
):
    citations: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitation]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationSource(
    typing.TypedDict, total=False
):
    referenceIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReference(
    typing.TypedDict, total=False
):
    chunkContents: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReferenceChunkContent
    ]
    document: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReferenceChunkContent(
    typing.TypedDict, total=False
):
    blobAttachmentIndexes: _list[str]
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySafetyAttributes(
    typing.TypedDict, total=False
):
    categories: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummaryWithMetadata(
    typing.TypedDict, total=False
):
    blobAttachments: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryBlobAttachment
    ]
    citationMetadata: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationMetadata
    )
    references: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReference]
    summary: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaServingConfig(typing.TypedDict, total=False):
    answerGenerationSpec: GoogleCloudDiscoveryengineV1alphaAnswerGenerationSpec
    boostControlIds: _list[str]
    createTime: str
    customFineTuningSpec: GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec
    displayName: str
    dissociateControlIds: _list[str]
    diversityLevel: str
    embeddingConfig: GoogleCloudDiscoveryengineV1alphaEmbeddingConfig
    filterControlIds: _list[str]
    genericConfig: GoogleCloudDiscoveryengineV1alphaServingConfigGenericConfig
    guidedSearchSpec: GoogleCloudDiscoveryengineV1alphaGuidedSearchSpec
    ignoreControlIds: _list[str]
    mediaConfig: GoogleCloudDiscoveryengineV1alphaServingConfigMediaConfig
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    personalizationSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestPersonalizationSpec
    )
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
class GoogleCloudDiscoveryengineV1alphaServingConfigGenericConfig(
    typing.TypedDict, total=False
):
    contentSearchSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaServingConfigMediaConfig(
    typing.TypedDict, total=False
):
    contentFreshnessCutoffDays: int
    contentWatchedPercentageThreshold: float
    contentWatchedSecondsThreshold: float
    demoteContentWatchedPastDays: int
    demotionEventType: str

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
class GoogleCloudDiscoveryengineV1alphaSetDedicatedCrawlRateRequest(
    typing.TypedDict, total=False
):
    crawlRate: int
    crawlRateScope: str
    crawlType: typing.Literal[
        "CRAWL_TYPE_UNSPECIFIED", "USER_TRIGGERED", "AUTO_REFRESH"
    ]
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTOMATIC", "EXPLICIT"]

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
class GoogleCloudDiscoveryengineV1alphaSetUpDataConnectorRequest(
    typing.TypedDict, total=False
):
    collectionDisplayName: str
    collectionId: str
    dataConnector: GoogleCloudDiscoveryengineV1alphaDataConnector

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataRequest(
    typing.TypedDict, total=False
):
    documentDataMap: dict[str, typing.Any]
    emptyDocumentDataMap: bool
    schema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSingleRegionKey(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSiteSearchEngine(typing.TypedDict, total=False):
    name: str

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
class GoogleCloudDiscoveryengineV1alphaSpannerSource(typing.TypedDict, total=False):
    databaseId: str
    enableDataBoost: bool
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStartConnectorRunRequest(
    typing.TypedDict, total=False
):
    entities: _list[str]
    forceRefreshContent: bool
    healthcareFhirResourceTypes: _list[str]
    syncIdentity: bool
    syncSinceTimestamp: str

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
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequest(
    typing.TypedDict, total=False
):
    actionSpec: GoogleCloudDiscoveryengineV1alphaStreamAssistRequestActionSpec
    generationSpec: GoogleCloudDiscoveryengineV1alphaStreamAssistRequestGenerationSpec
    query: GoogleCloudDiscoveryengineV1alphaQuery
    session: str
    toolsSpec: GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpec
    userMetadata: GoogleCloudDiscoveryengineV1alphaAssistUserMetadata

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequestActionSpec(
    typing.TypedDict, total=False
):
    actionDisabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequestGenerationSpec(
    typing.TypedDict, total=False
):
    modelId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpec(
    typing.TypedDict, total=False
):
    imageGenerationSpec: (
        GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecImageGenerationSpec
    )
    vertexAiSearchSpec: (
        GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecVertexAiSearchSpec
    )
    videoGenerationSpec: (
        GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecVideoGenerationSpec
    )
    webGroundingSpec: (
        GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecWebGroundingSpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecImageGenerationSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecVertexAiSearchSpec(
    typing.TypedDict, total=False
):
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec]
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecVideoGenerationSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistRequestToolsSpecWebGroundingSpec(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistResponse(
    typing.TypedDict, total=False
):
    answer: GoogleCloudDiscoveryengineV1alphaAssistAnswer
    assistToken: str
    connectorAuthErrors: _list[
        GoogleCloudDiscoveryengineV1alphaStreamAssistResponseConnectorAuthError
    ]
    invocationTools: _list[str]
    invokedSkills: _list[
        GoogleCloudDiscoveryengineV1alphaStreamAssistResponseInvokedSkill
    ]
    sessionInfo: GoogleCloudDiscoveryengineV1alphaStreamAssistResponseSessionInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistResponseConnectorAuthError(
    typing.TypedDict, total=False
):
    dataConnector: str
    errorMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistResponseInvokedSkill(
    typing.TypedDict, total=False
):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistResponseSessionInfo(
    typing.TypedDict, total=False
):
    session: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSubmitProgramsEvaluationsRequest(
    typing.TypedDict, total=False
):
    evaluationSubmissions: _list[
        GoogleCloudDiscoveryengineV1alphaAlphaEvolveProgramEvaluationSubmission
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSubmitProgramsEvaluationsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSuggestionDenyListEntry(
    typing.TypedDict, total=False
):
    blockPhrase: str
    matchOperator: typing.Literal[
        "MATCH_OPERATOR_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"
    ]

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
class GoogleCloudDiscoveryengineV1alphaTextInput(typing.TypedDict, total=False):
    context: GoogleCloudDiscoveryengineV1alphaConversationContext
    input: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequest(
    typing.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsTrainingInput: (
        GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequestGcsTrainingInput
    )
    modelId: str
    modelType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequestGcsTrainingInput(
    typing.TypedDict, total=False
):
    corpusDataPath: str
    queryDataPath: str
    testDataPath: str
    trainDataPath: str

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
class GoogleCloudDiscoveryengineV1alphaTransactionInfo(typing.TypedDict, total=False):
    cost: float
    currency: str
    discountValue: float
    tax: float
    transactionId: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineMetadata(
    typing.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineRequest(
    typing.TypedDict, total=False
): ...

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
class GoogleCloudDiscoveryengineV1alphaUserEvent(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    attributionToken: str
    completionInfo: GoogleCloudDiscoveryengineV1alphaCompletionInfo
    conversionType: str
    dataStore: str
    directUserRequest: bool
    documents: _list[GoogleCloudDiscoveryengineV1alphaDocumentInfo]
    engine: str
    entity: str
    eventTime: str
    eventType: str
    feedback: GoogleCloudDiscoveryengineV1alphaFeedback
    filter: str
    mediaInfo: GoogleCloudDiscoveryengineV1alphaMediaInfo
    pageInfo: GoogleCloudDiscoveryengineV1alphaPageInfo
    panel: GoogleCloudDiscoveryengineV1alphaPanelInfo
    panels: _list[GoogleCloudDiscoveryengineV1alphaPanelInfo]
    promotionIds: _list[str]
    searchInfo: GoogleCloudDiscoveryengineV1alphaSearchInfo
    sessionId: str
    tagIds: _list[str]
    transactionInfo: GoogleCloudDiscoveryengineV1alphaTransactionInfo
    userInfo: GoogleCloudDiscoveryengineV1alphaUserInfo
    userPseudoId: str

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
class GoogleCloudDiscoveryengineV1alphaUserStore(typing.TypedDict, total=False):
    defaultLicenseConfig: str
    displayName: str
    enableExpiredLicenseAutoUpdate: bool
    enableLicenseAutoRegister: bool
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaVideoCharacteristics(
    typing.TypedDict, total=False
):
    audioBitrateKbps: int
    audioCodecs: _list[str]
    duration: str
    frameRate: float
    height: int
    videoBitrateKbps: int
    videoCodecs: _list[str]
    width: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfig(typing.TypedDict, total=False):
    accessSettings: GoogleCloudDiscoveryengineV1alphaWidgetConfigAccessSettings
    allowPublicAccess: bool
    allowlistedDomains: _list[str]
    assistantSettings: GoogleCloudDiscoveryengineV1alphaWidgetConfigAssistantSettings
    batchAuthStatuses: _list[
        GoogleCloudDiscoveryengineV1alphaWidgetConfigBatchAuthStatus
    ]
    collectionComponents: _list[
        GoogleCloudDiscoveryengineV1alphaWidgetConfigCollectionComponent
    ]
    configId: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec
    createTime: str
    customerProvidedConfig: (
        GoogleCloudDiscoveryengineV1alphaWidgetConfigCustomerProvidedConfig
    )
    dataStoreType: typing.Literal[
        "DATA_STORE_TYPE_UNSPECIFIED",
        "SITE_SEARCH",
        "STRUCTURED",
        "UNSTRUCTURED",
        "BLENDED",
    ]
    dataStoreUiConfigs: _list[
        GoogleCloudDiscoveryengineV1alphaWidgetConfigDataStoreUiConfig
    ]
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
    facetField: _list[GoogleCloudDiscoveryengineV1alphaWidgetConfigFacetField]
    fieldsUiComponentsMap: dict[str, typing.Any]
    geminiBundle: bool
    homepageSetting: GoogleCloudDiscoveryengineV1alphaWidgetConfigHomepageSetting
    industryVertical: typing.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    llmEnabled: bool
    minimumDataTermAccepted: bool
    name: str
    nodes: _list[GoogleCloudDiscoveryengineV1alphaWidgetConfigNode]
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
    uiBranding: GoogleCloudDiscoveryengineV1alphaWidgetConfigUiBrandingSettings
    uiSettings: GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettings
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigAccessSettings(
    typing.TypedDict, total=False
):
    allowPublicAccess: bool
    allowlistedDomains: _list[str]
    enableWebApp: bool
    languageCode: str
    workforceIdentityPoolProvider: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigAssistantSettings(
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
class GoogleCloudDiscoveryengineV1alphaWidgetConfigBatchAuthStatus(
    typing.TypedDict, total=False
):
    batchAuthorizationGroup: str
    connectorAuthState: GoogleCloudDiscoveryengineV1alphaWidgetConfigConnectorAuthState
    placeholder: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigCollectionComponent(
    typing.TypedDict, total=False
):
    connectorAuthState: GoogleCloudDiscoveryengineV1alphaWidgetConfigConnectorAuthState
    connectorIconLink: str
    dataSource: str
    dataSourceDisplayName: str
    dataSourceEndUserDisplayName: str
    dataSourceVersion: float
    dataStoreComponents: _list[
        GoogleCloudDiscoveryengineV1alphaWidgetConfigDataStoreComponent
    ]
    displayName: str
    id: str
    isFirstParty: bool
    metadata: GoogleCloudDiscoveryengineV1alphaDataConnectorConnectorMetadata
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigConnectorAuthState(
    typing.TypedDict, total=False
):
    authState: typing.Literal[
        "AUTH_STATE_UNSPECIFIED", "AUTHORIZED", "EXPIRED", "ACTIONS_DISABLED", "NO_AUTH"
    ]
    authorizationUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigCustomerProvidedConfig(
    typing.TypedDict, total=False
):
    customerType: typing.Literal["DEFAULT_CUSTOMER", "GOVERNMENT_CUSTOMER"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigDataStoreComponent(
    typing.TypedDict, total=False
):
    contentConfig: typing.Literal[
        "CONTENT_CONFIG_UNSPECIFIED",
        "NO_CONTENT",
        "CONTENT_REQUIRED",
        "PUBLIC_WEBSITE",
        "GOOGLE_WORKSPACE",
    ]
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
    workspaceType: typing.Literal[
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
class GoogleCloudDiscoveryengineV1alphaWidgetConfigDataStoreUiConfig(
    typing.TypedDict, total=False
):
    facetField: _list[GoogleCloudDiscoveryengineV1alphaWidgetConfigFacetField]
    fieldsUiComponentsMap: dict[str, typing.Any]
    id: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigFacetField(
    typing.TypedDict, total=False
):
    displayName: str
    field: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigHomepageSetting(
    typing.TypedDict, total=False
):
    shortcuts: _list[
        GoogleCloudDiscoveryengineV1alphaWidgetConfigHomepageSettingShortcut
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigHomepageSettingShortcut(
    typing.TypedDict, total=False
):
    destinationUri: str
    icon: GoogleCloudDiscoveryengineV1alphaWidgetConfigImage
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigImage(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigNode(typing.TypedDict, total=False):
    description: str
    displayName: str
    iconUrl: str
    outputSchema: dict[str, typing.Any]
    parameterSchema: dict[str, typing.Any]
    type: typing.Literal["TYPE_UNSPECIFIED", "TRIGGER", "FLOW", "CONNECTOR"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUIComponentField(
    typing.TypedDict, total=False
):
    deviceVisibility: _list[
        typing.Literal["DEVICE_VISIBILITY_UNSPECIFIED", "MOBILE", "DESKTOP"]
    ]
    displayTemplate: str
    field: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUiBrandingSettings(
    typing.TypedDict, total=False
):
    logo: GoogleCloudDiscoveryengineV1alphaWidgetConfigImage

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettings(
    typing.TypedDict, total=False
):
    dataStoreUiConfigs: _list[
        GoogleCloudDiscoveryengineV1alphaWidgetConfigDataStoreUiConfig
    ]
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
        GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsGenerativeAnswerConfig
    )
    googleDrivePickerEnabled: bool
    interactionType: typing.Literal[
        "INTERACTION_TYPE_UNSPECIFIED",
        "SEARCH_ONLY",
        "SEARCH_WITH_ANSWER",
        "SEARCH_WITH_FOLLOW_UPS",
    ]
    modelConfigInfo: (
        GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsModelConfigInfo
    )
    modelConfigs: dict[str, typing.Any]
    onedrivePickerEnabled: bool
    resultDescriptionType: typing.Literal[
        "RESULT_DISPLAY_TYPE_UNSPECIFIED", "SNIPPET", "EXTRACTIVE_ANSWER"
    ]
    searchAddonSpec: (
        GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsSearchAddonSpec
    )
    sourceAdminDisplayNameEnabled: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsGenerativeAnswerConfig(
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
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsModelConfigInfo(
    typing.TypedDict, total=False
):
    defaultModelId: str
    resolvedModels: _list[
        GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsModelConfigInfoResolvedModel
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsModelConfigInfoResolvedModel(
    typing.TypedDict, total=False
):
    adminView: GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsModelConfigInfoResolvedModelAdminView
    description: str
    displayName: str
    icon: str
    isPreview: bool
    label: str
    modelId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsModelConfigInfoResolvedModelAdminView(
    typing.TypedDict, total=False
):
    adminOverridable: bool
    enabledByDefault: bool
    regions: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigUiSettingsSearchAddonSpec(
    typing.TypedDict, total=False
):
    generativeAnswerAddOnDisabled: bool
    kpiPersonalizationAddOnDisabled: bool
    semanticAddOnDisabled: bool

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
class GoogleCloudDiscoveryengineV1alphaWorkspaceSettings(typing.TypedDict, total=False):
    customerDomainValid: bool
    workspaceAccessEnabled: bool

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
class GoogleCloudNotebooklmV1alphaAccountAndRole(typing.TypedDict, total=False):
    email: str
    role: typing.Literal[
        "PROJECT_ROLE_UNKNOWN",
        "PROJECT_ROLE_OWNER",
        "PROJECT_ROLE_WRITER",
        "PROJECT_ROLE_READER",
        "PROJECT_ROLE_NOT_SHARED",
    ]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaAgentspaceMetadata(typing.TypedDict, total=False):
    documentName: str
    documentTitle: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaAudioOverview(typing.TypedDict, total=False):
    audioOverviewId: str
    generationOptions: GoogleCloudNotebooklmV1alphaAudioOverviewGenerationOptions
    languageCode: str
    mimeType: typing.Literal["MIME_TYPE_UNKNOWN", "MIME_TYPE_WAV", "MIME_TYPE_MP4"]
    name: str
    status: typing.Literal[
        "AUDIO_OVERVIEW_STATUS_UNSPECIFIED",
        "AUDIO_OVERVIEW_STATUS_NOT_STARTED",
        "AUDIO_OVERVIEW_STATUS_IN_PROGRESS",
        "AUDIO_OVERVIEW_STATUS_COMPLETE",
        "AUDIO_OVERVIEW_STATUS_FAILED",
    ]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaAudioOverviewGenerationOptions(
    typing.TypedDict, total=False
):
    episodeFocus: str
    languageCode: str
    sourceIds: _list[GoogleCloudNotebooklmV1alphaSourceId]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaBatchCreateSourcesRequest(
    typing.TypedDict, total=False
):
    userContents: _list[GoogleCloudNotebooklmV1alphaUserContent]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaBatchCreateSourcesResponse(
    typing.TypedDict, total=False
):
    sources: _list[GoogleCloudNotebooklmV1alphaSource]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaBatchDeleteNotebooksRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaBatchDeleteSourcesRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaCmekConfig(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaCreateAudioOverviewRequest(
    typing.TypedDict, total=False
):
    generationOptions: GoogleCloudNotebooklmV1alphaAudioOverviewGenerationOptions

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaCreateAudioOverviewResponse(
    typing.TypedDict, total=False
):
    audioOverview: GoogleCloudNotebooklmV1alphaAudioOverview

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReason(typing.TypedDict, total=False):
    audioTranscriptionError: (
        GoogleCloudNotebooklmV1alphaFailureReasonAudioTranscriptionError
    )
    domainBlocked: GoogleCloudNotebooklmV1alphaFailureReasonDomainBlocked
    googleDriveError: GoogleCloudNotebooklmV1alphaFailureReasonGoogleDriveError
    ingestionError: GoogleCloudNotebooklmV1alphaFailureReasonIngestionError
    mimeTypeBlocked: GoogleCloudNotebooklmV1alphaFailureReasonMimeTypeBlocked
    paywallError: GoogleCloudNotebooklmV1alphaFailureReasonPaywallError
    policyCheckFailed: GoogleCloudNotebooklmV1alphaFailureReasonPolicyCheckFailed
    sourceEmpty: GoogleCloudNotebooklmV1alphaFailureReasonSourceEmpty
    sourceLimitExceeded: GoogleCloudNotebooklmV1alphaFailureReasonSourceLimitExceeded
    sourceTooLong: GoogleCloudNotebooklmV1alphaFailureReasonSourceTooLong
    sourceUnreachable: GoogleCloudNotebooklmV1alphaFailureReasonSourceUnreachable
    unknown: GoogleCloudNotebooklmV1alphaFailureReasonUnknown
    uploadError: GoogleCloudNotebooklmV1alphaFailureReasonUploadError
    youtubeError: GoogleCloudNotebooklmV1alphaFailureReasonYoutubeError

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonAudioTranscriptionError(
    typing.TypedDict, total=False
):
    languageDetectionFailed: GoogleCloudNotebooklmV1alphaFailureReasonAudioTranscriptionErrorLanguageDetectionFailed
    noAudioDetected: (
        GoogleCloudNotebooklmV1alphaFailureReasonAudioTranscriptionErrorNoAudioDetected
    )

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonAudioTranscriptionErrorLanguageDetectionFailed(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonAudioTranscriptionErrorNoAudioDetected(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonDomainBlocked(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonGoogleDriveError(
    typing.TypedDict, total=False
):
    downloadPrevented: (
        GoogleCloudNotebooklmV1alphaFailureReasonGoogleDriveErrorDownloadPrevented
    )

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonGoogleDriveErrorDownloadPrevented(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonIngestionError(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonMimeTypeBlocked(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonPaywallError(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonPolicyCheckFailed(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonSourceEmpty(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonSourceLimitExceeded(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonSourceTooLong(
    typing.TypedDict, total=False
):
    wordCount: int
    wordLimit: int

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonSourceUnreachable(
    typing.TypedDict, total=False
):
    errorDetails: typing.Literal[
        "ERROR_REASON_UNSPECIFIED",
        "ERROR_REASON_INVALID_URL",
        "ERROR_REASON_NOT_ACCESSIBLE",
        "ERROR_REASON_NOT_REACHABLE",
        "ERROR_REASON_URL_NOT_FOUND",
        "ERROR_REASON_TRANSIENT_ERROR",
        "ERROR_REASON_FETCH_FAILED",
        "ERROR_REASON_NOT_SUPPORTED",
    ]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonUnknown(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonUploadError(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonYoutubeError(
    typing.TypedDict, total=False
):
    videoDeleted: GoogleCloudNotebooklmV1alphaFailureReasonYoutubeErrorVideoDeleted

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaFailureReasonYoutubeErrorVideoDeleted(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaGoogleDocsSourceMetadata(
    typing.TypedDict, total=False
):
    documentId: str
    revisionId: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaListRecentlyViewedNotebooksResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    notebooks: _list[GoogleCloudNotebooklmV1alphaNotebook]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaNotebook(typing.TypedDict, total=False):
    cmekConfig: GoogleCloudNotebooklmV1alphaCmekConfig
    emoji: str
    metadata: GoogleCloudNotebooklmV1alphaNotebookMetadata
    name: str
    notebookId: str
    sources: _list[GoogleCloudNotebooklmV1alphaSource]
    title: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaNotebookMetadata(typing.TypedDict, total=False):
    createTime: str
    isShareable: bool
    isShared: bool
    lastViewed: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaShareNotebookRequest(typing.TypedDict, total=False):
    accountAndRoles: _list[GoogleCloudNotebooklmV1alphaAccountAndRole]
    notifyViaEmail: bool

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaShareNotebookResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaSource(typing.TypedDict, total=False):
    metadata: GoogleCloudNotebooklmV1alphaSourceMetadata
    name: str
    settings: GoogleCloudNotebooklmV1alphaSourceSettings
    sourceId: GoogleCloudNotebooklmV1alphaSourceId
    title: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaSourceId(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaSourceMetadata(typing.TypedDict, total=False):
    agentspaceMetadata: GoogleCloudNotebooklmV1alphaAgentspaceMetadata
    googleDocsMetadata: GoogleCloudNotebooklmV1alphaGoogleDocsSourceMetadata
    sourceAddedTimestamp: str
    tokenCount: int
    wordCount: int
    youtubeMetadata: GoogleCloudNotebooklmV1alphaYoutubeMetadata

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaSourceSettings(typing.TypedDict, total=False):
    failureReason: GoogleCloudNotebooklmV1alphaFailureReason
    status: typing.Literal[
        "SOURCE_STATUS_UNSPECIFIED",
        "SOURCE_STATUS_PENDING",
        "SOURCE_STATUS_COMPLETE",
        "SOURCE_STATUS_ERROR",
        "SOURCE_STATUS_PENDING_DELETION",
        "SOURCE_STATUS_TENTATIVE",
    ]

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaUserContent(typing.TypedDict, total=False):
    agentspaceContent: GoogleCloudNotebooklmV1alphaUserContentAgentspaceContent
    googleDriveContent: GoogleCloudNotebooklmV1alphaUserContentGoogleDriveContent
    textContent: GoogleCloudNotebooklmV1alphaUserContentTextContent
    videoContent: GoogleCloudNotebooklmV1alphaUserContentVideoContent
    webContent: GoogleCloudNotebooklmV1alphaUserContentWebContent

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaUserContentAgentspaceContent(
    typing.TypedDict, total=False
):
    documentName: str
    engineName: str
    ideaforgeIdeaName: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaUserContentGoogleDriveContent(
    typing.TypedDict, total=False
):
    documentId: str
    mimeType: str
    sourceName: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaUserContentTextContent(typing.TypedDict, total=False):
    content: str
    sourceName: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaUserContentVideoContent(
    typing.TypedDict, total=False
):
    youtubeUrl: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaUserContentWebContent(typing.TypedDict, total=False):
    sourceName: str
    url: str

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaYoutubeMetadata(typing.TypedDict, total=False):
    channelName: str
    videoId: str

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
