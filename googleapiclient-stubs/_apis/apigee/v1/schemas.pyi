import typing

import typing_extensions

_list = list

@typing.type_check_only
class EdgeConfigstoreBundleBadBundle(typing_extensions.TypedDict, total=False):
    violations: _list[EdgeConfigstoreBundleBadBundleViolation]

@typing.type_check_only
class EdgeConfigstoreBundleBadBundleViolation(typing_extensions.TypedDict, total=False):
    description: str
    filename: str

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudApigeeV1APIProductAssociation(
    typing_extensions.TypedDict, total=False
):
    apiproduct: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1Access(typing_extensions.TypedDict, total=False):
    Get: GoogleCloudApigeeV1AccessGet
    Remove: GoogleCloudApigeeV1AccessRemove
    Set: GoogleCloudApigeeV1AccessSet

@typing.type_check_only
class GoogleCloudApigeeV1AccessGet(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1AccessLoggingConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    filter: str

@typing.type_check_only
class GoogleCloudApigeeV1AccessRemove(typing_extensions.TypedDict, total=False):
    name: str
    success: bool

@typing.type_check_only
class GoogleCloudApigeeV1AccessSet(typing_extensions.TypedDict, total=False):
    name: str
    success: bool
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1ActivateNatAddressRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1AddonsConfig(typing_extensions.TypedDict, total=False):
    advancedApiOpsConfig: GoogleCloudApigeeV1AdvancedApiOpsConfig
    analyticsConfig: GoogleCloudApigeeV1AnalyticsConfig
    apiSecurityConfig: GoogleCloudApigeeV1ApiSecurityConfig
    connectorsPlatformConfig: GoogleCloudApigeeV1ConnectorsPlatformConfig
    integrationConfig: GoogleCloudApigeeV1IntegrationConfig
    monetizationConfig: GoogleCloudApigeeV1MonetizationConfig

@typing.type_check_only
class GoogleCloudApigeeV1AdjustDeveloperBalanceRequest(
    typing_extensions.TypedDict, total=False
):
    adjustment: GoogleTypeMoney

@typing.type_check_only
class GoogleCloudApigeeV1AdvancedApiOpsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1Alias(typing_extensions.TypedDict, total=False):
    alias: str
    certsInfo: GoogleCloudApigeeV1Certificate
    type: typing_extensions.Literal["ALIAS_TYPE_UNSPECIFIED", "CERT", "KEY_CERT"]

@typing.type_check_only
class GoogleCloudApigeeV1AliasRevisionConfig(typing_extensions.TypedDict, total=False):
    location: str
    name: str
    type: typing_extensions.Literal["ALIAS_TYPE_UNSPECIFIED", "CERT", "KEY_CERT"]

@typing.type_check_only
class GoogleCloudApigeeV1AnalyticsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    expireTimeMillis: str
    state: typing_extensions.Literal[
        "ADDON_STATE_UNSPECIFIED", "ENABLING", "ENABLED", "DISABLING", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiCategory(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    siteId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiCategoryResponse(typing_extensions.TypedDict, total=False):
    data: GoogleCloudApigeeV1ApiCategory
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiDoc(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1ApiDocDocumentation(typing_extensions.TypedDict, total=False):
    graphqlDocumentation: GoogleCloudApigeeV1GraphqlDocumentation
    oasDocumentation: GoogleCloudApigeeV1OASDocumentation

@typing.type_check_only
class GoogleCloudApigeeV1ApiDocDocumentationResponse(
    typing_extensions.TypedDict, total=False
):
    data: GoogleCloudApigeeV1ApiDocDocumentation
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiDocResponse(typing_extensions.TypedDict, total=False):
    data: GoogleCloudApigeeV1ApiDoc
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProduct(typing_extensions.TypedDict, total=False):
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
    name: str
    operationGroup: GoogleCloudApigeeV1OperationGroup
    proxies: _list[str]
    quota: str
    quotaCounterScope: typing_extensions.Literal[
        "QUOTA_COUNTER_SCOPE_UNSPECIFIED", "PROXY", "OPERATION"
    ]
    quotaInterval: str
    quotaTimeUnit: str
    scopes: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1ApiProductRef(typing_extensions.TypedDict, total=False):
    apiproduct: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxy(typing_extensions.TypedDict, total=False):
    apiProxyType: typing_extensions.Literal[
        "API_PROXY_TYPE_UNSPECIFIED", "PROGRAMMABLE", "CONFIGURABLE"
    ]
    labels: dict[str, typing.Any]
    latestRevisionId: str
    metaData: GoogleCloudApigeeV1EntityMetadata
    name: str
    readOnly: bool
    revision: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxyRevision(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1ApiSecurityConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    expiresAt: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiSecurityRuntimeConfig(
    typing_extensions.TypedDict, total=False
):
    location: _list[str]
    name: str
    revisionId: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1App(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1AppGroup(typing_extensions.TypedDict, total=False):
    appGroupId: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    channelId: str
    channelUri: str
    createdAt: str
    displayName: str
    lastModifiedAt: str
    name: str
    organization: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupApp(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1AppGroupAppKey(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1ArchiveDeployment(typing_extensions.TypedDict, total=False):
    createdAt: str
    gcsUri: str
    labels: dict[str, typing.Any]
    name: str
    operation: str
    updatedAt: str

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQuery(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1AsyncQueryResult(typing_extensions.TypedDict, total=False):
    expires: str
    self: str

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQueryResultView(typing_extensions.TypedDict, total=False):
    code: int
    error: str
    metadata: GoogleCloudApigeeV1QueryMetadata
    rows: _list[typing.Any]
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1Attribute(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1Attributes(typing_extensions.TypedDict, total=False):
    attribute: _list[GoogleCloudApigeeV1Attribute]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequest(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestIncludeAll(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArray(
    typing_extensions.TypedDict, total=False
):
    resources: _list[
        GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArrayResource
    ]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequestResourceArrayResource(
    typing_extensions.TypedDict, total=False
):
    name: str
    type: typing_extensions.Literal["RESOURCE_TYPE_UNSPECIFIED", "API_PROXY"]

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponse(
    typing_extensions.TypedDict, total=False
):
    assessmentTime: str
    nextPageToken: str
    securityAssessmentResults: _list[GoogleCloudApigeeV1SecurityAssessmentResult]

@typing.type_check_only
class GoogleCloudApigeeV1BatchUpdateSecurityIncidentsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudApigeeV1UpdateSecurityIncidentRequest]

@typing.type_check_only
class GoogleCloudApigeeV1BatchUpdateSecurityIncidentsResponse(
    typing_extensions.TypedDict, total=False
):
    securityIncidents: _list[GoogleCloudApigeeV1SecurityIncident]

@typing.type_check_only
class GoogleCloudApigeeV1CanaryEvaluation(typing_extensions.TypedDict, total=False):
    control: str
    createTime: str
    endTime: str
    metricLabels: GoogleCloudApigeeV1CanaryEvaluationMetricLabels
    name: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED"]
    treatment: str
    verdict: typing_extensions.Literal["VERDICT_UNSPECIFIED", "NONE", "FAIL", "PASS"]

@typing.type_check_only
class GoogleCloudApigeeV1CanaryEvaluationMetricLabels(
    typing_extensions.TypedDict, total=False
):
    env: str
    instance_id: str
    location: str

@typing.type_check_only
class GoogleCloudApigeeV1CertInfo(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1Certificate(typing_extensions.TypedDict, total=False):
    certInfo: _list[GoogleCloudApigeeV1CertInfo]

@typing.type_check_only
class GoogleCloudApigeeV1CommonNameConfig(typing_extensions.TypedDict, total=False):
    matchWildCards: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ComputeEnvironmentScoresRequest(
    typing_extensions.TypedDict, total=False
):
    filters: _list[GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilter]
    pageSize: int
    pageToken: str
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilter(
    typing_extensions.TypedDict, total=False
):
    scorePath: str

@typing.type_check_only
class GoogleCloudApigeeV1ComputeEnvironmentScoresResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    scores: _list[GoogleCloudApigeeV1Score]

@typing.type_check_only
class GoogleCloudApigeeV1ConfigVersion(typing_extensions.TypedDict, total=False):
    majorVersion: int
    minorVersion: int

@typing.type_check_only
class GoogleCloudApigeeV1ConnectorsPlatformConfig(
    typing_extensions.TypedDict, total=False
):
    enabled: bool
    expiresAt: str

@typing.type_check_only
class GoogleCloudApigeeV1ControlPlaneAccess(typing_extensions.TypedDict, total=False):
    analyticsPublisherIdentities: _list[str]
    name: str
    synchronizerIdentities: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1Credential(typing_extensions.TypedDict, total=False):
    apiProducts: _list[GoogleCloudApigeeV1ApiProductRef]
    attributes: _list[GoogleCloudApigeeV1Attribute]
    consumerKey: str
    consumerSecret: str
    expiresAt: str
    issuedAt: str
    scopes: _list[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1CreditDeveloperBalanceRequest(
    typing_extensions.TypedDict, total=False
):
    transactionAmount: GoogleTypeMoney
    transactionId: str

@typing.type_check_only
class GoogleCloudApigeeV1CustomReport(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1CustomReportMetric(typing_extensions.TypedDict, total=False):
    function: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1DataCollector(typing_extensions.TypedDict, total=False):
    createdAt: str
    description: str
    lastModifiedAt: str
    name: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "STRING", "BOOLEAN", "DATETIME"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1DataCollectorConfig(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "STRING", "BOOLEAN", "DATETIME"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1Datastore(typing_extensions.TypedDict, total=False):
    createTime: str
    datastoreConfig: GoogleCloudApigeeV1DatastoreConfig
    displayName: str
    lastUpdateTime: str
    org: str
    self: str
    targetType: str

@typing.type_check_only
class GoogleCloudApigeeV1DatastoreConfig(typing_extensions.TypedDict, total=False):
    bucketName: str
    datasetName: str
    path: str
    projectId: str
    tablePrefix: str

@typing.type_check_only
class GoogleCloudApigeeV1DateRange(typing_extensions.TypedDict, total=False):
    end: str
    start: str

@typing.type_check_only
class GoogleCloudApigeeV1DebugMask(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1DebugSession(typing_extensions.TypedDict, total=False):
    count: int
    createTime: str
    filter: str
    name: str
    timeout: str
    tracesize: int
    validity: int

@typing.type_check_only
class GoogleCloudApigeeV1DebugSessionTransaction(
    typing_extensions.TypedDict, total=False
):
    completed: bool
    point: _list[GoogleCloudApigeeV1Point]

@typing.type_check_only
class GoogleCloudApigeeV1DeleteCustomReportResponse(
    typing_extensions.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudApigeeV1DeleteResponse(typing_extensions.TypedDict, total=False):
    errorCode: str
    gcpResource: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1Deployment(typing_extensions.TypedDict, total=False):
    apiProxy: str
    deployStartTime: str
    environment: str
    errors: _list[GoogleRpcStatus]
    instances: _list[GoogleCloudApigeeV1InstanceDeploymentStatus]
    pods: _list[GoogleCloudApigeeV1PodStatus]
    proxyDeploymentType: typing_extensions.Literal[
        "PROXY_DEPLOYMENT_TYPE_UNSPECIFIED", "STANDARD", "EXTENSIBLE"
    ]
    revision: str
    routeConflicts: _list[GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict]
    serviceAccount: str
    state: typing_extensions.Literal[
        "RUNTIME_STATE_UNSPECIFIED", "READY", "PROGRESSING", "ERROR"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReport(
    typing_extensions.TypedDict, total=False
):
    routingChanges: _list[GoogleCloudApigeeV1DeploymentChangeReportRoutingChange]
    routingConflicts: _list[GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict]
    validationErrors: GoogleRpcPreconditionFailure

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportRoutingChange(
    typing_extensions.TypedDict, total=False
):
    description: str
    environmentGroup: str
    fromDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment
    shouldSequenceRollout: bool
    toDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict(
    typing_extensions.TypedDict, total=False
):
    conflictingDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment
    description: str
    environmentGroup: str

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment(
    typing_extensions.TypedDict, total=False
):
    apiProxy: str
    basepath: str
    environment: str
    revision: str

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentConfig(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1DeploymentGroupConfig(
    typing_extensions.TypedDict, total=False
):
    deploymentGroupType: typing_extensions.Literal[
        "DEPLOYMENT_GROUP_TYPE_UNSPECIFIED", "STANDARD", "EXTENSIBLE"
    ]
    name: str
    revisionId: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Developer(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1DeveloperApp(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1DeveloperAppKey(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1DeveloperBalance(typing_extensions.TypedDict, total=False):
    wallets: _list[GoogleCloudApigeeV1DeveloperBalanceWallet]

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperBalanceWallet(
    typing_extensions.TypedDict, total=False
):
    balance: GoogleTypeMoney
    lastCreditTime: str

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperMonetizationConfig(
    typing_extensions.TypedDict, total=False
):
    billingType: typing_extensions.Literal[
        "BILLING_TYPE_UNSPECIFIED", "PREPAID", "POSTPAID"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperSubscription(
    typing_extensions.TypedDict, total=False
):
    apiproduct: str
    createdAt: str
    endTime: str
    lastModifiedAt: str
    name: str
    startTime: str

@typing.type_check_only
class GoogleCloudApigeeV1DimensionMetric(typing_extensions.TypedDict, total=False):
    individualNames: _list[str]
    metrics: _list[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1DisableSecurityActionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1DocumentationFile(typing_extensions.TypedDict, total=False):
    contents: str
    displayName: str

@typing.type_check_only
class GoogleCloudApigeeV1EnableSecurityActionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1EndpointAttachment(typing_extensions.TypedDict, total=False):
    connectionState: typing_extensions.Literal[
        "CONNECTION_STATE_UNSPECIFIED",
        "UNAVAILABLE",
        "PENDING",
        "ACCEPTED",
        "REJECTED",
        "CLOSED",
        "FROZEN",
        "NEEDS_ATTENTION",
    ]
    host: str
    location: str
    name: str
    serviceAttachment: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EndpointChainingRule(typing_extensions.TypedDict, total=False):
    deploymentGroup: str
    proxyIds: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1EntityMetadata(typing_extensions.TypedDict, total=False):
    createdAt: str
    lastModifiedAt: str
    subType: str

@typing.type_check_only
class GoogleCloudApigeeV1Environment(typing_extensions.TypedDict, total=False):
    apiProxyType: typing_extensions.Literal[
        "API_PROXY_TYPE_UNSPECIFIED", "PROGRAMMABLE", "CONFIGURABLE"
    ]
    clientIpResolutionConfig: GoogleCloudApigeeV1EnvironmentClientIPResolutionConfig
    createdAt: str
    deploymentType: typing_extensions.Literal[
        "DEPLOYMENT_TYPE_UNSPECIFIED", "PROXY", "ARCHIVE"
    ]
    description: str
    displayName: str
    forwardProxyUri: str
    hasAttachedFlowHooks: bool
    lastModifiedAt: str
    name: str
    nodeConfig: GoogleCloudApigeeV1NodeConfig
    properties: GoogleCloudApigeeV1Properties
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]
    type: typing_extensions.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "BASE", "INTERMEDIATE", "COMPREHENSIVE"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentClientIPResolutionConfig(
    typing_extensions.TypedDict, total=False
):
    headerIndexAlgorithm: (
        GoogleCloudApigeeV1EnvironmentClientIPResolutionConfigHeaderIndexAlgorithm
    )

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentClientIPResolutionConfigHeaderIndexAlgorithm(
    typing_extensions.TypedDict, total=False
):
    ipHeaderIndex: int
    ipHeaderName: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfig(typing_extensions.TypedDict, total=False):
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
    typing_extensions.TypedDict, total=False
):
    headerIndexAlgorithm: (
        GoogleCloudApigeeV1EnvironmentConfigClientIPResolutionConfigHeaderIndexAlgorithm
    )

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfigClientIPResolutionConfigHeaderIndexAlgorithm(
    typing_extensions.TypedDict, total=False
):
    ipHeaderIndex: int
    ipHeaderName: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroup(typing_extensions.TypedDict, total=False):
    createdAt: str
    hostnames: _list[str]
    lastModifiedAt: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupAttachment(
    typing_extensions.TypedDict, total=False
):
    createdAt: str
    environment: str
    environmentGroupId: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupConfig(
    typing_extensions.TypedDict, total=False
):
    endpointChainingRules: _list[GoogleCloudApigeeV1EndpointChainingRule]
    hostnames: _list[str]
    location: str
    name: str
    revisionId: str
    routingRules: _list[GoogleCloudApigeeV1RoutingRule]
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1Export(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1ExportRequest(typing_extensions.TypedDict, total=False):
    csvDelimiter: str
    datastoreName: str
    dateRange: GoogleCloudApigeeV1DateRange
    description: str
    name: str
    outputFormat: str

@typing.type_check_only
class GoogleCloudApigeeV1FlowHook(typing_extensions.TypedDict, total=False):
    continueOnError: bool
    description: str
    flowHookPoint: str
    sharedFlow: str

@typing.type_check_only
class GoogleCloudApigeeV1FlowHookConfig(typing_extensions.TypedDict, total=False):
    continueOnError: bool
    name: str
    sharedFlowName: str

@typing.type_check_only
class GoogleCloudApigeeV1GenerateDownloadUrlRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1GenerateDownloadUrlResponse(
    typing_extensions.TypedDict, total=False
):
    downloadUri: str

@typing.type_check_only
class GoogleCloudApigeeV1GenerateUploadUrlRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1GenerateUploadUrlResponse(
    typing_extensions.TypedDict, total=False
):
    uploadUri: str

@typing.type_check_only
class GoogleCloudApigeeV1GetAsyncQueryResultUrlResponse(
    typing_extensions.TypedDict, total=False
):
    urls: _list[GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfo]

@typing.type_check_only
class GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfo(
    typing_extensions.TypedDict, total=False
):
    md5: str
    sizeBytes: str
    uri: str

@typing.type_check_only
class GoogleCloudApigeeV1GetSyncAuthorizationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1GraphQLOperation(typing_extensions.TypedDict, total=False):
    operation: str
    operationTypes: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1GraphQLOperationConfig(
    typing_extensions.TypedDict, total=False
):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    operations: _list[GoogleCloudApigeeV1GraphQLOperation]
    quota: GoogleCloudApigeeV1Quota

@typing.type_check_only
class GoogleCloudApigeeV1GraphQLOperationGroup(
    typing_extensions.TypedDict, total=False
):
    operationConfigType: str
    operationConfigs: _list[GoogleCloudApigeeV1GraphQLOperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1GraphqlDocumentation(typing_extensions.TypedDict, total=False):
    endpointUri: str
    schema: GoogleCloudApigeeV1DocumentationFile

@typing.type_check_only
class GoogleCloudApigeeV1GrpcOperationConfig(typing_extensions.TypedDict, total=False):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    methods: _list[str]
    quota: GoogleCloudApigeeV1Quota
    service: str

@typing.type_check_only
class GoogleCloudApigeeV1GrpcOperationGroup(typing_extensions.TypedDict, total=False):
    operationConfigs: _list[GoogleCloudApigeeV1GrpcOperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1IngressConfig(typing_extensions.TypedDict, total=False):
    environmentGroups: _list[GoogleCloudApigeeV1EnvironmentGroupConfig]
    name: str
    revisionCreateTime: str
    revisionId: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Instance(typing_extensions.TypedDict, total=False):
    accessLoggingConfig: GoogleCloudApigeeV1AccessLoggingConfig
    consumerAcceptList: _list[str]
    createdAt: str
    description: str
    diskEncryptionKeyName: str
    displayName: str
    host: str
    ipRange: str
    lastModifiedAt: str
    location: str
    name: str
    peeringCidrRange: typing_extensions.Literal[
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
    serviceAttachment: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1InstanceAttachment(typing_extensions.TypedDict, total=False):
    createdAt: str
    environment: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1InstanceDeploymentStatus(
    typing_extensions.TypedDict, total=False
):
    deployedRevisions: _list[
        GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision
    ]
    deployedRoutes: _list[GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute]
    instance: str

@typing.type_check_only
class GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision(
    typing_extensions.TypedDict, total=False
):
    percentage: int
    revision: str

@typing.type_check_only
class GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute(
    typing_extensions.TypedDict, total=False
):
    basepath: str
    envgroup: str
    environment: str
    percentage: int

@typing.type_check_only
class GoogleCloudApigeeV1IntegrationConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1KeyAliasReference(typing_extensions.TypedDict, total=False):
    aliasId: str
    reference: str

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueEntry(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueMap(typing_extensions.TypedDict, total=False):
    encrypted: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1Keystore(typing_extensions.TypedDict, total=False):
    aliases: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1KeystoreConfig(typing_extensions.TypedDict, total=False):
    aliases: _list[GoogleCloudApigeeV1AliasRevisionConfig]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiCategoriesResponse(
    typing_extensions.TypedDict, total=False
):
    data: _list[GoogleCloudApigeeV1ApiCategory]
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiDocsResponse(typing_extensions.TypedDict, total=False):
    data: _list[GoogleCloudApigeeV1ApiDoc]
    errorCode: str
    message: str
    nextPageToken: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProductsResponse(
    typing_extensions.TypedDict, total=False
):
    apiProduct: _list[GoogleCloudApigeeV1ApiProduct]

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProxiesResponse(
    typing_extensions.TypedDict, total=False
):
    proxies: _list[GoogleCloudApigeeV1ApiProxy]

@typing.type_check_only
class GoogleCloudApigeeV1ListAppGroupAppsResponse(
    typing_extensions.TypedDict, total=False
):
    appGroupApps: _list[GoogleCloudApigeeV1AppGroupApp]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListAppGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    appGroups: _list[GoogleCloudApigeeV1AppGroup]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleCloudApigeeV1ListAppsResponse(typing_extensions.TypedDict, total=False):
    app: _list[GoogleCloudApigeeV1App]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleCloudApigeeV1ListArchiveDeploymentsResponse(
    typing_extensions.TypedDict, total=False
):
    archiveDeployments: _list[GoogleCloudApigeeV1ArchiveDeployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListAsyncQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    queries: _list[GoogleCloudApigeeV1AsyncQuery]

@typing.type_check_only
class GoogleCloudApigeeV1ListCustomReportsResponse(
    typing_extensions.TypedDict, total=False
):
    qualifier: _list[GoogleCloudApigeeV1CustomReport]

@typing.type_check_only
class GoogleCloudApigeeV1ListDataCollectorsResponse(
    typing_extensions.TypedDict, total=False
):
    dataCollectors: _list[GoogleCloudApigeeV1DataCollector]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListDatastoresResponse(
    typing_extensions.TypedDict, total=False
):
    datastores: _list[GoogleCloudApigeeV1Datastore]

@typing.type_check_only
class GoogleCloudApigeeV1ListDebugSessionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessions: _list[GoogleCloudApigeeV1Session]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeploymentsResponse(
    typing_extensions.TypedDict, total=False
):
    deployments: _list[GoogleCloudApigeeV1Deployment]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperAppsResponse(
    typing_extensions.TypedDict, total=False
):
    app: _list[GoogleCloudApigeeV1DeveloperApp]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperSubscriptionsResponse(
    typing_extensions.TypedDict, total=False
):
    developerSubscriptions: _list[GoogleCloudApigeeV1DeveloperSubscription]
    nextStartKey: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEndpointAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    endpointAttachments: _list[GoogleCloudApigeeV1EndpointAttachment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environmentGroupAttachments: _list[GoogleCloudApigeeV1EnvironmentGroupAttachment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    environmentGroups: _list[GoogleCloudApigeeV1EnvironmentGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    resourceFile: _list[GoogleCloudApigeeV1ResourceFile]

@typing.type_check_only
class GoogleCloudApigeeV1ListExportsResponse(typing_extensions.TypedDict, total=False):
    exports: _list[GoogleCloudApigeeV1Export]

@typing.type_check_only
class GoogleCloudApigeeV1ListHybridIssuersResponse(
    typing_extensions.TypedDict, total=False
):
    issuers: _list[GoogleCloudApigeeV1ServiceIssuersMapping]

@typing.type_check_only
class GoogleCloudApigeeV1ListInstanceAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    attachments: _list[GoogleCloudApigeeV1InstanceAttachment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleCloudApigeeV1Instance]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListKeyValueEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    keyValueEntries: _list[GoogleCloudApigeeV1KeyValueEntry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListNatAddressesResponse(
    typing_extensions.TypedDict, total=False
):
    natAddresses: _list[GoogleCloudApigeeV1NatAddress]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListOfDevelopersResponse(
    typing_extensions.TypedDict, total=False
):
    developer: _list[GoogleCloudApigeeV1Developer]

@typing.type_check_only
class GoogleCloudApigeeV1ListOrganizationsResponse(
    typing_extensions.TypedDict, total=False
):
    organizations: _list[GoogleCloudApigeeV1OrganizationProjectMapping]

@typing.type_check_only
class GoogleCloudApigeeV1ListRatePlansResponse(
    typing_extensions.TypedDict, total=False
):
    nextStartKey: str
    ratePlans: _list[GoogleCloudApigeeV1RatePlan]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityActionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securityActions: _list[GoogleCloudApigeeV1SecurityAction]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityIncidentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securityIncidents: _list[GoogleCloudApigeeV1SecurityIncident]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfileRevisionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securityProfiles: _list[GoogleCloudApigeeV1SecurityProfile]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfilesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securityProfiles: _list[GoogleCloudApigeeV1SecurityProfile]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfilesV2Response(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securityProfilesV2: _list[GoogleCloudApigeeV1SecurityProfileV2]

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityReportsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    securityReports: _list[GoogleCloudApigeeV1SecurityReport]

@typing.type_check_only
class GoogleCloudApigeeV1ListSharedFlowsResponse(
    typing_extensions.TypedDict, total=False
):
    sharedFlows: _list[GoogleCloudApigeeV1SharedFlow]

@typing.type_check_only
class GoogleCloudApigeeV1ListTraceConfigOverridesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    traceConfigOverrides: _list[GoogleCloudApigeeV1TraceConfigOverride]

@typing.type_check_only
class GoogleCloudApigeeV1Metadata(typing_extensions.TypedDict, total=False):
    errors: _list[str]
    notices: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1Metric(typing_extensions.TypedDict, total=False):
    name: str
    values: _list[typing.Any]

@typing.type_check_only
class GoogleCloudApigeeV1MetricAggregation(typing_extensions.TypedDict, total=False):
    aggregation: typing_extensions.Literal[
        "AGGREGATION_FUNCTION_UNSPECIFIED", "AVG", "SUM", "MIN", "MAX", "COUNT_DISTINCT"
    ]
    name: str
    order: typing_extensions.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class GoogleCloudApigeeV1MonetizationConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1NatAddress(typing_extensions.TypedDict, total=False):
    ipAddress: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RESERVED", "ACTIVE", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1NodeConfig(typing_extensions.TypedDict, total=False):
    currentAggregateNodeCount: str
    maxNodeCount: str
    minNodeCount: str

@typing.type_check_only
class GoogleCloudApigeeV1OASDocumentation(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "YAML", "JSON"]
    spec: GoogleCloudApigeeV1DocumentationFile

@typing.type_check_only
class GoogleCloudApigeeV1Operation(typing_extensions.TypedDict, total=False):
    methods: _list[str]
    resource: str

@typing.type_check_only
class GoogleCloudApigeeV1OperationConfig(typing_extensions.TypedDict, total=False):
    apiSource: str
    attributes: _list[GoogleCloudApigeeV1Attribute]
    operations: _list[GoogleCloudApigeeV1Operation]
    quota: GoogleCloudApigeeV1Quota

@typing.type_check_only
class GoogleCloudApigeeV1OperationGroup(typing_extensions.TypedDict, total=False):
    operationConfigType: str
    operationConfigs: _list[GoogleCloudApigeeV1OperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1OperationMetadata(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "INSERT", "DELETE", "UPDATE"
    ]
    progress: GoogleCloudApigeeV1OperationMetadataProgress
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "FINISHED"
    ]
    targetResourceName: str
    warnings: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1OperationMetadataProgress(
    typing_extensions.TypedDict, total=False
):
    description: str
    details: dict[str, typing.Any]
    percentDone: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "FINISHED"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStats(typing_extensions.TypedDict, total=False):
    Response: GoogleCloudApigeeV1OptimizedStatsResponse

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsNode(typing_extensions.TypedDict, total=False):
    data: _list[typing.Any]

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsResponse(
    typing_extensions.TypedDict, total=False
):
    TimeUnit: _list[str]
    metaData: GoogleCloudApigeeV1Metadata
    resultTruncated: bool
    stats: GoogleCloudApigeeV1OptimizedStatsNode

@typing.type_check_only
class GoogleCloudApigeeV1Organization(typing_extensions.TypedDict, total=False):
    addonsConfig: GoogleCloudApigeeV1AddonsConfig
    analyticsRegion: str
    apiConsumerDataEncryptionKeyName: str
    apiConsumerDataLocation: str
    apigeeProjectId: str
    attributes: _list[str]
    authorizedNetwork: str
    billingType: typing_extensions.Literal[
        "BILLING_TYPE_UNSPECIFIED", "SUBSCRIPTION", "EVALUATION", "PAYG"
    ]
    caCertificate: str
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
    portalDisabled: bool
    projectId: str
    properties: GoogleCloudApigeeV1Properties
    runtimeDatabaseEncryptionKeyName: str
    runtimeType: typing_extensions.Literal[
        "RUNTIME_TYPE_UNSPECIFIED", "CLOUD", "HYBRID"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]
    subscriptionPlan: typing_extensions.Literal[
        "SUBSCRIPTION_PLAN_UNSPECIFIED", "SUBSCRIPTION_2021", "SUBSCRIPTION_2024"
    ]
    subscriptionType: typing_extensions.Literal[
        "SUBSCRIPTION_TYPE_UNSPECIFIED", "PAID", "TRIAL"
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_TRIAL", "TYPE_PAID", "TYPE_INTERNAL"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1OrganizationProjectMapping(
    typing_extensions.TypedDict, total=False
):
    location: str
    organization: str
    projectId: str
    projectIds: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1PodStatus(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1Point(typing_extensions.TypedDict, total=False):
    id: str
    results: _list[GoogleCloudApigeeV1Result]

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfig(typing_extensions.TypedDict, total=False):
    categories: _list[GoogleCloudApigeeV1ProfileConfigCategory]

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigAbuse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigAuthorization(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigCORS(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigCategory(
    typing_extensions.TypedDict, total=False
):
    abuse: GoogleCloudApigeeV1ProfileConfigAbuse
    authorization: GoogleCloudApigeeV1ProfileConfigAuthorization
    cors: GoogleCloudApigeeV1ProfileConfigCORS
    mediation: GoogleCloudApigeeV1ProfileConfigMediation
    mtls: GoogleCloudApigeeV1ProfileConfigMTLS
    threat: GoogleCloudApigeeV1ProfileConfigThreat

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigMTLS(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigMediation(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ProfileConfigThreat(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1Properties(typing_extensions.TypedDict, total=False):
    property: _list[GoogleCloudApigeeV1Property]

@typing.type_check_only
class GoogleCloudApigeeV1Property(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1ProvisionOrganizationRequest(
    typing_extensions.TypedDict, total=False
):
    analyticsRegion: str
    authorizedNetwork: str
    disableVpcPeering: bool
    runtimeLocation: str

@typing.type_check_only
class GoogleCloudApigeeV1Query(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1QueryMetadata(typing_extensions.TypedDict, total=False):
    dimensions: _list[str]
    endTimestamp: str
    metrics: _list[str]
    outputFormat: str
    startTimestamp: str
    timeUnit: str

@typing.type_check_only
class GoogleCloudApigeeV1QueryMetric(typing_extensions.TypedDict, total=False):
    alias: str
    function: str
    name: str
    operator: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1QueryTabularStatsRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[GoogleCloudApigeeV1MetricAggregation]
    pageSize: int
    pageToken: str
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudApigeeV1QueryTabularStatsResponse(
    typing_extensions.TypedDict, total=False
):
    columns: _list[str]
    nextPageToken: str
    values: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudApigeeV1QueryTimeSeriesStatsRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[GoogleCloudApigeeV1MetricAggregation]
    pageSize: int
    pageToken: str
    timeRange: GoogleTypeInterval
    timestampOrder: typing_extensions.Literal[
        "ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    windowSize: typing_extensions.Literal[
        "WINDOW_SIZE_UNSPECIFIED", "MINUTE", "HOUR", "DAY", "MONTH"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1QueryTimeSeriesStatsResponse(
    typing_extensions.TypedDict, total=False
):
    columns: _list[str]
    nextPageToken: str
    values: _list[GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequence]

@typing.type_check_only
class GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequence(
    typing_extensions.TypedDict, total=False
):
    dimensions: dict[str, typing.Any]
    points: _list[_list[typing.Any]]

@typing.type_check_only
class GoogleCloudApigeeV1Quota(typing_extensions.TypedDict, total=False):
    interval: str
    limit: str
    timeUnit: str

@typing.type_check_only
class GoogleCloudApigeeV1RatePlan(typing_extensions.TypedDict, total=False):
    apiproduct: str
    billingPeriod: typing_extensions.Literal[
        "BILLING_PERIOD_UNSPECIFIED", "WEEKLY", "MONTHLY"
    ]
    consumptionPricingRates: _list[GoogleCloudApigeeV1RateRange]
    consumptionPricingType: typing_extensions.Literal[
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
    paymentFundingModel: typing_extensions.Literal[
        "PAYMENT_FUNDING_MODEL_UNSPECIFIED", "PREPAID", "POSTPAID"
    ]
    revenueShareRates: _list[GoogleCloudApigeeV1RevenueShareRange]
    revenueShareType: typing_extensions.Literal[
        "REVENUE_SHARE_TYPE_UNSPECIFIED", "FIXED", "VOLUME_BANDED"
    ]
    setupFee: GoogleTypeMoney
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "DRAFT", "PUBLISHED"]

@typing.type_check_only
class GoogleCloudApigeeV1RateRange(typing_extensions.TypedDict, total=False):
    end: str
    fee: GoogleTypeMoney
    start: str

@typing.type_check_only
class GoogleCloudApigeeV1Reference(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    refers: str
    resourceType: str

@typing.type_check_only
class GoogleCloudApigeeV1ReferenceConfig(typing_extensions.TypedDict, total=False):
    name: str
    resourceName: str

@typing.type_check_only
class GoogleCloudApigeeV1ReportInstanceStatusRequest(
    typing_extensions.TypedDict, total=False
):
    instanceUid: str
    reportTime: str
    resources: _list[GoogleCloudApigeeV1ResourceStatus]

@typing.type_check_only
class GoogleCloudApigeeV1ReportInstanceStatusResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ReportProperty(typing_extensions.TypedDict, total=False):
    property: str
    value: _list[GoogleCloudApigeeV1Attribute]

@typing.type_check_only
class GoogleCloudApigeeV1ResourceConfig(typing_extensions.TypedDict, total=False):
    location: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ResourceFile(typing_extensions.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1ResourceFiles(typing_extensions.TypedDict, total=False):
    resourceFile: _list[GoogleCloudApigeeV1ResourceFile]

@typing.type_check_only
class GoogleCloudApigeeV1ResourceStatus(typing_extensions.TypedDict, total=False):
    resource: str
    revisions: _list[GoogleCloudApigeeV1RevisionStatus]
    totalReplicas: int
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Result(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1RevenueShareRange(typing_extensions.TypedDict, total=False):
    end: str
    sharePercentage: float
    start: str

@typing.type_check_only
class GoogleCloudApigeeV1RevisionStatus(typing_extensions.TypedDict, total=False):
    errors: _list[GoogleCloudApigeeV1UpdateError]
    jsonSpec: str
    replicas: int
    revisionId: str

@typing.type_check_only
class GoogleCloudApigeeV1RoutingRule(typing_extensions.TypedDict, total=False):
    basepath: str
    deploymentGroup: str
    envGroupRevision: str
    environment: str
    otherTargets: _list[str]
    receiver: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeAddonsConfig(typing_extensions.TypedDict, total=False):
    analyticsConfig: GoogleCloudApigeeV1RuntimeAnalyticsConfig
    apiSecurityConfig: GoogleCloudApigeeV1RuntimeApiSecurityConfig
    name: str
    revisionId: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeAnalyticsConfig(
    typing_extensions.TypedDict, total=False
):
    billingPipelineEnabled: bool
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeApiSecurityConfig(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeConfig(typing_extensions.TypedDict, total=False):
    analyticsBucket: str
    name: str
    tenantProjectId: str
    traceBucket: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeTraceConfig(typing_extensions.TypedDict, total=False):
    endpoint: str
    exporter: typing_extensions.Literal["EXPORTER_UNSPECIFIED", "JAEGER", "CLOUD_TRACE"]
    name: str
    overrides: _list[GoogleCloudApigeeV1RuntimeTraceConfigOverride]
    revisionCreateTime: str
    revisionId: str
    samplingConfig: GoogleCloudApigeeV1RuntimeTraceSamplingConfig

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeTraceConfigOverride(
    typing_extensions.TypedDict, total=False
):
    apiProxy: str
    name: str
    revisionCreateTime: str
    revisionId: str
    samplingConfig: GoogleCloudApigeeV1RuntimeTraceSamplingConfig
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeTraceSamplingConfig(
    typing_extensions.TypedDict, total=False
):
    sampler: typing_extensions.Literal["SAMPLER_UNSPECIFIED", "OFF", "PROBABILITY"]
    samplingRate: float

@typing.type_check_only
class GoogleCloudApigeeV1Schema(typing_extensions.TypedDict, total=False):
    dimensions: _list[GoogleCloudApigeeV1SchemaSchemaElement]
    meta: _list[str]
    metrics: _list[GoogleCloudApigeeV1SchemaSchemaElement]

@typing.type_check_only
class GoogleCloudApigeeV1SchemaSchemaElement(typing_extensions.TypedDict, total=False):
    name: str
    properties: GoogleCloudApigeeV1SchemaSchemaProperty

@typing.type_check_only
class GoogleCloudApigeeV1SchemaSchemaProperty(typing_extensions.TypedDict, total=False):
    createTime: str
    custom: str
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1Score(typing_extensions.TypedDict, total=False):
    component: GoogleCloudApigeeV1ScoreComponent
    subcomponents: _list[GoogleCloudApigeeV1ScoreComponent]
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponent(typing_extensions.TypedDict, total=False):
    calculateTime: str
    dataCaptureTime: str
    drilldownPaths: _list[str]
    recommendations: _list[GoogleCloudApigeeV1ScoreComponentRecommendation]
    score: int
    scorePath: str

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponentRecommendation(
    typing_extensions.TypedDict, total=False
):
    actions: _list[GoogleCloudApigeeV1ScoreComponentRecommendationAction]
    description: str
    impact: int
    title: str

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponentRecommendationAction(
    typing_extensions.TypedDict, total=False
):
    actionContext: GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContext
    description: str

@typing.type_check_only
class GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContext(
    typing_extensions.TypedDict, total=False
):
    documentationLink: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAction(typing_extensions.TypedDict, total=False):
    allow: GoogleCloudApigeeV1SecurityActionAllow
    apiProxies: _list[str]
    conditionConfig: GoogleCloudApigeeV1SecurityActionConditionConfig
    createTime: str
    deny: GoogleCloudApigeeV1SecurityActionDeny
    description: str
    expireTime: str
    flag: GoogleCloudApigeeV1SecurityActionFlag
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    ttl: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionAllow(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionConditionConfig(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudApigeeV1SecurityActionDeny(typing_extensions.TypedDict, total=False):
    responseCode: int

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionFlag(typing_extensions.TypedDict, total=False):
    headers: _list[GoogleCloudApigeeV1SecurityActionHttpHeader]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionHttpHeader(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionsConfig(
    typing_extensions.TypedDict, total=False
):
    enabled: bool
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResult(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    error: GoogleRpcStatus
    resource: GoogleCloudApigeeV1SecurityAssessmentResultResource
    scoringResult: GoogleCloudApigeeV1SecurityAssessmentResultScoringResult

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultResource(
    typing_extensions.TypedDict, total=False
):
    name: str
    resourceRevisionId: str
    type: typing_extensions.Literal["RESOURCE_TYPE_UNSPECIFIED", "API_PROXY"]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResult(
    typing_extensions.TypedDict, total=False
):
    assessmentRecommendations: dict[str, typing.Any]
    dataUpdateTime: str
    failedAssessmentPerWeight: dict[str, typing.Any]
    score: int
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "MINIMAL"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendation(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    recommendations: _list[
        GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendation
    ]
    scoreImpact: int
    verdict: typing_extensions.Literal["VERDICT_UNSPECIFIED", "PASS", "FAIL"]
    weight: typing_extensions.Literal[
        "WEIGHT_UNSPECIFIED", "MINOR", "MODERATE", "MAJOR"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendation(
    typing_extensions.TypedDict, total=False
):
    description: str
    link: GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendationLink

@typing.type_check_only
class GoogleCloudApigeeV1SecurityAssessmentResultScoringResultAssessmentRecommendationRecommendationLink(
    typing_extensions.TypedDict, total=False
):
    text: str
    uri: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityIncident(typing_extensions.TypedDict, total=False):
    detectionTypes: _list[str]
    displayName: str
    firstDetectedTime: str
    lastDetectedTime: str
    lastObservabilityChangeTime: str
    name: str
    observability: typing_extensions.Literal[
        "OBSERVABILITY_UNSPECIFIED", "ACTIVE", "ARCHIVED"
    ]
    riskLevel: typing_extensions.Literal[
        "RISK_LEVEL_UNSPECIFIED", "LOW", "MODERATE", "SEVERE"
    ]
    trafficCount: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfile(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1SecurityProfileEnvironment(
    typing_extensions.TypedDict, total=False
):
    attachTime: str
    environment: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileEnvironmentAssociation(
    typing_extensions.TypedDict, total=False
):
    attachTime: str
    name: str
    securityProfileRevisionId: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileScoringConfig(
    typing_extensions.TypedDict, total=False
):
    description: str
    scorePath: str
    title: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileV2(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    googleDefined: bool
    name: str
    profileAssessmentConfigs: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileV2ProfileAssessmentConfig(
    typing_extensions.TypedDict, total=False
):
    weight: typing_extensions.Literal[
        "WEIGHT_UNSPECIFIED", "MINOR", "MODERATE", "MAJOR"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReport(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1SecurityReportMetadata(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    endTimestamp: str
    metrics: _list[str]
    mimeType: str
    startTimestamp: str
    timeUnit: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportQuery(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1SecurityReportQueryMetric(
    typing_extensions.TypedDict, total=False
):
    aggregationFunction: str
    alias: str
    name: str
    operator: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportResultMetadata(
    typing_extensions.TypedDict, total=False
):
    expires: str
    self: str

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportResultView(
    typing_extensions.TypedDict, total=False
):
    code: int
    error: str
    metadata: GoogleCloudApigeeV1SecurityReportMetadata
    rows: _list[typing.Any]
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1SecuritySettings(typing_extensions.TypedDict, total=False):
    mlRetrainingFeedbackEnabled: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ServiceIssuersMapping(
    typing_extensions.TypedDict, total=False
):
    emailIds: _list[str]
    service: str

@typing.type_check_only
class GoogleCloudApigeeV1Session(typing_extensions.TypedDict, total=False):
    id: str
    timestampMs: str

@typing.type_check_only
class GoogleCloudApigeeV1SetAddonEnablementRequest(
    typing_extensions.TypedDict, total=False
):
    analyticsEnabled: bool
    apiSecurityEnabled: bool

@typing.type_check_only
class GoogleCloudApigeeV1SetAddonsRequest(typing_extensions.TypedDict, total=False):
    addonsConfig: GoogleCloudApigeeV1AddonsConfig

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlow(typing_extensions.TypedDict, total=False):
    latestRevisionId: str
    metaData: GoogleCloudApigeeV1EntityMetadata
    name: str
    revision: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlowRevision(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1Stats(typing_extensions.TypedDict, total=False):
    environments: _list[GoogleCloudApigeeV1StatsEnvironmentStats]
    hosts: _list[GoogleCloudApigeeV1StatsHostStats]
    metaData: GoogleCloudApigeeV1Metadata

@typing.type_check_only
class GoogleCloudApigeeV1StatsEnvironmentStats(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[GoogleCloudApigeeV1DimensionMetric]
    metrics: _list[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1StatsHostStats(typing_extensions.TypedDict, total=False):
    dimensions: _list[GoogleCloudApigeeV1DimensionMetric]
    metrics: _list[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1Subscription(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1SyncAuthorization(typing_extensions.TypedDict, total=False):
    etag: str
    identities: _list[str]

@typing.type_check_only
class GoogleCloudApigeeV1TargetServer(typing_extensions.TypedDict, total=False):
    description: str
    host: str
    isEnabled: bool
    name: str
    port: int
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED",
        "HTTP",
        "HTTP2",
        "GRPC_TARGET",
        "GRPC",
        "EXTERNAL_CALLOUT",
    ]
    sSLInfo: GoogleCloudApigeeV1TlsInfo

@typing.type_check_only
class GoogleCloudApigeeV1TargetServerConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    host: str
    name: str
    port: int
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED",
        "HTTP",
        "HTTP2",
        "GRPC_TARGET",
        "GRPC",
        "EXTERNAL_CALLOUT",
    ]
    tlsInfo: GoogleCloudApigeeV1TlsInfoConfig

@typing.type_check_only
class GoogleCloudApigeeV1TestDatastoreResponse(
    typing_extensions.TypedDict, total=False
):
    error: str
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfo(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1TlsInfoCommonName(typing_extensions.TypedDict, total=False):
    value: str
    wildcardMatch: bool

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfoConfig(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApigeeV1TraceConfig(typing_extensions.TypedDict, total=False):
    endpoint: str
    exporter: typing_extensions.Literal["EXPORTER_UNSPECIFIED", "JAEGER", "CLOUD_TRACE"]
    samplingConfig: GoogleCloudApigeeV1TraceSamplingConfig

@typing.type_check_only
class GoogleCloudApigeeV1TraceConfigOverride(typing_extensions.TypedDict, total=False):
    apiProxy: str
    name: str
    samplingConfig: GoogleCloudApigeeV1TraceSamplingConfig

@typing.type_check_only
class GoogleCloudApigeeV1TraceSamplingConfig(typing_extensions.TypedDict, total=False):
    sampler: typing_extensions.Literal["SAMPLER_UNSPECIFIED", "OFF", "PROBABILITY"]
    samplingRate: float

@typing.type_check_only
class GoogleCloudApigeeV1UpdateAppGroupAppKeyRequest(
    typing_extensions.TypedDict, total=False
):
    action: str
    apiProducts: _list[str]
    appGroupAppKey: GoogleCloudApigeeV1AppGroupAppKey

@typing.type_check_only
class GoogleCloudApigeeV1UpdateError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
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
class GoogleCloudApigeeV1UpdateSecurityIncidentRequest(
    typing_extensions.TypedDict, total=False
):
    securityIncident: GoogleCloudApigeeV1SecurityIncident
    updateMask: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

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
class GoogleRpcPreconditionFailure(typing_extensions.TypedDict, total=False):
    violations: _list[GoogleRpcPreconditionFailureViolation]

@typing.type_check_only
class GoogleRpcPreconditionFailureViolation(typing_extensions.TypedDict, total=False):
    description: str
    subject: str
    type: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleTypeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
