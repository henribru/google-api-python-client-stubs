import typing

import typing_extensions

_list = list

@typing.type_check_only
class Circle(typing_extensions.TypedDict, total=False):
    latLng: LatLng
    place: str
    radius: int

@typing.type_check_only
class ComputeInsightsRequest(typing_extensions.TypedDict, total=False):
    filter: Filter
    insights: _list[
        typing_extensions.Literal[
            "INSIGHT_UNSPECIFIED", "INSIGHT_COUNT", "INSIGHT_PLACES"
        ]
    ]

@typing.type_check_only
class ComputeInsightsResponse(typing_extensions.TypedDict, total=False):
    count: str
    placeInsights: _list[PlaceInsight]

@typing.type_check_only
class CustomArea(typing_extensions.TypedDict, total=False):
    polygon: Polygon

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    locationFilter: LocationFilter
    operatingStatus: _list[
        typing_extensions.Literal[
            "OPERATING_STATUS_UNSPECIFIED",
            "OPERATING_STATUS_OPERATIONAL",
            "OPERATING_STATUS_PERMANENTLY_CLOSED",
            "OPERATING_STATUS_TEMPORARILY_CLOSED",
        ]
    ]
    priceLevels: _list[
        typing_extensions.Literal[
            "PRICE_LEVEL_UNSPECIFIED",
            "PRICE_LEVEL_FREE",
            "PRICE_LEVEL_INEXPENSIVE",
            "PRICE_LEVEL_MODERATE",
            "PRICE_LEVEL_EXPENSIVE",
            "PRICE_LEVEL_VERY_EXPENSIVE",
        ]
    ]
    ratingFilter: RatingFilter
    typeFilter: TypeFilter

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LocationFilter(typing_extensions.TypedDict, total=False):
    circle: Circle
    customArea: CustomArea
    region: Region

@typing.type_check_only
class PlaceInsight(typing_extensions.TypedDict, total=False):
    place: str

@typing.type_check_only
class Polygon(typing_extensions.TypedDict, total=False):
    coordinates: _list[LatLng]

@typing.type_check_only
class RatingFilter(typing_extensions.TypedDict, total=False):
    maxRating: float
    minRating: float

@typing.type_check_only
class Region(typing_extensions.TypedDict, total=False):
    place: str

@typing.type_check_only
class TypeFilter(typing_extensions.TypedDict, total=False):
    excludedPrimaryTypes: _list[str]
    excludedTypes: _list[str]
    includedPrimaryTypes: _list[str]
    includedTypes: _list[str]
