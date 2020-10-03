import typing

import typing_extensions

class AllocateInfo(typing_extensions.TypedDict, total=False):
    unusedArguments: typing.List[str]

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
    subject: str
    detail: str
    status: Status

class CheckRequest(typing_extensions.TypedDict, total=False):
    skipActivationCheck: bool
    requestProjectSettings: bool
    operation: Operation
    serviceConfigId: str

class AllocateQuotaResponse(typing_extensions.TypedDict, total=False):
    serviceConfigId: str
    allocateInfo: AllocateInfo
    allocateErrors: typing.List[QuotaError]
    operationId: str
    quotaMetrics: typing.List[MetricValueSet]

class LogEntrySourceLocation(typing_extensions.TypedDict, total=False):
    function: str
    line: str
    file: str

class CheckInfo(typing_extensions.TypedDict, total=False):
    consumerInfo: ConsumerInfo
    unusedArguments: typing.List[str]

class AllocateQuotaRequest(typing_extensions.TypedDict, total=False):
    serviceConfigId: str
    allocateOperation: QuotaOperation

class Peer(typing_extensions.TypedDict, total=False):
    ip: str
    regionCode: str
    principal: str
    labels: typing.Dict[str, typing.Any]
    port: str

class MetricValue(typing_extensions.TypedDict, total=False):
    startTime: str
    moneyValue: Money
    stringValue: str
    labels: typing.Dict[str, typing.Any]
    int64Value: str
    boolValue: bool
    endTime: str
    distributionValue: Distribution
    doubleValue: float

class Attributes(typing_extensions.TypedDict, total=False):
    droppedAttributesCount: int
    attributeMap: typing.Dict[str, typing.Any]

class AuditLog(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    methodName: str
    serviceData: typing.Dict[str, typing.Any]
    status: Status
    metadata: typing.Dict[str, typing.Any]
    requestMetadata: RequestMetadata
    resourceLocation: ResourceLocation
    serviceName: str
    request: typing.Dict[str, typing.Any]
    authenticationInfo: AuthenticationInfo
    numResponseItems: str
    authorizationInfo: typing.List[AuthorizationInfo]
    resourceName: str
    resourceOriginalState: typing.Dict[str, typing.Any]

class TruncatableString(typing_extensions.TypedDict, total=False):
    value: str
    truncatedByteCount: int

class ThirdPartyPrincipal(typing_extensions.TypedDict, total=False):
    thirdPartyClaims: typing.Dict[str, typing.Any]

class ReportInfo(typing_extensions.TypedDict, total=False):
    quotaInfo: QuotaInfo
    operationId: str

class RequestMetadata(typing_extensions.TypedDict, total=False):
    callerNetwork: str
    callerIp: str
    requestAttributes: Request
    callerSuppliedUserAgent: str
    destinationAttributes: Peer

class HttpRequest(typing_extensions.TypedDict, total=False):
    protocol: str
    latency: str
    serverIp: str
    cacheHit: bool
    cacheFillBytes: str
    responseSize: str
    remoteIp: str
    requestMethod: str
    cacheValidatedWithOriginServer: bool
    cacheLookup: bool
    requestUrl: str
    status: int
    referer: str
    requestSize: str
    userAgent: str

class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

class AuthorizationInfo(typing_extensions.TypedDict, total=False):
    permission: str
    granted: bool
    resourceAttributes: Resource
    resource: str

class ReportResponse(typing_extensions.TypedDict, total=False):
    serviceRolloutId: str
    reportInfos: typing.List[ReportInfo]
    reportErrors: typing.List[ReportError]
    serviceConfigId: str

class MetricValueSet(typing_extensions.TypedDict, total=False):
    metricValues: typing.List[MetricValue]
    metricName: str

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
    subject: str

class ReportError(typing_extensions.TypedDict, total=False):
    operationId: str
    status: Status

class Operation(typing_extensions.TypedDict, total=False):
    importance: typing_extensions.Literal["LOW", "HIGH", "DEBUG"]
    operationId: str
    userLabels: typing.Dict[str, typing.Any]
    consumerId: str
    logEntries: typing.List[LogEntry]
    extensions: typing.List[typing.Dict[str, typing.Any]]
    startTime: str
    operationName: str
    metricValueSets: typing.List[MetricValueSet]
    resources: typing.List[ResourceInfo]
    traceSpans: typing.List[TraceSpan]
    quotaProperties: QuotaProperties
    endTime: str
    labels: typing.Dict[str, typing.Any]

class ServiceAccountDelegationInfo(typing_extensions.TypedDict, total=False):
    firstPartyPrincipal: FirstPartyPrincipal
    thirdPartyPrincipal: ThirdPartyPrincipal

class CheckResponse(typing_extensions.TypedDict, total=False):
    serviceRolloutId: str
    serviceConfigId: str
    checkErrors: typing.List[CheckError]
    quotaInfo: QuotaInfo
    checkInfo: CheckInfo
    operationId: str

class ReportRequest(typing_extensions.TypedDict, total=False):
    serviceConfigId: str
    operations: typing.List[Operation]

class LogEntryOperation(typing_extensions.TypedDict, total=False):
    last: bool
    first: bool
    producer: str
    id: str

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

class ResourceInfo(typing_extensions.TypedDict, total=False):
    resourceContainer: str
    resourceName: str
    resourceLocation: str

class TraceSpan(typing_extensions.TypedDict, total=False):
    parentSpanId: str
    status: Status
    endTime: str
    childSpanCount: int
    name: str
    attributes: Attributes
    displayName: TruncatableString
    sameProcessAsParentSpan: bool
    startTime: str
    spanKind: typing_extensions.Literal[
        "SPAN_KIND_UNSPECIFIED", "INTERNAL", "SERVER", "CLIENT", "PRODUCER", "CONSUMER"
    ]
    spanId: str

class Exemplar(typing_extensions.TypedDict, total=False):
    value: float
    attachments: typing.List[typing.Dict[str, typing.Any]]
    timestamp: str

class QuotaInfo(typing_extensions.TypedDict, total=False):
    quotaConsumed: typing.Dict[str, typing.Any]
    quotaMetrics: typing.List[MetricValueSet]
    limitExceeded: typing.List[str]

class Money(typing_extensions.TypedDict, total=False):
    nanos: int
    currencyCode: str
    units: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class LinearBuckets(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    width: float
    offset: float

class LogEntry(typing_extensions.TypedDict, total=False):
    textPayload: str
    name: str
    structPayload: typing.Dict[str, typing.Any]
    insertId: str
    timestamp: str
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
    trace: str
    operation: LogEntryOperation
    protoPayload: typing.Dict[str, typing.Any]
    httpRequest: HttpRequest
    sourceLocation: LogEntrySourceLocation
    labels: typing.Dict[str, typing.Any]

class Request(typing_extensions.TypedDict, total=False):
    host: str
    scheme: str
    time: str
    protocol: str
    auth: Auth
    headers: typing.Dict[str, typing.Any]
    id: str
    reason: str
    method: str
    size: str
    query: str
    path: str

class AuthenticationInfo(typing_extensions.TypedDict, total=False):
    authoritySelector: str
    principalSubject: str
    principalEmail: str
    thirdPartyPrincipal: typing.Dict[str, typing.Any]
    serviceAccountDelegationInfo: typing.List[ServiceAccountDelegationInfo]
    serviceAccountKeyName: str

class Resource(typing_extensions.TypedDict, total=False):
    service: str
    type: str
    labels: typing.Dict[str, typing.Any]
    name: str

class QuotaProperties(typing_extensions.TypedDict, total=False):
    quotaMode: typing_extensions.Literal[
        "ACQUIRE", "ACQUIRE_BEST_EFFORT", "CHECK", "RELEASE"
    ]

class ResourceLocation(typing_extensions.TypedDict, total=False):
    currentLocations: typing.List[str]
    originalLocations: typing.List[str]

class Distribution(typing_extensions.TypedDict, total=False):
    explicitBuckets: ExplicitBuckets
    sumOfSquaredDeviation: float
    exemplars: typing.List[Exemplar]
    count: str
    linearBuckets: LinearBuckets
    maximum: float
    exponentialBuckets: ExponentialBuckets
    minimum: float
    mean: float
    bucketCounts: typing.List[str]

class QuotaOperation(typing_extensions.TypedDict, total=False):
    operationId: str
    consumerId: str
    methodName: str
    quotaMode: typing_extensions.Literal[
        "UNSPECIFIED",
        "NORMAL",
        "BEST_EFFORT",
        "CHECK_ONLY",
        "QUERY_ONLY",
        "ADJUST_ONLY",
    ]
    labels: typing.Dict[str, typing.Any]
    quotaMetrics: typing.List[MetricValueSet]

class Auth(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[str]
    principal: str
    presenter: str
    audiences: typing.List[str]
    claims: typing.Dict[str, typing.Any]

class AttributeValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    stringValue: TruncatableString
    intValue: str

class ExplicitBuckets(typing_extensions.TypedDict, total=False):
    bounds: typing.List[float]

class FirstPartyPrincipal(typing_extensions.TypedDict, total=False):
    serviceMetadata: typing.Dict[str, typing.Any]
    principalEmail: str

class ExponentialBuckets(typing_extensions.TypedDict, total=False):
    scale: float
    growthFactor: float
    numFiniteBuckets: int
