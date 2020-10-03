import typing

import typing_extensions

class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

class ContextRule(typing_extensions.TypedDict, total=False):
    allowedResponseExtensions: typing.List[str]
    selector: str
    provided: typing.List[str]
    allowedRequestExtensions: typing.List[str]
    requested: typing.List[str]

class CustomErrorRule(typing_extensions.TypedDict, total=False):
    isErrorType: bool
    selector: str

class V1Beta1EnableConsumerResponse(typing_extensions.TypedDict, total=False): ...

class CreateTenancyUnitRequest(typing_extensions.TypedDict, total=False):
    tenancyUnitId: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class LogDescriptor(typing_extensions.TypedDict, total=False):
    labels: typing.List[LabelDescriptor]
    displayName: str
    name: str
    description: str

class Endpoint(typing_extensions.TypedDict, total=False):
    name: str
    aliases: typing.List[str]
    allowCors: bool
    target: str

class AttachTenantProjectRequest(typing_extensions.TypedDict, total=False):
    externalResource: str
    reservedResource: str
    tag: str

class HttpRule(typing.Dict[str, typing.Any]): ...

class AuthRequirement(typing_extensions.TypedDict, total=False):
    providerId: str
    audiences: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str
    metadata: typing.Dict[str, typing.Any]
    done: bool

class V1Beta1ServiceIdentity(typing_extensions.TypedDict, total=False):
    uniqueId: str
    name: str
    email: str
    tag: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class AuthProvider(typing_extensions.TypedDict, total=False):
    id: str
    authorizationUrl: str
    jwtLocations: typing.List[JwtLocation]
    jwksUri: str
    audiences: str
    issuer: str

class SearchTenancyUnitsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tenancyUnits: typing.List[TenancyUnit]

class Page(typing.Dict[str, typing.Any]): ...

class V1Beta1GenerateServiceIdentityResponse(typing_extensions.TypedDict, total=False):
    identity: V1Beta1ServiceIdentity

class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

class Type(typing_extensions.TypedDict, total=False):
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    options: typing.List[Option]
    sourceContext: SourceContext
    name: str
    oneofs: typing.List[str]
    fields: typing.List[Field]

class BillingConfig(typing_extensions.TypedDict, total=False):
    billingAccount: str

class MonitoringDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

class EnumValue(typing_extensions.TypedDict, total=False):
    name: str
    options: typing.List[Option]
    number: int

class Service(typing_extensions.TypedDict, total=False):
    customError: CustomError
    control: Control
    systemTypes: typing.List[Type]
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    systemParameters: SystemParameters
    metrics: typing.List[MetricDescriptor]
    billing: Billing
    backend: Backend
    types: typing.List[Type]
    context: Context
    authentication: Authentication
    configVersion: int
    quota: Quota
    http: Http
    sourceInfo: SourceInfo
    endpoints: typing.List[Endpoint]
    monitoring: Monitoring
    apis: typing.List[Api]
    producerProjectId: str
    logs: typing.List[LogDescriptor]
    usage: Usage
    documentation: Documentation
    name: str
    id: str
    enums: typing.List[Enum]
    logging: Logging
    title: str

class Documentation(typing.Dict[str, typing.Any]): ...

class V1Beta1ImportProducerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[V1Beta1QuotaOverride]

class MetricRule(typing_extensions.TypedDict, total=False):
    selector: str
    metricCosts: typing.Dict[str, typing.Any]

class V1ServiceAccount(typing_extensions.TypedDict, total=False):
    tag: str
    email: str
    iamAccountName: str
    name: str
    uniqueId: str

class V1DisableConsumerResponse(typing_extensions.TypedDict, total=False): ...
class Http(typing.Dict[str, typing.Any]): ...

class V1Beta1ProducerQuotaPolicy(typing_extensions.TypedDict, total=False):
    name: str
    metric: str
    policyValue: str
    unit: str
    container: str
    dimensions: typing.Dict[str, typing.Any]

class ApplyTenantProjectConfigRequest(typing_extensions.TypedDict, total=False):
    projectConfig: TenantProjectConfig
    tag: str

class RemoveTenantProjectRequest(typing_extensions.TypedDict, total=False):
    tag: str

class Usage(typing_extensions.TypedDict, total=False):
    serviceIdentity: ServiceIdentity
    rules: typing.List[UsageRule]
    producerNotificationChannel: str
    requirements: typing.List[str]

class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

class SystemParameterRule(typing_extensions.TypedDict, total=False):
    selector: str
    parameters: typing.List[SystemParameter]

class DeleteTenantProjectRequest(typing_extensions.TypedDict, total=False):
    tag: str

class V1DefaultIdentity(typing_extensions.TypedDict, total=False):
    email: str
    name: str
    uniqueId: str

class V1GenerateServiceAccountResponse(typing_extensions.TypedDict, total=False):
    account: V1ServiceAccount

class Empty(typing_extensions.TypedDict, total=False): ...

class Method(typing_extensions.TypedDict, total=False):
    options: typing.List[Option]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    responseTypeUrl: str
    responseStreaming: bool
    name: str
    requestStreaming: bool
    requestTypeUrl: str

class UndeleteTenantProjectRequest(typing_extensions.TypedDict, total=False):
    tag: str

class JwtLocation(typing_extensions.TypedDict, total=False):
    header: str
    valuePrefix: str
    query: str

class CustomError(typing_extensions.TypedDict, total=False):
    rules: typing.List[CustomErrorRule]
    types: typing.List[str]

class Quota(typing_extensions.TypedDict, total=False):
    limits: typing.List[QuotaLimit]
    metricRules: typing.List[MetricRule]

class TenantProjectPolicy(typing_extensions.TypedDict, total=False):
    policyBindings: typing.List[PolicyBinding]

class TenancyUnit(typing_extensions.TypedDict, total=False):
    service: str
    createTime: str
    tenantResources: typing.List[TenantResource]
    consumer: str
    name: str

class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

class TenantResource(typing_extensions.TypedDict, total=False):
    resource: str
    tag: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PENDING_CREATE",
        "ACTIVE",
        "PENDING_DELETE",
        "FAILED",
        "DELETED",
    ]

class BillingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    metrics: typing.List[str]

class SystemParameter(typing_extensions.TypedDict, total=False):
    httpHeader: str
    urlQueryParameter: str
    name: str

class AddTenantProjectRequest(typing_extensions.TypedDict, total=False):
    tag: str
    projectConfig: TenantProjectConfig

class V1RemoveVisibilityLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: typing.List[str]

class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    path: str
    kind: str

class Mixin(typing_extensions.TypedDict, total=False):
    root: str
    name: str

class ServiceAccountConfig(typing_extensions.TypedDict, total=False):
    tenantProjectRoles: typing.List[str]
    accountId: str

class Monitoring(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[MonitoringDestination]
    producerDestinations: typing.List[MonitoringDestination]

class V1Beta1ImportProducerQuotaPoliciesResponse(
    typing_extensions.TypedDict, total=False
):
    policies: typing.List[V1Beta1ProducerQuotaPolicy]

class Field(typing_extensions.TypedDict, total=False):
    oneofIndex: int
    number: int
    typeUrl: str
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    packed: bool
    kind: typing_extensions.Literal[
        "TYPE_UNKNOWN",
        "TYPE_DOUBLE",
        "TYPE_FLOAT",
        "TYPE_INT64",
        "TYPE_UINT64",
        "TYPE_INT32",
        "TYPE_FIXED64",
        "TYPE_FIXED32",
        "TYPE_BOOL",
        "TYPE_STRING",
        "TYPE_GROUP",
        "TYPE_MESSAGE",
        "TYPE_BYTES",
        "TYPE_UINT32",
        "TYPE_ENUM",
        "TYPE_SFIXED32",
        "TYPE_SFIXED64",
        "TYPE_SINT32",
        "TYPE_SINT64",
    ]
    options: typing.List[Option]
    jsonName: str
    defaultValue: str
    name: str

class V1Beta1BatchCreateProducerOverridesResponse(
    typing_extensions.TypedDict, total=False
):
    overrides: typing.List[V1Beta1QuotaOverride]

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class TenantProjectConfig(typing_extensions.TypedDict, total=False):
    tenantProjectPolicy: TenantProjectPolicy
    folder: str
    billingConfig: BillingConfig
    serviceAccountConfig: ServiceAccountConfig
    services: typing.List[str]
    labels: typing.Dict[str, typing.Any]

class V1EnableConsumerResponse(typing_extensions.TypedDict, total=False): ...

class AuthenticationRule(typing_extensions.TypedDict, total=False):
    requirements: typing.List[AuthRequirement]
    oauth: OAuthRequirements
    allowWithoutCredential: bool
    selector: str

class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

class UsageRule(typing_extensions.TypedDict, total=False):
    skipServiceControl: bool
    allowUnregisteredCalls: bool
    selector: str

class LoggingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    logs: typing.List[str]

class Enum(typing_extensions.TypedDict, total=False):
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    options: typing.List[Option]
    enumvalue: typing.List[EnumValue]
    sourceContext: SourceContext
    name: str

class ListTenancyUnitsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tenancyUnits: typing.List[TenancyUnit]

class BackendRule(typing_extensions.TypedDict, total=False):
    address: str
    operationDeadline: float
    protocol: str
    disableAuth: bool
    minDeadline: float
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    jwtAudience: str
    selector: str
    deadline: float

class DocumentationRule(typing_extensions.TypedDict, total=False):
    description: str
    deprecationDescription: str
    selector: str

class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

class Api(typing_extensions.TypedDict, total=False):
    version: str
    sourceContext: SourceContext
    options: typing.List[Option]
    methods: typing.List[Method]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    mixins: typing.List[Mixin]
    name: str

class PolicyBinding(typing_extensions.TypedDict, total=False):
    role: str
    members: typing.List[str]

class V1Beta1RefreshConsumerResponse(typing_extensions.TypedDict, total=False): ...

class V1Beta1QuotaOverride(typing_extensions.TypedDict, total=False):
    adminOverrideAncestor: str
    name: str
    unit: str
    metric: str
    overrideValue: str
    dimensions: typing.Dict[str, typing.Any]

class ServiceIdentity(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    serviceAccountParent: str

class Authentication(typing_extensions.TypedDict, total=False):
    rules: typing.List[AuthenticationRule]
    providers: typing.List[AuthProvider]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class V1AddVisibilityLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: typing.List[str]

class V1RefreshConsumerResponse(typing_extensions.TypedDict, total=False): ...

class MetricDescriptor(typing_extensions.TypedDict, total=False):
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    labels: typing.List[LabelDescriptor]
    description: str
    monitoredResourceTypes: typing.List[str]
    displayName: str
    unit: str
    name: str
    type: str
    metadata: MetricDescriptorMetadata

class QuotaLimit(typing_extensions.TypedDict, total=False):
    values: typing.Dict[str, typing.Any]
    defaultLimit: str
    displayName: str
    name: str
    unit: str
    maxLimit: str
    duration: str
    metric: str
    description: str
    freeTier: str

class Control(typing_extensions.TypedDict, total=False):
    environment: str

class Logging(typing_extensions.TypedDict, total=False):
    producerDestinations: typing.List[LoggingDestination]
    consumerDestinations: typing.List[LoggingDestination]

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]
    key: str

class V1GenerateDefaultIdentityResponse(typing_extensions.TypedDict, total=False):
    role: str
    identity: V1DefaultIdentity
    attachStatus: typing_extensions.Literal[
        "ATTACH_STATUS_UNSPECIFIED",
        "ATTACHED",
        "ATTACH_SKIPPED",
        "PREVIOUSLY_ATTACHED",
        "ATTACH_DENIED_BY_ORG_POLICY",
    ]

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
    type: str
    displayName: str
    description: str
    labels: typing.List[LabelDescriptor]
    name: str
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]

class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

class MetricDescriptorMetadata(typing_extensions.TypedDict, total=False):
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    ingestDelay: str
    samplePeriod: str

class V1Beta1DisableConsumerResponse(typing_extensions.TypedDict, total=False): ...
