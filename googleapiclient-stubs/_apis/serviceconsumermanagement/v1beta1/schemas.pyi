import typing

import typing_extensions

class Field(typing_extensions.TypedDict, total=False):
    oneofIndex: int
    number: int
    name: str
    packed: bool
    options: typing.List[Option]
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
    jsonName: str
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    typeUrl: str
    defaultValue: str

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
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
    labels: typing.List[LabelDescriptor]
    description: str
    displayName: str
    name: str
    type: str

class Usage(typing_extensions.TypedDict, total=False):
    requirements: typing.List[str]
    producerNotificationChannel: str
    rules: typing.List[UsageRule]
    serviceIdentity: ServiceIdentity

class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

class V1beta1DefaultIdentity(typing_extensions.TypedDict, total=False):
    email: str
    uniqueId: str
    name: str

class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    path: str
    kind: str

class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

class Authentication(typing_extensions.TypedDict, total=False):
    rules: typing.List[AuthenticationRule]
    providers: typing.List[AuthProvider]

class Api(typing_extensions.TypedDict, total=False):
    methods: typing.List[Method]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    version: str
    mixins: typing.List[Mixin]
    sourceContext: SourceContext
    options: typing.List[Option]
    name: str

class V1Beta1ImportProducerQuotaPoliciesResponse(
    typing_extensions.TypedDict, total=False
):
    policies: typing.List[V1Beta1ProducerQuotaPolicy]

class V1Beta1GenerateServiceIdentityResponse(typing_extensions.TypedDict, total=False):
    identity: V1Beta1ServiceIdentity

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    key: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]

class V1beta1DisableConsumerResponse(typing_extensions.TypedDict, total=False): ...

class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

class V1Beta1ConsumerQuotaMetric(typing_extensions.TypedDict, total=False):
    metric: str
    name: str
    displayName: str
    unit: str
    consumerQuotaLimits: typing.List[V1Beta1ConsumerQuotaLimit]

class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

class SystemParameter(typing_extensions.TypedDict, total=False):
    httpHeader: str
    urlQueryParameter: str
    name: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Monitoring(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[MonitoringDestination]
    producerDestinations: typing.List[MonitoringDestination]

class V1Beta1RefreshConsumerResponse(typing_extensions.TypedDict, total=False): ...
class V1Beta1EnableConsumerResponse(typing_extensions.TypedDict, total=False): ...

class Quota(typing_extensions.TypedDict, total=False):
    metricRules: typing.List[MetricRule]
    limits: typing.List[QuotaLimit]

class V1Beta1QuotaOverride(typing_extensions.TypedDict, total=False):
    name: str
    metric: str
    dimensions: typing.Dict[str, typing.Any]
    unit: str
    adminOverrideAncestor: str
    overrideValue: str

class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

class V1Beta1QuotaBucket(typing_extensions.TypedDict, total=False):
    effectiveLimit: str
    producerOverride: V1Beta1QuotaOverride
    consumerOverride: V1Beta1QuotaOverride
    defaultLimit: str
    adminOverride: V1Beta1QuotaOverride
    dimensions: typing.Dict[str, typing.Any]

class Documentation(typing_extensions.TypedDict, total=False):
    summary: str
    documentationRootUrl: str
    pages: typing.List[Page]
    rules: typing.List[DocumentationRule]
    serviceRootUrl: str
    overview: str

class ServiceIdentity(typing_extensions.TypedDict, total=False):
    displayName: str
    description: str
    serviceAccountParent: str

class Method(typing_extensions.TypedDict, total=False):
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    requestTypeUrl: str
    requestStreaming: bool
    responseStreaming: bool
    name: str
    options: typing.List[Option]
    responseTypeUrl: str

class Endpoint(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    allowCors: bool
    name: str
    target: str

class V1beta1GenerateServiceAccountResponse(typing_extensions.TypedDict, total=False):
    account: V1beta1ServiceAccount

class ContextRule(typing_extensions.TypedDict, total=False):
    allowedRequestExtensions: typing.List[str]
    selector: str
    requested: typing.List[str]
    allowedResponseExtensions: typing.List[str]
    provided: typing.List[str]

class V1beta1RefreshConsumerResponse(typing_extensions.TypedDict, total=False): ...

class V1Beta1ServiceIdentity(typing_extensions.TypedDict, total=False):
    email: str
    tag: str
    uniqueId: str
    name: str

class Http(typing_extensions.TypedDict, total=False):
    fullyDecodeReservedExpansion: bool
    rules: typing.List[HttpRule]

class MetricDescriptor(typing_extensions.TypedDict, total=False):
    unit: str
    monitoredResourceTypes: typing.List[str]
    type: str
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
    name: str
    displayName: str
    metadata: MetricDescriptorMetadata
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
    description: str
    labels: typing.List[LabelDescriptor]

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class AuthenticationRule(typing_extensions.TypedDict, total=False):
    selector: str
    oauth: OAuthRequirements
    allowWithoutCredential: bool
    requirements: typing.List[AuthRequirement]

class AuthProvider(typing_extensions.TypedDict, total=False):
    issuer: str
    authorizationUrl: str
    jwksUri: str
    audiences: str
    id: str
    jwtLocations: typing.List[JwtLocation]

class V1Beta1ProducerQuotaPolicy(typing_extensions.TypedDict, total=False):
    unit: str
    container: str
    name: str
    dimensions: typing.Dict[str, typing.Any]
    metric: str
    policyValue: str

class V1Beta1ImportProducerOverridesRequest(typing_extensions.TypedDict, total=False):
    inlineSource: V1Beta1OverrideInlineSource
    force: bool

class Page(typing.Dict[str, typing.Any]): ...

class V1beta1AddVisibilityLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: typing.List[str]

class V1Beta1OverrideInlineSource(typing_extensions.TypedDict, total=False):
    overrides: typing.List[V1Beta1QuotaOverride]

class V1Beta1DisableConsumerResponse(typing_extensions.TypedDict, total=False): ...

class Type(typing_extensions.TypedDict, total=False):
    oneofs: typing.List[str]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    fields: typing.List[Field]
    name: str
    sourceContext: SourceContext
    options: typing.List[Option]

class BillingDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

class V1beta1GenerateDefaultIdentityResponse(typing_extensions.TypedDict, total=False):
    attachStatus: typing_extensions.Literal[
        "ATTACH_STATUS_UNSPECIFIED",
        "ATTACHED",
        "ATTACH_SKIPPED",
        "PREVIOUSLY_ATTACHED",
        "ATTACH_DENIED_BY_ORG_POLICY",
    ]
    identity: V1beta1DefaultIdentity
    role: str

class DocumentationRule(typing_extensions.TypedDict, total=False):
    selector: str
    deprecationDescription: str
    description: str

class SystemParameterRule(typing_extensions.TypedDict, total=False):
    parameters: typing.List[SystemParameter]
    selector: str

class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

class Service(typing_extensions.TypedDict, total=False):
    control: Control
    customError: CustomError
    context: Context
    metrics: typing.List[MetricDescriptor]
    enums: typing.List[Enum]
    configVersion: int
    id: str
    producerProjectId: str
    apis: typing.List[Api]
    systemParameters: SystemParameters
    name: str
    http: Http
    usage: Usage
    title: str
    systemTypes: typing.List[Type]
    authentication: Authentication
    quota: Quota
    endpoints: typing.List[Endpoint]
    backend: Backend
    logging: Logging
    logs: typing.List[LogDescriptor]
    types: typing.List[Type]
    documentation: Documentation
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    sourceInfo: SourceInfo
    monitoring: Monitoring
    billing: Billing

class Enum(typing_extensions.TypedDict, total=False):
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    enumvalue: typing.List[EnumValue]
    options: typing.List[Option]
    name: str
    sourceContext: SourceContext

class JwtLocation(typing_extensions.TypedDict, total=False):
    query: str
    valuePrefix: str
    header: str

class CustomErrorRule(typing_extensions.TypedDict, total=False):
    selector: str
    isErrorType: bool

class CustomError(typing_extensions.TypedDict, total=False):
    rules: typing.List[CustomErrorRule]
    types: typing.List[str]

class LogDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    labels: typing.List[LabelDescriptor]
    displayName: str

class Logging(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[LoggingDestination]
    producerDestinations: typing.List[LoggingDestination]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class V1Beta1ListConsumerQuotaMetricsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    metrics: typing.List[V1Beta1ConsumerQuotaMetric]

class EnumValue(typing_extensions.TypedDict, total=False):
    number: int
    options: typing.List[Option]
    name: str

class MetricRule(typing_extensions.TypedDict, total=False):
    selector: str
    metricCosts: typing.Dict[str, typing.Any]

class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status

class V1beta1RemoveVisibilityLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: typing.List[str]

class MonitoringDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

class HttpRule(typing.Dict[str, typing.Any]): ...

class MetricDescriptorMetadata(typing_extensions.TypedDict, total=False):
    ingestDelay: str
    samplePeriod: str
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

class V1Beta1ImportProducerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[V1Beta1QuotaOverride]

class QuotaLimit(typing_extensions.TypedDict, total=False):
    displayName: str
    values: typing.Dict[str, typing.Any]
    metric: str
    duration: str
    freeTier: str
    unit: str
    defaultLimit: str
    description: str
    maxLimit: str
    name: str

class V1Beta1ConsumerQuotaLimit(typing_extensions.TypedDict, total=False):
    quotaBuckets: typing.List[V1Beta1QuotaBucket]
    unit: str
    isPrecise: bool
    metric: str
    name: str

class V1beta1EnableConsumerResponse(typing_extensions.TypedDict, total=False): ...

class BackendRule(typing_extensions.TypedDict, total=False):
    deadline: float
    disableAuth: bool
    selector: str
    protocol: str
    operationDeadline: float
    minDeadline: float
    jwtAudience: str
    address: str
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]

class Control(typing_extensions.TypedDict, total=False):
    environment: str

class V1beta1ServiceAccount(typing_extensions.TypedDict, total=False):
    tag: str
    uniqueId: str
    email: str
    name: str
    iamAccountName: str

class UsageRule(typing_extensions.TypedDict, total=False):
    selector: str
    allowUnregisteredCalls: bool
    skipServiceControl: bool

class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

class LoggingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    logs: typing.List[str]

class V1Beta1ListProducerOverridesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    overrides: typing.List[V1Beta1QuotaOverride]

class Mixin(typing_extensions.TypedDict, total=False):
    root: str
    name: str

class V1Beta1BatchCreateProducerOverridesResponse(
    typing_extensions.TypedDict, total=False
):
    overrides: typing.List[V1Beta1QuotaOverride]
