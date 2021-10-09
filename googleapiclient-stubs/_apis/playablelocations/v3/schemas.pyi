import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleMapsPlayablelocationsV3Impression(typing_extensions.TypedDict, total=False):
    gameObjectType: int
    impressionType: typing_extensions.Literal[
        "IMPRESSION_TYPE_UNSPECIFIED", "PRESENTED", "INTERACTED"
    ]
    locationName: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogImpressionsRequest(
    typing_extensions.TypedDict, total=False
):
    clientInfo: GoogleMapsUnityClientInfo
    impressions: _list[GoogleMapsPlayablelocationsV3Impression]
    requestId: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogImpressionsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogPlayerReportsRequest(
    typing_extensions.TypedDict, total=False
):
    clientInfo: GoogleMapsUnityClientInfo
    playerReports: _list[GoogleMapsPlayablelocationsV3PlayerReport]
    requestId: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogPlayerReportsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleMapsPlayablelocationsV3PlayerReport(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    locationName: str
    reasonDetails: str
    reasons: _list[str]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleAreaFilter(
    typing_extensions.TypedDict, total=False
):
    s2CellId: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleCriterion(
    typing_extensions.TypedDict, total=False
):
    fieldsToReturn: str
    filter: GoogleMapsPlayablelocationsV3SampleFilter
    gameObjectType: int

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleFilter(
    typing_extensions.TypedDict, total=False
):
    includedTypes: _list[str]
    maxLocationCount: int
    spacing: GoogleMapsPlayablelocationsV3SampleSpacingOptions

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocation(
    typing_extensions.TypedDict, total=False
):
    centerPoint: GoogleTypeLatLng
    name: str
    placeId: str
    plusCode: str
    snappedPoint: GoogleTypeLatLng
    types: _list[str]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocationList(
    typing_extensions.TypedDict, total=False
):
    locations: _list[GoogleMapsPlayablelocationsV3SamplePlayableLocation]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest(
    typing_extensions.TypedDict, total=False
):
    areaFilter: GoogleMapsPlayablelocationsV3SampleAreaFilter
    criteria: _list[GoogleMapsPlayablelocationsV3SampleCriterion]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locationsPerGameObjectType: dict[str, typing.Any]
    ttl: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleSpacingOptions(
    typing_extensions.TypedDict, total=False
):
    minSpacingMeters: float
    pointType: typing_extensions.Literal[
        "POINT_TYPE_UNSPECIFIED", "CENTER_POINT", "SNAPPED_POINT"
    ]

@typing.type_check_only
class GoogleMapsUnityClientInfo(typing_extensions.TypedDict, total=False):
    apiClient: str
    applicationId: str
    applicationVersion: str
    deviceModel: str
    languageCode: str
    operatingSystem: str
    operatingSystemBuild: str
    platform: typing_extensions.Literal[
        "PLATFORM_UNSPECIFIED",
        "EDITOR",
        "MAC_OS",
        "WINDOWS",
        "LINUX",
        "ANDROID",
        "IOS",
        "WEB_GL",
    ]

@typing.type_check_only
class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float
