import typing

import typing_extensions
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

@typing.type_check_only
class AlertPolicy(typing_extensions.TypedDict, total=False):
    combiner: typing_extensions.Literal[
        "COMBINE_UNSPECIFIED", "AND", "OR", "AND_WITH_MATCHING_RESOURCE"
    ]
    conditions: typing.List[Condition]
    creationRecord: MutationRecord
    displayName: str
    documentation: Documentation
    enabled: bool
    mutationRecord: MutationRecord
    name: str
    notificationChannels: typing.List[str]
    userLabels: typing.Dict[str, typing.Any]
    validity: Status

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
class BasicSli(typing_extensions.TypedDict, total=False):
    availability: AvailabilityCriteria
    latency: LatencyCriteria
    location: typing.List[str]
    method: typing.List[str]
    version: typing.List[str]

@typing.type_check_only
class BucketOptions(typing_extensions.TypedDict, total=False):
    explicitBuckets: Explicit
    exponentialBuckets: Exponential
    linearBuckets: Linear

@typing.type_check_only
class CloudEndpoints(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class ClusterIstio(typing_extensions.TypedDict, total=False):
    clusterName: str
    location: str
    serviceName: str
    serviceNamespace: str

@typing.type_check_only
class CollectdPayload(typing_extensions.TypedDict, total=False):
    endTime: str
    metadata: typing.Dict[str, typing.Any]
    plugin: str
    pluginInstance: str
    startTime: str
    type: str
    typeInstance: str
    values: typing.List[CollectdValue]

@typing.type_check_only
class CollectdPayloadError(typing_extensions.TypedDict, total=False):
    error: Status
    index: int
    valueErrors: typing.List[CollectdValueError]

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
    conditionMonitoringQueryLanguage: MonitoringQueryLanguageCondition
    conditionThreshold: MetricThreshold
    displayName: str
    name: str

@typing.type_check_only
class ContentMatcher(typing_extensions.TypedDict, total=False):
    content: str
    matcher: typing_extensions.Literal[
        "CONTENT_MATCHER_OPTION_UNSPECIFIED",
        "CONTAINS_STRING",
        "NOT_CONTAINS_STRING",
        "MATCHES_REGEX",
        "NOT_MATCHES_REGEX",
    ]

@typing.type_check_only
class CreateCollectdTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    collectdPayloads: typing.List[CollectdPayload]
    collectdVersion: str
    resource: MonitoredResource

@typing.type_check_only
class CreateCollectdTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    payloadErrors: typing.List[CollectdPayloadError]
    summary: CreateTimeSeriesSummary

@typing.type_check_only
class CreateTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    timeSeries: typing.List[TimeSeries]

@typing.type_check_only
class CreateTimeSeriesSummary(typing_extensions.TypedDict, total=False):
    errors: typing.List[Error]
    successPointCount: int
    totalPointCount: int

@typing.type_check_only
class Custom(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Distribution(typing_extensions.TypedDict, total=False):
    bucketCounts: typing.List[str]
    bucketOptions: BucketOptions
    count: str
    exemplars: typing.List[Exemplar]
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
    label: typing.Dict[str, typing.Any]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    pointCount: int
    status: Status

@typing.type_check_only
class Exemplar(typing_extensions.TypedDict, total=False):
    attachments: typing.List[typing.Dict[str, typing.Any]]
    timestamp: str
    value: float

@typing.type_check_only
class Explicit(typing_extensions.TypedDict, total=False):
    bounds: typing.List[float]

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
    options: typing.List[Option]
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
    authInfo: BasicAuthentication
    body: str
    contentType: typing_extensions.Literal["TYPE_UNSPECIFIED", "URL_ENCODED"]
    headers: typing.Dict[str, typing.Any]
    maskHeaders: bool
    path: str
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
    alertPolicies: typing.List[AlertPolicy]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListGroupMembersResponse(typing_extensions.TypedDict, total=False):
    members: typing.List[MonitoredResource]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    group: typing.List[Group]
    nextPageToken: str

@typing.type_check_only
class ListMetricDescriptorsResponse(typing_extensions.TypedDict, total=False):
    metricDescriptors: typing.List[MetricDescriptor]
    nextPageToken: str

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    resourceDescriptors: typing.List[MonitoredResourceDescriptor]

@typing.type_check_only
class ListNotificationChannelDescriptorsResponse(
    typing_extensions.TypedDict, total=False
):
    channelDescriptors: typing.List[NotificationChannelDescriptor]
    nextPageToken: str

@typing.type_check_only
class ListNotificationChannelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notificationChannels: typing.List[NotificationChannel]
    totalSize: int

@typing.type_check_only
class ListServiceLevelObjectivesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceLevelObjectives: typing.List[ServiceLevelObjective]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[Service]

@typing.type_check_only
class ListTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    executionErrors: typing.List[Status]
    nextPageToken: str
    timeSeries: typing.List[TimeSeries]
    unit: str

@typing.type_check_only
class ListUptimeCheckConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    uptimeCheckConfigs: typing.List[UptimeCheckConfig]

@typing.type_check_only
class ListUptimeCheckIpsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    uptimeCheckIps: typing.List[UptimeCheckIp]

@typing.type_check_only
class MeshIstio(typing_extensions.TypedDict, total=False):
    meshUid: str
    serviceName: str
    serviceNamespace: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    type: str

@typing.type_check_only
class MetricAbsence(typing_extensions.TypedDict, total=False):
    aggregations: typing.List[Aggregation]
    duration: str
    filter: str
    trigger: Trigger

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
class MetricRange(typing_extensions.TypedDict, total=False):
    range: GoogleMonitoringV3Range
    timeSeries: str

@typing.type_check_only
class MetricThreshold(typing_extensions.TypedDict, total=False):
    aggregations: typing.List[Aggregation]
    comparison: typing_extensions.Literal[
        "COMPARISON_UNSPECIFIED",
        "COMPARISON_GT",
        "COMPARISON_GE",
        "COMPARISON_LT",
        "COMPARISON_LE",
        "COMPARISON_EQ",
        "COMPARISON_NE",
    ]
    denominatorAggregations: typing.List[Aggregation]
    denominatorFilter: str
    duration: str
    filter: str
    thresholdValue: float
    trigger: Trigger

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
class MonitoringQueryLanguageCondition(typing_extensions.TypedDict, total=False):
    duration: str
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
    labels: typing.Dict[str, typing.Any]
    mutationRecords: typing.List[MutationRecord]
    name: str
    type: str
    userLabels: typing.Dict[str, typing.Any]
    verificationStatus: typing_extensions.Literal[
        "VERIFICATION_STATUS_UNSPECIFIED", "UNVERIFIED", "VERIFIED"
    ]

@typing.type_check_only
class NotificationChannelDescriptor(typing_extensions.TypedDict, total=False):
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
class Option(typing_extensions.TypedDict, total=False):
    name: str
    value: typing.Dict[str, typing.Any]

@typing.type_check_only
class PerformanceThreshold(typing_extensions.TypedDict, total=False):
    basicSliPerformance: BasicSli
    performance: RequestBasedSli
    threshold: float

@typing.type_check_only
class Point(typing_extensions.TypedDict, total=False):
    interval: TimeInterval
    value: TypedValue

@typing.type_check_only
class PointData(typing_extensions.TypedDict, total=False):
    timeInterval: TimeInterval
    values: typing.List[TypedValue]

@typing.type_check_only
class QueryTimeSeriesRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class QueryTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partialErrors: typing.List[Status]
    timeSeriesData: typing.List[TimeSeriesData]
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
class SendNotificationChannelVerificationCodeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    appEngine: AppEngine
    cloudEndpoints: CloudEndpoints
    clusterIstio: ClusterIstio
    custom: Custom
    displayName: str
    istioCanonicalService: IstioCanonicalService
    meshIstio: MeshIstio
    name: str
    telemetry: Telemetry

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

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    fileName: str

@typing.type_check_only
class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TcpCheck(typing_extensions.TypedDict, total=False):
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
    points: typing.List[Point]
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
    labelValues: typing.List[LabelValue]
    pointData: typing.List[PointData]

@typing.type_check_only
class TimeSeriesDescriptor(typing_extensions.TypedDict, total=False):
    labelDescriptors: typing.List[LabelDescriptor]
    pointDescriptors: typing.List[ValueDescriptor]

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
    fields: typing.List[Field]
    name: str
    oneofs: typing.List[str]
    options: typing.List[Option]
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
    contentMatchers: typing.List[ContentMatcher]
    displayName: str
    httpCheck: HttpCheck
    internalCheckers: typing.List[InternalChecker]
    isInternal: bool
    monitoredResource: MonitoredResource
    name: str
    period: str
    resourceGroup: ResourceGroup
    selectedRegions: typing.List[str]
    tcpCheck: TcpCheck
    timeout: str

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
