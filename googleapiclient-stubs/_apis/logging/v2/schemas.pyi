import typing

import typing_extensions

_list = list

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
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CmekSettings(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyVersionName: str
    name: str
    serviceAccountId: str

@typing.type_check_only
class CopyLogEntriesMetadata(typing_extensions.TypedDict, total=False):
    cancellationRequested: bool
    endTime: str
    progress: int
    request: CopyLogEntriesRequest
    startTime: str
    state: typing_extensions.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "OPERATION_STATE_SCHEDULED",
        "OPERATION_STATE_WAITING_FOR_PERMISSIONS",
        "OPERATION_STATE_RUNNING",
        "OPERATION_STATE_SUCCEEDED",
        "OPERATION_STATE_FAILED",
        "OPERATION_STATE_CANCELLED",
    ]
    writerIdentity: str

@typing.type_check_only
class CopyLogEntriesRequest(typing_extensions.TypedDict, total=False):
    destination: str
    filter: str
    name: str

@typing.type_check_only
class CopyLogEntriesResponse(typing_extensions.TypedDict, total=False):
    logEntriesCopiedCount: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Explicit(typing_extensions.TypedDict, total=False):
    bounds: _list[float]

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
class IndexConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    fieldPath: str
    type: typing_extensions.Literal[
        "INDEX_TYPE_UNSPECIFIED", "INDEX_TYPE_STRING", "INDEX_TYPE_INTEGER"
    ]

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
    buckets: _list[LogBucket]
    nextPageToken: str

@typing.type_check_only
class ListExclusionsResponse(typing_extensions.TypedDict, total=False):
    exclusions: _list[LogExclusion]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListLogEntriesRequest(typing_extensions.TypedDict, total=False):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str
    projectIds: _list[str]
    resourceNames: _list[str]

@typing.type_check_only
class ListLogEntriesResponse(typing_extensions.TypedDict, total=False):
    entries: _list[LogEntry]
    nextPageToken: str

@typing.type_check_only
class ListLogMetricsResponse(typing_extensions.TypedDict, total=False):
    metrics: _list[LogMetric]
    nextPageToken: str

@typing.type_check_only
class ListLogsResponse(typing_extensions.TypedDict, total=False):
    logNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    resourceDescriptors: _list[MonitoredResourceDescriptor]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSinksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sinks: _list[LogSink]

@typing.type_check_only
class ListViewsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    views: _list[LogView]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogBucket(typing_extensions.TypedDict, total=False):
    cmekSettings: CmekSettings
    createTime: str
    description: str
    indexConfigs: _list[IndexConfig]
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    locked: bool
    name: str
    restrictedFields: _list[str]
    retentionDays: int
    updateTime: str

@typing.type_check_only
class LogEntry(typing_extensions.TypedDict, total=False):
    httpRequest: HttpRequest
    insertId: str
    jsonPayload: dict[str, typing.Any]
    labels: dict[str, typing.Any]
    logName: str
    metadata: MonitoredResourceMetadata
    operation: LogEntryOperation
    protoPayload: dict[str, typing.Any]
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
    split: LogSplit
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
    bucketName: str
    bucketOptions: BucketOptions
    createTime: str
    description: str
    disabled: bool
    filter: str
    labelExtractors: dict[str, typing.Any]
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
    exclusions: _list[LogExclusion]
    filter: str
    includeChildren: bool
    name: str
    outputVersionFormat: typing_extensions.Literal[
        "VERSION_FORMAT_UNSPECIFIED", "V2", "V1"
    ]
    updateTime: str
    writerIdentity: str

@typing.type_check_only
class LogSplit(typing_extensions.TypedDict, total=False):
    index: int
    totalSplits: int
    uid: str

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

@typing.type_check_only
class MonitoredResource(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

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
class MonitoredResourceMetadata(typing_extensions.TypedDict, total=False):
    systemLabels: dict[str, typing.Any]
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

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
    line: _list[LogLine]
    megaCycles: str
    method: str
    moduleId: str
    nickname: str
    pendingTime: str
    referrer: str
    requestId: str
    resource: str
    responseSize: str
    sourceReference: _list[SourceReference]
    spanId: str
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
class Settings(typing_extensions.TypedDict, total=False):
    disableDefaultSink: bool
    kmsKeyName: str
    kmsServiceAccountId: str
    name: str
    storageLocation: str

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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

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
    resourceNames: _list[str]

@typing.type_check_only
class TailLogEntriesResponse(typing_extensions.TypedDict, total=False):
    entries: _list[LogEntry]
    suppressionInfo: _list[SuppressionInfo]

@typing.type_check_only
class UndeleteBucketRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class WriteLogEntriesRequest(typing_extensions.TypedDict, total=False):
    dryRun: bool
    entries: _list[LogEntry]
    labels: dict[str, typing.Any]
    logName: str
    partialSuccess: bool
    resource: MonitoredResource

@typing.type_check_only
class WriteLogEntriesResponse(typing_extensions.TypedDict, total=False): ...
