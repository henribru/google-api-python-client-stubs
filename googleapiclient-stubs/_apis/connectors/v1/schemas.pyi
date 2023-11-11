import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthConfig(typing_extensions.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    authKey: str
    authType: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
    ]
    oauth2AuthCodeFlow: Oauth2AuthCodeFlow
    oauth2ClientCredentials: Oauth2ClientCredentials
    oauth2JwtBearer: Oauth2JwtBearer
    sshPublicKey: SshPublicKey
    userPassword: UserPassword

@typing.type_check_only
class AuthConfigTemplate(typing_extensions.TypedDict, total=False):
    authKey: str
    authType: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
    ]
    configVariableTemplates: _list[ConfigVariableTemplate]
    description: str
    displayName: str

@typing.type_check_only
class AuthorizationCodeLink(typing_extensions.TypedDict, total=False):
    clientId: str
    enablePkce: bool
    scopes: _list[str]
    uri: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConfigVariable(typing_extensions.TypedDict, total=False):
    boolValue: bool
    encryptionKeyValue: EncryptionKey
    intValue: str
    key: str
    secretValue: Secret
    stringValue: str

@typing.type_check_only
class ConfigVariableTemplate(typing_extensions.TypedDict, total=False):
    authorizationCodeLink: AuthorizationCodeLink
    description: str
    displayName: str
    enumOptions: _list[EnumOption]
    isAdvanced: bool
    key: str
    required: bool
    requiredCondition: LogicalExpression
    roleGrant: RoleGrant
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED"]
    validationRegex: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "STRING",
        "INT",
        "BOOL",
        "SECRET",
        "ENUM",
        "AUTHORIZATION_CODE",
        "ENCRYPTION_KEY",
    ]

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    authConfig: AuthConfig
    configVariables: _list[ConfigVariable]
    connectionRevision: str
    connectorVersion: str
    connectorVersionInfraConfig: ConnectorVersionInfraConfig
    connectorVersionLaunchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED", "PRIVATE_PREVIEW"
    ]
    createTime: str
    description: str
    destinationConfigs: _list[DestinationConfig]
    envoyImageLocation: str
    eventingConfig: EventingConfig
    eventingEnablementType: typing_extensions.Literal[
        "EVENTING_ENABLEMENT_TYPE_UNSPECIFIED",
        "EVENTING_AND_CONNECTION",
        "ONLY_EVENTING",
    ]
    eventingRuntimeData: EventingRuntimeData
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
    subscriptionType: typing_extensions.Literal[
        "SUBSCRIPTION_TYPE_UNSPECIFIED", "PAY_G", "PAID"
    ]
    suspended: bool
    updateTime: str

@typing.type_check_only
class ConnectionSchemaMetadata(typing_extensions.TypedDict, total=False):
    actions: _list[str]
    entities: _list[str]
    name: str
    refreshTime: str
    state: typing_extensions.Literal[
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
class ConnectionStatus(typing_extensions.TypedDict, total=False):
    description: str
    state: typing_extensions.Literal[
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
class Connector(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    documentationUri: str
    eventingDetails: EventingDetails
    externalUri: str
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED", "PRIVATE_PREVIEW"
    ]
    name: str
    updateTime: str
    webAssetsLocation: str

@typing.type_check_only
class ConnectorInfraConfig(typing_extensions.TypedDict, total=False):
    connectionRatelimitWindowSeconds: str
    deploymentModel: typing_extensions.Literal[
        "DEPLOYMENT_MODEL_UNSPECIFIED", "GKE_MST", "CLOUD_RUN_MST"
    ]
    hpaConfig: HPAConfig
    internalclientRatelimitThreshold: str
    ratelimitThreshold: str
    resourceLimits: ResourceLimits
    resourceRequests: ResourceRequests
    sharedDeployment: str

@typing.type_check_only
class ConnectorVersion(typing_extensions.TypedDict, total=False):
    authConfigTemplates: _list[AuthConfigTemplate]
    configVariableTemplates: _list[ConfigVariableTemplate]
    connectorInfraConfig: ConnectorInfraConfig
    createTime: str
    destinationConfigTemplates: _list[DestinationConfigTemplate]
    displayName: str
    egressControlConfig: EgressControlConfig
    eventingConfigTemplate: EventingConfigTemplate
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED", "PRIVATE_PREVIEW"
    ]
    name: str
    releaseVersion: str
    roleGrant: RoleGrant
    roleGrants: _list[RoleGrant]
    sslConfigTemplate: SslConfigTemplate
    supportedRuntimeFeatures: SupportedRuntimeFeatures
    updateTime: str

@typing.type_check_only
class ConnectorVersionInfraConfig(typing_extensions.TypedDict, total=False):
    connectionRatelimitWindowSeconds: str
    hpaConfig: HPAConfig
    internalclientRatelimitThreshold: str
    ratelimitThreshold: str
    resourceLimits: ResourceLimits
    resourceRequests: ResourceRequests
    sharedDeployment: str

@typing.type_check_only
class ConnectorsLogConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Destination(typing_extensions.TypedDict, total=False):
    host: str
    port: int
    serviceAttachment: str

@typing.type_check_only
class DestinationConfig(typing_extensions.TypedDict, total=False):
    destinations: _list[Destination]
    key: str

@typing.type_check_only
class DestinationConfigTemplate(typing_extensions.TypedDict, total=False):
    defaultPort: int
    description: str
    displayName: str
    isAdvanced: bool
    key: str
    max: int
    min: int
    portFieldType: typing_extensions.Literal[
        "FIELD_TYPE_UNSPECIFIED", "REQUIRED", "OPTIONAL", "NOT_USED"
    ]
    regexPattern: str

@typing.type_check_only
class EgressControlConfig(typing_extensions.TypedDict, total=False):
    backends: str
    extractionRules: ExtractionRules

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    encryptionType: typing_extensions.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED", "GMEK", "CMEK"
    ]
    kmsKeyName: str

@typing.type_check_only
class EncryptionKey(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GOOGLE_MANAGED", "CUSTOMER_MANAGED"
    ]

@typing.type_check_only
class EndPoint(typing_extensions.TypedDict, total=False):
    endpointUri: str
    headers: _list[Header]

@typing.type_check_only
class EndpointAttachment(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    endpointIp: str
    labels: dict[str, typing.Any]
    name: str
    serviceAttachment: str
    updateTime: str

@typing.type_check_only
class EnumOption(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class EventSubscription(typing_extensions.TypedDict, total=False):
    createTime: str
    destinations: EventSubscriptionDestination
    eventTypeId: str
    jms: JMS
    name: str
    status: EventSubscriptionStatus
    subscriber: str
    subscriberLink: str
    updateTime: str

@typing.type_check_only
class EventSubscriptionDestination(typing_extensions.TypedDict, total=False):
    endpoint: EndPoint
    serviceAccount: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ENDPOINT"]

@typing.type_check_only
class EventSubscriptionStatus(typing_extensions.TypedDict, total=False):
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "UPDATING", "ACTIVE", "SUSPENDED", "ERROR"
    ]

@typing.type_check_only
class EventType(typing_extensions.TypedDict, total=False):
    createTime: str
    enrichedEventPayloadSchema: str
    entityType: str
    eventPayloadSchema: str
    eventTypeId: str
    idPath: str
    name: str
    updateTime: str

@typing.type_check_only
class EventingConfig(typing_extensions.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    authConfig: AuthConfig
    encryptionKey: ConfigVariable
    enrichmentEnabled: bool
    eventsListenerIngressEndpoint: str
    privateConnectivityEnabled: bool
    registrationDestinationConfig: DestinationConfig

@typing.type_check_only
class EventingConfigTemplate(typing_extensions.TypedDict, total=False):
    additionalVariables: _list[ConfigVariableTemplate]
    authConfigTemplates: _list[AuthConfigTemplate]
    autoRefresh: bool
    autoRegistrationSupported: bool
    encryptionKeyTemplate: ConfigVariableTemplate
    enrichmentSupported: bool
    eventListenerType: typing_extensions.Literal[
        "EVENT_LISTENER_TYPE_UNSPECIFIED", "WEBHOOK_LISTENER", "JMS_LISTENER"
    ]
    isEventingSupported: bool
    registrationDestinationConfig: DestinationConfigTemplate

@typing.type_check_only
class EventingDetails(typing_extensions.TypedDict, total=False):
    customEventTypes: bool
    description: str
    documentationLink: str
    iconLocation: str
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED", "PRIVATE_PREVIEW"
    ]
    name: str
    searchTags: _list[str]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "WEBHOOK", "JMS"]

@typing.type_check_only
class EventingRuntimeData(typing_extensions.TypedDict, total=False):
    eventsListenerEndpoint: str
    eventsListenerPscSa: str
    status: EventingStatus

@typing.type_check_only
class EventingStatus(typing_extensions.TypedDict, total=False):
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ERROR", "INGRESS_ENDPOINT_REQUIRED"
    ]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtractionRule(typing_extensions.TypedDict, total=False):
    extractionRegex: str
    source: Source

@typing.type_check_only
class ExtractionRules(typing_extensions.TypedDict, total=False):
    extractionRule: _list[ExtractionRule]

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing_extensions.Literal[
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
class FieldComparison(typing_extensions.TypedDict, total=False):
    boolValue: bool
    comparator: typing_extensions.Literal[
        "COMPARATOR_UNSPECIFIED", "EQUALS", "NOT_EQUALS"
    ]
    intValue: str
    key: str
    stringValue: str

@typing.type_check_only
class HPAConfig(typing_extensions.TypedDict, total=False):
    cpuUtilizationThreshold: str
    memoryUtilizationThreshold: str

@typing.type_check_only
class Header(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class InputParameter(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
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
class JMS(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "QUEUE", "TOPIC"]

@typing.type_check_only
class JsonSchema(typing_extensions.TypedDict, total=False):
    default: typing.Any
    description: str
    enum: _list[typing.Any]
    format: str
    items: JsonSchema
    jdbcType: typing_extensions.Literal[
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
    properties: dict[str, typing.Any]
    required: _list[str]
    type: _list[str]

@typing.type_check_only
class JwtClaims(typing_extensions.TypedDict, total=False):
    audience: str
    issuer: str
    subject: str

@typing.type_check_only
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorVersionsResponse(typing_extensions.TypedDict, total=False):
    connectorVersions: _list[ConnectorVersion]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorsResponse(typing_extensions.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEndpointAttachmentsResponse(typing_extensions.TypedDict, total=False):
    endpointAttachments: _list[EndpointAttachment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEventSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    eventSubscriptions: _list[EventSubscription]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEventTypesResponse(typing_extensions.TypedDict, total=False):
    eventTypes: _list[EventType]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListManagedZonesResponse(typing_extensions.TypedDict, total=False):
    managedZones: _list[ManagedZone]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListProvidersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    providers: _list[Provider]
    unreachable: _list[str]

@typing.type_check_only
class ListRuntimeActionSchemasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    runtimeActionSchemas: _list[RuntimeActionSchema]

@typing.type_check_only
class ListRuntimeEntitySchemasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    runtimeEntitySchemas: _list[RuntimeEntitySchema]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LockConfig(typing_extensions.TypedDict, total=False):
    locked: bool
    reason: str

@typing.type_check_only
class LogicalExpression(typing_extensions.TypedDict, total=False):
    fieldComparisons: _list[FieldComparison]
    logicalExpressions: _list[LogicalExpression]
    logicalOperator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND", "OR"]

@typing.type_check_only
class ManagedZone(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    dns: str
    labels: dict[str, typing.Any]
    name: str
    targetProject: str
    targetVpc: str
    updateTime: str

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    egressIps: _list[str]
    egressMode: typing_extensions.Literal[
        "NETWORK_EGRESS_MODE_UNSPECIFIED", "AUTO_IP", "STATIC_IP"
    ]

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class Oauth2AuthCodeFlow(typing_extensions.TypedDict, total=False):
    authCode: str
    authUri: str
    clientId: str
    clientSecret: Secret
    enablePkce: bool
    pkceVerifier: str
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class Oauth2ClientCredentials(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: Secret

@typing.type_check_only
class Oauth2JwtBearer(typing_extensions.TypedDict, total=False):
    clientKey: Secret
    jwtClaims: JwtClaims

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Provider(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    documentationUri: str
    externalUri: str
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED", "PRIVATE_PREVIEW"
    ]
    name: str
    updateTime: str
    webAssetsLocation: str

@typing.type_check_only
class RefreshConnectionSchemaMetadataRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class RegionalSettings(typing_extensions.TypedDict, total=False):
    encryptionConfig: EncryptionConfig
    name: str
    networkConfig: NetworkConfig

@typing.type_check_only
class RepairEventingRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    pathTemplate: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "GCP_PROJECT",
        "GCP_RESOURCE",
        "GCP_SECRETMANAGER_SECRET",
        "GCP_SECRETMANAGER_SECRET_VERSION",
    ]

@typing.type_check_only
class ResourceLimits(typing_extensions.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class ResourceRequests(typing_extensions.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class ResultMetadata(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
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
    description: str
    field: str
    jsonSchema: JsonSchema

@typing.type_check_only
class RetryEventSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RoleGrant(typing_extensions.TypedDict, total=False):
    helperTextTemplate: str
    principal: typing_extensions.Literal["PRINCIPAL_UNSPECIFIED", "CONNECTOR_SA"]
    resource: Resource
    roles: _list[str]

@typing.type_check_only
class RuntimeActionSchema(typing_extensions.TypedDict, total=False):
    action: str
    description: str
    displayName: str
    inputJsonSchema: JsonSchema
    inputParameters: _list[InputParameter]
    resultJsonSchema: JsonSchema
    resultMetadata: _list[ResultMetadata]

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    conndSubscription: str
    conndTopic: str
    controlPlaneSubscription: str
    controlPlaneTopic: str
    locationId: str
    name: str
    runtimeEndpoint: str
    schemaGcsBucket: str
    serviceDirectory: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "UPDATING",
    ]

@typing.type_check_only
class RuntimeEntitySchema(typing_extensions.TypedDict, total=False):
    entity: str
    fields: _list[Field]
    jsonSchema: JsonSchema

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    name: str
    payg: bool
    tenantProjectId: str
    vpcsc: bool

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    fieldId: str
    sourceType: typing_extensions.Literal["SOURCE_TYPE_UNSPECIFIED", "CONFIG_VARIABLE"]

@typing.type_check_only
class SshPublicKey(typing_extensions.TypedDict, total=False):
    certType: str
    sshClientCert: Secret
    sshClientCertPass: Secret
    username: str

@typing.type_check_only
class SslConfig(typing_extensions.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    clientCertType: typing_extensions.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]
    clientCertificate: Secret
    clientPrivateKey: Secret
    clientPrivateKeyPass: Secret
    privateServerCertificate: Secret
    serverCertType: typing_extensions.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]
    trustModel: typing_extensions.Literal["PUBLIC", "PRIVATE", "INSECURE"]
    type: typing_extensions.Literal["SSL_TYPE_UNSPECIFIED", "TLS", "MTLS"]
    useSsl: bool

@typing.type_check_only
class SslConfigTemplate(typing_extensions.TypedDict, total=False):
    additionalVariables: _list[ConfigVariableTemplate]
    clientCertType: _list[str]
    isTlsMandatory: bool
    serverCertType: _list[str]
    sslType: typing_extensions.Literal["SSL_TYPE_UNSPECIFIED", "TLS", "MTLS"]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SupportedRuntimeFeatures(typing_extensions.TypedDict, total=False):
    actionApis: bool
    entityApis: bool
    sqlQuery: bool

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UserPassword(typing_extensions.TypedDict, total=False):
    password: Secret
    username: str
