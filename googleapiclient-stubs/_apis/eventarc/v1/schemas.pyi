import typing

_list = list

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Channel(typing.TypedDict, total=False):
    activationToken: str
    createTime: str
    cryptoKeyName: str
    labels: dict[str, typing.Any]
    name: str
    provider: str
    pubsubTopic: str
    satisfiesPzs: bool
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "INACTIVE"]
    uid: str
    updateTime: str

@typing.type_check_only
class ChannelConnection(typing.TypedDict, total=False):
    activationToken: str
    channel: str
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class CloudRun(typing.TypedDict, total=False):
    path: str
    region: str
    service: str

@typing.type_check_only
class Destination(typing.TypedDict, total=False):
    cloudFunction: str
    cloudRun: CloudRun
    gke: GKE
    httpEndpoint: HttpEndpoint
    networkConfig: NetworkConfig
    workflow: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Enrollment(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    celMatch: str
    createTime: str
    destination: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    messageBus: str
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class EventFilter(typing.TypedDict, total=False):
    attribute: str
    operator: str
    value: str

@typing.type_check_only
class EventType(typing.TypedDict, total=False):
    description: str
    eventSchemaUri: str
    filteringAttributes: _list[FilteringAttribute]
    type: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FilteringAttribute(typing.TypedDict, total=False):
    attribute: str
    description: str
    pathPatternSupported: bool
    required: bool

@typing.type_check_only
class GKE(typing.TypedDict, total=False):
    cluster: str
    location: str
    namespace: str
    path: str
    service: str

@typing.type_check_only
class GoogleApiSource(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    cryptoKeyName: str
    destination: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    loggingConfig: LoggingConfig
    name: str
    organizationSubscription: OrganizationSubscription
    projectSubscriptions: ProjectSubscriptions
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleChannelConfig(typing.TypedDict, total=False):
    cryptoKeyName: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineDestination(typing.TypedDict, total=False):
    authenticationConfig: GoogleCloudEventarcV1PipelineDestinationAuthenticationConfig
    httpEndpoint: GoogleCloudEventarcV1PipelineDestinationHttpEndpoint
    messageBus: str
    networkConfig: GoogleCloudEventarcV1PipelineDestinationNetworkConfig
    outputPayloadFormat: GoogleCloudEventarcV1PipelineMessagePayloadFormat
    topic: str
    workflow: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineDestinationAuthenticationConfig(
    typing.TypedDict, total=False
):
    googleOidc: GoogleCloudEventarcV1PipelineDestinationAuthenticationConfigOidcToken
    oauthToken: GoogleCloudEventarcV1PipelineDestinationAuthenticationConfigOAuthToken

@typing.type_check_only
class GoogleCloudEventarcV1PipelineDestinationAuthenticationConfigOAuthToken(
    typing.TypedDict, total=False
):
    scope: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineDestinationAuthenticationConfigOidcToken(
    typing.TypedDict, total=False
):
    audience: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineDestinationHttpEndpoint(
    typing.TypedDict, total=False
):
    messageBindingTemplate: str
    uri: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineDestinationNetworkConfig(
    typing.TypedDict, total=False
):
    networkAttachment: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineMediation(typing.TypedDict, total=False):
    transformation: GoogleCloudEventarcV1PipelineMediationTransformation

@typing.type_check_only
class GoogleCloudEventarcV1PipelineMediationTransformation(
    typing.TypedDict, total=False
):
    transformationTemplate: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineMessagePayloadFormat(typing.TypedDict, total=False):
    avro: GoogleCloudEventarcV1PipelineMessagePayloadFormatAvroFormat
    json: GoogleCloudEventarcV1PipelineMessagePayloadFormatJsonFormat
    protobuf: GoogleCloudEventarcV1PipelineMessagePayloadFormatProtobufFormat

@typing.type_check_only
class GoogleCloudEventarcV1PipelineMessagePayloadFormatAvroFormat(
    typing.TypedDict, total=False
):
    schemaDefinition: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineMessagePayloadFormatJsonFormat(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudEventarcV1PipelineMessagePayloadFormatProtobufFormat(
    typing.TypedDict, total=False
):
    schemaDefinition: str

@typing.type_check_only
class GoogleCloudEventarcV1PipelineRetryPolicy(typing.TypedDict, total=False):
    maxAttempts: int
    maxRetryDelay: str
    minRetryDelay: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class HttpEndpoint(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class ListChannelConnectionsResponse(typing.TypedDict, total=False):
    channelConnections: _list[ChannelConnection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListChannelsResponse(typing.TypedDict, total=False):
    channels: _list[Channel]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEnrollmentsResponse(typing.TypedDict, total=False):
    enrollments: _list[Enrollment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGoogleApiSourcesResponse(typing.TypedDict, total=False):
    googleApiSources: _list[GoogleApiSource]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMessageBusEnrollmentsResponse(typing.TypedDict, total=False):
    enrollments: _list[str]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMessageBusesResponse(typing.TypedDict, total=False):
    messageBuses: _list[MessageBus]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListPipelinesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pipelines: _list[Pipeline]
    unreachable: _list[str]

@typing.type_check_only
class ListProvidersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    providers: _list[Provider]
    unreachable: _list[str]

@typing.type_check_only
class ListTriggersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    triggers: _list[Trigger]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LoggingConfig(typing.TypedDict, total=False):
    logSeverity: typing.Literal[
        "LOG_SEVERITY_UNSPECIFIED",
        "NONE",
        "DEBUG",
        "INFO",
        "NOTICE",
        "WARNING",
        "ERROR",
        "CRITICAL",
        "ALERT",
        "EMERGENCY",
    ]

@typing.type_check_only
class MessageBus(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    cryptoKeyName: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    loggingConfig: LoggingConfig
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    networkAttachment: str

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class OrganizationSubscription(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Pipeline(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    cryptoKeyName: str
    destinations: _list[GoogleCloudEventarcV1PipelineDestination]
    displayName: str
    etag: str
    inputPayloadFormat: GoogleCloudEventarcV1PipelineMessagePayloadFormat
    labels: dict[str, typing.Any]
    loggingConfig: LoggingConfig
    mediations: _list[GoogleCloudEventarcV1PipelineMediation]
    name: str
    retryPolicy: GoogleCloudEventarcV1PipelineRetryPolicy
    satisfiesPzs: bool
    uid: str
    updateTime: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectSubscriptions(typing.TypedDict, total=False):
    list: _list[str]

@typing.type_check_only
class Provider(typing.TypedDict, total=False):
    displayName: str
    eventTypes: _list[EventType]
    name: str

@typing.type_check_only
class Pubsub(typing.TypedDict, total=False):
    subscription: str
    topic: str

@typing.type_check_only
class RetryPolicy(typing.TypedDict, total=False):
    maxAttempts: int

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class StateCondition(typing.TypedDict, total=False):
    code: typing.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Transport(typing.TypedDict, total=False):
    pubsub: Pubsub

@typing.type_check_only
class Trigger(typing.TypedDict, total=False):
    channel: str
    conditions: dict[str, typing.Any]
    createTime: str
    destination: Destination
    etag: str
    eventDataContentType: str
    eventFilters: _list[EventFilter]
    labels: dict[str, typing.Any]
    name: str
    retryPolicy: RetryPolicy
    satisfiesPzs: bool
    serviceAccount: str
    transport: Transport
    uid: str
    updateTime: str
