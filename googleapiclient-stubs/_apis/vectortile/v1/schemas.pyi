import typing

import typing_extensions

class SegmentInfo(typing_extensions.TypedDict, total=False):
    roadInfo: RoadInfo

class Line(typing_extensions.TypedDict, total=False):
    zOrder: int
    vertexOffsets: Vertex2DList

class ExtrudedArea(typing_extensions.TypedDict, total=False):
    minZ: int
    area: Area
    maxZ: int

class TileCoordinates(typing_extensions.TypedDict, total=False):
    zoom: int
    y: int
    x: int

class ModeledVolume(typing_extensions.TypedDict, total=False):
    strips: typing.List[TriangleStrip]
    vertexOffsets: Vertex3DList

class ProviderInfo(typing_extensions.TypedDict, total=False):
    description: str

class Feature(typing_extensions.TypedDict, total=False):
    placeId: str
    relations: typing.List[Relation]
    displayName: str
    segmentInfo: SegmentInfo
    geometry: Geometry
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

class TriangleStrip(typing_extensions.TypedDict, total=False):
    vertexIndices: typing.List[int]

class Row(typing_extensions.TypedDict, total=False):
    altitudeDiffs: typing.List[int]

class Geometry(typing_extensions.TypedDict, total=False):
    lines: typing.List[Line]
    modeledVolumes: typing.List[ModeledVolume]
    extrudedAreas: typing.List[ExtrudedArea]
    areas: typing.List[Area]

class Area(typing_extensions.TypedDict, total=False):
    loopBreaks: typing.List[int]
    internalEdges: typing.List[int]
    type: typing_extensions.Literal[
        "TRIANGLE_FAN", "INDEXED_TRIANGLES", "TRIANGLE_STRIP"
    ]
    triangleIndices: typing.List[int]
    zOrder: int
    hasExternalEdges: bool
    vertexOffsets: Vertex2DList

class FeatureTile(typing_extensions.TypedDict, total=False):
    features: typing.List[Feature]
    name: str
    versionId: str
    coordinates: TileCoordinates
    providers: typing.List[ProviderInfo]
    status: typing_extensions.Literal["STATUS_OK", "STATUS_OK_DATA_UNCHANGED"]

class Vertex2DList(typing_extensions.TypedDict, total=False):
    xOffsets: typing.List[int]
    yOffsets: typing.List[int]

class FirstDerivativeElevationGrid(typing_extensions.TypedDict, total=False):
    altitudeMultiplier: float
    rows: typing.List[Row]

class Relation(typing_extensions.TypedDict, total=False):
    relatedFeatureIndex: int
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "OCCUPIES", "PRIMARILY_OCCUPIED_BY"
    ]

class TerrainTile(typing_extensions.TypedDict, total=False):
    coordinates: TileCoordinates
    firstDerivative: FirstDerivativeElevationGrid
    name: str
    secondDerivative: SecondDerivativeElevationGrid

class RoadInfo(typing_extensions.TypedDict, total=False):
    isPrivate: bool

class SecondDerivativeElevationGrid(typing_extensions.TypedDict, total=False):
    rowCount: int
    encodedData: str
    altitudeMultiplier: float
    columnCount: int

class Vertex3DList(typing_extensions.TypedDict, total=False):
    zOffsets: typing.List[int]
    yOffsets: typing.List[int]
    xOffsets: typing.List[int]
