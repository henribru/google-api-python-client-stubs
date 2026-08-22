import typing

_list = list

@typing.type_check_only
class Color(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DayInfo(typing.TypedDict, total=False):
    date: Date
    plantInfo: _list[PlantInfo]
    pollenTypeInfo: _list[PollenTypeInfo]

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class IndexInfo(typing.TypedDict, total=False):
    category: str
    code: typing.Literal["INDEX_UNSPECIFIED", "UPI"]
    color: Color
    displayName: str
    indexDescription: str
    value: int

@typing.type_check_only
class LookupForecastResponse(typing.TypedDict, total=False):
    dailyInfo: _list[DayInfo]
    nextPageToken: str
    regionCode: str

@typing.type_check_only
class PlantDescription(typing.TypedDict, total=False):
    crossReaction: str
    family: str
    picture: str
    pictureCloseup: str
    season: str
    specialColors: str
    specialShapes: str
    type: typing.Literal["POLLEN_TYPE_UNSPECIFIED", "GRASS", "TREE", "WEED"]

@typing.type_check_only
class PlantInfo(typing.TypedDict, total=False):
    code: typing.Literal[
        "PLANT_UNSPECIFIED",
        "ALDER",
        "ASH",
        "BIRCH",
        "COTTONWOOD",
        "ELM",
        "MAPLE",
        "OLIVE",
        "JUNIPER",
        "OAK",
        "PINE",
        "CYPRESS_PINE",
        "HAZEL",
        "GRAMINALES",
        "RAGWEED",
        "MUGWORT",
        "JAPANESE_CEDAR",
        "JAPANESE_CYPRESS",
    ]
    displayName: str
    inSeason: bool
    indexInfo: IndexInfo
    plantDescription: PlantDescription

@typing.type_check_only
class PollenTypeInfo(typing.TypedDict, total=False):
    code: typing.Literal["POLLEN_TYPE_UNSPECIFIED", "GRASS", "TREE", "WEED"]
    displayName: str
    healthRecommendations: _list[str]
    inSeason: bool
    indexInfo: IndexInfo
