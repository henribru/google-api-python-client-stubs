import typing

import typing_extensions

class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

class GoogleApiServiceusageV1beta1ServiceIdentity(
    typing_extensions.TypedDict, total=False
):
    uniqueId: str
    email: str

class Monitoring(typing_extensions.TypedDict, total=False):
    producerDestinations: typing.List[MonitoringDestination]
    consumerDestinations: typing.List[MonitoringDestination]

class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

class Authentication(typing_extensions.TypedDict, total=False):
    rules: typing.List[AuthenticationRule]
    providers: typing.List[AuthProvider]

class Type(typing_extensions.TypedDict, total=False):
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    name: str
    options: typing.List[Option]
    fields: typing.List[Field]
    sourceContext: SourceContext
    oneofs: typing.List[str]

class ImportAdminOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class DisableServiceResponse(typing_extensions.TypedDict, total=False):
    service: GoogleApiServiceusageV1Service

class QuotaLimit(typing_extensions.TypedDict, total=False):
    metric: str
    name: str
    freeTier: str
    values: typing.Dict[str, typing.Any]
    maxLimit: str
    description: str
    displayName: str
    unit: str
    duration: str
    defaultLimit: str

class BatchCreateAdminOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class AdminQuotaPolicy(typing_extensions.TypedDict, total=False):
    dimensions: typing.Dict[str, typing.Any]
    name: str
    metric: str
    policyValue: str
    container: str
    unit: str

class Quota(typing_extensions.TypedDict, total=False):
    metricRules: typing.List[MetricRule]
    limits: typing.List[QuotaLimit]

class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    kind: str
    path: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

class Api(typing_extensions.TypedDict, total=False):
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    mixins: typing.List[Mixin]
    methods: typing.List[Method]
    name: str
    options: typing.List[Option]
    version: str

class ImportAdminQuotaPoliciesResponse(typing_extensions.TypedDict, total=False):
    policies: typing.List[AdminQuotaPolicy]

class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class DocumentationRule(typing_extensions.TypedDict, total=False):
    description: str
    deprecationDescription: str
    selector: str

class Documentation(typing_extensions.TypedDict, total=False):
    overview: str
    pages: typing.List[Page]
    summary: str
    rules: typing.List[DocumentationRule]
    serviceRootUrl: str
    documentationRootUrl: str

class LogDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    labels: typing.List[LabelDescriptor]
    name: str

class Http(typing_extensions.TypedDict, total=False):
    fullyDecodeReservedExpansion: bool
    rules: typing.List[HttpRule]

class HttpRule(typing.Dict[str, typing.Any]): ...
class EnableServiceRequest(typing_extensions.TypedDict, total=False): ...

class BatchEnableServicesRequest(typing_extensions.TypedDict, total=False):
    serviceIds: typing.List[str]

class Control(typing_extensions.TypedDict, total=False):
    environment: str

class AuthProvider(typing_extensions.TypedDict, total=False):
    authorizationUrl: str
    jwtLocations: typing.List[JwtLocation]
    issuer: str
    id: str
    audiences: str
    jwksUri: str

class ImportConsumerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class SystemParameter(typing_extensions.TypedDict, total=False):
    name: str
    httpHeader: str
    urlQueryParameter: str

class GoogleApiServiceusageV1Service(typing.Dict[str, typing.Any]): ...

class EnableServiceResponse(typing_extensions.TypedDict, total=False):
    service: GoogleApiServiceusageV1Service

class MetricDescriptor(typing_extensions.TypedDict, total=False):
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    unit: str
    metadata: MetricDescriptorMetadata
    monitoredResourceTypes: typing.List[str]
    type: str
    labels: typing.List[LabelDescriptor]
    name: str
    displayName: str
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
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]

class CustomErrorRule(typing_extensions.TypedDict, total=False):
    selector: str
    isErrorType: bool

class GoogleApiServiceusageV1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    resourceNames: typing.List[str]

class EnableFailure(typing_extensions.TypedDict, total=False):
    errorMessage: str
    serviceId: str

class UsageRule(typing_extensions.TypedDict, total=False):
    selector: str
    allowUnregisteredCalls: bool
    skipServiceControl: bool

class DisableServiceRequest(typing_extensions.TypedDict, total=False):
    disableDependentServices: bool
    checkIfServiceHasUsage: typing_extensions.Literal[
        "CHECK_IF_SERVICE_HAS_USAGE_UNSPECIFIED", "SKIP", "CHECK"
    ]

class OperationMetadata(typing_extensions.TypedDict, total=False):
    resourceNames: typing.List[str]

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[GoogleApiServiceusageV1Service]

class EnumValue(typing_extensions.TypedDict, total=False):
    options: typing.List[Option]
    number: int
    name: str

class ServiceIdentity(typing_extensions.TypedDict, total=False):
    uniqueId: str
    email: str

class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

class Mixin(typing_extensions.TypedDict, total=False):
    name: str
    root: str

class MetricRule(typing_extensions.TypedDict, total=False):
    metricCosts: typing.Dict[str, typing.Any]
    selector: str

class LoggingDestination(typing_extensions.TypedDict, total=False):
    logs: typing.List[str]
    monitoredResource: str

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
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
    displayName: str
    name: str
    description: str
    labels: typing.List[LabelDescriptor]

class GetServiceIdentityResponse(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["IDENTITY_STATE_UNSPECIFIED", "ACTIVE"]
    identity: ServiceIdentity

class GoogleApiServiceIdentity(typing_extensions.TypedDict, total=False):
    displayName: str
    serviceAccountParent: str
    description: str

class BackendRule(typing_extensions.TypedDict, total=False):
    minDeadline: float
    jwtAudience: str
    operationDeadline: float
    selector: str
    disableAuth: bool
    deadline: float
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    address: str
    protocol: str

class BatchEnableServicesResponse(typing_extensions.TypedDict, total=False):
    services: typing.List[GoogleApiServiceusageV1Service]
    failures: typing.List[EnableFailure]

class GoogleApiServiceusageV1beta1GetServiceIdentityResponse(
    typing_extensions.TypedDict, total=False
):
    identity: GoogleApiServiceusageV1beta1ServiceIdentity
    state: typing_extensions.Literal["IDENTITY_STATE_UNSPECIFIED", "ACTIVE"]

class Logging(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[LoggingDestination]
    producerDestinations: typing.List[LoggingDestination]

class BatchCreateConsumerOverridesResponse(typing_extensions.TypedDict, total=False):
    overrides: typing.List[QuotaOverride]

class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class BatchGetServicesResponse(typing_extensions.TypedDict, total=False):
    services: typing.List[GoogleApiServiceusageV1Service]

class BillingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    metrics: typing.List[str]

class Enum(typing_extensions.TypedDict, total=False):
    options: typing.List[Option]
    enumvalue: typing.List[EnumValue]
    name: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    sourceContext: SourceContext

class MonitoringDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    metrics: typing.List[str]

class QuotaOverride(typing_extensions.TypedDict, total=False):
    overrideValue: str
    metric: str
    unit: str
    adminOverrideAncestor: str
    name: str
    dimensions: typing.Dict[str, typing.Any]

class Endpoint(typing_extensions.TypedDict, total=False):
    name: str
    target: str
    aliases: typing.List[str]
    allowCors: bool

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    error: Status
    name: str
    done: bool

class GoogleApiService(typing_extensions.TypedDict, total=False):
    context: Context
    endpoints: typing.List[Endpoint]
    id: str
    title: str
    name: str
    apis: typing.List[Api]
    backend: Backend
    quota: Quota
    billing: Billing
    documentation: Documentation
    systemParameters: SystemParameters
    metrics: typing.List[MetricDescriptor]
    enums: typing.List[Enum]
    monitoring: Monitoring
    sourceInfo: SourceInfo
    producerProjectId: str
    authentication: Authentication
    control: Control
    systemTypes: typing.List[Type]
    customError: CustomError
    http: Http
    logging: Logging
    usage: Usage
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    logs: typing.List[LogDescriptor]
    configVersion: int
    types: typing.List[Type]

class JwtLocation(typing_extensions.TypedDict, total=False):
    query: str
    valuePrefix: str
    header: str

class Empty(typing_extensions.TypedDict, total=False): ...
class Page(typing.Dict[str, typing.Any]): ...

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

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]
    description: str
    key: str

class ContextRule(typing_extensions.TypedDict, total=False):
    allowedResponseExtensions: typing.List[str]
    allowedRequestExtensions: typing.List[str]
    requested: typing.List[str]
    selector: str
    provided: typing.List[str]

class Usage(typing_extensions.TypedDict, total=False):
    serviceIdentity: GoogleApiServiceIdentity
    requirements: typing.List[str]
    rules: typing.List[UsageRule]
    producerNotificationChannel: str

class SystemParameterRule(typing_extensions.TypedDict, total=False):
    selector: str
    parameters: typing.List[SystemParameter]

class GoogleApiServiceusageV1ServiceConfig(typing.Dict[str, typing.Any]): ...

class AuthenticationRule(typing_extensions.TypedDict, total=False):
    oauth: OAuthRequirements
    selector: str
    requirements: typing.List[AuthRequirement]
    allowWithoutCredential: bool

class Field(typing_extensions.TypedDict, total=False):
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
    packed: bool
    number: int
    oneofIndex: int
    jsonName: str
    typeUrl: str
    name: str
    options: typing.List[Option]
    defaultValue: str

class Method(typing_extensions.TypedDict, total=False):
    responseStreaming: bool
    requestTypeUrl: str
    requestStreaming: bool
    name: str
    options: typing.List[Option]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    responseTypeUrl: str

class CustomError(typing_extensions.TypedDict, total=False):
    types: typing.List[str]
    rules: typing.List[CustomErrorRule]
