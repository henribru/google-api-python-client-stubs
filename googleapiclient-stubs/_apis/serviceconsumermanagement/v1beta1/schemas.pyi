import typing

import typing_extensions

_list = list

@typing.type_check_only
class Api(typing_extensions.TypedDict, total=False):
    methods: _list[Method]
    mixins: _list[Mixin]
    name: str
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    version: str

@typing.type_check_only
class AuthProvider(typing_extensions.TypedDict, total=False):
    audiences: str
    authorizationUrl: str
    id: str
    issuer: str
    jwksUri: str
    jwtLocations: _list[JwtLocation]

@typing.type_check_only
class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

@typing.type_check_only
class Authentication(typing_extensions.TypedDict, total=False):
    providers: _list[AuthProvider]
    rules: _list[AuthenticationRule]

@typing.type_check_only
class AuthenticationRule(typing_extensions.TypedDict, total=False):
    allowWithoutCredential: bool
    oauth: OAuthRequirements
    requirements: _list[AuthRequirement]
    selector: str

@typing.type_check_only
class Backend(typing_extensions.TypedDict, total=False):
    rules: _list[BackendRule]

@typing.type_check_only
class BackendRule(typing_extensions.TypedDict, total=False):
    address: str
    deadline: float
    disableAuth: bool
    jwtAudience: str
    operationDeadline: float
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    protocol: str
    selector: str

@typing.type_check_only
class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: _list[BillingDestination]

@typing.type_check_only
class BillingDestination(typing_extensions.TypedDict, total=False):
    metrics: _list[str]
    monitoredResource: str

@typing.type_check_only
class Context(typing_extensions.TypedDict, total=False):
    rules: _list[ContextRule]

@typing.type_check_only
class ContextRule(typing_extensions.TypedDict, total=False):
    allowedRequestExtensions: _list[str]
    allowedResponseExtensions: _list[str]
    provided: _list[str]
    requested: _list[str]
    selector: str

@typing.type_check_only
class Control(typing_extensions.TypedDict, total=False):
    environment: str

@typing.type_check_only
class CustomError(typing_extensions.TypedDict, total=False):
    rules: _list[CustomErrorRule]
    types: _list[str]

@typing.type_check_only
class CustomErrorRule(typing_extensions.TypedDict, total=False):
    isErrorType: bool
    selector: str

@typing.type_check_only
class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    kind: str
    path: str

@typing.type_check_only
class Documentation(typing_extensions.TypedDict, total=False):
    documentationRootUrl: str
    overview: str
    pages: _list[Page]
    rules: _list[DocumentationRule]
    serviceRootUrl: str
    summary: str

@typing.type_check_only
class DocumentationRule(typing_extensions.TypedDict, total=False):
    deprecationDescription: str
    description: str
    selector: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    allowCors: bool
    name: str
    target: str

@typing.type_check_only
class Enum(typing_extensions.TypedDict, total=False):
    enumvalue: _list[EnumValue]
    name: str
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class EnumValue(typing_extensions.TypedDict, total=False):
    name: str
    number: int
    options: _list[Option]

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    defaultValue: str
    jsonName: str
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
    name: str
    number: int
    oneofIndex: int
    options: _list[Option]
    packed: bool
    typeUrl: str

@typing.type_check_only
class Http(typing_extensions.TypedDict, total=False):
    fullyDecodeReservedExpansion: bool
    rules: _list[HttpRule]

@typing.type_check_only
class HttpRule(dict[str, typing.Any]): ...

@typing.type_check_only
class JwtLocation(typing_extensions.TypedDict, total=False):
    cookie: str
    header: str
    query: str
    valuePrefix: str

@typing.type_check_only
class LabelDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    key: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]

@typing.type_check_only
class LogDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    labels: _list[LabelDescriptor]
    name: str

@typing.type_check_only
class Logging(typing_extensions.TypedDict, total=False):
    consumerDestinations: _list[LoggingDestination]
    producerDestinations: _list[LoggingDestination]

@typing.type_check_only
class LoggingDestination(typing_extensions.TypedDict, total=False):
    logs: _list[str]
    monitoredResource: str

@typing.type_check_only
class Method(typing_extensions.TypedDict, total=False):
    name: str
    options: _list[Option]
    requestStreaming: bool
    requestTypeUrl: str
    responseStreaming: bool
    responseTypeUrl: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class MetricDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    labels: _list[LabelDescriptor]
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
    metadata: MetricDescriptorMetadata
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    monitoredResourceTypes: _list[str]
    name: str
    type: str
    unit: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]

@typing.type_check_only
class MetricDescriptorMetadata(typing_extensions.TypedDict, total=False):
    ingestDelay: str
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
    samplePeriod: str

@typing.type_check_only
class MetricRule(typing_extensions.TypedDict, total=False):
    metricCosts: dict[str, typing.Any]
    selector: str

@typing.type_check_only
class Mixin(typing_extensions.TypedDict, total=False):
    name: str
    root: str

@typing.type_check_only
class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    labels: _list[LabelDescriptor]
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
    type: str

@typing.type_check_only
class Monitoring(typing_extensions.TypedDict, total=False):
    consumerDestinations: _list[MonitoringDestination]
    producerDestinations: _list[MonitoringDestination]

@typing.type_check_only
class MonitoringDestination(typing_extensions.TypedDict, total=False):
    metrics: _list[str]
    monitoredResource: str

@typing.type_check_only
class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: dict[str, typing.Any]

@typing.type_check_only
class Page(dict[str, typing.Any]): ...

@typing.type_check_only
class Quota(typing_extensions.TypedDict, total=False):
    limits: _list[QuotaLimit]
    metricRules: _list[MetricRule]

@typing.type_check_only
class QuotaLimit(typing_extensions.TypedDict, total=False):
    defaultLimit: str
    description: str
    displayName: str
    duration: str
    freeTier: str
    maxLimit: str
    metric: str
    name: str
    unit: str
    values: dict[str, typing.Any]

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    apis: _list[Api]
    authentication: Authentication
    backend: Backend
    billing: Billing
    configVersion: int
    context: Context
    control: Control
    customError: CustomError
    documentation: Documentation
    endpoints: _list[Endpoint]
    enums: _list[Enum]
    http: Http
    id: str
    logging: Logging
    logs: _list[LogDescriptor]
    metrics: _list[MetricDescriptor]
    monitoredResources: _list[MonitoredResourceDescriptor]
    monitoring: Monitoring
    name: str
    producerProjectId: str
    quota: Quota
    sourceInfo: SourceInfo
    systemParameters: SystemParameters
    systemTypes: _list[Type]
    title: str
    types: _list[Type]
    usage: Usage

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

@typing.type_check_only
class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: _list[dict[str, typing.Any]]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SystemParameter(typing_extensions.TypedDict, total=False):
    httpHeader: str
    name: str
    urlQueryParameter: str

@typing.type_check_only
class SystemParameterRule(typing_extensions.TypedDict, total=False):
    parameters: _list[SystemParameter]
    selector: str

@typing.type_check_only
class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: _list[SystemParameterRule]

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    fields: _list[Field]
    name: str
    oneofs: _list[str]
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class Usage(typing_extensions.TypedDict, total=False):
    producerNotificationChannel: str
    requirements: _list[str]
    rules: _list[UsageRule]

@typing.type_check_only
class UsageRule(typing_extensions.TypedDict, total=False):
    allowUnregisteredCalls: bool
    selector: str
    skipServiceControl: bool

@typing.type_check_only
class V1Beta1BatchCreateProducerOverridesResponse(
    typing_extensions.TypedDict, total=False
):
    overrides: _list[V1Beta1QuotaOverride]

@typing.type_check_only
class V1Beta1ConsumerQuotaLimit(typing_extensions.TypedDict, total=False):
    isPrecise: bool
    metric: str
    name: str
    quotaBuckets: _list[V1Beta1QuotaBucket]
    supportedLocations: _list[str]
    unit: str

@typing.type_check_only
class V1Beta1ConsumerQuotaMetric(typing_extensions.TypedDict, total=False):
    consumerQuotaLimits: _list[V1Beta1ConsumerQuotaLimit]
    descendantConsumerQuotaLimits: _list[V1Beta1ConsumerQuotaLimit]
    displayName: str
    metric: str
    name: str
    unit: str

@typing.type_check_only
class V1Beta1DisableConsumerResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class V1Beta1EnableConsumerResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class V1Beta1GenerateServiceIdentityResponse(typing_extensions.TypedDict, total=False):
    identity: V1Beta1ServiceIdentity

@typing.type_check_only
class V1Beta1ImportProducerOverridesRequest(typing_extensions.TypedDict, total=False):
    force: bool
    forceOnly: _list[str]
    inlineSource: V1Beta1OverrideInlineSource

@typing.type_check_only
class V1Beta1ImportProducerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: _list[V1Beta1QuotaOverride]

@typing.type_check_only
class V1Beta1ImportProducerQuotaPoliciesResponse(
    typing_extensions.TypedDict, total=False
):
    policies: _list[V1Beta1ProducerQuotaPolicy]

@typing.type_check_only
class V1Beta1ListConsumerQuotaMetricsResponse(typing_extensions.TypedDict, total=False):
    metrics: _list[V1Beta1ConsumerQuotaMetric]
    nextPageToken: str

@typing.type_check_only
class V1Beta1ListProducerOverridesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    overrides: _list[V1Beta1QuotaOverride]

@typing.type_check_only
class V1Beta1OverrideInlineSource(typing_extensions.TypedDict, total=False):
    overrides: _list[V1Beta1QuotaOverride]

@typing.type_check_only
class V1Beta1ProducerQuotaPolicy(typing_extensions.TypedDict, total=False):
    container: str
    dimensions: dict[str, typing.Any]
    metric: str
    name: str
    policyValue: str
    unit: str

@typing.type_check_only
class V1Beta1QuotaBucket(typing_extensions.TypedDict, total=False):
    adminOverride: V1Beta1QuotaOverride
    consumerOverride: V1Beta1QuotaOverride
    defaultLimit: str
    dimensions: dict[str, typing.Any]
    effectiveLimit: str
    producerOverride: V1Beta1QuotaOverride

@typing.type_check_only
class V1Beta1QuotaOverride(typing_extensions.TypedDict, total=False):
    adminOverrideAncestor: str
    dimensions: dict[str, typing.Any]
    metric: str
    name: str
    overrideValue: str
    unit: str

@typing.type_check_only
class V1Beta1RefreshConsumerResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class V1Beta1ServiceIdentity(typing_extensions.TypedDict, total=False):
    email: str
    name: str
    tag: str
    uniqueId: str

@typing.type_check_only
class V1beta1AddVisibilityLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: _list[str]

@typing.type_check_only
class V1beta1DefaultIdentity(typing_extensions.TypedDict, total=False):
    email: str
    name: str
    tag: str
    uniqueId: str

@typing.type_check_only
class V1beta1DisableConsumerResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class V1beta1EnableConsumerResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
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

@typing.type_check_only
class V1beta1GenerateServiceAccountResponse(typing_extensions.TypedDict, total=False):
    account: V1beta1ServiceAccount

@typing.type_check_only
class V1beta1RefreshConsumerResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class V1beta1RemoveVisibilityLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: _list[str]

@typing.type_check_only
class V1beta1ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    iamAccountName: str
    name: str
    tag: str
    uniqueId: str
