import typing

_list = list

@typing.type_check_only
class AppHub(typing.TypedDict, total=False):
    application: AppHubApplication
    service: AppHubService
    workload: AppHubWorkload

@typing.type_check_only
class AppHubApplication(typing.TypedDict, total=False):
    container: str
    id: str
    location: str

@typing.type_check_only
class AppHubService(typing.TypedDict, total=False):
    criticalityType: str
    environmentType: str
    id: str

@typing.type_check_only
class AppHubWorkload(typing.TypedDict, total=False):
    criticalityType: str
    environmentType: str
    id: str

@typing.type_check_only
class BigQueryDataset(typing.TypedDict, total=False):
    datasetId: str

@typing.type_check_only
class BigQueryOptions(typing.TypedDict, total=False):
    usePartitionedTables: bool
    usesTimestampColumnPartitioning: bool

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BucketMetadata(typing.TypedDict, total=False):
    createBucketRequest: CreateBucketRequest
    endTime: str
    startTime: str
    state: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "OPERATION_STATE_SCHEDULED",
        "OPERATION_STATE_WAITING_FOR_PERMISSIONS",
        "OPERATION_STATE_RUNNING",
        "OPERATION_STATE_SUCCEEDED",
        "OPERATION_STATE_FAILED",
        "OPERATION_STATE_CANCELLED",
        "OPERATION_STATE_PENDING",
    ]
    updateBucketRequest: UpdateBucketRequest

@typing.type_check_only
class BucketOptions(typing.TypedDict, total=False):
    explicitBuckets: Explicit
    exponentialBuckets: Exponential
    linearBuckets: Linear

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CmekSettings(typing.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyVersionName: str
    name: str
    serviceAccountId: str

@typing.type_check_only
class CopyLogEntriesMetadata(typing.TypedDict, total=False):
    cancellationRequested: bool
    destination: str
    endTime: str
    progress: int
    request: CopyLogEntriesRequest
    source: str
    startTime: str
    state: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "OPERATION_STATE_SCHEDULED",
        "OPERATION_STATE_WAITING_FOR_PERMISSIONS",
        "OPERATION_STATE_RUNNING",
        "OPERATION_STATE_SUCCEEDED",
        "OPERATION_STATE_FAILED",
        "OPERATION_STATE_CANCELLED",
        "OPERATION_STATE_PENDING",
    ]
    verb: str
    writerIdentity: str

@typing.type_check_only
class CopyLogEntriesRequest(typing.TypedDict, total=False):
    destination: str
    filter: str
    name: str

@typing.type_check_only
class CopyLogEntriesResponse(typing.TypedDict, total=False):
    logEntriesCopiedCount: str

@typing.type_check_only
class CreateBucketRequest(typing.TypedDict, total=False):
    bucket: LogBucket
    bucketId: str
    parent: str

@typing.type_check_only
class CreateLinkRequest(typing.TypedDict, total=False):
    link: Link
    linkId: str
    parent: str

@typing.type_check_only
class DefaultSinkConfig(typing.TypedDict, total=False):
    exclusions: _list[LogExclusion]
    filter: str
    mode: typing.Literal["FILTER_WRITE_MODE_UNSPECIFIED", "APPEND", "OVERWRITE"]

@typing.type_check_only
class DeleteLinkRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Explicit(typing.TypedDict, total=False):
    bounds: _list[float]

@typing.type_check_only
class Exponential(typing.TypedDict, total=False):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FieldSource(typing.TypedDict, total=False):
    aliasRef: str
    columnType: str
    field: str
    isJson: bool
    parentPath: str
    projectedField: ProjectedField

@typing.type_check_only
class FilterExpression(typing.TypedDict, total=False):
    comparator: typing.Literal[
        "COMPARATOR_UNSPECIFIED",
        "EQUALS",
        "MATCHES_REGEXP",
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_THAN_EQUALS",
        "LESS_THAN_EQUALS",
        "IS_NULL",
        "IN",
        "LIKE",
    ]
    fieldSource: FieldSource
    fieldSourceValue: FieldSource
    isNegation: bool
    literalValue: typing.Any

@typing.type_check_only
class FilterPredicate(typing.TypedDict, total=False):
    childPredicates: _list[FilterPredicate]
    leafPredicate: FilterExpression
    operatorType: typing.Literal["OPERATOR_TYPE_UNSPECIFIED", "AND", "OR", "LEAF"]

@typing.type_check_only
class FunctionApplication(typing.TypedDict, total=False):
    parameters: _list[typing.Any]
    type: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class HttpRequest(typing.TypedDict, total=False):
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
class IndexConfig(typing.TypedDict, total=False):
    createTime: str
    fieldPath: str
    type: typing.Literal[
        "INDEX_TYPE_UNSPECIFIED", "INDEX_TYPE_STRING", "INDEX_TYPE_INTEGER"
    ]

@typing.type_check_only
class LabelDescriptor(typing.TypedDict, total=False):
    description: str
    key: str
    valueType: typing.Literal["STRING", "BOOL", "INT64"]

@typing.type_check_only
class Linear(typing.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    bigqueryDataset: BigQueryDataset
    createTime: str
    description: str
    lifecycleState: typing.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "ACTIVE",
        "DELETE_REQUESTED",
        "UPDATING",
        "CREATING",
        "FAILED",
    ]
    name: str

@typing.type_check_only
class LinkMetadata(typing.TypedDict, total=False):
    createLinkRequest: CreateLinkRequest
    deleteLinkRequest: DeleteLinkRequest
    endTime: str
    startTime: str
    state: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "OPERATION_STATE_SCHEDULED",
        "OPERATION_STATE_WAITING_FOR_PERMISSIONS",
        "OPERATION_STATE_RUNNING",
        "OPERATION_STATE_SUCCEEDED",
        "OPERATION_STATE_FAILED",
        "OPERATION_STATE_CANCELLED",
        "OPERATION_STATE_PENDING",
    ]

@typing.type_check_only
class ListBucketsResponse(typing.TypedDict, total=False):
    buckets: _list[LogBucket]
    nextPageToken: str

@typing.type_check_only
class ListExclusionsResponse(typing.TypedDict, total=False):
    exclusions: _list[LogExclusion]
    nextPageToken: str

@typing.type_check_only
class ListLinksResponse(typing.TypedDict, total=False):
    links: _list[Link]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListLogEntriesRequest(typing.TypedDict, total=False):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str
    projectIds: _list[str]
    resourceNames: _list[str]

@typing.type_check_only
class ListLogEntriesResponse(typing.TypedDict, total=False):
    entries: _list[LogEntry]
    nextPageToken: str

@typing.type_check_only
class ListLogMetricsResponse(typing.TypedDict, total=False):
    metrics: _list[LogMetric]
    nextPageToken: str

@typing.type_check_only
class ListLogScopesResponse(typing.TypedDict, total=False):
    logScopes: _list[LogScope]
    nextPageToken: str

@typing.type_check_only
class ListLogsResponse(typing.TypedDict, total=False):
    logNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resourceDescriptors: _list[MonitoredResourceDescriptor]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListRecentQueriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    recentQueries: _list[RecentQuery]
    unreachable: _list[str]

@typing.type_check_only
class ListSavedQueriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    savedQueries: _list[SavedQuery]
    unreachable: _list[str]

@typing.type_check_only
class ListSinksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sinks: _list[LogSink]

@typing.type_check_only
class ListViewsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    views: _list[LogView]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    logAnalyticsEnabled: bool

@typing.type_check_only
class LogBucket(typing.TypedDict, total=False):
    analyticsEnabled: bool
    cmekSettings: CmekSettings
    createTime: str
    description: str
    indexConfigs: _list[IndexConfig]
    lifecycleState: typing.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "ACTIVE",
        "DELETE_REQUESTED",
        "UPDATING",
        "CREATING",
        "FAILED",
    ]
    locked: bool
    name: str
    restrictedFields: _list[str]
    retentionDays: int
    updateTime: str

@typing.type_check_only
class LogEntry(typing.TypedDict, total=False):
    apphub: AppHub
    apphubDestination: AppHub
    apphubSource: AppHub
    errorGroups: _list[LogErrorGroup]
    httpRequest: HttpRequest
    insertId: str
    jsonPayload: dict[str, typing.Any]
    labels: dict[str, typing.Any]
    logName: str
    metadata: MonitoredResourceMetadata
    operation: LogEntryOperation
    otel: dict[str, typing.Any]
    protoPayload: dict[str, typing.Any]
    receiveTimestamp: str
    resource: MonitoredResource
    severity: typing.Literal[
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
class LogEntryOperation(typing.TypedDict, total=False):
    first: bool
    id: str
    last: bool
    producer: str

@typing.type_check_only
class LogEntrySourceLocation(typing.TypedDict, total=False):
    file: str
    function: str
    line: str

@typing.type_check_only
class LogErrorGroup(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class LogExclusion(typing.TypedDict, total=False):
    createTime: str
    description: str
    disabled: bool
    filter: str
    name: str
    updateTime: str

@typing.type_check_only
class LogLine(typing.TypedDict, total=False):
    logMessage: str
    severity: typing.Literal[
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
class LogMetric(typing.TypedDict, total=False):
    bucketName: str
    bucketOptions: BucketOptions
    createTime: str
    description: str
    disabled: bool
    filter: str
    labelExtractors: dict[str, typing.Any]
    metricDescriptor: MetricDescriptor
    name: str
    resourceName: str
    updateTime: str
    valueExtractor: str
    version: typing.Literal["V2", "V1"]

@typing.type_check_only
class LogScope(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    resourceNames: _list[str]
    updateTime: str

@typing.type_check_only
class LogSink(typing.TypedDict, total=False):
    bigqueryOptions: BigQueryOptions
    createTime: str
    description: str
    destination: str
    disabled: bool
    exclusions: _list[LogExclusion]
    filter: str
    includeChildren: bool
    interceptChildren: bool
    name: str
    outputVersionFormat: typing.Literal["VERSION_FORMAT_UNSPECIFIED", "V2", "V1"]
    resourceName: str
    updateTime: str
    writerIdentity: str

@typing.type_check_only
class LogSplit(typing.TypedDict, total=False):
    index: int
    totalSplits: int
    uid: str

@typing.type_check_only
class LogView(typing.TypedDict, total=False):
    createTime: str
    description: str
    filter: str
    name: str
    updateTime: str

@typing.type_check_only
class LoggingQuery(typing.TypedDict, total=False):
    filter: str
    summaryFieldEnd: int
    summaryFieldStart: int
    summaryFields: _list[SummaryField]

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
class MonitoredResource(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

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
class MonitoredResourceMetadata(typing.TypedDict, total=False):
    systemLabels: dict[str, typing.Any]
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OpsAnalyticsQuery(typing.TypedDict, total=False):
    queryBuilder: QueryBuilderConfig
    sqlQueryText: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectedField(typing.TypedDict, total=False):
    alias: str
    cast: str
    field: str
    operation: typing.Literal[
        "FIELD_OPERATION_UNSPECIFIED", "NO_SETTING", "GROUP_BY", "AGGREGATE"
    ]
    regexExtraction: str
    sqlAggregationFunction: FunctionApplication
    truncationGranularity: str
    virtualField: VirtualField

@typing.type_check_only
class QueryBuilderConfig(typing.TypedDict, total=False):
    fieldSources: _list[FieldSource]
    filter: FilterPredicate
    limit: str
    orderBys: _list[SortOrderParameter]
    resourceNames: _list[str]
    searchTerm: str

@typing.type_check_only
class RecentQuery(typing.TypedDict, total=False):
    lastRunTime: str
    loggingQuery: LoggingQuery
    name: str
    opsAnalyticsQuery: OpsAnalyticsQuery

@typing.type_check_only
class RequestLog(typing.TypedDict, total=False):
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
class SavedQuery(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    loggingQuery: LoggingQuery
    name: str
    opsAnalyticsQuery: OpsAnalyticsQuery
    updateTime: str
    visibility: typing.Literal["VISIBILITY_UNSPECIFIED", "PRIVATE", "SHARED"]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Settings(typing.TypedDict, total=False):
    defaultSinkConfig: DefaultSinkConfig
    disableDefaultSink: bool
    kmsKeyName: str
    kmsServiceAccountId: str
    loggingServiceAccountId: str
    name: str
    storageLocation: str

@typing.type_check_only
class SortOrderParameter(typing.TypedDict, total=False):
    fieldSource: FieldSource
    sortOrderDirection: typing.Literal[
        "SORT_ORDER_UNSPECIFIED",
        "SORT_ORDER_NONE",
        "SORT_ORDER_ASCENDING",
        "SORT_ORDER_DESCENDING",
    ]

@typing.type_check_only
class SourceLocation(typing.TypedDict, total=False):
    file: str
    functionName: str
    line: str

@typing.type_check_only
class SourceReference(typing.TypedDict, total=False):
    repository: str
    revisionId: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SummaryField(typing.TypedDict, total=False):
    field: str

@typing.type_check_only
class SuppressionInfo(typing.TypedDict, total=False):
    reason: typing.Literal["REASON_UNSPECIFIED", "RATE_LIMIT", "NOT_CONSUMED"]
    suppressedCount: int

@typing.type_check_only
class TailLogEntriesRequest(typing.TypedDict, total=False):
    bufferWindow: str
    filter: str
    resourceNames: _list[str]

@typing.type_check_only
class TailLogEntriesResponse(typing.TypedDict, total=False):
    entries: _list[LogEntry]
    suppressionInfo: _list[SuppressionInfo]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeleteBucketRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateBucketRequest(typing.TypedDict, total=False):
    bucket: LogBucket
    name: str
    updateMask: str

@typing.type_check_only
class VirtualField(typing.TypedDict, total=False):
    underlyingFieldSources: _list[FieldSource]
    virtualFieldType: typing.Literal["VIRTUAL_FIELD_TYPE_UNSPECIFIED", "COALESCE"]

@typing.type_check_only
class WriteLogEntriesRequest(typing.TypedDict, total=False):
    dryRun: bool
    entries: _list[LogEntry]
    labels: dict[str, typing.Any]
    logName: str
    partialSuccess: bool
    resource: MonitoredResource

@typing.type_check_only
class WriteLogEntriesResponse(typing.TypedDict, total=False): ...
