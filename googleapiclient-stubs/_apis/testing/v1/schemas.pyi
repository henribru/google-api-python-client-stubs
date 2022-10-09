import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    googleAuto: GoogleAuto

@typing.type_check_only
class AndroidDevice(typing_extensions.TypedDict, total=False):
    androidModelId: str
    androidVersionId: str
    locale: str
    orientation: str

@typing.type_check_only
class AndroidDeviceCatalog(typing_extensions.TypedDict, total=False):
    models: _list[AndroidModel]
    runtimeConfiguration: AndroidRuntimeConfiguration
    versions: _list[AndroidVersion]

@typing.type_check_only
class AndroidDeviceList(typing_extensions.TypedDict, total=False):
    androidDevices: _list[AndroidDevice]

@typing.type_check_only
class AndroidInstrumentationTest(typing_extensions.TypedDict, total=False):
    appApk: FileReference
    appBundle: AppBundle
    appPackageId: str
    orchestratorOption: typing_extensions.Literal[
        "ORCHESTRATOR_OPTION_UNSPECIFIED", "USE_ORCHESTRATOR", "DO_NOT_USE_ORCHESTRATOR"
    ]
    shardingOption: ShardingOption
    testApk: FileReference
    testPackageId: str
    testRunnerClass: str
    testTargets: _list[str]

@typing.type_check_only
class AndroidMatrix(typing_extensions.TypedDict, total=False):
    androidModelIds: _list[str]
    androidVersionIds: _list[str]
    locales: _list[str]
    orientations: _list[str]

@typing.type_check_only
class AndroidModel(typing_extensions.TypedDict, total=False):
    brand: str
    codename: str
    form: typing_extensions.Literal[
        "DEVICE_FORM_UNSPECIFIED", "VIRTUAL", "PHYSICAL", "EMULATOR"
    ]
    formFactor: typing_extensions.Literal[
        "DEVICE_FORM_FACTOR_UNSPECIFIED", "PHONE", "TABLET", "WEARABLE"
    ]
    id: str
    lowFpsVideoRecording: bool
    manufacturer: str
    name: str
    screenDensity: int
    screenX: int
    screenY: int
    supportedAbis: _list[str]
    supportedVersionIds: _list[str]
    tags: _list[str]
    thumbnailUrl: str

@typing.type_check_only
class AndroidRoboTest(typing_extensions.TypedDict, total=False):
    appApk: FileReference
    appBundle: AppBundle
    appInitialActivity: str
    appPackageId: str
    maxDepth: int
    maxSteps: int
    roboDirectives: _list[RoboDirective]
    roboMode: typing_extensions.Literal[
        "ROBO_MODE_UNSPECIFIED", "ROBO_VERSION_1", "ROBO_VERSION_2"
    ]
    roboScript: FileReference
    startingIntents: _list[RoboStartingIntent]

@typing.type_check_only
class AndroidRuntimeConfiguration(typing_extensions.TypedDict, total=False):
    locales: _list[Locale]
    orientations: _list[Orientation]

@typing.type_check_only
class AndroidTestLoop(typing_extensions.TypedDict, total=False):
    appApk: FileReference
    appBundle: AppBundle
    appPackageId: str
    scenarioLabels: _list[str]
    scenarios: _list[int]

@typing.type_check_only
class AndroidVersion(typing_extensions.TypedDict, total=False):
    apiLevel: int
    codeName: str
    distribution: Distribution
    id: str
    releaseDate: Date
    tags: _list[str]
    versionString: str

@typing.type_check_only
class Apk(typing_extensions.TypedDict, total=False):
    location: FileReference
    packageName: str

@typing.type_check_only
class ApkDetail(typing_extensions.TypedDict, total=False):
    apkManifest: ApkManifest

@typing.type_check_only
class ApkManifest(typing_extensions.TypedDict, total=False):
    applicationLabel: str
    intentFilters: _list[IntentFilter]
    maxSdkVersion: int
    minSdkVersion: int
    packageName: str
    targetSdkVersion: int
    usesPermission: _list[str]
    versionCode: str
    versionName: str

@typing.type_check_only
class AppBundle(typing_extensions.TypedDict, total=False):
    bundleLocation: FileReference

@typing.type_check_only
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

@typing.type_check_only
class ClientInfo(typing_extensions.TypedDict, total=False):
    clientInfoDetails: _list[ClientInfoDetail]
    name: str

@typing.type_check_only
class ClientInfoDetail(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeviceFile(typing_extensions.TypedDict, total=False):
    obbFile: ObbFile
    regularFile: RegularFile

@typing.type_check_only
class DeviceIpBlock(typing_extensions.TypedDict, total=False):
    addedDate: Date
    block: str
    form: typing_extensions.Literal[
        "DEVICE_FORM_UNSPECIFIED", "VIRTUAL", "PHYSICAL", "EMULATOR"
    ]

@typing.type_check_only
class DeviceIpBlockCatalog(typing_extensions.TypedDict, total=False):
    ipBlocks: _list[DeviceIpBlock]

@typing.type_check_only
class Distribution(typing_extensions.TypedDict, total=False):
    marketShare: float
    measurementTime: str

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    androidDevice: AndroidDevice
    iosDevice: IosDevice

@typing.type_check_only
class EnvironmentMatrix(typing_extensions.TypedDict, total=False):
    androidDeviceList: AndroidDeviceList
    androidMatrix: AndroidMatrix
    iosDeviceList: IosDeviceList

@typing.type_check_only
class EnvironmentVariable(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class FileReference(typing_extensions.TypedDict, total=False):
    gcsPath: str

@typing.type_check_only
class GetApkDetailsResponse(typing_extensions.TypedDict, total=False):
    apkDetail: ApkDetail

@typing.type_check_only
class GoogleAuto(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudStorage(typing_extensions.TypedDict, total=False):
    gcsPath: str

@typing.type_check_only
class IntentFilter(typing_extensions.TypedDict, total=False):
    actionNames: _list[str]
    categoryNames: _list[str]
    mimeType: str

@typing.type_check_only
class IosDevice(typing_extensions.TypedDict, total=False):
    iosModelId: str
    iosVersionId: str
    locale: str
    orientation: str

@typing.type_check_only
class IosDeviceCatalog(typing_extensions.TypedDict, total=False):
    models: _list[IosModel]
    runtimeConfiguration: IosRuntimeConfiguration
    versions: _list[IosVersion]
    xcodeVersions: _list[XcodeVersion]

@typing.type_check_only
class IosDeviceFile(typing_extensions.TypedDict, total=False):
    bundleId: str
    content: FileReference
    devicePath: str

@typing.type_check_only
class IosDeviceList(typing_extensions.TypedDict, total=False):
    iosDevices: _list[IosDevice]

@typing.type_check_only
class IosModel(typing_extensions.TypedDict, total=False):
    deviceCapabilities: _list[str]
    formFactor: typing_extensions.Literal[
        "DEVICE_FORM_FACTOR_UNSPECIFIED", "PHONE", "TABLET", "WEARABLE"
    ]
    id: str
    name: str
    screenDensity: int
    screenX: int
    screenY: int
    supportedVersionIds: _list[str]
    tags: _list[str]

@typing.type_check_only
class IosRuntimeConfiguration(typing_extensions.TypedDict, total=False):
    locales: _list[Locale]
    orientations: _list[Orientation]

@typing.type_check_only
class IosTestLoop(typing_extensions.TypedDict, total=False):
    appBundleId: str
    appIpa: FileReference
    scenarios: _list[int]

@typing.type_check_only
class IosTestSetup(typing_extensions.TypedDict, total=False):
    additionalIpas: _list[FileReference]
    networkProfile: str
    pullDirectories: _list[IosDeviceFile]
    pushFiles: _list[IosDeviceFile]

@typing.type_check_only
class IosVersion(typing_extensions.TypedDict, total=False):
    id: str
    majorVersion: int
    minorVersion: int
    supportedXcodeVersionIds: _list[str]
    tags: _list[str]

@typing.type_check_only
class IosXcTest(typing_extensions.TypedDict, total=False):
    appBundleId: str
    testSpecialEntitlements: bool
    testsZip: FileReference
    xcodeVersion: str
    xctestrun: FileReference

@typing.type_check_only
class LauncherActivityIntent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Locale(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    region: str
    tags: _list[str]

@typing.type_check_only
class ManualSharding(typing_extensions.TypedDict, total=False):
    testTargetsForShard: _list[TestTargetsForShard]

@typing.type_check_only
class NetworkConfiguration(typing_extensions.TypedDict, total=False):
    downRule: TrafficRule
    id: str
    upRule: TrafficRule

@typing.type_check_only
class NetworkConfigurationCatalog(typing_extensions.TypedDict, total=False):
    configurations: _list[NetworkConfiguration]

@typing.type_check_only
class ObbFile(typing_extensions.TypedDict, total=False):
    obb: FileReference
    obbFileName: str

@typing.type_check_only
class Orientation(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    tags: _list[str]

@typing.type_check_only
class ProvidedSoftwareCatalog(typing_extensions.TypedDict, total=False):
    androidxOrchestratorVersion: str
    orchestratorVersion: str

@typing.type_check_only
class RegularFile(typing_extensions.TypedDict, total=False):
    content: FileReference
    devicePath: str

@typing.type_check_only
class ResultStorage(typing_extensions.TypedDict, total=False):
    googleCloudStorage: GoogleCloudStorage
    resultsUrl: str
    toolResultsExecution: ToolResultsExecution
    toolResultsHistory: ToolResultsHistory

@typing.type_check_only
class RoboDirective(typing_extensions.TypedDict, total=False):
    actionType: typing_extensions.Literal[
        "ACTION_TYPE_UNSPECIFIED", "SINGLE_CLICK", "ENTER_TEXT", "IGNORE"
    ]
    inputText: str
    resourceName: str

@typing.type_check_only
class RoboStartingIntent(typing_extensions.TypedDict, total=False):
    launcherActivity: LauncherActivityIntent
    startActivity: StartActivityIntent
    timeout: str

@typing.type_check_only
class Shard(typing_extensions.TypedDict, total=False):
    numShards: int
    shardIndex: int
    testTargetsForShard: TestTargetsForShard

@typing.type_check_only
class ShardingOption(typing_extensions.TypedDict, total=False):
    manualSharding: ManualSharding
    uniformSharding: UniformSharding

@typing.type_check_only
class StartActivityIntent(typing_extensions.TypedDict, total=False):
    action: str
    categories: _list[str]
    uri: str

@typing.type_check_only
class SystraceSetup(typing_extensions.TypedDict, total=False):
    durationSeconds: int

@typing.type_check_only
class TestDetails(typing_extensions.TypedDict, total=False):
    errorMessage: str
    progressMessages: _list[str]

@typing.type_check_only
class TestEnvironmentCatalog(typing_extensions.TypedDict, total=False):
    androidDeviceCatalog: AndroidDeviceCatalog
    deviceIpBlockCatalog: DeviceIpBlockCatalog
    iosDeviceCatalog: IosDeviceCatalog
    networkConfigurationCatalog: NetworkConfigurationCatalog
    softwareCatalog: ProvidedSoftwareCatalog

@typing.type_check_only
class TestExecution(typing_extensions.TypedDict, total=False):
    environment: Environment
    id: str
    matrixId: str
    projectId: str
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
    testDetails: TestDetails
    testSpecification: TestSpecification
    timestamp: str
    toolResultsStep: ToolResultsStep

@typing.type_check_only
class TestMatrix(typing_extensions.TypedDict, total=False):
    clientInfo: ClientInfo
    environmentMatrix: EnvironmentMatrix
    failFast: bool
    flakyTestAttempts: int
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
    outcomeSummary: typing_extensions.Literal[
        "OUTCOME_SUMMARY_UNSPECIFIED", "SUCCESS", "FAILURE", "INCONCLUSIVE", "SKIPPED"
    ]
    projectId: str
    resultStorage: ResultStorage
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
    testExecutions: _list[TestExecution]
    testMatrixId: str
    testSpecification: TestSpecification
    timestamp: str

@typing.type_check_only
class TestSetup(typing_extensions.TypedDict, total=False):
    account: Account
    additionalApks: _list[Apk]
    directoriesToPull: _list[str]
    dontAutograntPermissions: bool
    environmentVariables: _list[EnvironmentVariable]
    filesToPush: _list[DeviceFile]
    networkProfile: str
    systrace: SystraceSetup

@typing.type_check_only
class TestSpecification(typing_extensions.TypedDict, total=False):
    androidInstrumentationTest: AndroidInstrumentationTest
    androidRoboTest: AndroidRoboTest
    androidTestLoop: AndroidTestLoop
    disablePerformanceMetrics: bool
    disableVideoRecording: bool
    iosTestLoop: IosTestLoop
    iosTestSetup: IosTestSetup
    iosXcTest: IosXcTest
    testSetup: TestSetup
    testTimeout: str

@typing.type_check_only
class TestTargetsForShard(typing_extensions.TypedDict, total=False):
    testTargets: _list[str]

@typing.type_check_only
class ToolResultsExecution(typing_extensions.TypedDict, total=False):
    executionId: str
    historyId: str
    projectId: str

@typing.type_check_only
class ToolResultsHistory(typing_extensions.TypedDict, total=False):
    historyId: str
    projectId: str

@typing.type_check_only
class ToolResultsStep(typing_extensions.TypedDict, total=False):
    executionId: str
    historyId: str
    projectId: str
    stepId: str

@typing.type_check_only
class TrafficRule(typing_extensions.TypedDict, total=False):
    bandwidth: float
    burst: float
    delay: str
    packetDuplicationRatio: float
    packetLossRatio: float

@typing.type_check_only
class UniformSharding(typing_extensions.TypedDict, total=False):
    numShards: int

@typing.type_check_only
class XcodeVersion(typing_extensions.TypedDict, total=False):
    tags: _list[str]
    version: str
