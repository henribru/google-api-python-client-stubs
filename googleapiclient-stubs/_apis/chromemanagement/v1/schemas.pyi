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
class GoogleChromeManagementV1BrowserVersion(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "RELEASE_CHANNEL_UNSPECIFIED", "CANARY", "DEV", "BETA", "STABLE"
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
    isTheme: bool
    minUserCount: int
    permissions: _list[GoogleChromeManagementV1ChromeAppPermission]
    siteAccess: _list[GoogleChromeManagementV1ChromeAppSiteAccess]
    supportEnabled: bool

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
class GoogleChromeManagementV1CpuInfo(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X64"]
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
class GoogleChromeManagementV1DisplayInfo(typing_extensions.TypedDict, total=False):
    deviceId: str
    isInternal: bool
    refreshRate: int
    resolutionHeight: int
    resolutionWidth: int

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

@typing.type_check_only
class GoogleChromeManagementV1GraphicsStatusReport(
    typing_extensions.TypedDict, total=False
):
    displays: _list[GoogleChromeManagementV1DisplayInfo]
    reportTime: str

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

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: _list[GoogleChromeManagementV1TelemetryDevice]
    nextPageToken: str

@typing.type_check_only
class GoogleChromeManagementV1MemoryInfo(typing_extensions.TypedDict, total=False):
    availableRamBytes: str
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
class GoogleChromeManagementV1NetworkStatusReport(
    typing_extensions.TypedDict, total=False
):
    gatewayIpAddress: str
    lanIpAddress: str
    reportTime: str
    sampleFrequency: str
    signalStrengthDbm: int

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
class GoogleChromeManagementV1TelemetryDevice(typing_extensions.TypedDict, total=False):
    batteryInfo: _list[GoogleChromeManagementV1BatteryInfo]
    batteryStatusReport: _list[GoogleChromeManagementV1BatteryStatusReport]
    cpuInfo: _list[GoogleChromeManagementV1CpuInfo]
    cpuStatusReport: _list[GoogleChromeManagementV1CpuStatusReport]
    customer: str
    deviceId: str
    graphicsInfo: GoogleChromeManagementV1GraphicsInfo
    graphicsStatusReport: _list[GoogleChromeManagementV1GraphicsStatusReport]
    memoryInfo: GoogleChromeManagementV1MemoryInfo
    memoryStatusReport: _list[GoogleChromeManagementV1MemoryStatusReport]
    name: str
    networkStatusReport: _list[GoogleChromeManagementV1NetworkStatusReport]
    orgUnitId: str
    osUpdateStatus: _list[GoogleChromeManagementV1OsUpdateStatus]
    serialNumber: str
    storageInfo: GoogleChromeManagementV1StorageInfo
    storageStatusReport: _list[GoogleChromeManagementV1StorageStatusReport]

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
