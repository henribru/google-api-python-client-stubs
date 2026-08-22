import typing

_list = list

@typing.type_check_only
class AdminFilters(typing.TypedDict, total=False):
    filterKey: str
    filterType: typing.Literal["FILTER_TYPE_UNSPECIFIED", "INCLUSION", "EXCLUSION"]
    intValue: str
    stringListValues: StringListValues
    stringValue: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthConfig(typing.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    authKey: str
    authType: typing.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
        "GOOGLE_AUTHENTICATION",
        "OAUTH2_AUTH_CODE_FLOW_GOOGLE_MANAGED",
    ]
    oauth2AuthCodeFlow: Oauth2AuthCodeFlow
    oauth2AuthCodeFlowGoogleManaged: Oauth2AuthCodeFlowGoogleManaged
    oauth2ClientCredentials: Oauth2ClientCredentials
    oauth2JwtBearer: Oauth2JwtBearer
    sshPublicKey: SshPublicKey
    userPassword: UserPassword

@typing.type_check_only
class AuthConfigTemplate(typing.TypedDict, total=False):
    authKey: str
    authType: typing.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
        "GOOGLE_AUTHENTICATION",
        "OAUTH2_AUTH_CODE_FLOW_GOOGLE_MANAGED",
    ]
    configVariableTemplates: _list[ConfigVariableTemplate]
    description: str
    displayName: str
    isDefault: bool

@typing.type_check_only
class AuthField(typing.TypedDict, total=False):
    dataType: str
    description: str
    key: str

@typing.type_check_only
class AuthObject(typing.TypedDict, total=False):
    additionalProperties: bool
    authKey: str
    authType: str
    description: str
    isDefault: bool
    properties: dict[str, typing.Any]
    type: str

@typing.type_check_only
class AuthProperty(typing.TypedDict, total=False):
    description: str
    type: str

@typing.type_check_only
class AuthSchema(typing.TypedDict, total=False):
    authFields: _list[AuthField]
    authKey: str
    authType: typing.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
        "GOOGLE_AUTHENTICATION",
        "OAUTH2_AUTH_CODE_FLOW_GOOGLE_MANAGED",
    ]
    description: str
    displayName: str
    isDefault: bool

@typing.type_check_only
class AuthorizationCodeLink(typing.TypedDict, total=False):
    clientId: str
    clientSecret: Secret
    enablePkce: bool
    omitQueryParams: bool
    scopes: _list[str]
    uri: str

@typing.type_check_only
class BillingConfig(typing.TypedDict, total=False):
    billingCategory: typing.Literal[
        "BILLING_CATEGORY_UNSPECIFIED",
        "GCP_AND_TECHNICAL_CONNECTOR",
        "NON_GCP_CONNECTOR",
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ConfigVariable(typing.TypedDict, total=False):
    boolValue: bool
    encryptionKeyValue: EncryptionKey
    intValue: str
    key: str
    secretValue: Secret
    stringValue: str

@typing.type_check_only
class ConfigVariableTemplate(typing.TypedDict, total=False):
    authorizationCodeLink: AuthorizationCodeLink
    description: str
    displayName: str
    enumOptions: _list[EnumOption]
    enumSource: typing.Literal["ENUM_SOURCE_UNSPECIFIED", "EVENT_TYPES_API"]
    isAdvanced: bool
    key: str
    locationType: typing.Literal[
        "LOCATION_TYPE_UNSPECIFIED", "HEADER", "PAYLOAD", "QUERY_PARAM", "PATH_PARAM"
    ]
    multipleSelectConfig: MultipleSelectConfig
    required: bool
    requiredCondition: LogicalExpression
    roleGrant: RoleGrant
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED"]
    validationRegex: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "STRING",
        "INT",
        "BOOL",
        "SECRET",
        "ENUM",
        "AUTHORIZATION_CODE",
        "ENCRYPTION_KEY",
        "MULTIPLE_SELECT",
    ]

@typing.type_check_only
class Connection(typing.TypedDict, total=False):
    adminFilters: _list[AdminFilters]
    asyncOperationsEnabled: bool
    authConfig: AuthConfig
    authOverrideEnabled: bool
    billingConfig: BillingConfig
    configVariables: _list[ConfigVariable]
    connectionRevision: str
    connectorVersion: str
    connectorVersionInfraConfig: ConnectorVersionInfraConfig
    connectorVersionLaunchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "PREVIEW",
        "GA",
        "DEPRECATED",
        "TEST",
        "PRIVATE_PREVIEW",
    ]
    createTime: str
    description: str
    destinationConfigs: _list[DestinationConfig]
    envoyImageLocation: str
    euaOauthAuthConfig: AuthConfig
    eventingConfig: EventingConfig
    eventingEnablementType: typing.Literal[
        "EVENTING_ENABLEMENT_TYPE_UNSPECIFIED",
        "EVENTING_AND_CONNECTION",
        "ONLY_EVENTING",
    ]
    eventingRuntimeData: EventingRuntimeData
    fallbackOnAdminCredentials: bool
    host: str
    imageLocation: str
    isTrustedTester: bool
    labels: dict[str, typing.Any]
    lockConfig: LockConfig
    logConfig: ConnectorsLogConfig
    name: str
    nodeConfig: NodeConfig
    serviceAccount: str
    serviceDirectory: str
    sslConfig: SslConfig
    status: ConnectionStatus
    subscriptionType: typing.Literal["SUBSCRIPTION_TYPE_UNSPECIFIED", "PAY_G", "PAID"]
    suspended: bool
    tlsServiceDirectory: str
    trafficShapingConfigs: _list[TrafficShapingConfig]
    updateTime: str

@typing.type_check_only
class ConnectionSchemaMetadata(typing.TypedDict, total=False):
    actions: _list[str]
    entities: _list[str]
    errorMessage: str
    name: str
    refreshTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "REFRESHING",
        "UPDATED",
        "REFRESHING_SCHEMA_METADATA",
        "UPDATED_SCHEMA_METADATA",
        "REFRESH_SCHEMA_METADATA_FAILED",
        "REFRESHING_FULL_SCHEMA",
        "UPDATED_FULL_SCHEMA",
    ]
    updateTime: str

@typing.type_check_only
class ConnectionStatus(typing.TypedDict, total=False):
    description: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "INACTIVE",
        "DELETING",
        "UPDATING",
        "ERROR",
        "AUTHORIZATION_REQUIRED",
    ]
    status: str

@typing.type_check_only
class Connector(typing.TypedDict, total=False):
    category: str
    connectorType: typing.Literal[
        "CONNECTOR_TYPE_UNSPECIFIED",
        "CONNECTOR_TYPE_GOOGLE",
        "CONNECTOR_TYPE_TECHNICAL",
        "CONNECTOR_TYPE_THIRD_PARTY",
    ]
    createTime: str
    description: str
    displayName: str
    documentationUri: str
    eventingDetails: EventingDetails
    externalUri: str
    labels: dict[str, typing.Any]
    launchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "PREVIEW",
        "GA",
        "DEPRECATED",
        "TEST",
        "PRIVATE_PREVIEW",
    ]
    marketplaceConnectorDetails: MarketplaceConnectorDetails
    name: str
    tags: _list[str]
    updateTime: str
    webAssetsLocation: str

@typing.type_check_only
class ConnectorInfraConfig(typing.TypedDict, total=False):
    alwaysAllocateCpu: bool
    connectionRatelimitWindowSeconds: str
    connectionServiceAccountEnabled: bool
    connectorVersioningEnabled: bool
    deploymentModel: typing.Literal[
        "DEPLOYMENT_MODEL_UNSPECIFIED", "GKE_MST", "CLOUD_RUN_MST"
    ]
    hpaConfig: HPAConfig
    internalclientRatelimitThreshold: str
    maxInstanceRequestConcurrency: int
    migrateDeploymentModel: bool
    migrateTls: bool
    networkEgressModeOverride: NetworkEgressModeOverride
    provisionCloudSpanner: bool
    provisionMemstore: bool
    publicNetworkIngressEnabled: bool
    ratelimitThreshold: str
    resourceLimits: ResourceLimits
    resourceRequests: ResourceRequests
    sharedDeployment: str

@typing.type_check_only
class ConnectorVersion(typing.TypedDict, total=False):
    authConfigTemplates: _list[AuthConfigTemplate]
    authOverrideEnabled: bool
    configVariableTemplates: _list[ConfigVariableTemplate]
    connectorInfraConfig: ConnectorInfraConfig
    createTime: str
    destinationConfigTemplates: _list[DestinationConfigTemplate]
    displayName: str
    egressControlConfig: EgressControlConfig
    eventingConfigTemplate: EventingConfigTemplate
    isCustomActionsSupported: bool
    isCustomEntitiesSupported: bool
    labels: dict[str, typing.Any]
    launchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "PREVIEW",
        "GA",
        "DEPRECATED",
        "TEST",
        "PRIVATE_PREVIEW",
    ]
    name: str
    releaseVersion: str
    roleGrant: RoleGrant
    roleGrants: _list[RoleGrant]
    schemaRefreshConfig: SchemaRefreshConfig
    sslConfigTemplate: SslConfigTemplate
    supportedRuntimeFeatures: SupportedRuntimeFeatures
    supportedStandardActions: _list[StandardAction]
    supportedStandardEntities: _list[StandardEntity]
    unsupportedConnectionTypes: _list[
        typing.Literal[
            "CONNECTION_TYPE_UNSPECIFIED",
            "CONNECTION_WITH_EVENTING",
            "ONLY_CONNECTION",
            "ONLY_EVENTING",
        ]
    ]
    updateTime: str
    vpcscConfig: VpcscConfig

@typing.type_check_only
class ConnectorVersionInfraConfig(typing.TypedDict, total=False):
    connectionRatelimitWindowSeconds: str
    deploymentModel: typing.Literal[
        "DEPLOYMENT_MODEL_UNSPECIFIED", "GKE_MST", "CLOUD_RUN_MST"
    ]
    deploymentModelMigrationState: typing.Literal[
        "DEPLOYMENT_MODEL_MIGRATION_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "COMPLETED",
        "ROLLEDBACK",
        "ROLLBACK_IN_PROGRESS",
    ]
    hpaConfig: HPAConfig
    internalclientRatelimitThreshold: str
    maxInstanceRequestConcurrency: int
    ratelimitThreshold: str
    resourceLimits: ResourceLimits
    resourceRequests: ResourceRequests
    sharedDeployment: str
    tlsMigrationState: typing.Literal[
        "TLS_MIGRATION_STATE_UNSPECIFIED",
        "TLS_MIGRATION_NOT_STARTED",
        "TLS_MIGRATION_COMPLETED",
    ]

@typing.type_check_only
class ConnectorsLogConfig(typing.TypedDict, total=False):
    enabled: bool
    level: typing.Literal["LOG_LEVEL_UNSPECIFIED", "ERROR", "INFO", "DEBUG"]

@typing.type_check_only
class CustomConnector(typing.TypedDict, total=False):
    activeConnectorVersions: _list[str]
    allConnectorVersions: _list[str]
    allMarketplaceVersions: _list[str]
    createTime: str
    customConnectorType: typing.Literal[
        "CUSTOM_CONNECTOR_TYPE_UNSPECIFIED", "OPEN_API", "PROTO", "SDK"
    ]
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    logo: str
    name: str
    publishedMarketplaceVersions: _list[str]
    updateTime: str

@typing.type_check_only
class CustomConnectorVersion(typing.TypedDict, total=False):
    asyncOperationsSupport: bool
    authConfig: AuthConfig
    authConfigTemplates: _list[AuthConfigTemplate]
    authOverrideSupport: bool
    backendVariableTemplates: _list[ConfigVariableTemplate]
    createTime: str
    destinationConfigs: _list[DestinationConfig]
    enableBackendDestinationConfig: bool
    labels: dict[str, typing.Any]
    name: str
    partnerMetadata: PartnerMetadata
    publishStatus: PublishStatus
    serviceAccount: str
    specLocation: str
    specServerUrls: _list[str]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED"]
    updateTime: str

@typing.type_check_only
class DailyCycle(typing.TypedDict, total=False):
    duration: str
    startTime: TimeOfDay

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeadLetterConfig(typing.TypedDict, total=False):
    projectId: str
    topic: str

@typing.type_check_only
class DenyMaintenancePeriod(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date
    time: TimeOfDay

@typing.type_check_only
class DeprecateCustomConnectorVersionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Destination(typing.TypedDict, total=False):
    host: str
    port: int
    serviceAttachment: str

@typing.type_check_only
class DestinationConfig(typing.TypedDict, total=False):
    destinations: _list[Destination]
    key: str

@typing.type_check_only
class DestinationConfigTemplate(typing.TypedDict, total=False):
    autocompleteSuggestions: _list[str]
    defaultPort: int
    description: str
    displayName: str
    isAdvanced: bool
    key: str
    max: int
    min: int
    portFieldType: typing.Literal[
        "FIELD_TYPE_UNSPECIFIED", "REQUIRED", "OPTIONAL", "NOT_USED"
    ]
    regexPattern: str

@typing.type_check_only
class EUASecret(typing.TypedDict, total=False):
    secretValue: str
    secretVersion: str

@typing.type_check_only
class EgressControlConfig(typing.TypedDict, total=False):
    accessMode: typing.Literal["ACCESS_MODE_UNSPECIFIED", "RESTRICTED", "ALLOW_ALL"]
    additionalExtractionRules: ExtractionRules
    allowlistedProjectNumbers: _list[str]
    backends: str
    extractionRules: ExtractionRules
    launchEnvironment: typing.Literal[
        "LAUNCH_ENVIRONMENT_UNSPECIFIED", "AUTOPUSH", "STAGING", "PROD"
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    encryptionType: typing.Literal["ENCRYPTION_TYPE_UNSPECIFIED", "GMEK", "CMEK"]
    kmsKeyName: str

@typing.type_check_only
class EncryptionKey(typing.TypedDict, total=False):
    kmsKeyName: str
    type: typing.Literal["TYPE_UNSPECIFIED", "GOOGLE_MANAGED", "CUSTOMER_MANAGED"]

@typing.type_check_only
class EndPoint(typing.TypedDict, total=False):
    endpointUri: str
    headers: _list[Header]

@typing.type_check_only
class EndUserAuthentication(typing.TypedDict, total=False):
    configVariables: _list[EndUserAuthenticationConfigVariable]
    createTime: str
    destinationConfigs: _list[DestinationConfig]
    endUserAuthenticationConfig: EndUserAuthenticationConfig
    labels: _list[str]
    name: str
    notifyEndpointDestination: EndUserAuthenticationNotifyEndpointDestination
    roles: _list[
        typing.Literal["ROLE_UNSPECIFIED", "READER", "READER_DOMAIN_WIDE_ACCESSIBLE"]
    ]
    status: EndUserAuthenticationEndUserAuthenticationStatus
    updateTime: str
    userId: str

@typing.type_check_only
class EndUserAuthenticationConfig(typing.TypedDict, total=False):
    additionalVariables: _list[EndUserAuthenticationConfigVariable]
    authKey: str
    authType: typing.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
        "GOOGLE_AUTHENTICATION",
        "OAUTH2_AUTH_CODE_FLOW_GOOGLE_MANAGED",
    ]
    oauth2AuthCodeFlow: EndUserAuthenticationConfigOauth2AuthCodeFlow
    oauth2AuthCodeFlowGoogleManaged: (
        EndUserAuthenticationConfigOauth2AuthCodeFlowGoogleManaged
    )
    oauth2ClientCredentials: EndUserAuthenticationConfigOauth2ClientCredentials
    oauth2JwtBearer: EndUserAuthenticationConfigOauth2JwtBearer
    sshPublicKey: EndUserAuthenticationConfigSshPublicKey
    userPassword: EndUserAuthenticationConfigUserPassword

@typing.type_check_only
class EndUserAuthenticationConfigOauth2AuthCodeFlow(typing.TypedDict, total=False):
    authCode: str
    authUri: str
    clientId: str
    clientSecret: EUASecret
    enablePkce: bool
    oauthTokenData: OAuthTokenData
    pkceVerifier: str
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class EndUserAuthenticationConfigOauth2AuthCodeFlowGoogleManaged(
    typing.TypedDict, total=False
):
    authCode: str
    oauthTokenData: OAuthTokenData
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class EndUserAuthenticationConfigOauth2ClientCredentials(typing.TypedDict, total=False):
    clientId: str
    clientSecret: EUASecret

@typing.type_check_only
class EndUserAuthenticationConfigOauth2JwtBearer(typing.TypedDict, total=False):
    clientKey: EUASecret
    jwtClaims: EndUserAuthenticationConfigOauth2JwtBearerJwtClaims

@typing.type_check_only
class EndUserAuthenticationConfigOauth2JwtBearerJwtClaims(
    typing.TypedDict, total=False
):
    audience: str
    issuer: str
    subject: str

@typing.type_check_only
class EndUserAuthenticationConfigSshPublicKey(typing.TypedDict, total=False):
    certType: str
    sshClientCert: EUASecret
    sshClientCertPass: EUASecret
    username: str

@typing.type_check_only
class EndUserAuthenticationConfigUserPassword(typing.TypedDict, total=False):
    password: EUASecret
    username: str

@typing.type_check_only
class EndUserAuthenticationConfigVariable(typing.TypedDict, total=False):
    boolValue: bool
    intValue: str
    key: str
    secretValue: EUASecret
    stringValue: str

@typing.type_check_only
class EndUserAuthenticationEndUserAuthenticationStatus(typing.TypedDict, total=False):
    description: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ERROR"]

@typing.type_check_only
class EndUserAuthenticationNotifyEndpointDestination(typing.TypedDict, total=False):
    endpoint: EndUserAuthenticationNotifyEndpointDestinationEndPoint
    serviceAccount: str
    type: typing.Literal["TYPE_UNSPECIFIED", "ENDPOINT"]

@typing.type_check_only
class EndUserAuthenticationNotifyEndpointDestinationEndPoint(
    typing.TypedDict, total=False
):
    endpointUri: str
    headers: _list[EndUserAuthenticationNotifyEndpointDestinationEndPointHeader]

@typing.type_check_only
class EndUserAuthenticationNotifyEndpointDestinationEndPointHeader(
    typing.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class EndpointAttachment(typing.TypedDict, total=False):
    createTime: str
    description: str
    endpointGlobalAccess: bool
    endpointIp: str
    labels: dict[str, typing.Any]
    name: str
    serviceAttachment: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "ACCEPTED",
        "REJECTED",
        "CLOSED",
        "FROZEN",
        "NEEDS_ATTENTION",
        "ACCEPTED_NOT_PROGRAMMED",
    ]
    updateTime: str

@typing.type_check_only
class EnrichmentConfig(typing.TypedDict, total=False):
    appendAcl: bool

@typing.type_check_only
class EnumOption(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class EventSubscription(typing.TypedDict, total=False):
    createTime: str
    destinations: EventSubscriptionDestination
    eventTypeId: str
    filter: str
    jms: JMS
    name: str
    status: EventSubscriptionStatus
    subscriber: str
    subscriberLink: str
    triggerConfigVariables: _list[ConfigVariable]
    updateTime: str

@typing.type_check_only
class EventSubscriptionDestination(typing.TypedDict, total=False):
    endpoint: EndPoint
    pubsub: PubSub
    serviceAccount: str
    type: typing.Literal["TYPE_UNSPECIFIED", "ENDPOINT", "GCS", "PUBSUB"]

@typing.type_check_only
class EventSubscriptionStatus(typing.TypedDict, total=False):
    description: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "UPDATING", "ACTIVE", "SUSPENDED", "ERROR"
    ]

@typing.type_check_only
class EventType(typing.TypedDict, total=False):
    createTime: str
    enrichedEventPayloadSchema: str
    entityType: str
    eventPayloadSchema: str
    eventTypeId: str
    idPath: str
    name: str
    updateTime: str

@typing.type_check_only
class EventingConfig(typing.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    allowedEventTypes: _list[str]
    authConfig: AuthConfig
    deadLetterConfig: DeadLetterConfig
    enrichmentConfig: EnrichmentConfig
    enrichmentEnabled: bool
    eventsListenerIngressEndpoint: str
    globalEventFilter: str
    listenerAuthConfig: AuthConfig
    privateConnectivityAllowlistedProjects: _list[str]
    privateConnectivityEnabled: bool
    proxyDestinationConfig: DestinationConfig
    registrationDestinationConfig: DestinationConfig
    sslConfig: SslConfig

@typing.type_check_only
class EventingConfigTemplate(typing.TypedDict, total=False):
    additionalVariables: _list[ConfigVariableTemplate]
    authConfigTemplates: _list[AuthConfigTemplate]
    autoRefresh: bool
    autoRegistrationSupported: bool
    encryptionKeyTemplate: ConfigVariableTemplate
    enrichmentSupported: bool
    eventListenerType: typing.Literal[
        "EVENT_LISTENER_TYPE_UNSPECIFIED", "WEBHOOK_LISTENER", "JMS_LISTENER"
    ]
    isEventingSupported: bool
    listenerAuthConfigTemplates: _list[AuthConfigTemplate]
    proxyDestinationConfig: DestinationConfigTemplate
    registrationDestinationConfig: DestinationConfigTemplate
    sslConfigTemplate: SslConfigTemplate
    triggerConfigVariables: _list[ConfigVariableTemplate]

@typing.type_check_only
class EventingDetails(typing.TypedDict, total=False):
    customEventTypes: bool
    description: str
    documentationLink: str
    iconLocation: str
    launchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "PREVIEW",
        "GA",
        "DEPRECATED",
        "TEST",
        "PRIVATE_PREVIEW",
    ]
    name: str
    searchTags: _list[str]
    subscriptionType: typing.Literal[
        "SUBSCRIPTION_TYPE_UNSPECIFIED", "SHARED", "USER_SPECIFIC"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "WEBHOOK", "JMS"]

@typing.type_check_only
class EventingRuntimeData(typing.TypedDict, total=False):
    eventsListenerEndpoint: str
    eventsListenerPscSa: str
    status: EventingStatus
    webhookData: WebhookData
    webhookSubscriptions: WebhookSubscriptions

@typing.type_check_only
class EventingStatus(typing.TypedDict, total=False):
    description: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ERROR", "INGRESS_ENDPOINT_REQUIRED"
    ]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtractionRule(typing.TypedDict, total=False):
    extractionRegex: str
    formatString: str
    source: Source

@typing.type_check_only
class ExtractionRules(typing.TypedDict, total=False):
    extractionRule: _list[ExtractionRule]

@typing.type_check_only
class FetchAuthSchemaResponse(typing.TypedDict, total=False):
    authSchemas: _list[AuthSchema]
    jsonSchema: JsonAuthSchema

@typing.type_check_only
class FetchConnectionToolspecOverrideRequest(typing.TypedDict, total=False):
    toolNames: _list[ToolName]

@typing.type_check_only
class FetchConnectionToolspecOverrideResponse(typing.TypedDict, total=False):
    toolspecOverride: ToolspecOverride

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_INT",
        "DATA_TYPE_SMALLINT",
        "DATA_TYPE_DOUBLE",
        "DATA_TYPE_DATE",
        "DATA_TYPE_DATETIME",
        "DATA_TYPE_TIME",
        "DATA_TYPE_STRING",
        "DATA_TYPE_LONG",
        "DATA_TYPE_BOOLEAN",
        "DATA_TYPE_DECIMAL",
        "DATA_TYPE_UUID",
        "DATA_TYPE_BLOB",
        "DATA_TYPE_BIT",
        "DATA_TYPE_TINYINT",
        "DATA_TYPE_INTEGER",
        "DATA_TYPE_BIGINT",
        "DATA_TYPE_FLOAT",
        "DATA_TYPE_REAL",
        "DATA_TYPE_NUMERIC",
        "DATA_TYPE_CHAR",
        "DATA_TYPE_VARCHAR",
        "DATA_TYPE_LONGVARCHAR",
        "DATA_TYPE_TIMESTAMP",
        "DATA_TYPE_NCHAR",
        "DATA_TYPE_NVARCHAR",
        "DATA_TYPE_LONGNVARCHAR",
        "DATA_TYPE_NULL",
        "DATA_TYPE_OTHER",
        "DATA_TYPE_JAVA_OBJECT",
        "DATA_TYPE_DISTINCT",
        "DATA_TYPE_STRUCT",
        "DATA_TYPE_ARRAY",
        "DATA_TYPE_CLOB",
        "DATA_TYPE_REF",
        "DATA_TYPE_DATALINK",
        "DATA_TYPE_ROWID",
        "DATA_TYPE_BINARY",
        "DATA_TYPE_VARBINARY",
        "DATA_TYPE_LONGVARBINARY",
        "DATA_TYPE_NCLOB",
        "DATA_TYPE_SQLXML",
        "DATA_TYPE_REF_CURSOR",
        "DATA_TYPE_TIME_WITH_TIMEZONE",
        "DATA_TYPE_TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    field: str
    jsonSchema: JsonSchema
    key: bool
    nullable: bool
    readonly: bool

@typing.type_check_only
class FieldComparison(typing.TypedDict, total=False):
    boolValue: bool
    comparator: typing.Literal["COMPARATOR_UNSPECIFIED", "EQUALS", "NOT_EQUALS"]
    intValue: str
    key: str
    stringValue: str

@typing.type_check_only
class GenerateConnectionToolspecOverrideRequest(typing.TypedDict, total=False):
    toolNames: _list[ToolName]

@typing.type_check_only
class GenerateConnectionToolspecOverrideResponse(typing.TypedDict, total=False):
    toolspecOverride: ToolspecOverride

@typing.type_check_only
class HPAConfig(typing.TypedDict, total=False):
    cpuUtilizationThreshold: str
    memoryUtilizationThreshold: str

@typing.type_check_only
class Header(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class InputParameter(typing.TypedDict, total=False):
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_INT",
        "DATA_TYPE_SMALLINT",
        "DATA_TYPE_DOUBLE",
        "DATA_TYPE_DATE",
        "DATA_TYPE_DATETIME",
        "DATA_TYPE_TIME",
        "DATA_TYPE_STRING",
        "DATA_TYPE_LONG",
        "DATA_TYPE_BOOLEAN",
        "DATA_TYPE_DECIMAL",
        "DATA_TYPE_UUID",
        "DATA_TYPE_BLOB",
        "DATA_TYPE_BIT",
        "DATA_TYPE_TINYINT",
        "DATA_TYPE_INTEGER",
        "DATA_TYPE_BIGINT",
        "DATA_TYPE_FLOAT",
        "DATA_TYPE_REAL",
        "DATA_TYPE_NUMERIC",
        "DATA_TYPE_CHAR",
        "DATA_TYPE_VARCHAR",
        "DATA_TYPE_LONGVARCHAR",
        "DATA_TYPE_TIMESTAMP",
        "DATA_TYPE_NCHAR",
        "DATA_TYPE_NVARCHAR",
        "DATA_TYPE_LONGNVARCHAR",
        "DATA_TYPE_NULL",
        "DATA_TYPE_OTHER",
        "DATA_TYPE_JAVA_OBJECT",
        "DATA_TYPE_DISTINCT",
        "DATA_TYPE_STRUCT",
        "DATA_TYPE_ARRAY",
        "DATA_TYPE_CLOB",
        "DATA_TYPE_REF",
        "DATA_TYPE_DATALINK",
        "DATA_TYPE_ROWID",
        "DATA_TYPE_BINARY",
        "DATA_TYPE_VARBINARY",
        "DATA_TYPE_LONGVARBINARY",
        "DATA_TYPE_NCLOB",
        "DATA_TYPE_SQLXML",
        "DATA_TYPE_REF_CURSOR",
        "DATA_TYPE_TIME_WITH_TIMEZONE",
        "DATA_TYPE_TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    jsonSchema: JsonSchema
    nullable: bool
    parameter: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    consumerDefinedName: str
    consumerProjectNumber: str
    createTime: str
    instanceType: str
    labels: dict[str, typing.Any]
    maintenancePolicyNames: dict[str, typing.Any]
    maintenanceSchedules: dict[str, typing.Any]
    maintenanceSettings: MaintenanceSettings
    name: str
    notificationParameters: dict[str, typing.Any]
    producerMetadata: dict[str, typing.Any]
    provisionedResources: _list[ProvisionedResource]
    slmInstanceTemplate: str
    sloMetadata: SloMetadata
    softwareVersions: dict[str, typing.Any]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    tenantProjectId: str
    updateTime: str

@typing.type_check_only
class JMS(typing.TypedDict, total=False):
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "QUEUE", "TOPIC"]

AlternativeJsonAuthSchema = typing.TypedDict(
    "AlternativeJsonAuthSchema",
    {
        "$schema": str,
        "oneOf": _list[AuthObject],
    },
    total=False,
)

@typing.type_check_only
class JsonAuthSchema(AlternativeJsonAuthSchema): ...

AlternativeJsonSchema = typing.TypedDict(
    "AlternativeJsonSchema",
    {
        "$comment": str,
        "$defs": dict[str, typing.Any],
        "$id": str,
        "$ref": str,
        "$schema": str,
        "additionalDetails": dict[str, typing.Any],
        "additionalItems": JsonSchema,
        "additionalProperties": JsonSchema,
        "allOf": _list[JsonSchema],
        "anyOf": _list[JsonSchema],
        "const": typing.Any,
        "contains": JsonSchema,
        "contentEncoding": str,
        "contentMediaType": str,
        "default": typing.Any,
        "definitions": dict[str, typing.Any],
        "dependencies": dict[str, typing.Any],
        "description": str,
        "else": JsonSchema,
        "enum": _list[typing.Any],
        "examples": _list[typing.Any],
        "exclusiveMaximum": typing.Any,
        "exclusiveMinimum": typing.Any,
        "format": str,
        "if": JsonSchema,
        "items": JsonSchema,
        "jdbcType": typing.Literal[
            "DATA_TYPE_UNSPECIFIED",
            "DATA_TYPE_INT",
            "DATA_TYPE_SMALLINT",
            "DATA_TYPE_DOUBLE",
            "DATA_TYPE_DATE",
            "DATA_TYPE_DATETIME",
            "DATA_TYPE_TIME",
            "DATA_TYPE_STRING",
            "DATA_TYPE_LONG",
            "DATA_TYPE_BOOLEAN",
            "DATA_TYPE_DECIMAL",
            "DATA_TYPE_UUID",
            "DATA_TYPE_BLOB",
            "DATA_TYPE_BIT",
            "DATA_TYPE_TINYINT",
            "DATA_TYPE_INTEGER",
            "DATA_TYPE_BIGINT",
            "DATA_TYPE_FLOAT",
            "DATA_TYPE_REAL",
            "DATA_TYPE_NUMERIC",
            "DATA_TYPE_CHAR",
            "DATA_TYPE_VARCHAR",
            "DATA_TYPE_LONGVARCHAR",
            "DATA_TYPE_TIMESTAMP",
            "DATA_TYPE_NCHAR",
            "DATA_TYPE_NVARCHAR",
            "DATA_TYPE_LONGNVARCHAR",
            "DATA_TYPE_NULL",
            "DATA_TYPE_OTHER",
            "DATA_TYPE_JAVA_OBJECT",
            "DATA_TYPE_DISTINCT",
            "DATA_TYPE_STRUCT",
            "DATA_TYPE_ARRAY",
            "DATA_TYPE_CLOB",
            "DATA_TYPE_REF",
            "DATA_TYPE_DATALINK",
            "DATA_TYPE_ROWID",
            "DATA_TYPE_BINARY",
            "DATA_TYPE_VARBINARY",
            "DATA_TYPE_LONGVARBINARY",
            "DATA_TYPE_NCLOB",
            "DATA_TYPE_SQLXML",
            "DATA_TYPE_REF_CURSOR",
            "DATA_TYPE_TIME_WITH_TIMEZONE",
            "DATA_TYPE_TIMESTAMP_WITH_TIMEZONE",
        ],
        "maxItems": int,
        "maxLength": int,
        "maxProperties": int,
        "maximum": typing.Any,
        "minItems": int,
        "minLength": int,
        "minProperties": int,
        "minimum": typing.Any,
        "multipleOf": float,
        "not": JsonSchema,
        "oneOf": _list[JsonSchema],
        "pattern": str,
        "patternProperties": dict[str, typing.Any],
        "properties": dict[str, typing.Any],
        "propertyNames": JsonSchema,
        "readOnly": bool,
        "required": _list[str],
        "then": JsonSchema,
        "title": str,
        "type": _list[str],
        "uniqueItems": bool,
        "writeOnly": bool,
    },
    total=False,
)

@typing.type_check_only
class JsonSchema(AlternativeJsonSchema): ...

@typing.type_check_only
class JwtClaims(typing.TypedDict, total=False):
    audience: str
    issuer: str
    subject: str

@typing.type_check_only
class ListActionsResponse(typing.TypedDict, total=False):
    actions: _list[RuntimeActionSchema]
    nextPageToken: str

@typing.type_check_only
class ListConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorVersionsResponse(typing.TypedDict, total=False):
    connectorVersions: _list[ConnectorVersion]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorsResponse(typing.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCustomConnectorVersionsResponse(typing.TypedDict, total=False):
    customConnectorVersions: _list[CustomConnectorVersion]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCustomConnectorsResponse(typing.TypedDict, total=False):
    customConnectors: _list[CustomConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEndUserAuthenticationsResponse(typing.TypedDict, total=False):
    endUserAuthentications: _list[EndUserAuthentication]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEndpointAttachmentsResponse(typing.TypedDict, total=False):
    endpointAttachments: _list[EndpointAttachment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEntityTypesResponse(typing.TypedDict, total=False):
    entityTypes: _list[RuntimeEntitySchema]
    nextPageToken: str

@typing.type_check_only
class ListEventSubscriptionsResponse(typing.TypedDict, total=False):
    eventSubscriptions: _list[EventSubscription]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEventTypesResponse(typing.TypedDict, total=False):
    eventTypes: _list[EventType]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListManagedZonesResponse(typing.TypedDict, total=False):
    managedZones: _list[ManagedZone]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListProvidersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    providers: _list[Provider]
    unreachable: _list[str]

@typing.type_check_only
class ListRuntimeActionSchemasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    runtimeActionSchemas: _list[RuntimeActionSchema]

@typing.type_check_only
class ListRuntimeEntitySchemasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    runtimeEntitySchemas: _list[RuntimeEntitySchema]

@typing.type_check_only
class ListenEventRequest(typing.TypedDict, total=False):
    payload: dict[str, typing.Any]

@typing.type_check_only
class ListenEventResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LockConfig(typing.TypedDict, total=False):
    locked: bool
    reason: str

@typing.type_check_only
class LogicalExpression(typing.TypedDict, total=False):
    fieldComparisons: _list[FieldComparison]
    logicalExpressions: _list[LogicalExpression]
    logicalOperator: typing.Literal["OPERATOR_UNSPECIFIED", "AND", "OR"]

@typing.type_check_only
class MaintenancePolicy(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "READY", "DELETING"]
    updatePolicy: UpdatePolicy
    updateTime: str

@typing.type_check_only
class MaintenanceSchedule(typing.TypedDict, total=False):
    canReschedule: bool
    endTime: str
    rolloutManagementPolicy: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class MaintenanceSettings(typing.TypedDict, total=False):
    exclude: bool
    isRollback: bool
    maintenancePolicies: dict[str, typing.Any]

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    dailyCycle: DailyCycle
    weeklyCycle: WeeklyCycle

@typing.type_check_only
class ManagedZone(typing.TypedDict, total=False):
    createTime: str
    description: str
    dns: str
    labels: dict[str, typing.Any]
    name: str
    targetProject: str
    targetVpc: str
    updateTime: str

@typing.type_check_only
class MarketplaceConnectorDetails(typing.TypedDict, total=False):
    marketplaceProduct: str
    marketplaceProductId: str
    marketplaceProductUri: str
    partner: str

@typing.type_check_only
class ModifyConnectionToolspecOverrideRequest(typing.TypedDict, total=False):
    toolspecOverride: ToolspecOverride

@typing.type_check_only
class ModifyConnectionToolspecOverrideResponse(typing.TypedDict, total=False):
    toolspecOverrides: ToolspecOverride

@typing.type_check_only
class MultipleSelectConfig(typing.TypedDict, total=False):
    allowCustomValues: bool
    multipleSelectOptions: _list[MultipleSelectOption]
    valueSeparator: str

@typing.type_check_only
class MultipleSelectOption(typing.TypedDict, total=False):
    description: str
    displayName: str
    key: str
    preselected: bool

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    egressIps: _list[str]
    egressMode: typing.Literal[
        "NETWORK_EGRESS_MODE_UNSPECIFIED", "AUTO_IP", "STATIC_IP"
    ]

@typing.type_check_only
class NetworkEgressModeOverride(typing.TypedDict, total=False):
    isEventingOverrideEnabled: bool
    isJobsOverrideEnabled: bool
    networkEgressMode: typing.Literal[
        "NETWORK_EGRESS_MODE_UNSPECIFIED",
        "SERVERLESS_VPC_ACCESS_CONNECTOR",
        "DIRECT_VPC_EGRESS",
    ]

@typing.type_check_only
class NodeConfig(typing.TypedDict, total=False):
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class NodeSloMetadata(typing.TypedDict, total=False):
    location: str
    nodeId: str
    perSliEligibility: PerSliSloEligibility

@typing.type_check_only
class NotificationParameter(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class OAuthTokenData(typing.TypedDict, total=False):
    accessToken: EUASecret
    createTime: str
    expiry: str
    refreshToken: EUASecret

@typing.type_check_only
class Oauth2AuthCodeFlow(typing.TypedDict, total=False):
    authCode: str
    authUri: str
    clientId: str
    clientSecret: Secret
    enablePkce: bool
    pkceVerifier: str
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class Oauth2AuthCodeFlowGoogleManaged(typing.TypedDict, total=False):
    authCode: str
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class Oauth2ClientCredentials(typing.TypedDict, total=False):
    clientId: str
    clientSecret: Secret

@typing.type_check_only
class Oauth2JwtBearer(typing.TypedDict, total=False):
    clientKey: Secret
    jwtClaims: JwtClaims

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PartnerMetadata(typing.TypedDict, total=False):
    acceptGcpTos: bool
    additionalComments: str
    confirmPartnerRequirements: bool
    demoUri: str
    hasDynamicSpecUri: bool
    integrationTemplates: str
    localSpecPath: str
    marketplaceProduct: str
    marketplaceProductId: str
    marketplaceProductProjectId: str
    marketplaceProductUri: str
    partner: str
    partnerConnectorDisplayName: str
    publishRequestTime: str
    targetApplication: str
    targetCustomerSegment: str
    useCases: str

@typing.type_check_only
class PerSliSloEligibility(typing.TypedDict, total=False):
    eligibilities: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Provider(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    documentationUri: str
    externalUri: str
    labels: dict[str, typing.Any]
    launchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "PREVIEW",
        "GA",
        "DEPRECATED",
        "TEST",
        "PRIVATE_PREVIEW",
    ]
    name: str
    updateTime: str
    webAssetsLocation: str

@typing.type_check_only
class ProvisionedResource(typing.TypedDict, total=False):
    resourceType: str
    resourceUrl: str

@typing.type_check_only
class PubSub(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    configVariables: _list[ConfigVariable]
    projectId: str
    topicId: str

@typing.type_check_only
class PublishCustomConnectorVersionRequest(typing.TypedDict, total=False):
    partnerMetadata: PartnerMetadata

@typing.type_check_only
class PublishStatus(typing.TypedDict, total=False):
    publishState: typing.Literal[
        "PUBLISH_STATE_UNSPECIFIED", "PUBLISHED", "PUBLISH_IN_PROGRESS", "UNPUBLISHED"
    ]
    publishTime: str
    publishedAs: str
    publishedSource: str

@typing.type_check_only
class RefreshConnectionSchemaMetadataRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RegionalSettings(typing.TypedDict, total=False):
    client: str
    encryptionConfig: EncryptionConfig
    name: str
    networkConfig: NetworkConfig
    provisioned: bool

@typing.type_check_only
class RemoveConnectionToolspecOverrideRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RepairEventingRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Resource(typing.TypedDict, total=False):
    pathTemplate: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "GCP_PROJECT",
        "GCP_RESOURCE",
        "GCP_SECRETMANAGER_SECRET",
        "GCP_SECRETMANAGER_SECRET_VERSION",
    ]

@typing.type_check_only
class ResourceLimits(typing.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class ResourceRequests(typing.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class ResultMetadata(typing.TypedDict, total=False):
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_INT",
        "DATA_TYPE_SMALLINT",
        "DATA_TYPE_DOUBLE",
        "DATA_TYPE_DATE",
        "DATA_TYPE_DATETIME",
        "DATA_TYPE_TIME",
        "DATA_TYPE_STRING",
        "DATA_TYPE_LONG",
        "DATA_TYPE_BOOLEAN",
        "DATA_TYPE_DECIMAL",
        "DATA_TYPE_UUID",
        "DATA_TYPE_BLOB",
        "DATA_TYPE_BIT",
        "DATA_TYPE_TINYINT",
        "DATA_TYPE_INTEGER",
        "DATA_TYPE_BIGINT",
        "DATA_TYPE_FLOAT",
        "DATA_TYPE_REAL",
        "DATA_TYPE_NUMERIC",
        "DATA_TYPE_CHAR",
        "DATA_TYPE_VARCHAR",
        "DATA_TYPE_LONGVARCHAR",
        "DATA_TYPE_TIMESTAMP",
        "DATA_TYPE_NCHAR",
        "DATA_TYPE_NVARCHAR",
        "DATA_TYPE_LONGNVARCHAR",
        "DATA_TYPE_NULL",
        "DATA_TYPE_OTHER",
        "DATA_TYPE_JAVA_OBJECT",
        "DATA_TYPE_DISTINCT",
        "DATA_TYPE_STRUCT",
        "DATA_TYPE_ARRAY",
        "DATA_TYPE_CLOB",
        "DATA_TYPE_REF",
        "DATA_TYPE_DATALINK",
        "DATA_TYPE_ROWID",
        "DATA_TYPE_BINARY",
        "DATA_TYPE_VARBINARY",
        "DATA_TYPE_LONGVARBINARY",
        "DATA_TYPE_NCLOB",
        "DATA_TYPE_SQLXML",
        "DATA_TYPE_REF_CURSOR",
        "DATA_TYPE_TIME_WITH_TIMEZONE",
        "DATA_TYPE_TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    field: str
    jsonSchema: JsonSchema
    nullable: bool

@typing.type_check_only
class RetryEventSubscriptionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RoleGrant(typing.TypedDict, total=False):
    helperTextTemplate: str
    principal: typing.Literal["PRINCIPAL_UNSPECIFIED", "CONNECTOR_SA"]
    resource: Resource
    roles: _list[str]

@typing.type_check_only
class RuntimeActionSchema(typing.TypedDict, total=False):
    action: str
    description: str
    displayName: str
    inputJsonSchema: JsonSchema
    inputParameters: _list[InputParameter]
    inputSchemaAsString: str
    resultJsonSchema: JsonSchema
    resultMetadata: _list[ResultMetadata]
    resultSchemaAsString: str

@typing.type_check_only
class RuntimeConfig(typing.TypedDict, total=False):
    conndSubscription: str
    conndTopic: str
    controlPlaneSubscription: str
    controlPlaneTopic: str
    locationId: str
    name: str
    runtimeEndpoint: str
    schemaGcsBucket: str
    serviceDirectory: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "UPDATING",
    ]

@typing.type_check_only
class RuntimeEntitySchema(typing.TypedDict, total=False):
    entity: str
    fields: _list[Field]
    jsonSchema: JsonSchema
    operations: _list[
        typing.Literal[
            "OPERATION_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
        ]
    ]

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
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
    duration: str
    startTime: TimeOfDay

@typing.type_check_only
class SchemaRefreshConfig(typing.TypedDict, total=False):
    useActionDisplayNames: bool
    useSynchronousSchemaRefresh: bool

@typing.type_check_only
class SearchConnectionInstance(typing.TypedDict, total=False):
    actionSchema: RuntimeActionSchema
    connection: Connection
    entitySchema: RuntimeEntitySchema

@typing.type_check_only
class SearchConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[SearchConnectionInstance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class Secret(typing.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Settings(typing.TypedDict, total=False):
    name: str
    payg: bool
    tenantProjectId: str
    vpcsc: bool

@typing.type_check_only
class SloEligibility(typing.TypedDict, total=False):
    eligible: bool
    reason: str

@typing.type_check_only
class SloMetadata(typing.TypedDict, total=False):
    nodes: _list[NodeSloMetadata]
    perSliEligibility: PerSliSloEligibility
    tier: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    fieldId: str
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED", "CONFIG_VARIABLE", "AUTH_CONFIG_VARIABLE"
    ]

@typing.type_check_only
class SshPublicKey(typing.TypedDict, total=False):
    certType: str
    sshClientCert: Secret
    sshClientCertPass: Secret
    username: str

@typing.type_check_only
class SslConfig(typing.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    clientCertType: typing.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]
    clientCertificate: Secret
    clientPrivateKey: Secret
    clientPrivateKeyPass: Secret
    privateServerCertificate: Secret
    serverCertType: typing.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]
    trustModel: typing.Literal["PUBLIC", "PRIVATE", "INSECURE"]
    type: typing.Literal["SSL_TYPE_UNSPECIFIED", "TLS", "MTLS"]
    useSsl: bool

@typing.type_check_only
class SslConfigTemplate(typing.TypedDict, total=False):
    additionalVariables: _list[ConfigVariableTemplate]
    clientCertType: _list[typing.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]]
    isTlsMandatory: bool
    serverCertType: _list[typing.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]]
    sslType: typing.Literal["SSL_TYPE_UNSPECIFIED", "TLS", "MTLS"]

@typing.type_check_only
class StandardAction(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class StandardEntity(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringListValues(typing.TypedDict, total=False):
    listValues: _list[str]

@typing.type_check_only
class SupportedRuntimeFeatures(typing.TypedDict, total=False):
    actionApis: bool
    asyncOperations: bool
    entityApis: bool
    sqlQuery: bool

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class ToolName(typing.TypedDict, total=False):
    entityType: str
    name: str
    operation: typing.Literal[
        "OPERATION_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
    ]

@typing.type_check_only
class ToolspecOverride(typing.TypedDict, total=False):
    baseVersion: str
    createTime: str
    tools: _list[dict[str, typing.Any]]
    updateTime: str

@typing.type_check_only
class TrafficShapingConfig(typing.TypedDict, total=False):
    duration: str
    quotaLimit: str

@typing.type_check_only
class UpdatePolicy(typing.TypedDict, total=False):
    channel: typing.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class UserPassword(typing.TypedDict, total=False):
    password: Secret
    username: str

@typing.type_check_only
class ValidateCustomConnectorSpecRequest(typing.TypedDict, total=False):
    serviceAccount: str
    specLocation: str
    specType: typing.Literal[
        "CUSTOM_CONNECTOR_TYPE_UNSPECIFIED", "OPEN_API", "PROTO", "SDK"
    ]

@typing.type_check_only
class ValidateCustomConnectorSpecResponse(typing.TypedDict, total=False):
    errorMessage: str

@typing.type_check_only
class VpcscConfig(typing.TypedDict, total=False):
    defaultAllowlistedHost: _list[str]
    disableFirewallVpcscFlow: bool

@typing.type_check_only
class WebhookData(typing.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    createTime: str
    eventSubscriptions: _list[str]
    eventTypes: _list[str]
    id: str
    name: str
    nextRefreshTime: str
    updateTime: str

@typing.type_check_only
class WebhookSubscriptions(typing.TypedDict, total=False):
    webhookData: _list[WebhookData]

@typing.type_check_only
class WeeklyCycle(typing.TypedDict, total=False):
    schedule: _list[Schedule]

@typing.type_check_only
class WithdrawCustomConnectorVersionRequest(typing.TypedDict, total=False): ...
