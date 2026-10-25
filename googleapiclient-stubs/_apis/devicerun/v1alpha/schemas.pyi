import typing

_list = list

@typing.type_check_only
class AllocationConfig(typing.TypedDict, total=False):
    deviceConfigs: _list[DeviceConfig]

@typing.type_check_only
class AndroidBugreportDeviceAction(typing.TypedDict, total=False):
    collectOnPass: bool

@typing.type_check_only
class AndroidDumpsysDeviceAction(typing.TypedDict, total=False):
    collectOnPass: bool

@typing.type_check_only
class AndroidInstallPackagesDeviceAction(typing.TypedDict, total=False):
    installables: _list[AndroidInstallable]
    postTargetAppInstallables: _list[AndroidInstallable]
    preTargetAppInstallables: _list[AndroidInstallable]
    targetApp: AndroidInstallable

@typing.type_check_only
class AndroidInstallable(typing.TypedDict, total=False):
    files: _list[InputFile]

@typing.type_check_only
class AndroidInstrumentationTest(typing.TypedDict, total=False):
    additionalTestOptions: dict[str, typing.Any]
    enableCodeCoverage: bool
    instrumentationTimeout: str
    orchestratorVersion: str
    smartSharding: AndroidInstrumentationTestSmartSharding
    testInstallable: AndroidInstallable
    testRunnerClass: str
    testTargets: _list[str]
    uniformSharding: AndroidInstrumentationTestUniformSharding

@typing.type_check_only
class AndroidInstrumentationTestSmartSharding(typing.TypedDict, total=False):
    maxShardCount: int
    targetedShardDuration: str
    timingRecord: InputFile

@typing.type_check_only
class AndroidInstrumentationTestUniformSharding(typing.TypedDict, total=False):
    shardCount: int

@typing.type_check_only
class AndroidLogcatDeviceAction(typing.TypedDict, total=False): ...

@typing.type_check_only
class AndroidMockLocationDeviceAction(typing.TypedDict, total=False):
    location: LatLng

@typing.type_check_only
class AndroidNativeBinary(typing.TypedDict, total=False):
    androidNativeBinary: InputFile
    args: _list[str]
    envVars: dict[str, typing.Any]
    executionTimeout: str

@typing.type_check_only
class AndroidOrientationDeviceAction(typing.TypedDict, total=False):
    orientation: str

@typing.type_check_only
class AndroidPullFilesDeviceAction(typing.TypedDict, total=False):
    paths: _list[str]

@typing.type_check_only
class AndroidPushFilesDeviceAction(typing.TypedDict, total=False):
    fileConfigs: _list[AndroidPushFilesDeviceActionFileConfig]

@typing.type_check_only
class AndroidPushFilesDeviceActionFileConfig(typing.TypedDict, total=False):
    destinationPath: str
    sourceFile: InputFile

@typing.type_check_only
class AndroidRecordVideoDeviceAction(typing.TypedDict, total=False):
    discardOnPass: bool

@typing.type_check_only
class AndroidSwitchLocaleDeviceAction(typing.TypedDict, total=False):
    localeCode: str

@typing.type_check_only
class BatchGetSessionsResponse(typing.TypedDict, total=False):
    sessions: _list[Session]

@typing.type_check_only
class CancelSessionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelSessionResponse(typing.TypedDict, total=False):
    cancelResult: typing.Literal[
        "CANCEL_RESULT_UNSPECIFIED", "SESSION_MARKED_AS_CANCELLED", "SESSION_FINISHED"
    ]

@typing.type_check_only
class CatalogAndroidDeviceDetails(typing.TypedDict, total=False):
    buildType: str
    supportedAbis: _list[str]

@typing.type_check_only
class CatalogAndroidxTestOrchestratorDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class CatalogAutomationSupport(typing.TypedDict, total=False): ...

@typing.type_check_only
class CatalogDevice(typing.TypedDict, total=False):
    accessDeniedReasons: _list[
        typing.Literal["ACCESS_DENIED_REASON_UNSPECIFIED", "EULA_NOT_ACCEPTED"]
    ]
    androidDetails: CatalogAndroidDeviceDetails
    availability: CatalogDeviceAvailability
    displayName: str
    formFactor: typing.Literal[
        "FORM_FACTOR_UNSPECIFIED", "PHONE", "TABLET", "WEARABLE", "TV"
    ]
    hardwareType: typing.Literal["HARDWARE_TYPE_UNSPECIFIED", "PHYSICAL", "VIRTUAL"]
    iosDetails: CatalogIosDeviceDetails
    labInfo: CatalogLabInfo
    labels: dict[str, typing.Any]
    lifecycle: CatalogLifecycle
    manufacturer: str
    modelCode: str
    name: str
    osVersion: str
    platform: typing.Literal["PLATFORM_UNSPECIFIED", "ANDROID", "IOS"]
    primaryScreen: CatalogScreenMetrics
    supportedProducts: _list[CatalogSupportedProduct]

@typing.type_check_only
class CatalogDeviceAvailability(typing.TypedDict, total=False):
    available: typing.Literal[
        "AVAILABILITY_UNSPECIFIED",
        "AVAILABILITY_NONE",
        "AVAILABILITY_LOW",
        "AVAILABILITY_MEDIUM",
        "AVAILABILITY_HIGH",
    ]
    capacity: typing.Literal[
        "CAPACITY_UNSPECIFIED",
        "CAPACITY_NONE",
        "CAPACITY_LOW",
        "CAPACITY_MEDIUM",
        "CAPACITY_HIGH",
    ]

@typing.type_check_only
class CatalogDeviceStreamingSupport(typing.TypedDict, total=False):
    minimumAndroidStudioVersion: str

@typing.type_check_only
class CatalogIosDeviceDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class CatalogLabInfo(typing.TypedDict, total=False):
    displayName: str
    regionCode: str

@typing.type_check_only
class CatalogLifecycle(typing.TypedDict, total=False):
    removalDate: Date
    state: typing.Literal["STATE_UNSPECIFIED", "PREVIEW", "ACTIVE", "DEPRECATED"]

@typing.type_check_only
class CatalogListDevicesResponse(typing.TypedDict, total=False):
    devices: _list[CatalogDevice]
    nextPageToken: str

@typing.type_check_only
class CatalogListSoftwareVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    softwareVersions: _list[CatalogSoftwareVersion]

@typing.type_check_only
class CatalogScreenMetrics(typing.TypedDict, total=False):
    densityDpi: int
    heightPx: int
    widthPx: int

@typing.type_check_only
class CatalogSoftwareVersion(typing.TypedDict, total=False):
    androidxTestOrchestratorDetails: CatalogAndroidxTestOrchestratorDetails
    displayName: str
    isDefault: bool
    lifecycle: CatalogLifecycle
    name: str
    softwareType: typing.Literal[
        "SOFTWARE_TYPE_UNSPECIFIED", "ANDROIDX_TEST_ORCHESTRATOR", "XCODE"
    ]
    version: str
    xcodeDetails: CatalogXcodeDetails

@typing.type_check_only
class CatalogSupportedProduct(typing.TypedDict, total=False):
    automation: CatalogAutomationSupport
    deviceStreaming: CatalogDeviceStreamingSupport

@typing.type_check_only
class CatalogXcodeDetails(typing.TypedDict, total=False):
    supportedIosVersions: _list[str]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeviceAction(typing.TypedDict, total=False):
    androidBugreport: AndroidBugreportDeviceAction
    androidDumpsys: AndroidDumpsysDeviceAction
    androidInstallPackages: AndroidInstallPackagesDeviceAction
    androidLogcat: AndroidLogcatDeviceAction
    androidMockLocation: AndroidMockLocationDeviceAction
    androidOrientation: AndroidOrientationDeviceAction
    androidPullFiles: AndroidPullFilesDeviceAction
    androidPushFiles: AndroidPushFilesDeviceAction
    androidRecordVideo: AndroidRecordVideoDeviceAction
    androidSwitchLocale: AndroidSwitchLocaleDeviceAction
    iosAppPrivacyReport: IosAppPrivacyReportDeviceAction
    iosInstallPackages: IosInstallPackagesDeviceAction
    iosPullFiles: IosPullFilesDeviceAction
    iosPushFiles: IosPushFilesDeviceAction
    iosRecordVideo: IosRecordVideoDeviceAction
    iosSwitchLocale: IosSwitchLocaleDeviceAction

@typing.type_check_only
class DeviceConfig(typing.TypedDict, total=False):
    actions: _list[DeviceAction]
    requirement: DeviceRequirement

@typing.type_check_only
class DeviceRequirement(typing.TypedDict, total=False):
    deviceId: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExecutionReport(typing.TypedDict, total=False):
    displayName: str
    endTime: str
    id: str
    outputFiles: _list[OutputFile]
    result: Result
    startTime: str
    status: Status
    warnings: _list[Warning]

@typing.type_check_only
class GcsPath(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class InputFile(typing.TypedDict, total=False):
    gcsInputFile: GcsPath

@typing.type_check_only
class IosAppPrivacyReportDeviceAction(typing.TypedDict, total=False): ...

@typing.type_check_only
class IosInstallPackagesDeviceAction(typing.TypedDict, total=False):
    ipas: _list[InputFile]

@typing.type_check_only
class IosPullFilesDeviceAction(typing.TypedDict, total=False):
    paths: _list[IosPullFilesDeviceActionPathConfig]

@typing.type_check_only
class IosPullFilesDeviceActionPathConfig(typing.TypedDict, total=False):
    bundleId: str
    devicePath: str

@typing.type_check_only
class IosPushFilesDeviceAction(typing.TypedDict, total=False):
    fileConfigs: _list[IosPushFilesDeviceActionFileConfig]

@typing.type_check_only
class IosPushFilesDeviceActionFileConfig(typing.TypedDict, total=False):
    bundleId: str
    destinationPath: str
    sourceFile: InputFile

@typing.type_check_only
class IosRecordVideoDeviceAction(typing.TypedDict, total=False):
    discardOnPass: bool

@typing.type_check_only
class IosSwitchLocaleDeviceAction(typing.TypedDict, total=False):
    localeCode: str

@typing.type_check_only
class IosXcTest(typing.TypedDict, total=False):
    testsZip: InputFile
    xcTestTimeout: str
    xcodeVersion: str
    xctestrun: InputFile

@typing.type_check_only
class IssueSummary(typing.TypedDict, total=False):
    message: str
    metadata: dict[str, typing.Any]
    reason: str
    type: typing.Literal["ISSUE_TYPE_UNSPECIFIED", "INFRA", "CUSTOMER"]

@typing.type_check_only
class JobAction(typing.TypedDict, total=False):
    androidInstrumentationTest: AndroidInstrumentationTest
    androidNativeBinary: AndroidNativeBinary
    iosXcTest: IosXcTest

@typing.type_check_only
class JobConfig(typing.TypedDict, total=False):
    action: JobAction
    allocationConfig: AllocationConfig
    displayName: str
    labels: dict[str, typing.Any]
    settings: JobSettings

@typing.type_check_only
class JobReport(typing.TypedDict, total=False):
    displayName: str
    endTime: str
    executionReports: _list[ExecutionReport]
    id: str
    labels: dict[str, typing.Any]
    outputFiles: _list[OutputFile]
    result: Result
    startTime: str
    status: Status
    warnings: _list[Warning]

@typing.type_check_only
class JobSettings(typing.TypedDict, total=False):
    retrySettings: RetrySettings

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[Session]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class OutputFile(typing.TypedDict, total=False):
    gcsOutputFile: GcsPath

@typing.type_check_only
class Result(typing.TypedDict, total=False):
    cause: ResultCause
    resultType: typing.Literal[
        "RESULT_TYPE_UNSPECIFIED", "PASSED", "FAILED", "ERROR", "TIMED_OUT", "CANCELLED"
    ]

@typing.type_check_only
class ResultCause(typing.TypedDict, total=False):
    summary: IssueSummary

@typing.type_check_only
class RetrySettings(typing.TypedDict, total=False):
    flakyTestRetryStrategy: RetrySettingsFlakyTestRetryStrategy

@typing.type_check_only
class RetrySettingsFlakyTestRetryStrategy(typing.TypedDict, total=False):
    flakyTestAttempts: int
    parallelRetry: bool
    testReductionMode: typing.Literal[
        "TEST_REDUCTION_MODE_UNSPECIFIED", "NO_REDUCTION", "REDUCE_TO_FAILED_TEST_CASES"
    ]

@typing.type_check_only
class Session(typing.TypedDict, total=False):
    createTime: str
    name: str
    sessionConfig: SessionConfig
    sessionReport: SessionReport

@typing.type_check_only
class SessionConfig(typing.TypedDict, total=False):
    displayName: str
    jobConfigs: _list[JobConfig]
    notificationConfig: SessionConfigSessionNotificationConfig
    outputDirectoryConfig: SessionConfigSessionOutputFileDirectoryConfig

@typing.type_check_only
class SessionConfigSessionNotificationConfig(typing.TypedDict, total=False):
    pubsubTopic: _list[str]

@typing.type_check_only
class SessionConfigSessionOutputFileDirectoryConfig(typing.TypedDict, total=False):
    flatDirectoryStructure: bool
    gcsOutputDirectory: GcsPath

@typing.type_check_only
class SessionReport(typing.TypedDict, total=False):
    endTime: str
    id: str
    jobReports: _list[JobReport]
    result: Result
    startTime: str
    status: Status

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    progressMessages: _list[str]
    statusType: typing.Literal[
        "STATUS_TYPE_UNSPECIFIED", "PENDING", "RUNNING", "DONE", "SUSPENDED"
    ]

@typing.type_check_only
class Warning(typing.TypedDict, total=False):
    summary: IssueSummary
