import typing

import typing_extensions
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
class BillingView(typing_extensions.TypedDict, total=False):
    reportRequests: typing.List[ReportRequest]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

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
class Empty(typing_extensions.TypedDict, total=False): ...

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
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

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
class Hub(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: typing.Dict[str, typing.Any]
    name: str
    spokes: typing.List[str]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]
    uniqueId: str
    updateTime: str

@typing.type_check_only
class LinearBuckets(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class ListHubsResponse(typing_extensions.TypedDict, total=False):
    hubs: typing.List[Hub]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListSpokesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    spokes: typing.List[Spoke]
    unreachable: typing.List[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

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
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class QuotaProperties(typing_extensions.TypedDict, total=False):
    quotaMode: typing_extensions.Literal[
        "ACQUIRE", "ACQUIRE_BEST_EFFORT", "CHECK", "RELEASE"
    ]

@typing.type_check_only
class ReportRequest(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    serviceConfigId: str
    serviceName: str

@typing.type_check_only
class ResourceInfo(typing_extensions.TypedDict, total=False):
    resourceContainer: str
    resourceLocation: str
    resourceName: str

@typing.type_check_only
class RouterApplianceInstance(typing_extensions.TypedDict, total=False):
    ipAddress: str
    networkInterface: str
    virtualMachine: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Spoke(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    hub: str
    labels: typing.Dict[str, typing.Any]
    linkedInterconnectAttachments: typing.List[str]
    linkedRouterApplianceInstances: typing.List[RouterApplianceInstance]
    linkedVpnTunnels: typing.List[str]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]
    uniqueId: str
    updateTime: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

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
    status: GoogleRpcStatus

@typing.type_check_only
class TruncatableString(typing_extensions.TypedDict, total=False):
    truncatedByteCount: int
    value: str
