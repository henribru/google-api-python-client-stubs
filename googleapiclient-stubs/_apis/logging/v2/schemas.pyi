import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...
class UndeleteBucketRequest(typing_extensions.TypedDict, total=False): ...

class Explicit(typing_extensions.TypedDict, total=False):
    bounds: typing.List[float]

class ListLogMetricsResponse(typing_extensions.TypedDict, total=False):
    metrics: typing.List[LogMetric]
    nextPageToken: str

class WriteLogEntriesRequest(typing_extensions.TypedDict, total=False):
    partialSuccess: bool
    entries: typing.List[LogEntry]
    dryRun: bool
    resource: MonitoredResource
    labels: typing.Dict[str, typing.Any]
    logName: str

class LogSink(typing_extensions.TypedDict, total=False):
    filter: str
    bigqueryOptions: BigQueryOptions
    updateTime: str
    outputVersionFormat: typing_extensions.Literal[
        "VERSION_FORMAT_UNSPECIFIED", "V2", "V1"
    ]
    writerIdentity: str
    createTime: str
    disabled: bool
    includeChildren: bool
    destination: str
    description: str
    name: str
    exclusions: typing.List[LogExclusion]

class ListLogsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    logNames: typing.List[str]

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

class LogExclusion(typing_extensions.TypedDict, total=False):
    filter: str
    name: str
    description: str
    disabled: bool
    createTime: str
    updateTime: str

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    key: str
    description: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]

class ListLogEntriesRequest(typing_extensions.TypedDict, total=False):
    resourceNames: typing.List[str]
    orderBy: str
    pageSize: int
    filter: str
    pageToken: str
    projectIds: typing.List[str]

class ListExclusionsResponse(typing_extensions.TypedDict, total=False):
    exclusions: typing.List[LogExclusion]
    nextPageToken: str

class LogLine(typing_extensions.TypedDict, total=False):
    sourceLocation: SourceLocation
    time: str
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

class CmekSettings(typing_extensions.TypedDict, total=False):
    serviceAccountId: str
    name: str
    kmsKeyName: str

class ListViewsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    views: typing.List[LogView]

class LogEntrySourceLocation(typing_extensions.TypedDict, total=False):
    file: str
    line: str
    function: str

class SourceLocation(typing_extensions.TypedDict, total=False):
    file: str
    line: str
    functionName: str

class ListLogEntriesResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[LogEntry]
    nextPageToken: str

class HttpRequest(typing_extensions.TypedDict, total=False):
    cacheFillBytes: str
    userAgent: str
    cacheLookup: bool
    cacheValidatedWithOriginServer: bool
    cacheHit: bool
    latency: str
    referer: str
    protocol: str
    requestUrl: str
    serverIp: str
    requestMethod: str
    requestSize: str
    responseSize: str
    status: int
    remoteIp: str

class BigQueryOptions(typing_extensions.TypedDict, total=False):
    usesTimestampColumnPartitioning: bool
    usePartitionedTables: bool

class SourceReference(typing_extensions.TypedDict, total=False):
    revisionId: str
    repository: str

class Linear(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

class LogView(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str
    name: str
    description: str
    filter: str

class RequestLog(typing_extensions.TypedDict, total=False):
    appId: str
    endTime: str
    urlMapEntry: str
    traceSampled: bool
    userAgent: str
    wasLoadingRequest: bool
    responseSize: str
    resource: str
    pendingTime: str
    requestId: str
    nickname: str
    host: str
    versionId: str
    referrer: str
    method: str
    traceId: str
    sourceReference: typing.List[SourceReference]
    latency: str
    line: typing.List[LogLine]
    startTime: str
    ip: str
    first: bool
    status: int
    moduleId: str
    instanceId: str
    taskName: str
    httpVersion: str
    cost: float
    megaCycles: str
    instanceIndex: int
    taskQueueName: str
    appEngineRelease: str
    finished: bool

class LogBucket(typing_extensions.TypedDict, total=False):
    retentionDays: int
    description: str
    updateTime: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    name: str
    locked: bool
    createTime: str

class BucketOptions(typing_extensions.TypedDict, total=False):
    linearBuckets: Linear
    exponentialBuckets: Exponential
    explicitBuckets: Explicit

class WriteLogEntriesResponse(typing_extensions.TypedDict, total=False): ...

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
    name: str
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
    type: str
    displayName: str
    description: str
    labels: typing.List[LabelDescriptor]

class LogEntry(typing_extensions.TypedDict, total=False):
    sourceLocation: LogEntrySourceLocation
    textPayload: str
    insertId: str
    httpRequest: HttpRequest
    labels: typing.Dict[str, typing.Any]
    receiveTimestamp: str
    operation: LogEntryOperation
    spanId: str
    trace: str
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
    traceSampled: bool
    resource: MonitoredResource
    timestamp: str
    jsonPayload: typing.Dict[str, typing.Any]
    logName: str
    metadata: MonitoredResourceMetadata
    protoPayload: typing.Dict[str, typing.Any]

class ListMonitoredResourceDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    resourceDescriptors: typing.List[MonitoredResourceDescriptor]
    nextPageToken: str

class MetricDescriptor(typing_extensions.TypedDict, total=False):
    metadata: MetricDescriptorMetadata
    name: str
    displayName: str
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
    type: str
    description: str
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    monitoredResourceTypes: typing.List[str]
    labels: typing.List[LabelDescriptor]

class Exponential(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    scale: float
    growthFactor: float

class ListSinksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sinks: typing.List[LogSink]

class LogEntryOperation(typing_extensions.TypedDict, total=False):
    first: bool
    id: str
    last: bool
    producer: str

class MonitoredResourceMetadata(typing_extensions.TypedDict, total=False):
    userLabels: typing.Dict[str, typing.Any]
    systemLabels: typing.Dict[str, typing.Any]

class MonitoredResource(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    type: str

class ListBucketsResponse(typing_extensions.TypedDict, total=False):
    buckets: typing.List[LogBucket]
    nextPageToken: str

class LogMetric(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    filter: str
    bucketOptions: BucketOptions
    valueExtractor: str
    metricDescriptor: MetricDescriptor
    createTime: str
    updateTime: str
    labelExtractors: typing.Dict[str, typing.Any]
    version: typing_extensions.Literal["V2", "V1"]
