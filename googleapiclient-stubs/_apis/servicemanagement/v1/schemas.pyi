import typing

import typing_extensions

class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

class Monitoring(typing_extensions.TypedDict, total=False):
    producerDestinations: typing.List[MonitoringDestination]
    consumerDestinations: typing.List[MonitoringDestination]

class EnableServiceRequest(typing_extensions.TypedDict, total=False):
    consumerId: str

class Logging(typing_extensions.TypedDict, total=False):
    producerDestinations: typing.List[LoggingDestination]
    consumerDestinations: typing.List[LoggingDestination]

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str

class FlowErrorDetails(typing_extensions.TypedDict, total=False):
    flowStepId: str
    exceptionType: str

class Field(typing_extensions.TypedDict, total=False):
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
    packed: bool
    typeUrl: str
    oneofIndex: int
    name: str
    number: int
    options: typing.List[Option]
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    defaultValue: str

class MetricRule(typing_extensions.TypedDict, total=False):
    selector: str
    metricCosts: typing.Dict[str, typing.Any]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
    description: str
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
    displayName: str
    type: str
    labels: typing.List[LabelDescriptor]

class Quota(typing_extensions.TypedDict, total=False):
    metricRules: typing.List[MetricRule]
    limits: typing.List[QuotaLimit]

class Service(typing_extensions.TypedDict, total=False):
    control: Control
    backend: Backend
    logs: typing.List[LogDescriptor]
    endpoints: typing.List[Endpoint]
    usage: Usage
    title: str
    authentication: Authentication
    systemTypes: typing.List[Type]
    monitoring: Monitoring
    metrics: typing.List[MetricDescriptor]
    documentation: Documentation
    billing: Billing
    producerProjectId: str
    logging: Logging
    id: str
    name: str
    customError: CustomError
    http: Http
    configVersion: int
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    apis: typing.List[Api]
    enums: typing.List[Enum]
    quota: Quota
    types: typing.List[Type]
    sourceInfo: SourceInfo
    systemParameters: SystemParameters
    context: Context

class EnumValue(typing_extensions.TypedDict, total=False):
    number: int
    options: typing.List[Option]
    name: str

class Api(typing_extensions.TypedDict, total=False):
    sourceContext: SourceContext
    methods: typing.List[Method]
    options: typing.List[Option]
    version: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    name: str
    mixins: typing.List[Mixin]

class Control(typing_extensions.TypedDict, total=False):
    environment: str

class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

class EnableServiceResponse(typing_extensions.TypedDict, total=False): ...

class ResourceReference(typing_extensions.TypedDict, total=False):
    childType: str
    type: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class TrafficPercentStrategy(typing_extensions.TypedDict, total=False):
    percentages: typing.Dict[str, typing.Any]

class ServiceIdentity(typing_extensions.TypedDict, total=False):
    serviceAccountParent: str
    displayName: str
    description: str

class Step(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "DONE",
        "NOT_STARTED",
        "IN_PROGRESS",
        "FAILED",
        "CANCELLED",
    ]
    description: str

class DeleteServiceStrategy(typing_extensions.TypedDict, total=False): ...

class OperationMetadata(typing_extensions.TypedDict, total=False):
    startTime: str
    steps: typing.List[Step]
    progressPercentage: int
    resourceNames: typing.List[str]

class Http(typing.Dict[str, typing.Any]): ...

class GenerateConfigReportRequest(typing_extensions.TypedDict, total=False):
    oldConfig: typing.Dict[str, typing.Any]
    newConfig: typing.Dict[str, typing.Any]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class QuotaLimit(typing_extensions.TypedDict, total=False):
    description: str
    values: typing.Dict[str, typing.Any]
    unit: str
    metric: str
    displayName: str
    freeTier: str
    maxLimit: str
    name: str
    defaultLimit: str
    duration: str

class Advice(typing_extensions.TypedDict, total=False):
    description: str

class MetricDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    type: str
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    metadata: MetricDescriptorMetadata
    name: str
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
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]
    displayName: str
    monitoredResourceTypes: typing.List[str]
    unit: str

class BillingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    metrics: typing.List[str]

class GenerateConfigReportResponse(typing_extensions.TypedDict, total=False):
    changeReports: typing.List[ChangeReport]
    serviceName: str
    diagnostics: typing.List[Diagnostic]
    id: str

class Type(typing_extensions.TypedDict, total=False):
    fields: typing.List[Field]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    options: typing.List[Option]
    oneofs: typing.List[str]
    name: str
    sourceContext: SourceContext

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class LogDescriptor(typing_extensions.TypedDict, total=False):
    labels: typing.List[LabelDescriptor]
    displayName: str
    description: str
    name: str

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

class Option(typing_extensions.TypedDict, total=False):
    value: typing.Dict[str, typing.Any]
    name: str

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

class ConfigRef(typing_extensions.TypedDict, total=False):
    name: str

class HttpRule(typing.Dict[str, typing.Any]): ...

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class Authentication(typing_extensions.TypedDict, total=False):
    rules: typing.List[AuthenticationRule]
    providers: typing.List[AuthProvider]

class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

class CustomError(typing_extensions.TypedDict, total=False):
    types: typing.List[str]
    rules: typing.List[CustomErrorRule]

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[ManagedService]

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[Binding]
    auditConfigs: typing.List[AuditConfig]
    etag: str

class DocumentationRule(typing_extensions.TypedDict, total=False):
    description: str
    deprecationDescription: str
    selector: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    description: str
    location: str
    expression: str

class Rollout(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "ROLLOUT_STATUS_UNSPECIFIED",
        "IN_PROGRESS",
        "SUCCESS",
        "CANCELLED",
        "FAILED",
        "PENDING",
        "FAILED_ROLLED_BACK",
    ]
    serviceName: str
    trafficPercentStrategy: TrafficPercentStrategy
    rolloutId: str
    createTime: str
    createdBy: str
    deleteServiceStrategy: DeleteServiceStrategy

class Diagnostic(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["WARNING", "ERROR"]
    message: str
    location: str

class UndeleteServiceResponse(typing_extensions.TypedDict, total=False):
    service: ManagedService

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class Usage(typing_extensions.TypedDict, total=False):
    rules: typing.List[UsageRule]
    serviceIdentity: ServiceIdentity
    producerNotificationChannel: str
    requirements: typing.List[str]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class CustomErrorRule(typing_extensions.TypedDict, total=False):
    isErrorType: bool
    selector: str

class AuthenticationRule(typing_extensions.TypedDict, total=False):
    requirements: typing.List[AuthRequirement]
    oauth: OAuthRequirements
    allowWithoutCredential: bool
    selector: str

class ListServiceRolloutsResponse(typing_extensions.TypedDict, total=False):
    rollouts: typing.List[Rollout]
    nextPageToken: str

class ManagedService(typing_extensions.TypedDict, total=False):
    serviceName: str
    producerProjectId: str

class ConfigChange(typing_extensions.TypedDict, total=False):
    advices: typing.List[Advice]
    oldValue: str
    element: str
    newValue: str
    changeType: typing_extensions.Literal[
        "CHANGE_TYPE_UNSPECIFIED", "ADDED", "REMOVED", "MODIFIED"
    ]

class SystemParameter(typing_extensions.TypedDict, total=False):
    httpHeader: str
    name: str
    urlQueryParameter: str

class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]
    key: str
    description: str

class SystemParameterRule(typing_extensions.TypedDict, total=False):
    selector: str
    parameters: typing.List[SystemParameter]

class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

class Enum(typing_extensions.TypedDict, total=False):
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    enumvalue: typing.List[EnumValue]
    name: str
    options: typing.List[Option]

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    condition: Expr

class ChangeReport(typing_extensions.TypedDict, total=False):
    configChanges: typing.List[ConfigChange]

class UsageRule(typing_extensions.TypedDict, total=False):
    selector: str
    allowUnregisteredCalls: bool
    skipServiceControl: bool

class Documentation(typing.Dict[str, typing.Any]): ...

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

class MonitoringDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    metrics: typing.List[str]

class ContextRule(typing_extensions.TypedDict, total=False):
    allowedResponseExtensions: typing.List[str]
    requested: typing.List[str]
    allowedRequestExtensions: typing.List[str]
    provided: typing.List[str]
    selector: str

class Page(typing.Dict[str, typing.Any]): ...

class SubmitConfigSourceRequest(typing_extensions.TypedDict, total=False):
    validateOnly: bool
    configSource: ConfigSource

class JwtLocation(typing_extensions.TypedDict, total=False):
    valuePrefix: str
    query: str
    header: str

class LoggingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    logs: typing.List[str]

class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

class Endpoint(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    allowCors: bool
    target: str
    name: str

class BackendRule(typing_extensions.TypedDict, total=False):
    minDeadline: float
    disableAuth: bool
    deadline: float
    selector: str
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    address: str
    operationDeadline: float
    protocol: str
    jwtAudience: str

class Mixin(typing_extensions.TypedDict, total=False):
    name: str
    root: str

class ConfigSource(typing_extensions.TypedDict, total=False):
    files: typing.List[ConfigFile]
    id: str

class AuthProvider(typing_extensions.TypedDict, total=False):
    id: str
    audiences: str
    authorizationUrl: str
    jwtLocations: typing.List[JwtLocation]
    jwksUri: str
    issuer: str

class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    kind: str
    path: str

class DisableServiceResponse(typing_extensions.TypedDict, total=False): ...

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class SubmitConfigSourceResponse(typing_extensions.TypedDict, total=False):
    serviceConfig: Service

class ListServiceConfigsResponse(typing_extensions.TypedDict, total=False):
    serviceConfigs: typing.List[Service]
    nextPageToken: str

class Method(typing_extensions.TypedDict, total=False):
    name: str
    options: typing.List[Option]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    requestStreaming: bool
    responseTypeUrl: str
    responseStreaming: bool
    requestTypeUrl: str
