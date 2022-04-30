import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class GamesConfigurationResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AchievementConfigurationsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, achievementId: str, **kwargs: typing.Any
        ) -> AchievementConfigurationHttpRequest: ...
        def insert(
            self,
            *,
            applicationId: str,
            body: AchievementConfiguration = ...,
            **kwargs: typing.Any
        ) -> AchievementConfigurationHttpRequest: ...
        def list(
            self,
            *,
            applicationId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AchievementConfigurationListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AchievementConfigurationListResponseHttpRequest,
            previous_response: AchievementConfigurationListResponse,
        ) -> AchievementConfigurationListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            achievementId: str,
            body: AchievementConfiguration = ...,
            **kwargs: typing.Any
        ) -> AchievementConfigurationHttpRequest: ...

    @typing.type_check_only
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

    @typing.type_check_only
    class LeaderboardConfigurationsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, leaderboardId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, leaderboardId: str, **kwargs: typing.Any
        ) -> LeaderboardConfigurationHttpRequest: ...
        def insert(
            self,
            *,
            applicationId: str,
            body: LeaderboardConfiguration = ...,
            **kwargs: typing.Any
        ) -> LeaderboardConfigurationHttpRequest: ...
        def list(
            self,
            *,
            applicationId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LeaderboardConfigurationListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: LeaderboardConfigurationListResponseHttpRequest,
            previous_response: LeaderboardConfigurationListResponse,
        ) -> LeaderboardConfigurationListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            leaderboardId: str,
            body: LeaderboardConfiguration = ...,
            **kwargs: typing.Any
        ) -> LeaderboardConfigurationHttpRequest: ...

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
    def achievementConfigurations(self) -> AchievementConfigurationsResource: ...
    def imageConfigurations(self) -> ImageConfigurationsResource: ...
    def leaderboardConfigurations(self) -> LeaderboardConfigurationsResource: ...

@typing.type_check_only
class AchievementConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementConfiguration: ...

@typing.type_check_only
class AchievementConfigurationListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AchievementConfigurationListResponse: ...

@typing.type_check_only
class ImageConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImageConfiguration: ...

@typing.type_check_only
class LeaderboardConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LeaderboardConfiguration: ...

@typing.type_check_only
class LeaderboardConfigurationListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LeaderboardConfigurationListResponse: ...
