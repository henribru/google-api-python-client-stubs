import typing

import typing_extensions
@typing.type_check_only
class Advice(typing_extensions.TypedDict, total=False):
    description: str

@typing.type_check_only
class Api(typing_extensions.TypedDict, total=False):
    methods: typing.List[Method]
    mixins: typing.List[Mixin]
    name: str
    options: typing.List[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    version: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthProvider(typing_extensions.TypedDict, total=False):
    audiences: str
    authorizationUrl: str
    id: str
    issuer: str
    jwksUri: str
    jwtLocations: typing.List[JwtLocation]

@typing.type_check_only
class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

@typing.type_check_only
class Authentication(typing_extensions.TypedDict, total=False):
    providers: typing.List[AuthProvider]
    rules: typing.List[AuthenticationRule]

@typing.type_check_only
class AuthenticationRule(typing_extensions.TypedDict, total=False):
    allowWithoutCredential: bool
    oauth: OAuthRequirements
    requirements: typing.List[AuthRequirement]
    selector: str

@typing.type_check_only
class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

@typing.type_check_only
class BackendRule(typing_extensions.TypedDict, total=False):
    address: str
    deadline: float
    disableAuth: bool
    jwtAudience: str
    minDeadline: float
    operationDeadline: float
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    protocol: str
    selector: str

@typing.type_check_only
class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

@typing.type_check_only
class BillingDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class ChangeReport(typing_extensions.TypedDict, total=False):
    configChanges: typing.List[ConfigChange]

@typing.type_check_only
class ConfigChange(typing_extensions.TypedDict, total=False):
    advices: typing.List[Advice]
    changeType: typing_extensions.Literal[
        "CHANGE_TYPE_UNSPECIFIED", "ADDED", "REMOVED", "MODIFIED"
    ]
    element: str
    newValue: str
    oldValue: str

@typing.type_check_only
class ConfigFile(typing_extensions.TypedDict, total=False):
    fileContents: str
    filePath: str
    fileType: typing_extensions.Literal[
        "FILE_TYPE_UNSPECIFIED",
        "SERVICE_CONFIG_YAML",
        "OPEN_API_JSON",
        "OPEN_API_YAML",
        "FILE_DESCRIPTOR_SET_PROTO",
        "PROTO_FILE",
    ]

@typing.type_check_only
class ConfigRef(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class ConfigSource(typing_extensions.TypedDict, total=False):
    files: typing.List[ConfigFile]
    id: str

@typing.type_check_only
class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

@typing.type_check_only
class ContextRule(typing_extensions.TypedDict, total=False):
    allowedRequestExtensions: typing.List[str]
    allowedResponseExtensions: typing.List[str]
    provided: typing.List[str]
    requested: typing.List[str]
    selector: str

@typing.type_check_only
class Control(typing_extensions.TypedDict, total=False):
    environment: str

@typing.type_check_only
class CustomError(typing_extensions.TypedDict, total=False):
    rules: typing.List[CustomErrorRule]
    types: typing.List[str]

@typing.type_check_only
class CustomErrorRule(typing_extensions.TypedDict, total=False):
    isErrorType: bool
    selector: str

@typing.type_check_only
class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    kind: str
    path: str

@typing.type_check_only
class DeleteServiceStrategy(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Diagnostic(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["WARNING", "ERROR"]
    location: str
    message: str

@typing.type_check_only
class DisableServiceResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Documentation(typing_extensions.TypedDict, total=False):
    documentationRootUrl: str
    overview: str
    pages: typing.List[Page]
    rules: typing.List[DocumentationRule]
    serviceRootUrl: str
    summary: str

@typing.type_check_only
class DocumentationRule(typing_extensions.TypedDict, total=False):
    deprecationDescription: str
    description: str
    selector: str

@typing.type_check_only
class EnableServiceRequest(typing_extensions.TypedDict, total=False):
    consumerId: str

@typing.type_check_only
class EnableServiceResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    allowCors: bool
    name: str
    target: str

@typing.type_check_only
class Enum(typing_extensions.TypedDict, total=False):
    enumvalue: typing.List[EnumValue]
    name: str
    options: typing.List[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class EnumValue(typing_extensions.TypedDict, total=False):
    name: str
    number: int
    options: typing.List[Option]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
    options: typing.List[Option]
    packed: bool
    typeUrl: str

@typing.type_check_only
class FlowErrorDetails(typing_extensions.TypedDict, total=False):
    exceptionType: str
    flowStepId: str

@typing.type_check_only
class GenerateConfigReportRequest(typing_extensions.TypedDict, total=False):
    newConfig: typing.Dict[str, typing.Any]
    oldConfig: typing.Dict[str, typing.Any]

@typing.type_check_only
class GenerateConfigReportResponse(typing_extensions.TypedDict, total=False):
    changeReports: typing.List[ChangeReport]
    diagnostics: typing.List[Diagnostic]
    id: str
    serviceName: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class Http(typing_extensions.TypedDict, total=False):
    fullyDecodeReservedExpansion: bool
    rules: typing.List[HttpRule]

@typing.type_check_only
class HttpRule(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JwtLocation(typing_extensions.TypedDict, total=False):
    header: str
    query: str
    valuePrefix: str

@typing.type_check_only
class LabelDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    key: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListServiceConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceConfigs: typing.List[Service]

@typing.type_check_only
class ListServiceRolloutsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rollouts: typing.List[Rollout]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[ManagedService]

@typing.type_check_only
class LogDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    labels: typing.List[LabelDescriptor]
    name: str

@typing.type_check_only
class Logging(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[LoggingDestination]
    producerDestinations: typing.List[LoggingDestination]

@typing.type_check_only
class LoggingDestination(typing_extensions.TypedDict, total=False):
    logs: typing.List[str]
    monitoredResource: str

@typing.type_check_only
class ManagedService(typing_extensions.TypedDict, total=False):
    producerProjectId: str
    serviceName: str

@typing.type_check_only
class Method(typing_extensions.TypedDict, total=False):
    name: str
    options: typing.List[Option]
    requestStreaming: bool
    requestTypeUrl: str
    responseStreaming: bool
    responseTypeUrl: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class MetricDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    labels: typing.List[LabelDescriptor]
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
    monitoredResourceTypes: typing.List[str]
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
    metricCosts: typing.Dict[str, typing.Any]
    selector: str

@typing.type_check_only
class Mixin(typing_extensions.TypedDict, total=False):
    name: str
    root: str

@typing.type_check_only
class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    labels: typing.List[LabelDescriptor]
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
    consumerDestinations: typing.List[MonitoringDestination]
    producerDestinations: typing.List[MonitoringDestination]

@typing.type_check_only
class MonitoringDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

@typing.type_check_only
class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    progressPercentage: int
    resourceNames: typing.List[str]
    startTime: str
    steps: typing.List[Step]

@typing.type_check_only
class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

@typing.type_check_only
class Page(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class Quota(typing_extensions.TypedDict, total=False):
    limits: typing.List[QuotaLimit]
    metricRules: typing.List[MetricRule]

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
    values: typing.Dict[str, typing.Any]

@typing.type_check_only
class ResourceReference(typing_extensions.TypedDict, total=False):
    childType: str
    type: str

@typing.type_check_only
class Rollout(typing_extensions.TypedDict, total=False):
    createTime: str
    createdBy: str
    deleteServiceStrategy: DeleteServiceStrategy
    rolloutId: str
    serviceName: str
    status: typing_extensions.Literal[
        "ROLLOUT_STATUS_UNSPECIFIED",
        "IN_PROGRESS",
        "SUCCESS",
        "CANCELLED",
        "FAILED",
        "PENDING",
        "FAILED_ROLLED_BACK",
    ]
    trafficPercentStrategy: TrafficPercentStrategy

@typing.type_check_only
class Service(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

@typing.type_check_only
class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing_extensions.TypedDict, total=False):
    description: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "DONE",
        "NOT_STARTED",
        "IN_PROGRESS",
        "FAILED",
        "CANCELLED",
    ]

@typing.type_check_only
class SubmitConfigSourceRequest(typing_extensions.TypedDict, total=False):
    configSource: ConfigSource
    validateOnly: bool

@typing.type_check_only
class SubmitConfigSourceResponse(typing_extensions.TypedDict, total=False):
    serviceConfig: Service

@typing.type_check_only
class SystemParameter(typing_extensions.TypedDict, total=False):
    httpHeader: str
    name: str
    urlQueryParameter: str

@typing.type_check_only
class SystemParameterRule(typing_extensions.TypedDict, total=False):
    parameters: typing.List[SystemParameter]
    selector: str

@typing.type_check_only
class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TrafficPercentStrategy(typing_extensions.TypedDict, total=False):
    percentages: typing.Dict[str, typing.Any]

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    fields: typing.List[Field]
    name: str
    oneofs: typing.List[str]
    options: typing.List[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class UndeleteServiceResponse(typing_extensions.TypedDict, total=False):
    service: ManagedService

@typing.type_check_only
class Usage(typing_extensions.TypedDict, total=False):
    producerNotificationChannel: str
    requirements: typing.List[str]
    rules: typing.List[UsageRule]

@typing.type_check_only
class UsageRule(typing_extensions.TypedDict, total=False):
    allowUnregisteredCalls: bool
    selector: str
    skipServiceControl: bool
