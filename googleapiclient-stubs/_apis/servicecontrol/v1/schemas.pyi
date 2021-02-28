import typing

import typing_extensions
@typing.type_check_only
class AllocateInfo(typing_extensions.TypedDict, total=False):
    unusedArguments: typing.List[str]

@typing.type_check_only
class AllocateQuotaRequest(typing_extensions.TypedDict, total=False):
    allocateOperation: QuotaOperation
    serviceConfigId: str

@typing.type_check_only
class AllocateQuotaResponse(typing_extensions.TypedDict, total=False):
    allocateErrors: typing.List[QuotaError]
    allocateInfo: AllocateInfo
    operationId: str
    quotaMetrics: typing.List[MetricValueSet]
    serviceConfigId: str

@typing.type_check_only
class AttributeValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    stringValue: TruncatableString

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    attributeMap: typing.Dict[str, typing.Any]
    droppedAttributesCount: int

@typing.type_check_only
class AuditLog(typing_extensions.TypedDict, total=False):
    authenticationInfo: AuthenticationInfo
    authorizationInfo: typing.List[AuthorizationInfo]
    metadata: typing.Dict[str, typing.Any]
    methodName: str
    numResponseItems: str
    request: typing.Dict[str, typing.Any]
    requestMetadata: RequestMetadata
    resourceLocation: ResourceLocation
    resourceName: str
    resourceOriginalState: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    serviceData: typing.Dict[str, typing.Any]
    serviceName: str
    status: Status

@typing.type_check_only
class Auth(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[str]
    audiences: typing.List[str]
    claims: typing.Dict[str, typing.Any]
    presenter: str
    principal: str

@typing.type_check_only
class AuthenticationInfo(typing_extensions.TypedDict, total=False):
    authoritySelector: str
    principalEmail: str
    principalSubject: str
    serviceAccountDelegationInfo: typing.List[ServiceAccountDelegationInfo]
    serviceAccountKeyName: str
    thirdPartyPrincipal: typing.Dict[str, typing.Any]

@typing.type_check_only
class AuthorizationInfo(typing_extensions.TypedDict, total=False):
    granted: bool
    permission: str
    resource: str
    resourceAttributes: Resource

@typing.type_check_only
class CheckError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "NOT_FOUND",
        "PERMISSION_DENIED",
        "RESOURCE_EXHAUSTED",
        "BUDGET_EXCEEDED",
        "DENIAL_OF_SERVICE_DETECTED",
        "LOAD_SHEDDING",
        "ABUSER_DETECTED",
        "SERVICE_NOT_ACTIVATED",
        "VISIBILITY_DENIED",
        "BILLING_DISABLED",
        "PROJECT_DELETED",
        "PROJECT_INVALID",
        "CONSUMER_INVALID",
        "IP_ADDRESS_BLOCKED",
        "REFERER_BLOCKED",
        "CLIENT_APP_BLOCKED",
        "API_TARGET_BLOCKED",
        "API_KEY_INVALID",
        "API_KEY_EXPIRED",
        "API_KEY_NOT_FOUND",
        "SPATULA_HEADER_INVALID",
        "LOAS_ROLE_INVALID",
        "NO_LOAS_PROJECT",
        "LOAS_PROJECT_DISABLED",
        "SECURITY_POLICY_VIOLATED",
        "INVALID_CREDENTIAL",
        "LOCATION_POLICY_VIOLATED",
        "NAMESPACE_LOOKUP_UNAVAILABLE",
        "SERVICE_STATUS_UNAVAILABLE",
        "BILLING_STATUS_UNAVAILABLE",
        "QUOTA_CHECK_UNAVAILABLE",
        "LOAS_PROJECT_LOOKUP_UNAVAILABLE",
        "CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE",
        "SECURITY_POLICY_BACKEND_UNAVAILABLE",
        "LOCATION_POLICY_BACKEND_UNAVAILABLE",
    ]
    detail: str
    status: Status
    subject: str

@typing.type_check_only
class CheckInfo(typing_extensions.TypedDict, total=False):
    consumerInfo: ConsumerInfo
    unusedArguments: typing.List[str]

@typing.type_check_only
class CheckRequest(typing_extensions.TypedDict, total=False):
    operation: Operation
    requestProjectSettings: bool
    serviceConfigId: str
    skipActivationCheck: bool

@typing.type_check_only
class CheckResponse(typing_extensions.TypedDict, total=False):
    checkErrors: typing.List[CheckError]
    checkInfo: CheckInfo
    operationId: str
    quotaInfo: QuotaInfo
    serviceConfigId: str
    serviceRolloutId: str

@typing.type_check_only
class ConsumerInfo(typing_extensions.TypedDict, total=False):
    consumerNumber: str
    projectNumber: str
    type: typing_extensions.Literal[
        "CONSUMER_TYPE_UNSPECIFIED",
        "PROJECT",
        "FOLDER",
        "ORGANIZATION",
        "SERVICE_SPECIFIC",
    ]

@typing.type_check_only
class Distribution(typing_extensions.TypedDict, total=False):
    bucketCounts: typing.List[str]
    count: str
    exemplars: typing.List[Exemplar]
    explicitBuckets: ExplicitBuckets
    exponentialBuckets: ExponentialBuckets
    linearBuckets: LinearBuckets
    maximum: float
    mean: float
    minimum: float
    sumOfSquaredDeviation: float

@typing.type_check_only
class Exemplar(typing_extensions.TypedDict, total=False):
    attachments: typing.List[typing.Dict[str, typing.Any]]
    timestamp: str
    value: float

@typing.type_check_only
class ExplicitBuckets(typing_extensions.TypedDict, total=False):
    bounds: typing.List[float]

@typing.type_check_only
class ExponentialBuckets(typing_extensions.TypedDict, total=False):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

@typing.type_check_only
class FirstPartyPrincipal(typing_extensions.TypedDict, total=False):
    principalEmail: str
    serviceMetadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class HttpRequest(typing_extensions.TypedDict, total=False):
    cacheFillBytes: str
    cacheHit: bool
    cacheLookup: bool
    cacheValidatedWithOriginServer: bool
    latency: str
    protocol: str
    referer: str
    remoteIp: str
    requestMethod: str
    requestSize: str
    requestUrl: str
    responseSize: str
    serverIp: str
    status: int
    userAgent: str

@typing.type_check_only
class LinearBuckets(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class LogEntry(typing_extensions.TypedDict, total=False):
    httpRequest: HttpRequest
    insertId: str
    labels: typing.Dict[str, typing.Any]
    name: str
    operation: LogEntryOperation
    protoPayload: typing.Dict[str, typing.Any]
    severity: typing_extensions.Literal[
        "DEFAULT",
        "DEBUG",
        "INFO",
        "NOTICE",
        "WARNING",
        "ERROR",
        "CRITICAL",
        "ALERT",
        "EMERGENCY",
    ]
    sourceLocation: LogEntrySourceLocation
    structPayload: typing.Dict[str, typing.Any]
    textPayload: str
    timestamp: str
    trace: str

@typing.type_check_only
class LogEntryOperation(typing_extensions.TypedDict, total=False):
    first: bool
    id: str
    last: bool
    producer: str

@typing.type_check_only
class LogEntrySourceLocation(typing_extensions.TypedDict, total=False):
    file: str
    function: str
    line: str

@typing.type_check_only
class MetricValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    distributionValue: Distribution
    doubleValue: float
    endTime: str
    int64Value: str
    labels: typing.Dict[str, typing.Any]
    moneyValue: Money
    startTime: str
    stringValue: str

@typing.type_check_only
class MetricValueSet(typing_extensions.TypedDict, total=False):
    metricName: str
    metricValues: typing.List[MetricValue]

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    consumerId: str
    endTime: str
    extensions: typing.List[typing.Dict[str, typing.Any]]
    importance: typing_extensions.Literal["LOW", "HIGH", "DEBUG"]
    labels: typing.Dict[str, typing.Any]
    logEntries: typing.List[LogEntry]
    metricValueSets: typing.List[MetricValueSet]
    operationId: str
    operationName: str
    quotaProperties: QuotaProperties
    resources: typing.List[ResourceInfo]
    startTime: str
    traceSpans: typing.List[TraceSpan]
    userLabels: typing.Dict[str, typing.Any]

@typing.type_check_only
class Peer(typing_extensions.TypedDict, total=False):
    ip: str
    labels: typing.Dict[str, typing.Any]
    port: str
    principal: str
    regionCode: str

@typing.type_check_only
class QuotaError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "UNSPECIFIED",
        "RESOURCE_EXHAUSTED",
        "OUT_OF_RANGE",
        "BILLING_NOT_ACTIVE",
        "PROJECT_DELETED",
        "API_KEY_INVALID",
        "API_KEY_EXPIRED",
        "SPATULA_HEADER_INVALID",
        "LOAS_ROLE_INVALID",
        "NO_LOAS_PROJECT",
        "PROJECT_STATUS_UNAVAILABLE",
        "SERVICE_STATUS_UNAVAILABLE",
        "BILLING_STATUS_UNAVAILABLE",
        "QUOTA_SYSTEM_UNAVAILABLE",
    ]
    description: str
    status: Status
    subject: str

@typing.type_check_only
class QuotaInfo(typing_extensions.TypedDict, total=False):
    limitExceeded: typing.List[str]
    quotaConsumed: typing.Dict[str, typing.Any]
    quotaMetrics: typing.List[MetricValueSet]

@typing.type_check_only
class QuotaOperation(typing_extensions.TypedDict, total=False):
    consumerId: str
    labels: typing.Dict[str, typing.Any]
    methodName: str
    operationId: str
    quotaMetrics: typing.List[MetricValueSet]
    quotaMode: typing_extensions.Literal[
        "UNSPECIFIED",
        "NORMAL",
        "BEST_EFFORT",
        "CHECK_ONLY",
        "QUERY_ONLY",
        "ADJUST_ONLY",
    ]

@typing.type_check_only
class QuotaProperties(typing_extensions.TypedDict, total=False):
    quotaMode: typing_extensions.Literal[
        "ACQUIRE", "ACQUIRE_BEST_EFFORT", "CHECK", "RELEASE"
    ]

@typing.type_check_only
class ReportError(typing_extensions.TypedDict, total=False):
    operationId: str
    status: Status

@typing.type_check_only
class ReportRequest(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    serviceConfigId: str

@typing.type_check_only
class ReportResponse(typing_extensions.TypedDict, total=False):
    reportErrors: typing.List[ReportError]
    serviceConfigId: str
    serviceRolloutId: str

@typing.type_check_only
class Request(typing_extensions.TypedDict, total=False):
    auth: Auth
    headers: typing.Dict[str, typing.Any]
    host: str
    id: str
    method: str
    path: str
    protocol: str
    query: str
    reason: str
    scheme: str
    size: str
    time: str

@typing.type_check_only
class RequestMetadata(typing_extensions.TypedDict, total=False):
    callerIp: str
    callerNetwork: str
    callerSuppliedUserAgent: str
    destinationAttributes: Peer
    requestAttributes: Request

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    labels: typing.Dict[str, typing.Any]
    location: str
    name: str
    service: str
    type: str
    uid: str
    updateTime: str

@typing.type_check_only
class ResourceInfo(typing_extensions.TypedDict, total=False):
    resourceContainer: str
    resourceLocation: str
    resourceName: str

@typing.type_check_only
class ResourceLocation(typing_extensions.TypedDict, total=False):
    currentLocations: typing.List[str]
    originalLocations: typing.List[str]

@typing.type_check_only
class ServiceAccountDelegationInfo(typing_extensions.TypedDict, total=False):
    firstPartyPrincipal: FirstPartyPrincipal
    principalSubject: str
    thirdPartyPrincipal: ThirdPartyPrincipal

@typing.type_check_only
class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ThirdPartyPrincipal(typing_extensions.TypedDict, total=False):
    thirdPartyClaims: typing.Dict[str, typing.Any]

@typing.type_check_only
class TraceSpan(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    childSpanCount: int
    displayName: TruncatableString
    endTime: str
    name: str
    parentSpanId: str
    sameProcessAsParentSpan: bool
    spanId: str
    spanKind: typing_extensions.Literal[
        "SPAN_KIND_UNSPECIFIED", "INTERNAL", "SERVER", "CLIENT", "PRODUCER", "CONSUMER"
    ]
    startTime: str
    status: Status

@typing.type_check_only
class TruncatableString(typing_extensions.TypedDict, total=False):
    truncatedByteCount: int
    value: str
