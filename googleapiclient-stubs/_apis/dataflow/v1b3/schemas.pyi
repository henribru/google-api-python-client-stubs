import typing

import typing_extensions
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
class Artifact(typing_extensions.TypedDict, total=False):
    containerSpec: ContainerSpec
    jobGraphGcsPath: str
    metadata: TemplateMetadata

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
class CPUTime(typing_extensions.TypedDict, total=False):
    rate: float
    timestamp: str
    totalMs: str

@typing.type_check_only
class CommitTemplateVersionRequest(typing_extensions.TypedDict, total=False):
    templateVersion: TemplateVersion

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
    inputs: typing.List[StreamLocation]
    keyRanges: typing.List[KeyRangeLocation]
    outputs: typing.List[StreamLocation]
    stateFamilies: typing.List[StateFamilyConfig]
    systemStageName: str

@typing.type_check_only
class ConcatPosition(typing_extensions.TypedDict, total=False):
    index: int
    position: Position

@typing.type_check_only
class ContainerSpec(typing_extensions.TypedDict, total=False):
    defaultEnvironment: FlexTemplateRuntimeEnvironment
    image: str
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
    parameters: typing.Dict[str, typing.Any]

@typing.type_check_only
class CreateTemplateVersionRequest(typing_extensions.TypedDict, total=False):
    templateVersion: TemplateVersion

@typing.type_check_only
class CustomSourceLocation(typing_extensions.TypedDict, total=False):
    stateful: bool

@typing.type_check_only
class DataDiskAssignment(typing_extensions.TypedDict, total=False):
    dataDisks: typing.List[str]
    vmInstance: str

@typing.type_check_only
class DatastoreIODetails(typing_extensions.TypedDict, total=False):
    namespace: str
    projectId: str

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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    clusterManagerApiService: str
    dataset: str
    experiments: typing.List[str]
    flexResourceSchedulingGoal: typing_extensions.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    internalExperiments: typing.Dict[str, typing.Any]
    sdkPipelineOptions: typing.Dict[str, typing.Any]
    serviceAccountEmail: str
    serviceKmsKeyName: str
    serviceOptions: typing.List[str]
    shuffleMode: typing_extensions.Literal[
        "SHUFFLE_MODE_UNSPECIFIED", "VM_BASED", "SERVICE_BASED"
    ]
    tempStoragePrefix: str
    userAgent: typing.Dict[str, typing.Any]
    version: typing.Dict[str, typing.Any]
    workerPools: typing.List[WorkerPool]
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
    componentSource: typing.List[ComponentSource]
    componentTransform: typing.List[ComponentTransform]
    id: str
    inputSource: typing.List[StageSource]
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
    outputSource: typing.List[StageSource]
    prerequisiteStage: typing.List[str]

@typing.type_check_only
class FailedLocation(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class FileIODetails(typing_extensions.TypedDict, total=False):
    filePattern: str

@typing.type_check_only
class FlattenInstruction(typing_extensions.TypedDict, total=False):
    inputs: typing.List[InstructionInput]

@typing.type_check_only
class FlexTemplateRuntimeEnvironment(typing_extensions.TypedDict, total=False):
    additionalExperiments: typing.List[str]
    additionalUserLabels: typing.Dict[str, typing.Any]
    enableStreamingEngine: bool
    flexrsGoal: typing_extensions.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    ipConfiguration: typing_extensions.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    kmsKeyName: str
    machineType: str
    maxWorkers: int
    network: str
    numWorkers: int
    serviceAccountEmail: str
    subnetwork: str
    tempLocation: str
    workerRegion: str
    workerZone: str
    zone: str

@typing.type_check_only
class FloatingPointList(typing_extensions.TypedDict, total=False):
    elements: typing.List[float]

@typing.type_check_only
class FloatingPointMean(typing_extensions.TypedDict, total=False):
    count: SplitInt64
    sum: float

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
class Histogram(typing_extensions.TypedDict, total=False):
    bucketCounts: typing.List[str]
    firstBucketOffset: int

@typing.type_check_only
class HotKeyDetection(typing_extensions.TypedDict, total=False):
    hotKeyAge: str
    systemName: str
    userStepName: str

@typing.type_check_only
class InstructionInput(typing_extensions.TypedDict, total=False):
    outputNum: int
    producerInstructionIndex: int

@typing.type_check_only
class InstructionOutput(typing_extensions.TypedDict, total=False):
    codec: typing.Dict[str, typing.Any]
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
    elements: typing.List[SplitInt64]

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
    labels: typing.Dict[str, typing.Any]
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
    satisfiesPzs: bool
    stageStates: typing.List[ExecutionStageState]
    startTime: str
    steps: typing.List[Step]
    stepsLocation: str
    tempFiles: typing.List[str]
    transformNameMapping: typing.Dict[str, typing.Any]
    type: typing_extensions.Literal[
        "JOB_TYPE_UNKNOWN", "JOB_TYPE_BATCH", "JOB_TYPE_STREAMING"
    ]

@typing.type_check_only
class JobExecutionDetails(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    stages: typing.List[StageSummary]

@typing.type_check_only
class JobExecutionInfo(typing_extensions.TypedDict, total=False):
    stages: typing.Dict[str, typing.Any]

@typing.type_check_only
class JobExecutionStageInfo(typing_extensions.TypedDict, total=False):
    stepName: typing.List[str]

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
    bigTableDetails: typing.List[BigTableIODetails]
    bigqueryDetails: typing.List[BigQueryIODetails]
    datastoreDetails: typing.List[DatastoreIODetails]
    fileDetails: typing.List[FileIODetails]
    pubsubDetails: typing.List[PubSubIODetails]
    sdkVersion: SdkVersion
    spannerDetails: typing.List[SpannerIODetails]

@typing.type_check_only
class JobMetrics(typing_extensions.TypedDict, total=False):
    metricTime: str
    metrics: typing.List[MetricUpdate]

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
    launchOptions: typing.Dict[str, typing.Any]
    parameters: typing.Dict[str, typing.Any]
    transformNameMappings: typing.Dict[str, typing.Any]
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
    parameters: typing.Dict[str, typing.Any]
    transformNameMapping: typing.Dict[str, typing.Any]
    update: bool

@typing.type_check_only
class LaunchTemplateResponse(typing_extensions.TypedDict, total=False):
    job: Job

@typing.type_check_only
class LeaseWorkItemRequest(typing_extensions.TypedDict, total=False):
    currentWorkerTime: str
    location: str
    requestedLeaseDuration: str
    unifiedWorkerRequest: typing.Dict[str, typing.Any]
    workItemTypes: typing.List[str]
    workerCapabilities: typing.List[str]
    workerId: str

@typing.type_check_only
class LeaseWorkItemResponse(typing_extensions.TypedDict, total=False):
    unifiedWorkerResponse: typing.Dict[str, typing.Any]
    workItems: typing.List[WorkItem]

@typing.type_check_only
class ListJobMessagesResponse(typing_extensions.TypedDict, total=False):
    autoscalingEvents: typing.List[AutoscalingEvent]
    jobMessages: typing.List[JobMessage]
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    failedLocation: typing.List[FailedLocation]
    jobs: typing.List[Job]
    nextPageToken: str

@typing.type_check_only
class ListSnapshotsResponse(typing_extensions.TypedDict, total=False):
    snapshots: typing.List[Snapshot]

@typing.type_check_only
class ListTemplateVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    templateVersions: typing.List[TemplateVersion]

@typing.type_check_only
class MapTask(typing_extensions.TypedDict, total=False):
    counterPrefix: str
    instructions: typing.List[ParallelInstruction]
    stageName: str
    systemName: str

@typing.type_check_only
class MemInfo(typing_extensions.TypedDict, total=False):
    currentLimitBytes: str
    currentRssBytes: str
    timestamp: str
    totalGbMs: str

@typing.type_check_only
class MetricShortId(typing_extensions.TypedDict, total=False):
    metricIndex: int
    shortId: str

@typing.type_check_only
class MetricStructuredName(typing_extensions.TypedDict, total=False):
    context: typing.Dict[str, typing.Any]
    name: str
    origin: str

@typing.type_check_only
class MetricUpdate(typing_extensions.TypedDict, total=False):
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
    updateTime: str

@typing.type_check_only
class ModifyTemplateVersionLabelRequest(typing_extensions.TypedDict, total=False):
    key: str
    op: typing_extensions.Literal["OPERATION_UNSPECIFIED", "ADD", "REMOVE"]
    value: str

@typing.type_check_only
class ModifyTemplateVersionLabelResponse(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class ModifyTemplateVersionTagRequest(typing_extensions.TypedDict, total=False):
    removeOnly: bool
    tag: str

@typing.type_check_only
class ModifyTemplateVersionTagResponse(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]

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
class Package(typing_extensions.TypedDict, total=False):
    location: str
    name: str

@typing.type_check_only
class ParDoInstruction(typing_extensions.TypedDict, total=False):
    input: InstructionInput
    multiOutputInfos: typing.List[MultiOutputInfo]
    numOutputs: int
    sideInputs: typing.List[SideInputInfo]
    userFn: typing.Dict[str, typing.Any]

@typing.type_check_only
class ParallelInstruction(typing_extensions.TypedDict, total=False):
    flatten: FlattenInstruction
    name: str
    originalName: str
    outputs: typing.List[InstructionOutput]
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
    helpText: str
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
    ]
    regexes: typing.List[str]

@typing.type_check_only
class PartialGroupByKeyInstruction(typing_extensions.TypedDict, total=False):
    input: InstructionInput
    inputElementCodec: typing.Dict[str, typing.Any]
    originalCombineValuesInputStoreName: str
    originalCombineValuesStepName: str
    sideInputs: typing.List[SideInputInfo]
    valueCombiningFn: typing.Dict[str, typing.Any]

@typing.type_check_only
class PipelineDescription(typing_extensions.TypedDict, total=False):
    displayData: typing.List[DisplayData]
    executionPipelineStage: typing.List[ExecutionStageSummary]
    originalPipelineTransform: typing.List[TransformSummary]

@typing.type_check_only
class Point(typing_extensions.TypedDict, total=False):
    time: str
    value: float

@typing.type_check_only
class Position(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ProgressTimeseries(typing_extensions.TypedDict, total=False):
    currentProgress: float
    dataPoints: typing.List[Point]

@typing.type_check_only
class PubSubIODetails(typing_extensions.TypedDict, total=False):
    subscription: str
    topic: str

@typing.type_check_only
class PubsubLocation(typing_extensions.TypedDict, total=False):
    dropLateData: bool
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
class QueryInfo(typing_extensions.TypedDict, total=False):
    queryProperty: typing.List[str]

@typing.type_check_only
class ReadInstruction(typing_extensions.TypedDict, total=False):
    source: Source

@typing.type_check_only
class ReportWorkItemStatusRequest(typing_extensions.TypedDict, total=False):
    currentWorkerTime: str
    location: str
    unifiedWorkerRequest: typing.Dict[str, typing.Any]
    workItemStatuses: typing.List[WorkItemStatus]
    workerId: str

@typing.type_check_only
class ReportWorkItemStatusResponse(typing_extensions.TypedDict, total=False):
    unifiedWorkerResponse: typing.Dict[str, typing.Any]
    workItemServiceStates: typing.List[WorkItemServiceState]

@typing.type_check_only
class ReportedParallelism(typing_extensions.TypedDict, total=False):
    isInfinite: bool
    value: float

@typing.type_check_only
class ResourceUtilizationReport(typing_extensions.TypedDict, total=False):
    containers: typing.Dict[str, typing.Any]
    cpuTime: typing.List[CPUTime]
    memoryInfo: typing.List[MemInfo]

@typing.type_check_only
class ResourceUtilizationReportResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RuntimeEnvironment(typing_extensions.TypedDict, total=False):
    additionalExperiments: typing.List[str]
    additionalUserLabels: typing.Dict[str, typing.Any]
    bypassTempDirValidation: bool
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
    subnetwork: str
    tempLocation: str
    workerRegion: str
    workerZone: str
    zone: str

@typing.type_check_only
class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    parameters: typing.List[ParameterMetadata]
    sdkInfo: SDKInfo

@typing.type_check_only
class SDKInfo(typing_extensions.TypedDict, total=False):
    language: typing_extensions.Literal["UNKNOWN", "JAVA", "PYTHON"]
    version: str

@typing.type_check_only
class SdkHarnessContainerImage(typing_extensions.TypedDict, total=False):
    containerImage: str
    environmentId: str
    useSingleCorePerContainer: bool

@typing.type_check_only
class SdkVersion(typing_extensions.TypedDict, total=False):
    sdkSupportStatus: typing_extensions.Literal[
        "UNKNOWN", "SUPPORTED", "STALE", "DEPRECATED", "UNSUPPORTED"
    ]
    version: str
    versionDisplayName: str

@typing.type_check_only
class SendDebugCaptureRequest(typing_extensions.TypedDict, total=False):
    componentId: str
    data: str
    location: str
    workerId: str

@typing.type_check_only
class SendDebugCaptureResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SendWorkerMessagesRequest(typing_extensions.TypedDict, total=False):
    location: str
    workerMessages: typing.List[WorkerMessage]

@typing.type_check_only
class SendWorkerMessagesResponse(typing_extensions.TypedDict, total=False):
    workerMessageResponses: typing.List[WorkerMessageResponse]

@typing.type_check_only
class SeqMapTask(typing_extensions.TypedDict, total=False):
    inputs: typing.List[SideInputInfo]
    name: str
    outputInfos: typing.List[SeqMapTaskOutputInfo]
    stageName: str
    systemName: str
    userFn: typing.Dict[str, typing.Any]

@typing.type_check_only
class SeqMapTaskOutputInfo(typing_extensions.TypedDict, total=False):
    sink: Sink
    tag: str

@typing.type_check_only
class ShellTask(typing_extensions.TypedDict, total=False):
    command: str
    exitCode: int

@typing.type_check_only
class SideInputInfo(typing_extensions.TypedDict, total=False):
    kind: typing.Dict[str, typing.Any]
    sources: typing.List[Source]
    tag: str

@typing.type_check_only
class Sink(typing_extensions.TypedDict, total=False):
    codec: typing.Dict[str, typing.Any]
    spec: typing.Dict[str, typing.Any]

@typing.type_check_only
class Snapshot(typing_extensions.TypedDict, total=False):
    creationTime: str
    description: str
    diskSizeBytes: str
    id: str
    projectId: str
    pubsubMetadata: typing.List[PubsubSnapshotMetadata]
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
    baseSpecs: typing.List[typing.Dict[str, typing.Any]]
    codec: typing.Dict[str, typing.Any]
    doesNotNeedSplitting: bool
    metadata: SourceMetadata
    spec: typing.Dict[str, typing.Any]

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
    bundles: typing.List[DerivedSource]
    outcome: typing_extensions.Literal[
        "SOURCE_SPLIT_OUTCOME_UNKNOWN",
        "SOURCE_SPLIT_OUTCOME_USE_CURRENT",
        "SOURCE_SPLIT_OUTCOME_SPLITTING_HAPPENED",
    ]
    shards: typing.List[SourceSplitShard]

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
class StageExecutionDetails(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workers: typing.List[WorkerDetails]

@typing.type_check_only
class StageSource(typing_extensions.TypedDict, total=False):
    name: str
    originalTransformOrCollection: str
    sizeBytes: str
    userName: str

@typing.type_check_only
class StageSummary(typing_extensions.TypedDict, total=False):
    endTime: str
    metrics: typing.List[MetricUpdate]
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

@typing.type_check_only
class StateFamilyConfig(typing_extensions.TypedDict, total=False):
    isRead: bool
    stateFamily: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    properties: typing.Dict[str, typing.Any]

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
    instructions: typing.List[ParallelInstruction]
    stageName: str
    systemName: str
    transformUserNameToStateFamily: typing.Dict[str, typing.Any]

@typing.type_check_only
class StreamingComputationRanges(typing_extensions.TypedDict, total=False):
    computationId: str
    rangeAssignments: typing.List[KeyRangeDataDiskAssignment]

@typing.type_check_only
class StreamingComputationTask(typing_extensions.TypedDict, total=False):
    computationRanges: typing.List[StreamingComputationRanges]
    dataDisks: typing.List[MountedDataDisk]
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
    streamingComputationConfigs: typing.List[StreamingComputationConfig]
    userStepToStateFamilyNameMap: typing.Dict[str, typing.Any]
    windmillServiceEndpoint: str
    windmillServicePort: str

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
class StringList(typing_extensions.TypedDict, total=False):
    elements: typing.List[str]

@typing.type_check_only
class StructuredMessage(typing_extensions.TypedDict, total=False):
    messageKey: str
    messageText: str
    parameters: typing.List[Parameter]

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
    oauthScopes: typing.List[str]
    parallelWorkerSettings: WorkerSettings
    streamingWorkerMainClass: str
    taskGroup: str
    taskUser: str
    tempStoragePrefix: str
    vmId: str
    workflowFileName: str

@typing.type_check_only
class TemplateMetadata(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    parameters: typing.List[ParameterMetadata]

@typing.type_check_only
class TemplateVersion(typing_extensions.TypedDict, total=False):
    artifact: Artifact
    createTime: str
    description: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    projectId: str
    tags: typing.List[str]
    type: typing_extensions.Literal["TEMPLATE_TYPE_UNSPECIFIED", "LEGACY", "FLEX"]
    versionId: str

@typing.type_check_only
class TopologyConfig(typing_extensions.TypedDict, total=False):
    computations: typing.List[ComputationTopology]
    dataDiskAssignments: typing.List[DataDiskAssignment]
    forwardingKeyBits: int
    persistentStateVersion: int
    userStageToComputationNameMap: typing.Dict[str, typing.Any]

@typing.type_check_only
class TransformSummary(typing_extensions.TypedDict, total=False):
    displayData: typing.List[DisplayData]
    id: str
    inputCollectionName: typing.List[str]
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
    outputCollectionName: typing.List[str]

@typing.type_check_only
class ValidateResponse(typing_extensions.TypedDict, total=False):
    errorMessage: str
    queryInfo: QueryInfo

@typing.type_check_only
class WorkItem(typing_extensions.TypedDict, total=False):
    configuration: str
    id: str
    initialReportIndex: str
    jobId: str
    leaseExpireTime: str
    mapTask: MapTask
    packages: typing.List[Package]
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
    metrics: typing.List[MetricUpdate]
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
    taskId: str

@typing.type_check_only
class WorkItemServiceState(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class WorkItemStatus(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class WorkerDetails(typing_extensions.TypedDict, total=False):
    workItems: typing.List[WorkItemDetails]
    workerName: str

@typing.type_check_only
class WorkerHealthReport(typing_extensions.TypedDict, total=False):
    msg: str
    pods: typing.List[typing.Dict[str, typing.Any]]
    reportInterval: str
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
    metadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class WorkerMessage(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    time: str
    workerHealthReport: WorkerHealthReport
    workerLifecycleEvent: WorkerLifecycleEvent
    workerMessageCode: WorkerMessageCode
    workerMetrics: ResourceUtilizationReport
    workerShutdownNotice: WorkerShutdownNotice

@typing.type_check_only
class WorkerMessageCode(typing_extensions.TypedDict, total=False):
    code: str
    parameters: typing.Dict[str, typing.Any]

@typing.type_check_only
class WorkerMessageResponse(typing_extensions.TypedDict, total=False):
    workerHealthReportResponse: WorkerHealthReportResponse
    workerMetricsResponse: ResourceUtilizationReportResponse
    workerShutdownNoticeResponse: WorkerShutdownNoticeResponse

@typing.type_check_only
class WorkerPool(typing_extensions.TypedDict, total=False):
    autoscalingSettings: AutoscalingSettings
    dataDisks: typing.List[Disk]
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
    metadata: typing.Dict[str, typing.Any]
    network: str
    numThreadsPerWorker: int
    numWorkers: int
    onHostMaintenance: str
    packages: typing.List[Package]
    poolArgs: typing.Dict[str, typing.Any]
    sdkHarnessContainerImages: typing.List[SdkHarnessContainerImage]
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
class WriteInstruction(typing_extensions.TypedDict, total=False):
    input: InstructionInput
    sink: Sink
