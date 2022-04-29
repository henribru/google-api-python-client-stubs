import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SemanticTileResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FeaturetilesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            name: str,
            alwaysIncludeBuildingFootprints: bool = ...,
            clientInfo_apiClient: str = ...,
            clientInfo_applicationId: str = ...,
            clientInfo_applicationVersion: str = ...,
            clientInfo_deviceModel: str = ...,
            clientInfo_operatingSystem: str = ...,
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
            clientInfo_userId: str = ...,
            clientTileVersionId: str = ...,
            enableDetailedHighwayTypes: bool = ...,
            enableFeatureNames: bool = ...,
            enableModeledVolumes: bool = ...,
            enablePoliticalFeatures: bool = ...,
            enablePrivateRoads: bool = ...,
            enableUnclippedBuildings: bool = ...,
            languageCode: str = ...,
            regionCode: str = ...,
            **kwargs: typing.Any
        ) -> FeatureTileHttpRequest: ...

    @typing.type_check_only
    class TerraintilesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            name: str,
            altitudePrecisionCentimeters: int = ...,
            clientInfo_apiClient: str = ...,
            clientInfo_applicationId: str = ...,
            clientInfo_applicationVersion: str = ...,
            clientInfo_deviceModel: str = ...,
            clientInfo_operatingSystem: str = ...,
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
            clientInfo_userId: str = ...,
            maxElevationResolutionCells: int = ...,
            minElevationResolutionCells: int = ...,
            terrainFormats: typing_extensions.Literal[
                "TERRAIN_FORMAT_UNKNOWN", "FIRST_DERIVATIVE", "SECOND_DERIVATIVE"
            ]
            | _list[
                typing_extensions.Literal[
                    "TERRAIN_FORMAT_UNKNOWN", "FIRST_DERIVATIVE", "SECOND_DERIVATIVE"
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> TerrainTileHttpRequest: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def featuretiles(self) -> FeaturetilesResource: ...
    def terraintiles(self) -> TerraintilesResource: ...

@typing.type_check_only
class FeatureTileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FeatureTile: ...

@typing.type_check_only
class TerrainTileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TerrainTile: ...
