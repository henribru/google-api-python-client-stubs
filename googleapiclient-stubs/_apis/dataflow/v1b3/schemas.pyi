import typing

import typing_extensions

class WriteInstruction(typing_extensions.TypedDict, total=False):
    input: InstructionInput
    sink: Sink

class CounterStructuredName(typing_extensions.TypedDict, total=False):
    originalStepName: str
    originNamespace: str
    originalRequestingStepName: str
    workerId: str
    executionStepName: str
    origin: typing_extensions.Literal["SYSTEM", "USER"]
    portion: typing_extensions.Literal["ALL", "KEY", "VALUE"]
    componentStepName: str
    inputIndex: int
    name: str

class JobExecutionDetails(typing_extensions.TypedDict, total=False):
    stages: typing.List[StageSummary]
    nextPageToken: str

class QueryInfo(typing_extensions.TypedDict, total=False):
    queryProperty: typing.List[str]

class WorkerDetails(typing_extensions.TypedDict, total=False):
    workerName: str
    workItems: typing.List[WorkItemDetails]

class JobMetadata(typing_extensions.TypedDict, total=False):
    sdkVersion: SdkVersion
    bigqueryDetails: typing.List[BigQueryIODetails]
    datastoreDetails: typing.List[DatastoreIODetails]
    pubsubDetails: typing.List[PubSubIODetails]
    bigTableDetails: typing.List[BigTableIODetails]
    fileDetails: typing.List[FileIODetails]
    spannerDetails: typing.List[SpannerIODetails]

class LaunchTemplateResponse(typing_extensions.TypedDict, total=False):
    job: Job

class ParallelInstruction(typing_extensions.TypedDict, total=False):
    parDo: ParDoInstruction
    write: WriteInstruction
    outputs: typing.List[InstructionOutput]
    read: ReadInstruction
    flatten: FlattenInstruction
    systemName: str
    originalName: str
    partialGroupByKey: PartialGroupByKeyInstruction
    name: str

class SourceSplitRequest(typing_extensions.TypedDict, total=False):
    options: SourceSplitOptions
    source: Source

class MemInfo(typing_extensions.TypedDict, total=False):
    timestamp: str
    currentRssBytes: str
    currentLimitBytes: str
    totalGbMs: str

class SourceFork(typing_extensions.TypedDict, total=False):
    residual: SourceSplitShard
    primary: SourceSplitShard
    residualSource: DerivedSource
    primarySource: DerivedSource

class MountedDataDisk(typing_extensions.TypedDict, total=False):
    dataDisk: str

class DisplayData(typing_extensions.TypedDict, total=False):
    int64Value: str
    url: str
    namespace: str
    timestampValue: str
    floatValue: float
    durationValue: str
    boolValue: bool
    strValue: str
    javaClassValue: str
    key: str
    shortStrValue: str
    label: str

class SendWorkerMessagesResponse(typing_extensions.TypedDict, total=False):
    workerMessageResponses: typing.List[WorkerMessageResponse]

class ReadInstruction(typing_extensions.TypedDict, total=False):
    source: Source

class CustomSourceLocation(typing_extensions.TypedDict, total=False):
    stateful: bool

class ListTemplateVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    templateVersions: typing.List[TemplateVersion]

class StringList(typing_extensions.TypedDict, total=False):
    elements: typing.List[str]

class Disk(typing_extensions.TypedDict, total=False):
    sizeGb: int
    diskType: str
    mountPoint: str

class SeqMapTaskOutputInfo(typing_extensions.TypedDict, total=False):
    tag: str
    sink: Sink

class ComponentSource(typing_extensions.TypedDict, total=False):
    userName: str
    originalTransformOrCollection: str
    name: str

class TransformSummary(typing_extensions.TypedDict, total=False):
    displayData: typing.List[DisplayData]
    outputCollectionName: typing.List[str]
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

class WorkerPool(typing_extensions.TypedDict, total=False):
    network: str
    zone: str
    poolArgs: typing.Dict[str, typing.Any]
    dataDisks: typing.List[Disk]
    diskType: str
    ipConfiguration: typing_extensions.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    sdkHarnessContainerImages: typing.List[SdkHarnessContainerImage]
    autoscalingSettings: AutoscalingSettings
    numWorkers: int
    onHostMaintenance: str
    numThreadsPerWorker: int
    workerHarnessContainerImage: str
    machineType: str
    metadata: typing.Dict[str, typing.Any]
    kind: str
    defaultPackageSet: typing_extensions.Literal[
        "DEFAULT_PACKAGE_SET_UNKNOWN",
        "DEFAULT_PACKAGE_SET_NONE",
        "DEFAULT_PACKAGE_SET_JAVA",
        "DEFAULT_PACKAGE_SET_PYTHON",
    ]
    packages: typing.List[Package]
    subnetwork: str
    diskSourceImage: str
    teardownPolicy: typing_extensions.Literal[
        "TEARDOWN_POLICY_UNKNOWN",
        "TEARDOWN_ALWAYS",
        "TEARDOWN_ON_SUCCESS",
        "TEARDOWN_NEVER",
    ]
    diskSizeGb: int
    taskrunnerSettings: TaskRunnerSettings

class Snapshot(typing_extensions.TypedDict, total=False):
    pubsubMetadata: typing.List[PubsubSnapshotMetadata]
    creationTime: str
    id: str
    projectId: str
    diskSizeBytes: str
    state: typing_extensions.Literal[
        "UNKNOWN_SNAPSHOT_STATE", "PENDING", "RUNNING", "READY", "FAILED", "DELETED"
    ]
    sourceJobId: str
    ttl: str
    description: str

class CreateTemplateVersionRequest(typing_extensions.TypedDict, total=False):
    templateVersion: TemplateVersion

class LaunchTemplateParameters(typing_extensions.TypedDict, total=False):
    jobName: str
    environment: RuntimeEnvironment
    update: bool
    transformNameMapping: typing.Dict[str, typing.Any]
    parameters: typing.Dict[str, typing.Any]

class LaunchFlexTemplateParameter(typing_extensions.TypedDict, total=False):
    launchOptions: typing.Dict[str, typing.Any]
    parameters: typing.Dict[str, typing.Any]
    containerSpecGcsPath: str
    jobName: str
    containerSpec: ContainerSpec
    environment: FlexTemplateRuntimeEnvironment

class WorkItemStatus(typing_extensions.TypedDict, total=False):
    sourceOperationResponse: SourceOperationResponse
    metricUpdates: typing.List[MetricUpdate]
    dynamicSourceSplit: DynamicSourceSplit
    counterUpdates: typing.List[CounterUpdate]
    stopPosition: Position
    totalThrottlerWaitTimeSeconds: float
    errors: typing.List[Status]
    workItemId: str
    progress: ApproximateProgress
    completed: bool
    sourceFork: SourceFork
    reportIndex: str
    reportedProgress: ApproximateReportedProgress
    requestedLeaseDuration: str

class CounterStructuredNameAndMetadata(typing_extensions.TypedDict, total=False):
    metadata: CounterMetadata
    name: CounterStructuredName

class MultiOutputInfo(typing_extensions.TypedDict, total=False):
    tag: str

class StreamingComputationRanges(typing_extensions.TypedDict, total=False):
    rangeAssignments: typing.List[KeyRangeDataDiskAssignment]
    computationId: str

class ProgressTimeseries(typing_extensions.TypedDict, total=False):
    dataPoints: typing.List[Point]
    currentProgress: float

class PubsubSnapshotMetadata(typing_extensions.TypedDict, total=False):
    topicName: str
    snapshotName: str
    expireTime: str

class ResourceUtilizationReport(typing_extensions.TypedDict, total=False):
    memoryInfo: typing.List[MemInfo]
    cpuTime: typing.List[CPUTime]
    containers: typing.Dict[str, typing.Any]

class CommitTemplateVersionRequest(typing_extensions.TypedDict, total=False):
    templateVersion: TemplateVersion

class Histogram(typing_extensions.TypedDict, total=False):
    bucketCounts: typing.List[str]
    firstBucketOffset: int

class FloatingPointList(typing_extensions.TypedDict, total=False):
    elements: typing.List[float]

class WorkItemDetails(typing_extensions.TypedDict, total=False):
    taskId: str
    startTime: str
    endTime: str
    attemptId: str
    metrics: typing.List[MetricUpdate]
    state: typing_extensions.Literal[
        "EXECUTION_STATE_UNKNOWN",
        "EXECUTION_STATE_NOT_STARTED",
        "EXECUTION_STATE_RUNNING",
        "EXECUTION_STATE_SUCCEEDED",
        "EXECUTION_STATE_FAILED",
        "EXECUTION_STATE_CANCELLED",
    ]
    progress: ProgressTimeseries

class SourceOperationResponse(typing_extensions.TypedDict, total=False):
    split: SourceSplitResponse
    getMetadata: SourceGetMetadataResponse

class BigTableIODetails(typing_extensions.TypedDict, total=False):
    instanceId: str
    tableId: str
    projectId: str

class WorkerMessageResponse(typing_extensions.TypedDict, total=False):
    workerHealthReportResponse: WorkerHealthReportResponse
    workerShutdownNoticeResponse: WorkerShutdownNoticeResponse
    workerMetricsResponse: ResourceUtilizationReportResponse

class PartialGroupByKeyInstruction(typing_extensions.TypedDict, total=False):
    sideInputs: typing.List[SideInputInfo]
    inputElementCodec: typing.Dict[str, typing.Any]
    valueCombiningFn: typing.Dict[str, typing.Any]
    input: InstructionInput
    originalCombineValuesStepName: str
    originalCombineValuesInputStoreName: str

class WorkerLifecycleEvent(typing_extensions.TypedDict, total=False):
    containerStartTime: str
    metadata: typing.Dict[str, typing.Any]
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

class StructuredMessage(typing_extensions.TypedDict, total=False):
    messageKey: str
    messageText: str
    parameters: typing.List[Parameter]

class FloatingPointMean(typing_extensions.TypedDict, total=False):
    sum: float
    count: SplitInt64

class ListSnapshotsResponse(typing_extensions.TypedDict, total=False):
    snapshots: typing.List[Snapshot]

class HotKeyDetection(typing_extensions.TypedDict, total=False):
    systemName: str
    hotKeyAge: str
    userStepName: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class SourceSplitShard(typing_extensions.TypedDict, total=False):
    derivationMode: typing_extensions.Literal[
        "SOURCE_DERIVATION_MODE_UNKNOWN",
        "SOURCE_DERIVATION_MODE_INDEPENDENT",
        "SOURCE_DERIVATION_MODE_CHILD_OF_CURRENT",
        "SOURCE_DERIVATION_MODE_SIBLING_OF_CURRENT",
    ]
    source: Source

class ApproximateReportedProgress(typing.Dict[str, typing.Any]): ...

class JobExecutionInfo(typing_extensions.TypedDict, total=False):
    stages: typing.Dict[str, typing.Any]

class TaskRunnerSettings(typing_extensions.TypedDict, total=False):
    streamingWorkerMainClass: str
    logUploadLocation: str
    dataflowApiVersion: str
    baseTaskDir: str
    parallelWorkerSettings: WorkerSettings
    taskUser: str
    workflowFileName: str
    languageHint: str
    baseUrl: str
    tempStoragePrefix: str
    commandlinesFileName: str
    alsologtostderr: bool
    logToSerialconsole: bool
    vmId: str
    harnessCommand: str
    taskGroup: str
    oauthScopes: typing.List[str]
    logDir: str
    continueOnException: bool

class ModifyTemplateVersionLabelRequest(typing_extensions.TypedDict, total=False):
    value: str
    op: typing_extensions.Literal["OPERATION_UNSPECIFIED", "ADD", "REMOVE"]
    key: str

class DistributionUpdate(typing_extensions.TypedDict, total=False):
    histogram: Histogram
    max: SplitInt64
    min: SplitInt64
    sumOfSquares: float
    count: SplitInt64
    sum: SplitInt64

class ModifyTemplateVersionTagResponse(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]

class StreamingStageLocation(typing_extensions.TypedDict, total=False):
    streamId: str

class ExecutionStageState(typing_extensions.TypedDict, total=False):
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
    ]
    currentStateTime: str

class AutoscalingEvent(typing_extensions.TypedDict, total=False):
    description: StructuredMessage
    eventType: typing_extensions.Literal[
        "TYPE_UNKNOWN",
        "TARGET_NUM_WORKERS_CHANGED",
        "CURRENT_NUM_WORKERS_CHANGED",
        "ACTUATION_FAILURE",
        "NO_CHANGE",
    ]
    targetNumWorkers: str
    workerPool: str
    time: str
    currentNumWorkers: str

class SeqMapTask(typing_extensions.TypedDict, total=False):
    userFn: typing.Dict[str, typing.Any]
    stageName: str
    outputInfos: typing.List[SeqMapTaskOutputInfo]
    inputs: typing.List[SideInputInfo]
    name: str
    systemName: str

class TemplateVersion(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TEMPLATE_TYPE_UNSPECIFIED", "LEGACY", "FLEX"]
    versionId: str
    displayName: str
    artifact: Artifact
    labels: typing.Dict[str, typing.Any]
    createTime: str
    description: str
    tags: typing.List[str]
    projectId: str

class LaunchFlexTemplateRequest(typing_extensions.TypedDict, total=False):
    launchParameter: LaunchFlexTemplateParameter
    validateOnly: bool

class WorkerSettings(typing_extensions.TypedDict, total=False):
    reportingEnabled: bool
    servicePath: str
    baseUrl: str
    tempStoragePrefix: str
    workerId: str
    shuffleServicePath: str

class JobMessage(typing_extensions.TypedDict, total=False):
    id: str
    time: str
    messageImportance: typing_extensions.Literal[
        "JOB_MESSAGE_IMPORTANCE_UNKNOWN",
        "JOB_MESSAGE_DEBUG",
        "JOB_MESSAGE_DETAILED",
        "JOB_MESSAGE_BASIC",
        "JOB_MESSAGE_WARNING",
        "JOB_MESSAGE_ERROR",
    ]
    messageText: str

class ContainerSpec(typing_extensions.TypedDict, total=False):
    sdkInfo: SDKInfo
    image: str
    metadata: TemplateMetadata

class FailedLocation(typing_extensions.TypedDict, total=False):
    name: str

class StreamingSideInputLocation(typing_extensions.TypedDict, total=False):
    stateFamily: str
    tag: str

class ParDoInstruction(typing_extensions.TypedDict, total=False):
    multiOutputInfos: typing.List[MultiOutputInfo]
    input: InstructionInput
    numOutputs: int
    sideInputs: typing.List[SideInputInfo]
    userFn: typing.Dict[str, typing.Any]

class SpannerIODetails(typing_extensions.TypedDict, total=False):
    projectId: str
    instanceId: str
    databaseId: str

class MapTask(typing_extensions.TypedDict, total=False):
    counterPrefix: str
    stageName: str
    instructions: typing.List[ParallelInstruction]
    systemName: str

class PubSubIODetails(typing_extensions.TypedDict, total=False):
    topic: str
    subscription: str

class ComponentTransform(typing_extensions.TypedDict, total=False):
    userName: str
    name: str
    originalTransform: str

class MetricUpdate(typing_extensions.TypedDict, total=False):
    cumulative: bool
    scalar: typing.Any
    updateTime: str
    set: typing.Any
    kind: str
    gauge: typing.Any
    meanSum: typing.Any
    distribution: typing.Any
    internal: typing.Any
    name: MetricStructuredName
    meanCount: typing.Any

class FlexTemplateRuntimeEnvironment(typing_extensions.TypedDict, total=False):
    machineType: str
    enableStreamingEngine: bool
    maxWorkers: int
    workerRegion: str
    additionalExperiments: typing.List[str]
    subnetwork: str
    workerZone: str
    network: str
    kmsKeyName: str
    tempLocation: str
    zone: str
    ipConfiguration: typing_extensions.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    additionalUserLabels: typing.Dict[str, typing.Any]
    serviceAccountEmail: str
    numWorkers: int

class ReportWorkItemStatusRequest(typing_extensions.TypedDict, total=False):
    workerId: str
    currentWorkerTime: str
    workItemStatuses: typing.List[WorkItemStatus]
    location: str
    unifiedWorkerRequest: typing.Dict[str, typing.Any]

class TemplateMetadata(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    parameters: typing.List[ParameterMetadata]

class StateFamilyConfig(typing_extensions.TypedDict, total=False):
    stateFamily: str
    isRead: bool

class GetDebugConfigResponse(typing_extensions.TypedDict, total=False):
    config: str

class ListJobMessagesResponse(typing_extensions.TypedDict, total=False):
    autoscalingEvents: typing.List[AutoscalingEvent]
    nextPageToken: str
    jobMessages: typing.List[JobMessage]

class SnapshotJobRequest(typing_extensions.TypedDict, total=False):
    snapshotSources: bool
    ttl: str
    description: str
    location: str

class MetricShortId(typing_extensions.TypedDict, total=False):
    shortId: str
    metricIndex: int

class WorkerMessage(typing_extensions.TypedDict, total=False):
    workerLifecycleEvent: WorkerLifecycleEvent
    workerHealthReport: WorkerHealthReport
    workerMetrics: ResourceUtilizationReport
    workerShutdownNotice: WorkerShutdownNotice
    workerMessageCode: WorkerMessageCode
    time: str
    labels: typing.Dict[str, typing.Any]

class ShellTask(typing_extensions.TypedDict, total=False):
    command: str
    exitCode: int

class InstructionOutput(typing_extensions.TypedDict, total=False):
    systemName: str
    codec: typing.Dict[str, typing.Any]
    originalName: str
    onlyCountValueBytes: bool
    name: str
    onlyCountKeyBytes: bool

class SideInputInfo(typing_extensions.TypedDict, total=False):
    kind: typing.Dict[str, typing.Any]
    sources: typing.List[Source]
    tag: str

class ModifyTemplateVersionTagRequest(typing_extensions.TypedDict, total=False):
    removeOnly: bool
    tag: str

class CPUTime(typing_extensions.TypedDict, total=False):
    rate: float
    totalMs: str
    timestamp: str

class SourceGetMetadataRequest(typing_extensions.TypedDict, total=False):
    source: Source

class Package(typing_extensions.TypedDict, total=False):
    name: str
    location: str

class DataDiskAssignment(typing_extensions.TypedDict, total=False):
    dataDisks: typing.List[str]
    vmInstance: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    failedLocation: typing.List[FailedLocation]
    jobs: typing.List[Job]
    nextPageToken: str

class StreamingConfigTask(typing_extensions.TypedDict, total=False):
    streamingComputationConfigs: typing.List[StreamingComputationConfig]
    maxWorkItemCommitBytes: str
    windmillServicePort: str
    userStepToStateFamilyNameMap: typing.Dict[str, typing.Any]
    getDataStreamChunkSizeBytes: str
    windmillServiceEndpoint: str
    commitStreamChunkSizeBytes: str

class StageSummary(typing_extensions.TypedDict, total=False):
    startTime: str
    progress: ProgressTimeseries
    metrics: typing.List[MetricUpdate]
    stageId: str
    state: typing_extensions.Literal[
        "EXECUTION_STATE_UNKNOWN",
        "EXECUTION_STATE_NOT_STARTED",
        "EXECUTION_STATE_RUNNING",
        "EXECUTION_STATE_SUCCEEDED",
        "EXECUTION_STATE_FAILED",
        "EXECUTION_STATE_CANCELLED",
    ]
    endTime: str

class LeaseWorkItemResponse(typing_extensions.TypedDict, total=False):
    unifiedWorkerResponse: typing.Dict[str, typing.Any]
    workItems: typing.List[WorkItem]

class TopologyConfig(typing_extensions.TypedDict, total=False):
    persistentStateVersion: int
    computations: typing.List[ComputationTopology]
    userStageToComputationNameMap: typing.Dict[str, typing.Any]
    dataDiskAssignments: typing.List[DataDiskAssignment]
    forwardingKeyBits: int

class WorkerShutdownNoticeResponse(typing_extensions.TypedDict, total=False): ...

class WorkerMessageCode(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]
    code: str

class ResourceUtilizationReportResponse(typing_extensions.TypedDict, total=False): ...

class SourceMetadata(typing_extensions.TypedDict, total=False):
    estimatedSizeBytes: str
    producesSortedKeys: bool
    infinite: bool

class WorkItemServiceState(typing_extensions.TypedDict, total=False):
    harnessData: typing.Dict[str, typing.Any]
    completeWorkStatus: Status
    suggestedStopPoint: ApproximateProgress
    leaseExpireTime: str
    suggestedStopPosition: Position
    nextReportIndex: str
    hotKeyDetection: HotKeyDetection
    reportStatusInterval: str
    metricShortId: typing.List[MetricShortId]
    splitRequest: ApproximateSplitRequest

class FileIODetails(typing_extensions.TypedDict, total=False):
    filePattern: str

class SplitInt64(typing_extensions.TypedDict, total=False):
    lowBits: int
    highBits: int

class ReportWorkItemStatusResponse(typing_extensions.TypedDict, total=False):
    workItemServiceStates: typing.List[WorkItemServiceState]
    unifiedWorkerResponse: typing.Dict[str, typing.Any]

class KeyRangeDataDiskAssignment(typing_extensions.TypedDict, total=False):
    end: str
    dataDisk: str
    start: str

class StreamingApplianceSnapshotConfig(typing_extensions.TypedDict, total=False):
    snapshotId: str
    importStateEndpoint: str

class CounterUpdate(typing_extensions.TypedDict, total=False):
    shortId: str
    floatingPointMean: FloatingPointMean
    integerGauge: IntegerGauge
    integerList: IntegerList
    stringList: StringList
    integer: SplitInt64
    internal: typing.Any
    floatingPointList: FloatingPointList
    boolean: bool
    floatingPoint: float
    distribution: DistributionUpdate
    cumulative: bool
    nameAndKind: NameAndKind
    integerMean: IntegerMean
    structuredNameAndMetadata: CounterStructuredNameAndMetadata

class ValidateResponse(typing_extensions.TypedDict, total=False):
    queryInfo: QueryInfo
    errorMessage: str

class StreamingComputationTask(typing_extensions.TypedDict, total=False):
    computationRanges: typing.List[StreamingComputationRanges]
    dataDisks: typing.List[MountedDataDisk]
    taskType: typing_extensions.Literal[
        "STREAMING_COMPUTATION_TASK_UNKNOWN",
        "STREAMING_COMPUTATION_TASK_STOP",
        "STREAMING_COMPUTATION_TASK_START",
    ]

class StageSource(typing_extensions.TypedDict, total=False):
    name: str
    sizeBytes: str
    userName: str
    originalTransformOrCollection: str

class Step(typing_extensions.TypedDict, total=False):
    kind: str
    properties: typing.Dict[str, typing.Any]
    name: str

class WorkItem(typing_extensions.TypedDict, total=False):
    reportStatusInterval: str
    shellTask: ShellTask
    leaseExpireTime: str
    packages: typing.List[Package]
    mapTask: MapTask
    streamingConfigTask: StreamingConfigTask
    streamingSetupTask: StreamingSetupTask
    sourceOperationTask: SourceOperationRequest
    seqMapTask: SeqMapTask
    projectId: str
    streamingComputationTask: StreamingComputationTask
    initialReportIndex: str
    jobId: str
    configuration: str
    id: str

class ConcatPosition(typing_extensions.TypedDict, total=False):
    index: int
    position: Position

class ComputationTopology(typing_extensions.TypedDict, total=False):
    inputs: typing.List[StreamLocation]
    keyRanges: typing.List[KeyRangeLocation]
    outputs: typing.List[StreamLocation]
    systemStageName: str
    stateFamilies: typing.List[StateFamilyConfig]
    computationId: str

class WorkerShutdownNotice(typing_extensions.TypedDict, total=False):
    reason: str

class SourceOperationRequest(typing_extensions.TypedDict, total=False):
    name: str
    stageName: str
    systemName: str
    split: SourceSplitRequest
    getMetadata: SourceGetMetadataRequest
    originalName: str

class StreamingSetupTask(typing_extensions.TypedDict, total=False):
    streamingComputationTopology: TopologyConfig
    drain: bool
    receiveWorkPort: int
    workerHarnessPort: int
    snapshotConfig: StreamingApplianceSnapshotConfig

class GetTemplateResponse(typing_extensions.TypedDict, total=False):
    runtimeMetadata: RuntimeMetadata
    status: Status
    metadata: TemplateMetadata
    templateType: typing_extensions.Literal["UNKNOWN", "LEGACY", "FLEX"]

class GetDebugConfigRequest(typing_extensions.TypedDict, total=False):
    workerId: str
    location: str
    componentId: str

class ExecutionStageSummary(typing_extensions.TypedDict, total=False):
    inputSource: typing.List[StageSource]
    componentTransform: typing.List[ComponentTransform]
    outputSource: typing.List[StageSource]
    name: str
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
    id: str
    componentSource: typing.List[ComponentSource]

class StreamLocation(typing_extensions.TypedDict, total=False):
    streamingStageLocation: StreamingStageLocation
    sideInputLocation: StreamingSideInputLocation
    pubsubLocation: PubsubLocation
    customSourceLocation: CustomSourceLocation

class PubsubLocation(typing_extensions.TypedDict, total=False):
    subscription: str
    withAttributes: bool
    timestampLabel: str
    dropLateData: bool
    idLabel: str
    topic: str
    trackingSubscription: str

class Point(typing_extensions.TypedDict, total=False):
    time: str
    value: float

class SendWorkerMessagesRequest(typing_extensions.TypedDict, total=False):
    workerMessages: typing.List[WorkerMessage]
    location: str

class DeleteSnapshotResponse(typing_extensions.TypedDict, total=False): ...

class DatastoreIODetails(typing_extensions.TypedDict, total=False):
    namespace: str
    projectId: str

class Sink(typing_extensions.TypedDict, total=False):
    codec: typing.Dict[str, typing.Any]
    spec: typing.Dict[str, typing.Any]

class DerivedSource(typing_extensions.TypedDict, total=False):
    derivationMode: typing_extensions.Literal[
        "SOURCE_DERIVATION_MODE_UNKNOWN",
        "SOURCE_DERIVATION_MODE_INDEPENDENT",
        "SOURCE_DERIVATION_MODE_CHILD_OF_CURRENT",
        "SOURCE_DERIVATION_MODE_SIBLING_OF_CURRENT",
    ]
    source: Source

class JobMetrics(typing_extensions.TypedDict, total=False):
    metrics: typing.List[MetricUpdate]
    metricTime: str

class ApproximateSplitRequest(typing.Dict[str, typing.Any]): ...

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

class WorkerHealthReportResponse(typing_extensions.TypedDict, total=False):
    reportInterval: str

class JobExecutionStageInfo(typing_extensions.TypedDict, total=False):
    stepName: typing.List[str]

class BigQueryIODetails(typing_extensions.TypedDict, total=False):
    table: str
    projectId: str
    dataset: str
    query: str

class Position(typing.Dict[str, typing.Any]): ...

class Parameter(typing_extensions.TypedDict, total=False):
    value: typing.Any
    key: str

class SourceGetMetadataResponse(typing_extensions.TypedDict, total=False):
    metadata: SourceMetadata

class StageExecutionDetails(typing_extensions.TypedDict, total=False):
    workers: typing.List[WorkerDetails]
    nextPageToken: str

class AutoscalingSettings(typing_extensions.TypedDict, total=False):
    maxNumWorkers: int
    algorithm: typing_extensions.Literal[
        "AUTOSCALING_ALGORITHM_UNKNOWN",
        "AUTOSCALING_ALGORITHM_NONE",
        "AUTOSCALING_ALGORITHM_BASIC",
    ]

class CreateJobFromTemplateRequest(typing_extensions.TypedDict, total=False):
    location: str
    environment: RuntimeEnvironment
    gcsPath: str
    jobName: str
    parameters: typing.Dict[str, typing.Any]

class ApproximateProgress(typing.Dict[str, typing.Any]): ...

class Job(typing_extensions.TypedDict, total=False):
    stepsLocation: str
    executionInfo: JobExecutionInfo
    currentStateTime: str
    labels: typing.Dict[str, typing.Any]
    tempFiles: typing.List[str]
    type: typing_extensions.Literal[
        "JOB_TYPE_UNKNOWN", "JOB_TYPE_BATCH", "JOB_TYPE_STREAMING"
    ]
    clientRequestId: str
    name: str
    stageStates: typing.List[ExecutionStageState]
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
    ]
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
    ]
    projectId: str
    pipelineDescription: PipelineDescription
    startTime: str
    replaceJobId: str
    jobMetadata: JobMetadata
    environment: Environment
    transformNameMapping: typing.Dict[str, typing.Any]
    steps: typing.List[Step]
    createTime: str
    id: str
    replacedByJobId: str
    createdFromSnapshotId: str
    location: str

class SourceSplitResponse(typing_extensions.TypedDict, total=False):
    bundles: typing.List[DerivedSource]
    shards: typing.List[SourceSplitShard]
    outcome: typing_extensions.Literal[
        "SOURCE_SPLIT_OUTCOME_UNKNOWN",
        "SOURCE_SPLIT_OUTCOME_USE_CURRENT",
        "SOURCE_SPLIT_OUTCOME_SPLITTING_HAPPENED",
    ]

class CounterMetadata(typing_extensions.TypedDict, total=False):
    otherUnits: str
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

class IntegerList(typing_extensions.TypedDict, total=False):
    elements: typing.List[SplitInt64]

class FlattenInstruction(typing_extensions.TypedDict, total=False):
    inputs: typing.List[InstructionInput]

class IntegerGauge(typing_extensions.TypedDict, total=False):
    timestamp: str
    value: SplitInt64

class LaunchFlexTemplateResponse(typing_extensions.TypedDict, total=False):
    job: Job

class LeaseWorkItemRequest(typing_extensions.TypedDict, total=False):
    workItemTypes: typing.List[str]
    workerId: str
    location: str
    unifiedWorkerRequest: typing.Dict[str, typing.Any]
    requestedLeaseDuration: str
    workerCapabilities: typing.List[str]
    currentWorkerTime: str

class KeyRangeLocation(typing_extensions.TypedDict, total=False):
    dataDisk: str
    end: str
    deprecatedPersistentDirectory: str
    start: str
    deliveryEndpoint: str

class WorkerHealthReport(typing_extensions.TypedDict, total=False):
    reportInterval: str
    pods: typing.List[typing.Dict[str, typing.Any]]
    msg: str
    vmIsBroken: bool
    vmIsHealthy: bool
    vmStartupTime: str

class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    sdkInfo: SDKInfo
    parameters: typing.List[ParameterMetadata]

class StreamingComputationConfig(typing_extensions.TypedDict, total=False):
    systemName: str
    stageName: str
    transformUserNameToStateFamily: typing.Dict[str, typing.Any]
    computationId: str
    instructions: typing.List[ParallelInstruction]

class PipelineDescription(typing_extensions.TypedDict, total=False):
    executionPipelineStage: typing.List[ExecutionStageSummary]
    originalPipelineTransform: typing.List[TransformSummary]
    displayData: typing.List[DisplayData]

class IntegerMean(typing_extensions.TypedDict, total=False):
    sum: SplitInt64
    count: SplitInt64

class ParameterMetadata(typing_extensions.TypedDict, total=False):
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
    label: str
    isOptional: bool
    name: str
    helpText: str
    regexes: typing.List[str]

class SDKInfo(typing_extensions.TypedDict, total=False):
    language: typing_extensions.Literal["UNKNOWN", "JAVA", "PYTHON"]
    version: str

class RuntimeEnvironment(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    numWorkers: int
    additionalUserLabels: typing.Dict[str, typing.Any]
    network: str
    bypassTempDirValidation: bool
    additionalExperiments: typing.List[str]
    enableStreamingEngine: bool
    workerZone: str
    maxWorkers: int
    workerRegion: str
    zone: str
    machineType: str
    tempLocation: str
    ipConfiguration: typing_extensions.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    subnetwork: str
    serviceAccountEmail: str

class SendDebugCaptureResponse(typing_extensions.TypedDict, total=False): ...

class SdkHarnessContainerImage(typing_extensions.TypedDict, total=False):
    useSingleCorePerContainer: bool
    containerImage: str

class Source(typing_extensions.TypedDict, total=False):
    doesNotNeedSplitting: bool
    metadata: SourceMetadata
    codec: typing.Dict[str, typing.Any]
    baseSpecs: typing.List[typing.Dict[str, typing.Any]]
    spec: typing.Dict[str, typing.Any]

class ReportedParallelism(typing_extensions.TypedDict, total=False):
    isInfinite: bool
    value: float

class DynamicSourceSplit(typing_extensions.TypedDict, total=False):
    residual: DerivedSource
    primary: DerivedSource

class SourceSplitOptions(typing_extensions.TypedDict, total=False):
    desiredBundleSizeBytes: str
    desiredShardSizeBytes: str

class Artifact(typing_extensions.TypedDict, total=False):
    metadata: TemplateMetadata
    containerSpec: ContainerSpec
    jobGraphGcsPath: str

class InstructionInput(typing_extensions.TypedDict, total=False):
    producerInstructionIndex: int
    outputNum: int

class Environment(typing_extensions.TypedDict, total=False):
    serviceAccountEmail: str
    userAgent: typing.Dict[str, typing.Any]
    sdkPipelineOptions: typing.Dict[str, typing.Any]
    internalExperiments: typing.Dict[str, typing.Any]
    serviceKmsKeyName: str
    tempStoragePrefix: str
    workerPools: typing.List[WorkerPool]
    clusterManagerApiService: str
    version: typing.Dict[str, typing.Any]
    workerRegion: str
    experiments: typing.List[str]
    flexResourceSchedulingGoal: typing_extensions.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    dataset: str
    workerZone: str

class SendDebugCaptureRequest(typing_extensions.TypedDict, total=False):
    location: str
    data: str
    componentId: str
    workerId: str

class MetricStructuredName(typing_extensions.TypedDict, total=False):
    name: str
    origin: str
    context: typing.Dict[str, typing.Any]

class ModifyTemplateVersionLabelResponse(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

class SdkVersion(typing_extensions.TypedDict, total=False):
    version: str
    versionDisplayName: str
    sdkSupportStatus: typing_extensions.Literal[
        "UNKNOWN", "SUPPORTED", "STALE", "DEPRECATED", "UNSUPPORTED"
    ]
