import typing

import typing_extensions
@typing.type_check_only
class BigQueryOptions(typing_extensions.TypedDict, total=False):
    usePartitionedTables: bool
    usesTimestampColumnPartitioning: bool

@typing.type_check_only
class BucketOptions(typing_extensions.TypedDict, total=False):
    explicitBuckets: Explicit
    exponentialBuckets: Exponential
    linearBuckets: Linear

@typing.type_check_only
class CmekSettings(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    name: str
    serviceAccountId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Explicit(typing_extensions.TypedDict, total=False):
    bounds: typing.List[float]

@typing.type_check_only
class Exponential(typing_extensions.TypedDict, total=False):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

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
class LabelDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    key: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]

@typing.type_check_only
class Linear(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class ListBucketsResponse(typing_extensions.TypedDict, total=False):
    buckets: typing.List[LogBucket]
    nextPageToken: str

@typing.type_check_only
class ListExclusionsResponse(typing_extensions.TypedDict, total=False):
    exclusions: typing.List[LogExclusion]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListLogEntriesRequest(typing_extensions.TypedDict, total=False):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str
    projectIds: typing.List[str]
    resourceNames: typing.List[str]

@typing.type_check_only
class ListLogEntriesResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[LogEntry]
    nextPageToken: str

@typing.type_check_only
class ListLogMetricsResponse(typing_extensions.TypedDict, total=False):
    metrics: typing.List[LogMetric]
    nextPageToken: str

@typing.type_check_only
class ListLogsResponse(typing_extensions.TypedDict, total=False):
    logNames: typing.List[str]
    nextPageToken: str

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    resourceDescriptors: typing.List[MonitoredResourceDescriptor]

@typing.type_check_only
class ListSinksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sinks: typing.List[LogSink]

@typing.type_check_only
class ListViewsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    views: typing.List[LogView]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogBucket(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    locked: bool
    name: str
    retentionDays: int
    updateTime: str

@typing.type_check_only
class LogEntry(typing_extensions.TypedDict, total=False):
    httpRequest: HttpRequest
    insertId: str
    jsonPayload: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    logName: str
    metadata: MonitoredResourceMetadata
    operation: LogEntryOperation
    protoPayload: typing.Dict[str, typing.Any]
    receiveTimestamp: str
    resource: MonitoredResource
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
    spanId: str
    textPayload: str
    timestamp: str
    trace: str
    traceSampled: bool

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
class LogExclusion(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    disabled: bool
    filter: str
    name: str
    updateTime: str

@typing.type_check_only
class LogLine(typing_extensions.TypedDict, total=False):
    logMessage: str
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
    sourceLocation: SourceLocation
    time: str

@typing.type_check_only
class LogMetric(typing_extensions.TypedDict, total=False):
    bucketOptions: BucketOptions
    createTime: str
    description: str
    filter: str
    labelExtractors: typing.Dict[str, typing.Any]
    metricDescriptor: MetricDescriptor
    name: str
    updateTime: str
    valueExtractor: str
    version: typing_extensions.Literal["V2", "V1"]

@typing.type_check_only
class LogSink(typing_extensions.TypedDict, total=False):
    bigqueryOptions: BigQueryOptions
    createTime: str
    description: str
    destination: str
    disabled: bool
    exclusions: typing.List[LogExclusion]
    filter: str
    includeChildren: bool
    name: str
    outputVersionFormat: typing_extensions.Literal[
        "VERSION_FORMAT_UNSPECIFIED", "V2", "V1"
    ]
    updateTime: str
    writerIdentity: str

@typing.type_check_only
class LogView(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    filter: str
    name: str
    updateTime: str

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
class MonitoredResource(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    type: str

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
class MonitoredResourceMetadata(typing_extensions.TypedDict, total=False):
    systemLabels: typing.Dict[str, typing.Any]
    userLabels: typing.Dict[str, typing.Any]

@typing.type_check_only
class RequestLog(typing_extensions.TypedDict, total=False):
    appEngineRelease: str
    appId: str
    cost: float
    endTime: str
    finished: bool
    first: bool
    host: str
    httpVersion: str
    instanceId: str
    instanceIndex: int
    ip: str
    latency: str
    line: typing.List[LogLine]
    megaCycles: str
    method: str
    moduleId: str
    nickname: str
    pendingTime: str
    referrer: str
    requestId: str
    resource: str
    responseSize: str
    sourceReference: typing.List[SourceReference]
    startTime: str
    status: int
    taskName: str
    taskQueueName: str
    traceId: str
    traceSampled: bool
    urlMapEntry: str
    userAgent: str
    versionId: str
    wasLoadingRequest: bool

@typing.type_check_only
class SourceLocation(typing_extensions.TypedDict, total=False):
    file: str
    functionName: str
    line: str

@typing.type_check_only
class SourceReference(typing_extensions.TypedDict, total=False):
    repository: str
    revisionId: str

@typing.type_check_only
class SuppressionInfo(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED", "RATE_LIMIT", "NOT_CONSUMED"
    ]
    suppressedCount: int

@typing.type_check_only
class TailLogEntriesRequest(typing_extensions.TypedDict, total=False):
    bufferWindow: str
    filter: str
    resourceNames: typing.List[str]

@typing.type_check_only
class TailLogEntriesResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[LogEntry]
    suppressionInfo: typing.List[SuppressionInfo]

@typing.type_check_only
class UndeleteBucketRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class WriteLogEntriesRequest(typing_extensions.TypedDict, total=False):
    dryRun: bool
    entries: typing.List[LogEntry]
    labels: typing.Dict[str, typing.Any]
    logName: str
    partialSuccess: bool
    resource: MonitoredResource

@typing.type_check_only
class WriteLogEntriesResponse(typing_extensions.TypedDict, total=False): ...
