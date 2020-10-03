import typing

import typing_extensions

class GoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest(
    typing_extensions.TypedDict, total=False
):
    areaFilter: GoogleMapsPlayablelocationsV3SampleAreaFilter
    criteria: typing.List[GoogleMapsPlayablelocationsV3SampleCriterion]

class GoogleMapsPlayablelocationsV3PlayerReport(
    typing_extensions.TypedDict, total=False
):
    locationName: str
    reasons: typing.List[str]
    reasonDetails: str
    languageCode: str

class GoogleMapsPlayablelocationsV3SamplePlayableLocation(
    typing_extensions.TypedDict, total=False
):
    types: typing.List[str]
    placeId: str
    snappedPoint: GoogleTypeLatLng
    centerPoint: GoogleTypeLatLng
    plusCode: str
    name: str

class GoogleMapsPlayablelocationsV3SampleFilter(
    typing_extensions.TypedDict, total=False
):
    includedTypes: typing.List[str]
    spacing: GoogleMapsPlayablelocationsV3SampleSpacingOptions
    maxLocationCount: int

class GoogleMapsPlayablelocationsV3SamplePlayableLocationList(
    typing_extensions.TypedDict, total=False
):
    locations: typing.List[GoogleMapsPlayablelocationsV3SamplePlayableLocation]

class GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locationsPerGameObjectType: typing.Dict[str, typing.Any]
    ttl: str

class GoogleMapsPlayablelocationsV3Impression(typing_extensions.TypedDict, total=False):
    impressionType: typing_extensions.Literal[
        "IMPRESSION_TYPE_UNSPECIFIED", "PRESENTED", "INTERACTED"
    ]
    locationName: str
    gameObjectType: int

class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleMapsPlayablelocationsV3LogPlayerReportsResponse(
    typing_extensions.TypedDict, total=False
): ...

class GoogleMapsPlayablelocationsV3LogImpressionsRequest(
    typing_extensions.TypedDict, total=False
):
    clientInfo: GoogleMapsUnityClientInfo
    requestId: str
    impressions: typing.List[GoogleMapsPlayablelocationsV3Impression]

class GoogleMapsUnityClientInfo(typing_extensions.TypedDict, total=False):
    applicationId: str
    apiClient: str
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
    operatingSystemBuild: str
    languageCode: str
    applicationVersion: str
    deviceModel: str
    operatingSystem: str

class GoogleMapsPlayablelocationsV3SampleSpacingOptions(
    typing_extensions.TypedDict, total=False
):
    pointType: typing_extensions.Literal[
        "POINT_TYPE_UNSPECIFIED", "CENTER_POINT", "SNAPPED_POINT"
    ]
    minSpacingMeters: float

class GoogleMapsPlayablelocationsV3SampleCriterion(
    typing_extensions.TypedDict, total=False
):
    fieldsToReturn: str
    gameObjectType: int
    filter: GoogleMapsPlayablelocationsV3SampleFilter

class GoogleMapsPlayablelocationsV3SampleAreaFilter(
    typing_extensions.TypedDict, total=False
):
    s2CellId: str

class GoogleMapsPlayablelocationsV3LogPlayerReportsRequest(
    typing_extensions.TypedDict, total=False
):
    playerReports: typing.List[GoogleMapsPlayablelocationsV3PlayerReport]
    clientInfo: GoogleMapsUnityClientInfo
    requestId: str

class GoogleMapsPlayablelocationsV3LogImpressionsResponse(
    typing_extensions.TypedDict, total=False
): ...
