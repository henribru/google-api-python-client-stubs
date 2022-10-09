import typing

import typing_extensions

_list = list

@typing.type_check_only
class ANR(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class AndroidAppInfo(typing_extensions.TypedDict, total=False):
    name: str
    packageName: str
    versionCode: str
    versionName: str

@typing.type_check_only
class AndroidInstrumentationTest(typing_extensions.TypedDict, total=False):
    testPackageId: str
    testRunnerClass: str
    testTargets: _list[str]
    useOrchestrator: bool

@typing.type_check_only
class AndroidRoboTest(typing_extensions.TypedDict, total=False):
    appInitialActivity: str
    bootstrapPackageId: str
    bootstrapRunnerClass: str
    maxDepth: int
    maxSteps: int

@typing.type_check_only
class AndroidTest(typing_extensions.TypedDict, total=False):
    androidAppInfo: AndroidAppInfo
    androidInstrumentationTest: AndroidInstrumentationTest
    androidRoboTest: AndroidRoboTest
    androidTestLoop: AndroidTestLoop
    testTimeout: Duration

@typing.type_check_only
class AndroidTestLoop(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Any(typing_extensions.TypedDict, total=False):
    typeUrl: str
    value: str

@typing.type_check_only
class AppStartTime(typing_extensions.TypedDict, total=False):
    fullyDrawnTime: Duration
    initialDisplayTime: Duration

@typing.type_check_only
class AvailableDeepLinks(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BasicPerfSampleSeries(typing_extensions.TypedDict, total=False):
    perfMetricType: typing_extensions.Literal[
        "perfMetricTypeUnspecified", "memory", "cpu", "network", "graphics"
    ]
    perfUnit: typing_extensions.Literal[
        "perfUnitUnspecified",
        "kibibyte",
        "percent",
        "bytesPerSecond",
        "framesPerSecond",
        "byte",
    ]
    sampleSeriesLabel: typing_extensions.Literal[
        "sampleSeriesTypeUnspecified",
        "memoryRssPrivate",
        "memoryRssShared",
        "memoryRssTotal",
        "memoryTotal",
        "cpuUser",
        "cpuKernel",
        "cpuTotal",
        "ntBytesTransferred",
        "ntBytesReceived",
        "networkSent",
        "networkReceived",
        "graphicsFrameRate",
    ]

@typing.type_check_only
class BatchCreatePerfSamplesRequest(typing_extensions.TypedDict, total=False):
    perfSamples: _list[PerfSample]

@typing.type_check_only
class BatchCreatePerfSamplesResponse(typing_extensions.TypedDict, total=False):
    perfSamples: _list[PerfSample]

@typing.type_check_only
class BlankScreen(typing_extensions.TypedDict, total=False):
    screenId: str

@typing.type_check_only
class CPUInfo(typing_extensions.TypedDict, total=False):
    cpuProcessor: str
    cpuSpeedInGhz: float
    numberOfCores: int

@typing.type_check_only
class CrashDialogError(typing_extensions.TypedDict, total=False):
    crashPackage: str

@typing.type_check_only
class DetectedAppSplashScreen(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeviceOutOfMemory(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Duration(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class EncounteredLoginScreen(typing_extensions.TypedDict, total=False):
    distinctScreens: int
    screenIds: _list[str]

@typing.type_check_only
class EncounteredNonAndroidUiWidgetScreen(typing_extensions.TypedDict, total=False):
    distinctScreens: int
    screenIds: _list[str]

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    completionTime: Timestamp
    creationTime: Timestamp
    dimensionValue: _list[EnvironmentDimensionValueEntry]
    displayName: str
    environmentId: str
    environmentResult: MergedResult
    executionId: str
    historyId: str
    projectId: str
    resultsStorage: ResultsStorage
    shardSummaries: _list[ShardSummary]

@typing.type_check_only
class EnvironmentDimensionValueEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class Execution(typing_extensions.TypedDict, total=False):
    completionTime: Timestamp
    creationTime: Timestamp
    dimensionDefinitions: _list[MatrixDimensionDefinition]
    executionId: str
    outcome: Outcome
    specification: Specification
    state: typing_extensions.Literal[
        "unknownState", "pending", "inProgress", "complete"
    ]
    testExecutionMatrixId: str

@typing.type_check_only
class FailedToInstall(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FailureDetail(typing_extensions.TypedDict, total=False):
    crashed: bool
    deviceOutOfMemory: bool
    failedRoboscript: bool
    notInstalled: bool
    otherNativeCrash: bool
    timedOut: bool
    unableToCrawl: bool

@typing.type_check_only
class FatalException(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class FileReference(typing_extensions.TypedDict, total=False):
    fileUri: str

@typing.type_check_only
class GraphicsStats(typing_extensions.TypedDict, total=False):
    buckets: _list[GraphicsStatsBucket]
    highInputLatencyCount: str
    jankyFrames: str
    missedVsyncCount: str
    p50Millis: str
    p90Millis: str
    p95Millis: str
    p99Millis: str
    slowBitmapUploadCount: str
    slowDrawCount: str
    slowUiThreadCount: str
    totalFrames: str

@typing.type_check_only
class GraphicsStatsBucket(typing_extensions.TypedDict, total=False):
    frameCount: str
    renderMillis: str

@typing.type_check_only
class History(typing_extensions.TypedDict, total=False):
    displayName: str
    historyId: str
    name: str
    testPlatform: typing_extensions.Literal["unknownPlatform", "android", "ios"]

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    error: Status
    sourceImage: ToolOutputReference
    stepId: str
    thumbnail: Thumbnail

@typing.type_check_only
class InAppPurchasesFound(typing_extensions.TypedDict, total=False):
    inAppPurchasesFlowsExplored: int
    inAppPurchasesFlowsStarted: int

@typing.type_check_only
class InconclusiveDetail(typing_extensions.TypedDict, total=False):
    abortedByUser: bool
    hasErrorLogs: bool
    infrastructureFailure: bool

@typing.type_check_only
class IndividualOutcome(typing_extensions.TypedDict, total=False):
    multistepNumber: int
    outcomeSummary: typing_extensions.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]
    runDuration: Duration
    stepId: str

@typing.type_check_only
class InsufficientCoverage(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class IosAppCrashed(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class IosAppInfo(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class IosRoboTest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class IosTest(typing_extensions.TypedDict, total=False):
    iosAppInfo: IosAppInfo
    iosRoboTest: IosRoboTest
    iosTestLoop: IosTestLoop
    iosXcTest: IosXcTest
    testTimeout: Duration

@typing.type_check_only
class IosTestLoop(typing_extensions.TypedDict, total=False):
    bundleId: str

@typing.type_check_only
class IosXcTest(typing_extensions.TypedDict, total=False):
    bundleId: str
    xcodeVersion: str

@typing.type_check_only
class LauncherActivityNotFound(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: _list[Environment]
    executionId: str
    historyId: str
    nextPageToken: str
    projectId: str

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: _list[Execution]
    nextPageToken: str

@typing.type_check_only
class ListHistoriesResponse(typing_extensions.TypedDict, total=False):
    histories: _list[History]
    nextPageToken: str

@typing.type_check_only
class ListPerfSampleSeriesResponse(typing_extensions.TypedDict, total=False):
    perfSampleSeries: _list[PerfSampleSeries]

@typing.type_check_only
class ListPerfSamplesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    perfSamples: _list[PerfSample]

@typing.type_check_only
class ListScreenshotClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[ScreenshotCluster]

@typing.type_check_only
class ListStepAccessibilityClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[SuggestionClusterProto]
    name: str

@typing.type_check_only
class ListStepThumbnailsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    thumbnails: _list[Image]

@typing.type_check_only
class ListStepsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    steps: _list[Step]

@typing.type_check_only
class ListTestCasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    testCases: _list[TestCase]

@typing.type_check_only
class LogcatCollectionError(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MatrixDimensionDefinition(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MemoryInfo(typing_extensions.TypedDict, total=False):
    memoryCapInKibibyte: str
    memoryTotalInKibibyte: str

@typing.type_check_only
class MergedResult(typing_extensions.TypedDict, total=False):
    outcome: Outcome
    state: typing_extensions.Literal[
        "unknownState", "pending", "inProgress", "complete"
    ]
    testSuiteOverviews: _list[TestSuiteOverview]

@typing.type_check_only
class MultiStep(typing_extensions.TypedDict, total=False):
    multistepNumber: int
    primaryStep: PrimaryStep
    primaryStepId: str

@typing.type_check_only
class NativeCrash(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class NonSdkApi(typing_extensions.TypedDict, total=False):
    apiSignature: str
    exampleStackTraces: _list[str]
    insights: _list[NonSdkApiInsight]
    invocationCount: int
    list: typing_extensions.Literal[
        "NONE",
        "WHITE",
        "BLACK",
        "GREY",
        "GREY_MAX_O",
        "GREY_MAX_P",
        "GREY_MAX_Q",
        "GREY_MAX_R",
    ]

@typing.type_check_only
class NonSdkApiInsight(typing_extensions.TypedDict, total=False):
    exampleTraceMessages: _list[str]
    matcherId: str
    pendingGoogleUpdateInsight: PendingGoogleUpdateInsight
    upgradeInsight: UpgradeInsight

@typing.type_check_only
class NonSdkApiUsageViolation(typing_extensions.TypedDict, total=False):
    apiSignatures: _list[str]
    uniqueApis: int

@typing.type_check_only
class NonSdkApiUsageViolationReport(typing_extensions.TypedDict, total=False):
    exampleApis: _list[NonSdkApi]
    minSdkVersion: int
    targetSdkVersion: int
    uniqueApis: int

@typing.type_check_only
class Outcome(typing_extensions.TypedDict, total=False):
    failureDetail: FailureDetail
    inconclusiveDetail: InconclusiveDetail
    skippedDetail: SkippedDetail
    successDetail: SuccessDetail
    summary: typing_extensions.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]

@typing.type_check_only
class OverlappingUIElements(typing_extensions.TypedDict, total=False):
    resourceName: _list[str]
    screenId: str

@typing.type_check_only
class PendingGoogleUpdateInsight(typing_extensions.TypedDict, total=False):
    nameOfGoogleLibrary: str

@typing.type_check_only
class PerfEnvironment(typing_extensions.TypedDict, total=False):
    cpuInfo: CPUInfo
    memoryInfo: MemoryInfo

@typing.type_check_only
class PerfMetricsSummary(typing_extensions.TypedDict, total=False):
    appStartTime: AppStartTime
    executionId: str
    graphicsStats: GraphicsStats
    historyId: str
    perfEnvironment: PerfEnvironment
    perfMetrics: _list[str]
    projectId: str
    stepId: str

@typing.type_check_only
class PerfSample(typing_extensions.TypedDict, total=False):
    sampleTime: Timestamp
    value: float

@typing.type_check_only
class PerfSampleSeries(typing_extensions.TypedDict, total=False):
    basicPerfSampleSeries: BasicPerfSampleSeries
    executionId: str
    historyId: str
    projectId: str
    sampleSeriesId: str
    stepId: str

@typing.type_check_only
class PerformedGoogleLogin(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PerformedMonkeyActions(typing_extensions.TypedDict, total=False):
    totalActions: int

@typing.type_check_only
class PrimaryStep(typing_extensions.TypedDict, total=False):
    individualOutcome: _list[IndividualOutcome]
    rollUp: typing_extensions.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]

@typing.type_check_only
class ProjectSettings(typing_extensions.TypedDict, total=False):
    defaultBucket: str
    name: str

@typing.type_check_only
class PublishXunitXmlFilesRequest(typing_extensions.TypedDict, total=False):
    xunitXmlFiles: _list[FileReference]

@typing.type_check_only
class RegionProto(typing_extensions.TypedDict, total=False):
    heightPx: int
    leftPx: int
    topPx: int
    widthPx: int

@typing.type_check_only
class ResultsStorage(typing_extensions.TypedDict, total=False):
    resultsStoragePath: FileReference
    xunitXmlFile: FileReference

@typing.type_check_only
class RoboScriptExecution(typing_extensions.TypedDict, total=False):
    successfulActions: int
    totalActions: int

@typing.type_check_only
class SafeHtmlProto(typing_extensions.TypedDict, total=False):
    privateDoNotAccessOrElseSafeHtmlWrappedValue: str

@typing.type_check_only
class Screen(typing_extensions.TypedDict, total=False):
    fileReference: str
    locale: str
    model: str
    version: str

@typing.type_check_only
class ScreenshotCluster(typing_extensions.TypedDict, total=False):
    activity: str
    clusterId: str
    keyScreen: Screen
    screens: _list[Screen]

@typing.type_check_only
class ShardSummary(typing_extensions.TypedDict, total=False):
    runs: _list[StepSummary]
    shardResult: MergedResult

@typing.type_check_only
class SkippedDetail(typing_extensions.TypedDict, total=False):
    incompatibleAppVersion: bool
    incompatibleArchitecture: bool
    incompatibleDevice: bool

@typing.type_check_only
class Specification(typing_extensions.TypedDict, total=False):
    androidTest: AndroidTest
    iosTest: IosTest

@typing.type_check_only
class StackTrace(typing_extensions.TypedDict, total=False):
    exception: str

@typing.type_check_only
class StartActivityNotFound(typing_extensions.TypedDict, total=False):
    action: str
    uri: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing_extensions.TypedDict, total=False):
    completionTime: Timestamp
    creationTime: Timestamp
    description: str
    deviceUsageDuration: Duration
    dimensionValue: _list[StepDimensionValueEntry]
    hasImages: bool
    labels: _list[StepLabelsEntry]
    multiStep: MultiStep
    name: str
    outcome: Outcome
    runDuration: Duration
    state: typing_extensions.Literal[
        "unknownState", "pending", "inProgress", "complete"
    ]
    stepId: str
    testExecutionStep: TestExecutionStep
    toolExecutionStep: ToolExecutionStep

@typing.type_check_only
class StepDimensionValueEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class StepLabelsEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class StepSummary(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SuccessDetail(typing_extensions.TypedDict, total=False):
    otherNativeCrash: bool

@typing.type_check_only
class SuggestionClusterProto(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "unknownCategory",
        "contentLabeling",
        "touchTargetSize",
        "lowContrast",
        "implementation",
    ]
    suggestions: _list[SuggestionProto]

@typing.type_check_only
class SuggestionProto(typing_extensions.TypedDict, total=False):
    helpUrl: str
    longMessage: SafeHtmlProto
    priority: typing_extensions.Literal["unknownPriority", "error", "warning", "info"]
    pseudoResourceId: str
    region: RegionProto
    resourceName: str
    screenId: str
    secondaryPriority: float
    shortMessage: SafeHtmlProto
    title: str

@typing.type_check_only
class TestCase(typing_extensions.TypedDict, total=False):
    elapsedTime: Duration
    endTime: Timestamp
    skippedMessage: str
    stackTraces: _list[StackTrace]
    startTime: Timestamp
    status: typing_extensions.Literal["passed", "failed", "error", "skipped", "flaky"]
    testCaseId: str
    testCaseReference: TestCaseReference
    toolOutputs: _list[ToolOutputReference]

@typing.type_check_only
class TestCaseReference(typing_extensions.TypedDict, total=False):
    className: str
    name: str
    testSuiteName: str

@typing.type_check_only
class TestExecutionStep(typing_extensions.TypedDict, total=False):
    testIssues: _list[TestIssue]
    testSuiteOverviews: _list[TestSuiteOverview]
    testTiming: TestTiming
    toolExecution: ToolExecution

@typing.type_check_only
class TestIssue(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal["unspecifiedCategory", "common", "robo"]
    errorMessage: str
    severity: typing_extensions.Literal[
        "unspecifiedSeverity", "info", "suggestion", "warning", "severe"
    ]
    stackTrace: StackTrace
    type: typing_extensions.Literal[
        "unspecifiedType",
        "fatalException",
        "nativeCrash",
        "anr",
        "unusedRoboDirective",
        "compatibleWithOrchestrator",
        "launcherActivityNotFound",
        "startActivityNotFound",
        "incompleteRoboScriptExecution",
        "completeRoboScriptExecution",
        "failedToInstall",
        "availableDeepLinks",
        "nonSdkApiUsageViolation",
        "nonSdkApiUsageReport",
        "encounteredNonAndroidUiWidgetScreen",
        "encounteredLoginScreen",
        "performedGoogleLogin",
        "iosException",
        "iosCrash",
        "performedMonkeyActions",
        "usedRoboDirective",
        "usedRoboIgnoreDirective",
        "insufficientCoverage",
        "inAppPurchases",
        "crashDialogError",
        "uiElementsTooDeep",
        "blankScreen",
        "overlappingUiElements",
        "unityException",
        "deviceOutOfMemory",
        "logcatCollectionError",
        "detectedAppSplashScreen",
    ]
    warning: Any

@typing.type_check_only
class TestSuiteOverview(typing_extensions.TypedDict, total=False):
    elapsedTime: Duration
    errorCount: int
    failureCount: int
    flakyCount: int
    name: str
    skippedCount: int
    totalCount: int
    xmlSource: FileReference

@typing.type_check_only
class TestTiming(typing_extensions.TypedDict, total=False):
    testProcessDuration: Duration

@typing.type_check_only
class Thumbnail(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    heightPx: int
    widthPx: int

@typing.type_check_only
class Timestamp(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class ToolExecution(typing_extensions.TypedDict, total=False):
    commandLineArguments: _list[str]
    exitCode: ToolExitCode
    toolLogs: _list[FileReference]
    toolOutputs: _list[ToolOutputReference]

@typing.type_check_only
class ToolExecutionStep(typing_extensions.TypedDict, total=False):
    toolExecution: ToolExecution

@typing.type_check_only
class ToolExitCode(typing_extensions.TypedDict, total=False):
    number: int

@typing.type_check_only
class ToolOutputReference(typing_extensions.TypedDict, total=False):
    creationTime: Timestamp
    output: FileReference
    testCase: TestCaseReference

@typing.type_check_only
class UIElementTooDeep(typing_extensions.TypedDict, total=False):
    depth: int
    screenId: str
    screenStateId: str

@typing.type_check_only
class UnspecifiedWarning(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UnusedRoboDirective(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class UpgradeInsight(typing_extensions.TypedDict, total=False):
    packageName: str
    upgradeToVersion: str

@typing.type_check_only
class UsedRoboDirective(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class UsedRoboIgnoreDirective(typing_extensions.TypedDict, total=False):
    resourceName: str
