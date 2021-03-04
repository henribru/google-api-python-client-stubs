import typing

import typing_extensions
@typing.type_check_only
class AddDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddDnsRecordSetRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    dnsRecordSet: DnsRecordSet
    zone: str

@typing.type_check_only
class AddDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddDnsZoneRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    dnsSuffix: str
    name: str

@typing.type_check_only
class AddDnsZoneResponse(typing_extensions.TypedDict, total=False):
    consumerPeeringZone: DnsZone
    producerPrivateZone: DnsZone

@typing.type_check_only
class AddRolesMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddRolesRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    policyBinding: typing.List[PolicyBinding]

@typing.type_check_only
class AddRolesResponse(typing_extensions.TypedDict, total=False):
    policyBinding: typing.List[PolicyBinding]

@typing.type_check_only
class AddSubnetworkRequest(typing_extensions.TypedDict, total=False):
    consumer: str
    consumerNetwork: str
    description: str
    ipPrefixLength: int
    region: str
    requestedAddress: str
    requestedRanges: typing.List[str]
    secondaryIpRangeSpecs: typing.List[SecondaryIpRangeSpec]
    subnetwork: str
    subnetworkUsers: typing.List[str]

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
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    network: str
    peering: str
    reservedPeeringRanges: typing.List[str]
    service: str

@typing.type_check_only
class ConsumerConfig(typing_extensions.TypedDict, total=False):
    consumerExportCustomRoutes: bool
    consumerExportSubnetRoutesWithPublicIp: bool
    consumerImportCustomRoutes: bool
    consumerImportSubnetRoutesWithPublicIp: bool
    producerExportCustomRoutes: bool
    producerExportSubnetRoutesWithPublicIp: bool
    producerImportCustomRoutes: bool
    producerImportSubnetRoutesWithPublicIp: bool
    producerNetwork: str
    reservedRanges: typing.List[
        GoogleCloudServicenetworkingV1ConsumerConfigReservedRange
    ]
    vpcScReferenceArchitectureEnabled: bool

@typing.type_check_only
class ConsumerConfigMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConsumerProject(typing_extensions.TypedDict, total=False):
    projectNum: str

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
class DeleteConnectionMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeletePeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DisableVpcServiceControlsRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str

@typing.type_check_only
class DnsRecordSet(typing_extensions.TypedDict, total=False):
    data: typing.List[str]
    domain: str
    ttl: str
    type: str

@typing.type_check_only
class DnsZone(typing_extensions.TypedDict, total=False):
    dnsSuffix: str
    name: str

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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableVpcServiceControlsRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str

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
class GoogleCloudServicenetworkingV1ConsumerConfigReservedRange(
    typing_extensions.TypedDict, total=False
):
    address: str
    ipPrefixLength: int
    name: str

@typing.type_check_only
class GoogleCloudServicenetworkingV1betaConnection(
    typing_extensions.TypedDict, total=False
):
    network: str
    peering: str
    reservedPeeringRanges: typing.List[str]
    service: str

@typing.type_check_only
class GoogleCloudServicenetworkingV1betaSubnetwork(
    typing_extensions.TypedDict, total=False
):
    ipCidrRange: str
    name: str
    network: str
    outsideAllocation: bool

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
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: typing.List[Connection]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListPeeredDnsDomainsResponse(typing_extensions.TypedDict, total=False):
    peeredDnsDomains: typing.List[PeeredDnsDomain]

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
class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

@typing.type_check_only
class Page(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class PeeredDnsDomain(typing_extensions.TypedDict, total=False):
    dnsSuffix: str
    name: str

@typing.type_check_only
class PeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PolicyBinding(typing_extensions.TypedDict, total=False):
    member: str
    role: str

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
class Range(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    network: str

@typing.type_check_only
class RangeReservation(typing_extensions.TypedDict, total=False):
    ipPrefixLength: int
    requestedRanges: typing.List[str]
    secondaryRangeIpPrefixLengths: typing.List[int]
    subnetworkCandidates: typing.List[Subnetwork]

@typing.type_check_only
class RemoveDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsRecordSetRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    dnsRecordSet: DnsRecordSet
    zone: str

@typing.type_check_only
class RemoveDnsRecordSetResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsZoneRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    name: str

@typing.type_check_only
class RemoveDnsZoneResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    destRange: str
    name: str
    network: str
    nextHopGateway: str

@typing.type_check_only
class SearchRangeRequest(typing_extensions.TypedDict, total=False):
    ipPrefixLength: int
    network: str

@typing.type_check_only
class SecondaryIpRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

@typing.type_check_only
class SecondaryIpRangeSpec(typing_extensions.TypedDict, total=False):
    ipPrefixLength: int
    rangeName: str
    requestedAddress: str

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    apis: typing.List[Api]
    authentication: Authentication
    backend: Backend
    billing: Billing
    configVersion: int
    context: Context
    control: Control
    customError: CustomError
    documentation: Documentation
    endpoints: typing.List[Endpoint]
    enums: typing.List[Enum]
    http: Http
    id: str
    logging: Logging
    logs: typing.List[LogDescriptor]
    metrics: typing.List[MetricDescriptor]
    monitoredResources: typing.List[MonitoredResourceDescriptor]
    monitoring: Monitoring
    name: str
    producerProjectId: str
    quota: Quota
    sourceInfo: SourceInfo
    systemParameters: SystemParameters
    systemTypes: typing.List[Type]
    title: str
    types: typing.List[Type]
    usage: Usage

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
class Subnetwork(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    name: str
    network: str
    outsideAllocation: bool
    region: str
    secondaryIpRanges: typing.List[SecondaryIpRange]

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
class Type(typing_extensions.TypedDict, total=False):
    fields: typing.List[Field]
    name: str
    oneofs: typing.List[str]
    options: typing.List[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class UpdateConsumerConfigRequest(typing_extensions.TypedDict, total=False):
    consumerConfig: ConsumerConfig

@typing.type_check_only
class UpdateDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateDnsRecordSetRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    existingDnsRecordSet: DnsRecordSet
    newDnsRecordSet: DnsRecordSet
    zone: str

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

@typing.type_check_only
class ValidateConsumerConfigRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    consumerProject: ConsumerProject
    rangeReservation: RangeReservation
    validateNetwork: bool

@typing.type_check_only
class ValidateConsumerConfigResponse(typing_extensions.TypedDict, total=False):
    existingSubnetworkCandidates: typing.List[Subnetwork]
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
