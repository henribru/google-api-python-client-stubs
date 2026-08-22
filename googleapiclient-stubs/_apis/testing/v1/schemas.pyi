import typing

_list = list

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    googleAuto: GoogleAuto

@typing.type_check_only
class AndroidDevice(typing.TypedDict, total=False):
    androidModelId: str
    androidVersionId: str
    locale: str
    orientation: str

@typing.type_check_only
class AndroidDeviceCatalog(typing.TypedDict, total=False):
    models: _list[AndroidModel]
    runtimeConfiguration: AndroidRuntimeConfiguration
    versions: _list[AndroidVersion]

@typing.type_check_only
class AndroidDeviceList(typing.TypedDict, total=False):
    androidDevices: _list[AndroidDevice]

@typing.type_check_only
class AndroidInstrumentationTest(typing.TypedDict, total=False):
    appApk: FileReference
    appBundle: AppBundle
    appPackageId: str
    orchestratorOption: typing.Literal[
        "ORCHESTRATOR_OPTION_UNSPECIFIED", "USE_ORCHESTRATOR", "DO_NOT_USE_ORCHESTRATOR"
    ]
    shardingOption: ShardingOption
    testApk: FileReference
    testPackageId: str
    testRunnerClass: str
    testTargets: _list[str]

@typing.type_check_only
class AndroidMatrix(typing.TypedDict, total=False):
    androidModelIds: _list[str]
    androidVersionIds: _list[str]
    locales: _list[str]
    orientations: _list[str]

@typing.type_check_only
class AndroidModel(typing.TypedDict, total=False):
    accessDeniedReasons: _list[
        typing.Literal["ACCESS_DENIED_REASON_UNSPECIFIED", "EULA_NOT_ACCEPTED"]
    ]
    brand: str
    codename: str
    form: typing.Literal["DEVICE_FORM_UNSPECIFIED", "VIRTUAL", "PHYSICAL", "EMULATOR"]
    formFactor: typing.Literal[
        "DEVICE_FORM_FACTOR_UNSPECIFIED",
        "PHONE",
        "TABLET",
        "WEARABLE",
        "TV",
        "AUTOMOTIVE",
        "DESKTOP",
        "XR",
    ]
    id: str
    labInfo: LabInfo
    lowFpsVideoRecording: bool
    manufacturer: str
    name: str
    perVersionInfo: _list[PerAndroidVersionInfo]
    screenDensity: int
    screenX: int
    screenY: int
    supportedAbis: _list[str]
    supportedVersionIds: _list[str]
    tags: _list[str]
    thumbnailUrl: str

@typing.type_check_only
class AndroidRoboTest(typing.TypedDict, total=False):
    appApk: FileReference
    appBundle: AppBundle
    appInitialActivity: str
    appPackageId: str
    maxDepth: int
    maxSteps: int
    roboDirectives: _list[RoboDirective]
    roboMode: typing.Literal[
        "ROBO_MODE_UNSPECIFIED", "ROBO_VERSION_1", "ROBO_VERSION_2"
    ]
    roboScript: FileReference
    startingIntents: _list[RoboStartingIntent]

@typing.type_check_only
class AndroidRuntimeConfiguration(typing.TypedDict, total=False):
    locales: _list[Locale]
    orientations: _list[Orientation]

@typing.type_check_only
class AndroidTestLoop(typing.TypedDict, total=False):
    appApk: FileReference
    appBundle: AppBundle
    appPackageId: str
    scenarioLabels: _list[str]
    scenarios: _list[int]

@typing.type_check_only
class AndroidVersion(typing.TypedDict, total=False):
    apiLevel: int
    codeName: str
    distribution: Distribution
    id: str
    releaseDate: Date
    tags: _list[str]
    versionString: str

@typing.type_check_only
class Apk(typing.TypedDict, total=False):
    location: FileReference
    packageName: str

@typing.type_check_only
class ApkDetail(typing.TypedDict, total=False):
    apkManifest: ApkManifest

@typing.type_check_only
class ApkManifest(typing.TypedDict, total=False):
    applicationLabel: str
    intentFilters: _list[IntentFilter]
    maxSdkVersion: int
    metadata: _list[Metadata]
    minSdkVersion: int
    packageName: str
    services: _list[Service]
    targetSdkVersion: int
    usesFeature: _list[UsesFeature]
    usesPermission: _list[str]
    usesPermissionTags: _list[UsesPermissionTag]
    versionCode: str
    versionName: str

@typing.type_check_only
class ApkSplits(typing.TypedDict, total=False):
    bundleSplits: _list[FileReference]

@typing.type_check_only
class AppBundle(typing.TypedDict, total=False):
    apks: ApkSplits
    bundleLocation: FileReference

@typing.type_check_only
class CancelDeviceSessionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelTestMatrixResponse(typing.TypedDict, total=False):
    testState: typing.Literal[
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
class ClientInfo(typing.TypedDict, total=False):
    clientInfoDetails: _list[ClientInfoDetail]
    name: str

@typing.type_check_only
class ClientInfoDetail(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeviceFile(typing.TypedDict, total=False):
    obbFile: ObbFile
    regularFile: RegularFile

@typing.type_check_only
class DeviceIpBlock(typing.TypedDict, total=False):
    addedDate: Date
    block: str
    form: typing.Literal["DEVICE_FORM_UNSPECIFIED", "VIRTUAL", "PHYSICAL", "EMULATOR"]

@typing.type_check_only
class DeviceIpBlockCatalog(typing.TypedDict, total=False):
    ipBlocks: _list[DeviceIpBlock]

@typing.type_check_only
class DeviceSession(typing.TypedDict, total=False):
    activeStartTime: str
    androidDevice: AndroidDevice
    createTime: str
    displayName: str
    expireTime: str
    inactivityTimeout: str
    name: str
    state: typing.Literal[
        "SESSION_STATE_UNSPECIFIED",
        "REQUESTED",
        "PENDING",
        "ACTIVE",
        "EXPIRED",
        "FINISHED",
        "UNAVAILABLE",
        "ERROR",
    ]
    stateHistories: _list[SessionStateEvent]
    ttl: str

@typing.type_check_only
class DirectAccessVersionInfo(typing.TypedDict, total=False):
    directAccessSupported: bool
    minimumAndroidStudioVersion: str

@typing.type_check_only
class Distribution(typing.TypedDict, total=False):
    marketShare: float
    measurementTime: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    androidDevice: AndroidDevice
    iosDevice: IosDevice

@typing.type_check_only
class EnvironmentMatrix(typing.TypedDict, total=False):
    androidDeviceList: AndroidDeviceList
    androidMatrix: AndroidMatrix
    iosDeviceList: IosDeviceList

@typing.type_check_only
class EnvironmentVariable(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class FileReference(typing.TypedDict, total=False):
    gcsPath: str

@typing.type_check_only
class GetApkDetailsResponse(typing.TypedDict, total=False):
    apkDetail: ApkDetail

@typing.type_check_only
class GoogleAuto(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudStorage(typing.TypedDict, total=False):
    gcsPath: str

@typing.type_check_only
class IntentFilter(typing.TypedDict, total=False):
    actionNames: _list[str]
    categoryNames: _list[str]
    mimeType: str

@typing.type_check_only
class IosDevice(typing.TypedDict, total=False):
    iosModelId: str
    iosVersionId: str
    locale: str
    orientation: str

@typing.type_check_only
class IosDeviceCatalog(typing.TypedDict, total=False):
    models: _list[IosModel]
    runtimeConfiguration: IosRuntimeConfiguration
    versions: _list[IosVersion]
    xcodeVersions: _list[XcodeVersion]

@typing.type_check_only
class IosDeviceFile(typing.TypedDict, total=False):
    bundleId: str
    content: FileReference
    devicePath: str

@typing.type_check_only
class IosDeviceList(typing.TypedDict, total=False):
    iosDevices: _list[IosDevice]

@typing.type_check_only
class IosModel(typing.TypedDict, total=False):
    deviceCapabilities: _list[str]
    formFactor: typing.Literal[
        "DEVICE_FORM_FACTOR_UNSPECIFIED",
        "PHONE",
        "TABLET",
        "WEARABLE",
        "TV",
        "AUTOMOTIVE",
        "DESKTOP",
        "XR",
    ]
    id: str
    name: str
    perVersionInfo: _list[PerIosVersionInfo]
    screenDensity: int
    screenX: int
    screenY: int
    supportedVersionIds: _list[str]
    tags: _list[str]

@typing.type_check_only
class IosRoboTest(typing.TypedDict, total=False):
    appBundleId: str
    appIpa: FileReference
    roboScript: FileReference

@typing.type_check_only
class IosRuntimeConfiguration(typing.TypedDict, total=False):
    locales: _list[Locale]
    orientations: _list[Orientation]

@typing.type_check_only
class IosTestLoop(typing.TypedDict, total=False):
    appBundleId: str
    appIpa: FileReference
    scenarios: _list[int]

@typing.type_check_only
class IosTestSetup(typing.TypedDict, total=False):
    additionalIpas: _list[FileReference]
    networkProfile: str
    pullDirectories: _list[IosDeviceFile]
    pushFiles: _list[IosDeviceFile]

@typing.type_check_only
class IosVersion(typing.TypedDict, total=False):
    id: str
    majorVersion: int
    minorVersion: int
    supportedXcodeVersionIds: _list[str]
    tags: _list[str]

@typing.type_check_only
class IosXcTest(typing.TypedDict, total=False):
    appBundleId: str
    testSpecialEntitlements: bool
    testsZip: FileReference
    xcodeVersion: str
    xctestrun: FileReference

@typing.type_check_only
class LabInfo(typing.TypedDict, total=False):
    name: str
    regionCode: str

@typing.type_check_only
class LauncherActivityIntent(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListDeviceSessionsResponse(typing.TypedDict, total=False):
    deviceSessions: _list[DeviceSession]
    nextPageToken: str

@typing.type_check_only
class Locale(typing.TypedDict, total=False):
    id: str
    name: str
    region: str
    tags: _list[str]

@typing.type_check_only
class ManualSharding(typing.TypedDict, total=False):
    testTargetsForShard: _list[TestTargetsForShard]

@typing.type_check_only
class MatrixErrorDetail(typing.TypedDict, total=False):
    message: str
    reason: str

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class NetworkConfiguration(typing.TypedDict, total=False):
    downRule: TrafficRule
    id: str
    upRule: TrafficRule

@typing.type_check_only
class NetworkConfigurationCatalog(typing.TypedDict, total=False):
    configurations: _list[NetworkConfiguration]

@typing.type_check_only
class NoActivityIntent(typing.TypedDict, total=False): ...

@typing.type_check_only
class ObbFile(typing.TypedDict, total=False):
    obb: FileReference
    obbFileName: str

@typing.type_check_only
class Orientation(typing.TypedDict, total=False):
    id: str
    name: str
    tags: _list[str]

@typing.type_check_only
class PerAndroidVersionInfo(typing.TypedDict, total=False):
    deviceCapacity: typing.Literal[
        "DEVICE_CAPACITY_UNSPECIFIED",
        "DEVICE_CAPACITY_HIGH",
        "DEVICE_CAPACITY_MEDIUM",
        "DEVICE_CAPACITY_LOW",
        "DEVICE_CAPACITY_NONE",
    ]
    directAccessVersionInfo: DirectAccessVersionInfo
    interactiveDeviceAvailabilityEstimate: str
    versionId: str

@typing.type_check_only
class PerIosVersionInfo(typing.TypedDict, total=False):
    deviceCapacity: typing.Literal[
        "DEVICE_CAPACITY_UNSPECIFIED",
        "DEVICE_CAPACITY_HIGH",
        "DEVICE_CAPACITY_MEDIUM",
        "DEVICE_CAPACITY_LOW",
        "DEVICE_CAPACITY_NONE",
    ]
    versionId: str

@typing.type_check_only
class ProvidedSoftwareCatalog(typing.TypedDict, total=False):
    androidxOrchestratorVersion: str
    orchestratorVersion: str

@typing.type_check_only
class RegularFile(typing.TypedDict, total=False):
    content: FileReference
    devicePath: str

@typing.type_check_only
class ResultStorage(typing.TypedDict, total=False):
    googleCloudStorage: GoogleCloudStorage
    resultsUrl: str
    toolResultsExecution: ToolResultsExecution
    toolResultsHistory: ToolResultsHistory

@typing.type_check_only
class RoboDirective(typing.TypedDict, total=False):
    actionType: typing.Literal[
        "ACTION_TYPE_UNSPECIFIED", "SINGLE_CLICK", "ENTER_TEXT", "IGNORE"
    ]
    inputText: str
    resourceName: str

@typing.type_check_only
class RoboStartingIntent(typing.TypedDict, total=False):
    launcherActivity: LauncherActivityIntent
    noActivity: NoActivityIntent
    startActivity: StartActivityIntent
    timeout: str

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    intentFilter: _list[IntentFilter]
    name: str

@typing.type_check_only
class SessionStateEvent(typing.TypedDict, total=False):
    eventTime: str
    sessionState: typing.Literal[
        "SESSION_STATE_UNSPECIFIED",
        "REQUESTED",
        "PENDING",
        "ACTIVE",
        "EXPIRED",
        "FINISHED",
        "UNAVAILABLE",
        "ERROR",
    ]
    stateMessage: str

@typing.type_check_only
class Shard(typing.TypedDict, total=False):
    estimatedShardDuration: str
    numShards: int
    shardIndex: int
    testTargetsForShard: TestTargetsForShard

@typing.type_check_only
class ShardingOption(typing.TypedDict, total=False):
    manualSharding: ManualSharding
    smartSharding: SmartSharding
    uniformSharding: UniformSharding

@typing.type_check_only
class SmartSharding(typing.TypedDict, total=False):
    targetedShardDuration: str

@typing.type_check_only
class StartActivityIntent(typing.TypedDict, total=False):
    action: str
    categories: _list[str]
    uri: str

@typing.type_check_only
class SystraceSetup(typing.TypedDict, total=False):
    durationSeconds: int

@typing.type_check_only
class TestDetails(typing.TypedDict, total=False):
    errorMessage: str
    progressMessages: _list[str]

@typing.type_check_only
class TestEnvironmentCatalog(typing.TypedDict, total=False):
    androidDeviceCatalog: AndroidDeviceCatalog
    deviceIpBlockCatalog: DeviceIpBlockCatalog
    iosDeviceCatalog: IosDeviceCatalog
    networkConfigurationCatalog: NetworkConfigurationCatalog
    softwareCatalog: ProvidedSoftwareCatalog

@typing.type_check_only
class TestExecution(typing.TypedDict, total=False):
    environment: Environment
    id: str
    matrixId: str
    projectId: str
    shard: Shard
    state: typing.Literal[
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
class TestMatrix(typing.TypedDict, total=False):
    clientInfo: ClientInfo
    environmentMatrix: EnvironmentMatrix
    extendedInvalidMatrixDetails: _list[MatrixErrorDetail]
    failFast: bool
    flakyTestAttempts: int
    invalidMatrixDetails: typing.Literal[
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
        "MATRIX_TOO_LARGE",
        "TEST_QUOTA_EXCEEDED",
        "SERVICE_NOT_ACTIVATED",
        "UNKNOWN_PERMISSION_ERROR",
    ]
    outcomeSummary: typing.Literal[
        "OUTCOME_SUMMARY_UNSPECIFIED", "SUCCESS", "FAILURE", "INCONCLUSIVE", "SKIPPED"
    ]
    projectId: str
    resultStorage: ResultStorage
    state: typing.Literal[
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
class TestSetup(typing.TypedDict, total=False):
    account: Account
    additionalApks: _list[Apk]
    directoriesToPull: _list[str]
    dontAutograntPermissions: bool
    environmentVariables: _list[EnvironmentVariable]
    filesToPush: _list[DeviceFile]
    initialSetupApks: _list[Apk]
    networkProfile: str
    systrace: SystraceSetup

@typing.type_check_only
class TestSpecification(typing.TypedDict, total=False):
    androidInstrumentationTest: AndroidInstrumentationTest
    androidRoboTest: AndroidRoboTest
    androidTestLoop: AndroidTestLoop
    disablePerformanceMetrics: bool
    disableVideoRecording: bool
    iosRoboTest: IosRoboTest
    iosTestLoop: IosTestLoop
    iosTestSetup: IosTestSetup
    iosXcTest: IosXcTest
    testSetup: TestSetup
    testTimeout: str

@typing.type_check_only
class TestTargetsForShard(typing.TypedDict, total=False):
    testTargets: _list[str]

@typing.type_check_only
class ToolResultsExecution(typing.TypedDict, total=False):
    executionId: str
    historyId: str
    projectId: str

@typing.type_check_only
class ToolResultsHistory(typing.TypedDict, total=False):
    historyId: str
    projectId: str

@typing.type_check_only
class ToolResultsStep(typing.TypedDict, total=False):
    executionId: str
    historyId: str
    projectId: str
    stepId: str

@typing.type_check_only
class TrafficRule(typing.TypedDict, total=False):
    bandwidth: float
    burst: float
    delay: str
    packetDuplicationRatio: float
    packetLossRatio: float

@typing.type_check_only
class UniformSharding(typing.TypedDict, total=False):
    numShards: int

@typing.type_check_only
class UsesFeature(typing.TypedDict, total=False):
    isRequired: bool
    name: str

@typing.type_check_only
class UsesPermissionTag(typing.TypedDict, total=False):
    maxSdkVersion: int
    name: str

@typing.type_check_only
class XcodeVersion(typing.TypedDict, total=False):
    tags: _list[str]
    version: str
