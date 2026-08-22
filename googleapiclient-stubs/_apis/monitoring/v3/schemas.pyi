import typing

_list = list

@typing.type_check_only
class Aggregation(typing.TypedDict, total=False):
    alignmentPeriod: str
    crossSeriesReducer: typing.Literal[
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
    perSeriesAligner: typing.Literal[
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
class Alert(typing.TypedDict, total=False):
    closeTime: str
    log: LogMetadata
    metadata: MonitoredResourceMetadata
    metric: Metric
    name: str
    openTime: str
    policy: PolicySnapshot
    resource: MonitoredResource
    state: typing.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED"]

@typing.type_check_only
class AlertPolicy(typing.TypedDict, total=False):
    alertStrategy: AlertStrategy
    combiner: typing.Literal[
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
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "ERROR", "WARNING"]
    userLabels: dict[str, typing.Any]
    validity: Status

@typing.type_check_only
class AlertStrategy(typing.TypedDict, total=False):
    autoClose: str
    notificationChannelStrategy: _list[NotificationChannelStrategy]
    notificationPrompts: _list[
        typing.Literal["NOTIFICATION_PROMPT_UNSPECIFIED", "OPENED", "CLOSED"]
    ]
    notificationRateLimit: NotificationRateLimit

@typing.type_check_only
class AppEngine(typing.TypedDict, total=False):
    moduleId: str

@typing.type_check_only
class AvailabilityCriteria(typing.TypedDict, total=False): ...

@typing.type_check_only
class BasicAuthentication(typing.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class BasicService(typing.TypedDict, total=False):
    serviceLabels: dict[str, typing.Any]
    serviceType: str

@typing.type_check_only
class BasicSli(typing.TypedDict, total=False):
    availability: AvailabilityCriteria
    latency: LatencyCriteria
    location: _list[str]
    method: _list[str]
    version: _list[str]

@typing.type_check_only
class BooleanTest(typing.TypedDict, total=False):
    column: str

@typing.type_check_only
class BucketOptions(typing.TypedDict, total=False):
    explicitBuckets: Explicit
    exponentialBuckets: Exponential
    linearBuckets: Linear

@typing.type_check_only
class CloudEndpoints(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class CloudFunctionV2Target(typing.TypedDict, total=False):
    cloudRunRevision: MonitoredResource
    name: str

@typing.type_check_only
class CloudRun(typing.TypedDict, total=False):
    location: str
    serviceName: str

@typing.type_check_only
class ClusterIstio(typing.TypedDict, total=False):
    clusterName: str
    location: str
    serviceName: str
    serviceNamespace: str

@typing.type_check_only
class CollectdPayload(typing.TypedDict, total=False):
    endTime: str
    metadata: dict[str, typing.Any]
    plugin: str
    pluginInstance: str
    startTime: str
    type: str
    typeInstance: str
    values: _list[CollectdValue]

@typing.type_check_only
class CollectdPayloadError(typing.TypedDict, total=False):
    error: Status
    index: int
    valueErrors: _list[CollectdValueError]

@typing.type_check_only
class CollectdValue(typing.TypedDict, total=False):
    dataSourceName: str
    dataSourceType: typing.Literal[
        "UNSPECIFIED_DATA_SOURCE_TYPE", "GAUGE", "COUNTER", "DERIVE", "ABSOLUTE"
    ]
    value: TypedValue

@typing.type_check_only
class CollectdValueError(typing.TypedDict, total=False):
    error: Status
    index: int

@typing.type_check_only
class Condition(typing.TypedDict, total=False):
    conditionAbsent: MetricAbsence
    conditionMatchedLog: LogMatch
    conditionMonitoringQueryLanguage: MonitoringQueryLanguageCondition
    conditionPrometheusQueryLanguage: PrometheusQueryLanguageCondition
    conditionSql: SqlCondition
    conditionThreshold: MetricThreshold
    displayName: str
    name: str

@typing.type_check_only
class ContentMatcher(typing.TypedDict, total=False):
    content: str
    jsonPathMatcher: JsonPathMatcher
    matcher: typing.Literal[
        "CONTENT_MATCHER_OPTION_UNSPECIFIED",
        "CONTAINS_STRING",
        "NOT_CONTAINS_STRING",
        "MATCHES_REGEX",
        "NOT_MATCHES_REGEX",
        "MATCHES_JSON_PATH",
        "NOT_MATCHES_JSON_PATH",
    ]

@typing.type_check_only
class CreateCollectdTimeSeriesRequest(typing.TypedDict, total=False):
    collectdPayloads: _list[CollectdPayload]
    collectdVersion: str
    resource: MonitoredResource

@typing.type_check_only
class CreateCollectdTimeSeriesResponse(typing.TypedDict, total=False):
    payloadErrors: _list[CollectdPayloadError]
    summary: CreateTimeSeriesSummary

@typing.type_check_only
class CreateTimeSeriesRequest(typing.TypedDict, total=False):
    timeSeries: _list[TimeSeries]

@typing.type_check_only
class CreateTimeSeriesSummary(typing.TypedDict, total=False):
    errors: _list[Error]
    successPointCount: int
    totalPointCount: int

@typing.type_check_only
class Criteria(typing.TypedDict, total=False):
    filter: str
    policies: _list[str]

@typing.type_check_only
class Custom(typing.TypedDict, total=False): ...

@typing.type_check_only
class Daily(typing.TypedDict, total=False):
    executionTime: TimeOfDay
    periodicity: int

@typing.type_check_only
class Distribution(typing.TypedDict, total=False):
    bucketCounts: _list[str]
    bucketOptions: BucketOptions
    count: str
    exemplars: _list[Exemplar]
    mean: float
    range: Range
    sumOfSquaredDeviation: float

@typing.type_check_only
class DistributionCut(typing.TypedDict, total=False):
    distributionFilter: str
    range: GoogleMonitoringV3Range

@typing.type_check_only
class Documentation(typing.TypedDict, total=False):
    content: str
    links: _list[Link]
    mimeType: str
    subject: str

@typing.type_check_only
class DroppedLabels(typing.TypedDict, total=False):
    label: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing.TypedDict, total=False):
    pointCount: int
    status: Status

@typing.type_check_only
class Exemplar(typing.TypedDict, total=False):
    attachments: _list[dict[str, typing.Any]]
    timestamp: str
    value: float

@typing.type_check_only
class Explicit(typing.TypedDict, total=False):
    bounds: _list[float]

@typing.type_check_only
class Exponential(typing.TypedDict, total=False):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    cardinality: typing.Literal[
        "CARDINALITY_UNKNOWN",
        "CARDINALITY_OPTIONAL",
        "CARDINALITY_REQUIRED",
        "CARDINALITY_REPEATED",
    ]
    defaultValue: str
    jsonName: str
    kind: typing.Literal[
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
class ForecastOptions(typing.TypedDict, total=False):
    forecastHorizon: str

@typing.type_check_only
class GetNotificationChannelVerificationCodeRequest(typing.TypedDict, total=False):
    expireTime: str

@typing.type_check_only
class GetNotificationChannelVerificationCodeResponse(typing.TypedDict, total=False):
    code: str
    expireTime: str

@typing.type_check_only
class GkeNamespace(typing.TypedDict, total=False):
    clusterName: str
    location: str
    namespaceName: str
    projectId: str

@typing.type_check_only
class GkeService(typing.TypedDict, total=False):
    clusterName: str
    location: str
    namespaceName: str
    projectId: str
    serviceName: str

@typing.type_check_only
class GkeWorkload(typing.TypedDict, total=False):
    clusterName: str
    location: str
    namespaceName: str
    projectId: str
    topLevelControllerName: str
    topLevelControllerType: str

@typing.type_check_only
class GoogleMonitoringV3Range(typing.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    displayName: str
    filter: str
    isCluster: bool
    name: str
    parentName: str

@typing.type_check_only
class Hourly(typing.TypedDict, total=False):
    minuteOffset: int
    periodicity: int

@typing.type_check_only
class HttpCheck(typing.TypedDict, total=False):
    acceptedResponseStatusCodes: _list[ResponseStatusCode]
    authInfo: BasicAuthentication
    body: str
    contentType: typing.Literal["TYPE_UNSPECIFIED", "URL_ENCODED", "USER_PROVIDED"]
    customContentType: str
    headers: dict[str, typing.Any]
    maskHeaders: bool
    path: str
    pingConfig: PingConfig
    port: int
    requestMethod: typing.Literal["METHOD_UNSPECIFIED", "GET", "POST"]
    serviceAgentAuthentication: ServiceAgentAuthentication
    useSsl: bool
    validateSsl: bool

@typing.type_check_only
class InternalChecker(typing.TypedDict, total=False):
    displayName: str
    gcpZone: str
    name: str
    network: str
    peerProjectId: str
    state: typing.Literal["UNSPECIFIED", "CREATING", "RUNNING"]

@typing.type_check_only
class IstioCanonicalService(typing.TypedDict, total=False):
    canonicalService: str
    canonicalServiceNamespace: str
    meshUid: str

@typing.type_check_only
class JsonPathMatcher(typing.TypedDict, total=False):
    jsonMatcher: typing.Literal[
        "JSON_PATH_MATCHER_OPTION_UNSPECIFIED", "EXACT_MATCH", "REGEX_MATCH"
    ]
    jsonPath: str

@typing.type_check_only
class LabelDescriptor(typing.TypedDict, total=False):
    description: str
    key: str
    valueType: typing.Literal["STRING", "BOOL", "INT64"]

@typing.type_check_only
class LabelValue(typing.TypedDict, total=False):
    boolValue: bool
    int64Value: str
    stringValue: str

@typing.type_check_only
class LatencyCriteria(typing.TypedDict, total=False):
    threshold: str

@typing.type_check_only
class Linear(typing.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    displayName: str
    url: str

@typing.type_check_only
class ListAlertPoliciesResponse(typing.TypedDict, total=False):
    alertPolicies: _list[AlertPolicy]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListAlertsResponse(typing.TypedDict, total=False):
    alerts: _list[Alert]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListGroupMembersResponse(typing.TypedDict, total=False):
    members: _list[MonitoredResource]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListGroupsResponse(typing.TypedDict, total=False):
    group: _list[Group]
    nextPageToken: str

@typing.type_check_only
class ListMetricDescriptorsResponse(typing.TypedDict, total=False):
    metricDescriptors: _list[MetricDescriptor]
    nextPageToken: str

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resourceDescriptors: _list[MonitoredResourceDescriptor]

@typing.type_check_only
class ListNotificationChannelDescriptorsResponse(typing.TypedDict, total=False):
    channelDescriptors: _list[NotificationChannelDescriptor]
    nextPageToken: str

@typing.type_check_only
class ListNotificationChannelsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    notificationChannels: _list[NotificationChannel]
    totalSize: int

@typing.type_check_only
class ListServiceLevelObjectivesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    serviceLevelObjectives: _list[ServiceLevelObjective]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class ListSnoozesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    snoozes: _list[Snooze]

@typing.type_check_only
class ListTimeSeriesResponse(typing.TypedDict, total=False):
    executionErrors: _list[Status]
    nextPageToken: str
    timeSeries: _list[TimeSeries]
    unit: str
    unreachable: _list[str]

@typing.type_check_only
class ListUptimeCheckConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    uptimeCheckConfigs: _list[UptimeCheckConfig]

@typing.type_check_only
class ListUptimeCheckIpsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    uptimeCheckIps: _list[UptimeCheckIp]

@typing.type_check_only
class LogMatch(typing.TypedDict, total=False):
    filter: str
    labelExtractors: dict[str, typing.Any]

@typing.type_check_only
class LogMetadata(typing.TypedDict, total=False):
    extractedLabels: dict[str, typing.Any]

@typing.type_check_only
class MeshIstio(typing.TypedDict, total=False):
    meshUid: str
    serviceName: str
    serviceNamespace: str

@typing.type_check_only
class Metric(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class MetricAbsence(typing.TypedDict, total=False):
    aggregations: _list[Aggregation]
    duration: str
    filter: str
    trigger: Trigger

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
class MetricRange(typing.TypedDict, total=False):
    range: GoogleMonitoringV3Range
    timeSeries: str

@typing.type_check_only
class MetricThreshold(typing.TypedDict, total=False):
    aggregations: _list[Aggregation]
    comparison: typing.Literal[
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
    evaluationMissingData: typing.Literal[
        "EVALUATION_MISSING_DATA_UNSPECIFIED",
        "EVALUATION_MISSING_DATA_INACTIVE",
        "EVALUATION_MISSING_DATA_ACTIVE",
        "EVALUATION_MISSING_DATA_NO_OP",
    ]
    filter: str
    forecastOptions: ForecastOptions
    thresholdValue: float
    trigger: Trigger

@typing.type_check_only
class Minutes(typing.TypedDict, total=False):
    periodicity: int

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
class MonitoringQueryLanguageCondition(typing.TypedDict, total=False):
    duration: str
    evaluationMissingData: typing.Literal[
        "EVALUATION_MISSING_DATA_UNSPECIFIED",
        "EVALUATION_MISSING_DATA_INACTIVE",
        "EVALUATION_MISSING_DATA_ACTIVE",
        "EVALUATION_MISSING_DATA_NO_OP",
    ]
    query: str
    trigger: Trigger

@typing.type_check_only
class MutationRecord(typing.TypedDict, total=False):
    mutateTime: str
    mutatedBy: str

@typing.type_check_only
class NotificationChannel(typing.TypedDict, total=False):
    creationRecord: MutationRecord
    description: str
    displayName: str
    enabled: bool
    labels: dict[str, typing.Any]
    mutationRecords: _list[MutationRecord]
    name: str
    type: str
    userLabels: dict[str, typing.Any]
    verificationStatus: typing.Literal[
        "VERIFICATION_STATUS_UNSPECIFIED", "UNVERIFIED", "VERIFIED"
    ]

@typing.type_check_only
class NotificationChannelDescriptor(typing.TypedDict, total=False):
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
    supportedTiers: _list[
        typing.Literal[
            "SERVICE_TIER_UNSPECIFIED", "SERVICE_TIER_BASIC", "SERVICE_TIER_PREMIUM"
        ]
    ]
    type: str

@typing.type_check_only
class NotificationChannelStrategy(typing.TypedDict, total=False):
    notificationChannelNames: _list[str]
    renotifyInterval: str

@typing.type_check_only
class NotificationRateLimit(typing.TypedDict, total=False):
    period: str

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    createTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATED", "RUNNING", "DONE", "CANCELLED"
    ]
    updateTime: str

@typing.type_check_only
class Option(typing.TypedDict, total=False):
    name: str
    value: dict[str, typing.Any]

@typing.type_check_only
class PerformanceThreshold(typing.TypedDict, total=False):
    basicSliPerformance: BasicSli
    performance: RequestBasedSli
    threshold: float

@typing.type_check_only
class PingConfig(typing.TypedDict, total=False):
    pingsCount: int

@typing.type_check_only
class Point(typing.TypedDict, total=False):
    interval: TimeInterval
    value: TypedValue

@typing.type_check_only
class PointData(typing.TypedDict, total=False):
    timeInterval: TimeInterval
    values: _list[TypedValue]

@typing.type_check_only
class PolicySnapshot(typing.TypedDict, total=False):
    displayName: str
    name: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "ERROR", "WARNING"]
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class PrometheusQueryLanguageCondition(typing.TypedDict, total=False):
    alertRule: str
    disableMetricValidation: bool
    duration: str
    evaluationInterval: str
    labels: dict[str, typing.Any]
    query: str
    ruleGroup: str

@typing.type_check_only
class QueryTimeSeriesRequest(typing.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class QueryTimeSeriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    partialErrors: _list[Status]
    timeSeriesData: _list[TimeSeriesData]
    timeSeriesDescriptor: TimeSeriesDescriptor

@typing.type_check_only
class Range(typing.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class RequestBasedSli(typing.TypedDict, total=False):
    distributionCut: DistributionCut
    goodTotalRatio: TimeSeriesRatio

@typing.type_check_only
class ResourceGroup(typing.TypedDict, total=False):
    groupId: str
    resourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "INSTANCE", "AWS_ELB_LOAD_BALANCER"
    ]

@typing.type_check_only
class ResponseStatusCode(typing.TypedDict, total=False):
    statusClass: typing.Literal[
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
class RowCountTest(typing.TypedDict, total=False):
    comparison: typing.Literal[
        "COMPARISON_UNSPECIFIED",
        "COMPARISON_GT",
        "COMPARISON_GE",
        "COMPARISON_LT",
        "COMPARISON_LE",
        "COMPARISON_EQ",
        "COMPARISON_NE",
    ]
    threshold: str

@typing.type_check_only
class SendNotificationChannelVerificationCodeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Service(typing.TypedDict, total=False):
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
class ServiceAgentAuthentication(typing.TypedDict, total=False):
    type: typing.Literal["SERVICE_AGENT_AUTHENTICATION_TYPE_UNSPECIFIED", "OIDC_TOKEN"]

@typing.type_check_only
class ServiceLevelIndicator(typing.TypedDict, total=False):
    basicSli: BasicSli
    requestBased: RequestBasedSli
    windowsBased: WindowsBasedSli

@typing.type_check_only
class ServiceLevelObjective(typing.TypedDict, total=False):
    calendarPeriod: typing.Literal[
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
class Snooze(typing.TypedDict, total=False):
    criteria: Criteria
    displayName: str
    interval: TimeInterval
    name: str

@typing.type_check_only
class SourceContext(typing.TypedDict, total=False):
    fileName: str

@typing.type_check_only
class SpanContext(typing.TypedDict, total=False):
    spanName: str

@typing.type_check_only
class SqlCondition(typing.TypedDict, total=False):
    booleanTest: BooleanTest
    daily: Daily
    hourly: Hourly
    minutes: Minutes
    query: str
    rowCountTest: RowCountTest

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SyntheticMonitorTarget(typing.TypedDict, total=False):
    cloudFunctionV2: CloudFunctionV2Target

@typing.type_check_only
class TcpCheck(typing.TypedDict, total=False):
    pingConfig: PingConfig
    port: int

@typing.type_check_only
class Telemetry(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class TimeInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeSeries(typing.TypedDict, total=False):
    description: str
    metadata: MonitoredResourceMetadata
    metric: Metric
    metricKind: typing.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
    points: _list[Point]
    resource: MonitoredResource
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
class TimeSeriesData(typing.TypedDict, total=False):
    labelValues: _list[LabelValue]
    pointData: _list[PointData]

@typing.type_check_only
class TimeSeriesDescriptor(typing.TypedDict, total=False):
    labelDescriptors: _list[LabelDescriptor]
    pointDescriptors: _list[ValueDescriptor]

@typing.type_check_only
class TimeSeriesRatio(typing.TypedDict, total=False):
    badServiceFilter: str
    goodServiceFilter: str
    totalServiceFilter: str

@typing.type_check_only
class Trigger(typing.TypedDict, total=False):
    count: int
    percent: float

@typing.type_check_only
class Type(typing.TypedDict, total=False):
    edition: str
    fields: _list[Field]
    name: str
    oneofs: _list[str]
    options: _list[Option]
    sourceContext: SourceContext
    syntax: typing.Literal["SYNTAX_PROTO2", "SYNTAX_PROTO3", "SYNTAX_EDITIONS"]

@typing.type_check_only
class TypedValue(typing.TypedDict, total=False):
    boolValue: bool
    distributionValue: Distribution
    doubleValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class UptimeCheckConfig(typing.TypedDict, total=False):
    checkerType: typing.Literal[
        "CHECKER_TYPE_UNSPECIFIED", "STATIC_IP_CHECKERS", "VPC_CHECKERS"
    ]
    contentMatchers: _list[ContentMatcher]
    disabled: bool
    displayName: str
    httpCheck: HttpCheck
    internalCheckers: _list[InternalChecker]
    isInternal: bool
    logCheckFailures: bool
    monitoredResource: MonitoredResource
    name: str
    period: str
    resourceGroup: ResourceGroup
    selectedRegions: _list[
        typing.Literal[
            "REGION_UNSPECIFIED",
            "USA",
            "EUROPE",
            "SOUTH_AMERICA",
            "ASIA_PACIFIC",
            "USA_OREGON",
            "USA_IOWA",
            "USA_VIRGINIA",
        ]
    ]
    syntheticMonitor: SyntheticMonitorTarget
    tcpCheck: TcpCheck
    timeout: str
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class UptimeCheckIp(typing.TypedDict, total=False):
    ipAddress: str
    location: str
    region: typing.Literal[
        "REGION_UNSPECIFIED",
        "USA",
        "EUROPE",
        "SOUTH_AMERICA",
        "ASIA_PACIFIC",
        "USA_OREGON",
        "USA_IOWA",
        "USA_VIRGINIA",
    ]

@typing.type_check_only
class ValueDescriptor(typing.TypedDict, total=False):
    key: str
    metricKind: typing.Literal[
        "METRIC_KIND_UNSPECIFIED", "GAUGE", "DELTA", "CUMULATIVE"
    ]
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
class VerifyNotificationChannelRequest(typing.TypedDict, total=False):
    code: str

@typing.type_check_only
class WindowsBasedSli(typing.TypedDict, total=False):
    goodBadMetricFilter: str
    goodTotalRatioThreshold: PerformanceThreshold
    metricMeanInRange: MetricRange
    metricSumInRange: MetricRange
    windowPeriod: str
