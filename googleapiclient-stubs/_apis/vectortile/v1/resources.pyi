import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

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
            alwaysIncludeBuildingFootprints: bool | None = ...,
            clientInfo_apiClient: str | None = ...,
            clientInfo_applicationId: str | None = ...,
            clientInfo_applicationVersion: str | None = ...,
            clientInfo_deviceModel: str | None = ...,
            clientInfo_operatingSystem: str | None = ...,
            clientInfo_platform: typing.Literal[
                "PLATFORM_UNSPECIFIED",
                "EDITOR",
                "MAC_OS",
                "WINDOWS",
                "LINUX",
                "ANDROID",
                "IOS",
                "WEB_GL",
            ]
            | None = ...,
            clientInfo_userId: str | None = ...,
            clientTileVersionId: str | None = ...,
            enableDetailedHighwayTypes: bool | None = ...,
            enableFeatureNames: bool | None = ...,
            enableModeledVolumes: bool | None = ...,
            enablePoliticalFeatures: bool | None = ...,
            enablePrivateRoads: bool | None = ...,
            enableUnclippedBuildings: bool | None = ...,
            languageCode: str | None = ...,
            regionCode: str | None = ...,
            **kwargs: typing.Any,
        ) -> FeatureTileHttpRequest: ...

    @typing.type_check_only
    class TerraintilesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            name: str,
            altitudePrecisionCentimeters: int | None = ...,
            clientInfo_apiClient: str | None = ...,
            clientInfo_applicationId: str | None = ...,
            clientInfo_applicationVersion: str | None = ...,
            clientInfo_deviceModel: str | None = ...,
            clientInfo_operatingSystem: str | None = ...,
            clientInfo_platform: typing.Literal[
                "PLATFORM_UNSPECIFIED",
                "EDITOR",
                "MAC_OS",
                "WINDOWS",
                "LINUX",
                "ANDROID",
                "IOS",
                "WEB_GL",
            ]
            | None = ...,
            clientInfo_userId: str | None = ...,
            maxElevationResolutionCells: int | None = ...,
            minElevationResolutionCells: int | None = ...,
            terrainFormats: typing.Literal[
                "TERRAIN_FORMAT_UNKNOWN", "FIRST_DERIVATIVE", "SECOND_DERIVATIVE"
            ]
            | _list[
                typing.Literal[
                    "TERRAIN_FORMAT_UNKNOWN", "FIRST_DERIVATIVE", "SECOND_DERIVATIVE"
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def featuretiles(self) -> FeaturetilesResource: ...
    def terraintiles(self) -> TerraintilesResource: ...

@typing.type_check_only
class FeatureTileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FeatureTile: ...

@typing.type_check_only
class TerrainTileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TerrainTile: ...
