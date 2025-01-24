import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleChromeManagementV1AndroidAppInfo(typing_extensions.TypedDict, total=False):
    permissions: _list[GoogleChromeManagementV1AndroidAppPermission]

@typing.type_check_only
class GoogleChromeManagementV1AndroidAppPermission(
    typing_extensions.TypedDict, total=False
):
    type: str

@typing.type_check_only
class GoogleChromeManagementV1AppDetails(typing_extensions.TypedDict, total=False):
    androidAppInfo: GoogleChromeManagementV1AndroidAppInfo
    appId: str
    chromeAppInfo: GoogleChromeManagementV1ChromeAppInfo
    description: str
    detailUri: str
    displayName: str
    firstPublishTime: str
    homepageUri: str
    iconUri: str
    isPaidApp: bool
    latestPublishTime: str
    name: str
    privacyPolicyUri: str
    publisher: str
    reviewNumber: str
    reviewRating: float
    revisionId: str
    serviceError: GoogleRpcStatus
    type: typing_extensions.Literal[
        "APP_ITEM_TYPE_UNSPECIFIED", "CHROME", "ANDROID", "WEB"
    ]

@typing.type_check_only
class GoogleChromeManagementV1AppReport(typing_extensions.TypedDict, total=False):
    reportTime: str
    usageData: _list[GoogleChromeManagementV1AppUsageData]

@typing.type_check_only
class GoogleChromeManagementV1AppUsageData(typing_extensions.TypedDict, total=False):
    appId: str
    appInstanceId: str
    appType: typing_extensions.Literal[
        "TELEMETRY_APPLICATION_TYPE_UNSPECIFIED",
        "APPLICATION_TYPE_ARC",
        "APPLICATION_TYPE_BUILT_IN",
        "APPLICATION_TYPE_CROSTINI",
        "APPLICATION_TYPE_CHROME_APP",
        "APPLICATION_TYPE_WEB",
        "APPLICATION_TYPE_MAC_OS",
        "APPLICATION_TYPE_PLUGIN_VM",
        "APPLICATION_TYPE_STANDALONE_BROWSER",
        "APPLICATION_TYPE_REMOTE",
        "APPLICATION_TYPE_BOREALIS",
        "APPLICATION_TYPE_SYSTEM_WEB",
        "APPLICATION_TYPE_STANDALONE_BROWSER_CHROME_APP",
        "APPLICATION_TYPE_EXTENSION",
        "APPLICATION_TYPE_STANDALONE_BROWSER_EXTENSION",
        "APPLICATION_TYPE_BRUSCHETTA",
    ]
    runningDuration: str

@typing.type_check_only
class GoogleChromeManagementV1AudioStatusReport(
    typing_extensions.TypedDict, total=False
):
    inputDevice: str
    inputGain: int
    inputMute: bool
    outputDevice: str
    outputMute: bool
    outputVolume: int
    reportTime: str

@typing.type_check_only
class GoogleChromeManagementV1BatteryInfo(typing_extensions.TypedDict, total=False):
    designCapacity: str
    designMinVoltage: int
    manufactureDate: GoogleTypeDate
    manufacturer: str
    serialNumber: str
    technology: str

@typing.type_check_only
class GoogleChromeManagementV1BatterySampleReport(
    typing_extensions.TypedDict, total=False
):
    chargeRate: int
    current: str
    dischargeRate: int
    remainingCapacity: str
    reportTime: str
    status: str
    temperature: int
    voltage: str

@typing.type_check_only
class GoogleChromeManagementV1BatteryStatusReport(
    typing_extensions.TypedDict, total=False
):
    batteryHealth: typing_extensions.Literal[
        "BATTERY_HEALTH_UNSPECIFIED",
        "BATTERY_HEALTH_NORMAL",
        "BATTERY_REPLACE_SOON",
        "BATTERY_REPLACE_NOW",
    ]
    cycleCount: int
    fullChargeCapacity: str
    reportTime: str
    sample: _list[GoogleChromeManagementV1BatterySampleReport]
    serialNumber: str

@typing.type_check_only
class GoogleChromeManagementV1BootPerformanceReport(
    typing_extensions.TypedDict, total=False
):
    bootUpDuration: str
    bootUpTime: str
    reportTime: str
    shutdownDuration: str
    shutdownReason: typing_extensions.Literal[
        "SHUTDOWN_REASON_UNSPECIFIED",
        "USER_REQUEST",
        "SYSTEM_UPDATE",
        "LOW_BATTERY",
        "OTHER",
    ]
    shutdownTime: str

@typing.type_check_only
class GoogleChromeManagementV1BrowserVersion(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "RELEASE_CHANNEL_UNSPECIFIED", "CANARY", "DEV", "BETA", "STABLE", "LTS"
    ]
    count: str
    deviceOsVersion: str
    system: typing_extensions.Literal[
        "DEVICE_SYSTEM_UNSPECIFIED",
        "SYSTEM_OTHER",
        "SYSTEM_ANDROID",
        "SYSTEM_IOS",
        "SYSTEM_CROS",
        "SYSTEM_WINDOWS",
        "SYSTEM_MAC",
        "SYSTEM_LINUX",
    ]
    version: str

@typing.type_check_only
class GoogleChromeManagementV1ChromeAppInfo(typing_extensions.TypedDict, total=False):
    googleOwned: bool
    isCwsHosted: bool
    isExtensionPolicySupported: bool
    isKioskOnly: bool
    isTheme: bool
    kioskEnabled: bool
    minUserCount: int
    permissions: _list[GoogleChromeManagementV1ChromeAppPermission]
    siteAccess: _list[GoogleChromeManagementV1ChromeAppSiteAccess]
    supportEnabled: bool
    type: typing_extensions.Literal["ITEM_TYPE_UNSPECIFIED", "EXTENSION", "OTHERS"]

@typing.type_check_only
class GoogleChromeManagementV1ChromeAppPermission(
    typing_extensions.TypedDict, total=False
):
    accessUserData: bool
    documentationUri: str
    type: str

@typing.type_check_only
class GoogleChromeManagementV1ChromeAppRequest(
    typing_extensions.TypedDict, total=False
):
    appDetails: str
    appId: str
    detailUri: str
    displayName: str
    iconUri: str
    latestRequestTime: str
    requestCount: str

@typing.type_check_only
class GoogleChromeManagementV1ChromeAppSiteAccess(
    typing_extensions.TypedDict, total=False
):
    hostMatch: str

@typing.type_check_only
class GoogleChromeManagementV1CountChromeAppRequestsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    requestedApps: _list[GoogleChromeManagementV1ChromeAppRequest]
    totalSize: int

@typing.type_check_only
class GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponse(
    typing_extensions.TypedDict, total=False
):
    noRecentActivityCount: str
    pendingBrowserUpdateCount: str
    recentlyEnrolledCount: str

@typing.type_check_only
class GoogleChromeManagementV1CountChromeCrashEventsResponse(
    typing_extensions.TypedDict, total=False
):
    crashEventCounts: _list[
        GoogleChromeManagementV1CountChromeCrashEventsResponseCrashEventCount
    ]

@typing.type_check_only
class GoogleChromeManagementV1CountChromeCrashEventsResponseCrashEventCount(
    typing_extensions.TypedDict, total=False
):
    browserVersion: str
    count: str
    date: GoogleTypeDate

@typing.type_check_only
class GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponse(
    typing_extensions.TypedDict, total=False
):
    deviceAueCountReports: _list[GoogleChromeManagementV1DeviceAueCountReport]

@typing.type_check_only
class GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponse(
    typing_extensions.TypedDict, total=False
):
    noRecentPolicySyncCount: str
    noRecentUserActivityCount: str
    osVersionNotCompliantCount: str
    pendingUpdate: str
    unsupportedPolicyCount: str

@typing.type_check_only
class GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    cpuReports: _list[GoogleChromeManagementV1DeviceHardwareCountReport]
    memoryReports: _list[GoogleChromeManagementV1DeviceHardwareCountReport]
    modelReports: _list[GoogleChromeManagementV1DeviceHardwareCountReport]
    storageReports: _list[GoogleChromeManagementV1DeviceHardwareCountReport]

@typing.type_check_only
class GoogleChromeManagementV1CountChromeVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    browserVersions: _list[GoogleChromeManagementV1BrowserVersion]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleChromeManagementV1CountInstalledAppsResponse(
    typing_extensions.TypedDict, total=False
):
    installedApps: _list[GoogleChromeManagementV1InstalledApp]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleChromeManagementV1CountPrintJobsByPrinterResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    printerReports: _list[GoogleChromeManagementV1PrinterReport]
    totalSize: str

@typing.type_check_only
class GoogleChromeManagementV1CountPrintJobsByUserResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    totalSize: str
    userPrintReports: _list[GoogleChromeManagementV1UserPrintReport]

@typing.type_check_only
class GoogleChromeManagementV1CpuInfo(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X64"]
    keylockerConfigured: bool
    keylockerSupported: bool
    maxClockSpeed: int
    model: str

@typing.type_check_only
class GoogleChromeManagementV1CpuStatusReport(typing_extensions.TypedDict, total=False):
    cpuTemperatureInfo: _list[GoogleChromeManagementV1CpuTemperatureInfo]
    cpuUtilizationPct: int
    reportTime: str
    sampleFrequency: str

@typing.type_check_only
class GoogleChromeManagementV1CpuTemperatureInfo(
    typing_extensions.TypedDict, total=False
):
    label: str
    temperatureCelsius: int

@typing.type_check_only
class GoogleChromeManagementV1Device(typing_extensions.TypedDict, total=False):
    deviceId: str
    machine: str

@typing.type_check_only
class GoogleChromeManagementV1DeviceActivityReport(
    typing_extensions.TypedDict, total=False
):
    deviceActivityState: typing_extensions.Literal[
        "DEVICE_ACTIVITY_STATE_UNSPECIFIED", "ACTIVE", "IDLE", "LOCKED"
    ]
    reportTime: str

@typing.type_check_only
class GoogleChromeManagementV1DeviceAueCountReport(
    typing_extensions.TypedDict, total=False
):
    aueMonth: typing_extensions.Literal[
        "MONTH_UNSPECIFIED",
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]
    aueYear: str
    count: str
    expired: bool
    model: str

@typing.type_check_only
class GoogleChromeManagementV1DeviceHardwareCountReport(
    typing_extensions.TypedDict, total=False
):
    bucket: str
    count: str

@typing.type_check_only
class GoogleChromeManagementV1DeviceRequestingExtensionDetails(
    typing_extensions.TypedDict, total=False
):
    deviceName: str
    justification: str

@typing.type_check_only
class GoogleChromeManagementV1DiskInfo(typing_extensions.TypedDict, total=False):
    bytesReadThisSession: str
    bytesWrittenThisSession: str
    discardTimeThisSession: str
    health: str
    ioTimeThisSession: str
    manufacturer: str
    model: str
    readTimeThisSession: str
    serialNumber: str
    sizeBytes: str
    type: str
    volumeIds: _list[str]
    writeTimeThisSession: str

@typing.type_check_only
class GoogleChromeManagementV1DisplayDevice(typing_extensions.TypedDict, total=False):
    displayHeightMm: int
    displayName: str
    displayWidthMm: int
    internal: bool
    manufactureYear: int
    manufacturerId: str
    modelId: int

@typing.type_check_only
class GoogleChromeManagementV1DisplayInfo(typing_extensions.TypedDict, total=False):
    deviceId: str
    displayName: str
    isInternal: bool
    refreshRate: int
    resolutionHeight: int
    resolutionWidth: int

@typing.type_check_only
class GoogleChromeManagementV1EnumeratePrintJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    printJobs: _list[GoogleChromeManagementV1PrintJob]
    totalSize: str

@typing.type_check_only
class GoogleChromeManagementV1FetchDevicesRequestingExtensionResponse(
    typing_extensions.TypedDict, total=False
):
    deviceDetails: _list[GoogleChromeManagementV1DeviceRequestingExtensionDetails]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleChromeManagementV1FetchUsersRequestingExtensionResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    totalSize: int
    userDetails: _list[GoogleChromeManagementV1UserRequestingExtensionDetails]

@typing.type_check_only
class GoogleChromeManagementV1FindInstalledAppDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: _list[GoogleChromeManagementV1Device]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleChromeManagementV1GraphicsAdapterInfo(
    typing_extensions.TypedDict, total=False
):
    adapter: str
    deviceId: str
    driverVersion: str

@typing.type_check_only
class GoogleChromeManagementV1GraphicsInfo(typing_extensions.TypedDict, total=False):
    adapterInfo: GoogleChromeManagementV1GraphicsAdapterInfo
    displayDevices: _list[GoogleChromeManagementV1DisplayDevice]
    eprivacySupported: bool
    touchScreenInfo: GoogleChromeManagementV1TouchScreenInfo

@typing.type_check_only
class GoogleChromeManagementV1GraphicsStatusReport(
    typing_extensions.TypedDict, total=False
):
    displays: _list[GoogleChromeManagementV1DisplayInfo]
    reportTime: str

@typing.type_check_only
class GoogleChromeManagementV1HeartbeatStatusReport(
    typing_extensions.TypedDict, total=False
):
    reportTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNKNOWN", "ONLINE", "OFFLINE"
    ]

@typing.type_check_only
class GoogleChromeManagementV1HttpsLatencyRoutineData(
    typing_extensions.TypedDict, total=False
):
    latency: str
    problem: typing_extensions.Literal[
        "HTTPS_LATENCY_PROBLEM_UNSPECIFIED",
        "FAILED_DNS_RESOLUTIONS",
        "FAILED_HTTPS_REQUESTS",
        "HIGH_LATENCY",
        "VERY_HIGH_LATENCY",
    ]

@typing.type_check_only
class GoogleChromeManagementV1InstalledApp(typing_extensions.TypedDict, total=False):
    appId: str
    appInstallType: typing_extensions.Literal[
        "APP_INSTALL_TYPE_UNSPECIFIED",
        "MULTIPLE",
        "NORMAL",
        "ADMIN",
        "DEVELOPMENT",
        "SIDELOAD",
        "OTHER",
    ]
    appSource: typing_extensions.Literal[
        "APP_SOURCE_UNSPECIFIED", "CHROME_WEBSTORE", "PLAY_STORE"
    ]
    appType: typing_extensions.Literal[
        "APP_TYPE_UNSPECIFIED", "EXTENSION", "APP", "THEME", "HOSTED_APP", "ANDROID_APP"
    ]
    browserDeviceCount: str
    description: str
    disabled: bool
    displayName: str
    homepageUri: str
    osUserCount: str
    permissions: _list[str]
    riskAssessment: GoogleChromeManagementV1RiskAssessmentData

@typing.type_check_only
class GoogleChromeManagementV1KioskAppStatusReport(
    typing_extensions.TypedDict, total=False
):
    appId: str
    appVersion: str
    reportTime: str

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: _list[GoogleChromeManagementV1TelemetryDevice]
    nextPageToken: str

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryEventsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    telemetryEvents: _list[GoogleChromeManagementV1TelemetryEvent]

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryNotificationConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    telemetryNotificationConfigs: _list[
        GoogleChromeManagementV1TelemetryNotificationConfig
    ]

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryUsersResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    telemetryUsers: _list[GoogleChromeManagementV1TelemetryUser]

@typing.type_check_only
class GoogleChromeManagementV1MemoryInfo(typing_extensions.TypedDict, total=False):
    availableRamBytes: str
    totalMemoryEncryption: GoogleChromeManagementV1TotalMemoryEncryptionInfo
    totalRamBytes: str

@typing.type_check_only
class GoogleChromeManagementV1MemoryStatusReport(
    typing_extensions.TypedDict, total=False
):
    pageFaults: int
    reportTime: str
    sampleFrequency: str
    systemRamFreeBytes: str

@typing.type_check_only
class GoogleChromeManagementV1NetworkBandwidthReport(
    typing_extensions.TypedDict, total=False
):
    downloadSpeedKbps: str
    reportTime: str

@typing.type_check_only
class GoogleChromeManagementV1NetworkDevice(typing_extensions.TypedDict, total=False):
    iccid: str
    imei: str
    macAddress: str
    mdn: str
    meid: str
    type: typing_extensions.Literal[
        "NETWORK_DEVICE_TYPE_UNSPECIFIED",
        "CELLULAR_DEVICE",
        "ETHERNET_DEVICE",
        "WIFI_DEVICE",
    ]

@typing.type_check_only
class GoogleChromeManagementV1NetworkDiagnosticsReport(
    typing_extensions.TypedDict, total=False
):
    httpsLatencyData: GoogleChromeManagementV1HttpsLatencyRoutineData
    reportTime: str

@typing.type_check_only
class GoogleChromeManagementV1NetworkInfo(typing_extensions.TypedDict, total=False):
    networkDevices: _list[GoogleChromeManagementV1NetworkDevice]

@typing.type_check_only
class GoogleChromeManagementV1NetworkStatusReport(
    typing_extensions.TypedDict, total=False
):
    connectionState: typing_extensions.Literal[
        "NETWORK_CONNECTION_STATE_UNSPECIFIED",
        "ONLINE",
        "CONNECTED",
        "PORTAL",
        "CONNECTING",
        "NOT_CONNECTED",
    ]
    connectionType: typing_extensions.Literal[
        "NETWORK_TYPE_UNSPECIFIED", "CELLULAR", "ETHERNET", "TETHER", "VPN", "WIFI"
    ]
    encryptionOn: bool
    gatewayIpAddress: str
    guid: str
    lanIpAddress: str
    receivingBitRateMbps: str
    reportTime: str
    sampleFrequency: str
    signalStrengthDbm: int
    transmissionBitRateMbps: str
    transmissionPowerDbm: int
    wifiLinkQuality: str
    wifiPowerManagementEnabled: bool

@typing.type_check_only
class GoogleChromeManagementV1OsUpdateStatus(typing_extensions.TypedDict, total=False):
    lastRebootTime: str
    lastUpdateCheckTime: str
    lastUpdateTime: str
    newPlatformVersion: str
    newRequestedPlatformVersion: str
    updateState: typing_extensions.Literal[
        "UPDATE_STATE_UNSPECIFIED",
        "OS_IMAGE_DOWNLOAD_NOT_STARTED",
        "OS_IMAGE_DOWNLOAD_IN_PROGRESS",
        "OS_UPDATE_NEED_REBOOT",
    ]

@typing.type_check_only
class GoogleChromeManagementV1PeripheralsReport(
    typing_extensions.TypedDict, total=False
):
    reportTime: str
    usbPeripheralReport: _list[GoogleChromeManagementV1UsbPeripheralReport]

@typing.type_check_only
class GoogleChromeManagementV1PrintJob(typing_extensions.TypedDict, total=False):
    colorMode: typing_extensions.Literal[
        "COLOR_MODE_UNSPECIFIED", "BLACK_AND_WHITE", "COLOR"
    ]
    completeTime: str
    copyCount: int
    createTime: str
    documentPageCount: int
    duplexMode: typing_extensions.Literal[
        "DUPLEX_MODE_UNSPECIFIED",
        "ONE_SIDED",
        "TWO_SIDED_LONG_EDGE",
        "TWO_SIDED_SHORT_EDGE",
    ]
    id: str
    printer: str
    printerId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PRINTED", "CANCELLED", "FAILED"
    ]
    title: str
    userEmail: str
    userId: str

@typing.type_check_only
class GoogleChromeManagementV1PrinterReport(typing_extensions.TypedDict, total=False):
    deviceCount: str
    jobCount: str
    printer: str
    printerId: str
    printerModel: str
    userCount: str

@typing.type_check_only
class GoogleChromeManagementV1RiskAssessment(typing_extensions.TypedDict, total=False):
    assessment: str
    detailsUrl: str
    version: str

@typing.type_check_only
class GoogleChromeManagementV1RiskAssessmentData(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleChromeManagementV1RiskAssessmentEntry]
    overallRiskLevel: typing_extensions.Literal[
        "RISK_LEVEL_UNSPECIFIED",
        "RISK_LEVEL_LOW",
        "RISK_LEVEL_MEDIUM",
        "RISK_LEVEL_HIGH",
    ]

@typing.type_check_only
class GoogleChromeManagementV1RiskAssessmentEntry(
    typing_extensions.TypedDict, total=False
):
    provider: typing_extensions.Literal[
        "RISK_ASSESSMENT_PROVIDER_UNSPECIFIED",
        "RISK_ASSESSMENT_PROVIDER_CRXCAVATOR",
        "RISK_ASSESSMENT_PROVIDER_SPIN_AI",
    ]
    riskAssessment: GoogleChromeManagementV1RiskAssessment
    riskLevel: typing_extensions.Literal[
        "RISK_LEVEL_UNSPECIFIED",
        "RISK_LEVEL_LOW",
        "RISK_LEVEL_MEDIUM",
        "RISK_LEVEL_HIGH",
    ]

@typing.type_check_only
class GoogleChromeManagementV1RuntimeCountersReport(
    typing_extensions.TypedDict, total=False
):
    enterHibernationCount: str
    enterPoweroffCount: str
    enterSleepCount: str
    reportTime: str
    uptimeRuntimeDuration: str

@typing.type_check_only
class GoogleChromeManagementV1StorageInfo(typing_extensions.TypedDict, total=False):
    availableDiskBytes: str
    totalDiskBytes: str
    volume: _list[GoogleChromeManagementV1StorageInfoDiskVolume]

@typing.type_check_only
class GoogleChromeManagementV1StorageInfoDiskVolume(
    typing_extensions.TypedDict, total=False
):
    storageFreeBytes: str
    storageTotalBytes: str
    volumeId: str

@typing.type_check_only
class GoogleChromeManagementV1StorageStatusReport(
    typing_extensions.TypedDict, total=False
):
    disk: _list[GoogleChromeManagementV1DiskInfo]
    reportTime: str

@typing.type_check_only
class GoogleChromeManagementV1TelemetryAppInstallEvent(
    typing_extensions.TypedDict, total=False
):
    appId: str
    appInstallReason: typing_extensions.Literal[
        "APPLICATION_INSTALL_REASON_UNSPECIFIED",
        "APPLICATION_INSTALL_REASON_SYSTEM",
        "APPLICATION_INSTALL_REASON_POLICY",
        "APPLICATION_INSTALL_REASON_OEM",
        "APPLICATION_INSTALL_REASON_DEFAULT",
        "APPLICATION_INSTALL_REASON_SYNC",
        "APPLICATION_INSTALL_REASON_USER",
        "APPLICATION_INSTALL_REASON_SUB_APP",
        "APPLICATION_INSTALL_REASON_KIOSK",
        "APPLICATION_INSTALL_REASON_COMMAND_LINE",
    ]
    appInstallSource: typing_extensions.Literal[
        "APPLICATION_INSTALL_SOURCE_UNSPECIFIED",
        "APPLICATION_INSTALL_SOURCE_SYSTEM",
        "APPLICATION_INSTALL_SOURCE_SYNC",
        "APPLICATION_INSTALL_SOURCE_PLAY_STORE",
        "APPLICATION_INSTALL_SOURCE_CHROME_WEB_STORE",
        "APPLICATION_INSTALL_SOURCE_BROWSER",
    ]
    appInstallTime: typing_extensions.Literal[
        "APPLICATION_INSTALL_TIME_UNSPECIFIED",
        "APPLICATION_INSTALL_TIME_INIT",
        "APPLICATION_INSTALL_TIME_RUNNING",
    ]
    appType: typing_extensions.Literal[
        "TELEMETRY_APPLICATION_TYPE_UNSPECIFIED",
        "APPLICATION_TYPE_ARC",
        "APPLICATION_TYPE_BUILT_IN",
        "APPLICATION_TYPE_CROSTINI",
        "APPLICATION_TYPE_CHROME_APP",
        "APPLICATION_TYPE_WEB",
        "APPLICATION_TYPE_MAC_OS",
        "APPLICATION_TYPE_PLUGIN_VM",
        "APPLICATION_TYPE_STANDALONE_BROWSER",
        "APPLICATION_TYPE_REMOTE",
        "APPLICATION_TYPE_BOREALIS",
        "APPLICATION_TYPE_SYSTEM_WEB",
        "APPLICATION_TYPE_STANDALONE_BROWSER_CHROME_APP",
        "APPLICATION_TYPE_EXTENSION",
        "APPLICATION_TYPE_STANDALONE_BROWSER_EXTENSION",
        "APPLICATION_TYPE_BRUSCHETTA",
    ]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryAppLaunchEvent(
    typing_extensions.TypedDict, total=False
):
    appId: str
    appLaunchSource: typing_extensions.Literal[
        "APPLICATION_LAUNCH_SOURCE_UNSPECIFIED",
        "APPLICATION_LAUNCH_SOURCE_APP_LIST_GRID",
        "APPLICATION_LAUNCH_SOURCE_APP_LIST_GRID_CONTEXT_MENU",
        "APPLICATION_LAUNCH_SOURCE_APP_LIST_QUERY",
        "APPLICATION_LAUNCH_SOURCE_APP_LIST_QUERY_CONTEXT_MENU",
        "APPLICATION_LAUNCH_SOURCE_APP_LIST_RECOMMENDATION",
        "APPLICATION_LAUNCH_SOURCE_PARENTAL_CONTROLS",
        "APPLICATION_LAUNCH_SOURCE_SHELF",
        "APPLICATION_LAUNCH_SOURCE_FILE_MANAGER",
        "APPLICATION_LAUNCH_SOURCE_LINK",
        "APPLICATION_LAUNCH_SOURCE_OMNIBOX",
        "APPLICATION_LAUNCH_SOURCE_CHROME_INTERNAL",
        "APPLICATION_LAUNCH_SOURCE_KEYBOARD",
        "APPLICATION_LAUNCH_SOURCE_OTHER_APP",
        "APPLICATION_LAUNCH_SOURCE_MENU",
        "APPLICATION_LAUNCH_SOURCE_INSTALLED_NOTIFICATION",
        "APPLICATION_LAUNCH_SOURCE_TEST",
        "APPLICATION_LAUNCH_SOURCE_ARC",
        "APPLICATION_LAUNCH_SOURCE_SHARESHEET",
        "APPLICATION_LAUNCH_SOURCE_RELEASE_NOTES_NOTIFICATION",
        "APPLICATION_LAUNCH_SOURCE_FULL_RESTORE",
        "APPLICATION_LAUNCH_SOURCE_SMART_TEXT_CONTEXT_MENU",
        "APPLICATION_LAUNCH_SOURCE_DISCOVER_TAB_NOTIFICATION",
        "APPLICATION_LAUNCH_SOURCE_MANAGEMENT_API",
        "APPLICATION_LAUNCH_SOURCE_KIOSK",
        "APPLICATION_LAUNCH_SOURCE_COMMAND_LINE",
        "APPLICATION_LAUNCH_SOURCE_BACKGROUND_MODE",
        "APPLICATION_LAUNCH_SOURCE_NEW_TAB_PAGE",
        "APPLICATION_LAUNCH_SOURCE_INTENT_URL",
        "APPLICATION_LAUNCH_SOURCE_OS_LOGIN",
        "APPLICATION_LAUNCH_SOURCE_PROTOCOL_HANDLER",
        "APPLICATION_LAUNCH_SOURCE_URL_HANDLER",
        "APPLICATION_LAUNCH_SOURCE_LOCK_SCREEN",
        "APPLICATION_LAUNCH_SOURCE_APP_HOME_PAGE",
        "APPLICATION_LAUNCH_SOURCE_REPARENTING",
        "APPLICATION_LAUNCH_SOURCE_PROFILE_MENU",
        "APPLICATION_LAUNCH_SOURCE_SYSTEM_TRAY_CALENDAR",
        "APPLICATION_LAUNCH_SOURCE_INSTALLER",
        "APPLICATION_LAUNCH_SOURCE_FIRST_RUN",
        "APPLICATION_LAUNCH_SOURCE_WELCOME_TOUR",
        "APPLICATION_LAUNCH_SOURCE_FOCUS_MODE",
        "APPLICATION_LAUNCH_SOURCE_SPARKY",
        "APPLICATION_LAUNCH_SOURCE_NAVIGATION_CAPTURING",
        "APPLICATION_LAUNCH_SOURCE_WEB_INSTALL_API",
    ]
    appType: typing_extensions.Literal[
        "TELEMETRY_APPLICATION_TYPE_UNSPECIFIED",
        "APPLICATION_TYPE_ARC",
        "APPLICATION_TYPE_BUILT_IN",
        "APPLICATION_TYPE_CROSTINI",
        "APPLICATION_TYPE_CHROME_APP",
        "APPLICATION_TYPE_WEB",
        "APPLICATION_TYPE_MAC_OS",
        "APPLICATION_TYPE_PLUGIN_VM",
        "APPLICATION_TYPE_STANDALONE_BROWSER",
        "APPLICATION_TYPE_REMOTE",
        "APPLICATION_TYPE_BOREALIS",
        "APPLICATION_TYPE_SYSTEM_WEB",
        "APPLICATION_TYPE_STANDALONE_BROWSER_CHROME_APP",
        "APPLICATION_TYPE_EXTENSION",
        "APPLICATION_TYPE_STANDALONE_BROWSER_EXTENSION",
        "APPLICATION_TYPE_BRUSCHETTA",
    ]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryAppUninstallEvent(
    typing_extensions.TypedDict, total=False
):
    appId: str
    appType: typing_extensions.Literal[
        "TELEMETRY_APPLICATION_TYPE_UNSPECIFIED",
        "APPLICATION_TYPE_ARC",
        "APPLICATION_TYPE_BUILT_IN",
        "APPLICATION_TYPE_CROSTINI",
        "APPLICATION_TYPE_CHROME_APP",
        "APPLICATION_TYPE_WEB",
        "APPLICATION_TYPE_MAC_OS",
        "APPLICATION_TYPE_PLUGIN_VM",
        "APPLICATION_TYPE_STANDALONE_BROWSER",
        "APPLICATION_TYPE_REMOTE",
        "APPLICATION_TYPE_BOREALIS",
        "APPLICATION_TYPE_SYSTEM_WEB",
        "APPLICATION_TYPE_STANDALONE_BROWSER_CHROME_APP",
        "APPLICATION_TYPE_EXTENSION",
        "APPLICATION_TYPE_STANDALONE_BROWSER_EXTENSION",
        "APPLICATION_TYPE_BRUSCHETTA",
    ]
    appUninstallSource: typing_extensions.Literal[
        "APPLICATION_UNINSTALL_SOURCE_UNSPECIFIED",
        "APPLICATION_UNINSTALL_SOURCE_APP_LIST",
        "APPLICATION_UNINSTALL_SOURCE_APP_MANAGEMENT",
        "APPLICATION_UNINSTALL_SOURCE_SHELF",
        "APPLICATION_UNINSTALL_SOURCE_MIGRATION",
    ]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryAudioSevereUnderrunEvent(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleChromeManagementV1TelemetryDevice(typing_extensions.TypedDict, total=False):
    appReport: _list[GoogleChromeManagementV1AppReport]
    audioStatusReport: _list[GoogleChromeManagementV1AudioStatusReport]
    batteryInfo: _list[GoogleChromeManagementV1BatteryInfo]
    batteryStatusReport: _list[GoogleChromeManagementV1BatteryStatusReport]
    bootPerformanceReport: _list[GoogleChromeManagementV1BootPerformanceReport]
    cpuInfo: _list[GoogleChromeManagementV1CpuInfo]
    cpuStatusReport: _list[GoogleChromeManagementV1CpuStatusReport]
    customer: str
    deviceId: str
    graphicsInfo: GoogleChromeManagementV1GraphicsInfo
    graphicsStatusReport: _list[GoogleChromeManagementV1GraphicsStatusReport]
    heartbeatStatusReport: _list[GoogleChromeManagementV1HeartbeatStatusReport]
    kioskAppStatusReport: _list[GoogleChromeManagementV1KioskAppStatusReport]
    memoryInfo: GoogleChromeManagementV1MemoryInfo
    memoryStatusReport: _list[GoogleChromeManagementV1MemoryStatusReport]
    name: str
    networkBandwidthReport: _list[GoogleChromeManagementV1NetworkBandwidthReport]
    networkDiagnosticsReport: _list[GoogleChromeManagementV1NetworkDiagnosticsReport]
    networkInfo: GoogleChromeManagementV1NetworkInfo
    networkStatusReport: _list[GoogleChromeManagementV1NetworkStatusReport]
    orgUnitId: str
    osUpdateStatus: _list[GoogleChromeManagementV1OsUpdateStatus]
    peripheralsReport: _list[GoogleChromeManagementV1PeripheralsReport]
    runtimeCountersReport: _list[GoogleChromeManagementV1RuntimeCountersReport]
    serialNumber: str
    storageInfo: GoogleChromeManagementV1StorageInfo
    storageStatusReport: _list[GoogleChromeManagementV1StorageStatusReport]
    thunderboltInfo: _list[GoogleChromeManagementV1ThunderboltInfo]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryDeviceInfo(
    typing_extensions.TypedDict, total=False
):
    deviceId: str
    orgUnitId: str

@typing.type_check_only
class GoogleChromeManagementV1TelemetryEvent(typing_extensions.TypedDict, total=False):
    appInstallEvent: GoogleChromeManagementV1TelemetryAppInstallEvent
    appLaunchEvent: GoogleChromeManagementV1TelemetryAppLaunchEvent
    appUninstallEvent: GoogleChromeManagementV1TelemetryAppUninstallEvent
    audioSevereUnderrunEvent: GoogleChromeManagementV1TelemetryAudioSevereUnderrunEvent
    device: GoogleChromeManagementV1TelemetryDeviceInfo
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "AUDIO_SEVERE_UNDERRUN",
        "NETWORK_STATE_CHANGE",
        "USB_ADDED",
        "USB_REMOVED",
        "NETWORK_HTTPS_LATENCY_CHANGE",
        "WIFI_SIGNAL_STRENGTH_LOW",
        "WIFI_SIGNAL_STRENGTH_RECOVERED",
        "VPN_CONNECTION_STATE_CHANGE",
        "APP_INSTALLED",
        "APP_UNINSTALLED",
        "APP_LAUNCHED",
        "OS_CRASH",
    ]
    httpsLatencyChangeEvent: GoogleChromeManagementV1TelemetryHttpsLatencyChangeEvent
    name: str
    networkStateChangeEvent: (
        GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent
    )
    reportTime: str
    usbPeripheralsEvent: GoogleChromeManagementV1TelemetryUsbPeripheralsEvent
    user: GoogleChromeManagementV1TelemetryUserInfo
    vpnConnectionStateChangeEvent: (
        GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent
    )
    wifiSignalStrengthEvent: GoogleChromeManagementV1TelemetryNetworkSignalStrengthEvent

@typing.type_check_only
class GoogleChromeManagementV1TelemetryEventNotificationFilter(
    typing_extensions.TypedDict, total=False
):
    eventTypes: _list[
        typing_extensions.Literal[
            "EVENT_TYPE_UNSPECIFIED",
            "AUDIO_SEVERE_UNDERRUN",
            "NETWORK_STATE_CHANGE",
            "USB_ADDED",
            "USB_REMOVED",
            "NETWORK_HTTPS_LATENCY_CHANGE",
            "WIFI_SIGNAL_STRENGTH_LOW",
            "WIFI_SIGNAL_STRENGTH_RECOVERED",
            "VPN_CONNECTION_STATE_CHANGE",
            "APP_INSTALLED",
            "APP_UNINSTALLED",
            "APP_LAUNCHED",
            "OS_CRASH",
        ]
    ]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryHttpsLatencyChangeEvent(
    typing_extensions.TypedDict, total=False
):
    httpsLatencyRoutineData: GoogleChromeManagementV1HttpsLatencyRoutineData
    httpsLatencyState: typing_extensions.Literal[
        "HTTPS_LATENCY_STATE_UNSPECIFIED", "RECOVERY", "PROBLEM"
    ]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent(
    typing_extensions.TypedDict, total=False
):
    connectionState: typing_extensions.Literal[
        "NETWORK_CONNECTION_STATE_UNSPECIFIED",
        "ONLINE",
        "CONNECTED",
        "PORTAL",
        "CONNECTING",
        "NOT_CONNECTED",
    ]
    guid: str

@typing.type_check_only
class GoogleChromeManagementV1TelemetryNetworkSignalStrengthEvent(
    typing_extensions.TypedDict, total=False
):
    guid: str
    signalStrengthDbm: int

@typing.type_check_only
class GoogleChromeManagementV1TelemetryNotificationConfig(
    typing_extensions.TypedDict, total=False
):
    customer: str
    filter: GoogleChromeManagementV1TelemetryNotificationFilter
    googleCloudPubsubTopic: str
    name: str

@typing.type_check_only
class GoogleChromeManagementV1TelemetryNotificationFilter(
    typing_extensions.TypedDict, total=False
):
    deviceId: str
    deviceOrgUnitId: str
    telemetryEventNotificationFilter: (
        GoogleChromeManagementV1TelemetryEventNotificationFilter
    )
    userEmail: str
    userOrgUnitId: str

@typing.type_check_only
class GoogleChromeManagementV1TelemetryUsbPeripheralsEvent(
    typing_extensions.TypedDict, total=False
):
    usbPeripheralReport: _list[GoogleChromeManagementV1UsbPeripheralReport]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryUser(typing_extensions.TypedDict, total=False):
    customer: str
    name: str
    orgUnitId: str
    userDevice: _list[GoogleChromeManagementV1TelemetryUserDevice]
    userEmail: str
    userId: str

@typing.type_check_only
class GoogleChromeManagementV1TelemetryUserDevice(
    typing_extensions.TypedDict, total=False
):
    appReport: _list[GoogleChromeManagementV1AppReport]
    audioStatusReport: _list[GoogleChromeManagementV1AudioStatusReport]
    deviceActivityReport: _list[GoogleChromeManagementV1DeviceActivityReport]
    deviceId: str
    networkBandwidthReport: _list[GoogleChromeManagementV1NetworkBandwidthReport]
    peripheralsReport: _list[GoogleChromeManagementV1PeripheralsReport]

@typing.type_check_only
class GoogleChromeManagementV1TelemetryUserInfo(
    typing_extensions.TypedDict, total=False
):
    email: str
    orgUnitId: str

@typing.type_check_only
class GoogleChromeManagementV1ThunderboltInfo(typing_extensions.TypedDict, total=False):
    securityLevel: typing_extensions.Literal[
        "THUNDERBOLT_SECURITY_LEVEL_UNSPECIFIED",
        "THUNDERBOLT_SECURITY_NONE_LEVEL",
        "THUNDERBOLT_SECURITY_USER_LEVEL",
        "THUNDERBOLT_SECURITY_SECURE_LEVEL",
        "THUNDERBOLT_SECURITY_DP_ONLY_LEVEL",
        "THUNDERBOLT_SECURITY_USB_ONLY_LEVEL",
        "THUNDERBOLT_SECURITY_NO_PCIE_LEVEL",
    ]

@typing.type_check_only
class GoogleChromeManagementV1TotalMemoryEncryptionInfo(
    typing_extensions.TypedDict, total=False
):
    encryptionAlgorithm: typing_extensions.Literal[
        "MEMORY_ENCRYPTION_ALGORITHM_UNSPECIFIED",
        "MEMORY_ENCRYPTION_ALGORITHM_UNKNOWN",
        "MEMORY_ENCRYPTION_ALGORITHM_AES_XTS_128",
        "MEMORY_ENCRYPTION_ALGORITHM_AES_XTS_256",
    ]
    encryptionState: typing_extensions.Literal[
        "MEMORY_ENCRYPTION_STATE_UNSPECIFIED",
        "MEMORY_ENCRYPTION_STATE_UNKNOWN",
        "MEMORY_ENCRYPTION_STATE_DISABLED",
        "MEMORY_ENCRYPTION_STATE_TME",
        "MEMORY_ENCRYPTION_STATE_MKTME",
    ]
    keyLength: str
    maxKeys: str

@typing.type_check_only
class GoogleChromeManagementV1TouchScreenDevice(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    stylusCapable: bool
    touchPointCount: int

@typing.type_check_only
class GoogleChromeManagementV1TouchScreenInfo(typing_extensions.TypedDict, total=False):
    devices: _list[GoogleChromeManagementV1TouchScreenDevice]
    touchpadLibrary: str

@typing.type_check_only
class GoogleChromeManagementV1UsbPeripheralReport(
    typing_extensions.TypedDict, total=False
):
    categories: _list[str]
    classId: int
    firmwareVersion: str
    name: str
    pid: int
    subclassId: int
    vendor: str
    vid: int

@typing.type_check_only
class GoogleChromeManagementV1UserPrintReport(typing_extensions.TypedDict, total=False):
    deviceCount: str
    jobCount: str
    printerCount: str
    userEmail: str
    userId: str

@typing.type_check_only
class GoogleChromeManagementV1UserRequestingExtensionDetails(
    typing_extensions.TypedDict, total=False
):
    email: str
    justification: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1AttestationCredential(
    typing_extensions.TypedDict, total=False
):
    keyRotationTime: str
    keyTrustLevel: typing_extensions.Literal[
        "KEY_TRUST_LEVEL_UNSPECIFIED", "CHROME_BROWSER_HW_KEY", "CHROME_BROWSER_OS_KEY"
    ]
    keyType: typing_extensions.Literal["KEY_TYPE_UNSPECIFIED", "RSA_KEY", "EC_KEY"]
    publicKey: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1CertificateProvisioningProcess(
    typing_extensions.TypedDict, total=False
):
    caConnectionAdapterConfigReference: str
    chromeOsDevice: GoogleChromeManagementVersionsV1ChromeOsDevice
    chromeOsUserSession: GoogleChromeManagementVersionsV1ChromeOsUserSession
    failureMessage: str
    issuedCertificate: str
    name: str
    profileAdapterConfigReference: str
    provisioningProfileId: str
    signData: str
    signature: str
    signatureAlgorithm: typing_extensions.Literal[
        "SIGNATURE_ALGORITHM_UNSPECIFIED",
        "SIGNATURE_ALGORITHM_RSA_PKCS1_V1_5_SHA256",
        "SIGNATURE_ALGORITHM_ECDSA_SHA256",
    ]
    startTime: str
    subjectPublicKeyInfo: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1ChromeBrowserProfile(
    typing_extensions.TypedDict, total=False
):
    affiliationState: typing_extensions.Literal[
        "AFFILIATION_STATE_UNSPECIFIED",
        "UNAFFILIATED_GENERIC",
        "PROFILE_ONLY",
        "UNAFFILIATED_LOCAL_MACHINE",
        "UNAFFILIATED_CLOUD_MACHINE",
        "AFFILIATED_CLOUD_MANAGED",
    ]
    annotatedLocation: str
    annotatedUser: str
    attestationCredential: GoogleChromeManagementVersionsV1AttestationCredential
    browserChannel: str
    browserVersion: str
    deviceInfo: GoogleChromeManagementVersionsV1DeviceInfo
    displayName: str
    etag: str
    extensionCount: str
    firstEnrollmentTime: str
    identityProvider: typing_extensions.Literal[
        "IDENTITY_PROVIDER_UNSPECIFIED",
        "GOOGLE_IDENTITY_PROVIDER",
        "EXTERNAL_IDENTITY_PROVIDER",
    ]
    lastActivityTime: str
    lastPolicyFetchTime: str
    lastPolicySyncTime: str
    lastStatusReportTime: str
    name: str
    osPlatformType: str
    osPlatformVersion: str
    osVersion: str
    policyCount: str
    profileId: str
    profilePermanentId: str
    reportingData: GoogleChromeManagementVersionsV1ReportingData
    userEmail: str
    userId: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1ChromeOsDevice(
    typing_extensions.TypedDict, total=False
):
    deviceDirectoryApiId: str
    serialNumber: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1ChromeOsUserSession(
    typing_extensions.TypedDict, total=False
):
    chromeOsDevice: GoogleChromeManagementVersionsV1ChromeOsDevice
    userDirectoryApiId: str
    userPrimaryEmail: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1DeviceInfo(
    typing_extensions.TypedDict, total=False
):
    affiliatedDeviceId: str
    deviceType: typing_extensions.Literal["DEVICE_TYPE_UNSPECIFIED", "CHROME_BROWSER"]
    hostname: str
    machine: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1ListChromeBrowserProfilesResponse(
    typing_extensions.TypedDict, total=False
):
    chromeBrowserProfiles: _list[GoogleChromeManagementVersionsV1ChromeBrowserProfile]
    nextPageToken: str
    totalSize: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1ReportingData(
    typing_extensions.TypedDict, total=False
):
    browserExecutablePath: str
    extensionData: _list[GoogleChromeManagementVersionsV1ReportingDataExtensionData]
    extensionPolicyData: _list[
        GoogleChromeManagementVersionsV1ReportingDataExtensionPolicyData
    ]
    installedBrowserVersion: str
    policyData: _list[GoogleChromeManagementVersionsV1ReportingDataPolicyData]
    profilePath: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1ReportingDataConflictingPolicyData(
    typing_extensions.TypedDict, total=False
):
    source: typing_extensions.Literal[
        "POLICY_SOURCE_UNSPECIFIED",
        "MACHINE_PLATFORM",
        "USER_PLATFORM",
        "MACHINE_LEVEL_USER_CLOUD",
        "USER_CLOUD",
        "MACHINE_MERGED",
    ]

@typing.type_check_only
class GoogleChromeManagementVersionsV1ReportingDataExtensionData(
    typing_extensions.TypedDict, total=False
):
    description: str
    extensionId: str
    extensionType: typing_extensions.Literal[
        "EXTENSION_TYPE_UNSPECIFIED", "EXTENSION", "APP", "THEME", "HOSTED_APP"
    ]
    homepageUri: str
    installationType: typing_extensions.Literal[
        "INSTALLATION_TYPE_UNSPECIFIED",
        "MULTIPLE",
        "NORMAL",
        "ADMIN",
        "DEVELOPMENT",
        "SIDELOAD",
        "OTHER",
    ]
    isDisabled: bool
    isWebstoreExtension: bool
    manifestVersion: int
    name: str
    permissions: _list[str]
    version: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1ReportingDataExtensionPolicyData(
    typing_extensions.TypedDict, total=False
):
    extensionId: str
    extensionName: str
    policyData: _list[GoogleChromeManagementVersionsV1ReportingDataPolicyData]

@typing.type_check_only
class GoogleChromeManagementVersionsV1ReportingDataPolicyData(
    typing_extensions.TypedDict, total=False
):
    conflicts: _list[GoogleChromeManagementVersionsV1ReportingDataConflictingPolicyData]
    error: str
    name: str
    source: typing_extensions.Literal[
        "POLICY_SOURCE_UNSPECIFIED",
        "MACHINE_PLATFORM",
        "USER_PLATFORM",
        "MACHINE_LEVEL_USER_CLOUD",
        "USER_CLOUD",
        "MACHINE_MERGED",
    ]
    value: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1SignDataMetadata(
    typing_extensions.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1SignDataResponse(
    typing_extensions.TypedDict, total=False
):
    certificateProvisioningProcess: (
        GoogleChromeManagementVersionsV1CertificateProvisioningProcess
    )

@typing.type_check_only
class GoogleChromeManagementVersionsV1alpha1CertificateProvisioningProcess(
    typing_extensions.TypedDict, total=False
):
    caConnectionAdapterConfigReference: str
    chromeOsDevice: GoogleChromeManagementVersionsV1alpha1ChromeOsDevice
    chromeOsUserSession: GoogleChromeManagementVersionsV1alpha1ChromeOsUserSession
    failureMessage: str
    issuedCertificate: str
    name: str
    profileAdapterConfigReference: str
    provisioningProfileId: str
    signData: str
    signature: str
    signatureAlgorithm: typing_extensions.Literal[
        "SIGNATURE_ALGORITHM_UNSPECIFIED",
        "SIGNATURE_ALGORITHM_RSA_PKCS1_V1_5_SHA256",
        "SIGNATURE_ALGORITHM_ECDSA_SHA256",
    ]
    startTime: str
    subjectPublicKeyInfo: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1alpha1ChromeOsDevice(
    typing_extensions.TypedDict, total=False
):
    deviceDirectoryApiId: str
    serialNumber: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1alpha1ChromeOsUserSession(
    typing_extensions.TypedDict, total=False
):
    chromeOsDevice: GoogleChromeManagementVersionsV1alpha1ChromeOsDevice
    userDirectoryApiId: str
    userPrimaryEmail: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1alpha1SignDataMetadata(
    typing_extensions.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleChromeManagementVersionsV1alpha1SignDataResponse(
    typing_extensions.TypedDict, total=False
):
    certificateProvisioningProcess: (
        GoogleChromeManagementVersionsV1alpha1CertificateProvisioningProcess
    )

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int
