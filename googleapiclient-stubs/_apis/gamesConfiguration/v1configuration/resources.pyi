import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GamesConfigurationResource(googleapiclient.discovery.Resource):
    class AchievementConfigurationsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            applicationId: str,
            body: AchievementConfiguration = ...,
            **kwargs: typing.Any
        ) -> AchievementConfigurationHttpRequest: ...
        def get(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> AchievementConfigurationHttpRequest: ...
        def update(
            self,
            *,
            achievementId: str,
            body: AchievementConfiguration = ...,
            **kwargs: typing.Any
        ) -> AchievementConfigurationHttpRequest: ...
        def delete(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            applicationId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AchievementConfigurationListResponseHttpRequest: ...
    class ImageConfigurationsResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            resourceId: str,
            imageType: typing_extensions.Literal[
                "IMAGE_TYPE_UNSPECIFIED", "ACHIEVEMENT_ICON", "LEADERBOARD_ICON"
            ],
            **kwargs: typing.Any
        ) -> ImageConfigurationHttpRequest: ...
    class LeaderboardConfigurationsResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            leaderboardId: str,
            body: LeaderboardConfiguration = ...,
            **kwargs: typing.Any
        ) -> LeaderboardConfigurationHttpRequest: ...
        def delete(
            self, *, leaderboardId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            applicationId: str,
            body: LeaderboardConfiguration = ...,
            **kwargs: typing.Any
        ) -> LeaderboardConfigurationHttpRequest: ...
        def get(
            self, *, leaderboardId: str, **kwargs: typing.Any
        ) -> LeaderboardConfigurationHttpRequest: ...
        def list(
            self,
            *,
            applicationId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LeaderboardConfigurationListResponseHttpRequest: ...
    def achievementConfigurations(self) -> AchievementConfigurationsResource: ...
    def imageConfigurations(self) -> ImageConfigurationsResource: ...
    def leaderboardConfigurations(self) -> LeaderboardConfigurationsResource: ...

class LeaderboardConfigurationListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LeaderboardConfigurationListResponse: ...

class LeaderboardConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LeaderboardConfiguration: ...

class AchievementConfigurationListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementConfigurationListResponse: ...

class ImageConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImageConfiguration: ...

class AchievementConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AchievementConfiguration: ...
