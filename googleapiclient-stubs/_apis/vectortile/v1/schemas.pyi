import typing

_list = list

@typing.type_check_only
class Area(typing.TypedDict, total=False):
    basemapZOrder: BasemapZOrder
    hasExternalEdges: bool
    internalEdges: _list[int]
    loopBreaks: _list[int]
    triangleIndices: _list[int]
    type: typing.Literal["TRIANGLE_FAN", "INDEXED_TRIANGLES", "TRIANGLE_STRIP"]
    vertexOffsets: Vertex2DList
    zOrder: int

@typing.type_check_only
class BasemapZOrder(typing.TypedDict, total=False):
    zGrade: int
    zPlane: int
    zWithinGrade: int

@typing.type_check_only
class ExtrudedArea(typing.TypedDict, total=False):
    area: Area
    maxZ: int
    minZ: int

@typing.type_check_only
class Feature(typing.TypedDict, total=False):
    displayName: str
    geometry: Geometry
    placeId: str
    relations: _list[Relation]
    segmentInfo: SegmentInfo
    type: typing.Literal[
        "FEATURE_TYPE_UNSPECIFIED",
        "STRUCTURE",
        "BAR",
        "BANK",
        "LODGING",
        "CAFE",
        "RESTAURANT",
        "EVENT_VENUE",
        "TOURIST_DESTINATION",
        "SHOPPING",
        "SCHOOL",
        "SEGMENT",
        "ROAD",
        "LOCAL_ROAD",
        "ARTERIAL_ROAD",
        "HIGHWAY",
        "CONTROLLED_ACCESS_HIGHWAY",
        "FOOTPATH",
        "RAIL",
        "FERRY",
        "REGION",
        "PARK",
        "BEACH",
        "FOREST",
        "POLITICAL",
        "ADMINISTRATIVE_AREA1",
        "LOCALITY",
        "SUBLOCALITY",
        "WATER",
    ]

@typing.type_check_only
class FeatureTile(typing.TypedDict, total=False):
    coordinates: TileCoordinates
    features: _list[Feature]
    name: str
    providers: _list[ProviderInfo]
    status: typing.Literal["STATUS_OK", "STATUS_OK_DATA_UNCHANGED"]
    versionId: str

@typing.type_check_only
class FirstDerivativeElevationGrid(typing.TypedDict, total=False):
    altitudeMultiplier: float
    rows: _list[Row]

@typing.type_check_only
class Geometry(typing.TypedDict, total=False):
    areas: _list[Area]
    extrudedAreas: _list[ExtrudedArea]
    lines: _list[Line]
    modeledVolumes: _list[ModeledVolume]

@typing.type_check_only
class Line(typing.TypedDict, total=False):
    basemapZOrder: BasemapZOrder
    vertexOffsets: Vertex2DList
    zOrder: int

@typing.type_check_only
class ModeledVolume(typing.TypedDict, total=False):
    strips: _list[TriangleStrip]
    vertexOffsets: Vertex3DList

@typing.type_check_only
class ProviderInfo(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class Relation(typing.TypedDict, total=False):
    relatedFeatureIndex: int
    relationType: typing.Literal[
        "RELATION_TYPE_UNSPECIFIED", "OCCUPIES", "PRIMARILY_OCCUPIED_BY"
    ]

@typing.type_check_only
class RoadInfo(typing.TypedDict, total=False):
    isPrivate: bool

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    altitudeDiffs: _list[int]

@typing.type_check_only
class SecondDerivativeElevationGrid(typing.TypedDict, total=False):
    altitudeMultiplier: float
    columnCount: int
    encodedData: str
    rowCount: int

@typing.type_check_only
class SegmentInfo(typing.TypedDict, total=False):
    roadInfo: RoadInfo

@typing.type_check_only
class TerrainTile(typing.TypedDict, total=False):
    coordinates: TileCoordinates
    firstDerivative: FirstDerivativeElevationGrid
    name: str
    secondDerivative: SecondDerivativeElevationGrid

@typing.type_check_only
class TileCoordinates(typing.TypedDict, total=False):
    x: int
    y: int
    zoom: int

@typing.type_check_only
class TriangleStrip(typing.TypedDict, total=False):
    vertexIndices: _list[int]

@typing.type_check_only
class Vertex2DList(typing.TypedDict, total=False):
    xOffsets: _list[int]
    yOffsets: _list[int]

@typing.type_check_only
class Vertex3DList(typing.TypedDict, total=False):
    xOffsets: _list[int]
    yOffsets: _list[int]
    zOffsets: _list[int]
