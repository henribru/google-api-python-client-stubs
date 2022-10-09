import typing

import typing_extensions

_list = list

@typing.type_check_only
class Aggregation(typing_extensions.TypedDict, total=False):
    alignmentPeriod: str
    crossSeriesReducer: typing_extensions.Literal[
        "REDUCE_NONE",
        "REDUCE_MEAN",
        "REDUCE_MIN",
        "REDUCE_MAX",
        "REDUCE_SUM",
        "REDUCE_STDDEV",
        "REDUCE_COUNT",
        "REDUCE_COUNT_TRUE",
        "REDUCE_COUNT_FALSE",
        "REDUCE_FRACTION_TRUE",
        "REDUCE_PERCENTILE_99",
        "REDUCE_PERCENTILE_95",
        "REDUCE_PERCENTILE_50",
        "REDUCE_PERCENTILE_05",
    ]
    groupByFields: _list[str]
    perSeriesAligner: typing_extensions.Literal[
        "ALIGN_NONE",
        "ALIGN_DELTA",
        "ALIGN_RATE",
        "ALIGN_INTERPOLATE",
        "ALIGN_NEXT_OLDER",
        "ALIGN_MIN",
        "ALIGN_MAX",
        "ALIGN_MEAN",
        "ALIGN_COUNT",
        "ALIGN_SUM",
        "ALIGN_STDDEV",
        "ALIGN_COUNT_TRUE",
        "ALIGN_COUNT_FALSE",
        "ALIGN_FRACTION_TRUE",
        "ALIGN_PERCENTILE_99",
        "ALIGN_PERCENTILE_95",
        "ALIGN_PERCENTILE_50",
        "ALIGN_PERCENTILE_05",
        "ALIGN_PERCENT_CHANGE",
    ]

@typing.type_check_only
class AlertPolicy(typing_extensions.TypedDict, total=False):
    alertStrategy: AlertStrategy
    combiner: typing_extensions.Literal[
        "COMBINE_UNSPECIFIED", "AND", "OR", "AND_WITH_MATCHING_RESOURCE"
    ]
    conditions: _list[Condition]
    creationRecord: MutationRecord
    displayName: str
    documentation: Documentation
    enabled: bool
    mutationRecord: MutationRecord
    name: str
    notificationChannels: _list[str]
    userLabels: dict[str, typing.Any]
    validity: Status

@typing.type_check_only
class AlertStrategy(typing_extensions.TypedDict, total=False):
    autoClose: str
    notificationRateLimit: NotificationRateLimit

@typing.type_check_only
class AppEngine(typing_extensions.TypedDict, total=False):
    moduleId: str

@typing.type_check_only
class AvailabilityCriteria(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BasicAuthentication(typing_extensions.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class BasicService(typing_extensions.TypedDict, total=False):
    serviceLabels: dict[str, typing.Any]
    serviceType: str

@typing.type_check_only
class BasicSli(typing_extensions.TypedDict, total=False):
    availability: AvailabilityCriteria
    latency: LatencyCriteria
    location: _list[str]
    method: _list[str]
    version: _list[str]

@typing.type_check_only
class BucketOptions(typing_extensions.TypedDict, total=False):
    explicitBuckets: Explicit
    exponentialBuckets: Exponential
    linearBuckets: Linear

@typing.type_check_only
class CloudEndpoints(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class CloudRun(typing_extensions.TypedDict, total=False):
    location: str
    serviceName: str

@typing.type_check_only
class ClusterIstio(typing_extensions.TypedDict, total=False):
    clusterName: str
    location: str
    serviceName: str
    serviceNamespace: str

@typing.type_check_only
class CollectdPayload(typing_extensions.TypedDict, total=False):
    endTime: str
    metadata: dict[str, typing.Any]
    plugin: str
    pluginInstance: str
    startTime: str
    type: str
    typeInstance: str
    values: _list[CollectdValue]

@typing.type_check_only
class CollectdPayloadError(typing_extensions.TypedDict, total=False):
    error: Status
    index: int
    valueErrors: _list[CollectdValueError]

@typing.type_check_only
class CollectdValue(typing_extensions.TypedDict, total=False):
    dataSourceName: str
    dataSourceType: typing_extensions.Literal[
        "UNSPECIFIED_DATA_SOURCE_TYPE", "GAUGE", "COUNTER", "DERIVE", "ABSOLUTE"
    ]
    value: TypedValue

@typing.type_check_only
class CollectdValueError(typing_extensions.TypedDict, total=False):
    error: Status
    index: int

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    conditionAbsent: MetricAbsence
    conditionMatchedLog: LogMatch
    conditionMonitoringQueryLanguage: MonitoringQueryLanguageCondition
    conditionThreshold: MetricThreshold
    displayName: str
    name: str

@typing.type_check_only
class ContentMatcher(typing_extensions.TypedDict, total=False):
    content: str
    jsonPathMatcher: JsonPathMatcher
    matcher: typing_extensions.Literal[
        "CONTENT_MATCHER_OPTION_UNSPECIFIED",
        "CONTAINS_STRING",
        "NOT_CONTAINS_STRING",
        "MATCHES_REGEX",
        "NOT_MATCHES_REGEX",
        "MATCHES_JSON_PATH",
        "NOT_MATCHES_JSON_PATH",
    ]

@typing.type_check_only
class CreateCollectdTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    collectdPayloads: _list[CollectdPayload]
    collectdVersion: str
    resource: MonitoredResource

@typing.type_check_only
class CreateCollectdTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    payloadErrors: _list[CollectdPayloadError]
    summary: CreateTimeSeriesSummary

@typing.type_check_only
class CreateTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    timeSeries: _list[TimeSeries]

@typing.type_check_only
class CreateTimeSeriesSummary(typing_extensions.TypedDict, total=False):
    errors: _list[Error]
    successPointCount: int
    totalPointCount: int

@typing.type_check_only
class Custom(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Distribution(typing_extensions.TypedDict, total=False):
    bucketCounts: _list[str]
    bucketOptions: BucketOptions
    count: str
    exemplars: _list[Exemplar]
    mean: float
    range: Range
    sumOfSquaredDeviation: float

@typing.type_check_only
class DistributionCut(typing_extensions.TypedDict, total=False):
    distributionFilter: str
    range: GoogleMonitoringV3Range

@typing.type_check_only
class Documentation(typing_extensions.TypedDict, total=False):
    content: str
    mimeType: str

@typing.type_check_only
class DroppedLabels(typing_extensions.TypedDict, total=False):
    label: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    pointCount: int
    status: Status

@typing.type_check_only
class Exemplar(typing_extensions.TypedDict, total=False):
    attachments: _list[dict[str, typing.Any]]
    timestamp: str
    value: float

@typing.type_check_only
class Explicit(typing_extensions.TypedDict, total=False):
    bounds: _list[float]

@typing.type_check_only
class Exponential(typing_extensions.TypedDict, total=False):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

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
class GetNotificationChannelVerificationCodeRequest(
    typing_extensions.TypedDict, total=False
):
    expireTime: str

@typing.type_check_only
class GetNotificationChannelVerificationCodeResponse(
    typing_extensions.TypedDict, total=False
):
    code: str
    expireTime: str

@typing.type_check_only
class GkeNamespace(typing_extensions.TypedDict, total=False):
    clusterName: str
    location: str
    namespaceName: str
    projectId: str

@typing.type_check_only
class GkeService(typing_extensions.TypedDict, total=False):
    clusterName: str
    location: str
    namespaceName: str
    projectId: str
    serviceName: str

@typing.type_check_only
class GkeWorkload(typing_extensions.TypedDict, total=False):
    clusterName: str
    location: str
    namespaceName: str
    projectId: str
    topLevelControllerName: str
    topLevelControllerType: str

@typing.type_check_only
class GoogleMonitoringV3Range(typing_extensions.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    displayName: str
    filter: str
    isCluster: bool
    name: str
    parentName: str

@typing.type_check_only
class HttpCheck(typing_extensions.TypedDict, total=False):
    acceptedResponseStatusCodes: _list[ResponseStatusCode]
    authInfo: BasicAuthentication
    body: str
    contentType: typing_extensions.Literal["TYPE_UNSPECIFIED", "URL_ENCODED"]
    headers: dict[str, typing.Any]
    maskHeaders: bool
    path: str
    pingConfig: PingConfig
    port: int
    requestMethod: typing_extensions.Literal["METHOD_UNSPECIFIED", "GET", "POST"]
    useSsl: bool
    validateSsl: bool

@typing.type_check_only
class InternalChecker(typing_extensions.TypedDict, total=False):
    displayName: str
    gcpZone: str
    name: str
    network: str
    peerProjectId: str
    state: typing_extensions.Literal["UNSPECIFIED", "CREATING", "RUNNING"]

@typing.type_check_only
class IstioCanonicalService(typing_extensions.TypedDict, total=False):
    canonicalService: str
    canonicalServiceNamespace: str
    meshUid: str

@typing.type_check_only
class JsonPathMatcher(typing_extensions.TypedDict, total=False):
    jsonMatcher: typing_extensions.Literal[
        "JSON_PATH_MATCHER_OPTION_UNSPECIFIED", "EXACT_MATCH", "REGEX_MATCH"
    ]
    jsonPath: str

@typing.type_check_only
class LabelDescriptor(typing_extensions.TypedDict, total=False):
    description: str
    key: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]

@typing.type_check_only
class LabelValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    int64Value: str
    stringValue: str

@typing.type_check_only
class LatencyCriteria(typing_extensions.TypedDict, total=False):
    threshold: str

@typing.type_check_only
class Linear(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class ListAlertPoliciesResponse(typing_extensions.TypedDict, total=False):
    alertPolicies: _list[AlertPolicy]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListGroupMembersResponse(typing_extensions.TypedDict, total=False):
    members: _list[MonitoredResource]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    group: _list[Group]
    nextPageToken: str

@typing.type_check_only
class ListMetricDescriptorsResponse(typing_extensions.TypedDict, total=False):
    metricDescriptors: _list[MetricDescriptor]
    nextPageToken: str

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    resourceDescriptors: _list[MonitoredResourceDescriptor]

@typing.type_check_only
class ListNotificationChannelDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    channelDescriptors: _list[NotificationChannelDescriptor]
    nextPageToken: str

@typing.type_check_only
class ListNotificationChannelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notificationChannels: _list[NotificationChannel]
    totalSize: int

@typing.type_check_only
class ListServiceLevelObjectivesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceLevelObjectives: _list[ServiceLevelObjective]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class ListTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    executionErrors: _list[Status]
    nextPageToken: str
    timeSeries: _list[TimeSeries]
    unit: str

@typing.type_check_only
class ListUptimeCheckConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    uptimeCheckConfigs: _list[UptimeCheckConfig]

@typing.type_check_only
class ListUptimeCheckIpsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    uptimeCheckIps: _list[UptimeCheckIp]

@typing.type_check_only
class LogMatch(typing_extensions.TypedDict, total=False):
    filter: str
    labelExtractors: dict[str, typing.Any]

@typing.type_check_only
class MeshIstio(typing_extensions.TypedDict, total=False):
    meshUid: str
    serviceName: str
    serviceNamespace: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class MetricAbsence(typing_extensions.TypedDict, total=False):
    aggregations: _list[Aggregation]
    duration: str
    filter: str
    trigger: Trigger

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
class MetricRange(typing_extensions.TypedDict, total=False):
    range: GoogleMonitoringV3Range
    timeSeries: str

@typing.type_check_only
class MetricThreshold(typing_extensions.TypedDict, total=False):
    aggregations: _list[Aggregation]
    comparison: typing_extensions.Literal[
        "COMPARISON_UNSPECIFIED",
        "COMPARISON_GT",
        "COMPARISON_GE",
        "COMPARISON_LT",
        "COMPARISON_LE",
        "COMPARISON_EQ",
        "COMPARISON_NE",
    ]
    denominatorAggregations: _list[Aggregation]
    denominatorFilter: str
    duration: str
    evaluationMissingData: typing_extensions.Literal[
        "EVALUATION_MISSING_DATA_UNSPECIFIED",
        "EVALUATION_MISSING_DATA_INACTIVE",
        "EVALUATION_MISSING_DATA_ACTIVE",
        "EVALUATION_MISSING_DATA_NO_OP",
    ]
    filter: str
    thresholdValue: float
    trigger: Trigger

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
class MonitoringQueryLanguageCondition(typing_extensions.TypedDict, total=False):
    duration: str
    evaluationMissingData: typing_extensions.Literal[
        "EVALUATION_MISSING_DATA_UNSPECIFIED",
        "EVALUATION_MISSING_DATA_INACTIVE",
        "EVALUATION_MISSING_DATA_ACTIVE",
        "EVALUATION_MISSING_DATA_NO_OP",
    ]
    query: str
    trigger: Trigger

@typing.type_check_only
class MutationRecord(typing_extensions.TypedDict, total=False):
    mutateTime: str
    mutatedBy: str

@typing.type_check_only
class NotificationChannel(typing_extensions.TypedDict, total=False):
    creationRecord: MutationRecord
    description: str
    displayName: str
    enabled: bool
    labels: dict[str, typing.Any]
    mutationRecords: _list[MutationRecord]
    name: str
    type: str
    userLabels: dict[str, typing.Any]
    verificationStatus: typing_extensions.Literal[
        "VERIFICATION_STATUS_UNSPECIFIED", "UNVERIFIED", "VERIFIED"
    ]

@typing.type_check_only
class NotificationChannelDescriptor(typing_extensions.TypedDict, total=False):
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
    supportedTiers: _list[str]
    type: str

@typing.type_check_only
class NotificationRateLimit(typing_extensions.TypedDict, total=False):
    period: str

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: dict[str, typing.Any]

@typing.type_check_only
class PerformanceThreshold(typing_extensions.TypedDict, total=False):
    basicSliPerformance: BasicSli
    performance: RequestBasedSli
    threshold: float

@typing.type_check_only
class PingConfig(typing_extensions.TypedDict, total=False):
    pingsCount: int

@typing.type_check_only
class Point(typing_extensions.TypedDict, total=False):
    interval: TimeInterval
    value: TypedValue

@typing.type_check_only
class PointData(typing_extensions.TypedDict, total=False):
    timeInterval: TimeInterval
    values: _list[TypedValue]

@typing.type_check_only
class QueryTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class QueryTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partialErrors: _list[Status]
    timeSeriesData: _list[TimeSeriesData]
    timeSeriesDescriptor: TimeSeriesDescriptor

@typing.type_check_only
class Range(typing_extensions.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class RequestBasedSli(typing_extensions.TypedDict, total=False):
    distributionCut: DistributionCut
    goodTotalRatio: TimeSeriesRatio

@typing.type_check_only
class ResourceGroup(typing_extensions.TypedDict, total=False):
    groupId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "INSTANCE", "AWS_ELB_LOAD_BALANCER"
    ]

@typing.type_check_only
class ResponseStatusCode(typing_extensions.TypedDict, total=False):
    statusClass: typing_extensions.Literal[
        "STATUS_CLASS_UNSPECIFIED",
        "STATUS_CLASS_1XX",
        "STATUS_CLASS_2XX",
        "STATUS_CLASS_3XX",
        "STATUS_CLASS_4XX",
        "STATUS_CLASS_5XX",
        "STATUS_CLASS_ANY",
    ]
    statusValue: int

@typing.type_check_only
class SendNotificationChannelVerificationCodeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    appEngine: AppEngine
    basicService: BasicService
    cloudEndpoints: CloudEndpoints
    cloudRun: CloudRun
    clusterIstio: ClusterIstio
    custom: Custom
    displayName: str
    gkeNamespace: GkeNamespace
    gkeService: GkeService
    gkeWorkload: GkeWorkload
    istioCanonicalService: IstioCanonicalService
    meshIstio: MeshIstio
    name: str
    telemetry: Telemetry
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class ServiceLevelIndicator(typing_extensions.TypedDict, total=False):
    basicSli: BasicSli
    requestBased: RequestBasedSli
    windowsBased: WindowsBasedSli

@typing.type_check_only
class ServiceLevelObjective(typing_extensions.TypedDict, total=False):
    calendarPeriod: typing_extensions.Literal[
        "CALENDAR_PERIOD_UNSPECIFIED",
        "DAY",
        "WEEK",
        "FORTNIGHT",
        "MONTH",
        "QUARTER",
        "HALF",
        "YEAR",
    ]
    displayName: str
    goal: float
    name: str
    rollingPeriod: str
    serviceLevelIndicator: ServiceLevelIndicator
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

@typing.type_check_only
class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TcpCheck(typing_extensions.TypedDict, total=False):
    pingConfig: PingConfig
    port: int

@typing.type_check_only
class Telemetry(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class TimeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TimeSeries(typing_extensions.TypedDict, total=False):
    metadata: MonitoredResourceMetadata
    metric: Metric
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    points: _list[Point]
    resource: MonitoredResource
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
class TimeSeriesData(typing_extensions.TypedDict, total=False):
    labelValues: _list[LabelValue]
    pointData: _list[PointData]

@typing.type_check_only
class TimeSeriesDescriptor(typing_extensions.TypedDict, total=False):
    labelDescriptors: _list[LabelDescriptor]
    pointDescriptors: _list[ValueDescriptor]

@typing.type_check_only
class TimeSeriesRatio(typing_extensions.TypedDict, total=False):
    badServiceFilter: str
    goodServiceFilter: str
    totalServiceFilter: str

@typing.type_check_only
class Trigger(typing_extensions.TypedDict, total=False):
    count: int
    percent: float

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    fields: _list[Field]
    name: str
    oneofs: _list[str]
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]

@typing.type_check_only
class TypedValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    distributionValue: Distribution
    doubleValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class UptimeCheckConfig(typing_extensions.TypedDict, total=False):
    checkerType: typing_extensions.Literal[
        "CHECKER_TYPE_UNSPECIFIED", "STATIC_IP_CHECKERS", "VPC_CHECKERS"
    ]
    contentMatchers: _list[ContentMatcher]
    displayName: str
    httpCheck: HttpCheck
    internalCheckers: _list[InternalChecker]
    isInternal: bool
    monitoredResource: MonitoredResource
    name: str
    period: str
    resourceGroup: ResourceGroup
    selectedRegions: _list[str]
    tcpCheck: TcpCheck
    timeout: str
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class UptimeCheckIp(typing_extensions.TypedDict, total=False):
    ipAddress: str
    location: str
    region: typing_extensions.Literal[
        "REGION_UNSPECIFIED", "USA", "EUROPE", "SOUTH_AMERICA", "ASIA_PACIFIC"
    ]

@typing.type_check_only
class ValueDescriptor(typing_extensions.TypedDict, total=False):
    key: str
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
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
class VerifyNotificationChannelRequest(typing_extensions.TypedDict, total=False):
    code: str

@typing.type_check_only
class WindowsBasedSli(typing_extensions.TypedDict, total=False):
    goodBadMetricFilter: str
    goodTotalRatioThreshold: PerformanceThreshold
    metricMeanInRange: MetricRange
    metricSumInRange: MetricRange
    windowPeriod: str
