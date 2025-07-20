import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApihubV1APIMetadata(typing_extensions.TypedDict, total=False):
    api: GoogleCloudApihubV1Api
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str
    versions: _list[GoogleCloudApihubV1VersionMetadata]

@typing.type_check_only
class GoogleCloudApihubV1ActionExecutionDetail(
    typing_extensions.TypedDict, total=False
):
    actionId: str

@typing.type_check_only
class GoogleCloudApihubV1AllowedValue(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    id: str
    immutable: bool

@typing.type_check_only
class GoogleCloudApihubV1Api(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApihubV1ApiData(typing_extensions.TypedDict, total=False):
    apiMetadataList: GoogleCloudApihubV1ApiMetadataList

@typing.type_check_only
class GoogleCloudApihubV1ApiHubInstance(typing_extensions.TypedDict, total=False):
    config: GoogleCloudApihubV1Config
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
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
class GoogleCloudApihubV1ApiHubResource(typing_extensions.TypedDict, total=False):
    api: GoogleCloudApihubV1Api
    definition: GoogleCloudApihubV1Definition
    deployment: GoogleCloudApihubV1Deployment
    operation: GoogleCloudApihubV1ApiOperation
    spec: GoogleCloudApihubV1Spec
    version: GoogleCloudApihubV1Version

@typing.type_check_only
class GoogleCloudApihubV1ApiKeyConfig(typing_extensions.TypedDict, total=False):
    apiKey: GoogleCloudApihubV1Secret
    httpElementLocation: typing_extensions.Literal[
        "HTTP_ELEMENT_LOCATION_UNSPECIFIED", "QUERY", "HEADER", "PATH", "BODY", "COOKIE"
    ]
    name: str

@typing.type_check_only
class GoogleCloudApihubV1ApiMetadataList(typing_extensions.TypedDict, total=False):
    apiMetadata: _list[GoogleCloudApihubV1APIMetadata]

@typing.type_check_only
class GoogleCloudApihubV1ApiOperation(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    createTime: str
    details: GoogleCloudApihubV1OperationDetails
    name: str
    sourceMetadata: _list[GoogleCloudApihubV1SourceMetadata]
    spec: str
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1ApplicationIntegrationEndpointDetails(
    typing_extensions.TypedDict, total=False
):
    triggerId: str
    uri: str

@typing.type_check_only
class GoogleCloudApihubV1Attribute(typing_extensions.TypedDict, total=False):
    allowedValues: _list[GoogleCloudApihubV1AllowedValue]
    cardinality: int
    createTime: str
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "ENUM", "JSON", "STRING", "URI"
    ]
    definitionType: typing_extensions.Literal[
        "DEFINITION_TYPE_UNSPECIFIED", "SYSTEM_DEFINED", "USER_DEFINED"
    ]
    description: str
    displayName: str
    mandatory: bool
    name: str
    scope: typing_extensions.Literal[
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
class GoogleCloudApihubV1AttributeValues(typing_extensions.TypedDict, total=False):
    attribute: str
    enumValues: GoogleCloudApihubV1EnumAttributeValues
    jsonValues: GoogleCloudApihubV1StringAttributeValues
    stringValues: GoogleCloudApihubV1StringAttributeValues
    uriValues: GoogleCloudApihubV1StringAttributeValues

@typing.type_check_only
class GoogleCloudApihubV1AuthConfig(typing_extensions.TypedDict, total=False):
    apiKeyConfig: GoogleCloudApihubV1ApiKeyConfig
    authType: typing_extensions.Literal[
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
class GoogleCloudApihubV1AuthConfigTemplate(typing_extensions.TypedDict, total=False):
    serviceAccount: GoogleCloudApihubV1GoogleServiceAccountConfig
    supportedAuthTypes: _list[
        typing_extensions.Literal[
            "AUTH_TYPE_UNSPECIFIED",
            "NO_AUTH",
            "GOOGLE_SERVICE_ACCOUNT",
            "USER_PASSWORD",
            "API_KEY",
            "OAUTH2_CLIENT_CREDENTIALS",
        ]
    ]

@typing.type_check_only
class GoogleCloudApihubV1CollectApiDataRequest(
    typing_extensions.TypedDict, total=False
):
    actionId: str
    apiData: GoogleCloudApihubV1ApiData
    collectionType: typing_extensions.Literal[
        "COLLECTION_TYPE_UNSPECIFIED",
        "COLLECTION_TYPE_UPSERT",
        "COLLECTION_TYPE_DELETE",
    ]
    pluginInstance: str

@typing.type_check_only
class GoogleCloudApihubV1Config(typing_extensions.TypedDict, total=False):
    cmekKeyName: str
    disableSearch: bool
    encryptionType: typing_extensions.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED", "GMEK", "CMEK"
    ]
    vertexLocation: str

@typing.type_check_only
class GoogleCloudApihubV1ConfigTemplate(typing_extensions.TypedDict, total=False):
    additionalConfigTemplate: _list[GoogleCloudApihubV1ConfigVariableTemplate]
    authConfigTemplate: GoogleCloudApihubV1AuthConfigTemplate

@typing.type_check_only
class GoogleCloudApihubV1ConfigValueOption(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudApihubV1ConfigVariable(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApihubV1ConfigVariableTemplate(
    typing_extensions.TypedDict, total=False
):
    description: str
    enumOptions: _list[GoogleCloudApihubV1ConfigValueOption]
    id: str
    multiSelectOptions: _list[GoogleCloudApihubV1ConfigValueOption]
    required: bool
    validationRegex: str
    valueType: typing_extensions.Literal[
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
class GoogleCloudApihubV1Curation(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    endpoint: GoogleCloudApihubV1Endpoint
    lastExecutionErrorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED", "INTERNAL_ERROR", "UNAUTHORIZED"
    ]
    lastExecutionErrorMessage: str
    lastExecutionState: typing_extensions.Literal[
        "LAST_EXECUTION_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"
    ]
    name: str
    pluginInstanceActions: _list[GoogleCloudApihubV1PluginInstanceActionID]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1CurationConfig(typing_extensions.TypedDict, total=False):
    curationType: typing_extensions.Literal[
        "CURATION_TYPE_UNSPECIFIED",
        "DEFAULT_CURATION_FOR_API_METADATA",
        "CUSTOM_CURATION_FOR_API_METADATA",
    ]
    customCuration: GoogleCloudApihubV1CustomCuration

@typing.type_check_only
class GoogleCloudApihubV1CustomCuration(typing_extensions.TypedDict, total=False):
    curation: str

@typing.type_check_only
class GoogleCloudApihubV1Definition(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    createTime: str
    name: str
    schema: GoogleCloudApihubV1Schema
    spec: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SCHEMA"]
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1Dependency(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    consumer: GoogleCloudApihubV1DependencyEntityReference
    createTime: str
    description: str
    discoveryMode: typing_extensions.Literal["DISCOVERY_MODE_UNSPECIFIED", "MANUAL"]
    errorDetail: GoogleCloudApihubV1DependencyErrorDetail
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PROPOSED", "VALIDATED"]
    supplier: GoogleCloudApihubV1DependencyEntityReference
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1DependencyEntityReference(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    externalApiResourceName: str
    operationResourceName: str

@typing.type_check_only
class GoogleCloudApihubV1DependencyErrorDetail(
    typing_extensions.TypedDict, total=False
):
    error: typing_extensions.Literal[
        "ERROR_UNSPECIFIED", "SUPPLIER_NOT_FOUND", "SUPPLIER_RECREATED"
    ]
    errorTime: str

@typing.type_check_only
class GoogleCloudApihubV1Deployment(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApihubV1DeploymentMetadata(typing_extensions.TypedDict, total=False):
    deployment: GoogleCloudApihubV1Deployment
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str

@typing.type_check_only
class GoogleCloudApihubV1DisablePluginInstanceActionRequest(
    typing_extensions.TypedDict, total=False
):
    actionId: str

@typing.type_check_only
class GoogleCloudApihubV1DisablePluginRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApihubV1Documentation(typing_extensions.TypedDict, total=False):
    externalUri: str

@typing.type_check_only
class GoogleCloudApihubV1EnablePluginInstanceActionRequest(
    typing_extensions.TypedDict, total=False
):
    actionId: str

@typing.type_check_only
class GoogleCloudApihubV1EnablePluginRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudApihubV1Endpoint(typing_extensions.TypedDict, total=False):
    applicationIntegrationEndpointDetails: (
        GoogleCloudApihubV1ApplicationIntegrationEndpointDetails
    )

@typing.type_check_only
class GoogleCloudApihubV1EnumAttributeValues(typing_extensions.TypedDict, total=False):
    values: _list[GoogleCloudApihubV1AllowedValue]

@typing.type_check_only
class GoogleCloudApihubV1ExecutePluginInstanceActionRequest(
    typing_extensions.TypedDict, total=False
):
    actionExecutionDetail: GoogleCloudApihubV1ActionExecutionDetail

@typing.type_check_only
class GoogleCloudApihubV1ExecutionStatus(typing_extensions.TypedDict, total=False):
    currentExecutionState: typing_extensions.Literal[
        "CURRENT_EXECUTION_STATE_UNSPECIFIED", "RUNNING", "NOT_RUNNING"
    ]
    lastExecution: GoogleCloudApihubV1LastExecution

@typing.type_check_only
class GoogleCloudApihubV1ExternalApi(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApihubV1GoogleServiceAccountConfig(
    typing_extensions.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudApihubV1HostProjectRegistration(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    gcpProject: str
    name: str

@typing.type_check_only
class GoogleCloudApihubV1HostingService(typing_extensions.TypedDict, total=False):
    serviceUri: str

@typing.type_check_only
class GoogleCloudApihubV1HttpOperation(typing_extensions.TypedDict, total=False):
    method: typing_extensions.Literal[
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
class GoogleCloudApihubV1Issue(typing_extensions.TypedDict, total=False):
    code: str
    message: str
    path: _list[str]
    range: GoogleCloudApihubV1Range
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED",
        "SEVERITY_ERROR",
        "SEVERITY_WARNING",
        "SEVERITY_INFO",
        "SEVERITY_HINT",
    ]

@typing.type_check_only
class GoogleCloudApihubV1LastExecution(typing_extensions.TypedDict, total=False):
    endTime: str
    errorMessage: str
    result: typing_extensions.Literal["RESULT_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    startTime: str

@typing.type_check_only
class GoogleCloudApihubV1LintResponse(typing_extensions.TypedDict, total=False):
    createTime: str
    issues: _list[GoogleCloudApihubV1Issue]
    linter: typing_extensions.Literal["LINTER_UNSPECIFIED", "SPECTRAL", "OTHER"]
    source: str
    state: typing_extensions.Literal[
        "LINT_STATE_UNSPECIFIED", "LINT_STATE_SUCCESS", "LINT_STATE_ERROR"
    ]
    summary: _list[GoogleCloudApihubV1SummaryEntry]

@typing.type_check_only
class GoogleCloudApihubV1LintSpecRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudApihubV1ListApiOperationsResponse(
    typing_extensions.TypedDict, total=False
):
    apiOperations: _list[GoogleCloudApihubV1ApiOperation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListApisResponse(typing_extensions.TypedDict, total=False):
    apis: _list[GoogleCloudApihubV1Api]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListAttributesResponse(
    typing_extensions.TypedDict, total=False
):
    attributes: _list[GoogleCloudApihubV1Attribute]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListCurationsResponse(
    typing_extensions.TypedDict, total=False
):
    curations: _list[GoogleCloudApihubV1Curation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListDependenciesResponse(
    typing_extensions.TypedDict, total=False
):
    dependencies: _list[GoogleCloudApihubV1Dependency]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListDeploymentsResponse(
    typing_extensions.TypedDict, total=False
):
    deployments: _list[GoogleCloudApihubV1Deployment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListExternalApisResponse(
    typing_extensions.TypedDict, total=False
):
    externalApis: _list[GoogleCloudApihubV1ExternalApi]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListHostProjectRegistrationsResponse(
    typing_extensions.TypedDict, total=False
):
    hostProjectRegistrations: _list[GoogleCloudApihubV1HostProjectRegistration]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudApihubV1ListPluginInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pluginInstances: _list[GoogleCloudApihubV1PluginInstance]

@typing.type_check_only
class GoogleCloudApihubV1ListPluginsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    plugins: _list[GoogleCloudApihubV1Plugin]

@typing.type_check_only
class GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    runtimeProjectAttachments: _list[GoogleCloudApihubV1RuntimeProjectAttachment]

@typing.type_check_only
class GoogleCloudApihubV1ListSpecsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    specs: _list[GoogleCloudApihubV1Spec]

@typing.type_check_only
class GoogleCloudApihubV1ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: _list[GoogleCloudApihubV1Version]

@typing.type_check_only
class GoogleCloudApihubV1LookupApiHubInstanceResponse(
    typing_extensions.TypedDict, total=False
):
    apiHubInstance: GoogleCloudApihubV1ApiHubInstance

@typing.type_check_only
class GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse(
    typing_extensions.TypedDict, total=False
):
    runtimeProjectAttachment: GoogleCloudApihubV1RuntimeProjectAttachment

@typing.type_check_only
class GoogleCloudApihubV1MultiIntValues(typing_extensions.TypedDict, total=False):
    values: _list[int]

@typing.type_check_only
class GoogleCloudApihubV1MultiSelectValues(typing_extensions.TypedDict, total=False):
    values: _list[GoogleCloudApihubV1ConfigValueOption]

@typing.type_check_only
class GoogleCloudApihubV1MultiStringValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudApihubV1Oauth2ClientCredentialsConfig(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    clientSecret: GoogleCloudApihubV1Secret

@typing.type_check_only
class GoogleCloudApihubV1OpenApiSpecDetails(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED",
        "OPEN_API_SPEC_2_0",
        "OPEN_API_SPEC_3_0",
        "OPEN_API_SPEC_3_1",
    ]
    owner: GoogleCloudApihubV1Owner
    version: str

@typing.type_check_only
class GoogleCloudApihubV1OperationDetails(typing_extensions.TypedDict, total=False):
    deprecated: bool
    description: str
    documentation: GoogleCloudApihubV1Documentation
    httpOperation: GoogleCloudApihubV1HttpOperation

@typing.type_check_only
class GoogleCloudApihubV1OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudApihubV1Owner(typing_extensions.TypedDict, total=False):
    displayName: str
    email: str

@typing.type_check_only
class GoogleCloudApihubV1Path(typing_extensions.TypedDict, total=False):
    description: str
    path: str

@typing.type_check_only
class GoogleCloudApihubV1Plugin(typing_extensions.TypedDict, total=False):
    actionsConfig: _list[GoogleCloudApihubV1PluginActionConfig]
    configTemplate: GoogleCloudApihubV1ConfigTemplate
    createTime: str
    description: str
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    gatewayType: typing_extensions.Literal[
        "GATEWAY_TYPE_UNSPECIFIED",
        "APIGEE_X_AND_HYBRID",
        "APIGEE_EDGE_PUBLIC_CLOUD",
        "APIGEE_EDGE_PRIVATE_CLOUD",
        "CLOUD_API_GATEWAY",
        "CLOUD_ENDPOINTS",
        "API_DISCOVERY",
        "OTHERS",
    ]
    hostingService: GoogleCloudApihubV1HostingService
    name: str
    ownershipType: typing_extensions.Literal[
        "OWNERSHIP_TYPE_UNSPECIFIED", "SYSTEM_OWNED", "USER_OWNED"
    ]
    pluginCategory: typing_extensions.Literal[
        "PLUGIN_CATEGORY_UNSPECIFIED", "API_GATEWAY", "API_PRODUCER"
    ]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    type: GoogleCloudApihubV1AttributeValues
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1PluginActionConfig(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    id: str
    triggerMode: typing_extensions.Literal[
        "TRIGGER_MODE_UNSPECIFIED",
        "API_HUB_ON_DEMAND_TRIGGER",
        "API_HUB_SCHEDULE_TRIGGER",
        "NON_API_HUB_MANAGED",
    ]

@typing.type_check_only
class GoogleCloudApihubV1PluginInstance(typing_extensions.TypedDict, total=False):
    actions: _list[GoogleCloudApihubV1PluginInstanceAction]
    additionalConfig: dict[str, typing.Any]
    authConfig: GoogleCloudApihubV1AuthConfig
    createTime: str
    displayName: str
    errorMessage: str
    name: str
    sourceProjectId: str
    state: typing_extensions.Literal[
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
class GoogleCloudApihubV1PluginInstanceAction(typing_extensions.TypedDict, total=False):
    actionId: str
    curationConfig: GoogleCloudApihubV1CurationConfig
    hubInstanceAction: GoogleCloudApihubV1ExecutionStatus
    resourceConfig: GoogleCloudApihubV1ResourceConfig
    scheduleCronExpression: str
    scheduleTimeZone: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DISABLED", "ENABLING", "DISABLING", "ERROR"
    ]

@typing.type_check_only
class GoogleCloudApihubV1PluginInstanceActionID(
    typing_extensions.TypedDict, total=False
):
    actionId: str
    pluginInstance: str

@typing.type_check_only
class GoogleCloudApihubV1PluginInstanceActionSource(
    typing_extensions.TypedDict, total=False
):
    actionId: str
    pluginInstance: str

@typing.type_check_only
class GoogleCloudApihubV1Point(typing_extensions.TypedDict, total=False):
    character: int
    line: int

@typing.type_check_only
class GoogleCloudApihubV1Range(typing_extensions.TypedDict, total=False):
    end: GoogleCloudApihubV1Point
    start: GoogleCloudApihubV1Point

@typing.type_check_only
class GoogleCloudApihubV1ResourceConfig(typing_extensions.TypedDict, total=False):
    actionType: typing_extensions.Literal[
        "ACTION_TYPE_UNSPECIFIED", "SYNC_METADATA", "SYNC_RUNTIME_DATA"
    ]
    pubsubTopic: str

@typing.type_check_only
class GoogleCloudApihubV1RuntimeProjectAttachment(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    name: str
    runtimeProject: str

@typing.type_check_only
class GoogleCloudApihubV1Schema(typing_extensions.TypedDict, total=False):
    displayName: str
    rawValue: str

@typing.type_check_only
class GoogleCloudApihubV1SearchResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class GoogleCloudApihubV1SearchResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    searchResults: _list[GoogleCloudApihubV1SearchResult]

@typing.type_check_only
class GoogleCloudApihubV1SearchResult(typing_extensions.TypedDict, total=False):
    resource: GoogleCloudApihubV1ApiHubResource

@typing.type_check_only
class GoogleCloudApihubV1Secret(typing_extensions.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class GoogleCloudApihubV1SourceMetadata(typing_extensions.TypedDict, total=False):
    originalResourceCreateTime: str
    originalResourceId: str
    originalResourceUpdateTime: str
    pluginInstanceActionSource: GoogleCloudApihubV1PluginInstanceActionSource
    sourceType: typing_extensions.Literal["SOURCE_TYPE_UNSPECIFIED", "PLUGIN"]

@typing.type_check_only
class GoogleCloudApihubV1Spec(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    contents: GoogleCloudApihubV1SpecContents
    createTime: str
    details: GoogleCloudApihubV1SpecDetails
    displayName: str
    documentation: GoogleCloudApihubV1Documentation
    lintResponse: GoogleCloudApihubV1LintResponse
    name: str
    parsingMode: typing_extensions.Literal[
        "PARSING_MODE_UNSPECIFIED", "RELAXED", "STRICT"
    ]
    sourceMetadata: _list[GoogleCloudApihubV1SourceMetadata]
    sourceUri: str
    specType: GoogleCloudApihubV1AttributeValues
    updateTime: str

@typing.type_check_only
class GoogleCloudApihubV1SpecContents(typing_extensions.TypedDict, total=False):
    contents: str
    mimeType: str

@typing.type_check_only
class GoogleCloudApihubV1SpecDetails(typing_extensions.TypedDict, total=False):
    description: str
    openApiSpecDetails: GoogleCloudApihubV1OpenApiSpecDetails

@typing.type_check_only
class GoogleCloudApihubV1SpecMetadata(typing_extensions.TypedDict, total=False):
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str
    spec: GoogleCloudApihubV1Spec

@typing.type_check_only
class GoogleCloudApihubV1StringAttributeValues(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudApihubV1StyleGuide(typing_extensions.TypedDict, total=False):
    contents: GoogleCloudApihubV1StyleGuideContents
    linter: typing_extensions.Literal["LINTER_UNSPECIFIED", "SPECTRAL", "OTHER"]
    name: str

@typing.type_check_only
class GoogleCloudApihubV1StyleGuideContents(typing_extensions.TypedDict, total=False):
    contents: str
    mimeType: str

@typing.type_check_only
class GoogleCloudApihubV1SummaryEntry(typing_extensions.TypedDict, total=False):
    count: int
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED",
        "SEVERITY_ERROR",
        "SEVERITY_WARNING",
        "SEVERITY_INFO",
        "SEVERITY_HINT",
    ]

@typing.type_check_only
class GoogleCloudApihubV1UserPasswordConfig(typing_extensions.TypedDict, total=False):
    password: GoogleCloudApihubV1Secret
    username: str

@typing.type_check_only
class GoogleCloudApihubV1Version(typing_extensions.TypedDict, total=False):
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
class GoogleCloudApihubV1VersionMetadata(typing_extensions.TypedDict, total=False):
    deployments: _list[GoogleCloudApihubV1DeploymentMetadata]
    originalCreateTime: str
    originalId: str
    originalUpdateTime: str
    specs: _list[GoogleCloudApihubV1SpecMetadata]
    version: GoogleCloudApihubV1Version

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

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
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
