import typing

import typing_extensions

@typing.type_check_only
class GoogleChromeManagementV1AndroidAppInfo(typing_extensions.TypedDict, total=False):
    permissions: typing.List[GoogleChromeManagementV1AndroidAppPermission]

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
    permissions: typing.List[GoogleChromeManagementV1ChromeAppPermission]
    siteAccess: typing.List[GoogleChromeManagementV1ChromeAppSiteAccess]
    supportEnabled: bool

@typing.type_check_only
class GoogleChromeManagementV1ChromeAppPermission(
    typing_extensions.TypedDict, total=False
):
    accessUserData: bool
    documentationUri: str
    type: str

@typing.type_check_only
class GoogleChromeManagementV1ChromeAppSiteAccess(
    typing_extensions.TypedDict, total=False
):
    hostMatch: str

@typing.type_check_only
class GoogleChromeManagementV1CountChromeVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    browserVersions: typing.List[GoogleChromeManagementV1BrowserVersion]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleChromeManagementV1CountInstalledAppsResponse(
    typing_extensions.TypedDict, total=False
):
    installedApps: typing.List[GoogleChromeManagementV1InstalledApp]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GoogleChromeManagementV1Device(typing_extensions.TypedDict, total=False):
    deviceId: str
    machine: str

@typing.type_check_only
class GoogleChromeManagementV1FindInstalledAppDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: typing.List[GoogleChromeManagementV1Device]
    nextPageToken: str
    totalSize: int

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
    permissions: typing.List[str]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
