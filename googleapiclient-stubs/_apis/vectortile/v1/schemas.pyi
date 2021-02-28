import typing

import typing_extensions
@typing.type_check_only
class Area(typing_extensions.TypedDict, total=False):
    basemapZOrder: BasemapZOrder
    hasExternalEdges: bool
    internalEdges: typing.List[int]
    loopBreaks: typing.List[int]
    triangleIndices: typing.List[int]
    type: typing_extensions.Literal[
        "TRIANGLE_FAN", "INDEXED_TRIANGLES", "TRIANGLE_STRIP"
    ]
    vertexOffsets: Vertex2DList
    zOrder: int

@typing.type_check_only
class BasemapZOrder(typing_extensions.TypedDict, total=False):
    zGrade: int
    zPlane: int
    zWithinGrade: int

@typing.type_check_only
class ExtrudedArea(typing_extensions.TypedDict, total=False):
    area: Area
    maxZ: int
    minZ: int

@typing.type_check_only
class Feature(typing_extensions.TypedDict, total=False):
    displayName: str
    geometry: Geometry
    placeId: str
    relations: typing.List[Relation]
    segmentInfo: SegmentInfo
    type: typing_extensions.Literal[
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
class FeatureTile(typing_extensions.TypedDict, total=False):
    coordinates: TileCoordinates
    features: typing.List[Feature]
    name: str
    providers: typing.List[ProviderInfo]
    status: typing_extensions.Literal["STATUS_OK", "STATUS_OK_DATA_UNCHANGED"]
    versionId: str

@typing.type_check_only
class FirstDerivativeElevationGrid(typing_extensions.TypedDict, total=False):
    altitudeMultiplier: float
    rows: typing.List[Row]

@typing.type_check_only
class Geometry(typing_extensions.TypedDict, total=False):
    areas: typing.List[Area]
    extrudedAreas: typing.List[ExtrudedArea]
    lines: typing.List[Line]
    modeledVolumes: typing.List[ModeledVolume]

@typing.type_check_only
class Line(typing_extensions.TypedDict, total=False):
    basemapZOrder: BasemapZOrder
    vertexOffsets: Vertex2DList
    zOrder: int

@typing.type_check_only
class ModeledVolume(typing_extensions.TypedDict, total=False):
    strips: typing.List[TriangleStrip]
    vertexOffsets: Vertex3DList

@typing.type_check_only
class ProviderInfo(typing_extensions.TypedDict, total=False):
    description: str

@typing.type_check_only
class Relation(typing_extensions.TypedDict, total=False):
    relatedFeatureIndex: int
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "OCCUPIES", "PRIMARILY_OCCUPIED_BY"
    ]

@typing.type_check_only
class RoadInfo(typing_extensions.TypedDict, total=False):
    isPrivate: bool

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    altitudeDiffs: typing.List[int]

@typing.type_check_only
class SecondDerivativeElevationGrid(typing_extensions.TypedDict, total=False):
    altitudeMultiplier: float
    columnCount: int
    encodedData: str
    rowCount: int

@typing.type_check_only
class SegmentInfo(typing_extensions.TypedDict, total=False):
    roadInfo: RoadInfo

@typing.type_check_only
class TerrainTile(typing_extensions.TypedDict, total=False):
    coordinates: TileCoordinates
    firstDerivative: FirstDerivativeElevationGrid
    name: str
    secondDerivative: SecondDerivativeElevationGrid

@typing.type_check_only
class TileCoordinates(typing_extensions.TypedDict, total=False):
    x: int
    y: int
    zoom: int

@typing.type_check_only
class TriangleStrip(typing_extensions.TypedDict, total=False):
    vertexIndices: typing.List[int]

@typing.type_check_only
class Vertex2DList(typing_extensions.TypedDict, total=False):
    xOffsets: typing.List[int]
    yOffsets: typing.List[int]

@typing.type_check_only
class Vertex3DList(typing_extensions.TypedDict, total=False):
    xOffsets: typing.List[int]
    yOffsets: typing.List[int]
    zOffsets: typing.List[int]
