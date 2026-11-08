import typing

_list = list

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
class Empty(typing.TypedDict, total=False): ...

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
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str
