import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApproximateProgress(typing_extensions.TypedDict, total=False):
    percentComplete: float
    position: Position
    remainingTime: str

@typing.type_check_only
class ApproximateReportedProgress(typing_extensions.TypedDict, total=False):
    consumedParallelism: ReportedParallelism
    fractionConsumed: float
    position: Position
    remainingParallelism: ReportedParallelism

@typing.type_check_only
class ApproximateSplitRequest(typing_extensions.TypedDict, total=False):
    fractionConsumed: float
    fractionOfRemainder: float
    position: Position

@typing.type_check_only
class AutoscalingEvent(typing_extensions.TypedDict, total=False):
    currentNumWorkers: str
    description: StructuredMessage
    eventType: typing_extensions.Literal[
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
class AutoscalingSettings(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
        "AUTOSCALING_ALGORITHM_UNKNOWN",
        "AUTOSCALING_ALGORITHM_NONE",
        "AUTOSCALING_ALGORITHM_BASIC",
    ]
    maxNumWorkers: int

@typing.type_check_only
class Base2Exponent(typing_extensions.TypedDict, total=False):
    numberOfBuckets: int
    scale: int

@typing.type_check_only
class BigQueryIODetails(typing_extensions.TypedDict, total=False):
    dataset: str
    projectId: str
    query: str
    table: str

@typing.type_check_only
class BigTableIODetails(typing_extensions.TypedDict, total=False):
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class BoundedTrie(typing_extensions.TypedDict, total=False):
    bound: int
    root: BoundedTrieNode
    singleton: _list[str]

@typing.type_check_only
class BoundedTrieNode(typing_extensions.TypedDict, total=False):
    children: dict[str, typing.Any]
    truncated: bool

@typing.type_check_only
class BucketOptions(typing_extensions.TypedDict, total=False):
    exponential: Base2Exponent
    linear: Linear

@typing.type_check_only
class CPUTime(typing_extensions.TypedDict, total=False):
    rate: float
    timestamp: str
    totalMs: str

@typing.type_check_only
class ComponentSource(typing_extensions.TypedDict, total=False):
    name: str
    originalTransformOrCollection: str
    userName: str

@typing.type_check_only
class ComponentTransform(typing_extensions.TypedDict, total=False):
    name: str
    originalTransform: str
    userName: str

@typing.type_check_only
class ComputationTopology(typing_extensions.TypedDict, total=False):
    computationId: str
    inputs: _list[StreamLocation]
    keyRanges: _list[KeyRangeLocation]
    outputs: _list[StreamLocation]
    stateFamilies: _list[StateFamilyConfig]
    systemStageName: str

@typing.type_check_only
class ConcatPosition(typing_extensions.TypedDict, total=False):
    index: int
    position: Position

@typing.type_check_only
class ContainerSpec(typing_extensions.TypedDict, total=False):
    defaultEnvironment: FlexTemplateRuntimeEnvironment
    image: str
    imageRepositoryCertPath: str
    imageRepositoryPasswordSecretId: str
    imageRepositoryUsernameSecretId: str
    metadata: TemplateMetadata
    sdkInfo: SDKInfo

@typing.type_check_only
class CounterMetadata(typing_extensions.TypedDict, total=False):
    description: str
    kind: typing_extensions.Literal[
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
    standardUnits: typing_extensions.Literal[
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
class CounterStructuredName(typing_extensions.TypedDict, total=False):
    componentStepName: str
    executionStepName: str
    inputIndex: int
    name: str
    origin: typing_extensions.Literal["SYSTEM", "USER"]
    originNamespace: str
    originalRequestingStepName: str
    originalStepName: str
    portion: typing_extensions.Literal["ALL", "KEY", "VALUE"]
    workerId: str

@typing.type_check_only
class CounterStructuredNameAndMetadata(typing_extensions.TypedDict, total=False):
    metadata: CounterMetadata
    name: CounterStructuredName

@typing.type_check_only
class CounterUpdate(typing_extensions.TypedDict, total=False):
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
class CreateJobFromTemplateRequest(typing_extensions.TypedDict, total=False):
    environment: RuntimeEnvironment
    gcsPath: str
    jobName: str
    location: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class CustomSourceLocation(typing_extensions.TypedDict, total=False):
    stateful: bool

@typing.type_check_only
class DataDiskAssignment(typing_extensions.TypedDict, total=False):
    dataDisks: _list[str]
    vmInstance: str

@typing.type_check_only
class DataSamplingConfig(typing_extensions.TypedDict, total=False):
    behaviors: _list[
        typing_extensions.Literal[
            "DATA_SAMPLING_BEHAVIOR_UNSPECIFIED", "DISABLED", "ALWAYS_ON", "EXCEPTIONS"
        ]
    ]

@typing.type_check_only
class DataSamplingReport(typing_extensions.TypedDict, total=False):
    bytesWrittenDelta: str
    elementsSampledBytes: str
    elementsSampledCount: str
    exceptionsSampledCount: str
    pcollectionsSampledCount: str
    persistenceErrorsCount: str
    translationErrorsCount: str

@typing.type_check_only
class DataflowGaugeValue(typing_extensions.TypedDict, total=False):
    measuredTime: str
    value: str

@typing.type_check_only
class DataflowHistogramValue(typing_extensions.TypedDict, total=False):
    bucketCounts: _list[str]
    bucketOptions: BucketOptions
    count: str
    outlierStats: OutlierStats

@typing.type_check_only
class DatastoreIODetails(typing_extensions.TypedDict, total=False):
    namespace: str
    projectId: str

@typing.type_check_only
class DebugOptions(typing_extensions.TypedDict, total=False):
    dataSampling: DataSamplingConfig
    enableHotKeyLogging: bool

@typing.type_check_only
class DeleteSnapshotResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DerivedSource(typing_extensions.TypedDict, total=False):
    derivationMode: typing_extensions.Literal[
        "SOURCE_DERIVATION_MODE_UNKNOWN",
        "SOURCE_DERIVATION_MODE_INDEPENDENT",
        "SOURCE_DERIVATION_MODE_CHILD_OF_CURRENT",
        "SOURCE_DERIVATION_MODE_SIBLING_OF_CURRENT",
    ]
    source: Source

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    diskType: str
    mountPoint: str
    sizeGb: int

@typing.type_check_only
class DisplayData(typing_extensions.TypedDict, total=False):
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
class DistributionUpdate(typing_extensions.TypedDict, total=False):
    count: SplitInt64
    histogram: Histogram
    max: SplitInt64
    min: SplitInt64
    sum: SplitInt64
    sumOfSquares: float

@typing.type_check_only
class DynamicSourceSplit(typing_extensions.TypedDict, total=False):
    primary: DerivedSource
    residual: DerivedSource

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    clusterManagerApiService: str
    dataset: str
    debugOptions: DebugOptions
    experiments: _list[str]
    flexResourceSchedulingGoal: typing_extensions.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    internalExperiments: dict[str, typing.Any]
    sdkPipelineOptions: dict[str, typing.Any]
    serviceAccountEmail: str
    serviceKmsKeyName: str
    serviceOptions: _list[str]
    shuffleMode: typing_extensions.Literal[
        "SHUFFLE_MODE_UNSPECIFIED", "VM_BASED", "SERVICE_BASED"
    ]
    streamingMode: typing_extensions.Literal[
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
class ExecutionStageState(typing_extensions.TypedDict, total=False):
    currentStateTime: str
    executionStageName: str
    executionStageState: typing_extensions.Literal[
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
    ]

@typing.type_check_only
class ExecutionStageSummary(typing_extensions.TypedDict, total=False):
    componentSource: _list[ComponentSource]
    componentTransform: _list[ComponentTransform]
    id: str
    inputSource: _list[StageSource]
    kind: typing_extensions.Literal[
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
class FailedLocation(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class FileIODetails(typing_extensions.TypedDict, total=False):
    filePattern: str

@typing.type_check_only
class FlattenInstruction(typing_extensions.TypedDict, total=False):
    inputs: _list[InstructionInput]

@typing.type_check_only
class FlexTemplateRuntimeEnvironment(typing_extensions.TypedDict, total=False):
    additionalExperiments: _list[str]
    additionalPipelineOptions: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    autoscalingAlgorithm: typing_extensions.Literal[
        "AUTOSCALING_ALGORITHM_UNKNOWN",
        "AUTOSCALING_ALGORITHM_NONE",
        "AUTOSCALING_ALGORITHM_BASIC",
    ]
    diskSizeGb: int
    dumpHeapOnOom: bool
    enableLauncherVmSerialPortLogging: bool
    enableStreamingEngine: bool
    flexrsGoal: typing_extensions.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    ipConfiguration: typing_extensions.Literal[
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
    streamingMode: typing_extensions.Literal[
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
class FloatingPointList(typing_extensions.TypedDict, total=False):
    elements: _list[float]

@typing.type_check_only
class FloatingPointMean(typing_extensions.TypedDict, total=False):
    count: SplitInt64
    sum: float

@typing.type_check_only
class GPUUsage(typing_extensions.TypedDict, total=False):
    timestamp: str
    utilization: GPUUtilization

@typing.type_check_only
class GPUUtilization(typing_extensions.TypedDict, total=False):
    rate: float

@typing.type_check_only
class GetDebugConfigRequest(typing_extensions.TypedDict, total=False):
    componentId: str
    location: str
    workerId: str

@typing.type_check_only
class GetDebugConfigResponse(typing_extensions.TypedDict, total=False):
    config: str

@typing.type_check_only
class GetTemplateResponse(typing_extensions.TypedDict, total=False):
    metadata: TemplateMetadata
    runtimeMetadata: RuntimeMetadata
    status: Status
    templateType: typing_extensions.Literal["UNKNOWN", "LEGACY", "FLEX"]

@typing.type_check_only
class GetWorkerStacktracesRequest(typing_extensions.TypedDict, total=False):
    workerId: str

@typing.type_check_only
class GetWorkerStacktracesResponse(typing_extensions.TypedDict, total=False):
    sdks: _list[Sdk]

@typing.type_check_only
class Histogram(typing_extensions.TypedDict, total=False):
    bucketCounts: _list[str]
    firstBucketOffset: int

@typing.type_check_only
class HotKeyDebuggingInfo(typing_extensions.TypedDict, total=False):
    detectedHotKeys: dict[str, typing.Any]

@typing.type_check_only
class HotKeyDetection(typing_extensions.TypedDict, total=False):
    hotKeyAge: str
    systemName: str
    userStepName: str

@typing.type_check_only
class HotKeyInfo(typing_extensions.TypedDict, total=False):
    hotKeyAge: str
    key: str
    keyTruncated: bool

@typing.type_check_only
class InstructionInput(typing_extensions.TypedDict, total=False):
    outputNum: int
    producerInstructionIndex: int

@typing.type_check_only
class InstructionOutput(typing_extensions.TypedDict, total=False):
    codec: dict[str, typing.Any]
    name: str
    onlyCountKeyBytes: bool
    onlyCountValueBytes: bool
    originalName: str
    systemName: str

@typing.type_check_only
class IntegerGauge(typing_extensions.TypedDict, total=False):
    timestamp: str
    value: SplitInt64

@typing.type_check_only
class IntegerList(typing_extensions.TypedDict, total=False):
    elements: _list[SplitInt64]

@typing.type_check_only
class IntegerMean(typing_extensions.TypedDict, total=False):
    count: SplitInt64
    sum: SplitInt64

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    clientRequestId: str
    createTime: str
    createdFromSnapshotId: str
    currentState: typing_extensions.Literal[
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
    ]
    currentStateTime: str
    environment: Environment
    executionInfo: JobExecutionInfo
    id: str
    jobMetadata: JobMetadata
    labels: dict[str, typing.Any]
    location: str
    name: str
    pipelineDescription: PipelineDescription
    projectId: str
    replaceJobId: str
    replacedByJobId: str
    requestedState: typing_extensions.Literal[
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
    type: typing_extensions.Literal[
        "JOB_TYPE_UNKNOWN", "JOB_TYPE_BATCH", "JOB_TYPE_STREAMING"
    ]

@typing.type_check_only
class JobExecutionDetails(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    stages: _list[StageSummary]

@typing.type_check_only
class JobExecutionInfo(typing_extensions.TypedDict, total=False):
    stages: dict[str, typing.Any]

@typing.type_check_only
class JobExecutionStageInfo(typing_extensions.TypedDict, total=False):
    stepName: _list[str]

@typing.type_check_only
class JobMessage(typing_extensions.TypedDict, total=False):
    id: str
    messageImportance: typing_extensions.Literal[
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
class JobMetadata(typing_extensions.TypedDict, total=False):
    bigTableDetails: _list[BigTableIODetails]
    bigqueryDetails: _list[BigQueryIODetails]
    datastoreDetails: _list[DatastoreIODetails]
    fileDetails: _list[FileIODetails]
    pubsubDetails: _list[PubSubIODetails]
    sdkVersion: SdkVersion
    spannerDetails: _list[SpannerIODetails]
    userDisplayProperties: dict[str, typing.Any]

@typing.type_check_only
class JobMetrics(typing_extensions.TypedDict, total=False):
    metricTime: str
    metrics: _list[MetricUpdate]

@typing.type_check_only
class KeyRangeDataDiskAssignment(typing_extensions.TypedDict, total=False):
    dataDisk: str
    end: str
    start: str

@typing.type_check_only
class KeyRangeLocation(typing_extensions.TypedDict, total=False):
    dataDisk: str
    deliveryEndpoint: str
    deprecatedPersistentDirectory: str
    end: str
    start: str

@typing.type_check_only
class LaunchFlexTemplateParameter(typing_extensions.TypedDict, total=False):
    containerSpec: ContainerSpec
    containerSpecGcsPath: str
    environment: FlexTemplateRuntimeEnvironment
    jobName: str
    launchOptions: dict[str, typing.Any]
    parameters: dict[str, typing.Any]
    transformNameMappings: dict[str, typing.Any]
    update: bool

@typing.type_check_only
class LaunchFlexTemplateRequest(typing_extensions.TypedDict, total=False):
    launchParameter: LaunchFlexTemplateParameter
    validateOnly: bool

@typing.type_check_only
class LaunchFlexTemplateResponse(typing_extensions.TypedDict, total=False):
    job: Job

@typing.type_check_only
class LaunchTemplateParameters(typing_extensions.TypedDict, total=False):
    environment: RuntimeEnvironment
    jobName: str
    parameters: dict[str, typing.Any]
    transformNameMapping: dict[str, typing.Any]
    update: bool

@typing.type_check_only
class LaunchTemplateResponse(typing_extensions.TypedDict, total=False):
    job: Job

@typing.type_check_only
class LeaseWorkItemRequest(typing_extensions.TypedDict, total=False):
    currentWorkerTime: str
    location: str
    projectNumber: str
    requestedLeaseDuration: str
    unifiedWorkerRequest: dict[str, typing.Any]
    workItemTypes: _list[str]
    workerCapabilities: _list[str]
    workerId: str

@typing.type_check_only
class LeaseWorkItemResponse(typing_extensions.TypedDict, total=False):
    unifiedWorkerResponse: dict[str, typing.Any]
    workItems: _list[WorkItem]

@typing.type_check_only
class Linear(typing_extensions.TypedDict, total=False):
    numberOfBuckets: int
    start: float
    width: float

@typing.type_check_only
class ListJobMessagesResponse(typing_extensions.TypedDict, total=False):
    autoscalingEvents: _list[AutoscalingEvent]
    jobMessages: _list[JobMessage]
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    failedLocation: _list[FailedLocation]
    jobs: _list[Job]
    nextPageToken: str

@typing.type_check_only
class ListSnapshotsResponse(typing_extensions.TypedDict, total=False):
    snapshots: _list[Snapshot]

@typing.type_check_only
class MapTask(typing_extensions.TypedDict, total=False):
    counterPrefix: str
    instructions: _list[ParallelInstruction]
    stageName: str
    systemName: str

@typing.type_check_only
class MemInfo(typing_extensions.TypedDict, total=False):
    currentLimitBytes: str
    currentOoms: str
    currentRssBytes: str
    timestamp: str
    totalGbMs: str

@typing.type_check_only
class MetricShortId(typing_extensions.TypedDict, total=False):
    metricIndex: int
    shortId: str

@typing.type_check_only
class MetricStructuredName(typing_extensions.TypedDict, total=False):
    context: dict[str, typing.Any]
    name: str
    origin: str

@typing.type_check_only
class MetricUpdate(typing_extensions.TypedDict, total=False):
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
class MetricValue(typing_extensions.TypedDict, total=False):
    metric: str
    metricLabels: dict[str, typing.Any]
    valueGauge64: DataflowGaugeValue
    valueHistogram: DataflowHistogramValue
    valueInt64: str

@typing.type_check_only
class MountedDataDisk(typing_extensions.TypedDict, total=False):
    dataDisk: str

@typing.type_check_only
class MultiOutputInfo(typing_extensions.TypedDict, total=False):
    tag: str

@typing.type_check_only
class NameAndKind(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal[
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
class OutlierStats(typing_extensions.TypedDict, total=False):
    overflowCount: str
    overflowMean: float
    underflowCount: str
    underflowMean: float

@typing.type_check_only
class Package(typing_extensions.TypedDict, total=False):
    location: str
    name: str

@typing.type_check_only
class ParDoInstruction(typing_extensions.TypedDict, total=False):
    input: InstructionInput
    multiOutputInfos: _list[MultiOutputInfo]
    numOutputs: int
    sideInputs: _list[SideInputInfo]
    userFn: dict[str, typing.Any]

@typing.type_check_only
class ParallelInstruction(typing_extensions.TypedDict, total=False):
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
class Parameter(typing_extensions.TypedDict, total=False):
    key: str
    value: typing.Any

@typing.type_check_only
class ParameterMetadata(typing_extensions.TypedDict, total=False):
    customMetadata: dict[str, typing.Any]
    defaultValue: str
    enumOptions: _list[ParameterMetadataEnumOption]
    groupName: str
    helpText: str
    hiddenUi: bool
    isOptional: bool
    label: str
    name: str
    paramType: typing_extensions.Literal[
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
class ParameterMetadataEnumOption(typing_extensions.TypedDict, total=False):
    description: str
    label: str
    value: str

@typing.type_check_only
class PartialGroupByKeyInstruction(typing_extensions.TypedDict, total=False):
    input: InstructionInput
    inputElementCodec: dict[str, typing.Any]
    originalCombineValuesInputStoreName: str
    originalCombineValuesStepName: str
    sideInputs: _list[SideInputInfo]
    valueCombiningFn: dict[str, typing.Any]

@typing.type_check_only
class PerStepNamespaceMetrics(typing_extensions.TypedDict, total=False):
    metricValues: _list[MetricValue]
    metricsNamespace: str
    originalStep: str

@typing.type_check_only
class PerWorkerMetrics(typing_extensions.TypedDict, total=False):
    perStepNamespaceMetrics: _list[PerStepNamespaceMetrics]

@typing.type_check_only
class PipelineDescription(typing_extensions.TypedDict, total=False):
    displayData: _list[DisplayData]
    executionPipelineStage: _list[ExecutionStageSummary]
    originalPipelineTransform: _list[TransformSummary]
    stepNamesHash: str

@typing.type_check_only
class Point(typing_extensions.TypedDict, total=False):
    time: str
    value: float

@typing.type_check_only
class Position(typing_extensions.TypedDict, total=False):
    byteOffset: str
    concatPosition: ConcatPosition
    end: bool
    key: str
    recordIndex: str
    shufflePosition: str

@typing.type_check_only
class ProgressTimeseries(typing_extensions.TypedDict, total=False):
    currentProgress: float
    dataPoints: _list[Point]

@typing.type_check_only
class PubSubIODetails(typing_extensions.TypedDict, total=False):
    subscription: str
    topic: str

@typing.type_check_only
class PubsubLocation(typing_extensions.TypedDict, total=False):
    dropLateData: bool
    dynamicDestinations: bool
    idLabel: str
    subscription: str
    timestampLabel: str
    topic: str
    trackingSubscription: str
    withAttributes: bool

@typing.type_check_only
class PubsubSnapshotMetadata(typing_extensions.TypedDict, total=False):
    expireTime: str
    snapshotName: str
    topicName: str

@typing.type_check_only
class ReadInstruction(typing_extensions.TypedDict, total=False):
    source: Source

@typing.type_check_only
class ReportWorkItemStatusRequest(typing_extensions.TypedDict, total=False):
    currentWorkerTime: str
    location: str
    projectNumber: str
    unifiedWorkerRequest: dict[str, typing.Any]
    workItemStatuses: _list[WorkItemStatus]
    workerId: str

@typing.type_check_only
class ReportWorkItemStatusResponse(typing_extensions.TypedDict, total=False):
    unifiedWorkerResponse: dict[str, typing.Any]
    workItemServiceStates: _list[WorkItemServiceState]

@typing.type_check_only
class ReportedParallelism(typing_extensions.TypedDict, total=False):
    isInfinite: bool
    value: float

@typing.type_check_only
class ResourceUtilizationReport(typing_extensions.TypedDict, total=False):
    containers: dict[str, typing.Any]
    cpuTime: _list[CPUTime]
    gpuUsage: _list[GPUUsage]
    memoryInfo: _list[MemInfo]

@typing.type_check_only
class ResourceUtilizationReportResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RuntimeEnvironment(typing_extensions.TypedDict, total=False):
    additionalExperiments: _list[str]
    additionalPipelineOptions: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    bypassTempDirValidation: bool
    diskSizeGb: int
    enableStreamingEngine: bool
    ipConfiguration: typing_extensions.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    kmsKeyName: str
    machineType: str
    maxWorkers: int
    network: str
    numWorkers: int
    serviceAccountEmail: str
    streamingMode: typing_extensions.Literal[
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
class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    parameters: _list[ParameterMetadata]
    sdkInfo: SDKInfo

@typing.type_check_only
class RuntimeUpdatableParams(typing_extensions.TypedDict, total=False):
    maxNumWorkers: int
    minNumWorkers: int
    workerUtilizationHint: float

@typing.type_check_only
class SDKInfo(typing_extensions.TypedDict, total=False):
    language: typing_extensions.Literal["UNKNOWN", "JAVA", "PYTHON", "GO", "YAML"]
    version: str

@typing.type_check_only
class Sdk(typing_extensions.TypedDict, total=False):
    sdkId: str
    stacks: _list[Stack]

@typing.type_check_only
class SdkBug(typing_extensions.TypedDict, total=False):
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "NOTICE", "WARNING", "SEVERE"
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GENERAL", "PERFORMANCE", "DATALOSS"
    ]
    uri: str

@typing.type_check_only
class SdkHarnessContainerImage(typing_extensions.TypedDict, total=False):
    capabilities: _list[str]
    containerImage: str
    environmentId: str
    useSingleCorePerContainer: bool

@typing.type_check_only
class SdkVersion(typing_extensions.TypedDict, total=False):
    bugs: _list[SdkBug]
    sdkSupportStatus: typing_extensions.Literal[
        "UNKNOWN", "SUPPORTED", "STALE", "DEPRECATED", "UNSUPPORTED"
    ]
    version: str
    versionDisplayName: str

@typing.type_check_only
class SendDebugCaptureRequest(typing_extensions.TypedDict, total=False):
    componentId: str
    data: str
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "RAW", "JSON", "ZLIB", "BROTLI"
    ]
    location: str
    workerId: str

@typing.type_check_only
class SendDebugCaptureResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SendWorkerMessagesRequest(typing_extensions.TypedDict, total=False):
    location: str
    workerMessages: _list[WorkerMessage]

@typing.type_check_only
class SendWorkerMessagesResponse(typing_extensions.TypedDict, total=False):
    workerMessageResponses: _list[WorkerMessageResponse]

@typing.type_check_only
class SeqMapTask(typing_extensions.TypedDict, total=False):
    inputs: _list[SideInputInfo]
    name: str
    outputInfos: _list[SeqMapTaskOutputInfo]
    stageName: str
    systemName: str
    userFn: dict[str, typing.Any]

@typing.type_check_only
class SeqMapTaskOutputInfo(typing_extensions.TypedDict, total=False):
    sink: Sink
    tag: str

@typing.type_check_only
class ServiceResources(typing_extensions.TypedDict, total=False):
    zones: _list[str]

@typing.type_check_only
class ShellTask(typing_extensions.TypedDict, total=False):
    command: str
    exitCode: int

@typing.type_check_only
class SideInputInfo(typing_extensions.TypedDict, total=False):
    kind: dict[str, typing.Any]
    sources: _list[Source]
    tag: str

@typing.type_check_only
class Sink(typing_extensions.TypedDict, total=False):
    codec: dict[str, typing.Any]
    spec: dict[str, typing.Any]

@typing.type_check_only
class Snapshot(typing_extensions.TypedDict, total=False):
    creationTime: str
    description: str
    diskSizeBytes: str
    id: str
    projectId: str
    pubsubMetadata: _list[PubsubSnapshotMetadata]
    region: str
    sourceJobId: str
    state: typing_extensions.Literal[
        "UNKNOWN_SNAPSHOT_STATE", "PENDING", "RUNNING", "READY", "FAILED", "DELETED"
    ]
    ttl: str

@typing.type_check_only
class SnapshotJobRequest(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    snapshotSources: bool
    ttl: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    baseSpecs: _list[dict[str, typing.Any]]
    codec: dict[str, typing.Any]
    doesNotNeedSplitting: bool
    metadata: SourceMetadata
    spec: dict[str, typing.Any]

@typing.type_check_only
class SourceFork(typing_extensions.TypedDict, total=False):
    primary: SourceSplitShard
    primarySource: DerivedSource
    residual: SourceSplitShard
    residualSource: DerivedSource

@typing.type_check_only
class SourceGetMetadataRequest(typing_extensions.TypedDict, total=False):
    source: Source

@typing.type_check_only
class SourceGetMetadataResponse(typing_extensions.TypedDict, total=False):
    metadata: SourceMetadata

@typing.type_check_only
class SourceMetadata(typing_extensions.TypedDict, total=False):
    estimatedSizeBytes: str
    infinite: bool
    producesSortedKeys: bool

@typing.type_check_only
class SourceOperationRequest(typing_extensions.TypedDict, total=False):
    getMetadata: SourceGetMetadataRequest
    name: str
    originalName: str
    split: SourceSplitRequest
    stageName: str
    systemName: str

@typing.type_check_only
class SourceOperationResponse(typing_extensions.TypedDict, total=False):
    getMetadata: SourceGetMetadataResponse
    split: SourceSplitResponse

@typing.type_check_only
class SourceSplitOptions(typing_extensions.TypedDict, total=False):
    desiredBundleSizeBytes: str
    desiredShardSizeBytes: str

@typing.type_check_only
class SourceSplitRequest(typing_extensions.TypedDict, total=False):
    options: SourceSplitOptions
    source: Source

@typing.type_check_only
class SourceSplitResponse(typing_extensions.TypedDict, total=False):
    bundles: _list[DerivedSource]
    outcome: typing_extensions.Literal[
        "SOURCE_SPLIT_OUTCOME_UNKNOWN",
        "SOURCE_SPLIT_OUTCOME_USE_CURRENT",
        "SOURCE_SPLIT_OUTCOME_SPLITTING_HAPPENED",
    ]
    shards: _list[SourceSplitShard]

@typing.type_check_only
class SourceSplitShard(typing_extensions.TypedDict, total=False):
    derivationMode: typing_extensions.Literal[
        "SOURCE_DERIVATION_MODE_UNKNOWN",
        "SOURCE_DERIVATION_MODE_INDEPENDENT",
        "SOURCE_DERIVATION_MODE_CHILD_OF_CURRENT",
        "SOURCE_DERIVATION_MODE_SIBLING_OF_CURRENT",
    ]
    source: Source

@typing.type_check_only
class SpannerIODetails(typing_extensions.TypedDict, total=False):
    databaseId: str
    instanceId: str
    projectId: str

@typing.type_check_only
class SplitInt64(typing_extensions.TypedDict, total=False):
    highBits: int
    lowBits: int

@typing.type_check_only
class Stack(typing_extensions.TypedDict, total=False):
    stackContent: str
    threadCount: int
    threadName: str
    threadState: str
    timestamp: str

@typing.type_check_only
class StageExecutionDetails(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workers: _list[WorkerDetails]

@typing.type_check_only
class StageSource(typing_extensions.TypedDict, total=False):
    name: str
    originalTransformOrCollection: str
    sizeBytes: str
    userName: str

@typing.type_check_only
class StageSummary(typing_extensions.TypedDict, total=False):
    endTime: str
    metrics: _list[MetricUpdate]
    progress: ProgressTimeseries
    stageId: str
    startTime: str
    state: typing_extensions.Literal[
        "EXECUTION_STATE_UNKNOWN",
        "EXECUTION_STATE_NOT_STARTED",
        "EXECUTION_STATE_RUNNING",
        "EXECUTION_STATE_SUCCEEDED",
        "EXECUTION_STATE_FAILED",
        "EXECUTION_STATE_CANCELLED",
    ]
    stragglerSummary: StragglerSummary

@typing.type_check_only
class StateFamilyConfig(typing_extensions.TypedDict, total=False):
    isRead: bool
    stateFamily: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class Straggler(typing_extensions.TypedDict, total=False):
    batchStraggler: StragglerInfo
    streamingStraggler: StreamingStragglerInfo

@typing.type_check_only
class StragglerDebuggingInfo(typing_extensions.TypedDict, total=False):
    hotKey: HotKeyDebuggingInfo

@typing.type_check_only
class StragglerInfo(typing_extensions.TypedDict, total=False):
    causes: dict[str, typing.Any]
    startTime: str

@typing.type_check_only
class StragglerSummary(typing_extensions.TypedDict, total=False):
    recentStragglers: _list[Straggler]
    stragglerCauseCount: dict[str, typing.Any]
    totalStragglerCount: str

@typing.type_check_only
class StreamLocation(typing_extensions.TypedDict, total=False):
    customSourceLocation: CustomSourceLocation
    pubsubLocation: PubsubLocation
    sideInputLocation: StreamingSideInputLocation
    streamingStageLocation: StreamingStageLocation

@typing.type_check_only
class StreamingApplianceSnapshotConfig(typing_extensions.TypedDict, total=False):
    importStateEndpoint: str
    snapshotId: str

@typing.type_check_only
class StreamingComputationConfig(typing_extensions.TypedDict, total=False):
    computationId: str
    instructions: _list[ParallelInstruction]
    stageName: str
    systemName: str
    transformUserNameToStateFamily: dict[str, typing.Any]

@typing.type_check_only
class StreamingComputationRanges(typing_extensions.TypedDict, total=False):
    computationId: str
    rangeAssignments: _list[KeyRangeDataDiskAssignment]

@typing.type_check_only
class StreamingComputationTask(typing_extensions.TypedDict, total=False):
    computationRanges: _list[StreamingComputationRanges]
    dataDisks: _list[MountedDataDisk]
    taskType: typing_extensions.Literal[
        "STREAMING_COMPUTATION_TASK_UNKNOWN",
        "STREAMING_COMPUTATION_TASK_STOP",
        "STREAMING_COMPUTATION_TASK_START",
    ]

@typing.type_check_only
class StreamingConfigTask(typing_extensions.TypedDict, total=False):
    commitStreamChunkSizeBytes: str
    getDataStreamChunkSizeBytes: str
    maxWorkItemCommitBytes: str
    operationalLimits: StreamingOperationalLimits
    streamingComputationConfigs: _list[StreamingComputationConfig]
    userStepToStateFamilyNameMap: dict[str, typing.Any]
    userWorkerRunnerV1Settings: str
    userWorkerRunnerV2Settings: str
    windmillServiceEndpoint: str
    windmillServicePort: str

@typing.type_check_only
class StreamingOperationalLimits(typing_extensions.TypedDict, total=False):
    maxBagElementBytes: str
    maxGlobalDataBytes: str
    maxKeyBytes: str
    maxProductionOutputBytes: str
    maxSortedListElementBytes: str
    maxSourceStateBytes: str
    maxTagBytes: str
    maxValueBytes: str

@typing.type_check_only
class StreamingScalingReport(typing_extensions.TypedDict, total=False):
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
class StreamingScalingReportResponse(typing_extensions.TypedDict, total=False):
    maximumThreadCount: int

@typing.type_check_only
class StreamingSetupTask(typing_extensions.TypedDict, total=False):
    drain: bool
    receiveWorkPort: int
    snapshotConfig: StreamingApplianceSnapshotConfig
    streamingComputationTopology: TopologyConfig
    workerHarnessPort: int

@typing.type_check_only
class StreamingSideInputLocation(typing_extensions.TypedDict, total=False):
    stateFamily: str
    tag: str

@typing.type_check_only
class StreamingStageLocation(typing_extensions.TypedDict, total=False):
    streamId: str

@typing.type_check_only
class StreamingStragglerInfo(typing_extensions.TypedDict, total=False):
    dataWatermarkLag: str
    endTime: str
    startTime: str
    systemWatermarkLag: str
    workerName: str

@typing.type_check_only
class StringList(typing_extensions.TypedDict, total=False):
    elements: _list[str]

@typing.type_check_only
class StructuredMessage(typing_extensions.TypedDict, total=False):
    messageKey: str
    messageText: str
    parameters: _list[Parameter]

@typing.type_check_only
class TaskRunnerSettings(typing_extensions.TypedDict, total=False):
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
class TemplateMetadata(typing_extensions.TypedDict, total=False):
    defaultStreamingMode: str
    description: str
    name: str
    parameters: _list[ParameterMetadata]
    streaming: bool
    supportsAtLeastOnce: bool
    supportsExactlyOnce: bool
    yamlDefinition: str

@typing.type_check_only
class TopologyConfig(typing_extensions.TypedDict, total=False):
    computations: _list[ComputationTopology]
    dataDiskAssignments: _list[DataDiskAssignment]
    forwardingKeyBits: int
    persistentStateVersion: int
    userStageToComputationNameMap: dict[str, typing.Any]

@typing.type_check_only
class TransformSummary(typing_extensions.TypedDict, total=False):
    displayData: _list[DisplayData]
    id: str
    inputCollectionName: _list[str]
    kind: typing_extensions.Literal[
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
class WorkItem(typing_extensions.TypedDict, total=False):
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
class WorkItemDetails(typing_extensions.TypedDict, total=False):
    attemptId: str
    endTime: str
    metrics: _list[MetricUpdate]
    progress: ProgressTimeseries
    startTime: str
    state: typing_extensions.Literal[
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
class WorkItemServiceState(typing_extensions.TypedDict, total=False):
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
class WorkItemStatus(typing_extensions.TypedDict, total=False):
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
class WorkerDetails(typing_extensions.TypedDict, total=False):
    workItems: _list[WorkItemDetails]
    workerName: str

@typing.type_check_only
class WorkerHealthReport(typing_extensions.TypedDict, total=False):
    msg: str
    pods: _list[dict[str, typing.Any]]
    reportInterval: str
    vmBrokenCode: str
    vmIsBroken: bool
    vmIsHealthy: bool
    vmStartupTime: str

@typing.type_check_only
class WorkerHealthReportResponse(typing_extensions.TypedDict, total=False):
    reportInterval: str

@typing.type_check_only
class WorkerLifecycleEvent(typing_extensions.TypedDict, total=False):
    containerStartTime: str
    event: typing_extensions.Literal[
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
class WorkerMessage(typing_extensions.TypedDict, total=False):
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
class WorkerMessageCode(typing_extensions.TypedDict, total=False):
    code: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class WorkerMessageResponse(typing_extensions.TypedDict, total=False):
    streamingScalingReportResponse: StreamingScalingReportResponse
    workerHealthReportResponse: WorkerHealthReportResponse
    workerMetricsResponse: ResourceUtilizationReportResponse
    workerShutdownNoticeResponse: WorkerShutdownNoticeResponse
    workerThreadScalingReportResponse: WorkerThreadScalingReportResponse

@typing.type_check_only
class WorkerPool(typing_extensions.TypedDict, total=False):
    autoscalingSettings: AutoscalingSettings
    dataDisks: _list[Disk]
    defaultPackageSet: typing_extensions.Literal[
        "DEFAULT_PACKAGE_SET_UNKNOWN",
        "DEFAULT_PACKAGE_SET_NONE",
        "DEFAULT_PACKAGE_SET_JAVA",
        "DEFAULT_PACKAGE_SET_PYTHON",
    ]
    diskSizeGb: int
    diskSourceImage: str
    diskType: str
    ipConfiguration: typing_extensions.Literal[
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
    teardownPolicy: typing_extensions.Literal[
        "TEARDOWN_POLICY_UNKNOWN",
        "TEARDOWN_ALWAYS",
        "TEARDOWN_ON_SUCCESS",
        "TEARDOWN_NEVER",
    ]
    workerHarnessContainerImage: str
    zone: str

@typing.type_check_only
class WorkerSettings(typing_extensions.TypedDict, total=False):
    baseUrl: str
    reportingEnabled: bool
    servicePath: str
    shuffleServicePath: str
    tempStoragePrefix: str
    workerId: str

@typing.type_check_only
class WorkerShutdownNotice(typing_extensions.TypedDict, total=False):
    reason: str

@typing.type_check_only
class WorkerShutdownNoticeResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class WorkerThreadScalingReport(typing_extensions.TypedDict, total=False):
    currentThreadCount: int

@typing.type_check_only
class WorkerThreadScalingReportResponse(typing_extensions.TypedDict, total=False):
    recommendedThreadCount: int

@typing.type_check_only
class WriteInstruction(typing_extensions.TypedDict, total=False):
    input: InstructionInput
    sink: Sink
