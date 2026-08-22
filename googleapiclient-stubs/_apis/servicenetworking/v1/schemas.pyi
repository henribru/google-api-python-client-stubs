import typing

_list = list

@typing.type_check_only
class AddDnsRecordSetMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class AddDnsRecordSetRequest(typing.TypedDict, total=False):
    consumerNetwork: str
    dnsRecordSet: DnsRecordSet
    zone: str

@typing.type_check_only
class AddDnsZoneMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class AddDnsZoneRequest(typing.TypedDict, total=False):
    consumerNetwork: str
    dnsSuffix: str
    name: str

@typing.type_check_only
class AddDnsZoneResponse(typing.TypedDict, total=False):
    consumerPeeringZone: DnsZone
    producerPrivateZone: DnsZone

@typing.type_check_only
class AddRolesMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class AddRolesRequest(typing.TypedDict, total=False):
    consumerNetwork: str
    policyBinding: _list[PolicyBinding]

@typing.type_check_only
class AddRolesResponse(typing.TypedDict, total=False):
    policyBinding: _list[PolicyBinding]

@typing.type_check_only
class AddSubnetworkRequest(typing.TypedDict, total=False):
    allowSubnetCidrRoutesOverlap: bool
    checkServiceNetworkingUsePermission: bool
    computeIdempotencyWindow: str
    consumer: str
    consumerNetwork: str
    description: str
    internalRange: str
    ipPrefixLength: int
    outsideAllocationPublicIpRange: str
    privateIpv6GoogleAccess: str
    purpose: str
    region: str
    requestedAddress: str
    requestedRanges: _list[str]
    role: str
    secondaryIpRangeSpecs: _list[SecondaryIpRangeSpec]
    skipRequestedAddressValidation: bool
    subnetwork: str
    subnetworkUsers: _list[str]
    useCustomComputeIdempotencyWindow: bool

@typing.type_check_only
class Api(typing.TypedDict, total=False):
    edition: str
    methods: _list[Method]
    mixins: _list[Mixin]
    name: str
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"]
    version: str

@typing.type_check_only
class Aspect(typing.TypedDict, total=False):
    kind: str
    rules: _list[AspectRule]
    spec: dict[str, typing.Any]

@typing.type_check_only
class AspectRule(typing.TypedDict, total=False):
    config: dict[str, typing.Any]
    selector: str

@typing.type_check_only
class AuthProvider(typing.TypedDict, total=False):
    audiences: str
    authorizationUrl: str
    id: str
    issuer: str
    jwksUri: str
    jwtLocations: _list[JwtLocation]

@typing.type_check_only
class AuthRequirement(typing.TypedDict, total=False):
    audiences: str
    providerId: str

@typing.type_check_only
class Authentication(typing.TypedDict, total=False):
    providers: _list[AuthProvider]
    rules: _list[AuthenticationRule]

@typing.type_check_only
class AuthenticationRule(typing.TypedDict, total=False):
    allowWithoutCredential: bool
    oauth: OAuthRequirements
    requirements: _list[AuthRequirement]
    selector: str

@typing.type_check_only
class Backend(typing.TypedDict, total=False):
    rules: _list[BackendRule]

@typing.type_check_only
class BackendRule(typing.TypedDict, total=False):
    address: str
    deadline: float
    disableAuth: bool
    jwtAudience: str
    loadBalancingPolicy: str
    minDeadline: float
    operationDeadline: float
    overridesByRequestProtocol: dict[str, typing.Any]
    pathTranslation: typing.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    protocol: str
    selector: str

@typing.type_check_only
class BatchingConfigProto(typing.TypedDict, total=False):
    batchDescriptor: BatchingDescriptorProto
    thresholds: BatchingSettingsProto

@typing.type_check_only
class BatchingDescriptorProto(typing.TypedDict, total=False):
    batchedField: str
    discriminatorFields: _list[str]
    subresponseField: str

@typing.type_check_only
class BatchingSettingsProto(typing.TypedDict, total=False):
    delayThreshold: str
    elementCountLimit: int
    elementCountThreshold: int
    flowControlByteLimit: int
    flowControlElementLimit: int
    flowControlLimitExceededBehavior: typing.Literal[
        "UNSET_BEHAVIOR", "THROW_EXCEPTION", "BLOCK", "IGNORE"
    ]
    requestByteLimit: int
    requestByteThreshold: str

@typing.type_check_only
class Billing(typing.TypedDict, total=False):
    consumerDestinations: _list[BillingDestination]

@typing.type_check_only
class BillingDestination(typing.TypedDict, total=False):
    metrics: _list[str]
    monitoredResource: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CleanupConnectionMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClientLibrarySettings(typing.TypedDict, total=False):
    cppSettings: CppSettings
    dotnetSettings: DotnetSettings
    goSettings: GoSettings
    javaSettings: JavaSettings
    launchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    nodeSettings: NodeSettings
    phpSettings: PhpSettings
    pythonSettings: PythonSettings
    restNumericEnums: bool
    rubySettings: RubySettings
    version: str

@typing.type_check_only
class CloudSQLConfig(typing.TypedDict, total=False):
    service: str
    umbrellaNetwork: str
    umbrellaProject: str

@typing.type_check_only
class CommonLanguageSettings(typing.TypedDict, total=False):
    destinations: _list[
        typing.Literal[
            "CLIENT_LIBRARY_DESTINATION_UNSPECIFIED", "GITHUB", "PACKAGE_MANAGER"
        ]
    ]
    referenceDocsUri: str
    selectiveGapicGeneration: SelectiveGapicGeneration

@typing.type_check_only
class Connection(typing.TypedDict, total=False):
    network: str
    peering: str
    reservedPeeringRanges: _list[str]
    service: str

@typing.type_check_only
class ConsumerConfig(typing.TypedDict, total=False):
    cloudsqlConfigs: _list[CloudSQLConfig]
    consumerExportCustomRoutes: bool
    consumerExportSubnetRoutesWithPublicIp: bool
    consumerImportCustomRoutes: bool
    consumerImportSubnetRoutesWithPublicIp: bool
    consumerPeeringActive: bool
    producerExportCustomRoutes: bool
    producerExportSubnetRoutesWithPublicIp: bool
    producerImportCustomRoutes: bool
    producerImportSubnetRoutesWithPublicIp: bool
    producerNetwork: str
    reservedRanges: _list[GoogleCloudServicenetworkingV1ConsumerConfigReservedRange]
    usedIpRanges: _list[str]
    vpcScReferenceArchitectureEnabled: bool

@typing.type_check_only
class ConsumerConfigMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class ConsumerProject(typing.TypedDict, total=False):
    projectNum: str

@typing.type_check_only
class Context(typing.TypedDict, total=False):
    rules: _list[ContextRule]

@typing.type_check_only
class ContextRule(typing.TypedDict, total=False):
    allowedRequestExtensions: _list[str]
    allowedResponseExtensions: _list[str]
    provided: _list[str]
    requested: _list[str]
    selector: str

@typing.type_check_only
class Control(typing.TypedDict, total=False):
    environment: str
    methodPolicies: _list[MethodPolicy]

@typing.type_check_only
class CppSettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings

@typing.type_check_only
class CustomError(typing.TypedDict, total=False):
    rules: _list[CustomErrorRule]
    types: _list[str]

@typing.type_check_only
class CustomErrorRule(typing.TypedDict, total=False):
    isErrorType: bool
    selector: str

@typing.type_check_only
class CustomHttpPattern(typing.TypedDict, total=False):
    kind: str
    path: str

@typing.type_check_only
class DeleteConnectionMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteConnectionRequest(typing.TypedDict, total=False):
    consumerNetwork: str

@typing.type_check_only
class DeletePeeredDnsDomainMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DisableVpcServiceControlsRequest(typing.TypedDict, total=False):
    consumerNetwork: str

@typing.type_check_only
class DnsRecordSet(typing.TypedDict, total=False):
    data: _list[str]
    domain: str
    ttl: str
    type: str

@typing.type_check_only
class DnsZone(typing.TypedDict, total=False):
    dnsSuffix: str
    name: str

@typing.type_check_only
class DnsZonePair(typing.TypedDict, total=False):
    consumerPeeringZone: DnsZone
    producerPrivateZone: DnsZone

@typing.type_check_only
class Documentation(typing.TypedDict, total=False):
    additionalIamInfo: str
    documentationRootUrl: str
    overview: str
    pages: _list[Page]
    rules: _list[DocumentationRule]
    sectionOverrides: _list[Page]
    serviceRootUrl: str
    summary: str

@typing.type_check_only
class DocumentationRule(typing.TypedDict, total=False):
    deprecationDescription: str
    description: str
    disableReplacementWords: str
    selector: str

@typing.type_check_only
class DotnetSettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings
    forcedNamespaceAliases: _list[str]
    handwrittenSignatures: _list[str]
    ignoredResources: _list[str]
    renamedResources: dict[str, typing.Any]
    renamedServices: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableVpcServiceControlsRequest(typing.TypedDict, total=False):
    consumerNetwork: str

@typing.type_check_only
class Endpoint(typing.TypedDict, total=False):
    aliases: _list[str]
    allowCors: bool
    name: str
    target: str

@typing.type_check_only
class Enum(typing.TypedDict, total=False):
    edition: str
    enumvalue: _list[EnumValue]
    name: str
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"]

@typing.type_check_only
class EnumValue(typing.TypedDict, total=False):
    name: str
    number: int
    options: _list[Option]

@typing.type_check_only
class ExperimentalFeatures(typing.TypedDict, total=False):
    protobufPythonicTypesEnabled: bool
    restAsyncIoEnabled: bool
    unversionedPackageDisabled: bool

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    cardinality: typing.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    defaultValue: str
    jsonName: str
    kind: typing.Literal[
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
class FieldPolicy(typing.TypedDict, total=False):
    resourcePermission: str
    resourceType: str
    selector: str

@typing.type_check_only
class GetDnsZoneResponse(typing.TypedDict, total=False):
    consumerPeeringZone: DnsZone
    producerPrivateZone: DnsZone

@typing.type_check_only
class GoSettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings
    renamedServices: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudServicenetworkingV1ConsumerConfigReservedRange(
    typing.TypedDict, total=False
):
    address: str
    ipPrefixLength: int
    name: str

@typing.type_check_only
class GoogleCloudServicenetworkingV1betaConnection(typing.TypedDict, total=False):
    network: str
    peering: str
    reservedPeeringRanges: _list[str]
    service: str

@typing.type_check_only
class GoogleCloudServicenetworkingV1betaSubnetwork(typing.TypedDict, total=False):
    ipCidrRange: str
    name: str
    network: str
    outsideAllocation: bool

@typing.type_check_only
class Http(typing.TypedDict, total=False):
    fullyDecodeReservedExpansion: bool
    rules: _list[HttpRule]

@typing.type_check_only
class HttpRule(typing.TypedDict, total=False):
    additionalBindings: _list[HttpRule]
    body: str
    custom: CustomHttpPattern
    delete: str
    get: str
    patch: str
    post: str
    put: str
    responseBody: str
    selector: str

@typing.type_check_only
class JavaSettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings
    libraryPackage: str
    serviceClassNames: dict[str, typing.Any]

@typing.type_check_only
class JwtLocation(typing.TypedDict, total=False):
    cookie: str
    header: str
    query: str
    valuePrefix: str

@typing.type_check_only
class LabelDescriptor(typing.TypedDict, total=False):
    description: str
    key: str
    valueType: typing.Literal["STRING", "BOOL", "INT64"]

@typing.type_check_only
class ListConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[Connection]

@typing.type_check_only
class ListDnsRecordSetsResponse(typing.TypedDict, total=False):
    dnsRecordSets: _list[DnsRecordSet]

@typing.type_check_only
class ListDnsZonesResponse(typing.TypedDict, total=False):
    dnsZonePairs: _list[DnsZonePair]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPeeredDnsDomainsResponse(typing.TypedDict, total=False):
    peeredDnsDomains: _list[PeeredDnsDomain]

@typing.type_check_only
class LogDescriptor(typing.TypedDict, total=False):
    description: str
    displayName: str
    labels: _list[LabelDescriptor]
    name: str

@typing.type_check_only
class Logging(typing.TypedDict, total=False):
    consumerDestinations: _list[LoggingDestination]
    producerDestinations: _list[LoggingDestination]

@typing.type_check_only
class LoggingDestination(typing.TypedDict, total=False):
    logs: _list[str]
    monitoredResource: str

@typing.type_check_only
class LongRunning(typing.TypedDict, total=False):
    initialPollDelay: str
    maxPollDelay: str
    pollDelayMultiplier: float
    totalPollTimeout: str

@typing.type_check_only
class Method(typing.TypedDict, total=False):
    edition: str
    name: str
    options: _list[Option]
    requestStreaming: bool
    requestTypeUrl: str
    responseStreaming: bool
    responseTypeUrl: str
    syntax: typing.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"]

@typing.type_check_only
class MethodPolicy(typing.TypedDict, total=False):
    requestPolicies: _list[FieldPolicy]
    selector: str

@typing.type_check_only
class MethodSettings(typing.TypedDict, total=False):
    autoPopulatedFields: _list[str]
    batching: BatchingConfigProto
    longRunning: LongRunning
    selector: str

@typing.type_check_only
class MetricDescriptor(typing.TypedDict, total=False):
    description: str
    displayName: str
    labels: _list[LabelDescriptor]
    launchStage: typing.Literal[
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
    metricKind: typing.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    monitoredResourceTypes: _list[str]
    name: str
    type: str
    unit: str
    valueType: typing.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]

@typing.type_check_only
class MetricDescriptorMetadata(typing.TypedDict, total=False):
    ingestDelay: str
    launchStage: typing.Literal[
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
    timeSeriesResourceHierarchyLevel: _list[
        typing.Literal[
            "TIME_SERIES_RESOURCE_HIERARCHY_LEVEL_UNSPECIFIED",
            "PROJECT",
            "ORGANIZATION",
            "FOLDER",
        ]
    ]

@typing.type_check_only
class MetricRule(typing.TypedDict, total=False):
    agenticMetricCosts: dict[str, typing.Any]
    metricCosts: dict[str, typing.Any]
    nonagenticMetricCosts: dict[str, typing.Any]
    selector: str

@typing.type_check_only
class Mixin(typing.TypedDict, total=False):
    name: str
    root: str

@typing.type_check_only
class MonitoredResourceDescriptor(typing.TypedDict, total=False):
    description: str
    displayName: str
    labels: _list[LabelDescriptor]
    launchStage: typing.Literal[
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
class Monitoring(typing.TypedDict, total=False):
    consumerDestinations: _list[MonitoringDestination]
    producerDestinations: _list[MonitoringDestination]

@typing.type_check_only
class MonitoringDestination(typing.TypedDict, total=False):
    metrics: _list[str]
    monitoredResource: str

@typing.type_check_only
class NodeSettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings

@typing.type_check_only
class OAuthRequirements(typing.TypedDict, total=False):
    canonicalScopes: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Option(typing.TypedDict, total=False):
    name: str
    value: dict[str, typing.Any]

@typing.type_check_only
class Page(typing.TypedDict, total=False):
    content: str
    name: str
    subpages: _list[Page]

@typing.type_check_only
class PartialDeleteConnectionMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class PeeredDnsDomain(typing.TypedDict, total=False):
    dnsSuffix: str
    name: str

@typing.type_check_only
class PeeredDnsDomainMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class PhpSettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings
    libraryPackage: str

@typing.type_check_only
class PolicyBinding(typing.TypedDict, total=False):
    member: str
    role: str

@typing.type_check_only
class Publishing(typing.TypedDict, total=False):
    apiShortName: str
    codeownerGithubTeams: _list[str]
    docTagPrefix: str
    documentationUri: str
    githubLabel: str
    librarySettings: _list[ClientLibrarySettings]
    methodSettings: _list[MethodSettings]
    newIssueUri: str
    organization: typing.Literal[
        "CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED",
        "CLOUD",
        "ADS",
        "PHOTOS",
        "STREET_VIEW",
        "SHOPPING",
        "GEO",
        "GENERATIVE_AI",
        "HEALTH",
    ]
    protoReferenceDocumentationUri: str
    restReferenceDocumentationUri: str

@typing.type_check_only
class PythonSettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings
    experimentalFeatures: ExperimentalFeatures

@typing.type_check_only
class Quota(typing.TypedDict, total=False):
    limits: _list[QuotaLimit]
    metricRules: _list[MetricRule]

@typing.type_check_only
class QuotaLimit(typing.TypedDict, total=False):
    defaultLimit: str
    description: str
    displayName: str
    duration: str
    freeTier: str
    maxLimit: str
    metric: str
    name: str
    trafficSource: typing.Literal[
        "TRAFFIC_SOURCE_UNSPECIFIED",
        "TRAFFIC_SOURCE_NONAGENTIC",
        "TRAFFIC_SOURCE_AGENTIC",
    ]
    unit: str
    values: dict[str, typing.Any]

@typing.type_check_only
class Range(typing.TypedDict, total=False):
    ipCidrRange: str
    network: str

@typing.type_check_only
class RangeReservation(typing.TypedDict, total=False):
    ipPrefixLength: int
    requestedRanges: _list[str]
    secondaryRangeIpPrefixLengths: _list[int]
    subnetworkCandidates: _list[Subnetwork]

@typing.type_check_only
class RemoveDnsRecordSetMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsRecordSetRequest(typing.TypedDict, total=False):
    consumerNetwork: str
    dnsRecordSet: DnsRecordSet
    zone: str

@typing.type_check_only
class RemoveDnsRecordSetResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsZoneMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsZoneRequest(typing.TypedDict, total=False):
    consumerNetwork: str
    name: str

@typing.type_check_only
class RemoveDnsZoneResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Route(typing.TypedDict, total=False):
    destRange: str
    name: str
    network: str
    nextHopGateway: str

@typing.type_check_only
class RubySettings(typing.TypedDict, total=False):
    common: CommonLanguageSettings

@typing.type_check_only
class SearchRangeRequest(typing.TypedDict, total=False):
    ipPrefixLength: int
    network: str

@typing.type_check_only
class SecondaryIpRange(typing.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

@typing.type_check_only
class SecondaryIpRangeSpec(typing.TypedDict, total=False):
    ipPrefixLength: int
    outsideAllocationPublicIpRange: str
    rangeName: str
    requestedAddress: str

@typing.type_check_only
class SelectiveGapicGeneration(typing.TypedDict, total=False):
    generateOmittedAsInternal: bool
    methods: _list[str]

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    apis: _list[Api]
    aspects: _list[Aspect]
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
    publishing: Publishing
    quota: Quota
    sourceInfo: SourceInfo
    systemParameters: SystemParameters
    systemTypes: _list[Type]
    title: str
    types: _list[Type]
    usage: Usage

@typing.type_check_only
class SourceContext(typing.TypedDict, total=False):
    fileName: str

@typing.type_check_only
class SourceInfo(typing.TypedDict, total=False):
    sourceFiles: _list[dict[str, typing.Any]]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subnetwork(typing.TypedDict, total=False):
    ipCidrRange: str
    name: str
    network: str
    outsideAllocation: bool
    region: str
    secondaryIpRanges: _list[SecondaryIpRange]

@typing.type_check_only
class SystemParameter(typing.TypedDict, total=False):
    httpHeader: str
    name: str
    urlQueryParameter: str

@typing.type_check_only
class SystemParameterRule(typing.TypedDict, total=False):
    parameters: _list[SystemParameter]
    selector: str

@typing.type_check_only
class SystemParameters(typing.TypedDict, total=False):
    rules: _list[SystemParameterRule]

@typing.type_check_only
class Type(typing.TypedDict, total=False):
    edition: str
    fields: _list[Field]
    name: str
    oneofs: _list[str]
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"]

@typing.type_check_only
class UpdateConsumerConfigRequest(typing.TypedDict, total=False):
    consumerConfig: ConsumerConfig

@typing.type_check_only
class UpdateDnsRecordSetMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateDnsRecordSetRequest(typing.TypedDict, total=False):
    consumerNetwork: str
    existingDnsRecordSet: DnsRecordSet
    newDnsRecordSet: DnsRecordSet
    zone: str

@typing.type_check_only
class Usage(typing.TypedDict, total=False):
    producerNotificationChannel: str
    requirements: _list[str]
    rules: _list[UsageRule]

@typing.type_check_only
class UsageRule(typing.TypedDict, total=False):
    allowUnregisteredCalls: bool
    selector: str
    skipServiceControl: bool

@typing.type_check_only
class ValidateConsumerConfigRequest(typing.TypedDict, total=False):
    checkServiceNetworkingUsePermission: bool
    consumerNetwork: str
    consumerProject: ConsumerProject
    rangeReservation: RangeReservation
    validateNetwork: bool

@typing.type_check_only
class ValidateConsumerConfigResponse(typing.TypedDict, total=False):
    existingSubnetworkCandidates: _list[Subnetwork]
    isValid: bool
    validationError: typing.Literal[
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
        "USE_PERMISSION_NOT_FOUND",
        "SN_SERVICE_AGENT_PERMISSION_DENIED_ON_CONSUMER_PROJECT",
    ]

@typing.type_check_only
class VpcServiceControls(typing.TypedDict, total=False):
    enabled: bool
