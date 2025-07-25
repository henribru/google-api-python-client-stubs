import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddDnsZoneResponse(typing_extensions.TypedDict, total=False):
    consumerPeeringZone: DnsZone
    producerPrivateZone: DnsZone

@typing.type_check_only
class AddRolesMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddRolesResponse(typing_extensions.TypedDict, total=False):
    policyBinding: _list[PolicyBinding]

@typing.type_check_only
class AddSubnetworkRequest(typing_extensions.TypedDict, total=False):
    consumer: str
    consumerNetwork: str
    description: str
    ipPrefixLength: int
    region: str
    requestedAddress: str
    subnetwork: str
    subnetworkUsers: _list[str]

@typing.type_check_only
class Api(typing_extensions.TypedDict, total=False):
    methods: _list[Method]
    mixins: _list[Mixin]
    name: str
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal[
        "SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"
    ]
    version: str

@typing.type_check_only
class Aspect(typing_extensions.TypedDict, total=False):
    kind: str
    spec: dict[str, typing.Any]

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
    loadBalancingPolicy: str
    minDeadline: float
    operationDeadline: float
    overridesByRequestProtocol: dict[str, typing.Any]
    pathTranslation: typing_extensions.Literal[
        "PATH_TRANSLATION_UNSPECIFIED", "CONSTANT_ADDRESS", "APPEND_PATH_TO_ADDRESS"
    ]
    protocol: str
    selector: str

@typing.type_check_only
class BatchingConfigProto(typing_extensions.TypedDict, total=False):
    batchDescriptor: BatchingDescriptorProto
    thresholds: BatchingSettingsProto

@typing.type_check_only
class BatchingDescriptorProto(typing_extensions.TypedDict, total=False):
    batchedField: str
    discriminatorFields: _list[str]
    subresponseField: str

@typing.type_check_only
class BatchingSettingsProto(typing_extensions.TypedDict, total=False):
    delayThreshold: str
    elementCountLimit: int
    elementCountThreshold: int
    flowControlByteLimit: int
    flowControlElementLimit: int
    flowControlLimitExceededBehavior: typing_extensions.Literal[
        "UNSET_BEHAVIOR", "THROW_EXCEPTION", "BLOCK", "IGNORE"
    ]
    requestByteLimit: int
    requestByteThreshold: str

@typing.type_check_only
class Billing(typing_extensions.TypedDict, total=False):
    consumerDestinations: _list[BillingDestination]

@typing.type_check_only
class BillingDestination(typing_extensions.TypedDict, total=False):
    metrics: _list[str]
    monitoredResource: str

@typing.type_check_only
class CleanupConnectionMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ClientLibrarySettings(typing_extensions.TypedDict, total=False):
    cppSettings: CppSettings
    dotnetSettings: DotnetSettings
    goSettings: GoSettings
    javaSettings: JavaSettings
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
    nodeSettings: NodeSettings
    phpSettings: PhpSettings
    pythonSettings: PythonSettings
    restNumericEnums: bool
    rubySettings: RubySettings
    version: str

@typing.type_check_only
class CloudSQLConfig(typing_extensions.TypedDict, total=False):
    service: str
    umbrellaNetwork: str
    umbrellaProject: str

@typing.type_check_only
class CommonLanguageSettings(typing_extensions.TypedDict, total=False):
    destinations: _list[
        typing_extensions.Literal[
            "CLIENT_LIBRARY_DESTINATION_UNSPECIFIED", "GITHUB", "PACKAGE_MANAGER"
        ]
    ]
    referenceDocsUri: str
    selectiveGapicGeneration: SelectiveGapicGeneration

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    network: str
    peering: str
    reservedPeeringRanges: _list[str]
    service: str

@typing.type_check_only
class ConsumerConfig(typing_extensions.TypedDict, total=False):
    cloudsqlConfigs: _list[CloudSQLConfig]
    consumerExportCustomRoutes: bool
    consumerExportSubnetRoutesWithPublicIp: bool
    consumerImportCustomRoutes: bool
    consumerImportSubnetRoutesWithPublicIp: bool
    producerExportCustomRoutes: bool
    producerExportSubnetRoutesWithPublicIp: bool
    producerImportCustomRoutes: bool
    producerImportSubnetRoutesWithPublicIp: bool
    producerNetwork: str
    reservedRanges: _list[GoogleCloudServicenetworkingV1ConsumerConfigReservedRange]
    usedIpRanges: _list[str]
    vpcScReferenceArchitectureEnabled: bool

@typing.type_check_only
class ConsumerConfigMetadata(typing_extensions.TypedDict, total=False): ...

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
    methodPolicies: _list[MethodPolicy]

@typing.type_check_only
class CppSettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings

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
class DeleteConnectionMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeletePeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DnsRecordSet(typing_extensions.TypedDict, total=False):
    data: _list[str]
    domain: str
    ttl: str
    type: str

@typing.type_check_only
class DnsZone(typing_extensions.TypedDict, total=False):
    dnsSuffix: str
    name: str

@typing.type_check_only
class Documentation(typing_extensions.TypedDict, total=False):
    additionalIamInfo: str
    documentationRootUrl: str
    overview: str
    pages: _list[Page]
    rules: _list[DocumentationRule]
    sectionOverrides: _list[Page]
    serviceRootUrl: str
    summary: str

@typing.type_check_only
class DocumentationRule(typing_extensions.TypedDict, total=False):
    deprecationDescription: str
    description: str
    disableReplacementWords: str
    selector: str

@typing.type_check_only
class DotnetSettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings
    forcedNamespaceAliases: _list[str]
    handwrittenSignatures: _list[str]
    ignoredResources: _list[str]
    renamedResources: dict[str, typing.Any]
    renamedServices: dict[str, typing.Any]

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    aliases: _list[str]
    allowCors: bool
    name: str
    target: str

@typing.type_check_only
class Enum(typing_extensions.TypedDict, total=False):
    edition: str
    enumvalue: _list[EnumValue]
    name: str
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal[
        "SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"
    ]

@typing.type_check_only
class EnumValue(typing_extensions.TypedDict, total=False):
    name: str
    number: int
    options: _list[Option]

@typing.type_check_only
class ExperimentalFeatures(typing_extensions.TypedDict, total=False):
    protobufPythonicTypesEnabled: bool
    restAsyncIoEnabled: bool
    unversionedPackageDisabled: bool

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
class FieldPolicy(typing_extensions.TypedDict, total=False):
    resourcePermission: str
    resourceType: str
    selector: str

@typing.type_check_only
class GoSettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings
    renamedServices: dict[str, typing.Any]

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
    reservedPeeringRanges: _list[str]
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
    rules: _list[HttpRule]

@typing.type_check_only
class HttpRule(typing_extensions.TypedDict, total=False):
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
class JavaSettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings
    libraryPackage: str
    serviceClassNames: dict[str, typing.Any]

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
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: _list[GoogleCloudServicenetworkingV1betaConnection]

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
class LongRunning(typing_extensions.TypedDict, total=False):
    initialPollDelay: str
    maxPollDelay: str
    pollDelayMultiplier: float
    totalPollTimeout: str

@typing.type_check_only
class Method(typing_extensions.TypedDict, total=False):
    name: str
    options: _list[Option]
    requestStreaming: bool
    requestTypeUrl: str
    responseStreaming: bool
    responseTypeUrl: str
    syntax: typing_extensions.Literal[
        "SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"
    ]

@typing.type_check_only
class MethodPolicy(typing_extensions.TypedDict, total=False):
    requestPolicies: _list[FieldPolicy]
    selector: str

@typing.type_check_only
class MethodSettings(typing_extensions.TypedDict, total=False):
    autoPopulatedFields: _list[str]
    batching: BatchingConfigProto
    longRunning: LongRunning
    selector: str

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
    timeSeriesResourceHierarchyLevel: _list[
        typing_extensions.Literal[
            "TIME_SERIES_RESOURCE_HIERARCHY_LEVEL_UNSPECIFIED",
            "PROJECT",
            "ORGANIZATION",
            "FOLDER",
        ]
    ]

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
class NodeSettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings

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
class Page(typing_extensions.TypedDict, total=False):
    content: str
    name: str
    subpages: _list[Page]

@typing.type_check_only
class PartialDeleteConnectionMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PeeredDnsDomain(typing_extensions.TypedDict, total=False):
    dnsSuffix: str
    name: str

@typing.type_check_only
class PeeredDnsDomainMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PhpSettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings
    libraryPackage: str

@typing.type_check_only
class PolicyBinding(typing_extensions.TypedDict, total=False):
    member: str
    role: str

@typing.type_check_only
class Publishing(typing_extensions.TypedDict, total=False):
    apiShortName: str
    codeownerGithubTeams: _list[str]
    docTagPrefix: str
    documentationUri: str
    githubLabel: str
    librarySettings: _list[ClientLibrarySettings]
    methodSettings: _list[MethodSettings]
    newIssueUri: str
    organization: typing_extensions.Literal[
        "CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED",
        "CLOUD",
        "ADS",
        "PHOTOS",
        "STREET_VIEW",
        "SHOPPING",
        "GEO",
        "GENERATIVE_AI",
    ]
    protoReferenceDocumentationUri: str
    restReferenceDocumentationUri: str

@typing.type_check_only
class PythonSettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings
    experimentalFeatures: ExperimentalFeatures

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
class Range(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    network: str

@typing.type_check_only
class RemoveDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsRecordSetResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsZoneMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveDnsZoneResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    destRange: str
    name: str
    network: str
    nextHopGateway: str

@typing.type_check_only
class RubySettings(typing_extensions.TypedDict, total=False):
    common: CommonLanguageSettings

@typing.type_check_only
class SearchRangeRequest(typing_extensions.TypedDict, total=False):
    ipPrefixLength: int
    network: str

@typing.type_check_only
class SecondaryIpRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

@typing.type_check_only
class SelectiveGapicGeneration(typing_extensions.TypedDict, total=False):
    generateOmittedAsInternal: bool
    methods: _list[str]

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
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
class Subnetwork(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    name: str
    network: str
    outsideAllocation: bool
    region: str
    secondaryIpRanges: _list[SecondaryIpRange]

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
    edition: str
    fields: _list[Field]
    name: str
    oneofs: _list[str]
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal[
        "SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"
    ]

@typing.type_check_only
class UpdateDnsRecordSetMetadata(typing_extensions.TypedDict, total=False): ...

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
class VpcServiceControls(typing_extensions.TypedDict, total=False):
    enabled: bool
