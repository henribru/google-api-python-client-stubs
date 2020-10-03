import typing

import typing_extensions

class GoogleCloudApigeeV1EnvironmentGroupConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    hostnames: typing.List[str]
    routingRules: typing.List[GoogleCloudApigeeV1RoutingRule]
    revisionId: str
    uid: str

class GoogleCloudApigeeV1ResourceStatus(typing_extensions.TypedDict, total=False):
    resource: str
    totalReplicas: int
    uid: str
    revisions: typing.List[GoogleCloudApigeeV1RevisionStatus]

class GoogleCloudApigeeV1DateRange(typing_extensions.TypedDict, total=False):
    start: str
    end: str

class GoogleCloudApigeeV1ListEnvironmentGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    environmentGroups: typing.List[GoogleCloudApigeeV1EnvironmentGroup]
    nextPageToken: str

class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: GoogleIamV1Policy

class GoogleCloudApigeeV1ListEnvironmentResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    resourceFile: typing.List[GoogleCloudApigeeV1ResourceFile]

class GoogleCloudApigeeV1ResourceFiles(typing_extensions.TypedDict, total=False):
    resourceFile: typing.List[GoogleCloudApigeeV1ResourceFile]

class GoogleCloudApigeeV1CommonNameConfig(typing_extensions.TypedDict, total=False):
    name: str
    matchWildCards: bool

class GoogleCloudApigeeV1OperationGroup(typing_extensions.TypedDict, total=False):
    operationConfigs: typing.List[GoogleCloudApigeeV1OperationConfig]
    operationConfigType: str

class GoogleCloudApigeeV1Deployment(typing_extensions.TypedDict, total=False):
    apiProxy: str
    state: typing_extensions.Literal[
        "RUNTIME_STATE_UNSPECIFIED", "READY", "PROGRESSING", "ERROR"
    ]
    errors: typing.List[GoogleRpcStatus]
    environment: str
    pods: typing.List[GoogleCloudApigeeV1PodStatus]
    routeConflicts: typing.List[
        GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict
    ]
    revision: str
    deployStartTime: str
    instances: typing.List[GoogleCloudApigeeV1InstanceDeploymentStatus]

class GoogleCloudApigeeV1EnvironmentConfig(typing_extensions.TypedDict, total=False):
    flowhooks: typing.List[GoogleCloudApigeeV1FlowHookConfig]
    revisionId: str
    name: str
    sequenceNumber: str
    createTime: str
    resourceReferences: typing.List[GoogleCloudApigeeV1ReferenceConfig]
    traceConfig: GoogleCloudApigeeV1RuntimeTraceConfig
    provider: str
    deployments: typing.List[GoogleCloudApigeeV1DeploymentConfig]
    keystores: typing.List[GoogleCloudApigeeV1KeystoreConfig]
    uid: str
    resources: typing.List[GoogleCloudApigeeV1ResourceConfig]
    dataCollectors: typing.List[GoogleCloudApigeeV1DataCollectorConfig]
    debugMask: GoogleCloudApigeeV1DebugMask
    pubsubTopic: str
    featureFlags: typing.Dict[str, typing.Any]
    targets: typing.List[GoogleCloudApigeeV1TargetServerConfig]

class GoogleCloudApigeeV1Result(typing_extensions.TypedDict, total=False):
    ActionResult: str
    content: str
    statusCode: str
    properties: GoogleCloudApigeeV1Properties
    uRI: str
    accessList: typing.List[GoogleCloudApigeeV1Access]
    headers: typing.List[GoogleCloudApigeeV1Property]
    verb: str
    reasonPhrase: str
    timestamp: str

class GoogleCloudApigeeV1DebugSession(typing_extensions.TypedDict, total=False):
    tracesize: int
    count: int
    name: str
    validity: int
    timeout: str
    filter: str

class GoogleCloudApigeeV1GetSyncAuthorizationRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class GoogleCloudApigeeV1EnvironmentGroup(typing_extensions.TypedDict, total=False):
    lastModifiedAt: str
    createdAt: str
    name: str
    hostnames: typing.List[str]

class GoogleCloudApigeeV1DeploymentChangeReportRoutingChange(
    typing_extensions.TypedDict, total=False
):
    description: str
    shouldSequenceRollout: bool
    toDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment
    fromDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment
    environmentGroup: str

class GoogleCloudApigeeV1DeveloperApp(typing_extensions.TypedDict, total=False):
    createdAt: str
    name: str
    lastModifiedAt: str
    appFamily: str
    apiProducts: typing.List[str]
    developerId: str
    appId: str
    status: str
    keyExpiresIn: str
    scopes: typing.List[str]
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    callbackUrl: str
    credentials: typing.List[GoogleCloudApigeeV1Credential]

class GoogleCloudApigeeV1ListAppsResponse(typing_extensions.TypedDict, total=False):
    app: typing.List[GoogleCloudApigeeV1App]

class GoogleCloudApigeeV1Instance(typing_extensions.TypedDict, total=False):
    description: str
    host: str
    lastModifiedAt: str
    createdAt: str
    name: str
    port: str
    location: str
    displayName: str
    diskEncryptionKeyName: str

class GoogleCloudApigeeV1ServiceIssuersMapping(
    typing_extensions.TypedDict, total=False
):
    emailIds: typing.List[str]
    service: str

class GoogleCloudApigeeV1TargetServer(typing_extensions.TypedDict, total=False):
    name: str
    isEnabled: bool
    sSLInfo: GoogleCloudApigeeV1TlsInfo
    description: str
    host: str
    port: int

class GoogleCloudApigeeV1RuntimeTraceConfig(typing_extensions.TypedDict, total=False):
    endpoint: str
    exporter: typing_extensions.Literal["EXPORTER_UNSPECIFIED", "JAEGER", "CLOUD_TRACE"]
    samplingConfig: GoogleCloudApigeeV1RuntimeTraceSamplingConfig
    name: str
    revisionId: str
    overrides: typing.List[GoogleCloudApigeeV1RuntimeTraceConfigOverride]
    revisionCreateTime: str

class GoogleCloudApigeeV1ApiProxy(typing_extensions.TypedDict, total=False):
    metaData: GoogleCloudApigeeV1EntityMetadata
    latestRevisionId: str
    revision: typing.List[str]
    name: str

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool
    response: typing.Dict[str, typing.Any]
    error: GoogleRpcStatus

class GoogleCloudApigeeV1ListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[GoogleCloudApigeeV1Instance]
    nextPageToken: str

class GoogleCloudApigeeV1OptimizedStatsResponse(
    typing_extensions.TypedDict, total=False
):
    TimeUnit: typing.List[str]
    metaData: GoogleCloudApigeeV1Metadata
    stats: GoogleCloudApigeeV1OptimizedStatsNode
    resultTruncated: bool

class GoogleCloudApigeeV1AccessRemove(typing_extensions.TypedDict, total=False):
    success: bool
    name: str

class GoogleCloudApigeeV1ListOrganizationsResponse(
    typing_extensions.TypedDict, total=False
):
    organizations: typing.List[GoogleCloudApigeeV1OrganizationProjectMapping]

class GoogleCloudApigeeV1Metric(typing_extensions.TypedDict, total=False):
    values: typing.List[typing.Any]
    name: str

class GoogleCloudApigeeV1DataCollectorConfig(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "INTEGER", "FLOAT", "STRING", "BOOLEAN", "DATETIME"
    ]
    name: str

class GoogleCloudApigeeV1RuntimeTraceSamplingConfig(
    typing_extensions.TypedDict, total=False
):
    sampler: typing_extensions.Literal[
        "SAMPLER_UNSPECIFIED", "OFF", "ON", "PROBABILITY"
    ]
    errorSources: typing.List[str]
    responseCodeRanges: typing.List[
        GoogleCloudApigeeV1RuntimeTraceSamplingConfigResponseCodeRange
    ]
    samplingRate: float
    responseCodes: typing.List[int]

class GoogleCloudApigeeV1OperationMetadata(typing_extensions.TypedDict, total=False):
    targetResourceName: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "FINISHED"
    ]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "INSERT", "DELETE", "UPDATE"
    ]

class GoogleCloudApigeeV1ListExportsResponse(typing_extensions.TypedDict, total=False):
    exports: typing.List[GoogleCloudApigeeV1Export]

class GoogleCloudApigeeV1Credential(typing_extensions.TypedDict, total=False):
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    status: str
    issuedAt: str
    expiresAt: str
    consumerSecret: str
    consumerKey: str
    apiProducts: typing.List[GoogleCloudApigeeV1ApiProductRef]
    scopes: typing.List[str]

class GoogleCloudApigeeV1ResourceFile(typing_extensions.TypedDict, total=False):
    type: str
    name: str

class GoogleCloudApigeeV1ListDatastoresResponse(
    typing_extensions.TypedDict, total=False
):
    datastores: typing.List[GoogleCloudApigeeV1Datastore]

class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

class GoogleCloudApigeeV1DeveloperAppKey(typing_extensions.TypedDict, total=False):
    apiProducts: typing.List[typing.Any]
    issuedAt: str
    consumerSecret: str
    expiresAt: str
    scopes: typing.List[str]
    status: str
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    consumerKey: str

class GoogleCloudApigeeV1ReportInstanceStatusResponse(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudApigeeV1CustomReport(typing_extensions.TypedDict, total=False):
    createdAt: str
    toTime: str
    timeUnit: str
    organization: str
    fromTime: str
    properties: typing.List[GoogleCloudApigeeV1ReportProperty]
    comments: typing.List[str]
    limit: str
    filter: str
    tags: typing.List[str]
    sortByCols: typing.List[str]
    sortOrder: str
    lastViewedAt: str
    metrics: typing.List[GoogleCloudApigeeV1CustomReportMetric]
    dimensions: typing.List[str]
    lastModifiedAt: str
    environment: str
    displayName: str
    name: str
    topk: str
    chartType: str
    offset: str

class GoogleCloudApigeeV1RuntimeTraceConfigOverride(
    typing_extensions.TypedDict, total=False
):
    name: str
    revisionCreateTime: str
    uid: str
    revisionId: str
    samplingConfig: GoogleCloudApigeeV1RuntimeTraceSamplingConfig
    apiProxy: str

class GoogleCloudApigeeV1ReportInstanceStatusRequest(
    typing_extensions.TypedDict, total=False
):
    resources: typing.List[GoogleCloudApigeeV1ResourceStatus]
    reportTime: str
    instanceUid: str

class GoogleCloudApigeeV1Query(typing_extensions.TypedDict, total=False):
    name: str
    dimensions: typing.List[str]
    limit: int
    timeRange: typing.Any
    csvDelimiter: str
    outputFormat: str
    metrics: typing.List[GoogleCloudApigeeV1QueryMetric]
    filter: str
    groupByTimeUnit: str
    reportDefinitionId: str

class GoogleCloudApigeeV1RoutingRule(typing_extensions.TypedDict, total=False):
    environment: str
    basepath: str

class GoogleCloudApigeeV1ListSharedFlowsResponse(
    typing_extensions.TypedDict, total=False
):
    sharedFlows: typing.List[GoogleCloudApigeeV1SharedFlow]

class GoogleCloudApigeeV1Access(typing_extensions.TypedDict, total=False):
    Remove: GoogleCloudApigeeV1AccessRemove
    Set: GoogleCloudApigeeV1AccessSet
    Get: GoogleCloudApigeeV1AccessGet

class GoogleCloudApigeeV1EnvironmentGroupAttachment(
    typing_extensions.TypedDict, total=False
):
    name: str
    environment: str
    createdAt: str

class GoogleCloudApigeeV1ListOfDevelopersResponse(
    typing_extensions.TypedDict, total=False
):
    developer: typing.List[GoogleCloudApigeeV1Developer]

class GoogleCloudApigeeV1KeyValueMap(typing_extensions.TypedDict, total=False):
    name: str
    encrypted: bool

class GoogleCloudApigeeV1DeleteCustomReportResponse(
    typing_extensions.TypedDict, total=False
):
    message: str

class GoogleCloudApigeeV1RevisionStatus(typing_extensions.TypedDict, total=False):
    jsonSpec: str
    replicas: int
    errors: typing.List[GoogleCloudApigeeV1UpdateError]
    revisionId: str

class GoogleCloudApigeeV1ReferenceConfig(typing_extensions.TypedDict, total=False):
    resourceName: str
    name: str

class GoogleCloudApigeeV1Operation(typing_extensions.TypedDict, total=False):
    resource: str
    methods: typing.List[str]

class GoogleCloudApigeeV1QueryMetric(typing_extensions.TypedDict, total=False):
    alias: str
    value: str
    operator: str
    name: str
    function: str

class GoogleRpcPreconditionFailure(typing_extensions.TypedDict, total=False):
    violations: typing.List[GoogleRpcPreconditionFailureViolation]

class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    data: str
    contentType: str
    extensions: typing.List[typing.Dict[str, typing.Any]]

class GoogleCloudApigeeV1DatastoreConfig(typing_extensions.TypedDict, total=False):
    datasetName: str
    tablePrefix: str
    path: str
    projectId: str
    bucketName: str

class GoogleCloudApigeeV1Reference(typing_extensions.TypedDict, total=False):
    description: str
    refers: str
    name: str
    resourceType: str

class GoogleCloudApigeeV1Export(typing_extensions.TypedDict, total=False):
    name: str
    datastoreName: str
    error: str
    self: str
    created: str
    description: str
    executionTime: str
    state: str
    updated: str

class GoogleCloudApigeeV1ReportProperty(typing_extensions.TypedDict, total=False):
    value: typing.List[GoogleCloudApigeeV1Attribute]
    property: str

class GoogleCloudApigeeV1ListInstanceAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    attachments: typing.List[GoogleCloudApigeeV1InstanceAttachment]
    nextPageToken: str

class GoogleCloudApigeeV1ListApiProxiesResponse(
    typing_extensions.TypedDict, total=False
):
    proxies: typing.List[GoogleCloudApigeeV1ApiProxy]

class GoogleCloudApigeeV1SharedFlowRevision(typing_extensions.TypedDict, total=False):
    contextInfo: str
    entityMetaDataAsProperties: typing.Dict[str, typing.Any]
    resourceFiles: GoogleCloudApigeeV1ResourceFiles
    resources: typing.List[str]
    description: str
    displayName: str
    configurationVersion: GoogleCloudApigeeV1ConfigVersion
    revision: str
    type: str
    policies: typing.List[str]
    name: str
    lastModifiedAt: str
    createdAt: str
    sharedFlows: typing.List[str]

class GoogleCloudApigeeV1ResourceConfig(typing_extensions.TypedDict, total=False):
    location: str
    name: str

class GoogleCloudApigeeV1DebugMask(typing_extensions.TypedDict, total=False):
    responseXPaths: typing.List[str]
    responseJSONPaths: typing.List[str]
    variables: typing.List[str]
    faultJSONPaths: typing.List[str]
    namespaces: typing.Dict[str, typing.Any]
    requestXPaths: typing.List[str]
    name: str
    faultXPaths: typing.List[str]
    requestJSONPaths: typing.List[str]

class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class GoogleCloudApigeeV1Organization(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_TRIAL", "TYPE_PAID", "TYPE_INTERNAL"
    ]
    customerName: str
    caCertificate: str
    environments: typing.List[str]
    runtimeType: typing_extensions.Literal[
        "RUNTIME_TYPE_UNSPECIFIED", "CLOUD", "HYBRID"
    ]
    authorizedNetwork: str
    description: str
    createdAt: str
    lastModifiedAt: str
    analyticsRegion: str
    name: str
    projectId: str
    subscriptionType: typing_extensions.Literal[
        "SUBSCRIPTION_TYPE_UNSPECIFIED", "PAID", "TRIAL"
    ]
    displayName: str
    properties: GoogleCloudApigeeV1Properties
    attributes: typing.List[str]

class GoogleCloudApigeeV1AccessSet(typing_extensions.TypedDict, total=False):
    success: bool
    value: str
    name: str

class GoogleCloudApigeeV1Point(typing_extensions.TypedDict, total=False):
    results: typing.List[GoogleCloudApigeeV1Result]
    id: str

class GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute(
    typing_extensions.TypedDict, total=False
):
    environment: str
    envgroup: str
    percentage: int
    basepath: str

class GoogleCloudApigeeV1OptimizedStatsNode(typing_extensions.TypedDict, total=False):
    data: typing.List[typing.Any]

class GoogleCloudApigeeV1DimensionMetric(typing_extensions.TypedDict, total=False):
    name: str
    metrics: typing.List[GoogleCloudApigeeV1Metric]

class GoogleCloudApigeeV1SyncAuthorization(typing_extensions.TypedDict, total=False):
    etag: str
    identities: typing.List[str]

class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GoogleCloudApigeeV1Properties(typing_extensions.TypedDict, total=False):
    property: typing.List[GoogleCloudApigeeV1Property]

class GoogleCloudApigeeV1ListApiProductsResponse(
    typing_extensions.TypedDict, total=False
):
    apiProduct: typing.List[GoogleCloudApigeeV1ApiProduct]

class GoogleCloudApigeeV1TlsInfoCommonName(typing_extensions.TypedDict, total=False):
    wildcardMatch: bool
    value: str

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

class GoogleCloudApigeeV1Quota(typing_extensions.TypedDict, total=False):
    interval: str
    timeUnit: str
    limit: str

class GoogleCloudApigeeV1Keystore(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    name: str

class GoogleCloudApigeeV1TlsInfo(typing_extensions.TypedDict, total=False):
    keyStore: str
    protocols: typing.List[str]
    enabled: bool
    ciphers: typing.List[str]
    clientAuthEnabled: bool
    keyAlias: str
    commonName: GoogleCloudApigeeV1TlsInfoCommonName
    trustStore: str
    ignoreValidationErrors: bool

class GoogleCloudApigeeV1DeploymentConfig(typing_extensions.TypedDict, total=False):
    basePath: str
    proxyUid: str
    attributes: typing.Dict[str, typing.Any]
    location: str
    name: str
    uid: str

class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[GoogleIamV1Binding]
    etag: str
    auditConfigs: typing.List[GoogleIamV1AuditConfig]
    version: int

class GoogleCloudApigeeV1FlowHook(typing_extensions.TypedDict, total=False):
    continueOnError: bool
    description: str
    flowHookPoint: str
    sharedFlow: str

class GoogleCloudApigeeV1ListDebugSessionsResponse(
    typing_extensions.TypedDict, total=False
):
    sessions: typing.List[GoogleCloudApigeeV1Session]
    nextPageToken: str

class GoogleCloudApigeeV1TlsInfoConfig(typing_extensions.TypedDict, total=False):
    keyAlias: str
    trustStore: str
    commonName: GoogleCloudApigeeV1CommonNameConfig
    ignoreValidationErrors: bool
    ciphers: typing.List[str]
    enabled: bool
    protocols: typing.List[str]
    clientAuthEnabled: bool
    keyAliasReference: GoogleCloudApigeeV1KeyAliasReference

class GoogleCloudApigeeV1Attributes(typing_extensions.TypedDict, total=False):
    attribute: typing.List[GoogleCloudApigeeV1Attribute]

class GoogleCloudApigeeV1TestDatastoreResponse(
    typing_extensions.TypedDict, total=False
):
    error: str
    state: str

class GoogleCloudApigeeV1RuntimeTraceSamplingConfigResponseCodeRange(
    typing_extensions.TypedDict, total=False
):
    lastResponseCode: int
    firstResponseCode: int

class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GoogleCloudApigeeV1ListDeveloperAppsResponse(
    typing_extensions.TypedDict, total=False
):
    app: typing.List[GoogleCloudApigeeV1DeveloperApp]

class GoogleCloudApigeeV1AccessGet(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class GoogleCloudApigeeV1Alias(typing_extensions.TypedDict, total=False):
    certsInfo: GoogleCloudApigeeV1Certificate
    alias: str
    type: typing_extensions.Literal["ALIAS_TYPE_UNSPECIFIED", "CERT", "KEY_CERT"]

class GoogleCloudApigeeV1ConfigVersion(typing_extensions.TypedDict, total=False):
    majorVersion: int
    minorVersion: int

class GoogleCloudApigeeV1SchemaSchemaProperty(typing_extensions.TypedDict, total=False):
    type: str
    custom: str
    createTime: str

class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: GoogleTypeExpr
    role: str

class GoogleCloudApigeeV1IngressConfig(typing_extensions.TypedDict, total=False):
    name: str
    revisionId: str
    revisionCreateTime: str
    environmentGroups: typing.List[GoogleCloudApigeeV1EnvironmentGroupConfig]
    uid: str

class GoogleCloudApigeeV1Session(typing_extensions.TypedDict, total=False):
    timestampMs: str
    id: str

class GoogleCloudApigeeV1Schema(typing_extensions.TypedDict, total=False):
    meta: typing.List[str]
    metrics: typing.List[GoogleCloudApigeeV1SchemaSchemaElement]
    dimensions: typing.List[GoogleCloudApigeeV1SchemaSchemaElement]

class GoogleCloudApigeeV1InstanceAttachment(typing_extensions.TypedDict, total=False):
    createdAt: str
    name: str
    environment: str

class GoogleCloudApigeeV1ListCustomReportsResponse(
    typing_extensions.TypedDict, total=False
):
    qualifier: typing.List[GoogleCloudApigeeV1CustomReport]

class GoogleCloudApigeeV1ListAsyncQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    queries: typing.List[GoogleCloudApigeeV1AsyncQuery]

class GoogleCloudApigeeV1Subscription(typing_extensions.TypedDict, total=False):
    name: str

class GoogleCloudApigeeV1PodStatus(typing_extensions.TypedDict, total=False):
    podName: str
    statusCodeDetails: str
    appVersion: str
    deploymentStatusTime: str
    statusCode: str
    podStatusTime: str
    deploymentStatus: str
    podStatus: str
    deploymentTime: str

class GoogleCloudApigeeV1UpdateError(typing_extensions.TypedDict, total=False):
    type: str
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

class GoogleCloudApigeeV1Datastore(typing_extensions.TypedDict, total=False):
    targetType: str
    org: str
    lastUpdateTime: str
    datastoreConfig: GoogleCloudApigeeV1DatastoreConfig
    self: str
    displayName: str
    createTime: str

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[GoogleLongrunningOperation]
    nextPageToken: str

class GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict(
    typing_extensions.TypedDict, total=False
):
    environmentGroup: str
    conflictingDeployment: GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment
    description: str

class GoogleCloudApigeeV1KeystoreConfig(typing_extensions.TypedDict, total=False):
    name: str
    aliases: typing.List[GoogleCloudApigeeV1AliasRevisionConfig]

class GoogleCloudApigeeV1SharedFlow(typing_extensions.TypedDict, total=False):
    latestRevisionId: str
    metaData: GoogleCloudApigeeV1EntityMetadata
    name: str
    revision: typing.List[str]

class GoogleCloudApigeeV1OperationConfig(typing_extensions.TypedDict, total=False):
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    operations: typing.List[GoogleCloudApigeeV1Operation]
    apiSource: str
    quota: GoogleCloudApigeeV1Quota

class GoogleCloudApigeeV1App(typing_extensions.TypedDict, total=False):
    appId: str
    lastModifiedAt: str
    companyName: str
    keyExpiresIn: str
    developerId: str
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    createdAt: str
    apiProducts: typing.List[GoogleCloudApigeeV1ApiProductRef]
    status: str
    name: str
    scopes: typing.List[str]
    credentials: typing.List[GoogleCloudApigeeV1Credential]
    callbackUrl: str

class GoogleCloudApigeeV1SchemaSchemaElement(typing_extensions.TypedDict, total=False):
    properties: GoogleCloudApigeeV1SchemaSchemaProperty
    name: str

class GoogleCloudApigeeV1OrganizationProjectMapping(
    typing_extensions.TypedDict, total=False
):
    projectIds: typing.List[str]
    organization: str

class GoogleCloudApigeeV1DeploymentChangeReport(
    typing_extensions.TypedDict, total=False
):
    routingConflicts: typing.List[
        GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict
    ]
    routingChanges: typing.List[GoogleCloudApigeeV1DeploymentChangeReportRoutingChange]
    validationErrors: GoogleRpcPreconditionFailure

class GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment(
    typing_extensions.TypedDict, total=False
):
    basepath: str
    apiProxy: str
    revision: str
    environment: str

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environmentGroupAttachments: typing.List[
        GoogleCloudApigeeV1EnvironmentGroupAttachment
    ]
    nextPageToken: str

class GoogleCloudApigeeV1TargetServerConfig(typing_extensions.TypedDict, total=False):
    port: int
    tlsInfo: GoogleCloudApigeeV1TlsInfoConfig
    name: str
    host: str

class GoogleCloudApigeeV1CertInfo(typing_extensions.TypedDict, total=False):
    isValid: str
    validFrom: str
    expiryDate: str
    issuer: str
    serialNumber: str
    subjectAlternativeNames: typing.List[str]
    basicConstraints: str
    version: int
    publicKey: str
    sigAlgName: str
    subject: str

class GoogleCloudApigeeV1Metadata(typing_extensions.TypedDict, total=False):
    notices: typing.List[str]
    errors: typing.List[str]

class GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision(
    typing_extensions.TypedDict, total=False
):
    percentage: int
    revision: str

class GoogleCloudApigeeV1Developer(typing_extensions.TypedDict, total=False):
    email: str
    firstName: str
    accessType: str
    userName: str
    companies: typing.List[str]
    organizationName: str
    lastModifiedAt: str
    status: str
    developerId: str
    attributes: typing.List[GoogleCloudApigeeV1Attribute]
    lastName: str
    apps: typing.List[str]
    createdAt: str
    appFamily: str

class GoogleCloudApigeeV1CustomReportMetric(typing_extensions.TypedDict, total=False):
    name: str
    function: str

class GoogleCloudApigeeV1Stats(typing_extensions.TypedDict, total=False):
    environments: typing.List[GoogleCloudApigeeV1StatsEnvironmentStats]
    metaData: GoogleCloudApigeeV1Metadata

class GoogleCloudApigeeV1StatsEnvironmentStats(
    typing_extensions.TypedDict, total=False
):
    metrics: typing.List[GoogleCloudApigeeV1Metric]
    dimensions: typing.List[GoogleCloudApigeeV1DimensionMetric]
    name: str

class GoogleCloudApigeeV1AsyncQueryResult(typing_extensions.TypedDict, total=False):
    self: str
    expires: str

class GoogleCloudApigeeV1ExportRequest(typing_extensions.TypedDict, total=False):
    outputFormat: str
    description: str
    csvDelimiter: str
    dateRange: GoogleCloudApigeeV1DateRange
    datastoreName: str
    name: str

class GoogleCloudApigeeV1Certificate(typing_extensions.TypedDict, total=False):
    certInfo: typing.List[GoogleCloudApigeeV1CertInfo]

class GoogleCloudApigeeV1QueryMetadata(typing_extensions.TypedDict, total=False):
    endTimestamp: str
    outputFormat: str
    startTimestamp: str
    timeUnit: str
    metrics: typing.List[str]
    dimensions: typing.List[str]

class GoogleCloudApigeeV1ListHybridIssuersResponse(
    typing_extensions.TypedDict, total=False
):
    issuers: typing.List[GoogleCloudApigeeV1ServiceIssuersMapping]

class GoogleCloudApigeeV1OptimizedStats(typing_extensions.TypedDict, total=False):
    Response: GoogleCloudApigeeV1OptimizedStatsResponse

class GoogleCloudApigeeV1ApiProduct(typing_extensions.TypedDict, total=False):
    quota: str
    quotaInterval: str
    environments: typing.List[str]
    quotaTimeUnit: str
    createdAt: str
    displayName: str
    description: str
    operationGroup: GoogleCloudApigeeV1OperationGroup
    name: str
    apiResources: typing.List[str]
    lastModifiedAt: str
    scopes: typing.List[str]
    approvalType: str
    proxies: typing.List[str]
    attributes: typing.List[GoogleCloudApigeeV1Attribute]

class GoogleCloudApigeeV1ListDeploymentsResponse(
    typing_extensions.TypedDict, total=False
):
    deployments: typing.List[GoogleCloudApigeeV1Deployment]

class GoogleCloudApigeeV1AliasRevisionConfig(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal["ALIAS_TYPE_UNSPECIFIED", "CERT", "KEY_CERT"]
    location: str

class GoogleCloudApigeeV1Property(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[GoogleIamV1AuditLogConfig]

class GoogleCloudApigeeV1KeyAliasReference(typing_extensions.TypedDict, total=False):
    reference: str
    aliasId: str

class GoogleCloudApigeeV1FlowHookConfig(typing_extensions.TypedDict, total=False):
    continueOnError: bool
    sharedFlowName: str
    name: str

class GoogleCloudApigeeV1ApiProxyRevision(typing_extensions.TypedDict, total=False):
    targets: typing.List[str]
    policies: typing.List[str]
    name: str
    proxyEndpoints: typing.List[str]
    type: str
    spec: str
    sharedFlows: typing.List[str]
    teams: typing.List[str]
    createdAt: str
    resourceFiles: GoogleCloudApigeeV1ResourceFiles
    basepaths: typing.List[str]
    proxies: typing.List[str]
    resources: typing.List[str]
    description: str
    targetServers: typing.List[str]
    configurationVersion: GoogleCloudApigeeV1ConfigVersion
    revision: str
    displayName: str
    lastModifiedAt: str
    contextInfo: str
    targetEndpoints: typing.List[str]
    entityMetaDataAsProperties: typing.Dict[str, typing.Any]

class GoogleCloudApigeeV1ApiProductRef(typing_extensions.TypedDict, total=False):
    apiproduct: str
    status: str

class GoogleCloudApigeeV1DebugSessionTransaction(
    typing_extensions.TypedDict, total=False
):
    completed: bool
    point: typing.List[GoogleCloudApigeeV1Point]

class GoogleCloudApigeeV1Attribute(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class GoogleCloudApigeeV1AsyncQuery(typing_extensions.TypedDict, total=False):
    error: str
    reportDefinitionId: str
    state: str
    result: GoogleCloudApigeeV1AsyncQueryResult
    executionTime: str
    created: str
    resultFileSize: str
    queryParams: GoogleCloudApigeeV1QueryMetadata
    updated: str
    self: str
    resultRows: str
    name: str

class GoogleCloudApigeeV1Environment(typing_extensions.TypedDict, total=False):
    displayName: str
    lastModifiedAt: str
    description: str
    name: str
    properties: GoogleCloudApigeeV1Properties
    createdAt: str

class GoogleRpcPreconditionFailureViolation(typing_extensions.TypedDict, total=False):
    type: str
    description: str
    subject: str

class GoogleCloudApigeeV1EntityMetadata(typing_extensions.TypedDict, total=False):
    createdAt: str
    subType: str
    lastModifiedAt: str
