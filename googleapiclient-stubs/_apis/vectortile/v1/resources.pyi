import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SemanticTileResource(googleapiclient.discovery.Resource):
    class TerraintilesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            name: str,
            clientInfo_platform: typing_extensions.Literal[
                "PLATFORM_UNSPECIFIED",
                "EDITOR",
                "MAC_OS",
                "WINDOWS",
                "LINUX",
                "ANDROID",
                "IOS",
                "WEB_GL",
            ] = ...,
            minElevationResolutionCells: int = ...,
            clientInfo_applicationVersion: str = ...,
            clientInfo_applicationId: str = ...,
            clientInfo_deviceModel: str = ...,
            clientInfo_operatingSystem: str = ...,
            maxElevationResolutionCells: int = ...,
            clientInfo_userId: str = ...,
            clientInfo_apiClient: str = ...,
            terrainFormats: typing.Union[
                typing_extensions.Literal[
                    "TERRAIN_FORMAT_UNKNOWN", "FIRST_DERIVATIVE", "SECOND_DERIVATIVE"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "TERRAIN_FORMAT_UNKNOWN",
                        "FIRST_DERIVATIVE",
                        "SECOND_DERIVATIVE",
                    ]
                ],
            ] = ...,
            altitudePrecisionCentimeters: int = ...,
            **kwargs: typing.Any
        ) -> TerrainTileHttpRequest: ...
    class FeaturetilesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            name: str,
            clientInfo_operatingSystem: str = ...,
            enableModeledVolumes: bool = ...,
            enablePrivateRoads: bool = ...,
            clientInfo_applicationVersion: str = ...,
            languageCode: str = ...,
            enableFeatureNames: bool = ...,
            clientInfo_userId: str = ...,
            regionCode: str = ...,
            clientInfo_deviceModel: str = ...,
            clientInfo_apiClient: str = ...,
            enablePoliticalFeatures: bool = ...,
            clientInfo_platform: typing_extensions.Literal[
                "PLATFORM_UNSPECIFIED",
                "EDITOR",
                "MAC_OS",
                "WINDOWS",
                "LINUX",
                "ANDROID",
                "IOS",
                "WEB_GL",
            ] = ...,
            enableUnclippedBuildings: bool = ...,
            clientInfo_applicationId: str = ...,
            clientTileVersionId: str = ...,
            enableDetailedHighwayTypes: bool = ...,
            **kwargs: typing.Any
        ) -> FeatureTileHttpRequest: ...
    def terraintiles(self) -> TerraintilesResource: ...
    def featuretiles(self) -> FeaturetilesResource: ...

class FeatureTileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FeatureTile: ...

class TerrainTileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TerrainTile: ...
