import typing

_list = list

@typing.type_check_only
class ANR(typing.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class AndroidAppInfo(typing.TypedDict, total=False):
    name: str
    packageName: str
    versionCode: str
    versionName: str

@typing.type_check_only
class AndroidInstrumentationTest(typing.TypedDict, total=False):
    testPackageId: str
    testRunnerClass: str
    testTargets: _list[str]
    useOrchestrator: bool

@typing.type_check_only
class AndroidRoboTest(typing.TypedDict, total=False):
    appInitialActivity: str
    bootstrapPackageId: str
    bootstrapRunnerClass: str
    maxDepth: int
    maxSteps: int

@typing.type_check_only
class AndroidTest(typing.TypedDict, total=False):
    androidAppInfo: AndroidAppInfo
    androidInstrumentationTest: AndroidInstrumentationTest
    androidRoboTest: AndroidRoboTest
    androidTestLoop: AndroidTestLoop
    testTimeout: Duration

@typing.type_check_only
class AndroidTestLoop(typing.TypedDict, total=False): ...

@typing.type_check_only
class AntiTamperingTermination(typing.TypedDict, total=False): ...

@typing.type_check_only
class Any(typing.TypedDict, total=False):
    typeUrl: str
    value: str

@typing.type_check_only
class AppStartTime(typing.TypedDict, total=False):
    fullyDrawnTime: Duration
    initialDisplayTime: Duration

@typing.type_check_only
class AssetIssue(typing.TypedDict, total=False): ...

@typing.type_check_only
class AvailableDeepLinks(typing.TypedDict, total=False): ...

@typing.type_check_only
class BasicPerfSampleSeries(typing.TypedDict, total=False):
    perfMetricType: typing.Literal[
        "perfMetricTypeUnspecified", "memory", "cpu", "network", "graphics"
    ]
    perfUnit: typing.Literal[
        "perfUnitUnspecified",
        "kibibyte",
        "percent",
        "bytesPerSecond",
        "framesPerSecond",
        "byte",
    ]
    sampleSeriesLabel: typing.Literal[
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
class BatchCreatePerfSamplesRequest(typing.TypedDict, total=False):
    perfSamples: _list[PerfSample]

@typing.type_check_only
class BatchCreatePerfSamplesResponse(typing.TypedDict, total=False):
    perfSamples: _list[PerfSample]

@typing.type_check_only
class BlankScreen(typing.TypedDict, total=False):
    screenId: str

@typing.type_check_only
class CPUInfo(typing.TypedDict, total=False):
    cpuProcessor: str
    cpuSpeedInGhz: float
    numberOfCores: int

@typing.type_check_only
class CrashDialogError(typing.TypedDict, total=False):
    crashPackage: str

@typing.type_check_only
class DetectedAppSplashScreen(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeviceOutOfMemory(typing.TypedDict, total=False): ...

@typing.type_check_only
class Duration(typing.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class EncounteredLoginScreen(typing.TypedDict, total=False):
    distinctScreens: int
    screenIds: _list[str]

@typing.type_check_only
class EncounteredNonAndroidUiWidgetScreen(typing.TypedDict, total=False):
    distinctScreens: int
    screenIds: _list[str]

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
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
class EnvironmentDimensionValueEntry(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class Execution(typing.TypedDict, total=False):
    completionTime: Timestamp
    creationTime: Timestamp
    dimensionDefinitions: _list[MatrixDimensionDefinition]
    executionId: str
    outcome: Outcome
    specification: Specification
    state: typing.Literal["unknownState", "pending", "inProgress", "complete"]
    testExecutionMatrixId: str

@typing.type_check_only
class FailedToInstall(typing.TypedDict, total=False): ...

@typing.type_check_only
class FailureDetail(typing.TypedDict, total=False):
    crashed: bool
    deviceOutOfMemory: bool
    failedRoboscript: bool
    notInstalled: bool
    otherNativeCrash: bool
    timedOut: bool
    unableToCrawl: bool

@typing.type_check_only
class FatalException(typing.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class FileReference(typing.TypedDict, total=False):
    fileUri: str

@typing.type_check_only
class GraphicsStats(typing.TypedDict, total=False):
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
class GraphicsStatsBucket(typing.TypedDict, total=False):
    frameCount: str
    renderMillis: str

@typing.type_check_only
class History(typing.TypedDict, total=False):
    displayName: str
    historyId: str
    name: str
    testPlatform: typing.Literal["unknownPlatform", "android", "ios"]

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    error: Status
    sourceImage: ToolOutputReference
    stepId: str
    thumbnail: Thumbnail

@typing.type_check_only
class InAppPurchasesFound(typing.TypedDict, total=False):
    inAppPurchasesFlowsExplored: int
    inAppPurchasesFlowsStarted: int

@typing.type_check_only
class InconclusiveDetail(typing.TypedDict, total=False):
    abortedByUser: bool
    hasErrorLogs: bool
    infrastructureFailure: bool

@typing.type_check_only
class IndividualOutcome(typing.TypedDict, total=False):
    multistepNumber: int
    outcomeSummary: typing.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]
    runDuration: Duration
    stepId: str

@typing.type_check_only
class InsufficientCoverage(typing.TypedDict, total=False): ...

@typing.type_check_only
class IosAppCrashed(typing.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class IosAppInfo(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class IosRoboTest(typing.TypedDict, total=False): ...

@typing.type_check_only
class IosTest(typing.TypedDict, total=False):
    iosAppInfo: IosAppInfo
    iosRoboTest: IosRoboTest
    iosTestLoop: IosTestLoop
    iosXcTest: IosXcTest
    testTimeout: Duration

@typing.type_check_only
class IosTestLoop(typing.TypedDict, total=False):
    bundleId: str

@typing.type_check_only
class IosXcTest(typing.TypedDict, total=False):
    bundleId: str
    xcodeVersion: str

@typing.type_check_only
class LauncherActivityNotFound(typing.TypedDict, total=False): ...

@typing.type_check_only
class LicensingProtectionTermination(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListEnvironmentsResponse(typing.TypedDict, total=False):
    environments: _list[Environment]
    executionId: str
    historyId: str
    nextPageToken: str
    projectId: str

@typing.type_check_only
class ListExecutionsResponse(typing.TypedDict, total=False):
    executions: _list[Execution]
    nextPageToken: str

@typing.type_check_only
class ListHistoriesResponse(typing.TypedDict, total=False):
    histories: _list[History]
    nextPageToken: str

@typing.type_check_only
class ListPerfSampleSeriesResponse(typing.TypedDict, total=False):
    perfSampleSeries: _list[PerfSampleSeries]

@typing.type_check_only
class ListPerfSamplesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    perfSamples: _list[PerfSample]

@typing.type_check_only
class ListScreenshotClustersResponse(typing.TypedDict, total=False):
    clusters: _list[ScreenshotCluster]

@typing.type_check_only
class ListStepAccessibilityClustersResponse(typing.TypedDict, total=False):
    clusters: _list[SuggestionClusterProto]
    name: str

@typing.type_check_only
class ListStepThumbnailsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    thumbnails: _list[Image]

@typing.type_check_only
class ListStepsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    steps: _list[Step]

@typing.type_check_only
class ListTestCasesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    testCases: _list[TestCase]

@typing.type_check_only
class LogcatCollectionError(typing.TypedDict, total=False): ...

@typing.type_check_only
class MatrixDimensionDefinition(typing.TypedDict, total=False): ...

@typing.type_check_only
class MemoryInfo(typing.TypedDict, total=False):
    memoryCapInKibibyte: str
    memoryTotalInKibibyte: str

@typing.type_check_only
class MergedResult(typing.TypedDict, total=False):
    outcome: Outcome
    state: typing.Literal["unknownState", "pending", "inProgress", "complete"]
    testSuiteOverviews: _list[TestSuiteOverview]

@typing.type_check_only
class MultiStep(typing.TypedDict, total=False):
    multistepNumber: int
    primaryStep: PrimaryStep
    primaryStepId: str

@typing.type_check_only
class NativeCrash(typing.TypedDict, total=False):
    stackTrace: StackTrace

@typing.type_check_only
class NonSdkApi(typing.TypedDict, total=False):
    apiSignature: str
    exampleStackTraces: _list[str]
    insights: _list[NonSdkApiInsight]
    invocationCount: int
    list: typing.Literal[
        "NONE",
        "WHITE",
        "BLACK",
        "GREY",
        "GREY_MAX_O",
        "GREY_MAX_P",
        "GREY_MAX_Q",
        "GREY_MAX_R",
        "GREY_MAX_S",
    ]

@typing.type_check_only
class NonSdkApiInsight(typing.TypedDict, total=False):
    exampleTraceMessages: _list[str]
    matcherId: str
    pendingGoogleUpdateInsight: PendingGoogleUpdateInsight
    upgradeInsight: UpgradeInsight

@typing.type_check_only
class NonSdkApiUsageViolation(typing.TypedDict, total=False):
    apiSignatures: _list[str]
    uniqueApis: int

@typing.type_check_only
class NonSdkApiUsageViolationReport(typing.TypedDict, total=False):
    exampleApis: _list[NonSdkApi]
    minSdkVersion: int
    targetSdkVersion: int
    uniqueApis: int

@typing.type_check_only
class Outcome(typing.TypedDict, total=False):
    failureDetail: FailureDetail
    inconclusiveDetail: InconclusiveDetail
    skippedDetail: SkippedDetail
    successDetail: SuccessDetail
    summary: typing.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]

@typing.type_check_only
class OverlappingUIElements(typing.TypedDict, total=False):
    resourceName: _list[str]
    screenId: str

@typing.type_check_only
class PendingGoogleUpdateInsight(typing.TypedDict, total=False):
    nameOfGoogleLibrary: str

@typing.type_check_only
class PerfEnvironment(typing.TypedDict, total=False):
    cpuInfo: CPUInfo
    memoryInfo: MemoryInfo

@typing.type_check_only
class PerfMetricsSummary(typing.TypedDict, total=False):
    appStartTime: AppStartTime
    executionId: str
    graphicsStats: GraphicsStats
    historyId: str
    perfEnvironment: PerfEnvironment
    perfMetrics: _list[
        typing.Literal[
            "perfMetricTypeUnspecified", "memory", "cpu", "network", "graphics"
        ]
    ]
    projectId: str
    stepId: str

@typing.type_check_only
class PerfSample(typing.TypedDict, total=False):
    sampleTime: Timestamp
    value: float

@typing.type_check_only
class PerfSampleSeries(typing.TypedDict, total=False):
    basicPerfSampleSeries: BasicPerfSampleSeries
    executionId: str
    historyId: str
    projectId: str
    sampleSeriesId: str
    stepId: str

@typing.type_check_only
class PerformedGoogleLogin(typing.TypedDict, total=False): ...

@typing.type_check_only
class PerformedMonkeyActions(typing.TypedDict, total=False):
    totalActions: int

@typing.type_check_only
class PrimaryStep(typing.TypedDict, total=False):
    individualOutcome: _list[IndividualOutcome]
    rollUp: typing.Literal[
        "unset", "success", "failure", "inconclusive", "skipped", "flaky"
    ]

@typing.type_check_only
class ProjectSettings(typing.TypedDict, total=False):
    defaultBucket: str
    name: str

@typing.type_check_only
class PublishXunitXmlFilesRequest(typing.TypedDict, total=False):
    xunitXmlFiles: _list[FileReference]

@typing.type_check_only
class RegionProto(typing.TypedDict, total=False):
    heightPx: int
    leftPx: int
    topPx: int
    widthPx: int

@typing.type_check_only
class ResultsStorage(typing.TypedDict, total=False):
    resultsStoragePath: FileReference
    xunitXmlFile: FileReference

@typing.type_check_only
class RoboScriptExecution(typing.TypedDict, total=False):
    successfulActions: int
    totalActions: int

@typing.type_check_only
class SafeHtmlProto(typing.TypedDict, total=False):
    privateDoNotAccessOrElseSafeHtmlWrappedValue: str

@typing.type_check_only
class Screen(typing.TypedDict, total=False):
    fileReference: str
    locale: str
    model: str
    version: str

@typing.type_check_only
class ScreenshotCluster(typing.TypedDict, total=False):
    activity: str
    clusterId: str
    keyScreen: Screen
    screens: _list[Screen]

@typing.type_check_only
class ShardSummary(typing.TypedDict, total=False):
    runs: _list[StepSummary]
    shardResult: MergedResult

@typing.type_check_only
class SkippedDetail(typing.TypedDict, total=False):
    incompatibleAppVersion: bool
    incompatibleArchitecture: bool
    incompatibleDevice: bool
    pendingTimeout: bool

@typing.type_check_only
class Specification(typing.TypedDict, total=False):
    androidTest: AndroidTest
    iosTest: IosTest

@typing.type_check_only
class StackTrace(typing.TypedDict, total=False):
    exception: str

@typing.type_check_only
class StartActivityNotFound(typing.TypedDict, total=False):
    action: str
    uri: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing.TypedDict, total=False):
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
    state: typing.Literal["unknownState", "pending", "inProgress", "complete"]
    stepId: str
    testExecutionStep: TestExecutionStep
    toolExecutionStep: ToolExecutionStep

@typing.type_check_only
class StepDimensionValueEntry(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class StepLabelsEntry(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class StepSummary(typing.TypedDict, total=False): ...

@typing.type_check_only
class SuccessDetail(typing.TypedDict, total=False):
    otherNativeCrash: bool

@typing.type_check_only
class SuggestionClusterProto(typing.TypedDict, total=False):
    category: typing.Literal[
        "unknownCategory",
        "contentLabeling",
        "touchTargetSize",
        "lowContrast",
        "implementation",
    ]
    suggestions: _list[SuggestionProto]

@typing.type_check_only
class SuggestionProto(typing.TypedDict, total=False):
    helpUrl: str
    longMessage: SafeHtmlProto
    priority: typing.Literal["unknownPriority", "error", "warning", "info"]
    pseudoResourceId: str
    region: RegionProto
    resourceName: str
    screenId: str
    secondaryPriority: float
    shortMessage: SafeHtmlProto
    title: str

@typing.type_check_only
class TestCase(typing.TypedDict, total=False):
    elapsedTime: Duration
    endTime: Timestamp
    skippedMessage: str
    stackTraces: _list[StackTrace]
    startTime: Timestamp
    status: typing.Literal["passed", "failed", "error", "skipped", "flaky"]
    testCaseId: str
    testCaseReference: TestCaseReference
    toolOutputs: _list[ToolOutputReference]

@typing.type_check_only
class TestCaseReference(typing.TypedDict, total=False):
    className: str
    name: str
    testSuiteName: str

@typing.type_check_only
class TestExecutionStep(typing.TypedDict, total=False):
    testIssues: _list[TestIssue]
    testSuiteOverviews: _list[TestSuiteOverview]
    testTiming: TestTiming
    toolExecution: ToolExecution

@typing.type_check_only
class TestIssue(typing.TypedDict, total=False):
    category: typing.Literal["unspecifiedCategory", "common", "robo"]
    errorMessage: str
    severity: typing.Literal[
        "unspecifiedSeverity", "info", "suggestion", "warning", "severe"
    ]
    stackTrace: StackTrace
    type: typing.Literal[
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
        "assetIssue",
        "licensingProtectionTermination",
        "antiTamperingTermination",
    ]
    warning_migration: Any

@typing.type_check_only
class TestSuiteOverview(typing.TypedDict, total=False):
    elapsedTime: Duration
    errorCount: int
    failureCount: int
    flakyCount: int
    name: str
    skippedCount: int
    totalCount: int
    xmlSource: FileReference

@typing.type_check_only
class TestTiming(typing.TypedDict, total=False):
    testProcessDuration: Duration

@typing.type_check_only
class Thumbnail(typing.TypedDict, total=False):
    contentType: str
    data: str
    heightPx: int
    widthPx: int

@typing.type_check_only
class Timestamp(typing.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class ToolExecution(typing.TypedDict, total=False):
    commandLineArguments: _list[str]
    exitCode: ToolExitCode
    toolLogs: _list[FileReference]
    toolOutputs: _list[ToolOutputReference]

@typing.type_check_only
class ToolExecutionStep(typing.TypedDict, total=False):
    toolExecution: ToolExecution

@typing.type_check_only
class ToolExitCode(typing.TypedDict, total=False):
    number: int

@typing.type_check_only
class ToolOutputReference(typing.TypedDict, total=False):
    creationTime: Timestamp
    output: FileReference
    testCase: TestCaseReference

@typing.type_check_only
class UIElementTooDeep(typing.TypedDict, total=False):
    depth: int
    screenId: str
    screenStateId: str

@typing.type_check_only
class UnspecifiedWarning(typing.TypedDict, total=False): ...

@typing.type_check_only
class UnusedRoboDirective(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class UpgradeInsight(typing.TypedDict, total=False):
    packageName: str
    upgradeToVersion: str

@typing.type_check_only
class UsedRoboDirective(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class UsedRoboIgnoreDirective(typing.TypedDict, total=False):
    resourceName: str
