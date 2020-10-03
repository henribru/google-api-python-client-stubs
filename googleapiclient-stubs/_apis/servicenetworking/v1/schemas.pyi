import typing

import typing_extensions

class BackendRule(typing_extensions.TypedDict, total=False):
    disableAuth: bool
    minDeadline: float
    address: str
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    operationDeadline: float
    jwtAudience: str
    deadline: float
    selector: str
    protocol: str

class RangeReservation(typing_extensions.TypedDict, total=False):
    secondaryRangeIpPrefixLengths: typing.List[int]
    ipPrefixLength: int

class PolicyBinding(typing_extensions.TypedDict, total=False):
    role: str
    member: str

class RemoveDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...

class QuotaLimit(typing_extensions.TypedDict, total=False):
    description: str
    unit: str
    metric: str
    freeTier: str
    maxLimit: str
    name: str
    values: typing.Dict[str, typing.Any]
    defaultLimit: str
    displayName: str
    duration: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]

class Api(typing_extensions.TypedDict, total=False):
    methods: typing.List[Method]
    sourceContext: SourceContext
    mixins: typing.List[Mixin]
    options: typing.List[Option]
    name: str
    version: str
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]
    key: str

class Type(typing_extensions.TypedDict, total=False):
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    options: typing.List[Option]
    fields: typing.List[Field]
    sourceContext: SourceContext
    name: str
    oneofs: typing.List[str]

class ValidateConsumerConfigResponse(typing_extensions.TypedDict, total=False):
    isValid: bool
    validationError: typing_extensions.Literal[
        "VALIDATION_ERROR_UNSPECIFIED",
        "VALIDATION_NOT_REQUESTED",
        "SERVICE_NETWORKING_NOT_ENABLED",
        "NETWORK_NOT_FOUND",
        "NETWORK_NOT_PEERED",
        "NETWORK_PEERING_DELETED",
        "NETWORK_NOT_IN_CONSUMERS_PROJECT",
        "NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT",
        "HOST_PROJECT_NOT_FOUND",
        "CONSUMER_PROJECT_NOT_SERVICE_PROJECT",
        "RANGES_EXHAUSTED",
        "RANGES_NOT_RESERVED",
        "RANGES_DELETED_LATER",
        "COMPUTE_API_NOT_ENABLED",
    ]

class DnsZone(typing_extensions.TypedDict, total=False):
    name: str
    dnsSuffix: str

class CustomError(typing_extensions.TypedDict, total=False):
    types: typing.List[str]
    rules: typing.List[CustomErrorRule]

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class SystemParameterRule(typing_extensions.TypedDict, total=False):
    selector: str
    parameters: typing.List[SystemParameter]

class Empty(typing_extensions.TypedDict, total=False): ...

class UpdateDnsRecordSetRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    zone: str
    newDnsRecordSet: DnsRecordSet
    existingDnsRecordSet: DnsRecordSet

class PeeredDnsDomain(typing_extensions.TypedDict, total=False):
    name: str
    dnsSuffix: str

class Page(typing.Dict[str, typing.Any]): ...

class GoogleCloudServicenetworkingV1betaSubnetwork(
    typing_extensions.TypedDict, total=False
):
    network: str
    name: str
    ipCidrRange: str
    outsideAllocation: bool

class Route(typing_extensions.TypedDict, total=False):
    destRange: str
    network: str
    nextHopGateway: str
    name: str

class MonitoringDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

class AuthRequirement(typing_extensions.TypedDict, total=False):
    audiences: str
    providerId: str

class Field(typing_extensions.TypedDict, total=False):
    typeUrl: str
    name: str
    number: int
    jsonName: str
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
    defaultValue: str
    oneofIndex: int
    options: typing.List[Option]
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]

class RemoveDnsRecordSetRequest(typing_extensions.TypedDict, total=False):
    dnsRecordSet: DnsRecordSet
    zone: str
    consumerNetwork: str

class SystemParameter(typing_extensions.TypedDict, total=False):
    urlQueryParameter: str
    httpHeader: str
    name: str

class AuthProvider(typing_extensions.TypedDict, total=False):
    authorizationUrl: str
    jwtLocations: typing.List[JwtLocation]
    audiences: str
    id: str
    jwksUri: str
    issuer: str

class LoggingDestination(typing_extensions.TypedDict, total=False):
    monitoredResource: str
    logs: typing.List[str]

class SearchRangeRequest(typing_extensions.TypedDict, total=False):
    network: str
    ipPrefixLength: int

class RemoveDnsRecordSetResponse(typing_extensions.TypedDict, total=False): ...

class Backend(typing_extensions.TypedDict, total=False):
    rules: typing.List[BackendRule]

class AddRolesRequest(typing_extensions.TypedDict, total=False):
    policyBinding: typing.List[PolicyBinding]
    consumerNetwork: str

class Subnetwork(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    network: str
    name: str
    outsideAllocation: bool

class RemoveDnsZoneRequest(typing_extensions.TypedDict, total=False):
    name: str
    consumerNetwork: str

class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: typing.List[Connection]

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    type: str
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
    displayName: str

class ValidateConsumerConfigRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    consumerProject: ConsumerProject
    rangeReservation: RangeReservation
    validateNetwork: bool

class AddDnsRecordSetRequest(typing_extensions.TypedDict, total=False):
    zone: str
    dnsRecordSet: DnsRecordSet
    consumerNetwork: str

class DisableVpcServiceControlsRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class Endpoint(typing_extensions.TypedDict, total=False):
    name: str
    target: str
    allowCors: bool
    aliases: typing.List[str]

class EnableVpcServiceControlsRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str

class Http(typing_extensions.TypedDict, total=False):
    fullyDecodeReservedExpansion: bool
    rules: typing.List[HttpRule]

class Range(typing_extensions.TypedDict, total=False):
    network: str
    ipCidrRange: str

class SystemParameters(typing_extensions.TypedDict, total=False):
    rules: typing.List[SystemParameterRule]

class Logging(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[LoggingDestination]
    producerDestinations: typing.List[LoggingDestination]

class BillingDestination(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    monitoredResource: str

class Method(typing_extensions.TypedDict, total=False):
    requestStreaming: bool
    name: str
    responseStreaming: bool
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    requestTypeUrl: str
    responseTypeUrl: str
    options: typing.List[Option]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class ServiceIdentity(typing_extensions.TypedDict, total=False):
    serviceAccountParent: str
    description: str
    displayName: str

class Enum(typing_extensions.TypedDict, total=False):
    options: typing.List[Option]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    enumvalue: typing.List[EnumValue]
    sourceContext: SourceContext
    name: str

class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[BillingDestination]

class Monitoring(typing_extensions.TypedDict, total=False):
    consumerDestinations: typing.List[MonitoringDestination]
    producerDestinations: typing.List[MonitoringDestination]

class UsageRule(typing_extensions.TypedDict, total=False):
    skipServiceControl: bool
    allowUnregisteredCalls: bool
    selector: str

class JwtLocation(typing_extensions.TypedDict, total=False):
    valuePrefix: str
    header: str
    query: str

class ConsumerProject(typing_extensions.TypedDict, total=False):
    projectNum: str

class RemoveDnsZoneResponse(typing_extensions.TypedDict, total=False): ...
class UpdateDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

class Documentation(typing_extensions.TypedDict, total=False):
    rules: typing.List[DocumentationRule]
    summary: str
    serviceRootUrl: str
    overview: str
    pages: typing.List[Page]
    documentationRootUrl: str

class DnsRecordSet(typing_extensions.TypedDict, total=False):
    type: str
    domain: str
    ttl: str
    data: typing.List[str]

class Quota(typing_extensions.TypedDict, total=False):
    metricRules: typing.List[MetricRule]
    limits: typing.List[QuotaLimit]

class PeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...
class AddDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

class LogDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str
    labels: typing.List[LabelDescriptor]

class MetricRule(typing_extensions.TypedDict, total=False):
    selector: str
    metricCosts: typing.Dict[str, typing.Any]

class EnumValue(typing_extensions.TypedDict, total=False):
    number: int
    options: typing.List[Option]
    name: str

class AddSubnetworkRequest(typing_extensions.TypedDict, total=False):
    description: str
    subnetwork: str
    region: str
    consumer: str
    ipPrefixLength: int
    subnetworkUsers: typing.List[str]
    requestedAddress: str
    consumerNetwork: str

class HttpRule(typing.Dict[str, typing.Any]): ...
class RemoveDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

class AddRolesResponse(typing_extensions.TypedDict, total=False):
    policyBinding: typing.List[PolicyBinding]

class AddDnsZoneRequest(typing_extensions.TypedDict, total=False):
    dnsSuffix: str
    name: str
    consumerNetwork: str

class CustomErrorRule(typing_extensions.TypedDict, total=False):
    isErrorType: bool
    selector: str

class Authentication(typing_extensions.TypedDict, total=False):
    providers: typing.List[AuthProvider]
    rules: typing.List[AuthenticationRule]

class Usage(typing_extensions.TypedDict, total=False):
    producerNotificationChannel: str
    serviceIdentity: ServiceIdentity
    requirements: typing.List[str]
    rules: typing.List[UsageRule]

class ListPeeredDnsDomainsResponse(typing_extensions.TypedDict, total=False):
    peeredDnsDomains: typing.List[PeeredDnsDomain]

class SourceInfo(typing_extensions.TypedDict, total=False):
    sourceFiles: typing.List[typing.Dict[str, typing.Any]]

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
    unit: str
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    name: str
    monitoredResourceTypes: typing.List[str]
    labels: typing.List[LabelDescriptor]
    displayName: str
    description: str
    metadata: MetricDescriptorMetadata
    type: str

class AddDnsZoneResponse(typing_extensions.TypedDict, total=False):
    consumerPeeringZone: DnsZone
    producerPrivateZone: DnsZone

class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

class Control(typing_extensions.TypedDict, total=False):
    environment: str

class CustomHttpPattern(typing_extensions.TypedDict, total=False):
    kind: str
    path: str

class Connection(typing_extensions.TypedDict, total=False):
    network: str
    reservedPeeringRanges: typing.List[str]
    service: str
    peering: str

class Service(typing_extensions.TypedDict, total=False):
    logs: typing.List[LogDescriptor]
    usage: Usage
    billing: Billing
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    sourceInfo: SourceInfo
    types: typing.List[Type]
    name: str
    authentication: Authentication
    logging: Logging
    control: Control
    monitoring: Monitoring
    apis: typing.List[Api]
    producerProjectId: str
    backend: Backend
    systemTypes: typing.List[Type]
    context: Context
    http: Http
    customError: CustomError
    id: str
    endpoints: typing.List[Endpoint]
    metrics: typing.List[MetricDescriptor]
    enums: typing.List[Enum]
    title: str
    documentation: Documentation
    configVersion: int
    quota: Quota
    systemParameters: SystemParameters

class AddDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...
class AddRolesMetadata(typing_extensions.TypedDict, total=False): ...

class AuthenticationRule(typing_extensions.TypedDict, total=False):
    requirements: typing.List[AuthRequirement]
    allowWithoutCredential: bool
    oauth: OAuthRequirements
    selector: str

class DeletePeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...

class Mixin(typing_extensions.TypedDict, total=False):
    root: str
    name: str

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

class OAuthRequirements(typing_extensions.TypedDict, total=False):
    canonicalScopes: str

class ContextRule(typing_extensions.TypedDict, total=False):
    allowedResponseExtensions: typing.List[str]
    allowedRequestExtensions: typing.List[str]
    requested: typing.List[str]
    provided: typing.List[str]
    selector: str

class Context(typing_extensions.TypedDict, total=False):
    rules: typing.List[ContextRule]

class DocumentationRule(typing_extensions.TypedDict, total=False):
    deprecationDescription: str
    description: str
    selector: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...
