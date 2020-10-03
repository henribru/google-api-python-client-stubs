import typing

import typing_extensions

class CustomError(typing_extensions.TypedDict, total=False):
    types: typing.List[str]
    rules: typing.List[CustomErrorRule]

class ListConsumerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]
    nextPageToken: str

class Mixin(typing_extensions.TypedDict, total=False):
    root: str
    name: str

class GetServiceIdentityResponse(typing_extensions.TypedDict, total=False):
    identity: ServiceIdentity
    state: typing_extensions.Literal["IDENTITY_STATE_UNSPECIFIED", "ACTIVE"]

class AuthenticationRule(typing_extensions.TypedDict, total=False):
    requirements: typing.List[AuthRequirement]
    allowWithoutCredential: bool
    oauth: OAuthRequirements
    selector: str

class Field(typing_extensions.TypedDict, total=False):
    packed: bool
    name: str
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
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    options: typing.List[Option]
    oneofIndex: int
    number: int
    defaultValue: str
    typeUrl: str
    jsonName: str

class DisableServiceResponse(typing_extensions.TypedDict, total=False):
    service: GoogleApiServiceusageV1Service

class QuotaOverride(typing_extensions.TypedDict, total=False):
    dimensions: typing.Dict[str, typing.Any]
    overrideValue: str
    name: str
    adminOverrideAncestor: str
    unit: str
    metric: str

class Enum(typing_extensions.TypedDict, total=False):
    enumvalue: typing.List[EnumValue]
    options: typing.List[Option]
    name: str
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[Service]

class BatchEnableServicesRequest(typing_extensions.TypedDict, total=False):
    serviceIds: typing.List[str]

class Api(typing_extensions.TypedDict, total=False):
    options: typing.List[Option]
    mixins: typing.List[Mixin]
    sourceContext: SourceContext
    methods: typing.List[Method]
    name: str
    version: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

class BackendRule(typing_extensions.TypedDict, total=False):
    operationDeadline: float
    address: str
    jwtAudience: str
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    minDeadline: float
    protocol: str
    selector: str
    disableAuth: bool
    deadline: float

class ImportConsumerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class CustomErrorRule(typing_extensions.TypedDict, total=False):
    isErrorType: bool
    selector: str

class OverrideInlineSource(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class SystemParameter(typing_extensions.TypedDict, total=False):
    urlQueryParameter: str
    httpHeader: str
    name: str

class Documentation(typing_extensions.TypedDict, total=False):
    pages: typing.List[Page]
    overview: str
    documentationRootUrl: str
    serviceRootUrl: str
    rules: typing.List[DocumentationRule]
    summary: str

class EnableFailure(typing_extensions.TypedDict, total=False):
    errorMessage: str
    serviceId: str

class ImportAdminOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class GoogleApiServiceusageV1ServiceConfig(typing_extensions.TypedDict, total=False):
    name: str
    authentication: Authentication
    monitoring: Monitoring
    apis: typing.List[Api]
    title: str
    usage: Usage
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    documentation: Documentation
    quota: Quota
    endpoints: typing.List[Endpoint]

class OperationMetadata(typing_extensions.TypedDict, total=False):
    resourceNames: typing.List[str]

class DisableServiceRequest(typing_extensions.TypedDict, total=False): ...

class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

class GoogleApiService(typing_extensions.TypedDict, total=False):
    apis: typing.List[Api]
    quota: Quota
    producerProjectId: str
    logging: Logging
    types: typing.List[Type]
    usage: Usage
    logs: typing.List[LogDescriptor]
    endpoints: typing.List[Endpoint]
    id: str
    name: str
    documentation: Documentation
    control: Control
    systemTypes: typing.List[Type]
    authentication: Authentication
    configVersion: int
    monitoring: Monitoring
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    context: Context
    customError: CustomError
    http: Http
    metrics: typing.List[MetricDescriptor]
    enums: typing.List[Enum]
    systemParameters: SystemParameters
    sourceInfo: SourceInfo
    billing: Billing
    backend: Backend
    title: str

class MetricRule(typing_extensions.TypedDict, total=False):
    selector: str
    metricCosts: typing.Dict[str, typing.Any]

class EnableServiceRequest(typing_extensions.TypedDict, total=False): ...

class JwtLocation(typing_extensions.TypedDict, total=False):
    header: str
    query: str
    valuePrefix: str

class Option(typing_extensions.TypedDict, total=False):
    value: typing.Dict[str, typing.Any]
    name: str

class EnumValue(typing_extensions.TypedDict, total=False):
    number: int
    options: typing.List[Option]
    name: str

class ListAdminOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]
    nextPageToken: str

class Control(typing_extensions.TypedDict, total=False):
    environment: str

class Http(typing.Dict[str, typing.Any]): ...
class Empty(typing_extensions.TypedDict, total=False): ...

class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

class GoogleApiServiceusageV1beta1GetServiceIdentityResponse(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal["IDENTITY_STATE_UNSPECIFIED", "ACTIVE"]
    identity: GoogleApiServiceusageV1beta1ServiceIdentity

class ServiceConfig(typing_extensions.TypedDict, total=False):
    monitoring: Monitoring
    authentication: Authentication
    apis: typing.List[Api]
    endpoints: typing.List[Endpoint]
    quota: Quota
    name: str
    title: str
    usage: Usage
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    documentation: Documentation

class ImportAdminQuotaPoliciesResponse(typing_extensions.TypedDict, total=False):
    policies: typing.List[AdminQuotaPolicy]

class SystemParameterRule(typing_extensions.TypedDict, total=False):
    selector: str
    parameters: typing.List[SystemParameter]

class Usage(typing_extensions.TypedDict, total=False):
    producerNotificationChannel: str
    serviceIdentity: GoogleApiServiceIdentity
    rules: typing.List[UsageRule]
    requirements: typing.List[str]

class Monitoring(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[MonitoringDestination]
    producerDestinations: typing.List[MonitoringDestination]

class Endpoint(typing_extensions.TypedDict, total=False):
    allowCors: bool
    aliases: typing.List[str]
    target: str
    name: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Quota(typing_extensions.TypedDict, total=False):
    metricRules: typing.List[MetricRule]
    limits: typing.List[QuotaLimit]

class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

class ConsumerQuotaLimit(typing_extensions.TypedDict, total=False):
    quotaBuckets: typing.List[QuotaBucket]
    isPrecise: bool
    name: str
    unit: str
    allowsAdminOverrides: bool
    metric: str

class ListConsumerQuotaMetricsResponse(typing_extensions.TypedDict, total=False):
    metrics: typing.List[ConsumerQuotaMetric]
    nextPageToken: str

class AuthProvider(typing_extensions.TypedDict, total=False):
    jwksUri: str
    id: str
    issuer: str
    authorizationUrl: str
    audiences: str
    jwtLocations: typing.List[JwtLocation]

class GoogleApiServiceusageV1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    resourceNames: typing.List[str]

class MonitoringDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    metrics: typing.List[str]

class LogDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    labels: typing.List[LabelDescriptor]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Logging(typing_extensions.TypedDict, total=False):
    producerDestinations: typing.List[LoggingDestination]
    consumerDestinations: typing.List[LoggingDestination]

class BillingDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

class BatchCreateAdminOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class GoogleApiServiceusageV1beta1ServiceIdentity(
    typing_extensions.TypedDict, total=False
):
    uniqueId: str
    email: str

class EnableServiceResponse(typing_extensions.TypedDict, total=False):
    service: GoogleApiServiceusageV1Service

class DocumentationRule(typing_extensions.TypedDict, total=False):
    description: str
    deprecationDescription: str
    selector: str

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]
    key: str
    description: str

class BatchEnableServicesResponse(typing_extensions.TypedDict, total=False):
    services: typing.List[GoogleApiServiceusageV1Service]
    failures: typing.List[EnableFailure]

class AdminQuotaPolicy(typing_extensions.TypedDict, total=False):
    name: str
    unit: str
    metric: str
    policyValue: str
    dimensions: typing.Dict[str, typing.Any]
    container: str

class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

class Authentication(typing_extensions.TypedDict, total=False):
    providers: typing.List[AuthProvider]
    rules: typing.List[AuthenticationRule]

class Type(typing_extensions.TypedDict, total=False):
    name: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    sourceContext: SourceContext
    options: typing.List[Option]
    fields: typing.List[Field]
    oneofs: typing.List[str]

class BatchCreateConsumerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class HttpRule(typing.Dict[str, typing.Any]): ...

class ServiceIdentity(typing_extensions.TypedDict, total=False):
    email: str
    uniqueId: str

class Method(typing_extensions.TypedDict, total=False):
    responseStreaming: bool
    options: typing.List[Option]
    requestTypeUrl: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    name: str
    responseTypeUrl: str
    requestStreaming: bool

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str
    done: bool

class UsageRule(typing_extensions.TypedDict, total=False):
    selector: str
    allowUnregisteredCalls: bool
    skipServiceControl: bool

class ConsumerQuotaMetric(typing_extensions.TypedDict, total=False):
    unit: str
    name: str
    consumerQuotaLimits: typing.List[ConsumerQuotaLimit]
    displayName: str
    metric: str

class QuotaLimit(typing_extensions.TypedDict, total=False):
    maxLimit: str
    freeTier: str
    description: str
    displayName: str
    metric: str
    unit: str
    duration: str
    defaultLimit: str
    name: str
    values: typing.Dict[str, typing.Any]

class Service(typing.Dict[str, typing.Any]): ...
class GoogleApiServiceusageV1Service(typing.Dict[str, typing.Any]): ...

class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    kind: str
    path: str

class LoggingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    logs: typing.List[str]

class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

class MetricDescriptorMetadata(typing_extensions.TypedDict, total=False):
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
    ingestDelay: str

class ContextRule(typing_extensions.TypedDict, total=False):
    allowedRequestExtensions: typing.List[str]
    selector: str
    requested: typing.List[str]
    provided: typing.List[str]
    allowedResponseExtensions: typing.List[str]

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
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
    type: str
    description: str
    labels: typing.List[LabelDescriptor]
    displayName: str

class Page(typing.Dict[str, typing.Any]): ...

class GoogleApiServiceIdentity(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    serviceAccountParent: str

class QuotaBucket(typing_extensions.TypedDict, total=False):
    effectiveLimit: str
    adminOverride: QuotaOverride
    dimensions: typing.Dict[str, typing.Any]
    producerOverride: QuotaOverride
    defaultLimit: str
    consumerOverride: QuotaOverride

class MetricDescriptor(typing_extensions.TypedDict, total=False):
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]
    monitoredResourceTypes: typing.List[str]
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
    description: str
    type: str
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    metadata: MetricDescriptorMetadata
    labels: typing.List[LabelDescriptor]
    unit: str
    displayName: str

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class ImportConsumerOverridesRequest(typing_extensions.TypedDict, total=False):
    inlineSource: OverrideInlineSource
    force: bool
