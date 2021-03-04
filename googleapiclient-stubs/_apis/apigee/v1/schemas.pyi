import typing

import typing_extensions
@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]

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
class GoogleCloudApigeeV1ApiCategory(typing_extensions.TypedDict, total=False):
    data: GoogleCloudApigeeV1ApiCategoryData
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiCategoryData(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    siteId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProduct(typing_extensions.TypedDict, total=False):
    apiResources: typing.List[str]
    approvalType: str
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    createdAt: str
    description: str
    displayName: str
    environments: typing.List[str]
    lastModifiedAt: str
    name: str
    operationGroup: GoogleCloudApigeeV1OperationGroup
    proxies: typing.List[str]
    quota: str
    quotaInterval: str
    quotaTimeUnit: str
    scopes: typing.List[str]

@typing.type_check_only
class GoogleCloudApigeeV1ApiProductRef(typing_extensions.TypedDict, total=False):
    apiproduct: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxy(typing_extensions.TypedDict, total=False):
    latestRevisionId: str
    metaData: GoogleCloudApigeeV1EntityMetadata
    name: str
    revision: typing.List[str]

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxyRevision(typing_extensions.TypedDict, total=False):
    basepaths: typing.List[str]
    configurationVersion: GoogleCloudApigeeV1ConfigVersion
    contextInfo: str
    createdAt: str
    description: str
    displayName: str
    entityMetaDataAsProperties: typing.Dict[str, typing.Any]
    lastModifiedAt: str
    name: str
    policies: typing.List[str]
    proxies: typing.List[str]
    proxyEndpoints: typing.List[str]
    resourceFiles: GoogleCloudApigeeV1ResourceFiles
    resources: typing.List[str]
    revision: str
    sharedFlows: typing.List[str]
    spec: str
    targetEndpoints: typing.List[str]
    targetServers: typing.List[str]
    targets: typing.List[str]
    teams: typing.List[str]
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1ApiResponseWrapper(typing_extensions.TypedDict, total=False):
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1App(typing_extensions.TypedDict, total=False):
    apiProducts: typing.List[GoogleCloudApigeeV1ApiProductRef]
    appId: str
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    callbackUrl: str
    companyName: str
    createdAt: str
    credentials: typing.List[GoogleCloudApigeeV1Credential]
    developerId: str
    keyExpiresIn: str
    lastModifiedAt: str
    name: str
    scopes: typing.List[str]
    status: str

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
    rows: typing.List[typing.Any]
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1Attribute(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudApigeeV1Attributes(typing_extensions.TypedDict, total=False):
    attribute: typing.List[GoogleCloudApigeeV1Attribute]

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
    subjectAlternativeNames: typing.List[str]
    validFrom: str
    version: int

@typing.type_check_only
class GoogleCloudApigeeV1Certificate(typing_extensions.TypedDict, total=False):
    certInfo: typing.List[GoogleCloudApigeeV1CertInfo]

@typing.type_check_only
class GoogleCloudApigeeV1CommonNameConfig(typing_extensions.TypedDict, total=False):
    matchWildCards: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ConfigVersion(typing_extensions.TypedDict, total=False):
    majorVersion: int
    minorVersion: int

@typing.type_check_only
class GoogleCloudApigeeV1Credential(typing_extensions.TypedDict, total=False):
    apiProducts: typing.List[GoogleCloudApigeeV1ApiProductRef]
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    consumerKey: str
    consumerSecret: str
    expiresAt: str
    issuedAt: str
    scopes: typing.List[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1CustomReport(typing_extensions.TypedDict, total=False):
    chartType: str
    comments: typing.List[str]
    createdAt: str
    dimensions: typing.List[str]
    displayName: str
    environment: str
    filter: str
    fromTime: str
    lastModifiedAt: str
    lastViewedAt: str
    limit: str
    metrics: typing.List[GoogleCloudApigeeV1CustomReportMetric]
    name: str
    offset: str
    organization: str
    properties: typing.List[GoogleCloudApigeeV1ReportProperty]
    sortByCols: typing.List[str]
    sortOrder: str
    tags: typing.List[str]
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
    faultJSONPaths: typing.List[str]
    faultXPaths: typing.List[str]
    name: str
    namespaces: typing.Dict[str, typing.Any]
    requestJSONPaths: typing.List[str]
    requestXPaths: typing.List[str]
    responseJSONPaths: typing.List[str]
    responseXPaths: typing.List[str]
    variables: typing.List[str]

@typing.type_check_only
class GoogleCloudApigeeV1DebugSession(typing_extensions.TypedDict, total=False):
    count: int
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
    point: typing.List[GoogleCloudApigeeV1Point]

@typing.type_check_only
class GoogleCloudApigeeV1DeleteCustomReportResponse(
    typing_extensions.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudApigeeV1Deployment(typing_extensions.TypedDict, total=False):
    apiProxy: str
    deployStartTime: str
    environment: str
    errors: typing.List[GoogleRpcStatus]
    instances: typing.List[GoogleCloudApigeeV1InstanceDeploymentStatus]
    pods: typing.List[GoogleCloudApigeeV1PodStatus]
    revision: str
    routeConflicts: typing.List[
        GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict
    ]
    state: typing_extensions.Literal[
        "RUNTIME_STATE_UNSPECIFIED", "READY", "PROGRESSING", "ERROR"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReport(
    typing_extensions.TypedDict, total=False
):
    routingChanges: typing.List[GoogleCloudApigeeV1DeploymentChangeReportRoutingChange]
    routingConflicts: typing.List[
        GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict
    ]
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
    attributes: typing.Dict[str, typing.Any]
    basePath: str
    location: str
    name: str
    proxyUid: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Developer(typing_extensions.TypedDict, total=False):
    accessType: str
    appFamily: str
    apps: typing.List[str]
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    companies: typing.List[str]
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
    apiProducts: typing.List[str]
    appFamily: str
    appId: str
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    callbackUrl: str
    createdAt: str
    credentials: typing.List[GoogleCloudApigeeV1Credential]
    developerId: str
    keyExpiresIn: str
    lastModifiedAt: str
    name: str
    scopes: typing.List[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperAppKey(typing_extensions.TypedDict, total=False):
    apiProducts: typing.List[typing.Any]
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    consumerKey: str
    consumerSecret: str
    expiresAt: str
    expiresInSeconds: str
    issuedAt: str
    scopes: typing.List[str]
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1DimensionMetric(typing_extensions.TypedDict, total=False):
    metrics: typing.List[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1EntityMetadata(typing_extensions.TypedDict, total=False):
    createdAt: str
    lastModifiedAt: str
    subType: str

@typing.type_check_only
class GoogleCloudApigeeV1Environment(typing_extensions.TypedDict, total=False):
    createdAt: str
    description: str
    displayName: str
    lastModifiedAt: str
    name: str
    properties: GoogleCloudApigeeV1Properties
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    dataCollectors: typing.List[GoogleCloudApigeeV1DataCollectorConfig]
    debugMask: GoogleCloudApigeeV1DebugMask
    deployments: typing.List[GoogleCloudApigeeV1DeploymentConfig]
    featureFlags: typing.Dict[str, typing.Any]
    flowhooks: typing.List[GoogleCloudApigeeV1FlowHookConfig]
    keystores: typing.List[GoogleCloudApigeeV1KeystoreConfig]
    name: str
    provider: str
    pubsubTopic: str
    resourceReferences: typing.List[GoogleCloudApigeeV1ReferenceConfig]
    resources: typing.List[GoogleCloudApigeeV1ResourceConfig]
    revisionId: str
    sequenceNumber: str
    targets: typing.List[GoogleCloudApigeeV1TargetServerConfig]
    traceConfig: GoogleCloudApigeeV1RuntimeTraceConfig
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroup(typing_extensions.TypedDict, total=False):
    createdAt: str
    hostnames: typing.List[str]
    lastModifiedAt: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupAttachment(
    typing_extensions.TypedDict, total=False
):
    createdAt: str
    environment: str
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupConfig(
    typing_extensions.TypedDict, total=False
):
    hostnames: typing.List[str]
    name: str
    revisionId: str
    routingRules: typing.List[GoogleCloudApigeeV1RoutingRule]
    uid: str

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
class GoogleCloudApigeeV1GetSyncAuthorizationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1IngressConfig(typing_extensions.TypedDict, total=False):
    environmentGroups: typing.List[GoogleCloudApigeeV1EnvironmentGroupConfig]
    name: str
    revisionCreateTime: str
    revisionId: str
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Instance(typing_extensions.TypedDict, total=False):
    createdAt: str
    description: str
    diskEncryptionKeyName: str
    displayName: str
    host: str
    lastModifiedAt: str
    location: str
    name: str
    peeringCidrRange: typing_extensions.Literal[
        "CIDR_RANGE_UNSPECIFIED", "SLASH_16", "SLASH_20"
    ]
    port: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
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
    deployedRevisions: typing.List[
        GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision
    ]
    deployedRoutes: typing.List[
        GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute
    ]
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
class GoogleCloudApigeeV1KeyAliasReference(typing_extensions.TypedDict, total=False):
    aliasId: str
    reference: str

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueMap(typing_extensions.TypedDict, total=False):
    encrypted: bool
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1Keystore(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1KeystoreConfig(typing_extensions.TypedDict, total=False):
    aliases: typing.List[GoogleCloudApigeeV1AliasRevisionConfig]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiCategoriesResponse(
    typing_extensions.TypedDict, total=False
):
    data: typing.List[GoogleCloudApigeeV1ApiCategoryData]
    errorCode: str
    message: str
    requestId: str
    status: str

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProductsResponse(
    typing_extensions.TypedDict, total=False
):
    apiProduct: typing.List[GoogleCloudApigeeV1ApiProduct]

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProxiesResponse(
    typing_extensions.TypedDict, total=False
):
    proxies: typing.List[GoogleCloudApigeeV1ApiProxy]

@typing.type_check_only
class GoogleCloudApigeeV1ListAppsResponse(typing_extensions.TypedDict, total=False):
    app: typing.List[GoogleCloudApigeeV1App]

@typing.type_check_only
class GoogleCloudApigeeV1ListAsyncQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    queries: typing.List[GoogleCloudApigeeV1AsyncQuery]

@typing.type_check_only
class GoogleCloudApigeeV1ListCustomReportsResponse(
    typing_extensions.TypedDict, total=False
):
    qualifier: typing.List[GoogleCloudApigeeV1CustomReport]

@typing.type_check_only
class GoogleCloudApigeeV1ListDataCollectorsResponse(
    typing_extensions.TypedDict, total=False
):
    dataCollectors: typing.List[GoogleCloudApigeeV1DataCollector]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListDatastoresResponse(
    typing_extensions.TypedDict, total=False
):
    datastores: typing.List[GoogleCloudApigeeV1Datastore]

@typing.type_check_only
class GoogleCloudApigeeV1ListDebugSessionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessions: typing.List[GoogleCloudApigeeV1Session]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeploymentsResponse(
    typing_extensions.TypedDict, total=False
):
    deployments: typing.List[GoogleCloudApigeeV1Deployment]

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperAppsResponse(
    typing_extensions.TypedDict, total=False
):
    app: typing.List[GoogleCloudApigeeV1DeveloperApp]

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environmentGroupAttachments: typing.List[
        GoogleCloudApigeeV1EnvironmentGroupAttachment
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    environmentGroups: typing.List[GoogleCloudApigeeV1EnvironmentGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    resourceFile: typing.List[GoogleCloudApigeeV1ResourceFile]

@typing.type_check_only
class GoogleCloudApigeeV1ListExportsResponse(typing_extensions.TypedDict, total=False):
    exports: typing.List[GoogleCloudApigeeV1Export]

@typing.type_check_only
class GoogleCloudApigeeV1ListHybridIssuersResponse(
    typing_extensions.TypedDict, total=False
):
    issuers: typing.List[GoogleCloudApigeeV1ServiceIssuersMapping]

@typing.type_check_only
class GoogleCloudApigeeV1ListInstanceAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    attachments: typing.List[GoogleCloudApigeeV1InstanceAttachment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[GoogleCloudApigeeV1Instance]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListNatAddressesResponse(
    typing_extensions.TypedDict, total=False
):
    natAddresses: typing.List[GoogleCloudApigeeV1NatAddress]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApigeeV1ListOfDevelopersResponse(
    typing_extensions.TypedDict, total=False
):
    developer: typing.List[GoogleCloudApigeeV1Developer]

@typing.type_check_only
class GoogleCloudApigeeV1ListOrganizationsResponse(
    typing_extensions.TypedDict, total=False
):
    organizations: typing.List[GoogleCloudApigeeV1OrganizationProjectMapping]

@typing.type_check_only
class GoogleCloudApigeeV1ListSharedFlowsResponse(
    typing_extensions.TypedDict, total=False
):
    sharedFlows: typing.List[GoogleCloudApigeeV1SharedFlow]

@typing.type_check_only
class GoogleCloudApigeeV1ListTraceConfigOverridesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    traceConfigOverrides: typing.List[GoogleCloudApigeeV1TraceConfigOverride]

@typing.type_check_only
class GoogleCloudApigeeV1Metadata(typing_extensions.TypedDict, total=False):
    errors: typing.List[str]
    notices: typing.List[str]

@typing.type_check_only
class GoogleCloudApigeeV1Metric(typing_extensions.TypedDict, total=False):
    name: str
    values: typing.List[typing.Any]

@typing.type_check_only
class GoogleCloudApigeeV1NatAddress(typing_extensions.TypedDict, total=False):
    ipAddress: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RESERVED", "ACTIVE", "DELETING"
    ]

@typing.type_check_only
class GoogleCloudApigeeV1Operation(typing_extensions.TypedDict, total=False):
    methods: typing.List[str]
    resource: str

@typing.type_check_only
class GoogleCloudApigeeV1OperationConfig(typing_extensions.TypedDict, total=False):
    apiSource: str
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    operations: typing.List[GoogleCloudApigeeV1Operation]
    quota: GoogleCloudApigeeV1Quota

@typing.type_check_only
class GoogleCloudApigeeV1OperationGroup(typing_extensions.TypedDict, total=False):
    operationConfigType: str
    operationConfigs: typing.List[GoogleCloudApigeeV1OperationConfig]

@typing.type_check_only
class GoogleCloudApigeeV1OperationMetadata(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "INSERT", "DELETE", "UPDATE"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "FINISHED"
    ]
    targetResourceName: str

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStats(typing_extensions.TypedDict, total=False):
    Response: GoogleCloudApigeeV1OptimizedStatsResponse

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsNode(typing_extensions.TypedDict, total=False):
    data: typing.List[typing.Any]

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsResponse(
    typing_extensions.TypedDict, total=False
):
    TimeUnit: typing.List[str]
    metaData: GoogleCloudApigeeV1Metadata
    resultTruncated: bool
    stats: GoogleCloudApigeeV1OptimizedStatsNode

@typing.type_check_only
class GoogleCloudApigeeV1Organization(typing_extensions.TypedDict, total=False):
    analyticsRegion: str
    attributes: typing.List[str]
    authorizedNetwork: str
    billingType: typing_extensions.Literal[
        "BILLING_TYPE_UNSPECIFIED", "SUBSCRIPTION", "EVALUATION"
    ]
    caCertificate: str
    createdAt: str
    customerName: str
    description: str
    displayName: str
    environments: typing.List[str]
    expiresAt: str
    lastModifiedAt: str
    name: str
    projectId: str
    properties: GoogleCloudApigeeV1Properties
    runtimeDatabaseEncryptionKeyName: str
    runtimeType: typing_extensions.Literal[
        "RUNTIME_TYPE_UNSPECIFIED", "CLOUD", "HYBRID"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
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
    organization: str
    projectIds: typing.List[str]

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
    results: typing.List[GoogleCloudApigeeV1Result]

@typing.type_check_only
class GoogleCloudApigeeV1Properties(typing_extensions.TypedDict, total=False):
    property: typing.List[GoogleCloudApigeeV1Property]

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
    runtimeLocation: str

@typing.type_check_only
class GoogleCloudApigeeV1Query(typing_extensions.TypedDict, total=False):
    csvDelimiter: str
    dimensions: typing.List[str]
    envgroupHostname: str
    filter: str
    groupByTimeUnit: str
    limit: int
    metrics: typing.List[GoogleCloudApigeeV1QueryMetric]
    name: str
    outputFormat: str
    reportDefinitionId: str
    timeRange: typing.Any

@typing.type_check_only
class GoogleCloudApigeeV1QueryMetadata(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[str]
    endTimestamp: str
    metrics: typing.List[str]
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
class GoogleCloudApigeeV1Quota(typing_extensions.TypedDict, total=False):
    interval: str
    limit: str
    timeUnit: str

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
    resources: typing.List[GoogleCloudApigeeV1ResourceStatus]

@typing.type_check_only
class GoogleCloudApigeeV1ReportInstanceStatusResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApigeeV1ReportProperty(typing_extensions.TypedDict, total=False):
    property: str
    value: typing.List[GoogleCloudApigeeV1Attribute]

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
    resourceFile: typing.List[GoogleCloudApigeeV1ResourceFile]

@typing.type_check_only
class GoogleCloudApigeeV1ResourceStatus(typing_extensions.TypedDict, total=False):
    resource: str
    revisions: typing.List[GoogleCloudApigeeV1RevisionStatus]
    totalReplicas: int
    uid: str

@typing.type_check_only
class GoogleCloudApigeeV1Result(typing_extensions.TypedDict, total=False):
    ActionResult: str
    accessList: typing.List[GoogleCloudApigeeV1Access]
    content: str
    headers: typing.List[GoogleCloudApigeeV1Property]
    properties: GoogleCloudApigeeV1Properties
    reasonPhrase: str
    statusCode: str
    timestamp: str
    uRI: str
    verb: str

@typing.type_check_only
class GoogleCloudApigeeV1RevisionStatus(typing_extensions.TypedDict, total=False):
    errors: typing.List[GoogleCloudApigeeV1UpdateError]
    jsonSpec: str
    replicas: int
    revisionId: str

@typing.type_check_only
class GoogleCloudApigeeV1RoutingRule(typing_extensions.TypedDict, total=False):
    basepath: str
    envGroupRevision: str
    environment: str
    receiver: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeTraceConfig(typing_extensions.TypedDict, total=False):
    endpoint: str
    exporter: typing_extensions.Literal["EXPORTER_UNSPECIFIED", "JAEGER", "CLOUD_TRACE"]
    name: str
    overrides: typing.List[GoogleCloudApigeeV1RuntimeTraceConfigOverride]
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
    dimensions: typing.List[GoogleCloudApigeeV1SchemaSchemaElement]
    meta: typing.List[str]
    metrics: typing.List[GoogleCloudApigeeV1SchemaSchemaElement]

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
class GoogleCloudApigeeV1ServiceIssuersMapping(
    typing_extensions.TypedDict, total=False
):
    emailIds: typing.List[str]
    service: str

@typing.type_check_only
class GoogleCloudApigeeV1Session(typing_extensions.TypedDict, total=False):
    id: str
    timestampMs: str

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlow(typing_extensions.TypedDict, total=False):
    latestRevisionId: str
    metaData: GoogleCloudApigeeV1EntityMetadata
    name: str
    revision: typing.List[str]

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlowRevision(typing_extensions.TypedDict, total=False):
    configurationVersion: GoogleCloudApigeeV1ConfigVersion
    contextInfo: str
    createdAt: str
    description: str
    displayName: str
    entityMetaDataAsProperties: typing.Dict[str, typing.Any]
    lastModifiedAt: str
    name: str
    policies: typing.List[str]
    resourceFiles: GoogleCloudApigeeV1ResourceFiles
    resources: typing.List[str]
    revision: str
    sharedFlows: typing.List[str]
    type: str

@typing.type_check_only
class GoogleCloudApigeeV1Stats(typing_extensions.TypedDict, total=False):
    environments: typing.List[GoogleCloudApigeeV1StatsEnvironmentStats]
    hosts: typing.List[GoogleCloudApigeeV1StatsHostStats]
    metaData: GoogleCloudApigeeV1Metadata

@typing.type_check_only
class GoogleCloudApigeeV1StatsEnvironmentStats(
    typing_extensions.TypedDict, total=False
):
    dimensions: typing.List[GoogleCloudApigeeV1DimensionMetric]
    metrics: typing.List[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1StatsHostStats(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[GoogleCloudApigeeV1DimensionMetric]
    metrics: typing.List[GoogleCloudApigeeV1Metric]
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1Subscription(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudApigeeV1SyncAuthorization(typing_extensions.TypedDict, total=False):
    etag: str
    identities: typing.List[str]

@typing.type_check_only
class GoogleCloudApigeeV1TargetServer(typing_extensions.TypedDict, total=False):
    description: str
    host: str
    isEnabled: bool
    name: str
    port: int
    sSLInfo: GoogleCloudApigeeV1TlsInfo

@typing.type_check_only
class GoogleCloudApigeeV1TargetServerConfig(typing_extensions.TypedDict, total=False):
    host: str
    name: str
    port: int
    tlsInfo: GoogleCloudApigeeV1TlsInfoConfig

@typing.type_check_only
class GoogleCloudApigeeV1TestDatastoreResponse(
    typing_extensions.TypedDict, total=False
):
    error: str
    state: str

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfo(typing_extensions.TypedDict, total=False):
    ciphers: typing.List[str]
    clientAuthEnabled: bool
    commonName: GoogleCloudApigeeV1TlsInfoCommonName
    enabled: bool
    ignoreValidationErrors: bool
    keyAlias: str
    keyStore: str
    protocols: typing.List[str]
    trustStore: str

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfoCommonName(typing_extensions.TypedDict, total=False):
    value: str
    wildcardMatch: bool

@typing.type_check_only
class GoogleCloudApigeeV1TlsInfoConfig(typing_extensions.TypedDict, total=False):
    ciphers: typing.List[str]
    clientAuthEnabled: bool
    commonName: GoogleCloudApigeeV1CommonNameConfig
    enabled: bool
    ignoreValidationErrors: bool
    keyAlias: str
    keyAliasReference: GoogleCloudApigeeV1KeyAliasReference
    protocols: typing.List[str]
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
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: typing.List[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[GoogleIamV1AuditConfig]
    bindings: typing.List[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcPreconditionFailure(typing_extensions.TypedDict, total=False):
    violations: typing.List[GoogleRpcPreconditionFailureViolation]

@typing.type_check_only
class GoogleRpcPreconditionFailureViolation(typing_extensions.TypedDict, total=False):
    description: str
    subject: str
    type: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
