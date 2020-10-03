import typing

import typing_extensions

class QueryTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    partialErrors: typing.List[Status]
    nextPageToken: str
    timeSeriesDescriptor: TimeSeriesDescriptor
    timeSeriesData: typing.List[TimeSeriesData]

class TimeSeriesRatio(typing_extensions.TypedDict, total=False):
    badServiceFilter: str
    goodServiceFilter: str
    totalServiceFilter: str

class Telemetry(typing_extensions.TypedDict, total=False):
    resourceName: str

class ListServiceLevelObjectivesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceLevelObjectives: typing.List[ServiceLevelObjective]

class Metric(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    type: str

class CreateCollectdTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    collectdVersion: str
    collectdPayloads: typing.List[CollectdPayload]
    resource: MonitoredResource

class ListAlertPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    alertPolicies: typing.List[AlertPolicy]

class Documentation(typing_extensions.TypedDict, total=False):
    mimeType: str
    content: str

class Type(typing_extensions.TypedDict, total=False):
    sourceContext: SourceContext
    name: str
    oneofs: typing.List[str]
    syntax: typing_extensions.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3"]
    fields: typing.List[Field]
    options: typing.List[Option]

class QueryTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

class AppEngine(typing_extensions.TypedDict, total=False):
    moduleId: str

class ServiceLevelIndicator(typing_extensions.TypedDict, total=False):
    requestBased: RequestBasedSli
    windowsBased: WindowsBasedSli
    basicSli: BasicSli

class Empty(typing_extensions.TypedDict, total=False): ...

class MonitoredResource(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    type: str

class Custom(typing_extensions.TypedDict, total=False): ...

class MeshIstio(typing_extensions.TypedDict, total=False):
    serviceNamespace: str
    meshUid: str
    serviceName: str

class MetricDescriptor(typing_extensions.TypedDict, total=False):
    monitoredResourceTypes: typing.List[str]
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
    labels: typing.List[LabelDescriptor]
    name: str
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    description: str
    unit: str
    type: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]
    displayName: str
    metadata: MetricDescriptorMetadata

class BucketOptions(typing_extensions.TypedDict, total=False):
    linearBuckets: Linear
    explicitBuckets: Explicit
    exponentialBuckets: Exponential

class AvailabilityCriteria(typing_extensions.TypedDict, total=False): ...

class MonitoredResourceMetadata(typing_extensions.TypedDict, total=False):
    userLabels: typing.Dict[str, typing.Any]
    systemLabels: typing.Dict[str, typing.Any]

class Error(typing_extensions.TypedDict, total=False):
    status: Status
    pointCount: int

class Exemplar(typing_extensions.TypedDict, total=False):
    attachments: typing.List[typing.Dict[str, typing.Any]]
    value: float
    timestamp: str

class PerformanceThreshold(typing_extensions.TypedDict, total=False):
    threshold: float
    basicSliPerformance: BasicSli
    performance: RequestBasedSli

class UptimeCheckConfig(typing_extensions.TypedDict, total=False):
    displayName: str
    contentMatchers: typing.List[ContentMatcher]
    resourceGroup: ResourceGroup
    timeout: str
    isInternal: bool
    name: str
    internalCheckers: typing.List[InternalChecker]
    period: str
    selectedRegions: typing.List[str]
    monitoredResource: MonitoredResource
    httpCheck: HttpCheck
    tcpCheck: TcpCheck

class DroppedLabels(typing_extensions.TypedDict, total=False):
    label: typing.Dict[str, typing.Any]

class Trigger(typing_extensions.TypedDict, total=False):
    count: int
    percent: float

class HttpCheck(typing_extensions.TypedDict, total=False):
    useSsl: bool
    maskHeaders: bool
    requestMethod: typing_extensions.Literal["METHOD_UNSPECIFIED", "GET", "POST"]
    path: str
    authInfo: BasicAuthentication
    port: int
    headers: typing.Dict[str, typing.Any]
    contentType: typing_extensions.Literal["TYPE_UNSPECIFIED", "URL_ENCODED"]
    validateSsl: bool
    body: str

class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

class Group(typing_extensions.TypedDict, total=False):
    filter: str
    name: str
    displayName: str
    parentName: str
    isCluster: bool

class ListNotificationChannelDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    channelDescriptors: typing.List[NotificationChannelDescriptor]

class GoogleMonitoringV3Range(typing_extensions.TypedDict, total=False):
    max: float
    min: float

class CreateTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    timeSeries: typing.List[TimeSeries]

class CollectdPayloadError(typing_extensions.TypedDict, total=False):
    error: Status
    index: int
    valueErrors: typing.List[CollectdValueError]

class MutationRecord(typing_extensions.TypedDict, total=False):
    mutatedBy: str
    mutateTime: str

class AlertPolicy(typing_extensions.TypedDict, total=False):
    displayName: str
    userLabels: typing.Dict[str, typing.Any]
    mutationRecord: MutationRecord
    creationRecord: MutationRecord
    combiner: typing_extensions.Literal[
        "COMBINE_UNSPECIFIED", "AND", "OR", "AND_WITH_MATCHING_RESOURCE"
    ]
    name: str
    validity: Status
    conditions: typing.List[Condition]
    notificationChannels: typing.List[str]
    enabled: bool
    documentation: Documentation

class CollectdValueError(typing_extensions.TypedDict, total=False):
    index: int
    error: Status

class MetricAbsence(typing_extensions.TypedDict, total=False):
    filter: str
    duration: str
    aggregations: typing.List[Aggregation]
    trigger: Trigger

class Linear(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    width: float
    offset: float

class ListUptimeCheckIpsResponse(typing_extensions.TypedDict, total=False):
    uptimeCheckIps: typing.List[UptimeCheckIp]
    nextPageToken: str

class MonitoredResourceDescriptor(typing_extensions.TypedDict, total=False):
    labels: typing.List[LabelDescriptor]
    description: str
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
    displayName: str

class TypedValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    int64Value: str
    distributionValue: Distribution
    stringValue: str
    doubleValue: float

class Service(typing_extensions.TypedDict, total=False):
    clusterIstio: ClusterIstio
    custom: Custom
    displayName: str
    appEngine: AppEngine
    telemetry: Telemetry
    name: str
    meshIstio: MeshIstio
    cloudEndpoints: CloudEndpoints

class TcpCheck(typing_extensions.TypedDict, total=False):
    port: int

class VerifyNotificationChannelRequest(typing_extensions.TypedDict, total=False):
    code: str

class ContentMatcher(typing_extensions.TypedDict, total=False):
    matcher: typing_extensions.Literal[
        "CONTENT_MATCHER_OPTION_UNSPECIFIED",
        "CONTAINS_STRING",
        "NOT_CONTAINS_STRING",
        "MATCHES_REGEX",
        "NOT_MATCHES_REGEX",
    ]
    content: str

class ListTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    timeSeries: typing.List[TimeSeries]
    nextPageToken: str
    executionErrors: typing.List[Status]
    unit: str

class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

class GetNotificationChannelVerificationCodeResponse(
    typing_extensions.TypedDict, total=False
):
    code: str
    expireTime: str

class Field(typing_extensions.TypedDict, total=False):
    typeUrl: str
    options: typing.List[Option]
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
    number: int
    packed: bool
    oneofIndex: int
    name: str
    defaultValue: str
    cardinality: typing_extensions.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    jsonName: str

class ListUptimeCheckConfigsResponse(typing_extensions.TypedDict, total=False):
    totalSize: int
    nextPageToken: str
    uptimeCheckConfigs: typing.List[UptimeCheckConfig]

class TimeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class ValueDescriptor(typing_extensions.TypedDict, total=False):
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    key: str
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

class BasicSli(typing_extensions.TypedDict, total=False):
    version: typing.List[str]
    availability: AvailabilityCriteria
    method: typing.List[str]
    latency: LatencyCriteria
    location: typing.List[str]

class InternalChecker(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["UNSPECIFIED", "CREATING", "RUNNING"]
    name: str
    network: str
    gcpZone: str
    peerProjectId: str
    displayName: str

class ResourceGroup(typing_extensions.TypedDict, total=False):
    groupId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "INSTANCE", "AWS_ELB_LOAD_BALANCER"
    ]

class ClusterIstio(typing_extensions.TypedDict, total=False):
    serviceNamespace: str
    clusterName: str
    serviceName: str
    location: str

class ListMetricDescriptorsResponse(typing_extensions.TypedDict, total=False):
    metricDescriptors: typing.List[MetricDescriptor]
    nextPageToken: str

class SendNotificationChannelVerificationCodeRequest(
    typing_extensions.TypedDict, total=False
): ...

class LatencyCriteria(typing_extensions.TypedDict, total=False):
    threshold: str

class TimeSeries(typing_extensions.TypedDict, total=False):
    unit: str
    metadata: MonitoredResourceMetadata
    resource: MonitoredResource
    points: typing.List[Point]
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "DOUBLE",
        "STRING",
        "DISTRIBUTION",
        "MONEY",
    ]
    metricKind: typing_extensions.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    metric: Metric

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    services: typing.List[Service]
    nextPageToken: str

class TimeSeriesData(typing_extensions.TypedDict, total=False):
    labelValues: typing.List[LabelValue]
    pointData: typing.List[PointData]

class RequestBasedSli(typing_extensions.TypedDict, total=False):
    distributionCut: DistributionCut
    goodTotalRatio: TimeSeriesRatio

class NotificationChannel(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    displayName: str
    verificationStatus: typing_extensions.Literal[
        "VERIFICATION_STATUS_UNSPECIFIED", "UNVERIFIED", "VERIFIED"
    ]
    name: str
    type: str
    userLabels: typing.Dict[str, typing.Any]
    description: str
    enabled: bool

class Aggregation(typing_extensions.TypedDict, total=False):
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
    alignmentPeriod: str
    groupByFields: typing.List[str]
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

class TimeSeriesDescriptor(typing_extensions.TypedDict, total=False):
    pointDescriptors: typing.List[ValueDescriptor]
    labelDescriptors: typing.List[LabelDescriptor]

class Distribution(typing_extensions.TypedDict, total=False):
    mean: float
    sumOfSquaredDeviation: float
    range: Range
    count: str
    bucketOptions: BucketOptions
    exemplars: typing.List[Exemplar]
    bucketCounts: typing.List[str]

class Condition(typing_extensions.TypedDict, total=False):
    displayName: str
    conditionAbsent: MetricAbsence
    name: str
    conditionThreshold: MetricThreshold

class ServiceLevelObjective(typing_extensions.TypedDict, total=False):
    displayName: str
    goal: float
    serviceLevelIndicator: ServiceLevelIndicator
    rollingPeriod: str
    name: str
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

class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    group: typing.List[Group]

class BasicAuthentication(typing_extensions.TypedDict, total=False):
    username: str
    password: str

class GetNotificationChannelVerificationCodeRequest(
    typing_extensions.TypedDict, total=False
):
    expireTime: str

class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

class Point(typing_extensions.TypedDict, total=False):
    interval: TimeInterval
    value: TypedValue

class MetricThreshold(typing_extensions.TypedDict, total=False):
    denominatorAggregations: typing.List[Aggregation]
    aggregations: typing.List[Aggregation]
    trigger: Trigger
    filter: str
    duration: str
    thresholdValue: float
    denominatorFilter: str
    comparison: typing_extensions.Literal[
        "COMPARISON_UNSPECIFIED",
        "COMPARISON_GT",
        "COMPARISON_GE",
        "COMPARISON_LT",
        "COMPARISON_LE",
        "COMPARISON_EQ",
        "COMPARISON_NE",
    ]

class LabelValue(typing_extensions.TypedDict, total=False):
    stringValue: str
    int64Value: str
    boolValue: bool

class MetricRange(typing_extensions.TypedDict, total=False):
    timeSeries: str
    range: GoogleMonitoringV3Range

class CreateTimeSeriesSummary(typing_extensions.TypedDict, total=False):
    totalPointCount: int
    errors: typing.List[Error]
    successPointCount: int

class MetricDescriptorMetadata(typing_extensions.TypedDict, total=False):
    samplePeriod: str
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

class ListGroupMembersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    members: typing.List[MonitoredResource]

class ListMonitoredResourceDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    resourceDescriptors: typing.List[MonitoredResourceDescriptor]

class NotificationChannelDescriptor(typing_extensions.TypedDict, total=False):
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
    type: str
    displayName: str
    description: str
    name: str

class UptimeCheckIp(typing_extensions.TypedDict, total=False):
    location: str
    region: typing_extensions.Literal[
        "REGION_UNSPECIFIED", "USA", "EUROPE", "SOUTH_AMERICA", "ASIA_PACIFIC"
    ]
    ipAddress: str

class CloudEndpoints(typing_extensions.TypedDict, total=False):
    service: str

class CollectdPayload(typing_extensions.TypedDict, total=False):
    endTime: str
    typeInstance: str
    plugin: str
    metadata: typing.Dict[str, typing.Any]
    type: str
    values: typing.List[CollectdValue]
    startTime: str
    pluginInstance: str

class PointData(typing_extensions.TypedDict, total=False):
    timeInterval: TimeInterval
    values: typing.List[TypedValue]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Range(typing_extensions.TypedDict, total=False):
    max: float
    min: float

class Explicit(typing_extensions.TypedDict, total=False):
    bounds: typing.List[float]

class DistributionCut(typing_extensions.TypedDict, total=False):
    range: GoogleMonitoringV3Range
    distributionFilter: str

class Exponential(typing_extensions.TypedDict, total=False):
    scale: float
    growthFactor: float
    numFiniteBuckets: int

class LabelDescriptor(typing_extensions.TypedDict, total=False):
    key: str
    description: str
    valueType: typing_extensions.Literal["STRING", "BOOL", "INT64"]

class WindowsBasedSli(typing_extensions.TypedDict, total=False):
    metricMeanInRange: MetricRange
    goodTotalRatioThreshold: PerformanceThreshold
    metricSumInRange: MetricRange
    windowPeriod: str
    goodBadMetricFilter: str

class ListNotificationChannelsResponse(typing_extensions.TypedDict, total=False):
    notificationChannels: typing.List[NotificationChannel]
    totalSize: int
    nextPageToken: str

class CollectdValue(typing_extensions.TypedDict, total=False):
    dataSourceName: str
    value: TypedValue
    dataSourceType: typing_extensions.Literal[
        "UNSPECIFIED_DATA_SOURCE_TYPE", "GAUGE", "COUNTER", "DERIVE", "ABSOLUTE"
    ]

class CreateCollectdTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    summary: CreateTimeSeriesSummary
    payloadErrors: typing.List[CollectdPayloadError]
