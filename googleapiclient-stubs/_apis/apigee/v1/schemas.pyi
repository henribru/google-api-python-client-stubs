import typing

_list = list

@typing.type_check_only
class EdgeConfigstoreBundleBadBundle(typing.TypedDict, total=False):
    violations: _list[EdgeConfigstoreBundleBadBundleViolation]

@typing.type_check_only
class EdgeConfigstoreBundleBadBundleViolation(typing.TypedDict, total=False):
    description: str
    filename: str

@typing.type_check_only
class GoogleApiHttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudApigeeV1APIProductAssociation(typing.TypedDict, total=False):
    apiproduct: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1Access(typing.TypedDict, total=False):
    Get: GoogleCloudApigeeV1AccessGet
    Remove: GoogleCloudApigeeV1AccessRemove
    Set: GoogleCloudApigeeV1AccessSet

@typing.type_check_only
class GoogleCloudApigeeV1AccessGet(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1AccessLoggingConfig(typing.TypedDict, total=False):
    enabled: bool
    filter: str

@typing.type_check_only
class GoogleCloudApigeeV1AccessRemove(typing.TypedDict, total=False):
    name: str
    success: bool

@typing.type_check_only
class GoogleCloudApigeeV1AccessSet(typing.TypedDict, total=False):
    name: str
    success: bool
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1ActivateNatAddressRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1AddonsConfig(typing.TypedDict, total=False):
    advancedApiOpsConfig: GoogleCloudApigeeV1AdvancedApiOpsConfig
    analyticsConfig: GoogleCloudApigeeV1AnalyticsConfig
    apiSecurityConfig: GoogleCloudApigeeV1ApiSecurityConfig
    connectorsPlatformConfig: GoogleCloudApigeeV1ConnectorsPlatformConfig
    integrationConfig: GoogleCloudApigeeV1IntegrationConfig
    monetizationConfig: GoogleCloudApigeeV1MonetizationConfig

@typing.type_check_only
class GoogleCloudApigeeV1AdjustAppGroupBalanceRequest(typing.TypedDict, total=False):
    adjustment: GoogleTypeMoney

@typing.type_check_only
class GoogleCloudApigeeV1AdjustDeveloperBalanceRequest(typing.TypedDict, total=False):
    adjustment: GoogleTypeMoney

@typing.type_check_only
class GoogleCloudApigeeV1AdvancedApiOpsConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1Alias(typing.TypedDict, total=False):
    alias: str
    certsInfo: GoogleCloudApigeeV1Certificate
    type: typing.Literal["ALIAS_TYPE_UNSPECIFIED", "CERT", "KEY_CERT"]

@typing.type_check_only
class GoogleCloudApigeeV1AliasRevisionConfig(typing.TypedDict, total=False):
    location: str
    name: str
    type: typing.Literal["ALIAS_TYPE_UNSPECIFIED", "CERT", "KEY_CERT"]

@typing.type_check_only
class GoogleCloudApigeeV1AnalyticsConfig(typing.TypedDict, total=False):
    enabled: bool
    expireTimeMillis: str
    state: typing.Literal[
        "ADDON_STATE_UNSPECIFIED", "ENABLING", "ENABLED", "DISABLING", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiCategory(typing.TypedDict, total=False):
    id: str
    name: str
    siteId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiCategoryResponse(typing.TypedDict, total=False):
    data: GoogleCloudApigeeV1ApiCategory
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiDebugSession(typing.TypedDict, total=False):
    apiProxyRevisionId: str
    createTime: str
    environmentId: str
    id: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiDoc(typing.TypedDict, total=False):
    anonAllowed: bool
    apiProductName: str
    categoryIds: _list[str]
    description: str
    edgeAPIProductName: str
    graphqlEndpointUrl: str
    graphqlSchema: str
    graphqlSchemaDisplayName: str
    id: str
    imageUrl: str
    modified: str
    published: bool
    requireCallbackUrl: bool
    siteId: str
    specId: str
    title: str
    visibility: bool

@typing.type_check_only
class GoogleCloudApigeeV1ApiDocDocumentation(typing.TypedDict, total=False):
    asyncApiDocumentation: GoogleCloudApigeeV1AsyncApiDocumentation
    graphqlDocumentation: GoogleCloudApigeeV1GraphqlDocumentation
    oasDocumentation: GoogleCloudApigeeV1OASDocumentation

@typing.type_check_only
class GoogleCloudApigeeV1ApiDocDocumentationResponse(typing.TypedDict, total=False):
    data: GoogleCloudApigeeV1ApiDocDocumentation
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiDocResponse(typing.TypedDict, total=False):
    data: GoogleCloudApigeeV1ApiDoc
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProduct(typing.TypedDict, total=False):
    apiResources: _list[str]
    approvalType: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    createdAt: str
    description: str
    displayName: str
    environments: _list[str]
    graphqlOperationGroup: GoogleCloudApigeeV1GraphQLOperationGroup
    grpcOperationGroup: GoogleCloudApigeeV1GrpcOperationGroup
    lastModifiedAt: str
    llmOperationGroup: GoogleCloudApigeeV1LlmOperationGroup
    llmQuota: str
    llmQuotaInterval: str
    llmQuotaTimeUnit: str
    name: str
    operationGroup: GoogleCloudApigeeV1OperationGroup
    payloadOperationGroup: GoogleCloudApigeeV1PayloadOperationGroup
    proxies: _list[str]
    quota: str
    quotaCounterScope: typing.Literal[
        "QUOTA_COUNTER_SCOPE_UNSPECIFIED", "PROXY", "OPERATION", "PRODUCT"
    ]
    quotaInterval: str
    quotaTimeUnit: str
    scopes: _list[str]
    space: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProductRef(typing.TypedDict, total=False):
    apiproduct: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxy(typing.TypedDict, total=False):
    apiProxyType: typing.Literal[
        "API_PROXY_TYPE_UNSPECIFIED", "PROGRAMMABLE", "CONFIGURABLE"
    ]
    labels: dict[str, typing.Any]
    latestRevisionId: str
    metaData: GoogleCloudApigeeV1EntityMetadata
    name: str
    readOnly: bool
    revision: _list[str]
    space: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxyRevision(typing.TypedDict, total=False):
    archive: str
    basepaths: _list[str]
    configurationVersion: GoogleCloudApigeeV1ConfigVersion
    contextInfo: str
    createdAt: str
    description: str
    displayName: str
    entityMetaDataAsProperties: dict[str, typing.Any]
    hasExtensiblePolicy: bool
    integrationEndpoints: _list[str]
    lastModifiedAt: str
    mcp: bool
    name: str
    policies: _list[str]
    proxies: _list[str]
    proxyEndpoints: _list[str]
    resourceFiles: GoogleCloudApigeeV1ResourceFiles
    resources: _list[str]
    revision: str
    sharedFlows: _list[str]
    spec: str
    targetEndpoints: _list[str]
    targetServers: _list[str]
    targets: _list[str]
    teams: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiSecurityConfig(typing.TypedDict, total=False):
    enabled: bool
    expiresAt: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiSecurityRuntimeConfig(typing.TypedDict, total=False):
    location: _list[str]
    name: str
    revisionId: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ApimServiceExtension(typing.TypedDict, total=False):
    createTime: str
    extensionProcessor: str
    extensions: _list[GoogleCloudApigeeV1ApimServiceExtensionExtension]
    lbForwardingRule: str
    name: str
    network: str
    networkConfigs: _list[GoogleCloudApigeeV1ApimServiceExtensionNetworkConfig]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ApimServiceExtensionExtension(typing.TypedDict, total=False):
    failOpen: bool
    hostname: str
    matchCondition: str
    name: str
    supportedEvents: _list[
        typing.Literal[
            "SUPPORTED_EVENT_UNSPECIFIED",
            "REQUEST_HEADERS",
            "REQUEST_BODY",
            "RESPONSE_HEADERS",
            "RESPONSE_BODY",
            "REQUEST_TRAILERS",
            "RESPONSE_TRAILERS",
        ]
    ]

@typing.type_check_only
class GoogleCloudApigeeV1ApimServiceExtensionNetworkConfig(
    typing.TypedDict, total=False
):
    region: str
    subnet: str

@typing.type_check_only
class GoogleCloudApigeeV1App(typing.TypedDict, total=False):
    apiProducts: _list[GoogleCloudApigeeV1ApiProductRef]
    appGroup: str
    appId: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    callbackUrl: str
    companyName: str
    createdAt: str
    credentials: _list[GoogleCloudApigeeV1Credential]
    developerEmail: str
    developerId: str
    keyExpiresIn: str
    lastModifiedAt: str
    name: str
    scopes: _list[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1AppGroup(typing.TypedDict, total=False):
    appGroupId: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    channelId: str
    channelUri: str
    createdAt: str
    displayName: str
    email: str
    lastModifiedAt: str
    name: str
    organization: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupApp(typing.TypedDict, total=False):
    apiProducts: _list[str]
    appGroup: str
    appId: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    callbackUrl: str
    createdAt: str
    credentials: _list[GoogleCloudApigeeV1Credential]
    keyExpiresIn: str
    lastModifiedAt: str
    name: str
    scopes: _list[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupAppKey(typing.TypedDict, total=False):
    apiProducts: _list[GoogleCloudApigeeV1APIProductAssociation]
    attributes: _list[GoogleCloudApigeeV1Attribute]
    consumerKey: str
    consumerSecret: str
    expiresAt: str
    expiresInSeconds: str
    issuedAt: str
    scopes: _list[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupBalance(typing.TypedDict, total=False):
    wallets: _list[GoogleCloudApigeeV1AppGroupBalanceWallet]

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupBalanceWallet(typing.TypedDict, total=False):
    balance: GoogleTypeMoney
    lastCreditTime: str

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupMonetizationConfig(typing.TypedDict, total=False):
    billingType: typing.Literal["BILLING_TYPE_UNSPECIFIED", "PREPAID", "POSTPAID"]

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupSubscription(typing.TypedDict, total=False):
    apiproduct: str
    createdAt: str
    endTime: str
    lastModifiedAt: str
    name: str
    startTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ArchiveDeployment(typing.TypedDict, total=False):
    createdAt: str
    gcsUri: str
    labels: dict[str, typing.Any]
    name: str
    operation: str
    updatedAt: str

@typing.type_check_only
class GoogleCloudApigeeV1AsyncApiDocumentation(typing.TypedDict, total=False):
    spec: GoogleCloudApigeeV1DocumentationFile

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQuery(typing.TypedDict, total=False):
    created: str
    envgroupHostname: str
    error: str
    executionTime: str
    name: str
    queryParams: GoogleCloudApigeeV1QueryMetadata
    reportDefinitionId: str
    result: GoogleCloudApigeeV1AsyncQueryResult
    resultFileSize: str
    resultRows: str
    self: str
    state: str
    updated: str

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQueryResult(typing.TypedDict, total=False):
    expires: str
    self: str

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQueryResultView(typing.TypedDict, total=False):
    code: int
    error: str
    metadata: GoogleCloudApigeeV1QueryMetadata
    rows: _list[typing.Any]
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1Attribute(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1Attributes(typing.TypedDict, total=False):
    attribute: _list[GoogleCloudApigeeV1Attribute]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequest(
    typing.TypedDict, total=False
):
    apiHubApis: (
        GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestApiHubApiArray
    )
    apiHubGateways: GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestApiHubGatewayArray
    include: (
        GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArray
    )
    includeAllResources: (
        GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestIncludeAll
    )
    pageSize: int
    pageToken: str
    profile: str
    scope: str

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestApiHubApiArray(
    typing.TypedDict, total=False
):
    apis: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestApiHubGatewayArray(
    typing.TypedDict, total=False
):
    gateways: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestIncludeAll(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArray(
    typing.TypedDict, total=False
):
    resources: _list[
        GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArrayResource
    ]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArrayResource(
    typing.TypedDict, total=False
):
    name: str
    type: typing.Literal["RESOURCE_TYPE_UNSPECIFIED", "API_PROXY", "API_HUB_DEPLOYMENT"]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponse(
    typing.TypedDict, total=False
):
    assessmentTime: str
    nextPageToken: str
    securityAssessmentResults: _list[GoogleCloudApigeeV1SecurityAssessmentResult]

@typing.type_check_only
class GoogleCloudApigeeV1BatchUpdateSecurityIncidentsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudApigeeV1UpdateSecurityIncidentRequest]

@typing.type_check_only
class GoogleCloudApigeeV1BatchUpdateSecurityIncidentsResponse(
    typing.TypedDict, total=False
):
    securityIncidents: _list[GoogleCloudApigeeV1SecurityIncident]

@typing.type_check_only
class GoogleCloudApigeeV1CanaryEvaluation(typing.TypedDict, total=False):
    control: str
    createTime: str
    endTime: str
    metricLabels: GoogleCloudApigeeV1CanaryEvaluationMetricLabels
    name: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED"]
    treatment: str
    verdict: typing.Literal["VERDICT_UNSPECIFIED", "NONE", "FAIL", "PASS"]

@typing.type_check_only
class GoogleCloudApigeeV1CanaryEvaluationMetricLabels(typing.TypedDict, total=False):
    env: str
    instance_id: str
    location: str

@typing.type_check_only
class GoogleCloudApigeeV1CertInfo(typing.TypedDict, total=False):
    basicConstraints: str
    expiryDate: str
    isValid: str
    issuer: str
    publicKey: str
    serialNumber: str
    sigAlgName: str
    subject: str
    subjectAlternativeNames: _list[str]
    validFrom: str
    version: int

@typing.type_check_only
class GoogleCloudApigeeV1Certificate(typing.TypedDict, total=False):
    certInfo: _list[GoogleCloudApigeeV1CertInfo]

@typing.type_check_only
class GoogleCloudApigeeV1CommonNameConfig(typing.TypedDict, total=False):
    matchWildCards: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ComputeEnvironmentScoresRequest(typing.TypedDict, total=False):
    filters: _list[GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilter]
    pageSize: int
    pageToken: str
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilter(
    typing.TypedDict, total=False
):
    scorePath: str

@typing.type_check_only
class GoogleCloudApigeeV1ComputeEnvironmentScoresResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    scores: _list[GoogleCloudApigeeV1Score]

@typing.type_check_only
class GoogleCloudApigeeV1ConfigVersion(typing.TypedDict, total=False):
    majorVersion: int
    minorVersion: int

@typing.type_check_only
class GoogleCloudApigeeV1ConnectorsPlatformConfig(typing.TypedDict, total=False):
    enabled: bool
    expiresAt: str

@typing.type_check_only
class GoogleCloudApigeeV1ControlPlaneAccess(typing.TypedDict, total=False):
    analyticsPublisherIdentities: _list[str]
    name: str
    synchronizerIdentities: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1Credential(typing.TypedDict, total=False):
    apiProducts: _list[GoogleCloudApigeeV1ApiProductRef]
    attributes: _list[GoogleCloudApigeeV1Attribute]
    consumerKey: str
    consumerSecret: str
    expiresAt: str
    issuedAt: str
    scopes: _list[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1CreditAppGroupBalanceRequest(typing.TypedDict, total=False):
    transactionAmount: GoogleTypeMoney
    transactionId: str

@typing.type_check_only
class GoogleCloudApigeeV1CreditDeveloperBalanceRequest(typing.TypedDict, total=False):
    transactionAmount: GoogleTypeMoney
    transactionId: str

@typing.type_check_only
class GoogleCloudApigeeV1CustomReport(typing.TypedDict, total=False):
    chartType: str
    comments: _list[str]
    createdAt: str
    dimensions: _list[str]
    displayName: str
    environment: str
    filter: str
    fromTime: str
    lastModifiedAt: str
    lastViewedAt: str
    limit: str
    metrics: _list[GoogleCloudApigeeV1CustomReportMetric]
    name: str
    offset: str
    organization: str
    properties: _list[GoogleCloudApigeeV1ReportProperty]
    sortByCols: _list[str]
    sortOrder: str
    tags: _list[str]
    timeUnit: str
    toTime: str
    topk: str

@typing.type_check_only
class GoogleCloudApigeeV1CustomReportMetric(typing.TypedDict, total=False):
    function: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1DataCollector(typing.TypedDict, total=False):
    createdAt: str
    description: str
    lastModifiedAt: str
    name: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "STRING", "BOOLEAN", "DATETIME"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1DataCollectorConfig(typing.TypedDict, total=False):
    name: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "STRING", "BOOLEAN", "DATETIME"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1Datastore(typing.TypedDict, total=False):
    createTime: str
    datastoreConfig: GoogleCloudApigeeV1DatastoreConfig
    displayName: str
    lastUpdateTime: str
    org: str
    self: str
    targetType: str

@typing.type_check_only
class GoogleCloudApigeeV1DatastoreConfig(typing.TypedDict, total=False):
    bucketName: str
    datasetName: str
    path: str
    projectId: str
    tablePrefix: str

@typing.type_check_only
class GoogleCloudApigeeV1DateRange(typing.TypedDict, total=False):
    end: str
    start: str

@typing.type_check_only
class GoogleCloudApigeeV1DebugMask(typing.TypedDict, total=False):
    faultJSONPaths: _list[str]
    faultXPaths: _list[str]
    name: str
    namespaces: dict[str, typing.Any]
    requestJSONPaths: _list[str]
    requestXPaths: _list[str]
    responseJSONPaths: _list[str]
    responseXPaths: _list[str]
    variables: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1DebugSession(typing.TypedDict, total=False):
    count: int
    createTime: str
    filter: str
    name: str
    timeout: str
    tracesize: int
    validity: int

@typing.type_check_only
class GoogleCloudApigeeV1DebugSessionTransaction(typing.TypedDict, total=False):
    completed: bool
    point: _list[GoogleCloudApigeeV1Point]

@typing.type_check_only
class GoogleCloudApigeeV1DeleteCustomReportResponse(typing.TypedDict, total=False):
    message: str

@typing.type_check_only
class GoogleCloudApigeeV1DeleteResponse(typing.TypedDict, total=False):
    errorCode: str
    gcpResource: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1Deployment(typing.TypedDict, total=False):
    apiProxy: str
    deployStartTime: str
    environment: str
    errors: _list[GoogleRpcStatus]
    instances: _list[GoogleCloudApigeeV1InstanceDeploymentStatus]
    pods: _list[GoogleCloudApigeeV1PodStatus]
    proxyDeploymentType: typing.Literal[
        "PROXY_DEPLOYMENT_TYPE_UNSPECIFIED", "STANDARD", "EXTENSIBLE"
    ]
    revision: str
    routeConflicts: _list[GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict]
    serviceAccount: str
    state: typing.Literal["RUNTIME_STATE_UNSPECIFIED", "READY", "PROGRESSING", "ERROR"]

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReport(typing.TypedDict, total=False):
    routingChanges: _list[GoogleCloudApigeeV1DeploymentChangeReportRoutingChange]
    routingConflicts: _list[GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict]
    validationErrors: GoogleRpcPreconditionFailure

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportRoutingChange(
    typing.TypedDict, total=False
):
    description: str
    environmentGroup: str
    fromDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment
    shouldSequenceRollout: bool
    toDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict(
    typing.TypedDict, total=False
):
    conflictingDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment
    description: str
    environmentGroup: str

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment(
    typing.TypedDict, total=False
):
    apiProxy: str
    basepath: str
    environment: str
    revision: str

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentConfig(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    basePath: str
    deploymentGroups: _list[str]
    endpoints: dict[str, typing.Any]
    location: str
    name: str
    proxyUid: str
    serviceAccount: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentGroupConfig(typing.TypedDict, total=False):
    deploymentGroupType: typing.Literal[
        "DEPLOYMENT_GROUP_TYPE_UNSPECIFIED", "STANDARD", "EXTENSIBLE"
    ]
    name: str
    revisionId: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Developer(typing.TypedDict, total=False):
    accessType: str
    appFamily: str
    apps: _list[str]
    attributes: _list[GoogleCloudApigeeV1Attribute]
    companies: _list[str]
    createdAt: str
    developerId: str
    email: str
    firstName: str
    lastModifiedAt: str
    lastName: str
    organizationName: str
    status: str
    userName: str

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperApp(typing.TypedDict, total=False):
    apiProducts: _list[str]
    appFamily: str
    appId: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    callbackUrl: str
    createdAt: str
    credentials: _list[GoogleCloudApigeeV1Credential]
    developerId: str
    keyExpiresIn: str
    lastModifiedAt: str
    name: str
    scopes: _list[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperAppKey(typing.TypedDict, total=False):
    apiProducts: _list[typing.Any]
    attributes: _list[GoogleCloudApigeeV1Attribute]
    consumerKey: str
    consumerSecret: str
    expiresAt: str
    expiresInSeconds: str
    issuedAt: str
    scopes: _list[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperBalance(typing.TypedDict, total=False):
    wallets: _list[GoogleCloudApigeeV1DeveloperBalanceWallet]

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperBalanceWallet(typing.TypedDict, total=False):
    balance: GoogleTypeMoney
    lastCreditTime: str

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperMonetizationConfig(typing.TypedDict, total=False):
    billingType: typing.Literal["BILLING_TYPE_UNSPECIFIED", "PREPAID", "POSTPAID"]

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperSubscription(typing.TypedDict, total=False):
    apiproduct: str
    createdAt: str
    endTime: str
    lastModifiedAt: str
    name: str
    startTime: str

@typing.type_check_only
class GoogleCloudApigeeV1DimensionMetric(typing.TypedDict, total=False):
    individualNames: _list[str]
    metrics: _list[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1DisableSecurityActionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1DnsZone(typing.TypedDict, total=False):
    createTime: str
    description: str
    domain: str
    name: str
    peeringConfig: GoogleCloudApigeeV1DnsZonePeeringConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1DnsZonePeeringConfig(typing.TypedDict, total=False):
    targetNetworkId: str
    targetProjectId: str

@typing.type_check_only
class GoogleCloudApigeeV1DocumentationFile(typing.TypedDict, total=False):
    contents: str
    displayName: str

@typing.type_check_only
class GoogleCloudApigeeV1EnableSecurityActionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1EndpointAttachment(typing.TypedDict, total=False):
    connectionState: typing.Literal[
        "CONNECTION_STATE_UNSPECIFIED",
        "UNAVAILABLE",
        "PENDING",
        "ACCEPTED",
        "REJECTED",
        "CLOSED",
        "FROZEN",
        "NEEDS_ATTENTION",
        "ACCEPTED_LIMITED_CAPACITY",
    ]
    host: str
    location: str
    name: str
    serviceAttachment: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EndpointChainingRule(typing.TypedDict, total=False):
    deploymentGroup: str
    proxyIds: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1EntityMetadata(typing.TypedDict, total=False):
    createdAt: str
    lastModifiedAt: str
    subType: str

@typing.type_check_only
class GoogleCloudApigeeV1Environment(typing.TypedDict, total=False):
    apiProxyType: typing.Literal[
        "API_PROXY_TYPE_UNSPECIFIED", "PROGRAMMABLE", "CONFIGURABLE"
    ]
    clientIpResolutionConfig: GoogleCloudApigeeV1EnvironmentClientIPResolutionConfig
    createdAt: str
    deploymentType: typing.Literal["DEPLOYMENT_TYPE_UNSPECIFIED", "PROXY", "ARCHIVE"]
    description: str
    displayName: str
    forwardProxyUri: str
    hasAttachedFlowHooks: bool
    lastModifiedAt: str
    name: str
    nodeConfig: GoogleCloudApigeeV1NodeConfig
    properties: GoogleCloudApigeeV1Properties
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]
    type: typing.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "BASE", "INTERMEDIATE", "COMPREHENSIVE"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentClientIPResolutionConfig(
    typing.TypedDict, total=False
):
    headerIndexAlgorithm: (
        GoogleCloudApigeeV1EnvironmentClientIPResolutionConfigHeaderIndexAlgorithm
    )

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentClientIPResolutionConfigHeaderIndexAlgorithm(
    typing.TypedDict, total=False
):
    ipHeaderIndex: int
    ipHeaderName: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfig(typing.TypedDict, total=False):
    addonsConfig: GoogleCloudApigeeV1RuntimeAddonsConfig
    arcConfigLocation: str
    clientIpResolutionConfig: (
        GoogleCloudApigeeV1EnvironmentConfigClientIPResolutionConfig
    )
    createTime: str
    dataCollectors: _list[GoogleCloudApigeeV1DataCollectorConfig]
    debugMask: GoogleCloudApigeeV1DebugMask
    deploymentGroups: _list[GoogleCloudApigeeV1DeploymentGroupConfig]
    deployments: _list[GoogleCloudApigeeV1DeploymentConfig]
    envScopedRevisionId: str
    featureFlags: dict[str, typing.Any]
    flowhooks: _list[GoogleCloudApigeeV1FlowHookConfig]
    forwardProxyUri: str
    gatewayConfigLocation: str
    keystores: _list[GoogleCloudApigeeV1KeystoreConfig]
    name: str
    provider: str
    pubsubTopic: str
    resourceReferences: _list[GoogleCloudApigeeV1ReferenceConfig]
    resources: _list[GoogleCloudApigeeV1ResourceConfig]
    revisionId: str
    sequenceNumber: str
    targets: _list[GoogleCloudApigeeV1TargetServerConfig]
    traceConfig: GoogleCloudApigeeV1RuntimeTraceConfig
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfigClientIPResolutionConfig(
    typing.TypedDict, total=False
):
    headerIndexAlgorithm: (
        GoogleCloudApigeeV1EnvironmentConfigClientIPResolutionConfigHeaderIndexAlgorithm
    )

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfigClientIPResolutionConfigHeaderIndexAlgorithm(
    typing.TypedDict, total=False
):
    ipHeaderIndex: int
    ipHeaderName: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroup(typing.TypedDict, total=False):
    createdAt: str
    hostnames: _list[str]
    lastModifiedAt: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupAttachment(typing.TypedDict, total=False):
    createdAt: str
    environment: str
    environmentGroupId: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupConfig(typing.TypedDict, total=False):
    endpointChainingRules: _list[GoogleCloudApigeeV1EndpointChainingRule]
    hostnames: _list[str]
    location: str
    name: str
    revisionId: str
    routingRules: _list[GoogleCloudApigeeV1RoutingRule]
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1ExpireAppGroupSubscriptionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1Export(typing.TypedDict, total=False):
    created: str
    datastoreName: str
    description: str
    error: str
    executionTime: str
    name: str
    self: str
    state: str
    updated: str

@typing.type_check_only
class GoogleCloudApigeeV1ExportRequest(typing.TypedDict, total=False):
    csvDelimiter: str
    datastoreName: str
    dateRange: GoogleCloudApigeeV1DateRange
    description: str
    name: str
    outputFormat: str

@typing.type_check_only
class GoogleCloudApigeeV1FlowHook(typing.TypedDict, total=False):
    continueOnError: bool
    description: str
    flowHookPoint: str
    sharedFlow: str

@typing.type_check_only
class GoogleCloudApigeeV1FlowHookConfig(typing.TypedDict, total=False):
    continueOnError: bool
    name: str
    sharedFlowName: str

@typing.type_check_only
class GoogleCloudApigeeV1GenerateDownloadUrlRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1GenerateDownloadUrlResponse(typing.TypedDict, total=False):
    downloadUri: str

@typing.type_check_only
class GoogleCloudApigeeV1GenerateUploadUrlRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1GenerateUploadUrlResponse(typing.TypedDict, total=False):
    uploadUri: str

@typing.type_check_only
class GoogleCloudApigeeV1GetAsyncQueryResultUrlResponse(typing.TypedDict, total=False):
    urls: _list[GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfo]

@typing.type_check_only
class GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfo(
    typing.TypedDict, total=False
):
    md5: str
    sizeBytes: str
    uri: str

@typing.type_check_only
class GoogleCloudApigeeV1GetSyncAuthorizationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1GraphQLOperation(typing.TypedDict, total=False):
    operation: str
    operationTypes: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1GraphQLOperationConfig(typing.TypedDict, total=False):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    operations: _list[GoogleCloudApigeeV1GraphQLOperation]
    quota: GoogleCloudApigeeV1Quota

@typing.type_check_only
class GoogleCloudApigeeV1GraphQLOperationGroup(typing.TypedDict, total=False):
    operationConfigType: str
    operationConfigs: _list[GoogleCloudApigeeV1GraphQLOperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1GraphqlDocumentation(typing.TypedDict, total=False):
    endpointUri: str
    schema: GoogleCloudApigeeV1DocumentationFile

@typing.type_check_only
class GoogleCloudApigeeV1GrpcOperationConfig(typing.TypedDict, total=False):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    methods: _list[str]
    quota: GoogleCloudApigeeV1Quota
    service: str

@typing.type_check_only
class GoogleCloudApigeeV1GrpcOperationGroup(typing.TypedDict, total=False):
    operationConfigs: _list[GoogleCloudApigeeV1GrpcOperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1IngressConfig(typing.TypedDict, total=False):
    environmentGroups: _list[GoogleCloudApigeeV1EnvironmentGroupConfig]
    name: str
    revisionCreateTime: str
    revisionId: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Instance(typing.TypedDict, total=False):
    accessLoggingConfig: GoogleCloudApigeeV1AccessLoggingConfig
    consumerAcceptList: _list[str]
    createdAt: str
    description: str
    diskEncryptionKeyName: str
    displayName: str
    host: str
    ipRange: str
    isVersionLocked: bool
    lastModifiedAt: str
    location: str
    maintenanceUpdatePolicy: GoogleCloudApigeeV1MaintenanceUpdatePolicy
    name: str
    peeringCidrRange: typing.Literal[
        "CIDR_RANGE_UNSPECIFIED",
        "SLASH_16",
        "SLASH_17",
        "SLASH_18",
        "SLASH_19",
        "SLASH_20",
        "SLASH_22",
        "SLASH_23",
    ]
    port: str
    runtimeVersion: str
    scheduledMaintenance: GoogleCloudApigeeV1ScheduledMaintenance
    serviceAttachment: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1InstanceAttachment(typing.TypedDict, total=False):
    createdAt: str
    environment: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1InstanceDeploymentStatus(typing.TypedDict, total=False):
    deployedRevisions: _list[
        GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision
    ]
    deployedRoutes: _list[GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute]
    instance: str

@typing.type_check_only
class GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision(
    typing.TypedDict, total=False
):
    percentage: int
    revision: str

@typing.type_check_only
class GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute(
    typing.TypedDict, total=False
):
    basepath: str
    envgroup: str
    environment: str
    percentage: int

@typing.type_check_only
class GoogleCloudApigeeV1IntegrationConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1KeyAliasReference(typing.TypedDict, total=False):
    aliasId: str
    reference: str

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueEntry(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueMap(typing.TypedDict, total=False):
    encrypted: bool
    maskedValues: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1Keystore(typing.TypedDict, total=False):
    aliases: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1KeystoreConfig(typing.TypedDict, total=False):
    aliases: _list[GoogleCloudApigeeV1AliasRevisionConfig]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiCategoriesResponse(typing.TypedDict, total=False):
    data: _list[GoogleCloudApigeeV1ApiCategory]
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiDebugSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[GoogleCloudApigeeV1ApiDebugSession]

@typing.type_check_only
class GoogleCloudApigeeV1ListApiDocsResponse(typing.TypedDict, total=False):
    data: _list[GoogleCloudApigeeV1ApiDoc]
    errorCode: str
    message: str
    nextPageToken: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProductsResponse(typing.TypedDict, total=False):
    apiProduct: _list[GoogleCloudApigeeV1ApiProduct]

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProxiesResponse(typing.TypedDict, total=False):
    proxies: _list[GoogleCloudApigeeV1ApiProxy]

@typing.type_check_only
class GoogleCloudApigeeV1ListApimServiceExtensionsResponse(
    typing.TypedDict, total=False
):
    apimServiceExtensions: _list[GoogleCloudApigeeV1ApimServiceExtension]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListAppGroupAppsResponse(typing.TypedDict, total=False):
    appGroupApps: _list[GoogleCloudApigeeV1AppGroupApp]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListAppGroupSubscriptionsResponse(
    typing.TypedDict, total=False
):
    appGroupSubscriptions: _list[GoogleCloudApigeeV1AppGroupSubscription]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListAppGroupsResponse(typing.TypedDict, total=False):
    appGroups: _list[GoogleCloudApigeeV1AppGroup]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleCloudApigeeV1ListAppsResponse(typing.TypedDict, total=False):
    app: _list[GoogleCloudApigeeV1App]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleCloudApigeeV1ListArchiveDeploymentsResponse(typing.TypedDict, total=False):
    archiveDeployments: _list[GoogleCloudApigeeV1ArchiveDeployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListAsyncQueriesResponse(typing.TypedDict, total=False):
    queries: _list[GoogleCloudApigeeV1AsyncQuery]

@typing.type_check_only
class GoogleCloudApigeeV1ListCustomReportsResponse(typing.TypedDict, total=False):
    qualifier: _list[GoogleCloudApigeeV1CustomReport]

@typing.type_check_only
class GoogleCloudApigeeV1ListDataCollectorsResponse(typing.TypedDict, total=False):
    dataCollectors: _list[GoogleCloudApigeeV1DataCollector]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListDatastoresResponse(typing.TypedDict, total=False):
    datastores: _list[GoogleCloudApigeeV1Datastore]

@typing.type_check_only
class GoogleCloudApigeeV1ListDebugSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[GoogleCloudApigeeV1Session]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeploymentsResponse(typing.TypedDict, total=False):
    deployments: _list[GoogleCloudApigeeV1Deployment]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperAppsResponse(typing.TypedDict, total=False):
    app: _list[GoogleCloudApigeeV1DeveloperApp]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperSubscriptionsResponse(
    typing.TypedDict, total=False
):
    developerSubscriptions: _list[GoogleCloudApigeeV1DeveloperSubscription]
    nextStartKey: str

@typing.type_check_only
class GoogleCloudApigeeV1ListDnsZonesResponse(typing.TypedDict, total=False):
    dnsZones: _list[GoogleCloudApigeeV1DnsZone]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEndpointAttachmentsResponse(typing.TypedDict, total=False):
    endpointAttachments: _list[GoogleCloudApigeeV1EndpointAttachment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse(
    typing.TypedDict, total=False
):
    environmentGroupAttachments: _list[GoogleCloudApigeeV1EnvironmentGroupAttachment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupsResponse(typing.TypedDict, total=False):
    environmentGroups: _list[GoogleCloudApigeeV1EnvironmentGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentResourcesResponse(
    typing.TypedDict, total=False
):
    resourceFile: _list[GoogleCloudApigeeV1ResourceFile]

@typing.type_check_only
class GoogleCloudApigeeV1ListExportsResponse(typing.TypedDict, total=False):
    exports: _list[GoogleCloudApigeeV1Export]

@typing.type_check_only
class GoogleCloudApigeeV1ListHybridIssuersResponse(typing.TypedDict, total=False):
    issuers: _list[GoogleCloudApigeeV1ServiceIssuersMapping]

@typing.type_check_only
class GoogleCloudApigeeV1ListInstanceAttachmentsResponse(typing.TypedDict, total=False):
    attachments: _list[GoogleCloudApigeeV1InstanceAttachment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[GoogleCloudApigeeV1Instance]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListKeyValueEntriesResponse(typing.TypedDict, total=False):
    keyValueEntries: _list[GoogleCloudApigeeV1KeyValueEntry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListNatAddressesResponse(typing.TypedDict, total=False):
    natAddresses: _list[GoogleCloudApigeeV1NatAddress]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListOfDevelopersResponse(typing.TypedDict, total=False):
    developer: _list[GoogleCloudApigeeV1Developer]

@typing.type_check_only
class GoogleCloudApigeeV1ListOrganizationsResponse(typing.TypedDict, total=False):
    organizations: _list[GoogleCloudApigeeV1OrganizationProjectMapping]

@typing.type_check_only
class GoogleCloudApigeeV1ListRatePlansResponse(typing.TypedDict, total=False):
    nextStartKey: str
    ratePlans: _list[GoogleCloudApigeeV1RatePlan]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityActionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    securityActions: _list[GoogleCloudApigeeV1SecurityAction]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityFeedbackResponse(typing.TypedDict, total=False):
    nextPageToken: str
    securityFeedback: _list[GoogleCloudApigeeV1SecurityFeedback]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityIncidentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    securityIncidents: _list[GoogleCloudApigeeV1SecurityIncident]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityMonitoringConditionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    securityMonitoringConditions: _list[GoogleCloudApigeeV1SecurityMonitoringCondition]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfileRevisionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    securityProfiles: _list[GoogleCloudApigeeV1SecurityProfile]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfilesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    securityProfiles: _list[GoogleCloudApigeeV1SecurityProfile]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfilesV2Response(typing.TypedDict, total=False):
    nextPageToken: str
    securityProfilesV2: _list[GoogleCloudApigeeV1SecurityProfileV2]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    securityReports: _list[GoogleCloudApigeeV1SecurityReport]

@typing.type_check_only
class GoogleCloudApigeeV1ListSharedFlowsResponse(typing.TypedDict, total=False):
    sharedFlows: _list[GoogleCloudApigeeV1SharedFlow]

@typing.type_check_only
class GoogleCloudApigeeV1ListSpacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    spaces: _list[GoogleCloudApigeeV1Space]

@typing.type_check_only
class GoogleCloudApigeeV1ListTraceConfigOverridesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    traceConfigOverrides: _list[GoogleCloudApigeeV1TraceConfigOverride]

@typing.type_check_only
class GoogleCloudApigeeV1LlmOperation(typing.TypedDict, total=False):
    methods: _list[str]
    model: str
    resource: str

@typing.type_check_only
class GoogleCloudApigeeV1LlmOperationConfig(typing.TypedDict, total=False):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    llmOperations: _list[GoogleCloudApigeeV1LlmOperation]
    llmTokenQuota: GoogleCloudApigeeV1LlmTokenQuota

@typing.type_check_only
class GoogleCloudApigeeV1LlmOperationGroup(typing.TypedDict, total=False):
    operationConfigs: _list[GoogleCloudApigeeV1LlmOperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1LlmTokenQuota(typing.TypedDict, total=False):
    interval: str
    limit: str
    timeUnit: str

@typing.type_check_only
class GoogleCloudApigeeV1MaintenanceUpdatePolicy(typing.TypedDict, total=False):
    maintenanceChannel: typing.Literal[
        "MAINTENANCE_CHANNEL_UNSPECIFIED", "WEEK1", "WEEK2"
    ]
    maintenanceWindows: _list[
        GoogleCloudApigeeV1MaintenanceUpdatePolicyMaintenanceWindow
    ]

@typing.type_check_only
class GoogleCloudApigeeV1MaintenanceUpdatePolicyMaintenanceWindow(
    typing.TypedDict, total=False
):
    day: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    startTime: GoogleTypeTimeOfDay

@typing.type_check_only
class GoogleCloudApigeeV1Metadata(typing.TypedDict, total=False):
    errors: _list[str]
    notices: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1Metric(typing.TypedDict, total=False):
    name: str
    values: _list[typing.Any]

@typing.type_check_only
class GoogleCloudApigeeV1MetricAggregation(typing.TypedDict, total=False):
    aggregation: typing.Literal[
        "AGGREGATION_FUNCTION_UNSPECIFIED", "AVG", "SUM", "MIN", "MAX", "COUNT_DISTINCT"
    ]
    name: str
    order: typing.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class GoogleCloudApigeeV1MonetizationConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1MoveApiProductRequest(typing.TypedDict, total=False):
    space: str

@typing.type_check_only
class GoogleCloudApigeeV1MoveApiProxyRequest(typing.TypedDict, total=False):
    space: str

@typing.type_check_only
class GoogleCloudApigeeV1MoveSharedFlowRequest(typing.TypedDict, total=False):
    space: str

@typing.type_check_only
class GoogleCloudApigeeV1NatAddress(typing.TypedDict, total=False):
    ipAddress: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RESERVED", "ACTIVE", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1NodeConfig(typing.TypedDict, total=False):
    currentAggregateNodeCount: str
    maxNodeCount: str
    minNodeCount: str

@typing.type_check_only
class GoogleCloudApigeeV1OASDocumentation(typing.TypedDict, total=False):
    format: typing.Literal["FORMAT_UNSPECIFIED", "YAML", "JSON"]
    spec: GoogleCloudApigeeV1DocumentationFile

@typing.type_check_only
class GoogleCloudApigeeV1Operation(typing.TypedDict, total=False):
    methods: _list[str]
    resource: str

@typing.type_check_only
class GoogleCloudApigeeV1OperationConfig(typing.TypedDict, total=False):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    operations: _list[GoogleCloudApigeeV1Operation]
    quota: GoogleCloudApigeeV1Quota

@typing.type_check_only
class GoogleCloudApigeeV1OperationGroup(typing.TypedDict, total=False):
    operationConfigType: str
    operationConfigs: _list[GoogleCloudApigeeV1OperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1OperationMetadata(typing.TypedDict, total=False):
    operationType: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "INSERT", "DELETE", "UPDATE"
    ]
    progress: GoogleCloudApigeeV1OperationMetadataProgress
    state: typing.Literal["STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "FINISHED"]
    targetResourceName: str
    warnings: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1OperationMetadataProgress(typing.TypedDict, total=False):
    description: str
    details: dict[str, typing.Any]
    percentDone: int
    state: typing.Literal["STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "FINISHED"]

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStats(typing.TypedDict, total=False):
    Response: GoogleCloudApigeeV1OptimizedStatsResponse

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsNode(typing.TypedDict, total=False):
    data: _list[typing.Any]

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsResponse(typing.TypedDict, total=False):
    TimeUnit: _list[str]
    metaData: GoogleCloudApigeeV1Metadata
    resultTruncated: bool
    stats: GoogleCloudApigeeV1OptimizedStatsNode

@typing.type_check_only
class GoogleCloudApigeeV1Organization(typing.TypedDict, total=False):
    addonsConfig: GoogleCloudApigeeV1AddonsConfig
    analyticsRegion: str
    apiConsumerDataEncryptionKeyName: str
    apiConsumerDataLocation: str
    apigeeProjectId: str
    attributes: _list[str]
    authorizedNetwork: str
    billingType: typing.Literal[
        "BILLING_TYPE_UNSPECIFIED", "SUBSCRIPTION", "EVALUATION", "PAYG"
    ]
    caCertificate: str
    caCertificates: _list[str]
    controlPlaneEncryptionKeyName: str
    createdAt: str
    customerName: str
    description: str
    disableVpcPeering: bool
    displayName: str
    environments: _list[str]
    expiresAt: str
    lastModifiedAt: str
    name: str
    networkEgressRestricted: bool
    portalDisabled: bool
    projectId: str
    properties: GoogleCloudApigeeV1Properties
    runtimeDatabaseEncryptionKeyName: str
    runtimeType: typing.Literal["RUNTIME_TYPE_UNSPECIFIED", "CLOUD", "HYBRID"]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]
    subscriptionPlan: typing.Literal[
        "SUBSCRIPTION_PLAN_UNSPECIFIED", "SUBSCRIPTION_2021", "SUBSCRIPTION_2024"
    ]
    subscriptionType: typing.Literal["SUBSCRIPTION_TYPE_UNSPECIFIED", "PAID", "TRIAL"]
    type: typing.Literal["TYPE_UNSPECIFIED", "TYPE_TRIAL", "TYPE_PAID", "TYPE_INTERNAL"]

@typing.type_check_only
class GoogleCloudApigeeV1OrganizationProjectMapping(typing.TypedDict, total=False):
    location: str
    organization: str
    projectId: str
    projectIds: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1PayloadOperation(typing.TypedDict, total=False):
    operation: str

@typing.type_check_only
class GoogleCloudApigeeV1PayloadOperationConfig(typing.TypedDict, total=False):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    operations: _list[GoogleCloudApigeeV1PayloadOperation]
    quota: GoogleCloudApigeeV1Quota

@typing.type_check_only
class GoogleCloudApigeeV1PayloadOperationGroup(typing.TypedDict, total=False):
    operationConfigs: _list[GoogleCloudApigeeV1PayloadOperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1PodStatus(typing.TypedDict, total=False):
    appVersion: str
    deploymentStatus: str
    deploymentStatusTime: str
    deploymentTime: str
    podName: str
    podStatus: str
    podStatusTime: str
    statusCode: str
    statusCodeDetails: str

@typing.type_check_only
class GoogleCloudApigeeV1Point(typing.TypedDict, total=False):
    id: str
    results: _list[GoogleCloudApigeeV1Result]

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfig(typing.TypedDict, total=False):
    categories: _list[GoogleCloudApigeeV1ProfileConfigCategory]

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigAbuse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigAuthorization(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigCORS(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigCategory(typing.TypedDict, total=False):
    abuse: GoogleCloudApigeeV1ProfileConfigAbuse
    authorization: GoogleCloudApigeeV1ProfileConfigAuthorization
    cors: GoogleCloudApigeeV1ProfileConfigCORS
    mediation: GoogleCloudApigeeV1ProfileConfigMediation
    mtls: GoogleCloudApigeeV1ProfileConfigMTLS
    threat: GoogleCloudApigeeV1ProfileConfigThreat

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigMTLS(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigMediation(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigThreat(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1Properties(typing.TypedDict, total=False):
    property: _list[GoogleCloudApigeeV1Property]

@typing.type_check_only
class GoogleCloudApigeeV1Property(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1ProvisionOrganizationRequest(typing.TypedDict, total=False):
    analyticsRegion: str
    authorizedNetwork: str
    disableVpcPeering: bool
    runtimeLocation: str

@typing.type_check_only
class GoogleCloudApigeeV1Query(typing.TypedDict, total=False):
    csvDelimiter: str
    dimensions: _list[str]
    envgroupHostname: str
    filter: str
    groupByTimeUnit: str
    limit: int
    metrics: _list[GoogleCloudApigeeV1QueryMetric]
    name: str
    outputFormat: str
    reportDefinitionId: str
    timeRange: typing.Any

@typing.type_check_only
class GoogleCloudApigeeV1QueryMetadata(typing.TypedDict, total=False):
    dimensions: _list[str]
    endTimestamp: str
    metrics: _list[str]
    outputFormat: str
    startTimestamp: str
    timeUnit: str

@typing.type_check_only
class GoogleCloudApigeeV1QueryMetric(typing.TypedDict, total=False):
    alias: str
    function: str
    name: str
    operator: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1QueryTabularStatsRequest(typing.TypedDict, total=False):
    dimensions: _list[str]
    filter: str
    metrics: _list[GoogleCloudApigeeV1MetricAggregation]
    pageSize: int
    pageToken: str
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudApigeeV1QueryTabularStatsResponse(typing.TypedDict, total=False):
    columns: _list[str]
    nextPageToken: str
    values: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudApigeeV1QueryTimeSeriesStatsRequest(typing.TypedDict, total=False):
    dimensions: _list[str]
    filter: str
    metrics: _list[GoogleCloudApigeeV1MetricAggregation]
    pageSize: int
    pageToken: str
    timeRange: GoogleTypeInterval
    timestampOrder: typing.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]
    windowSize: typing.Literal[
        "WINDOW_SIZE_UNSPECIFIED", "MINUTE", "HOUR", "DAY", "MONTH"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1QueryTimeSeriesStatsResponse(typing.TypedDict, total=False):
    columns: _list[str]
    nextPageToken: str
    values: _list[GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequence]

@typing.type_check_only
class GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequence(
    typing.TypedDict, total=False
):
    dimensions: dict[str, typing.Any]
    points: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudApigeeV1Quota(typing.TypedDict, total=False):
    interval: str
    limit: str
    timeUnit: str

@typing.type_check_only
class GoogleCloudApigeeV1RatePlan(typing.TypedDict, total=False):
    apiproduct: str
    billingPeriod: typing.Literal["BILLING_PERIOD_UNSPECIFIED", "WEEKLY", "MONTHLY"]
    consumptionPricingRates: _list[GoogleCloudApigeeV1RateRange]
    consumptionPricingType: typing.Literal[
        "CONSUMPTION_PRICING_TYPE_UNSPECIFIED",
        "FIXED_PER_UNIT",
        "BANDED",
        "TIERED",
        "STAIRSTEP",
    ]
    createdAt: str
    currencyCode: str
    description: str
    displayName: str
    endTime: str
    fixedFeeFrequency: int
    fixedRecurringFee: GoogleTypeMoney
    lastModifiedAt: str
    name: str
    paymentFundingModel: typing.Literal[
        "PAYMENT_FUNDING_MODEL_UNSPECIFIED", "PREPAID", "POSTPAID"
    ]
    revenueShareRates: _list[GoogleCloudApigeeV1RevenueShareRange]
    revenueShareType: typing.Literal[
        "REVENUE_SHARE_TYPE_UNSPECIFIED", "FIXED", "VOLUME_BANDED"
    ]
    setupFee: GoogleTypeMoney
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "DRAFT", "PUBLISHED"]

@typing.type_check_only
class GoogleCloudApigeeV1RateRange(typing.TypedDict, total=False):
    end: str
    fee: GoogleTypeMoney
    start: str

@typing.type_check_only
class GoogleCloudApigeeV1Reference(typing.TypedDict, total=False):
    description: str
    name: str
    refers: str
    resourceType: str

@typing.type_check_only
class GoogleCloudApigeeV1ReferenceConfig(typing.TypedDict, total=False):
    name: str
    resourceName: str

@typing.type_check_only
class GoogleCloudApigeeV1ReportInstanceStatusRequest(typing.TypedDict, total=False):
    instanceUid: str
    reportTime: str
    resources: _list[GoogleCloudApigeeV1ResourceStatus]

@typing.type_check_only
class GoogleCloudApigeeV1ReportInstanceStatusResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ReportProperty(typing.TypedDict, total=False):
    property: str
    value: _list[GoogleCloudApigeeV1Attribute]

@typing.type_check_only
class GoogleCloudApigeeV1ResourceConfig(typing.TypedDict, total=False):
    location: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ResourceFile(typing.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1ResourceFiles(typing.TypedDict, total=False):
    resourceFile: _list[GoogleCloudApigeeV1ResourceFile]

@typing.type_check_only
class GoogleCloudApigeeV1ResourceStatus(typing.TypedDict, total=False):
    resource: str
    revisions: _list[GoogleCloudApigeeV1RevisionStatus]
    totalReplicas: int
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Result(typing.TypedDict, total=False):
    ActionResult: str
    accessList: _list[GoogleCloudApigeeV1Access]
    content: str
    headers: _list[GoogleCloudApigeeV1Property]
    properties: GoogleCloudApigeeV1Properties
    reasonPhrase: str
    statusCode: str
    timestamp: str
    uRI: str
    verb: str

@typing.type_check_only
class GoogleCloudApigeeV1RevenueShareRange(typing.TypedDict, total=False):
    end: str
    sharePercentage: float
    start: str

@typing.type_check_only
class GoogleCloudApigeeV1RevisionStatus(typing.TypedDict, total=False):
    errors: _list[GoogleCloudApigeeV1UpdateError]
    jsonSpec: str
    replicas: int
    revisionId: str

@typing.type_check_only
class GoogleCloudApigeeV1RoutingRule(typing.TypedDict, total=False):
    basepath: str
    deploymentGroup: str
    envGroupRevision: str
    environment: str
    otherTargets: _list[str]
    receiver: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeAddonsConfig(typing.TypedDict, total=False):
    analyticsConfig: GoogleCloudApigeeV1RuntimeAnalyticsConfig
    apiSecurityConfig: GoogleCloudApigeeV1RuntimeApiSecurityConfig
    name: str
    revisionId: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeAnalyticsConfig(typing.TypedDict, total=False):
    billingPipelineEnabled: bool
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeApiSecurityConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeConfig(typing.TypedDict, total=False):
    analyticsBucket: str
    name: str
    tenantProjectId: str
    traceBucket: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeTraceConfig(typing.TypedDict, total=False):
    endpoint: str
    exporter: typing.Literal[
        "EXPORTER_UNSPECIFIED",
        "JAEGER",
        "CLOUD_TRACE",
        "OPEN_TELEMETRY_COLLECTOR",
        "OPEN_TELEMETRY_CLOUD_TRACE",
    ]
    name: str
    openTelemetryProtocolEnabled: bool
    overrides: _list[GoogleCloudApigeeV1RuntimeTraceConfigOverride]
    revisionCreateTime: str
    revisionId: str
    samplingConfig: GoogleCloudApigeeV1RuntimeTraceSamplingConfig
    spanSemantics: typing.Literal["SPAN_SEMANTICS_UNSPECIFIED", "LEGACY", "OTEL"]
    traceProtocol: typing.Literal["TRACE_PROTOCOL_UNSPECIFIED", "OPEN_CENSUS", "OTLP"]

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeTraceConfigOverride(typing.TypedDict, total=False):
    apiProxy: str
    name: str
    openTelemetryProtocolEnabled: bool
    revisionCreateTime: str
    revisionId: str
    samplingConfig: GoogleCloudApigeeV1RuntimeTraceSamplingConfig
    spanSemantics: typing.Literal["SPAN_SEMANTICS_UNSPECIFIED", "LEGACY", "OTEL"]
    traceProtocol: typing.Literal["TRACE_PROTOCOL_UNSPECIFIED", "OPEN_CENSUS", "OTLP"]
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeTraceSamplingConfig(typing.TypedDict, total=False):
    sampler: typing.Literal["SAMPLER_UNSPECIFIED", "OFF", "PROBABILITY"]
    samplingRate: float

@typing.type_check_only
class GoogleCloudApigeeV1ScheduledMaintenance(typing.TypedDict, total=False):
    startTime: str

@typing.type_check_only
class GoogleCloudApigeeV1Schema(typing.TypedDict, total=False):
    dimensions: _list[GoogleCloudApigeeV1SchemaSchemaElement]
    meta: _list[str]
    metrics: _list[GoogleCloudApigeeV1SchemaSchemaElement]

@typing.type_check_only
class GoogleCloudApigeeV1SchemaSchemaElement(typing.TypedDict, total=False):
    name: str
    properties: GoogleCloudApigeeV1SchemaSchemaProperty

@typing.type_check_only
class GoogleCloudApigeeV1SchemaSchemaProperty(typing.TypedDict, total=False):
    createTime: str
    custom: str
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1Score(typing.TypedDict, total=False):
    component: GoogleCloudApigeeV1ScoreComponent
    subcomponents: _list[GoogleCloudApigeeV1ScoreComponent]
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponent(typing.TypedDict, total=False):
    calculateTime: str
    dataCaptureTime: str
    drilldownPaths: _list[str]
    recommendations: _list[GoogleCloudApigeeV1ScoreComponentRecommendation]
    score: int
    scorePath: str

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponentRecommendation(typing.TypedDict, total=False):
    actions: _list[GoogleCloudApigeeV1ScoreComponentRecommendationAction]
    description: str
    impact: int
    title: str

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponentRecommendationAction(
    typing.TypedDict, total=False
):
    actionContext: GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContext
    description: str

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContext(
    typing.TypedDict, total=False
):
    documentationLink: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAction(typing.TypedDict, total=False):
    allow: GoogleCloudApigeeV1SecurityActionAllow
    apiProxies: _list[str]
    conditionConfig: GoogleCloudApigeeV1SecurityActionConditionConfig
    createTime: str
    deny: GoogleCloudApigeeV1SecurityActionDeny
    description: str
    expireTime: str
    flag: GoogleCloudApigeeV1SecurityActionFlag
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    ttl: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionAllow(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionConditionConfig(typing.TypedDict, total=False):
    accessTokens: _list[str]
    apiKeys: _list[str]
    apiProducts: _list[str]
    asns: _list[str]
    botReasons: _list[str]
    developerApps: _list[str]
    developers: _list[str]
    httpMethods: _list[str]
    ipAddressRanges: _list[str]
    regionCodes: _list[str]
    userAgents: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionDeny(typing.TypedDict, total=False):
    responseCode: int

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionFlag(typing.TypedDict, total=False):
    headers: _list[GoogleCloudApigeeV1SecurityActionHttpHeader]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionHttpHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionsConfig(typing.TypedDict, total=False):
    enabled: bool
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResult(typing.TypedDict, total=False):
    createTime: str
    error: GoogleRpcStatus
    resource: GoogleCloudApigeeV1SecurityAssessmentResultResource
    scoringResult: GoogleCloudApigeeV1SecurityAssessmentResultScoringResult

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultResource(
    typing.TypedDict, total=False
):
    apiHubDeploymentDetails: (
        GoogleCloudApigeeV1SecurityAssessmentResultResourceApiHubDeploymentDetails
    )
    apiHubGatewayType: typing.Literal[
        "API_HUB_GATEWAY_TYPE_UNSPECIFIED",
        "APIGEE_X",
        "APIGEE_HYBRID",
        "APIGEE_EDGE",
        "APIGEE_OPDK",
    ]
    name: str
    resourceRevisionId: str
    type: typing.Literal["RESOURCE_TYPE_UNSPECIFIED", "API_PROXY", "API_HUB_DEPLOYMENT"]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultResourceApiHubDeploymentDetails(
    typing.TypedDict, total=False
):
    displayName: str
    gateway: str
    gatewayType: typing.Literal[
        "API_HUB_GATEWAY_TYPE_UNSPECIFIED",
        "APIGEE_X",
        "APIGEE_HYBRID",
        "APIGEE_EDGE",
        "APIGEE_OPDK",
    ]
    resourceUri: str
    sourceProject: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResult(
    typing.TypedDict, total=False
):
    assessmentRecommendations: dict[str, typing.Any]
    dataUpdateTime: str
    failedAssessmentPerWeight: dict[str, typing.Any]
    score: int
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "MINIMAL"]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendation(
    typing.TypedDict, total=False
):
    displayName: str
    recommendations: _list[
        GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendation
    ]
    scoreImpact: int
    verdict: typing.Literal["VERDICT_UNSPECIFIED", "PASS", "FAIL", "NOT_APPLICABLE"]
    weight: typing.Literal["WEIGHT_UNSPECIFIED", "MINOR", "MODERATE", "MAJOR"]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendation(
    typing.TypedDict, total=False
):
    description: str
    link: GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendationLink

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendationLink(
    typing.TypedDict, total=False
):
    text: str
    uri: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityFeedback(typing.TypedDict, total=False):
    comment: str
    createTime: str
    displayName: str
    feedbackContexts: _list[GoogleCloudApigeeV1SecurityFeedbackFeedbackContext]
    feedbackType: typing.Literal["FEEDBACK_TYPE_UNSPECIFIED", "EXCLUDED_DETECTION"]
    name: str
    reason: typing.Literal[
        "REASON_UNSPECIFIED",
        "INTERNAL_SYSTEM",
        "NON_RISK_CLIENT",
        "NAT",
        "PENETRATION_TEST",
        "OTHER",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityFeedbackFeedbackContext(typing.TypedDict, total=False):
    attribute: typing.Literal[
        "ATTRIBUTE_UNSPECIFIED", "ATTRIBUTE_ENVIRONMENTS", "ATTRIBUTE_IP_ADDRESS_RANGES"
    ]
    values: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityIncident(typing.TypedDict, total=False):
    detectionTypes: _list[str]
    displayName: str
    firstDetectedTime: str
    lastDetectedTime: str
    lastObservabilityChangeTime: str
    name: str
    observability: typing.Literal["OBSERVABILITY_UNSPECIFIED", "ACTIVE", "ARCHIVED"]
    riskLevel: typing.Literal["RISK_LEVEL_UNSPECIFIED", "LOW", "MODERATE", "SEVERE"]
    trafficCount: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityMonitoringCondition(typing.TypedDict, total=False):
    apiHubGateway: str
    createTime: str
    include: (
        GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArray
    )
    includeAllResources: (
        GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestIncludeAll
    )
    name: str
    profile: str
    riskAssessmentType: typing.Literal[
        "RISK_ASSESSMENT_TYPE_UNSPECIFIED", "APIGEE", "API_HUB"
    ]
    scope: str
    totalDeployedResources: int
    totalMonitoredResources: int
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfile(typing.TypedDict, total=False):
    description: str
    displayName: str
    environments: _list[GoogleCloudApigeeV1SecurityProfileEnvironment]
    maxScore: int
    minScore: int
    name: str
    profileConfig: GoogleCloudApigeeV1ProfileConfig
    revisionCreateTime: str
    revisionId: str
    revisionPublishTime: str
    revisionUpdateTime: str
    scoringConfigs: _list[GoogleCloudApigeeV1SecurityProfileScoringConfig]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileEnvironment(typing.TypedDict, total=False):
    attachTime: str
    environment: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileEnvironmentAssociation(
    typing.TypedDict, total=False
):
    attachTime: str
    name: str
    securityProfileRevisionId: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileScoringConfig(typing.TypedDict, total=False):
    description: str
    scorePath: str
    title: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileV2(typing.TypedDict, total=False):
    createTime: str
    description: str
    googleDefined: bool
    name: str
    profileAssessmentConfigs: dict[str, typing.Any]
    riskAssessmentType: typing.Literal[
        "RISK_ASSESSMENT_TYPE_UNSPECIFIED", "APIGEE", "API_HUB"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileV2ProfileAssessmentConfig(
    typing.TypedDict, total=False
):
    include: GoogleCloudApigeeV1SecurityProfileV2ProfileAssessmentConfigApiHubGatewayTypeArray
    weight: typing.Literal["WEIGHT_UNSPECIFIED", "MINOR", "MODERATE", "MAJOR"]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileV2ProfileAssessmentConfigApiHubGatewayTypeArray(
    typing.TypedDict, total=False
):
    gatewayTypes: _list[
        typing.Literal[
            "API_HUB_GATEWAY_TYPE_UNSPECIFIED",
            "APIGEE_X",
            "APIGEE_HYBRID",
            "APIGEE_EDGE",
            "APIGEE_OPDK",
        ]
    ]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReport(typing.TypedDict, total=False):
    created: str
    displayName: str
    envgroupHostname: str
    error: str
    executionTime: str
    queryParams: GoogleCloudApigeeV1SecurityReportMetadata
    reportDefinitionId: str
    result: GoogleCloudApigeeV1SecurityReportResultMetadata
    resultFileSize: str
    resultRows: str
    self: str
    state: str
    updated: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportMetadata(typing.TypedDict, total=False):
    dimensions: _list[str]
    endTimestamp: str
    metrics: _list[str]
    mimeType: str
    startTimestamp: str
    timeUnit: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportQuery(typing.TypedDict, total=False):
    csvDelimiter: str
    dimensions: _list[str]
    displayName: str
    envgroupHostname: str
    filter: str
    groupByTimeUnit: str
    limit: int
    metrics: _list[GoogleCloudApigeeV1SecurityReportQueryMetric]
    mimeType: str
    reportDefinitionId: str
    timeRange: typing.Any

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportQueryMetric(typing.TypedDict, total=False):
    aggregationFunction: str
    alias: str
    name: str
    operator: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportResultMetadata(typing.TypedDict, total=False):
    expires: str
    self: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportResultView(typing.TypedDict, total=False):
    code: int
    error: str
    metadata: GoogleCloudApigeeV1SecurityReportMetadata
    rows: _list[typing.Any]
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1SecuritySettings(typing.TypedDict, total=False):
    mlRetrainingFeedbackEnabled: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ServiceIssuersMapping(typing.TypedDict, total=False):
    emailIds: _list[str]
    service: str

@typing.type_check_only
class GoogleCloudApigeeV1Session(typing.TypedDict, total=False):
    id: str
    timestampMs: str

@typing.type_check_only
class GoogleCloudApigeeV1SetAddonEnablementRequest(typing.TypedDict, total=False):
    analyticsEnabled: bool
    apiSecurityEnabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1SetAddonsRequest(typing.TypedDict, total=False):
    addonsConfig: GoogleCloudApigeeV1AddonsConfig

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlow(typing.TypedDict, total=False):
    latestRevisionId: str
    metaData: GoogleCloudApigeeV1EntityMetadata
    name: str
    revision: _list[str]
    space: str

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlowRevision(typing.TypedDict, total=False):
    configurationVersion: GoogleCloudApigeeV1ConfigVersion
    contextInfo: str
    createdAt: str
    description: str
    displayName: str
    entityMetaDataAsProperties: dict[str, typing.Any]
    lastModifiedAt: str
    name: str
    policies: _list[str]
    resourceFiles: GoogleCloudApigeeV1ResourceFiles
    resources: _list[str]
    revision: str
    sharedFlows: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1Space(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1Stats(typing.TypedDict, total=False):
    environments: _list[GoogleCloudApigeeV1StatsEnvironmentStats]
    hosts: _list[GoogleCloudApigeeV1StatsHostStats]
    metaData: GoogleCloudApigeeV1Metadata

@typing.type_check_only
class GoogleCloudApigeeV1StatsEnvironmentStats(typing.TypedDict, total=False):
    dimensions: _list[GoogleCloudApigeeV1DimensionMetric]
    metrics: _list[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1StatsHostStats(typing.TypedDict, total=False):
    dimensions: _list[GoogleCloudApigeeV1DimensionMetric]
    metrics: _list[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1Subscription(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1SyncAuthorization(typing.TypedDict, total=False):
    etag: str
    identities: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1TargetServer(typing.TypedDict, total=False):
    description: str
    host: str
    isEnabled: bool
    name: str
    port: int
    protocol: typing.Literal[
        "PROTOCOL_UNSPECIFIED",
        "HTTP",
        "HTTP2",
        "GRPC_TARGET",
        "GRPC",
        "EXTERNAL_CALLOUT",
    ]
    sSLInfo: GoogleCloudApigeeV1TlsInfo

@typing.type_check_only
class GoogleCloudApigeeV1TargetServerConfig(typing.TypedDict, total=False):
    enabled: bool
    host: str
    name: str
    port: int
    protocol: typing.Literal[
        "PROTOCOL_UNSPECIFIED",
        "HTTP",
        "HTTP2",
        "GRPC_TARGET",
        "GRPC",
        "EXTERNAL_CALLOUT",
    ]
    tlsInfo: GoogleCloudApigeeV1TlsInfoConfig

@typing.type_check_only
class GoogleCloudApigeeV1TestDatastoreResponse(typing.TypedDict, total=False):
    error: str
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfo(typing.TypedDict, total=False):
    ciphers: _list[str]
    clientAuthEnabled: bool
    commonName: GoogleCloudApigeeV1TlsInfoCommonName
    enabled: bool
    enforce: bool
    ignoreValidationErrors: bool
    keyAlias: str
    keyStore: str
    protocols: _list[str]
    trustStore: str

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfoCommonName(typing.TypedDict, total=False):
    value: str
    wildcardMatch: bool

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfoConfig(typing.TypedDict, total=False):
    ciphers: _list[str]
    clientAuthEnabled: bool
    commonName: GoogleCloudApigeeV1CommonNameConfig
    enabled: bool
    enforce: bool
    ignoreValidationErrors: bool
    keyAlias: str
    keyAliasReference: GoogleCloudApigeeV1KeyAliasReference
    protocols: _list[str]
    trustStore: str

@typing.type_check_only
class GoogleCloudApigeeV1TraceConfig(typing.TypedDict, total=False):
    endpoint: str
    exporter: typing.Literal[
        "EXPORTER_UNSPECIFIED",
        "JAEGER",
        "CLOUD_TRACE",
        "OPEN_TELEMETRY_COLLECTOR",
        "OPEN_TELEMETRY_CLOUD_TRACE",
    ]
    samplingConfig: GoogleCloudApigeeV1TraceSamplingConfig
    spanSemantics: typing.Literal["SPAN_SEMANTICS_UNSPECIFIED", "LEGACY", "OTEL"]
    traceProtocol: typing.Literal["TRACE_PROTOCOL_UNSPECIFIED", "OPEN_CENSUS", "OTLP"]

@typing.type_check_only
class GoogleCloudApigeeV1TraceConfigOverride(typing.TypedDict, total=False):
    apiProxy: str
    name: str
    samplingConfig: GoogleCloudApigeeV1TraceSamplingConfig

@typing.type_check_only
class GoogleCloudApigeeV1TraceSamplingConfig(typing.TypedDict, total=False):
    sampler: typing.Literal["SAMPLER_UNSPECIFIED", "OFF", "PROBABILITY"]
    samplingRate: float

@typing.type_check_only
class GoogleCloudApigeeV1UpdateAppGroupAppKeyRequest(typing.TypedDict, total=False):
    action: str
    apiProducts: _list[str]
    appGroupAppKey: GoogleCloudApigeeV1AppGroupAppKey

@typing.type_check_only
class GoogleCloudApigeeV1UpdateError(typing.TypedDict, total=False):
    code: typing.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    message: str
    resource: str
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1UpdateSecurityIncidentRequest(typing.TypedDict, total=False):
    securityIncident: GoogleCloudApigeeV1SecurityIncident
    updateMask: str

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
class GoogleRpcPreconditionFailure(typing.TypedDict, total=False):
    violations: _list[GoogleRpcPreconditionFailureViolation]

@typing.type_check_only
class GoogleRpcPreconditionFailureViolation(typing.TypedDict, total=False):
    description: str
    subject: str
    type: str

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

@typing.type_check_only
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class GoogleTypeTimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int
