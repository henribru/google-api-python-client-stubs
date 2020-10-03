import typing

import typing_extensions

class ToolOutputReference(typing_extensions.TypedDict, total=False):
    output: FileReference
    testCase: TestCaseReference
    creationTime: Timestamp

class StepSummary(typing_extensions.TypedDict, total=False): ...

class ListScreenshotClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: typing.List[ScreenshotCluster]

class InAppPurchasesFound(typing_extensions.TypedDict, total=False):
    inAppPurchasesFlowsStarted: int
    inAppPurchasesFlowsExplored: int

class GraphicsStats(typing_extensions.TypedDict, total=False):
    slowUiThreadCount: str
    slowDrawCount: str
    buckets: typing.List[GraphicsStatsBucket]
    p90Millis: str
    p99Millis: str
    missedVsyncCount: str
    totalFrames: str
    p50Millis: str
    jankyFrames: str
    slowBitmapUploadCount: str
    highInputLatencyCount: str
    p95Millis: str

class InconclusiveDetail(typing_extensions.TypedDict, total=False):
    infrastructureFailure: bool
    hasErrorLogs: bool
    abortedByUser: bool

class SuggestionClusterProto(typing_extensions.TypedDict, total=False):
    suggestions: typing.List[SuggestionProto]
    category: typing_extensions.Literal[
        "unknownCategory",
        "contentLabeling",
        "touchTargetSize",
        "lowContrast",
        "implementation",
    ]

class MultiStep(typing_extensions.TypedDict, total=False):
    primaryStep: PrimaryStep
    primaryStepId: str
    multistepNumber: int

class BlankScreen(typing_extensions.TypedDict, total=False):
    screenId: str

class IosRoboTest(typing_extensions.TypedDict, total=False): ...

class Duration(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

class PerfMetricsSummary(typing_extensions.TypedDict, total=False):
    stepId: str
    projectId: str
    perfEnvironment: PerfEnvironment
    executionId: str
    graphicsStats: GraphicsStats
    perfMetrics: typing.List[str]
    historyId: str
    appStartTime: AppStartTime

class CPUInfo(typing_extensions.TypedDict, total=False):
    cpuProcessor: str
    cpuSpeedInGhz: float
    numberOfCores: int

class ListStepAccessibilityClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: typing.List[SuggestionClusterProto]
    name: str

class NonSdkApiInsight(typing_extensions.TypedDict, total=False):
    pendingGoogleUpdateInsight: PendingGoogleUpdateInsight
    exampleTraceMessages: typing.List[str]
    upgradeInsight: UpgradeInsight
    matcherId: str

class BatchCreatePerfSamplesRequest(typing_extensions.TypedDict, total=False):
    perfSamples: typing.List[PerfSample]

class StepLabelsEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class SuccessDetail(typing_extensions.TypedDict, total=False):
    otherNativeCrash: bool

class PrimaryStep(typing_extensions.TypedDict, total=False):
    individualOutcome: typing.List[IndividualOutcome]
    rollUp: typing_extensions.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]

class IndividualOutcome(typing_extensions.TypedDict, total=False):
    multistepNumber: int
    stepId: str
    runDuration: Duration
    outcomeSummary: typing_extensions.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]

class Timestamp(typing_extensions.TypedDict, total=False):
    seconds: str
    nanos: int

class EncounteredNonAndroidUiWidgetScreen(typing_extensions.TypedDict, total=False):
    distinctScreens: int
    screenIds: typing.List[str]

class ResultsStorage(typing_extensions.TypedDict, total=False):
    resultsStoragePath: FileReference
    xunitXmlFile: FileReference

class TestCaseReference(typing_extensions.TypedDict, total=False):
    className: str
    name: str
    testSuiteName: str

class UIElementTooDeep(typing_extensions.TypedDict, total=False):
    screenId: str
    screenStateId: str
    depth: int

class ListPerfSamplesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    perfSamples: typing.List[PerfSample]

class UsedRoboDirective(typing_extensions.TypedDict, total=False):
    resourceName: str

class EnvironmentDimensionValueEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class InsufficientCoverage(typing_extensions.TypedDict, total=False): ...

class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    environments: typing.List[Environment]
    projectId: str
    executionId: str
    historyId: str

class IosXcTest(typing_extensions.TypedDict, total=False):
    xcodeVersion: str
    bundleId: str

class Screen(typing_extensions.TypedDict, total=False):
    locale: str
    version: str
    fileReference: str
    model: str

class TestCase(typing_extensions.TypedDict, total=False):
    startTime: Timestamp
    stackTraces: typing.List[StackTrace]
    testCaseReference: TestCaseReference
    testCaseId: str
    status: typing_extensions.Literal["passed", "failed", "error", "skipped", "flaky"]
    endTime: Timestamp
    toolOutputs: typing.List[ToolOutputReference]
    elapsedTime: Duration
    skippedMessage: str

class NonSdkApi(typing_extensions.TypedDict, total=False):
    exampleStackTraces: typing.List[str]
    apiSignature: str
    insights: typing.List[NonSdkApiInsight]
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

class LauncherActivityNotFound(typing_extensions.TypedDict, total=False): ...

class IosAppInfo(typing_extensions.TypedDict, total=False):
    name: str

class AndroidTest(typing_extensions.TypedDict, total=False):
    testTimeout: Duration
    androidAppInfo: AndroidAppInfo
    androidInstrumentationTest: AndroidInstrumentationTest
    androidTestLoop: AndroidTestLoop
    androidRoboTest: AndroidRoboTest

class FailedToInstall(typing_extensions.TypedDict, total=False): ...

class MemoryInfo(typing_extensions.TypedDict, total=False):
    memoryCapInKibibyte: str
    memoryTotalInKibibyte: str

class Specification(typing_extensions.TypedDict, total=False):
    iosTest: IosTest
    androidTest: AndroidTest

class TestExecutionStep(typing_extensions.TypedDict, total=False):
    testTiming: TestTiming
    testIssues: typing.List[TestIssue]
    toolExecution: ToolExecution
    testSuiteOverviews: typing.List[TestSuiteOverview]

class PerformedMonkeyActions(typing_extensions.TypedDict, total=False):
    totalActions: int

class NativeCrash(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

class PerfSample(typing_extensions.TypedDict, total=False):
    sampleTime: Timestamp
    value: float

class PerfEnvironment(typing_extensions.TypedDict, total=False):
    memoryInfo: MemoryInfo
    cpuInfo: CPUInfo

class ListPerfSampleSeriesResponse(typing_extensions.TypedDict, total=False):
    perfSampleSeries: typing.List[PerfSampleSeries]

class OverlappingUIElements(typing_extensions.TypedDict, total=False):
    resourceName: typing.List[str]
    screenId: str

class PublishXunitXmlFilesRequest(typing_extensions.TypedDict, total=False):
    xunitXmlFiles: typing.List[FileReference]

class ToolExecutionStep(typing_extensions.TypedDict, total=False):
    toolExecution: ToolExecution

class BatchCreatePerfSamplesResponse(typing_extensions.TypedDict, total=False):
    perfSamples: typing.List[PerfSample]

class SuggestionProto(typing_extensions.TypedDict, total=False):
    longMessage: SafeHtmlProto
    resourceName: str
    region: RegionProto
    title: str
    screenId: str
    secondaryPriority: float
    shortMessage: SafeHtmlProto
    pseudoResourceId: str
    helpUrl: str
    priority: typing_extensions.Literal["unknownPriority", "error", "warning", "info"]

class UnusedRoboDirective(typing_extensions.TypedDict, total=False):
    resourceName: str

class Step(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    state: typing_extensions.Literal[
        "unknownState", "pending", "inProgress", "complete"
    ]
    outcome: Outcome
    labels: typing.List[StepLabelsEntry]
    stepId: str
    multiStep: MultiStep
    deviceUsageDuration: Duration
    hasImages: bool
    toolExecutionStep: ToolExecutionStep
    creationTime: Timestamp
    testExecutionStep: TestExecutionStep
    completionTime: Timestamp
    dimensionValue: typing.List[StepDimensionValueEntry]
    runDuration: Duration

class Execution(typing_extensions.TypedDict, total=False):
    outcome: Outcome
    specification: Specification
    state: typing_extensions.Literal[
        "unknownState", "pending", "inProgress", "complete"
    ]
    creationTime: Timestamp
    executionId: str
    dimensionDefinitions: typing.List[MatrixDimensionDefinition]
    testExecutionMatrixId: str
    completionTime: Timestamp

class MatrixDimensionDefinition(typing_extensions.TypedDict, total=False): ...

class ListStepsResponse(typing_extensions.TypedDict, total=False):
    steps: typing.List[Step]
    nextPageToken: str

class RoboScriptExecution(typing_extensions.TypedDict, total=False):
    successfulActions: int
    totalActions: int

class EncounteredLoginScreen(typing_extensions.TypedDict, total=False):
    distinctScreens: int
    screenIds: typing.List[str]

class ProjectSettings(typing_extensions.TypedDict, total=False):
    name: str
    defaultBucket: str

class Any(typing_extensions.TypedDict, total=False):
    value: str
    typeUrl: str

class PerfSampleSeries(typing_extensions.TypedDict, total=False):
    sampleSeriesId: str
    historyId: str
    basicPerfSampleSeries: BasicPerfSampleSeries
    executionId: str
    stepId: str
    projectId: str

class PerformedGoogleLogin(typing_extensions.TypedDict, total=False): ...

class RegionProto(typing_extensions.TypedDict, total=False):
    topPx: int
    widthPx: int
    leftPx: int
    heightPx: int

class UsedRoboIgnoreDirective(typing_extensions.TypedDict, total=False):
    resourceName: str

class FileReference(typing_extensions.TypedDict, total=False):
    fileUri: str

class StackTrace(typing_extensions.TypedDict, total=False):
    exception: str

class AndroidTestLoop(typing_extensions.TypedDict, total=False): ...

class AndroidInstrumentationTest(typing_extensions.TypedDict, total=False):
    testTargets: typing.List[str]
    useOrchestrator: bool
    testPackageId: str
    testRunnerClass: str

class StartActivityNotFound(typing_extensions.TypedDict, total=False):
    action: str
    uri: str

class MergedResult(typing_extensions.TypedDict, total=False):
    outcome: Outcome
    testSuiteOverviews: typing.List[TestSuiteOverview]
    state: typing_extensions.Literal[
        "unknownState", "pending", "inProgress", "complete"
    ]

class ListTestCasesResponse(typing_extensions.TypedDict, total=False):
    testCases: typing.List[TestCase]
    nextPageToken: str

class StepDimensionValueEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class UpgradeInsight(typing_extensions.TypedDict, total=False):
    packageName: str
    upgradeToVersion: str

class NonSdkApiUsageViolation(typing_extensions.TypedDict, total=False):
    apiSignatures: typing.List[str]
    uniqueApis: int

class TestSuiteOverview(typing_extensions.TypedDict, total=False):
    errorCount: int
    skippedCount: int
    elapsedTime: Duration
    totalCount: int
    flakyCount: int
    name: str
    xmlSource: FileReference
    failureCount: int

class FailureDetail(typing_extensions.TypedDict, total=False):
    deviceOutOfMemory: bool
    notInstalled: bool
    failedRoboscript: bool
    otherNativeCrash: bool
    timedOut: bool
    crashed: bool
    unableToCrawl: bool

class AndroidRoboTest(typing_extensions.TypedDict, total=False):
    bootstrapRunnerClass: str
    maxSteps: int
    appInitialActivity: str
    maxDepth: int
    bootstrapPackageId: str

class TestIssue(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace
    severity: typing_extensions.Literal[
        "unspecifiedSeverity", "info", "suggestion", "warning", "severe"
    ]
    category: typing_extensions.Literal["unspecifiedCategory", "common", "robo"]
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
    ]
    warning: Any
    errorMessage: str

class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    executions: typing.List[Execution]

class Environment(typing_extensions.TypedDict, total=False):
    completionTime: Timestamp
    executionId: str
    dimensionValue: typing.List[EnvironmentDimensionValueEntry]
    projectId: str
    resultsStorage: ResultsStorage
    environmentId: str
    historyId: str
    displayName: str
    creationTime: Timestamp
    environmentResult: MergedResult
    shardSummaries: typing.List[ShardSummary]

class ToolExecution(typing_extensions.TypedDict, total=False):
    commandLineArguments: typing.List[str]
    toolOutputs: typing.List[ToolOutputReference]
    toolLogs: typing.List[FileReference]
    exitCode: ToolExitCode

class GraphicsStatsBucket(typing_extensions.TypedDict, total=False):
    renderMillis: str
    frameCount: str

class SkippedDetail(typing_extensions.TypedDict, total=False):
    incompatibleAppVersion: bool
    incompatibleArchitecture: bool
    incompatibleDevice: bool

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class AndroidAppInfo(typing_extensions.TypedDict, total=False):
    versionName: str
    name: str
    versionCode: str
    packageName: str

class ListStepThumbnailsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    thumbnails: typing.List[Image]

class ShardSummary(typing_extensions.TypedDict, total=False):
    runs: typing.List[StepSummary]
    shardResult: MergedResult

class ScreenshotCluster(typing_extensions.TypedDict, total=False):
    activity: str
    clusterId: str
    screens: typing.List[Screen]
    keyScreen: Screen

class Outcome(typing_extensions.TypedDict, total=False):
    summary: typing_extensions.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]
    successDetail: SuccessDetail
    failureDetail: FailureDetail
    skippedDetail: SkippedDetail
    inconclusiveDetail: InconclusiveDetail

class ANR(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

class ToolExitCode(typing_extensions.TypedDict, total=False):
    number: int

class IosTestLoop(typing_extensions.TypedDict, total=False):
    bundleId: str

class FatalException(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

class TestTiming(typing_extensions.TypedDict, total=False):
    testProcessDuration: Duration

class SafeHtmlProto(typing_extensions.TypedDict, total=False):
    privateDoNotAccessOrElseSafeHtmlWrappedValue: str

class UnspecifiedWarning(typing_extensions.TypedDict, total=False): ...

class PendingGoogleUpdateInsight(typing_extensions.TypedDict, total=False):
    nameOfGoogleLibrary: str

class NonSdkApiUsageViolationReport(typing_extensions.TypedDict, total=False):
    uniqueApis: int
    targetSdkVersion: int
    minSdkVersion: int
    exampleApis: typing.List[NonSdkApi]

class Thumbnail(typing_extensions.TypedDict, total=False):
    contentType: str
    widthPx: int
    heightPx: int
    data: str

class History(typing_extensions.TypedDict, total=False):
    historyId: str
    name: str
    testPlatform: typing_extensions.Literal["unknownPlatform", "android", "ios"]
    displayName: str

class Image(typing_extensions.TypedDict, total=False):
    stepId: str
    sourceImage: ToolOutputReference
    thumbnail: Thumbnail
    error: Status

class ListHistoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    histories: typing.List[History]

class IosTest(typing_extensions.TypedDict, total=False):
    testTimeout: Duration
    iosTestLoop: IosTestLoop
    iosRoboTest: IosRoboTest
    iosAppInfo: IosAppInfo
    iosXcTest: IosXcTest

class AvailableDeepLinks(typing_extensions.TypedDict, total=False): ...

class CrashDialogError(typing_extensions.TypedDict, total=False):
    crashPackage: str

class IosAppCrashed(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace

class BasicPerfSampleSeries(typing_extensions.TypedDict, total=False):
    perfMetricType: typing_extensions.Literal[
        "perfMetricTypeUnspecified", "memory", "cpu", "network", "graphics"
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
    perfUnit: typing_extensions.Literal[
        "perfUnitUnspecified",
        "kibibyte",
        "percent",
        "bytesPerSecond",
        "framesPerSecond",
        "byte",
    ]

class AppStartTime(typing_extensions.TypedDict, total=False):
    fullyDrawnTime: Duration
    initialDisplayTime: Duration
