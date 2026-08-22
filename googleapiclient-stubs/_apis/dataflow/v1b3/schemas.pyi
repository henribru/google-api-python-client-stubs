import typing

_list = list

@typing.type_check_only
class ApproximateProgress(typing.TypedDict, total=False):
    percentComplete: float
    position: Position
    remainingTime: str

@typing.type_check_only
class ApproximateReportedProgress(typing.TypedDict, total=False):
    consumedParallelism: ReportedParallelism
    fractionConsumed: float
    position: Position
    remainingParallelism: ReportedParallelism

@typing.type_check_only
class ApproximateSplitRequest(typing.TypedDict, total=False):
    fractionConsumed: float
    fractionOfRemainder: float
    position: Position

@typing.type_check_only
class AutoscalingEvent(typing.TypedDict, total=False):
    currentNumWorkers: str
    description: StructuredMessage
    eventType: typing.Literal[
        "TYPE_UNKNOWN",
        "TARGET_NUM_WORKERS_CHANGED",
        "CURRENT_NUM_WORKERS_CHANGED",
        "ACTUATION_FAILURE",
        "NO_CHANGE",
    ]
    targetNumWorkers: str
    time: str
    workerPool: str

@typing.type_check_only
class AutoscalingSchedule(typing.TypedDict, total=False):
    crontab: str
    duration: str
    name: str
    parameters: Parameters
    priority: str
    timeZone: str
    updateTime: str

@typing.type_check_only
class AutoscalingSettings(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "AUTOSCALING_ALGORITHM_UNKNOWN",
        "AUTOSCALING_ALGORITHM_NONE",
        "AUTOSCALING_ALGORITHM_BASIC",
    ]
    maxNumWorkers: int

@typing.type_check_only
class Base2Exponent(typing.TypedDict, total=False):
    numberOfBuckets: int
    scale: int

@typing.type_check_only
class BigQueryIODetails(typing.TypedDict, total=False):
    dataset: str
    projectId: str
    query: str
    table: str

@typing.type_check_only
class BigTableIODetails(typing.TypedDict, total=False):
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class BoundedTrie(typing.TypedDict, total=False):
    bound: int
    root: BoundedTrieNode
    singleton: _list[str]

@typing.type_check_only
class BoundedTrieNode(typing.TypedDict, total=False):
    children: dict[str, typing.Any]
    truncated: bool

@typing.type_check_only
class BucketOptions(typing.TypedDict, total=False):
    exponential: Base2Exponent
    linear: Linear

@typing.type_check_only
class CPUTime(typing.TypedDict, total=False):
    rate: float
    timestamp: str
    totalMs: str

@typing.type_check_only
class ComponentSource(typing.TypedDict, total=False):
    name: str
    originalTransformOrCollection: str
    userName: str

@typing.type_check_only
class ComponentTransform(typing.TypedDict, total=False):
    name: str
    originalTransform: str
    userName: str

@typing.type_check_only
class ComputationTopology(typing.TypedDict, total=False):
    computationId: str
    inputs: _list[StreamLocation]
    keyRanges: _list[KeyRangeLocation]
    outputs: _list[StreamLocation]
    stateFamilies: _list[StateFamilyConfig]
    systemStageName: str

@typing.type_check_only
class ConcatPosition(typing.TypedDict, total=False):
    index: int
    position: Position

@typing.type_check_only
class ContainerSpec(typing.TypedDict, total=False):
    defaultEnvironment: FlexTemplateRuntimeEnvironment
    image: str
    imageRepositoryCertPath: str
    imageRepositoryPasswordSecretId: str
    imageRepositoryUsernameSecretId: str
    metadata: TemplateMetadata
    sdkInfo: SDKInfo

@typing.type_check_only
class CounterMetadata(typing.TypedDict, total=False):
    description: str
    kind: typing.Literal[
        "INVALID",
        "SUM",
        "MAX",
        "MIN",
        "MEAN",
        "OR",
        "AND",
        "SET",
        "DISTRIBUTION",
        "LATEST_VALUE",
    ]
    otherUnits: str
    standardUnits: typing.Literal[
        "BYTES",
        "BYTES_PER_SEC",
        "MILLISECONDS",
        "MICROSECONDS",
        "NANOSECONDS",
        "TIMESTAMP_MSEC",
        "TIMESTAMP_USEC",
        "TIMESTAMP_NSEC",
    ]

@typing.type_check_only
class CounterStructuredName(typing.TypedDict, total=False):
    componentStepName: str
    executionStepName: str
    inputIndex: int
    name: str
    origin: typing.Literal["SYSTEM", "USER"]
    originNamespace: str
    originalRequestingStepName: str
    originalStepName: str
    portion: typing.Literal["ALL", "KEY", "VALUE"]
    workerId: str

@typing.type_check_only
class CounterStructuredNameAndMetadata(typing.TypedDict, total=False):
    metadata: CounterMetadata
    name: CounterStructuredName

@typing.type_check_only
class CounterUpdate(typing.TypedDict, total=False):
    boolean: bool
    boundedTrie: BoundedTrie
    cumulative: bool
    distribution: DistributionUpdate
    floatingPoint: float
    floatingPointList: FloatingPointList
    floatingPointMean: FloatingPointMean
    integer: SplitInt64
    integerGauge: IntegerGauge
    integerList: IntegerList
    integerMean: IntegerMean
    internal: typing.Any
    nameAndKind: NameAndKind
    shortId: str
    stringList: StringList
    structuredNameAndMetadata: CounterStructuredNameAndMetadata

@typing.type_check_only
class CreateJobFromTemplateRequest(typing.TypedDict, total=False):
    environment: RuntimeEnvironment
    gcsPath: str
    jobName: str
    location: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class CustomSourceLocation(typing.TypedDict, total=False):
    stateful: bool

@typing.type_check_only
class DataDiskAssignment(typing.TypedDict, total=False):
    dataDisks: _list[str]
    vmInstance: str

@typing.type_check_only
class DataSamplingConfig(typing.TypedDict, total=False):
    behaviors: _list[
        typing.Literal[
            "DATA_SAMPLING_BEHAVIOR_UNSPECIFIED", "DISABLED", "ALWAYS_ON", "EXCEPTIONS"
        ]
    ]

@typing.type_check_only
class DataSamplingReport(typing.TypedDict, total=False):
    bytesWrittenDelta: str
    elementsSampledBytes: str
    elementsSampledCount: str
    exceptionsSampledCount: str
    pcollectionsSampledCount: str
    persistenceErrorsCount: str
    translationErrorsCount: str

@typing.type_check_only
class DataflowGaugeValue(typing.TypedDict, total=False):
    measuredTime: str
    value: str

@typing.type_check_only
class DataflowHistogramValue(typing.TypedDict, total=False):
    bucketCounts: _list[str]
    bucketOptions: BucketOptions
    count: str
    outlierStats: OutlierStats

@typing.type_check_only
class DatastoreIODetails(typing.TypedDict, total=False):
    namespace: str
    projectId: str

@typing.type_check_only
class DebugOptions(typing.TypedDict, total=False):
    dataSampling: DataSamplingConfig
    enableHotKeyLogging: bool

@typing.type_check_only
class DeleteSnapshotResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class DerivedSource(typing.TypedDict, total=False):
    derivationMode: typing.Literal[
        "SOURCE_DERIVATION_MODE_UNKNOWN",
        "SOURCE_DERIVATION_MODE_INDEPENDENT",
        "SOURCE_DERIVATION_MODE_CHILD_OF_CURRENT",
        "SOURCE_DERIVATION_MODE_SIBLING_OF_CURRENT",
    ]
    source: Source

@typing.type_check_only
class Disk(typing.TypedDict, total=False):
    diskType: str
    mountPoint: str
    sizeGb: int

@typing.type_check_only
class DisplayData(typing.TypedDict, total=False):
    boolValue: bool
    durationValue: str
    floatValue: float
    int64Value: str
    javaClassValue: str
    key: str
    label: str
    namespace: str
    shortStrValue: str
    strValue: str
    timestampValue: str
    url: str

@typing.type_check_only
class DistributionUpdate(typing.TypedDict, total=False):
    count: SplitInt64
    histogram: Histogram
    max: SplitInt64
    min: SplitInt64
    sum: SplitInt64
    sumOfSquares: float

@typing.type_check_only
class DynamicSourceSplit(typing.TypedDict, total=False):
    primary: DerivedSource
    residual: DerivedSource

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    clusterManagerApiService: str
    dataset: str
    debugOptions: DebugOptions
    experiments: _list[str]
    flexResourceSchedulingGoal: typing.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    internalExperiments: dict[str, typing.Any]
    sdkPipelineOptions: dict[str, typing.Any]
    serviceAccountEmail: str
    serviceKmsKeyName: str
    serviceOptions: _list[str]
    shuffleMode: typing.Literal["SHUFFLE_MODE_UNSPECIFIED", "VM_BASED", "SERVICE_BASED"]
    streamingMode: typing.Literal[
        "STREAMING_MODE_UNSPECIFIED",
        "STREAMING_MODE_EXACTLY_ONCE",
        "STREAMING_MODE_AT_LEAST_ONCE",
    ]
    tempStoragePrefix: str
    usePublicIps: bool
    useStreamingEngineResourceBasedBilling: bool
    userAgent: dict[str, typing.Any]
    version: dict[str, typing.Any]
    workerPools: _list[WorkerPool]
    workerRegion: str
    workerZone: str

@typing.type_check_only
class ExecutionStageState(typing.TypedDict, total=False):
    currentStateTime: str
    executionStageName: str
    executionStageState: typing.Literal[
        "JOB_STATE_UNKNOWN",
        "JOB_STATE_STOPPED",
        "JOB_STATE_RUNNING",
        "JOB_STATE_DONE",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_UPDATED",
        "JOB_STATE_DRAINING",
        "JOB_STATE_DRAINED",
        "JOB_STATE_PENDING",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_QUEUED",
        "JOB_STATE_RESOURCE_CLEANING_UP",
        "JOB_STATE_PAUSING",
        "JOB_STATE_PAUSED",
    ]

@typing.type_check_only
class ExecutionStageSummary(typing.TypedDict, total=False):
    componentSource: _list[ComponentSource]
    componentTransform: _list[ComponentTransform]
    id: str
    inputSource: _list[StageSource]
    kind: typing.Literal[
        "UNKNOWN_KIND",
        "PAR_DO_KIND",
        "GROUP_BY_KEY_KIND",
        "FLATTEN_KIND",
        "READ_KIND",
        "WRITE_KIND",
        "CONSTANT_KIND",
        "SINGLETON_KIND",
        "SHUFFLE_KIND",
    ]
    name: str
    outputSource: _list[StageSource]
    prerequisiteStage: _list[str]

@typing.type_check_only
class FailedLocation(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class FileIODetails(typing.TypedDict, total=False):
    filePattern: str

@typing.type_check_only
class FlattenInstruction(typing.TypedDict, total=False):
    inputs: _list[InstructionInput]

@typing.type_check_only
class FlexTemplateRuntimeEnvironment(typing.TypedDict, total=False):
    additionalExperiments: _list[str]
    additionalPipelineOptions: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    autoscalingAlgorithm: typing.Literal[
        "AUTOSCALING_ALGORITHM_UNKNOWN",
        "AUTOSCALING_ALGORITHM_NONE",
        "AUTOSCALING_ALGORITHM_BASIC",
    ]
    diskSizeGb: int
    dumpHeapOnOom: bool
    enableLauncherVmSerialPortLogging: bool
    enableStreamingEngine: bool
    flexrsGoal: typing.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    ipConfiguration: typing.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    kmsKeyName: str
    launcherMachineType: str
    machineType: str
    maxWorkers: int
    network: str
    numWorkers: int
    saveHeapDumpsToGcsPath: str
    sdkContainerImage: str
    serviceAccountEmail: str
    stagingLocation: str
    streamingMode: typing.Literal[
        "STREAMING_MODE_UNSPECIFIED",
        "STREAMING_MODE_EXACTLY_ONCE",
        "STREAMING_MODE_AT_LEAST_ONCE",
    ]
    subnetwork: str
    tempLocation: str
    workerRegion: str
    workerZone: str
    zone: str

@typing.type_check_only
class FloatingPointList(typing.TypedDict, total=False):
    elements: _list[float]

@typing.type_check_only
class FloatingPointMean(typing.TypedDict, total=False):
    count: SplitInt64
    sum: float

@typing.type_check_only
class GPUUsage(typing.TypedDict, total=False):
    timestamp: str
    utilization: GPUUtilization

@typing.type_check_only
class GPUUtilization(typing.TypedDict, total=False):
    rate: float

@typing.type_check_only
class GetDebugConfigRequest(typing.TypedDict, total=False):
    componentId: str
    location: str
    workerId: str

@typing.type_check_only
class GetDebugConfigResponse(typing.TypedDict, total=False):
    config: str

@typing.type_check_only
class GetTemplateResponse(typing.TypedDict, total=False):
    metadata: TemplateMetadata
    runtimeMetadata: RuntimeMetadata
    status: Status
    templateType: typing.Literal["UNKNOWN", "LEGACY", "FLEX"]

@typing.type_check_only
class GetWorkerStacktracesRequest(typing.TypedDict, total=False):
    endTime: str
    workerId: str

@typing.type_check_only
class GetWorkerStacktracesResponse(typing.TypedDict, total=False):
    sdks: _list[Sdk]

@typing.type_check_only
class Histogram(typing.TypedDict, total=False):
    bucketCounts: _list[str]
    firstBucketOffset: int

@typing.type_check_only
class HotKeyDebuggingInfo(typing.TypedDict, total=False):
    detectedHotKeys: dict[str, typing.Any]

@typing.type_check_only
class HotKeyDetection(typing.TypedDict, total=False):
    hotKeyAge: str
    systemName: str
    userStepName: str

@typing.type_check_only
class HotKeyInfo(typing.TypedDict, total=False):
    hotKeyAge: str
    key: str
    keyTruncated: bool

@typing.type_check_only
class InstructionInput(typing.TypedDict, total=False):
    outputNum: int
    producerInstructionIndex: int

@typing.type_check_only
class InstructionOutput(typing.TypedDict, total=False):
    codec: dict[str, typing.Any]
    name: str
    onlyCountKeyBytes: bool
    onlyCountValueBytes: bool
    originalName: str
    systemName: str

@typing.type_check_only
class IntegerGauge(typing.TypedDict, total=False):
    timestamp: str
    value: SplitInt64

@typing.type_check_only
class IntegerList(typing.TypedDict, total=False):
    elements: _list[SplitInt64]

@typing.type_check_only
class IntegerMean(typing.TypedDict, total=False):
    count: SplitInt64
    sum: SplitInt64

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    clientRequestId: str
    createTime: str
    createdFromSnapshotId: str
    currentState: typing.Literal[
        "JOB_STATE_UNKNOWN",
        "JOB_STATE_STOPPED",
        "JOB_STATE_RUNNING",
        "JOB_STATE_DONE",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_UPDATED",
        "JOB_STATE_DRAINING",
        "JOB_STATE_DRAINED",
        "JOB_STATE_PENDING",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_QUEUED",
        "JOB_STATE_RESOURCE_CLEANING_UP",
        "JOB_STATE_PAUSING",
        "JOB_STATE_PAUSED",
    ]
    currentStateTime: str
    environment: Environment
    executionInfo: JobExecutionInfo
    id: str
    jobMetadata: JobMetadata
    labels: dict[str, typing.Any]
    location: str
    name: str
    pausable: bool
    pipelineDescription: PipelineDescription
    projectId: str
    replaceJobId: str
    replacedByJobId: str
    requestedState: typing.Literal[
        "JOB_STATE_UNKNOWN",
        "JOB_STATE_STOPPED",
        "JOB_STATE_RUNNING",
        "JOB_STATE_DONE",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_UPDATED",
        "JOB_STATE_DRAINING",
        "JOB_STATE_DRAINED",
        "JOB_STATE_PENDING",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_QUEUED",
        "JOB_STATE_RESOURCE_CLEANING_UP",
        "JOB_STATE_PAUSING",
        "JOB_STATE_PAUSED",
    ]
    runtimeUpdatableParams: RuntimeUpdatableParams
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceResources: ServiceResources
    stageStates: _list[ExecutionStageState]
    startTime: str
    steps: _list[Step]
    stepsLocation: str
    tempFiles: _list[str]
    transformNameMapping: dict[str, typing.Any]
    type: typing.Literal["JOB_TYPE_UNKNOWN", "JOB_TYPE_BATCH", "JOB_TYPE_STREAMING"]

@typing.type_check_only
class JobExecutionDetails(typing.TypedDict, total=False):
    nextPageToken: str
    stages: _list[StageSummary]

@typing.type_check_only
class JobExecutionInfo(typing.TypedDict, total=False):
    stages: dict[str, typing.Any]

@typing.type_check_only
class JobExecutionStageInfo(typing.TypedDict, total=False):
    stepName: _list[str]

@typing.type_check_only
class JobMessage(typing.TypedDict, total=False):
    id: str
    messageImportance: typing.Literal[
        "JOB_MESSAGE_IMPORTANCE_UNKNOWN",
        "JOB_MESSAGE_DEBUG",
        "JOB_MESSAGE_DETAILED",
        "JOB_MESSAGE_BASIC",
        "JOB_MESSAGE_WARNING",
        "JOB_MESSAGE_ERROR",
    ]
    messageText: str
    time: str

@typing.type_check_only
class JobMetadata(typing.TypedDict, total=False):
    bigTableDetails: _list[BigTableIODetails]
    bigqueryDetails: _list[BigQueryIODetails]
    datastoreDetails: _list[DatastoreIODetails]
    fileDetails: _list[FileIODetails]
    pubsubDetails: _list[PubSubIODetails]
    sdkVersion: SdkVersion
    spannerDetails: _list[SpannerIODetails]
    userDisplayProperties: dict[str, typing.Any]

@typing.type_check_only
class JobMetrics(typing.TypedDict, total=False):
    metricTime: str
    metrics: _list[MetricUpdate]

@typing.type_check_only
class KeyRangeDataDiskAssignment(typing.TypedDict, total=False):
    dataDisk: str
    end: str
    start: str

@typing.type_check_only
class KeyRangeLocation(typing.TypedDict, total=False):
    dataDisk: str
    deliveryEndpoint: str
    deprecatedPersistentDirectory: str
    end: str
    start: str

@typing.type_check_only
class LaunchFlexTemplateParameter(typing.TypedDict, total=False):
    containerSpec: ContainerSpec
    containerSpecGcsPath: str
    environment: FlexTemplateRuntimeEnvironment
    jobName: str
    launchOptions: dict[str, typing.Any]
    parameters: dict[str, typing.Any]
    transformNameMappings: dict[str, typing.Any]
    update: bool

@typing.type_check_only
class LaunchFlexTemplateRequest(typing.TypedDict, total=False):
    launchParameter: LaunchFlexTemplateParameter
    validateOnly: bool

@typing.type_check_only
class LaunchFlexTemplateResponse(typing.TypedDict, total=False):
    job: Job

@typing.type_check_only
class LaunchTemplateParameters(typing.TypedDict, total=False):
    environment: RuntimeEnvironment
    jobName: str
    parameters: dict[str, typing.Any]
    transformNameMapping: dict[str, typing.Any]
    update: bool

@typing.type_check_only
class LaunchTemplateResponse(typing.TypedDict, total=False):
    job: Job

@typing.type_check_only
class LeaseWorkItemRequest(typing.TypedDict, total=False):
    currentWorkerTime: str
    location: str
    projectNumber: str
    requestedLeaseDuration: str
    unifiedWorkerRequest: dict[str, typing.Any]
    workItemTypes: _list[str]
    workerCapabilities: _list[str]
    workerId: str

@typing.type_check_only
class LeaseWorkItemResponse(typing.TypedDict, total=False):
    unifiedWorkerResponse: dict[str, typing.Any]
    workItems: _list[WorkItem]

@typing.type_check_only
class Linear(typing.TypedDict, total=False):
    numberOfBuckets: int
    start: float
    width: float

@typing.type_check_only
class ListJobMessagesResponse(typing.TypedDict, total=False):
    autoscalingEvents: _list[AutoscalingEvent]
    jobMessages: _list[JobMessage]
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    failedLocation: _list[FailedLocation]
    jobs: _list[Job]
    nextPageToken: str

@typing.type_check_only
class ListSnapshotsResponse(typing.TypedDict, total=False):
    snapshots: _list[Snapshot]

@typing.type_check_only
class MapTask(typing.TypedDict, total=False):
    counterPrefix: str
    instructions: _list[ParallelInstruction]
    stageName: str
    systemName: str

@typing.type_check_only
class MemInfo(typing.TypedDict, total=False):
    currentLimitBytes: str
    currentOoms: str
    currentRssBytes: str
    timestamp: str
    totalGbMs: str

@typing.type_check_only
class MetricShortId(typing.TypedDict, total=False):
    metricIndex: int
    shortId: str

@typing.type_check_only
class MetricStructuredName(typing.TypedDict, total=False):
    context: dict[str, typing.Any]
    name: str
    origin: str

@typing.type_check_only
class MetricUpdate(typing.TypedDict, total=False):
    boundedTrie: typing.Any
    cumulative: bool
    distribution: typing.Any
    gauge: typing.Any
    internal: typing.Any
    kind: str
    meanCount: typing.Any
    meanSum: typing.Any
    name: MetricStructuredName
    scalar: typing.Any
    set: typing.Any
    trie: typing.Any
    updateTime: str

@typing.type_check_only
class MetricValue(typing.TypedDict, total=False):
    metric: str
    metricLabels: dict[str, typing.Any]
    valueGauge64: DataflowGaugeValue
    valueHistogram: DataflowHistogramValue
    valueInt64: str

@typing.type_check_only
class MountedDataDisk(typing.TypedDict, total=False):
    dataDisk: str

@typing.type_check_only
class MultiOutputInfo(typing.TypedDict, total=False):
    tag: str

@typing.type_check_only
class NameAndKind(typing.TypedDict, total=False):
    kind: typing.Literal[
        "INVALID",
        "SUM",
        "MAX",
        "MIN",
        "MEAN",
        "OR",
        "AND",
        "SET",
        "DISTRIBUTION",
        "LATEST_VALUE",
    ]
    name: str

@typing.type_check_only
class OutlierStats(typing.TypedDict, total=False):
    overflowCount: str
    overflowMean: float
    underflowCount: str
    underflowMean: float

@typing.type_check_only
class Package(typing.TypedDict, total=False):
    location: str
    name: str
    sha256: str

@typing.type_check_only
class ParDoInstruction(typing.TypedDict, total=False):
    input: InstructionInput
    multiOutputInfos: _list[MultiOutputInfo]
    numOutputs: int
    sideInputs: _list[SideInputInfo]
    userFn: dict[str, typing.Any]

@typing.type_check_only
class ParallelInstruction(typing.TypedDict, total=False):
    flatten: FlattenInstruction
    name: str
    originalName: str
    outputs: _list[InstructionOutput]
    parDo: ParDoInstruction
    partialGroupByKey: PartialGroupByKeyInstruction
    read: ReadInstruction
    systemName: str
    write: WriteInstruction

@typing.type_check_only
class Parameter(typing.TypedDict, total=False):
    key: str
    value: typing.Any

@typing.type_check_only
class ParameterMetadata(typing.TypedDict, total=False):
    customMetadata: dict[str, typing.Any]
    defaultValue: str
    enumOptions: _list[ParameterMetadataEnumOption]
    groupName: str
    helpText: str
    hiddenUi: bool
    isOptional: bool
    label: str
    name: str
    paramType: typing.Literal[
        "DEFAULT",
        "TEXT",
        "GCS_READ_BUCKET",
        "GCS_WRITE_BUCKET",
        "GCS_READ_FILE",
        "GCS_WRITE_FILE",
        "GCS_READ_FOLDER",
        "GCS_WRITE_FOLDER",
        "PUBSUB_TOPIC",
        "PUBSUB_SUBSCRIPTION",
        "BIGQUERY_TABLE",
        "JAVASCRIPT_UDF_FILE",
        "SERVICE_ACCOUNT",
        "MACHINE_TYPE",
        "KMS_KEY_NAME",
        "WORKER_REGION",
        "WORKER_ZONE",
        "BOOLEAN",
        "ENUM",
        "NUMBER",
        "KAFKA_TOPIC",
        "KAFKA_READ_TOPIC",
        "KAFKA_WRITE_TOPIC",
    ]
    parentName: str
    parentTriggerValues: _list[str]
    regexes: _list[str]

@typing.type_check_only
class ParameterMetadataEnumOption(typing.TypedDict, total=False):
    description: str
    label: str
    value: str

@typing.type_check_only
class Parameters(typing.TypedDict, total=False):
    cpuUtilizationTarget: float
    latencyTarget: str
    maxWorkerCount: int
    minWorkerCount: int

@typing.type_check_only
class PartialGroupByKeyInstruction(typing.TypedDict, total=False):
    input: InstructionInput
    inputElementCodec: dict[str, typing.Any]
    originalCombineValuesInputStoreName: str
    originalCombineValuesStepName: str
    sideInputs: _list[SideInputInfo]
    valueCombiningFn: dict[str, typing.Any]

@typing.type_check_only
class PerStepNamespaceMetrics(typing.TypedDict, total=False):
    metricValues: _list[MetricValue]
    metricsNamespace: str
    originalStep: str

@typing.type_check_only
class PerWorkerMetrics(typing.TypedDict, total=False):
    perStepNamespaceMetrics: _list[PerStepNamespaceMetrics]

@typing.type_check_only
class PipelineDescription(typing.TypedDict, total=False):
    displayData: _list[DisplayData]
    executionPipelineStage: _list[ExecutionStageSummary]
    originalPipelineTransform: _list[TransformSummary]
    stepNamesHash: str

@typing.type_check_only
class Point(typing.TypedDict, total=False):
    time: str
    value: float

@typing.type_check_only
class Position(typing.TypedDict, total=False):
    byteOffset: str
    concatPosition: ConcatPosition
    end: bool
    key: str
    recordIndex: str
    shufflePosition: str

@typing.type_check_only
class ProgressTimeseries(typing.TypedDict, total=False):
    currentProgress: float
    dataPoints: _list[Point]

@typing.type_check_only
class PubSubIODetails(typing.TypedDict, total=False):
    subscription: str
    topic: str

@typing.type_check_only
class PubsubLocation(typing.TypedDict, total=False):
    dropLateData: bool
    dynamicDestinations: bool
    idLabel: str
    subscription: str
    timestampLabel: str
    topic: str
    trackingSubscription: str
    withAttributes: bool

@typing.type_check_only
class PubsubSnapshotMetadata(typing.TypedDict, total=False):
    expireTime: str
    snapshotName: str
    topicName: str

@typing.type_check_only
class ReadInstruction(typing.TypedDict, total=False):
    source: Source

@typing.type_check_only
class ReportWorkItemStatusRequest(typing.TypedDict, total=False):
    currentWorkerTime: str
    location: str
    projectNumber: str
    unifiedWorkerRequest: dict[str, typing.Any]
    workItemStatuses: _list[WorkItemStatus]
    workerId: str

@typing.type_check_only
class ReportWorkItemStatusResponse(typing.TypedDict, total=False):
    unifiedWorkerResponse: dict[str, typing.Any]
    workItemServiceStates: _list[WorkItemServiceState]

@typing.type_check_only
class ReportedParallelism(typing.TypedDict, total=False):
    isInfinite: bool
    value: float

@typing.type_check_only
class ResourceUtilizationReport(typing.TypedDict, total=False):
    containers: dict[str, typing.Any]
    cpuTime: _list[CPUTime]
    gpuUsage: _list[GPUUsage]
    memoryInfo: _list[MemInfo]

@typing.type_check_only
class ResourceUtilizationReportResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RuntimeEnvironment(typing.TypedDict, total=False):
    additionalExperiments: _list[str]
    additionalPipelineOptions: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    bypassTempDirValidation: bool
    diskSizeGb: int
    enableStreamingEngine: bool
    ipConfiguration: typing.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    kmsKeyName: str
    machineType: str
    maxWorkers: int
    network: str
    numWorkers: int
    serviceAccountEmail: str
    streamingMode: typing.Literal[
        "STREAMING_MODE_UNSPECIFIED",
        "STREAMING_MODE_EXACTLY_ONCE",
        "STREAMING_MODE_AT_LEAST_ONCE",
    ]
    subnetwork: str
    tempLocation: str
    workerRegion: str
    workerZone: str
    zone: str

@typing.type_check_only
class RuntimeMetadata(typing.TypedDict, total=False):
    parameters: _list[ParameterMetadata]
    sdkInfo: SDKInfo

@typing.type_check_only
class RuntimeUpdatableParams(typing.TypedDict, total=False):
    acceptableBacklogDuration: str
    autoscalingTier: str
    latencyTier: str
    maxNumWorkers: int
    minNumWorkers: int
    schedules: _list[AutoscalingSchedule]
    workerUtilizationHint: float

@typing.type_check_only
class SDKInfo(typing.TypedDict, total=False):
    language: typing.Literal["UNKNOWN", "JAVA", "PYTHON", "GO", "YAML"]
    version: str

@typing.type_check_only
class Sdk(typing.TypedDict, total=False):
    sdkId: str
    stacks: _list[Stack]

@typing.type_check_only
class SdkBug(typing.TypedDict, total=False):
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "NOTICE", "WARNING", "SEVERE"]
    type: typing.Literal["TYPE_UNSPECIFIED", "GENERAL", "PERFORMANCE", "DATALOSS"]
    uri: str

@typing.type_check_only
class SdkHarnessContainerImage(typing.TypedDict, total=False):
    capabilities: _list[str]
    containerImage: str
    environmentId: str
    useSingleCorePerContainer: bool

@typing.type_check_only
class SdkVersion(typing.TypedDict, total=False):
    bugs: _list[SdkBug]
    sdkSupportStatus: typing.Literal[
        "UNKNOWN", "SUPPORTED", "STALE", "DEPRECATED", "UNSUPPORTED"
    ]
    version: str
    versionDisplayName: str

@typing.type_check_only
class SendDebugCaptureRequest(typing.TypedDict, total=False):
    componentId: str
    data: str
    dataFormat: typing.Literal[
        "DATA_FORMAT_UNSPECIFIED", "RAW", "JSON", "ZLIB", "BROTLI"
    ]
    location: str
    workerId: str

@typing.type_check_only
class SendDebugCaptureResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class SendWorkerMessagesRequest(typing.TypedDict, total=False):
    location: str
    workerMessages: _list[WorkerMessage]

@typing.type_check_only
class SendWorkerMessagesResponse(typing.TypedDict, total=False):
    workerMessageResponses: _list[WorkerMessageResponse]

@typing.type_check_only
class SeqMapTask(typing.TypedDict, total=False):
    inputs: _list[SideInputInfo]
    name: str
    outputInfos: _list[SeqMapTaskOutputInfo]
    stageName: str
    systemName: str
    userFn: dict[str, typing.Any]

@typing.type_check_only
class SeqMapTaskOutputInfo(typing.TypedDict, total=False):
    sink: Sink
    tag: str

@typing.type_check_only
class ServiceResources(typing.TypedDict, total=False):
    zones: _list[str]

@typing.type_check_only
class ShellTask(typing.TypedDict, total=False):
    command: str
    exitCode: int

@typing.type_check_only
class SideInputInfo(typing.TypedDict, total=False):
    kind: dict[str, typing.Any]
    sources: _list[Source]
    tag: str

@typing.type_check_only
class Sink(typing.TypedDict, total=False):
    codec: dict[str, typing.Any]
    spec: dict[str, typing.Any]

@typing.type_check_only
class Snapshot(typing.TypedDict, total=False):
    creationTime: str
    description: str
    diskSizeBytes: str
    id: str
    projectId: str
    pubsubMetadata: _list[PubsubSnapshotMetadata]
    region: str
    sourceJobId: str
    state: typing.Literal[
        "UNKNOWN_SNAPSHOT_STATE", "PENDING", "RUNNING", "READY", "FAILED", "DELETED"
    ]
    ttl: str

@typing.type_check_only
class SnapshotJobRequest(typing.TypedDict, total=False):
    description: str
    location: str
    snapshotSources: bool
    ttl: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    baseSpecs: _list[dict[str, typing.Any]]
    codec: dict[str, typing.Any]
    doesNotNeedSplitting: bool
    metadata: SourceMetadata
    spec: dict[str, typing.Any]

@typing.type_check_only
class SourceFork(typing.TypedDict, total=False):
    primary: SourceSplitShard
    primarySource: DerivedSource
    residual: SourceSplitShard
    residualSource: DerivedSource

@typing.type_check_only
class SourceGetMetadataRequest(typing.TypedDict, total=False):
    source: Source

@typing.type_check_only
class SourceGetMetadataResponse(typing.TypedDict, total=False):
    metadata: SourceMetadata

@typing.type_check_only
class SourceMetadata(typing.TypedDict, total=False):
    estimatedSizeBytes: str
    infinite: bool
    producesSortedKeys: bool

@typing.type_check_only
class SourceOperationRequest(typing.TypedDict, total=False):
    getMetadata: SourceGetMetadataRequest
    name: str
    originalName: str
    split: SourceSplitRequest
    stageName: str
    systemName: str

@typing.type_check_only
class SourceOperationResponse(typing.TypedDict, total=False):
    getMetadata: SourceGetMetadataResponse
    split: SourceSplitResponse

@typing.type_check_only
class SourceSplitOptions(typing.TypedDict, total=False):
    desiredBundleSizeBytes: str
    desiredShardSizeBytes: str

@typing.type_check_only
class SourceSplitRequest(typing.TypedDict, total=False):
    options: SourceSplitOptions
    source: Source

@typing.type_check_only
class SourceSplitResponse(typing.TypedDict, total=False):
    bundles: _list[DerivedSource]
    outcome: typing.Literal[
        "SOURCE_SPLIT_OUTCOME_UNKNOWN",
        "SOURCE_SPLIT_OUTCOME_USE_CURRENT",
        "SOURCE_SPLIT_OUTCOME_SPLITTING_HAPPENED",
    ]
    shards: _list[SourceSplitShard]

@typing.type_check_only
class SourceSplitShard(typing.TypedDict, total=False):
    derivationMode: typing.Literal[
        "SOURCE_DERIVATION_MODE_UNKNOWN",
        "SOURCE_DERIVATION_MODE_INDEPENDENT",
        "SOURCE_DERIVATION_MODE_CHILD_OF_CURRENT",
        "SOURCE_DERIVATION_MODE_SIBLING_OF_CURRENT",
    ]
    source: Source

@typing.type_check_only
class SpannerIODetails(typing.TypedDict, total=False):
    databaseId: str
    instanceId: str
    projectId: str

@typing.type_check_only
class SplitInt64(typing.TypedDict, total=False):
    highBits: int
    lowBits: int

@typing.type_check_only
class Stack(typing.TypedDict, total=False):
    stackContent: str
    threadCount: int
    threadName: str
    threadState: str
    timestamp: str

@typing.type_check_only
class StageExecutionDetails(typing.TypedDict, total=False):
    nextPageToken: str
    workers: _list[WorkerDetails]

@typing.type_check_only
class StageSource(typing.TypedDict, total=False):
    name: str
    originalTransformOrCollection: str
    sizeBytes: str
    userName: str

@typing.type_check_only
class StageSummary(typing.TypedDict, total=False):
    endTime: str
    metrics: _list[MetricUpdate]
    progress: ProgressTimeseries
    stageId: str
    startTime: str
    state: typing.Literal[
        "EXECUTION_STATE_UNKNOWN",
        "EXECUTION_STATE_NOT_STARTED",
        "EXECUTION_STATE_RUNNING",
        "EXECUTION_STATE_SUCCEEDED",
        "EXECUTION_STATE_FAILED",
        "EXECUTION_STATE_CANCELLED",
    ]
    stragglerSummary: StragglerSummary

@typing.type_check_only
class StateFamilyConfig(typing.TypedDict, total=False):
    isRead: bool
    stateFamily: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing.TypedDict, total=False):
    kind: str
    name: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class Straggler(typing.TypedDict, total=False):
    batchStraggler: StragglerInfo
    streamingStraggler: StreamingStragglerInfo

@typing.type_check_only
class StragglerDebuggingInfo(typing.TypedDict, total=False):
    hotKey: HotKeyDebuggingInfo

@typing.type_check_only
class StragglerInfo(typing.TypedDict, total=False):
    causes: dict[str, typing.Any]
    startTime: str

@typing.type_check_only
class StragglerSummary(typing.TypedDict, total=False):
    recentStragglers: _list[Straggler]
    stragglerCauseCount: dict[str, typing.Any]
    totalStragglerCount: str

@typing.type_check_only
class StreamLocation(typing.TypedDict, total=False):
    customSourceLocation: CustomSourceLocation
    pubsubLocation: PubsubLocation
    sideInputLocation: StreamingSideInputLocation
    streamingStageLocation: StreamingStageLocation

@typing.type_check_only
class StreamingApplianceSnapshotConfig(typing.TypedDict, total=False):
    importStateEndpoint: str
    snapshotId: str

@typing.type_check_only
class StreamingComputationConfig(typing.TypedDict, total=False):
    computationId: str
    instructions: _list[ParallelInstruction]
    stageName: str
    systemName: str
    transformUserNameToStateFamily: dict[str, typing.Any]

@typing.type_check_only
class StreamingComputationRanges(typing.TypedDict, total=False):
    computationId: str
    rangeAssignments: _list[KeyRangeDataDiskAssignment]

@typing.type_check_only
class StreamingComputationTask(typing.TypedDict, total=False):
    computationRanges: _list[StreamingComputationRanges]
    dataDisks: _list[MountedDataDisk]
    taskType: typing.Literal[
        "STREAMING_COMPUTATION_TASK_UNKNOWN",
        "STREAMING_COMPUTATION_TASK_STOP",
        "STREAMING_COMPUTATION_TASK_START",
    ]

@typing.type_check_only
class StreamingConfigTask(typing.TypedDict, total=False):
    commitStreamChunkSizeBytes: str
    getDataStreamChunkSizeBytes: str
    maxWorkItemCommitBytes: str
    operationalLimits: StreamingOperationalLimits
    streamingComputationConfigs: _list[StreamingComputationConfig]
    streamingEngineStateTagEncodingVersion: int
    userStepToStateFamilyNameMap: dict[str, typing.Any]
    userWorkerRunnerV1Settings: str
    userWorkerRunnerV2Settings: str
    windmillServiceEndpoint: str
    windmillServicePort: str

@typing.type_check_only
class StreamingOperationalLimits(typing.TypedDict, total=False):
    maxBagElementBytes: str
    maxGlobalDataBytes: str
    maxKeyBytes: str
    maxProductionOutputBytes: str
    maxSortedListElementBytes: str
    maxSourceStateBytes: str
    maxTagBytes: str
    maxValueBytes: str

@typing.type_check_only
class StreamingScalingReport(typing.TypedDict, total=False):
    activeBundleCount: int
    activeThreadCount: int
    maximumBundleCount: int
    maximumBytes: str
    maximumBytesCount: int
    maximumThreadCount: int
    outstandingBundleCount: int
    outstandingBytes: str
    outstandingBytesCount: int

@typing.type_check_only
class StreamingScalingReportResponse(typing.TypedDict, total=False):
    maximumThreadCount: int

@typing.type_check_only
class StreamingSetupTask(typing.TypedDict, total=False):
    drain: bool
    receiveWorkPort: int
    snapshotConfig: StreamingApplianceSnapshotConfig
    streamingComputationTopology: TopologyConfig
    workerHarnessPort: int

@typing.type_check_only
class StreamingSideInputLocation(typing.TypedDict, total=False):
    stateFamily: str
    tag: str

@typing.type_check_only
class StreamingStageLocation(typing.TypedDict, total=False):
    streamId: str

@typing.type_check_only
class StreamingStragglerInfo(typing.TypedDict, total=False):
    dataWatermarkLag: str
    endTime: str
    startTime: str
    systemWatermarkLag: str
    workerName: str

@typing.type_check_only
class StringList(typing.TypedDict, total=False):
    elements: _list[str]

@typing.type_check_only
class StructuredMessage(typing.TypedDict, total=False):
    messageKey: str
    messageText: str
    parameters: _list[Parameter]

@typing.type_check_only
class TaskRunnerSettings(typing.TypedDict, total=False):
    alsologtostderr: bool
    baseTaskDir: str
    baseUrl: str
    commandlinesFileName: str
    continueOnException: bool
    dataflowApiVersion: str
    harnessCommand: str
    languageHint: str
    logDir: str
    logToSerialconsole: bool
    logUploadLocation: str
    oauthScopes: _list[str]
    parallelWorkerSettings: WorkerSettings
    streamingWorkerMainClass: str
    taskGroup: str
    taskUser: str
    tempStoragePrefix: str
    vmId: str
    workflowFileName: str

@typing.type_check_only
class TemplateMetadata(typing.TypedDict, total=False):
    defaultStreamingMode: str
    description: str
    name: str
    parameters: _list[ParameterMetadata]
    streaming: bool
    supportsAtLeastOnce: bool
    supportsExactlyOnce: bool
    yamlDefinition: str

@typing.type_check_only
class TopologyConfig(typing.TypedDict, total=False):
    computations: _list[ComputationTopology]
    dataDiskAssignments: _list[DataDiskAssignment]
    forwardingKeyBits: int
    persistentStateVersion: int
    userStageToComputationNameMap: dict[str, typing.Any]

@typing.type_check_only
class TransformSummary(typing.TypedDict, total=False):
    displayData: _list[DisplayData]
    id: str
    inputCollectionName: _list[str]
    kind: typing.Literal[
        "UNKNOWN_KIND",
        "PAR_DO_KIND",
        "GROUP_BY_KEY_KIND",
        "FLATTEN_KIND",
        "READ_KIND",
        "WRITE_KIND",
        "CONSTANT_KIND",
        "SINGLETON_KIND",
        "SHUFFLE_KIND",
    ]
    name: str
    outputCollectionName: _list[str]

@typing.type_check_only
class WorkItem(typing.TypedDict, total=False):
    configuration: str
    id: str
    initialReportIndex: str
    jobId: str
    leaseExpireTime: str
    mapTask: MapTask
    packages: _list[Package]
    projectId: str
    reportStatusInterval: str
    seqMapTask: SeqMapTask
    shellTask: ShellTask
    sourceOperationTask: SourceOperationRequest
    streamingComputationTask: StreamingComputationTask
    streamingConfigTask: StreamingConfigTask
    streamingSetupTask: StreamingSetupTask

@typing.type_check_only
class WorkItemDetails(typing.TypedDict, total=False):
    attemptId: str
    endTime: str
    metrics: _list[MetricUpdate]
    progress: ProgressTimeseries
    startTime: str
    state: typing.Literal[
        "EXECUTION_STATE_UNKNOWN",
        "EXECUTION_STATE_NOT_STARTED",
        "EXECUTION_STATE_RUNNING",
        "EXECUTION_STATE_SUCCEEDED",
        "EXECUTION_STATE_FAILED",
        "EXECUTION_STATE_CANCELLED",
    ]
    stragglerInfo: StragglerInfo
    taskId: str

@typing.type_check_only
class WorkItemServiceState(typing.TypedDict, total=False):
    completeWorkStatus: Status
    harnessData: dict[str, typing.Any]
    hotKeyDetection: HotKeyDetection
    leaseExpireTime: str
    metricShortId: _list[MetricShortId]
    nextReportIndex: str
    reportStatusInterval: str
    splitRequest: ApproximateSplitRequest
    suggestedStopPoint: ApproximateProgress
    suggestedStopPosition: Position

@typing.type_check_only
class WorkItemStatus(typing.TypedDict, total=False):
    completed: bool
    counterUpdates: _list[CounterUpdate]
    dynamicSourceSplit: DynamicSourceSplit
    errors: _list[Status]
    metricUpdates: _list[MetricUpdate]
    progress: ApproximateProgress
    reportIndex: str
    reportedProgress: ApproximateReportedProgress
    requestedLeaseDuration: str
    sourceFork: SourceFork
    sourceOperationResponse: SourceOperationResponse
    stopPosition: Position
    totalThrottlerWaitTimeSeconds: float
    workItemId: str

@typing.type_check_only
class WorkerDetails(typing.TypedDict, total=False):
    workItems: _list[WorkItemDetails]
    workerName: str

@typing.type_check_only
class WorkerHealthReport(typing.TypedDict, total=False):
    msg: str
    pods: _list[dict[str, typing.Any]]
    reportInterval: str
    vmBrokenCode: str
    vmIsBroken: bool
    vmIsHealthy: bool
    vmStartupTime: str

@typing.type_check_only
class WorkerHealthReportResponse(typing.TypedDict, total=False):
    reportInterval: str

@typing.type_check_only
class WorkerLifecycleEvent(typing.TypedDict, total=False):
    containerStartTime: str
    event: typing.Literal[
        "UNKNOWN_EVENT",
        "OS_START",
        "CONTAINER_START",
        "NETWORK_UP",
        "STAGING_FILES_DOWNLOAD_START",
        "STAGING_FILES_DOWNLOAD_FINISH",
        "SDK_INSTALL_START",
        "SDK_INSTALL_FINISH",
    ]
    metadata: dict[str, typing.Any]

@typing.type_check_only
class WorkerMessage(typing.TypedDict, total=False):
    dataSamplingReport: DataSamplingReport
    labels: dict[str, typing.Any]
    perWorkerMetrics: PerWorkerMetrics
    streamingScalingReport: StreamingScalingReport
    time: str
    workerHealthReport: WorkerHealthReport
    workerLifecycleEvent: WorkerLifecycleEvent
    workerMessageCode: WorkerMessageCode
    workerMetrics: ResourceUtilizationReport
    workerShutdownNotice: WorkerShutdownNotice
    workerThreadScalingReport: WorkerThreadScalingReport

@typing.type_check_only
class WorkerMessageCode(typing.TypedDict, total=False):
    code: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class WorkerMessageResponse(typing.TypedDict, total=False):
    streamingScalingReportResponse: StreamingScalingReportResponse
    workerHealthReportResponse: WorkerHealthReportResponse
    workerMetricsResponse: ResourceUtilizationReportResponse
    workerShutdownNoticeResponse: WorkerShutdownNoticeResponse
    workerThreadScalingReportResponse: WorkerThreadScalingReportResponse

@typing.type_check_only
class WorkerPool(typing.TypedDict, total=False):
    autoscalingSettings: AutoscalingSettings
    dataDisks: _list[Disk]
    defaultPackageSet: typing.Literal[
        "DEFAULT_PACKAGE_SET_UNKNOWN",
        "DEFAULT_PACKAGE_SET_NONE",
        "DEFAULT_PACKAGE_SET_JAVA",
        "DEFAULT_PACKAGE_SET_PYTHON",
    ]
    diskProvisionedIops: str
    diskProvisionedThroughputMibps: str
    diskSizeGb: int
    diskSourceImage: str
    diskType: str
    ipConfiguration: typing.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    kind: str
    machineType: str
    metadata: dict[str, typing.Any]
    network: str
    numThreadsPerWorker: int
    numWorkers: int
    onHostMaintenance: str
    packages: _list[Package]
    poolArgs: dict[str, typing.Any]
    sdkHarnessContainerImages: _list[SdkHarnessContainerImage]
    subnetwork: str
    taskrunnerSettings: TaskRunnerSettings
    teardownPolicy: typing.Literal[
        "TEARDOWN_POLICY_UNKNOWN",
        "TEARDOWN_ALWAYS",
        "TEARDOWN_ON_SUCCESS",
        "TEARDOWN_NEVER",
    ]
    workerHarnessContainerImage: str
    zone: str

@typing.type_check_only
class WorkerSettings(typing.TypedDict, total=False):
    baseUrl: str
    reportingEnabled: bool
    servicePath: str
    shuffleServicePath: str
    tempStoragePrefix: str
    workerId: str

@typing.type_check_only
class WorkerShutdownNotice(typing.TypedDict, total=False):
    reason: str

@typing.type_check_only
class WorkerShutdownNoticeResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class WorkerThreadScalingReport(typing.TypedDict, total=False):
    currentThreadCount: int

@typing.type_check_only
class WorkerThreadScalingReportResponse(typing.TypedDict, total=False):
    recommendedThreadCount: int

@typing.type_check_only
class WriteInstruction(typing.TypedDict, total=False):
    input: InstructionInput
    sink: Sink
