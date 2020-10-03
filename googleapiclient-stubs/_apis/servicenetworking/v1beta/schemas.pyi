import typing

import typing_extensions

class UpdateDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

class Monitoring(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[MonitoringDestination]
    producerDestinations: typing.List[MonitoringDestination]

class DeletePeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...

class LogDescriptor(typing_extensions.TypedDict, total=False):
    displayName: str
    description: str
    labels: typing.List[LabelDescriptor]
    name: str

class DnsZone(typing_extensions.TypedDict, total=False):
    name: str
    dnsSuffix: str

class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

class RemoveDnsZoneResponse(typing_extensions.TypedDict, total=False): ...
class AddDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...
class PeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...

class SystemParameter(typing_extensions.TypedDict, total=False):
    httpHeader: str
    urlQueryParameter: str
    name: str

class QuotaLimit(typing_extensions.TypedDict, total=False):
    displayName: str
    unit: str
    defaultLimit: str
    duration: str
    freeTier: str
    maxLimit: str
    name: str
    values: typing.Dict[str, typing.Any]
    metric: str
    description: str

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

class Logging(typing_extensions.TypedDict, total=False):
    producerDestinations: typing.List[LoggingDestination]
    consumerDestinations: typing.List[LoggingDestination]

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
    name: str
    labels: typing.List[LabelDescriptor]
    description: str
    displayName: str
    type: str

class MetricRule(typing_extensions.TypedDict, total=False):
    metricCosts: typing.Dict[str, typing.Any]
    selector: str

class GoogleCloudServicenetworkingV1betaSubnetwork(
    typing_extensions.TypedDict, total=False
):
    name: str
    network: str
    ipCidrRange: str
    outsideAllocation: bool

class SystemParameterRule(typing_extensions.TypedDict, total=False):
    parameters: typing.List[SystemParameter]
    selector: str

class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

class MonitoringDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

class Field(typing_extensions.TypedDict, total=False):
    typeUrl: str
    defaultValue: str
    jsonName: str
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    number: int
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
    name: str
    options: typing.List[Option]
    oneofIndex: int

class EnumValue(typing_extensions.TypedDict, total=False):
    name: str
    number: int
    options: typing.List[Option]

class LoggingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    logs: typing.List[str]

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]

class AuthProvider(typing_extensions.TypedDict, total=False):
    jwksUri: str
    audiences: str
    id: str
    authorizationUrl: str
    issuer: str
    jwtLocations: typing.List[JwtLocation]

class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: typing.List[Connection]

class CustomErrorRule(typing_extensions.TypedDict, total=False):
    isErrorType: bool
    selector: str

class RemoveDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...

class Type(typing_extensions.TypedDict, total=False):
    oneofs: typing.List[str]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    name: str
    fields: typing.List[Field]
    options: typing.List[Option]

class MetricDescriptorMetadata(typing_extensions.TypedDict, total=False):
    samplePeriod: str
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

class Authentication(typing_extensions.TypedDict, total=False):
    providers: typing.List[AuthProvider]
    rules: typing.List[AuthenticationRule]

class Connection(typing_extensions.TypedDict, total=False):
    reservedPeeringRanges: typing.List[str]
    service: str
    peering: str
    network: str

class JwtLocation(typing_extensions.TypedDict, total=False):
    header: str
    valuePrefix: str
    query: str

class HttpRule(typing.Dict[str, typing.Any]): ...

class Method(typing_extensions.TypedDict, total=False):
    responseTypeUrl: str
    options: typing.List[Option]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    name: str
    requestTypeUrl: str
    requestStreaming: bool
    responseStreaming: bool

class Documentation(typing_extensions.TypedDict, total=False):
    overview: str
    rules: typing.List[DocumentationRule]
    pages: typing.List[Page]
    documentationRootUrl: str
    serviceRootUrl: str
    summary: str

class Service(typing_extensions.TypedDict, total=False):
    usage: Usage
    systemTypes: typing.List[Type]
    quota: Quota
    id: str
    logs: typing.List[LogDescriptor]
    customError: CustomError
    systemParameters: SystemParameters
    context: Context
    documentation: Documentation
    control: Control
    apis: typing.List[Api]
    billing: Billing
    title: str
    logging: Logging
    authentication: Authentication
    configVersion: int
    http: Http
    endpoints: typing.List[Endpoint]
    producerProjectId: str
    types: typing.List[Type]
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    sourceInfo: SourceInfo
    enums: typing.List[Enum]
    metrics: typing.List[MetricDescriptor]
    backend: Backend
    name: str
    monitoring: Monitoring

class ContextRule(typing_extensions.TypedDict, total=False):
    provided: typing.List[str]
    allowedRequestExtensions: typing.List[str]
    requested: typing.List[str]
    selector: str
    allowedResponseExtensions: typing.List[str]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    kind: str
    path: str

class UsageRule(typing_extensions.TypedDict, total=False):
    selector: str
    skipServiceControl: bool
    allowUnregisteredCalls: bool

class MetricDescriptor(typing_extensions.TypedDict, total=False):
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
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    displayName: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]
    unit: str
    labels: typing.List[LabelDescriptor]
    metadata: MetricDescriptorMetadata
    name: str
    description: str

class AuthenticationRule(typing_extensions.TypedDict, total=False):
    allowWithoutCredential: bool
    oauth: OAuthRequirements
    selector: str
    requirements: typing.List[AuthRequirement]

class PeeredDnsDomain(typing_extensions.TypedDict, total=False):
    name: str
    dnsSuffix: str

class AddDnsZoneResponse(typing_extensions.TypedDict, total=False):
    consumerPeeringZone: DnsZone
    producerPrivateZone: DnsZone

class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

class Mixin(typing_extensions.TypedDict, total=False):
    root: str
    name: str

class SearchRangeRequest(typing_extensions.TypedDict, total=False):
    network: str
    ipPrefixLength: int

class Range(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    network: str

class Http(typing.Dict[str, typing.Any]): ...

class AddRolesResponse(typing_extensions.TypedDict, total=False):
    policyBinding: typing.List[PolicyBinding]

class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

class DocumentationRule(typing_extensions.TypedDict, total=False):
    description: str
    selector: str
    deprecationDescription: str

class Option(typing_extensions.TypedDict, total=False):
    value: typing.Dict[str, typing.Any]
    name: str

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    key: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]
    description: str

class BillingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    metrics: typing.List[str]

class AddDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...

class AddSubnetworkRequest(typing_extensions.TypedDict, total=False):
    subnetworkUsers: typing.List[str]
    consumerNetwork: str
    ipPrefixLength: int
    region: str
    description: str
    subnetwork: str
    requestedAddress: str
    consumer: str

class DnsRecordSet(typing_extensions.TypedDict, total=False):
    ttl: str
    data: typing.List[str]
    domain: str
    type: str

class Usage(typing_extensions.TypedDict, total=False):
    producerNotificationChannel: str
    requirements: typing.List[str]
    rules: typing.List[UsageRule]
    serviceIdentity: ServiceIdentity

class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

class Enum(typing_extensions.TypedDict, total=False):
    options: typing.List[Option]
    name: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    enumvalue: typing.List[EnumValue]
    sourceContext: SourceContext

class PolicyBinding(typing_extensions.TypedDict, total=False):
    member: str
    role: str

class Api(typing_extensions.TypedDict, total=False):
    version: str
    options: typing.List[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    mixins: typing.List[Mixin]
    name: str
    methods: typing.List[Method]

class CustomError(typing_extensions.TypedDict, total=False):
    types: typing.List[str]
    rules: typing.List[CustomErrorRule]

class Subnetwork(typing_extensions.TypedDict, total=False):
    network: str
    ipCidrRange: str
    outsideAllocation: bool
    name: str

class RemoveDnsRecordSetResponse(typing_extensions.TypedDict, total=False): ...
class RemoveDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...
class Page(typing.Dict[str, typing.Any]): ...

class BackendRule(typing_extensions.TypedDict, total=False):
    minDeadline: float
    deadline: float
    protocol: str
    jwtAudience: str
    operationDeadline: float
    selector: str
    disableAuth: bool
    address: str
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]

class Route(typing_extensions.TypedDict, total=False):
    network: str
    name: str
    nextHopGateway: str
    destRange: str

class Endpoint(typing_extensions.TypedDict, total=False):
    name: str
    target: str
    allowCors: bool
    aliases: typing.List[str]

class Quota(typing_extensions.TypedDict, total=False):
    metricRules: typing.List[MetricRule]
    limits: typing.List[QuotaLimit]

class ServiceIdentity(typing_extensions.TypedDict, total=False):
    description: str
    serviceAccountParent: str
    displayName: str

class Control(typing_extensions.TypedDict, total=False):
    environment: str

class AddRolesMetadata(typing_extensions.TypedDict, total=False): ...
