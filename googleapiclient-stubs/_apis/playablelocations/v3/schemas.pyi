import typing

_list = list

@typing.type_check_only
class GoogleMapsPlayablelocationsV3Impression(typing.TypedDict, total=False):
    gameObjectType: int
    impressionType: typing.Literal[
        "IMPRESSION_TYPE_UNSPECIFIED", "PRESENTED", "INTERACTED"
    ]
    locationName: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogImpressionsRequest(typing.TypedDict, total=False):
    clientInfo: GoogleMapsUnityClientInfo
    impressions: _list[GoogleMapsPlayablelocationsV3Impression]
    requestId: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogImpressionsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogPlayerReportsRequest(
    typing.TypedDict, total=False
):
    clientInfo: GoogleMapsUnityClientInfo
    playerReports: _list[GoogleMapsPlayablelocationsV3PlayerReport]
    requestId: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogPlayerReportsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleMapsPlayablelocationsV3PlayerReport(typing.TypedDict, total=False):
    languageCode: str
    locationName: str
    reasonDetails: str
    reasons: _list[
        typing.Literal[
            "BAD_LOCATION_REASON_UNSPECIFIED",
            "OTHER",
            "NOT_PEDESTRIAN_ACCESSIBLE",
            "NOT_OPEN_TO_PUBLIC",
            "PERMANENTLY_CLOSED",
            "TEMPORARILY_INACCESSIBLE",
        ]
    ]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleAreaFilter(typing.TypedDict, total=False):
    s2CellId: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleCriterion(typing.TypedDict, total=False):
    fieldsToReturn: str
    filter: GoogleMapsPlayablelocationsV3SampleFilter
    gameObjectType: int

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleFilter(typing.TypedDict, total=False):
    includedTypes: _list[str]
    maxLocationCount: int
    spacing: GoogleMapsPlayablelocationsV3SampleSpacingOptions

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocation(
    typing.TypedDict, total=False
):
    centerPoint: GoogleTypeLatLng
    name: str
    placeId: str
    plusCode: str
    snappedPoint: GoogleTypeLatLng
    types: _list[str]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocationList(
    typing.TypedDict, total=False
):
    locations: _list[GoogleMapsPlayablelocationsV3SamplePlayableLocation]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest(
    typing.TypedDict, total=False
):
    areaFilter: GoogleMapsPlayablelocationsV3SampleAreaFilter
    criteria: _list[GoogleMapsPlayablelocationsV3SampleCriterion]

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse(
    typing.TypedDict, total=False
):
    locationsPerGameObjectType: dict[str, typing.Any]
    ttl: str

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SampleSpacingOptions(typing.TypedDict, total=False):
    minSpacingMeters: float
    pointType: typing.Literal["POINT_TYPE_UNSPECIFIED", "CENTER_POINT", "SNAPPED_POINT"]

@typing.type_check_only
class GoogleMapsUnityClientInfo(typing.TypedDict, total=False):
    apiClient: str
    applicationId: str
    applicationVersion: str
    deviceModel: str
    languageCode: str
    operatingSystem: str
    operatingSystemBuild: str
    platform: typing.Literal[
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
class GoogleTypeLatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float
