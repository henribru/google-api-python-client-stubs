import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApihubV1APIMetadata(typing.TypedDict, total=False):
    api: GoogleCloudApihubV1Api
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str
    versions: _list[GoogleCloudApihubV1VersionMetadata]

@typing.type_check_only
class GoogleCloudApihubV1ActionExecutionDetail(typing.TypedDict, total=False):
    actionId: str

@typing.type_check_only
class GoogleCloudApihubV1AdditionalSpecContent(typing.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    specContentType: typing.Literal[
        "SPEC_CONTENT_TYPE_UNSPECIFIED", "BOOSTED_SPEC_CONTENT", "GATEWAY_OPEN_API_SPEC"
    ]
    specContents: GoogleCloudApihubV1SpecContents
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1Addon(typing.TypedDict, total=False):
    config: GoogleCloudApihubV1AddonConfig
    createTime: str
    dataSource: typing.Literal["DATA_SOURCE_UNSPECIFIED", "PLUGIN_INSTANCE", "ALL_DATA"]
    description: str
    displayName: str
    name: str
    state: typing.Literal[
        "ADDON_STATE_UNSPECIFIED", "ACTIVE", "UPDATING", "ERROR", "INACTIVE"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1AddonConfig(typing.TypedDict, total=False):
    allDataAddonConfig: GoogleCloudApihubV1AllDataAddonConfig
    gatewayPluginAddonConfig: GoogleCloudApihubV1GatewayPluginAddonConfig

@typing.type_check_only
class GoogleCloudApihubV1AgentRegistrySyncConfig(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class GoogleCloudApihubV1AllDataAddonConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudApihubV1AllowedValue(typing.TypedDict, total=False):
    description: str
    displayName: str
    id: str
    immutable: bool

@typing.type_check_only
class GoogleCloudApihubV1Api(typing.TypedDict, total=False):
    apiFunctionalRequirements: GoogleCloudApihubV1AttributeValues
    apiRequirements: GoogleCloudApihubV1AttributeValues
    apiStyle: GoogleCloudApihubV1AttributeValues
    apiTechnicalRequirements: GoogleCloudApihubV1AttributeValues
    attributes: dict[str, typing.Any]
    businessUnit: GoogleCloudApihubV1AttributeValues
    createTime: str
    description: str
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    fingerprint: str
    maturityLevel: GoogleCloudApihubV1AttributeValues
    name: str
    owner: GoogleCloudApihubV1Owner
    selectedVersion: str
    sourceMetadata: _list[GoogleCloudApihubV1SourceMetadata]
    targetUser: GoogleCloudApihubV1AttributeValues
    team: GoogleCloudApihubV1AttributeValues
    updateTime: str
    versions: _list[str]

@typing.type_check_only
class GoogleCloudApihubV1ApiData(typing.TypedDict, total=False):
    apiMetadataList: GoogleCloudApihubV1ApiMetadataList

@typing.type_check_only
class GoogleCloudApihubV1ApiHubInstance(typing.TypedDict, total=False):
    config: GoogleCloudApihubV1Config
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "INACTIVE",
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1ApiHubResource(typing.TypedDict, total=False):
    api: GoogleCloudApihubV1Api
    definition: GoogleCloudApihubV1Definition
    deployment: GoogleCloudApihubV1Deployment
    operation: GoogleCloudApihubV1ApiOperation
    spec: GoogleCloudApihubV1Spec
    version: GoogleCloudApihubV1Version

@typing.type_check_only
class GoogleCloudApihubV1ApiKeyConfig(typing.TypedDict, total=False):
    apiKey: GoogleCloudApihubV1Secret
    httpElementLocation: typing.Literal[
        "HTTP_ELEMENT_LOCATION_UNSPECIFIED", "QUERY", "HEADER", "PATH", "BODY", "COOKIE"
    ]
    name: str

@typing.type_check_only
class GoogleCloudApihubV1ApiMetadataList(typing.TypedDict, total=False):
    apiMetadata: _list[GoogleCloudApihubV1APIMetadata]

@typing.type_check_only
class GoogleCloudApihubV1ApiOperation(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    createTime: str
    details: GoogleCloudApihubV1OperationDetails
    name: str
    sourceMetadata: _list[GoogleCloudApihubV1SourceMetadata]
    spec: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1ApiView(typing.TypedDict, total=False):
    mcpServerView: GoogleCloudApihubV1FlattenedApiVersionDeploymentView
    mcpToolView: GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView

@typing.type_check_only
class GoogleCloudApihubV1ApigeeEdgeConfig(typing.TypedDict, total=False):
    environmentFilter: GoogleCloudApihubV1EnvironmentFilter

@typing.type_check_only
class GoogleCloudApihubV1ApigeeOPDKConfig(typing.TypedDict, total=False):
    environmentFilter: GoogleCloudApihubV1EnvironmentFilter

@typing.type_check_only
class GoogleCloudApihubV1ApigeeXHybridConfig(typing.TypedDict, total=False):
    environmentFilter: GoogleCloudApihubV1EnvironmentFilter

@typing.type_check_only
class GoogleCloudApihubV1ApigeeXTargetDetails(typing.TypedDict, total=False):
    deployedRevision: str
    environment: str
    metadata: GoogleCloudApihubV1MetaData
    proxy: str
    targetProject: str

@typing.type_check_only
class GoogleCloudApihubV1ApplicationIntegrationEndpointDetails(
    typing.TypedDict, total=False
):
    triggerId: str
    uri: str

@typing.type_check_only
class GoogleCloudApihubV1Attribute(typing.TypedDict, total=False):
    allowedValues: _list[GoogleCloudApihubV1AllowedValue]
    cardinality: int
    createTime: str
    dataType: typing.Literal["DATA_TYPE_UNSPECIFIED", "ENUM", "JSON", "STRING", "URI"]
    definitionType: typing.Literal[
        "DEFINITION_TYPE_UNSPECIFIED", "SYSTEM_DEFINED", "USER_DEFINED"
    ]
    description: str
    displayName: str
    mandatory: bool
    name: str
    scope: typing.Literal[
        "SCOPE_UNSPECIFIED",
        "API",
        "VERSION",
        "SPEC",
        "API_OPERATION",
        "DEPLOYMENT",
        "DEPENDENCY",
        "DEFINITION",
        "EXTERNAL_API",
        "PLUGIN",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1AttributeValues(typing.TypedDict, total=False):
    attribute: str
    enumValues: GoogleCloudApihubV1EnumAttributeValues
    jsonValues: GoogleCloudApihubV1StringAttributeValues
    stringValues: GoogleCloudApihubV1StringAttributeValues
    uriValues: GoogleCloudApihubV1StringAttributeValues

@typing.type_check_only
class GoogleCloudApihubV1AuthConfig(typing.TypedDict, total=False):
    apiKeyConfig: GoogleCloudApihubV1ApiKeyConfig
    authType: typing.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "NO_AUTH",
        "GOOGLE_SERVICE_ACCOUNT",
        "USER_PASSWORD",
        "API_KEY",
        "OAUTH2_CLIENT_CREDENTIALS",
    ]
    googleServiceAccountConfig: GoogleCloudApihubV1GoogleServiceAccountConfig
    oauth2ClientCredentialsConfig: GoogleCloudApihubV1Oauth2ClientCredentialsConfig
    userPasswordConfig: GoogleCloudApihubV1UserPasswordConfig

@typing.type_check_only
class GoogleCloudApihubV1AuthConfigTemplate(typing.TypedDict, total=False):
    serviceAccount: GoogleCloudApihubV1GoogleServiceAccountConfig
    supportedAuthTypes: _list[
        typing.Literal[
            "AUTH_TYPE_UNSPECIFIED",
            "NO_AUTH",
            "GOOGLE_SERVICE_ACCOUNT",
            "USER_PASSWORD",
            "API_KEY",
            "OAUTH2_CLIENT_CREDENTIALS",
        ]
    ]

@typing.type_check_only
class GoogleCloudApihubV1CollectApiDataRequest(typing.TypedDict, total=False):
    actionId: str
    apiData: GoogleCloudApihubV1ApiData
    collectionType: typing.Literal[
        "COLLECTION_TYPE_UNSPECIFIED",
        "COLLECTION_TYPE_UPSERT",
        "COLLECTION_TYPE_DELETE",
    ]
    pluginInstance: str

@typing.type_check_only
class GoogleCloudApihubV1Config(typing.TypedDict, total=False):
    agentRegistrySyncConfig: GoogleCloudApihubV1AgentRegistrySyncConfig
    cmekKeyName: str
    disableSearch: bool
    encryptionType: typing.Literal["ENCRYPTION_TYPE_UNSPECIFIED", "GMEK", "CMEK"]
    vertexLocation: str

@typing.type_check_only
class GoogleCloudApihubV1ConfigTemplate(typing.TypedDict, total=False):
    additionalConfigTemplate: _list[GoogleCloudApihubV1ConfigVariableTemplate]
    authConfigTemplate: GoogleCloudApihubV1AuthConfigTemplate

@typing.type_check_only
class GoogleCloudApihubV1ConfigValueOption(typing.TypedDict, total=False):
    description: str
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudApihubV1ConfigVariable(typing.TypedDict, total=False):
    boolValue: bool
    enumValue: GoogleCloudApihubV1ConfigValueOption
    intValue: str
    key: str
    multiIntValues: GoogleCloudApihubV1MultiIntValues
    multiSelectValues: GoogleCloudApihubV1MultiSelectValues
    multiStringValues: GoogleCloudApihubV1MultiStringValues
    secretValue: GoogleCloudApihubV1Secret
    stringValue: str

@typing.type_check_only
class GoogleCloudApihubV1ConfigVariableTemplate(typing.TypedDict, total=False):
    description: str
    enumOptions: _list[GoogleCloudApihubV1ConfigValueOption]
    id: str
    multiSelectOptions: _list[GoogleCloudApihubV1ConfigValueOption]
    required: bool
    validationRegex: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "STRING",
        "INT",
        "BOOL",
        "SECRET",
        "ENUM",
        "MULTI_SELECT",
        "MULTI_STRING",
        "MULTI_INT",
    ]

@typing.type_check_only
class GoogleCloudApihubV1ConfigureAndDeployServerRequest(typing.TypedDict, total=False):
    mcpServerConfig: GoogleCloudApihubV1McpServerConfig

@typing.type_check_only
class GoogleCloudApihubV1Curation(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    endpoint: GoogleCloudApihubV1Endpoint
    lastExecutionErrorCode: typing.Literal[
        "ERROR_CODE_UNSPECIFIED", "INTERNAL_ERROR", "UNAUTHORIZED"
    ]
    lastExecutionErrorMessage: str
    lastExecutionState: typing.Literal[
        "LAST_EXECUTION_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"
    ]
    name: str
    pluginInstanceActions: _list[GoogleCloudApihubV1PluginInstanceActionID]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1CurationConfig(typing.TypedDict, total=False):
    curationType: typing.Literal[
        "CURATION_TYPE_UNSPECIFIED",
        "DEFAULT_CURATION_FOR_API_METADATA",
        "CUSTOM_CURATION_FOR_API_METADATA",
    ]
    customCuration: GoogleCloudApihubV1CustomCuration

@typing.type_check_only
class GoogleCloudApihubV1CustomCuration(typing.TypedDict, total=False):
    curation: str

@typing.type_check_only
class GoogleCloudApihubV1Definition(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    createTime: str
    name: str
    schema: GoogleCloudApihubV1Schema
    spec: str
    type: typing.Literal["TYPE_UNSPECIFIED", "SCHEMA"]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1Dependency(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    consumer: GoogleCloudApihubV1DependencyEntityReference
    createTime: str
    description: str
    discoveryMode: typing.Literal["DISCOVERY_MODE_UNSPECIFIED", "MANUAL"]
    errorDetail: GoogleCloudApihubV1DependencyErrorDetail
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "PROPOSED", "VALIDATED"]
    supplier: GoogleCloudApihubV1DependencyEntityReference
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1DependencyEntityReference(typing.TypedDict, total=False):
    displayName: str
    externalApiResourceName: str
    operationResourceName: str

@typing.type_check_only
class GoogleCloudApihubV1DependencyErrorDetail(typing.TypedDict, total=False):
    error: typing.Literal[
        "ERROR_UNSPECIFIED", "SUPPLIER_NOT_FOUND", "SUPPLIER_RECREATED"
    ]
    errorTime: str

@typing.type_check_only
class GoogleCloudApihubV1Deployment(typing.TypedDict, total=False):
    apiVersions: _list[str]
    attributes: dict[str, typing.Any]
    createTime: str
    deploymentType: GoogleCloudApihubV1AttributeValues
    description: str
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    endpoints: _list[str]
    environment: GoogleCloudApihubV1AttributeValues
    managementUrl: GoogleCloudApihubV1AttributeValues
    name: str
    resourceUri: str
    slo: GoogleCloudApihubV1AttributeValues
    sourceEnvironment: str
    sourceMetadata: _list[GoogleCloudApihubV1SourceMetadata]
    sourceProject: str
    sourceUri: GoogleCloudApihubV1AttributeValues
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1DeploymentMetadata(typing.TypedDict, total=False):
    deployment: GoogleCloudApihubV1Deployment
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str

@typing.type_check_only
class GoogleCloudApihubV1DisablePluginInstanceActionRequest(
    typing.TypedDict, total=False
):
    actionId: str

@typing.type_check_only
class GoogleCloudApihubV1DisablePluginRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApihubV1DiscoveredApiObservation(typing.TypedDict, total=False):
    apiOperationCount: str
    createTime: str
    hostname: str
    knownOperationsCount: str
    lastEventDetectedTime: str
    name: str
    origin: str
    serverIps: _list[str]
    sourceLocations: _list[str]
    sourceMetadata: GoogleCloudApihubV1SourceMetadata
    sourceTypes: _list[typing.Literal["SOURCE_TYPE_UNSPECIFIED", "GCP_XLB", "GCP_ILB"]]
    style: typing.Literal["STYLE_UNSPECIFIED", "REST", "GRPC", "GRAPHQL"]
    unknownOperationsCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1DiscoveredApiOperation(typing.TypedDict, total=False):
    classification: typing.Literal["CLASSIFICATION_UNSPECIFIED", "KNOWN", "UNKNOWN"]
    count: str
    createTime: str
    firstSeenTime: str
    httpOperation: GoogleCloudApihubV1HttpOperationDetails
    lastSeenTime: str
    matchResults: _list[GoogleCloudApihubV1MatchResult]
    name: str
    sourceMetadata: GoogleCloudApihubV1SourceMetadata
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1Documentation(typing.TypedDict, total=False):
    externalUri: str

@typing.type_check_only
class GoogleCloudApihubV1EnablePluginInstanceActionRequest(
    typing.TypedDict, total=False
):
    actionId: str

@typing.type_check_only
class GoogleCloudApihubV1EnablePluginRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApihubV1Endpoint(typing.TypedDict, total=False):
    applicationIntegrationEndpointDetails: (
        GoogleCloudApihubV1ApplicationIntegrationEndpointDetails
    )

@typing.type_check_only
class GoogleCloudApihubV1EnumAttributeValues(typing.TypedDict, total=False):
    values: _list[GoogleCloudApihubV1AllowedValue]

@typing.type_check_only
class GoogleCloudApihubV1EnvironmentFilter(typing.TypedDict, total=False):
    allEnvironments: bool
    environments: _list[str]

@typing.type_check_only
class GoogleCloudApihubV1ExecutePluginInstanceActionRequest(
    typing.TypedDict, total=False
):
    actionExecutionDetail: GoogleCloudApihubV1ActionExecutionDetail

@typing.type_check_only
class GoogleCloudApihubV1ExecutionStatus(typing.TypedDict, total=False):
    currentExecutionState: typing.Literal[
        "CURRENT_EXECUTION_STATE_UNSPECIFIED", "RUNNING", "NOT_RUNNING"
    ]
    lastExecution: GoogleCloudApihubV1LastExecution

@typing.type_check_only
class GoogleCloudApihubV1ExternalApi(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    createTime: str
    description: str
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    endpoints: _list[str]
    name: str
    paths: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1FetchAdditionalSpecContentResponse(
    typing.TypedDict, total=False
):
    additionalSpecContent: GoogleCloudApihubV1AdditionalSpecContent

@typing.type_check_only
class GoogleCloudApihubV1FlattenedApiVersionDeploymentView(
    typing.TypedDict, total=False
):
    api: GoogleCloudApihubV1Api
    deployment: GoogleCloudApihubV1Deployment
    version: GoogleCloudApihubV1Version

@typing.type_check_only
class GoogleCloudApihubV1FlattenedApiVersionOperationDeploymentView(
    typing.TypedDict, total=False
):
    api: GoogleCloudApihubV1Api
    apiOperation: GoogleCloudApihubV1ApiOperation
    deployment: GoogleCloudApihubV1Deployment
    version: GoogleCloudApihubV1Version

@typing.type_check_only
class GoogleCloudApihubV1GatewayPluginAddonConfig(typing.TypedDict, total=False):
    gatewayPluginConfigs: _list[GoogleCloudApihubV1GatewayPluginConfig]

@typing.type_check_only
class GoogleCloudApihubV1GatewayPluginConfig(typing.TypedDict, total=False):
    apigeeEdgeConfig: GoogleCloudApihubV1ApigeeEdgeConfig
    apigeeOpdkConfig: GoogleCloudApihubV1ApigeeOPDKConfig
    apigeeXHybridConfig: GoogleCloudApihubV1ApigeeXHybridConfig
    pluginInstance: str

@typing.type_check_only
class GoogleCloudApihubV1GoogleServiceAccountConfig(typing.TypedDict, total=False):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudApihubV1Header(typing.TypedDict, total=False):
    count: str
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED", "BOOL", "INTEGER", "FLOAT", "STRING", "UUID"
    ]
    name: str

@typing.type_check_only
class GoogleCloudApihubV1HostProjectRegistration(typing.TypedDict, total=False):
    createTime: str
    gcpProject: str
    name: str

@typing.type_check_only
class GoogleCloudApihubV1HostingService(typing.TypedDict, total=False):
    serviceUri: str

@typing.type_check_only
class GoogleCloudApihubV1HttpOperation(typing.TypedDict, total=False):
    method: typing.Literal[
        "METHOD_UNSPECIFIED",
        "GET",
        "PUT",
        "POST",
        "DELETE",
        "OPTIONS",
        "HEAD",
        "PATCH",
        "TRACE",
    ]
    path: GoogleCloudApihubV1Path

@typing.type_check_only
class GoogleCloudApihubV1HttpOperationConfig(typing.TypedDict, total=False):
    method: typing.Literal[
        "METHOD_UNSPECIFIED",
        "GET",
        "PUT",
        "POST",
        "DELETE",
        "OPTIONS",
        "HEAD",
        "PATCH",
        "TRACE",
    ]
    path: str
    spec: str

@typing.type_check_only
class GoogleCloudApihubV1HttpOperationDetails(typing.TypedDict, total=False):
    httpOperation: GoogleCloudApihubV1HttpOperation
    pathParams: _list[GoogleCloudApihubV1PathParam]
    queryParams: dict[str, typing.Any]
    request: GoogleCloudApihubV1HttpRequest
    response: GoogleCloudApihubV1HttpResponse

@typing.type_check_only
class GoogleCloudApihubV1HttpRequest(typing.TypedDict, total=False):
    headers: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudApihubV1HttpResponse(typing.TypedDict, total=False):
    headers: dict[str, typing.Any]
    responseCodes: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudApihubV1Issue(typing.TypedDict, total=False):
    code: str
    message: str
    path: _list[str]
    range: GoogleCloudApihubV1Range
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED",
        "SEVERITY_ERROR",
        "SEVERITY_WARNING",
        "SEVERITY_INFO",
        "SEVERITY_HINT",
    ]

@typing.type_check_only
class GoogleCloudApihubV1LastExecution(typing.TypedDict, total=False):
    endTime: str
    errorMessage: str
    result: typing.Literal["RESULT_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    resultMetadata: str
    startTime: str

@typing.type_check_only
class GoogleCloudApihubV1LintResponse(typing.TypedDict, total=False):
    createTime: str
    issues: _list[GoogleCloudApihubV1Issue]
    linter: typing.Literal["LINTER_UNSPECIFIED", "SPECTRAL", "OTHER"]
    source: str
    state: typing.Literal[
        "LINT_STATE_UNSPECIFIED", "LINT_STATE_SUCCESS", "LINT_STATE_ERROR"
    ]
    summary: _list[GoogleCloudApihubV1SummaryEntry]

@typing.type_check_only
class GoogleCloudApihubV1LintSpecRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApihubV1ListAddonsResponse(typing.TypedDict, total=False):
    addons: _list[GoogleCloudApihubV1Addon]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListApiOperationsResponse(typing.TypedDict, total=False):
    apiOperations: _list[GoogleCloudApihubV1ApiOperation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListApisResponse(typing.TypedDict, total=False):
    apis: _list[GoogleCloudApihubV1Api]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListAttributesResponse(typing.TypedDict, total=False):
    attributes: _list[GoogleCloudApihubV1Attribute]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListCurationsResponse(typing.TypedDict, total=False):
    curations: _list[GoogleCloudApihubV1Curation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListDependenciesResponse(typing.TypedDict, total=False):
    dependencies: _list[GoogleCloudApihubV1Dependency]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListDeploymentsResponse(typing.TypedDict, total=False):
    deployments: _list[GoogleCloudApihubV1Deployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListDiscoveredApiObservationsResponse(
    typing.TypedDict, total=False
):
    discoveredApiObservations: _list[GoogleCloudApihubV1DiscoveredApiObservation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListDiscoveredApiOperationsResponse(
    typing.TypedDict, total=False
):
    discoveredApiOperations: _list[GoogleCloudApihubV1DiscoveredApiOperation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListExternalApisResponse(typing.TypedDict, total=False):
    externalApis: _list[GoogleCloudApihubV1ExternalApi]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListHostProjectRegistrationsResponse(
    typing.TypedDict, total=False
):
    hostProjectRegistrations: _list[GoogleCloudApihubV1HostProjectRegistration]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListPluginInstancesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pluginInstances: _list[GoogleCloudApihubV1PluginInstance]

@typing.type_check_only
class GoogleCloudApihubV1ListPluginsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    plugins: _list[GoogleCloudApihubV1Plugin]

@typing.type_check_only
class GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    runtimeProjectAttachments: _list[GoogleCloudApihubV1RuntimeProjectAttachment]

@typing.type_check_only
class GoogleCloudApihubV1ListSpecsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    specs: _list[GoogleCloudApihubV1Spec]

@typing.type_check_only
class GoogleCloudApihubV1ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[GoogleCloudApihubV1Version]

@typing.type_check_only
class GoogleCloudApihubV1LookupApiHubInstanceResponse(typing.TypedDict, total=False):
    apiHubInstance: GoogleCloudApihubV1ApiHubInstance

@typing.type_check_only
class GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse(
    typing.TypedDict, total=False
):
    runtimeProjectAttachment: GoogleCloudApihubV1RuntimeProjectAttachment

@typing.type_check_only
class GoogleCloudApihubV1ManageAddonConfigRequest(typing.TypedDict, total=False):
    config: GoogleCloudApihubV1AddonConfig

@typing.type_check_only
class GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest(
    typing.TypedDict, total=False
):
    action: typing.Literal["ACTION_UNSPECIFIED", "UPLOAD", "DELETE"]
    data: str
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "PROXY_DEPLOYMENT_MANIFEST",
        "ENVIRONMENT_MANIFEST",
        "PROXY_BUNDLE",
        "SHARED_FLOW_BUNDLE",
    ]
    relativePath: str

@typing.type_check_only
class GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApihubV1MatchResult(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudApihubV1McpServerConfig(typing.TypedDict, total=False):
    apigeeXTargetDetails: GoogleCloudApihubV1ApigeeXTargetDetails
    tools: _list[GoogleCloudApihubV1McpToolConfig]

@typing.type_check_only
class GoogleCloudApihubV1McpTool(typing.TypedDict, total=False):
    annotations: GoogleCloudApihubV1ToolAnnotations
    description: str
    inputSchema: GoogleCloudApihubV1OperationSchema
    name: str
    outputSchema: GoogleCloudApihubV1OperationSchema
    title: str

@typing.type_check_only
class GoogleCloudApihubV1McpToolConfig(typing.TypedDict, total=False):
    description: str
    operation: GoogleCloudApihubV1OperationConfig
    toolId: str

@typing.type_check_only
class GoogleCloudApihubV1MetaData(typing.TypedDict, total=False):
    description: str
    displayName: str

@typing.type_check_only
class GoogleCloudApihubV1MultiIntValues(typing.TypedDict, total=False):
    values: _list[int]

@typing.type_check_only
class GoogleCloudApihubV1MultiSelectValues(typing.TypedDict, total=False):
    values: _list[GoogleCloudApihubV1ConfigValueOption]

@typing.type_check_only
class GoogleCloudApihubV1MultiStringValues(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudApihubV1Oauth2ClientCredentialsConfig(typing.TypedDict, total=False):
    clientId: str
    clientSecret: GoogleCloudApihubV1Secret

@typing.type_check_only
class GoogleCloudApihubV1OpenApiSpecDetails(typing.TypedDict, total=False):
    format: typing.Literal[
        "FORMAT_UNSPECIFIED",
        "OPEN_API_SPEC_2_0",
        "OPEN_API_SPEC_3_0",
        "OPEN_API_SPEC_3_1",
    ]
    owner: GoogleCloudApihubV1Owner
    version: str

@typing.type_check_only
class GoogleCloudApihubV1OperationConfig(typing.TypedDict, total=False):
    httpOperation: GoogleCloudApihubV1HttpOperationConfig
    operation: str

@typing.type_check_only
class GoogleCloudApihubV1OperationDetails(typing.TypedDict, total=False):
    deprecated: bool
    description: str
    documentation: GoogleCloudApihubV1Documentation
    httpOperation: GoogleCloudApihubV1HttpOperation
    mcpTool: GoogleCloudApihubV1McpTool

@typing.type_check_only
class GoogleCloudApihubV1OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudApihubV1OperationSchema(typing.TypedDict, total=False):
    jsonSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudApihubV1Owner(typing.TypedDict, total=False):
    displayName: str
    email: str

@typing.type_check_only
class GoogleCloudApihubV1Path(typing.TypedDict, total=False):
    description: str
    path: str

@typing.type_check_only
class GoogleCloudApihubV1PathParam(typing.TypedDict, total=False):
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED", "BOOL", "INTEGER", "FLOAT", "STRING", "UUID"
    ]
    position: int

@typing.type_check_only
class GoogleCloudApihubV1Plugin(typing.TypedDict, total=False):
    actionsConfig: _list[GoogleCloudApihubV1PluginActionConfig]
    configTemplate: GoogleCloudApihubV1ConfigTemplate
    createTime: str
    description: str
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    gatewayType: typing.Literal[
        "GATEWAY_TYPE_UNSPECIFIED",
        "APIGEE_X_AND_HYBRID",
        "APIGEE_EDGE_PUBLIC_CLOUD",
        "APIGEE_EDGE_PRIVATE_CLOUD",
        "CLOUD_API_GATEWAY",
        "CLOUD_ENDPOINTS",
        "API_DISCOVERY",
        "OTHERS",
        "AWS_API_GATEWAY",
        "AZURE_API_MANAGEMENT",
    ]
    hostingService: GoogleCloudApihubV1HostingService
    name: str
    ownershipType: typing.Literal[
        "OWNERSHIP_TYPE_UNSPECIFIED", "SYSTEM_OWNED", "USER_OWNED"
    ]
    pluginCategory: typing.Literal[
        "PLUGIN_CATEGORY_UNSPECIFIED", "API_GATEWAY", "API_PRODUCER"
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    type: GoogleCloudApihubV1AttributeValues
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1PluginActionConfig(typing.TypedDict, total=False):
    description: str
    displayName: str
    id: str
    triggerMode: typing.Literal[
        "TRIGGER_MODE_UNSPECIFIED",
        "API_HUB_ON_DEMAND_TRIGGER",
        "API_HUB_SCHEDULE_TRIGGER",
        "NON_API_HUB_MANAGED",
    ]

@typing.type_check_only
class GoogleCloudApihubV1PluginInstance(typing.TypedDict, total=False):
    actions: _list[GoogleCloudApihubV1PluginInstanceAction]
    additionalConfig: dict[str, typing.Any]
    authConfig: GoogleCloudApihubV1AuthConfig
    createTime: str
    displayName: str
    errorMessage: str
    name: str
    sourceEnvironmentsConfig: dict[str, typing.Any]
    sourceProjectId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "APPLYING_CONFIG",
        "ERROR",
        "FAILED",
        "DELETING",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1PluginInstanceAction(typing.TypedDict, total=False):
    actionId: str
    curationConfig: GoogleCloudApihubV1CurationConfig
    hubInstanceAction: GoogleCloudApihubV1ExecutionStatus
    resourceConfig: GoogleCloudApihubV1ResourceConfig
    scheduleCronExpression: str
    scheduleTimeZone: str
    serviceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DISABLED", "ENABLING", "DISABLING", "ERROR"
    ]

@typing.type_check_only
class GoogleCloudApihubV1PluginInstanceActionID(typing.TypedDict, total=False):
    actionId: str
    pluginInstance: str

@typing.type_check_only
class GoogleCloudApihubV1PluginInstanceActionSource(typing.TypedDict, total=False):
    actionId: str
    pluginInstance: str

@typing.type_check_only
class GoogleCloudApihubV1Point(typing.TypedDict, total=False):
    character: int
    line: int

@typing.type_check_only
class GoogleCloudApihubV1QueryParam(typing.TypedDict, total=False):
    count: str
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED", "BOOL", "INTEGER", "FLOAT", "STRING", "UUID"
    ]
    name: str

@typing.type_check_only
class GoogleCloudApihubV1Range(typing.TypedDict, total=False):
    end: GoogleCloudApihubV1Point
    start: GoogleCloudApihubV1Point

@typing.type_check_only
class GoogleCloudApihubV1ResourceConfig(typing.TypedDict, total=False):
    actionType: typing.Literal[
        "ACTION_TYPE_UNSPECIFIED", "SYNC_METADATA", "SYNC_RUNTIME_DATA"
    ]
    pubsubTopic: str

@typing.type_check_only
class GoogleCloudApihubV1RetrieveApiViewsResponse(typing.TypedDict, total=False):
    apiViews: _list[GoogleCloudApihubV1ApiView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1RuntimeProjectAttachment(typing.TypedDict, total=False):
    createTime: str
    name: str
    runtimeProject: str

@typing.type_check_only
class GoogleCloudApihubV1Schema(typing.TypedDict, total=False):
    displayName: str
    rawValue: str

@typing.type_check_only
class GoogleCloudApihubV1SearchResourcesRequest(typing.TypedDict, total=False):
    filter: str
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class GoogleCloudApihubV1SearchResourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    searchResults: _list[GoogleCloudApihubV1SearchResult]

@typing.type_check_only
class GoogleCloudApihubV1SearchResult(typing.TypedDict, total=False):
    resource: GoogleCloudApihubV1ApiHubResource

@typing.type_check_only
class GoogleCloudApihubV1Secret(typing.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class GoogleCloudApihubV1SourceEnvironment(typing.TypedDict, total=False):
    createTime: str
    sourceEnvironment: str
    sourceEnvironmentUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1SourceMetadata(typing.TypedDict, total=False):
    originalResourceCreateTime: str
    originalResourceId: str
    originalResourceUpdateTime: str
    pluginInstanceActionSource: GoogleCloudApihubV1PluginInstanceActionSource
    sourceType: typing.Literal["SOURCE_TYPE_UNSPECIFIED", "PLUGIN"]

@typing.type_check_only
class GoogleCloudApihubV1Spec(typing.TypedDict, total=False):
    additionalSpecContents: _list[GoogleCloudApihubV1AdditionalSpecContent]
    attributes: dict[str, typing.Any]
    contents: GoogleCloudApihubV1SpecContents
    createTime: str
    details: GoogleCloudApihubV1SpecDetails
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    lintResponse: GoogleCloudApihubV1LintResponse
    name: str
    parsingMode: typing.Literal["PARSING_MODE_UNSPECIFIED", "RELAXED", "STRICT"]
    sourceMetadata: _list[GoogleCloudApihubV1SourceMetadata]
    sourceUri: str
    specType: GoogleCloudApihubV1AttributeValues
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1SpecContents(typing.TypedDict, total=False):
    contents: str
    mimeType: str

@typing.type_check_only
class GoogleCloudApihubV1SpecDetails(typing.TypedDict, total=False):
    description: str
    openApiSpecDetails: GoogleCloudApihubV1OpenApiSpecDetails

@typing.type_check_only
class GoogleCloudApihubV1SpecMetadata(typing.TypedDict, total=False):
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str
    spec: GoogleCloudApihubV1Spec

@typing.type_check_only
class GoogleCloudApihubV1StringAttributeValues(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudApihubV1StyleGuide(typing.TypedDict, total=False):
    contents: GoogleCloudApihubV1StyleGuideContents
    linter: typing.Literal["LINTER_UNSPECIFIED", "SPECTRAL", "OTHER"]
    name: str

@typing.type_check_only
class GoogleCloudApihubV1StyleGuideContents(typing.TypedDict, total=False):
    contents: str
    mimeType: str

@typing.type_check_only
class GoogleCloudApihubV1SummaryEntry(typing.TypedDict, total=False):
    count: int
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED",
        "SEVERITY_ERROR",
        "SEVERITY_WARNING",
        "SEVERITY_INFO",
        "SEVERITY_HINT",
    ]

@typing.type_check_only
class GoogleCloudApihubV1ToolAnnotations(typing.TypedDict, total=False):
    additionalHints: dict[str, typing.Any]
    destructiveHint: bool
    idempotentHint: bool
    openWorldHint: bool
    readOnlyHint: bool
    title: str

@typing.type_check_only
class GoogleCloudApihubV1UserPasswordConfig(typing.TypedDict, total=False):
    password: GoogleCloudApihubV1Secret
    username: str

@typing.type_check_only
class GoogleCloudApihubV1Version(typing.TypedDict, total=False):
    accreditation: GoogleCloudApihubV1AttributeValues
    apiOperations: _list[str]
    attributes: dict[str, typing.Any]
    compliance: GoogleCloudApihubV1AttributeValues
    createTime: str
    definitions: _list[str]
    deployments: _list[str]
    description: str
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    lifecycle: GoogleCloudApihubV1AttributeValues
    name: str
    selectedDeployment: str
    sourceMetadata: _list[GoogleCloudApihubV1SourceMetadata]
    specs: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1VersionMetadata(typing.TypedDict, total=False):
    deployments: _list[GoogleCloudApihubV1DeploymentMetadata]
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str
    specs: _list[GoogleCloudApihubV1SpecMetadata]
    version: GoogleCloudApihubV1Version

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

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
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
