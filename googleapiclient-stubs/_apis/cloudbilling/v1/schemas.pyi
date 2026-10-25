import typing

_list = list

@typing.type_check_only
class APIKeySecurityScheme(typing.TypedDict, total=False):
    description: str
    location: str
    name: str

@typing.type_check_only
class AgentCapabilities(typing.TypedDict, total=False):
    extensions: _list[AgentExtension]
    pushNotifications: bool
    streaming: bool

@typing.type_check_only
class AgentCard(typing.TypedDict, total=False):
    additionalInterfaces: _list[AgentInterface]
    capabilities: AgentCapabilities
    defaultInputModes: _list[str]
    defaultOutputModes: _list[str]
    description: str
    documentationUrl: str
    iconUrl: str
    name: str
    preferredTransport: str
    protocolVersion: str
    provider: AgentProvider
    security: _list[Security]
    securitySchemes: dict[str, typing.Any]
    signatures: _list[AgentCardSignature]
    skills: _list[AgentSkill]
    supportsAuthenticatedExtendedCard: bool
    url: str
    version: str

@typing.type_check_only
class AgentCardSignature(typing.TypedDict, total=False):
    header: dict[str, typing.Any]
    protected: str
    signature: str

@typing.type_check_only
class AgentExtension(typing.TypedDict, total=False):
    description: str
    params: dict[str, typing.Any]
    required: bool
    uri: str

@typing.type_check_only
class AgentInterface(typing.TypedDict, total=False):
    tenant: str
    transport: str
    url: str

@typing.type_check_only
class AgentProvider(typing.TypedDict, total=False):
    organization: str
    url: str

@typing.type_check_only
class AgentSkill(typing.TypedDict, total=False):
    description: str
    examples: _list[str]
    id: str
    inputModes: _list[str]
    name: str
    outputModes: _list[str]
    security: _list[Security]
    tags: _list[str]

@typing.type_check_only
class AggregationInfo(typing.TypedDict, total=False):
    aggregationCount: int
    aggregationInterval: typing.Literal[
        "AGGREGATION_INTERVAL_UNSPECIFIED", "DAILY", "MONTHLY"
    ]
    aggregationLevel: typing.Literal[
        "AGGREGATION_LEVEL_UNSPECIFIED", "ACCOUNT", "PROJECT"
    ]

@typing.type_check_only
class Artifact(typing.TypedDict, total=False):
    artifactId: str
    description: str
    extensions: _list[str]
    metadata: dict[str, typing.Any]
    name: str
    parts: _list[Part]

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
class AuthenticationInfo(typing.TypedDict, total=False):
    credentials: str
    schemes: _list[str]

@typing.type_check_only
class AuthorizationCodeOAuthFlow(typing.TypedDict, total=False):
    authorizationUrl: str
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class BillingAccount(typing.TypedDict, total=False):
    currencyCode: str
    displayName: str
    masterBillingAccount: str
    name: str
    open: bool
    parent: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelTaskRequest(typing.TypedDict, total=False):
    tenant: str

@typing.type_check_only
class Category(typing.TypedDict, total=False):
    resourceFamily: str
    resourceGroup: str
    serviceDisplayName: str
    usageType: str

@typing.type_check_only
class ClientCredentialsOAuthFlow(typing.TypedDict, total=False):
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class DataPart(typing.TypedDict, total=False):
    data: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FilePart(typing.TypedDict, total=False):
    fileWithBytes: str
    fileWithUri: str
    mimeType: str
    name: str

@typing.type_check_only
class GeoTaxonomy(typing.TypedDict, total=False):
    regions: _list[str]
    type: typing.Literal["TYPE_UNSPECIFIED", "GLOBAL", "REGIONAL", "MULTI_REGIONAL"]

@typing.type_check_only
class HTTPAuthSecurityScheme(typing.TypedDict, total=False):
    bearerFormat: str
    description: str
    scheme: str

@typing.type_check_only
class ImplicitOAuthFlow(typing.TypedDict, total=False):
    authorizationUrl: str
    refreshUrl: str
    scopes: dict[str, typing.Any]

@typing.type_check_only
class ListBillingAccountsResponse(typing.TypedDict, total=False):
    billingAccounts: _list[BillingAccount]
    nextPageToken: str

@typing.type_check_only
class ListProjectBillingInfoResponse(typing.TypedDict, total=False):
    nextPageToken: str
    projectBillingInfo: _list[ProjectBillingInfo]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class ListSkusResponse(typing.TypedDict, total=False):
    nextPageToken: str
    skus: _list[Sku]

@typing.type_check_only
class ListTaskPushNotificationConfigResponse(typing.TypedDict, total=False):
    configs: _list[TaskPushNotificationConfig]
    nextPageToken: str

@typing.type_check_only
class Message(typing.TypedDict, total=False):
    content: _list[Part]
    contextId: str
    extensions: _list[str]
    messageId: str
    metadata: dict[str, typing.Any]
    role: typing.Literal["ROLE_UNSPECIFIED", "ROLE_USER", "ROLE_AGENT"]
    taskId: str

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MoveBillingAccountRequest(typing.TypedDict, total=False):
    destinationParent: str

@typing.type_check_only
class MutualTlsSecurityScheme(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class OAuth2SecurityScheme(typing.TypedDict, total=False):
    description: str
    flows: OAuthFlows
    oauth2MetadataUrl: str

@typing.type_check_only
class OAuthFlows(typing.TypedDict, total=False):
    authorizationCode: AuthorizationCodeOAuthFlow
    clientCredentials: ClientCredentialsOAuthFlow
    implicit: ImplicitOAuthFlow
    password: PasswordOAuthFlow

@typing.type_check_only
class OpenIdConnectSecurityScheme(typing.TypedDict, total=False):
    description: str
    openIdConnectUrl: str

@typing.type_check_only
class Part(typing.TypedDict, total=False):
    data: DataPart
    file: FilePart
    metadata: dict[str, typing.Any]
    text: str

@typing.type_check_only
class PasswordOAuthFlow(typing.TypedDict, total=False):
    refreshUrl: str
    scopes: dict[str, typing.Any]
    tokenUrl: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PricingExpression(typing.TypedDict, total=False):
    baseUnit: str
    baseUnitConversionFactor: float
    baseUnitDescription: str
    displayQuantity: float
    tieredRates: _list[TierRate]
    usageUnit: str
    usageUnitDescription: str

@typing.type_check_only
class PricingInfo(typing.TypedDict, total=False):
    aggregationInfo: AggregationInfo
    currencyConversionRate: float
    effectiveTime: str
    pricingExpression: PricingExpression
    summary: str

@typing.type_check_only
class ProjectBillingInfo(typing.TypedDict, total=False):
    billingAccountName: str
    billingEnabled: bool
    name: str
    projectId: str

@typing.type_check_only
class PushNotificationConfig(typing.TypedDict, total=False):
    authentication: AuthenticationInfo
    id: str
    token: str
    url: str

@typing.type_check_only
class Security(typing.TypedDict, total=False):
    schemes: dict[str, typing.Any]

@typing.type_check_only
class SecurityScheme(typing.TypedDict, total=False):
    apiKeySecurityScheme: APIKeySecurityScheme
    httpAuthSecurityScheme: HTTPAuthSecurityScheme
    mtlsSecurityScheme: MutualTlsSecurityScheme
    oauth2SecurityScheme: OAuth2SecurityScheme
    openIdConnectSecurityScheme: OpenIdConnectSecurityScheme

@typing.type_check_only
class SendMessageConfiguration(typing.TypedDict, total=False):
    acceptedOutputModes: _list[str]
    blocking: bool
    historyLength: int
    pushNotification: PushNotificationConfig

@typing.type_check_only
class SendMessageRequest(typing.TypedDict, total=False):
    configuration: SendMessageConfiguration
    message: Message
    metadata: dict[str, typing.Any]
    tenant: str

@typing.type_check_only
class SendMessageResponse(typing.TypedDict, total=False):
    message: Message
    task: Task

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    businessEntityName: str
    displayName: str
    name: str
    serviceId: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Sku(typing.TypedDict, total=False):
    category: Category
    description: str
    geoTaxonomy: GeoTaxonomy
    name: str
    pricingInfo: _list[PricingInfo]
    serviceProviderName: str
    serviceRegions: _list[str]
    skuId: str

@typing.type_check_only
class StreamResponse(typing.TypedDict, total=False):
    artifactUpdate: TaskArtifactUpdateEvent
    message: Message
    statusUpdate: TaskStatusUpdateEvent
    task: Task

@typing.type_check_only
class StringList(typing.TypedDict, total=False):
    list: _list[str]

@typing.type_check_only
class Task(typing.TypedDict, total=False):
    artifacts: _list[Artifact]
    contextId: str
    history: _list[Message]
    id: str
    metadata: dict[str, typing.Any]
    status: TaskStatus

@typing.type_check_only
class TaskArtifactUpdateEvent(typing.TypedDict, total=False):
    append: bool
    artifact: Artifact
    contextId: str
    lastChunk: bool
    metadata: dict[str, typing.Any]
    taskId: str

@typing.type_check_only
class TaskPushNotificationConfig(typing.TypedDict, total=False):
    name: str
    pushNotificationConfig: PushNotificationConfig

@typing.type_check_only
class TaskStatus(typing.TypedDict, total=False):
    message: Message
    state: typing.Literal[
        "TASK_STATE_UNSPECIFIED",
        "TASK_STATE_SUBMITTED",
        "TASK_STATE_WORKING",
        "TASK_STATE_COMPLETED",
        "TASK_STATE_FAILED",
        "TASK_STATE_CANCELLED",
        "TASK_STATE_INPUT_REQUIRED",
        "TASK_STATE_REJECTED",
        "TASK_STATE_AUTH_REQUIRED",
    ]
    timestamp: str

@typing.type_check_only
class TaskStatusUpdateEvent(typing.TypedDict, total=False):
    contextId: str
    final: bool
    metadata: dict[str, typing.Any]
    status: TaskStatus
    taskId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TierRate(typing.TypedDict, total=False):
    startUsageAmount: float
    unitPrice: Money
