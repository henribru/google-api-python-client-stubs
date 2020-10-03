import typing

import typing_extensions

class TrafficRule(typing_extensions.TypedDict, total=False):
    burst: float
    packetLossRatio: float
    bandwidth: float
    packetDuplicationRatio: float
    delay: str

class AndroidDeviceCatalog(typing_extensions.TypedDict, total=False):
    models: typing.List[AndroidModel]
    runtimeConfiguration: AndroidRuntimeConfiguration
    versions: typing.List[AndroidVersion]

class ApkManifest(typing_extensions.TypedDict, total=False):
    maxSdkVersion: int
    minSdkVersion: int
    applicationLabel: str
    packageName: str
    intentFilters: typing.List[IntentFilter]
    targetSdkVersion: int

class XcodeVersion(typing_extensions.TypedDict, total=False):
    version: str
    tags: typing.List[str]

class FileReference(typing_extensions.TypedDict, total=False):
    gcsPath: str

class ProvidedSoftwareCatalog(typing_extensions.TypedDict, total=False):
    orchestratorVersion: str

class TestSetup(typing_extensions.TypedDict, total=False):
    dontAutograntPermissions: bool
    account: Account
    systrace: SystraceSetup
    filesToPush: typing.List[DeviceFile]
    additionalApks: typing.List[Apk]
    directoriesToPull: typing.List[str]
    environmentVariables: typing.List[EnvironmentVariable]
    networkProfile: str

class IosDevice(typing_extensions.TypedDict, total=False):
    orientation: str
    locale: str
    iosModelId: str
    iosVersionId: str

class ApkDetail(typing_extensions.TypedDict, total=False):
    apkManifest: ApkManifest

class IosXcTest(typing_extensions.TypedDict, total=False):
    appBundleId: str
    testSpecialEntitlements: bool
    testsZip: FileReference
    xcodeVersion: str
    xctestrun: FileReference

class Orientation(typing_extensions.TypedDict, total=False):
    id: str
    tags: typing.List[str]
    name: str

class IosRuntimeConfiguration(typing_extensions.TypedDict, total=False):
    locales: typing.List[Locale]
    orientations: typing.List[Orientation]

class ManualSharding(typing_extensions.TypedDict, total=False):
    testTargetsForShard: typing.List[TestTargetsForShard]

class ClientInfoDetail(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class IosTestSetup(typing_extensions.TypedDict, total=False):
    additionalIpas: typing.List[FileReference]
    networkProfile: str

class RegularFile(typing_extensions.TypedDict, total=False):
    devicePath: str
    content: FileReference

class NetworkConfigurationCatalog(typing_extensions.TypedDict, total=False):
    configurations: typing.List[NetworkConfiguration]

class AndroidVersion(typing_extensions.TypedDict, total=False):
    apiLevel: int
    distribution: Distribution
    codeName: str
    id: str
    tags: typing.List[str]
    versionString: str
    releaseDate: Date

class Shard(typing_extensions.TypedDict, total=False):
    shardIndex: int
    testTargetsForShard: TestTargetsForShard
    numShards: int

class TestSpecification(typing_extensions.TypedDict, total=False):
    iosTestSetup: IosTestSetup
    disableVideoRecording: bool
    testSetup: TestSetup
    testTimeout: str
    androidInstrumentationTest: AndroidInstrumentationTest
    iosTestLoop: IosTestLoop
    androidTestLoop: AndroidTestLoop
    androidRoboTest: AndroidRoboTest
    disablePerformanceMetrics: bool
    iosXcTest: IosXcTest

class SystraceSetup(typing_extensions.TypedDict, total=False):
    durationSeconds: int

class TestEnvironmentCatalog(typing_extensions.TypedDict, total=False):
    iosDeviceCatalog: IosDeviceCatalog
    deviceIpBlockCatalog: DeviceIpBlockCatalog
    softwareCatalog: ProvidedSoftwareCatalog
    networkConfigurationCatalog: NetworkConfigurationCatalog
    androidDeviceCatalog: AndroidDeviceCatalog

class Account(typing_extensions.TypedDict, total=False):
    googleAuto: GoogleAuto

class AndroidRoboTest(typing_extensions.TypedDict, total=False):
    appPackageId: str
    maxSteps: int
    roboScript: FileReference
    startingIntents: typing.List[RoboStartingIntent]
    appInitialActivity: str
    appBundle: AppBundle
    appApk: FileReference
    roboDirectives: typing.List[RoboDirective]
    maxDepth: int

class ClientInfo(typing_extensions.TypedDict, total=False):
    name: str
    clientInfoDetails: typing.List[ClientInfoDetail]

class Apk(typing_extensions.TypedDict, total=False):
    location: FileReference
    packageName: str

class IntentFilter(typing_extensions.TypedDict, total=False):
    mimeType: str
    actionNames: typing.List[str]
    categoryNames: typing.List[str]

class DeviceIpBlock(typing_extensions.TypedDict, total=False):
    form: typing_extensions.Literal[
        "DEVICE_FORM_UNSPECIFIED", "VIRTUAL", "PHYSICAL", "EMULATOR"
    ]
    addedDate: Date
    block: str

class GoogleAuto(typing_extensions.TypedDict, total=False): ...

class AndroidDeviceList(typing_extensions.TypedDict, total=False):
    androidDevices: typing.List[AndroidDevice]

class RoboDirective(typing_extensions.TypedDict, total=False):
    resourceName: str
    inputText: str
    actionType: typing_extensions.Literal[
        "ACTION_TYPE_UNSPECIFIED", "SINGLE_CLICK", "ENTER_TEXT", "IGNORE"
    ]

class StartActivityIntent(typing_extensions.TypedDict, total=False):
    uri: str
    categories: typing.List[str]
    action: str

class AndroidInstrumentationTest(typing_extensions.TypedDict, total=False):
    appPackageId: str
    testApk: FileReference
    testRunnerClass: str
    shardingOption: ShardingOption
    appBundle: AppBundle
    testTargets: typing.List[str]
    appApk: FileReference
    testPackageId: str
    orchestratorOption: typing_extensions.Literal[
        "ORCHESTRATOR_OPTION_UNSPECIFIED", "USE_ORCHESTRATOR", "DO_NOT_USE_ORCHESTRATOR"
    ]

class ObbFile(typing_extensions.TypedDict, total=False):
    obbFileName: str
    obb: FileReference

class GoogleCloudStorage(typing_extensions.TypedDict, total=False):
    gcsPath: str

class TestTargetsForShard(typing_extensions.TypedDict, total=False):
    testTargets: typing.List[str]

class GetApkDetailsResponse(typing_extensions.TypedDict, total=False):
    apkDetail: ApkDetail

class EnvironmentVariable(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class ToolResultsExecution(typing_extensions.TypedDict, total=False):
    executionId: str
    projectId: str
    historyId: str

class AndroidModel(typing_extensions.TypedDict, total=False):
    screenDensity: int
    supportedAbis: typing.List[str]
    screenX: int
    tags: typing.List[str]
    manufacturer: str
    supportedVersionIds: typing.List[str]
    formFactor: typing_extensions.Literal[
        "DEVICE_FORM_FACTOR_UNSPECIFIED", "PHONE", "TABLET", "WEARABLE"
    ]
    id: str
    thumbnailUrl: str
    screenY: int
    form: typing_extensions.Literal[
        "DEVICE_FORM_UNSPECIFIED", "VIRTUAL", "PHYSICAL", "EMULATOR"
    ]
    lowFpsVideoRecording: bool
    brand: str
    name: str
    codename: str

class ResultStorage(typing_extensions.TypedDict, total=False):
    toolResultsHistory: ToolResultsHistory
    resultsUrl: str
    toolResultsExecution: ToolResultsExecution
    googleCloudStorage: GoogleCloudStorage

class AndroidMatrix(typing_extensions.TypedDict, total=False):
    orientations: typing.List[str]
    androidVersionIds: typing.List[str]
    androidModelIds: typing.List[str]
    locales: typing.List[str]

class NetworkConfiguration(typing_extensions.TypedDict, total=False):
    upRule: TrafficRule
    id: str
    downRule: TrafficRule

class AppBundle(typing_extensions.TypedDict, total=False):
    bundleLocation: FileReference

class Date(typing_extensions.TypedDict, total=False):
    month: int
    year: int
    day: int

class Environment(typing_extensions.TypedDict, total=False):
    iosDevice: IosDevice
    androidDevice: AndroidDevice

class LauncherActivityIntent(typing_extensions.TypedDict, total=False): ...

class CancelTestMatrixResponse(typing_extensions.TypedDict, total=False):
    testState: typing_extensions.Literal[
        "TEST_STATE_UNSPECIFIED",
        "VALIDATING",
        "PENDING",
        "RUNNING",
        "FINISHED",
        "ERROR",
        "UNSUPPORTED_ENVIRONMENT",
        "INCOMPATIBLE_ENVIRONMENT",
        "INCOMPATIBLE_ARCHITECTURE",
        "CANCELLED",
        "INVALID",
    ]

class AndroidDevice(typing_extensions.TypedDict, total=False):
    androidVersionId: str
    androidModelId: str
    locale: str
    orientation: str

class IosDeviceCatalog(typing_extensions.TypedDict, total=False):
    xcodeVersions: typing.List[XcodeVersion]
    runtimeConfiguration: IosRuntimeConfiguration
    versions: typing.List[IosVersion]
    models: typing.List[IosModel]

class IosTestLoop(typing_extensions.TypedDict, total=False):
    appIpa: FileReference
    scenarios: typing.List[int]
    appBundleId: str

class IosModel(typing_extensions.TypedDict, total=False):
    id: str
    screenX: int
    deviceCapabilities: typing.List[str]
    tags: typing.List[str]
    supportedVersionIds: typing.List[str]
    name: str
    formFactor: typing_extensions.Literal[
        "DEVICE_FORM_FACTOR_UNSPECIFIED", "PHONE", "TABLET", "WEARABLE"
    ]
    screenY: int
    screenDensity: int

class UniformSharding(typing_extensions.TypedDict, total=False):
    numShards: int

class AndroidRuntimeConfiguration(typing_extensions.TypedDict, total=False):
    locales: typing.List[Locale]
    orientations: typing.List[Orientation]

class AndroidTestLoop(typing_extensions.TypedDict, total=False):
    scenarios: typing.List[int]
    scenarioLabels: typing.List[str]
    appPackageId: str
    appApk: FileReference
    appBundle: AppBundle

class DeviceIpBlockCatalog(typing_extensions.TypedDict, total=False):
    ipBlocks: typing.List[DeviceIpBlock]

class DeviceFile(typing_extensions.TypedDict, total=False):
    obbFile: ObbFile
    regularFile: RegularFile

class TestMatrix(typing_extensions.TypedDict, total=False):
    outcomeSummary: typing_extensions.Literal[
        "OUTCOME_SUMMARY_UNSPECIFIED", "SUCCESS", "FAILURE", "INCONCLUSIVE", "SKIPPED"
    ]
    testSpecification: TestSpecification
    invalidMatrixDetails: typing_extensions.Literal[
        "INVALID_MATRIX_DETAILS_UNSPECIFIED",
        "DETAILS_UNAVAILABLE",
        "MALFORMED_APK",
        "MALFORMED_TEST_APK",
        "NO_MANIFEST",
        "NO_PACKAGE_NAME",
        "INVALID_PACKAGE_NAME",
        "TEST_SAME_AS_APP",
        "NO_INSTRUMENTATION",
        "NO_SIGNATURE",
        "INSTRUMENTATION_ORCHESTRATOR_INCOMPATIBLE",
        "NO_TEST_RUNNER_CLASS",
        "NO_LAUNCHER_ACTIVITY",
        "FORBIDDEN_PERMISSIONS",
        "INVALID_ROBO_DIRECTIVES",
        "INVALID_RESOURCE_NAME",
        "INVALID_DIRECTIVE_ACTION",
        "TEST_LOOP_INTENT_FILTER_NOT_FOUND",
        "SCENARIO_LABEL_NOT_DECLARED",
        "SCENARIO_LABEL_MALFORMED",
        "SCENARIO_NOT_DECLARED",
        "DEVICE_ADMIN_RECEIVER",
        "MALFORMED_XC_TEST_ZIP",
        "BUILT_FOR_IOS_SIMULATOR",
        "NO_TESTS_IN_XC_TEST_ZIP",
        "USE_DESTINATION_ARTIFACTS",
        "TEST_NOT_APP_HOSTED",
        "PLIST_CANNOT_BE_PARSED",
        "TEST_ONLY_APK",
        "MALFORMED_IPA",
        "MISSING_URL_SCHEME",
        "MALFORMED_APP_BUNDLE",
        "NO_CODE_APK",
        "INVALID_INPUT_APK",
        "INVALID_APK_PREVIEW_SDK",
    ]
    projectId: str
    testMatrixId: str
    timestamp: str
    state: typing_extensions.Literal[
        "TEST_STATE_UNSPECIFIED",
        "VALIDATING",
        "PENDING",
        "RUNNING",
        "FINISHED",
        "ERROR",
        "UNSUPPORTED_ENVIRONMENT",
        "INCOMPATIBLE_ENVIRONMENT",
        "INCOMPATIBLE_ARCHITECTURE",
        "CANCELLED",
        "INVALID",
    ]
    clientInfo: ClientInfo
    environmentMatrix: EnvironmentMatrix
    flakyTestAttempts: int
    testExecutions: typing.List[TestExecution]
    resultStorage: ResultStorage

class IosDeviceList(typing_extensions.TypedDict, total=False):
    iosDevices: typing.List[IosDevice]

class EnvironmentMatrix(typing_extensions.TypedDict, total=False):
    androidDeviceList: AndroidDeviceList
    iosDeviceList: IosDeviceList
    androidMatrix: AndroidMatrix

class IosVersion(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]
    majorVersion: int
    supportedXcodeVersionIds: typing.List[str]
    id: str
    minorVersion: int

class ToolResultsHistory(typing_extensions.TypedDict, total=False):
    projectId: str
    historyId: str

class ToolResultsStep(typing_extensions.TypedDict, total=False):
    stepId: str
    projectId: str
    executionId: str
    historyId: str

class RoboStartingIntent(typing_extensions.TypedDict, total=False):
    startActivity: StartActivityIntent
    launcherActivity: LauncherActivityIntent
    timeout: str

class TestExecution(typing_extensions.TypedDict, total=False):
    testDetails: TestDetails
    matrixId: str
    id: str
    testSpecification: TestSpecification
    timestamp: str
    environment: Environment
    shard: Shard
    state: typing_extensions.Literal[
        "TEST_STATE_UNSPECIFIED",
        "VALIDATING",
        "PENDING",
        "RUNNING",
        "FINISHED",
        "ERROR",
        "UNSUPPORTED_ENVIRONMENT",
        "INCOMPATIBLE_ENVIRONMENT",
        "INCOMPATIBLE_ARCHITECTURE",
        "CANCELLED",
        "INVALID",
    ]
    projectId: str
    toolResultsStep: ToolResultsStep

class Locale(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]
    id: str
    region: str
    name: str

class ShardingOption(typing_extensions.TypedDict, total=False):
    manualSharding: ManualSharding
    uniformSharding: UniformSharding

class TestDetails(typing_extensions.TypedDict, total=False):
    progressMessages: typing.List[str]
    errorMessage: str

class Distribution(typing_extensions.TypedDict, total=False):
    marketShare: float
    measurementTime: str
